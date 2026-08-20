"""Reproducible generation evaluation and manual-annotation utilities."""

from __future__ import annotations

import json
import statistics
import time
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Sequence

from app.config import (
    EMBEDDING_MODEL_NAME,
    GENERATION_CONTEXT_TOP_K,
    PROJECT_ROOT,
    QDRANT_COLLECTION_NAME,
    QDRANT_PATH,
    RERANKER_MODEL_NAME,
)
from app.evaluation.runner import (
    CHUNK_OVERLAP,
    CHUNK_SIZE,
    build_corpus_inventory,
    load_dataset,
    validate_dataset,
)
from app.generation.llm_client import OpenAICompatibleLLMClient
from app.generation.rag import GeneratedAnswer, RAGPipeline
from app.retrieval.bm25 import BM25Retriever, TOKENIZER_DESCRIPTION
from app.retrieval.dense import DenseRetriever
from app.retrieval.embedder import SentenceTransformerEmbedder
from app.retrieval.hybrid import (
    BM25_CANDIDATE_DEPTH,
    DENSE_CANDIDATE_DEPTH,
    RRF_K,
    HybridRetriever,
)
from app.retrieval.reranker import (
    RERANKER_CANDIDATE_DEPTH,
    CrossEncoderReranker,
    RerankedRetriever,
)
from app.retrieval.vector_store import QdrantVectorStore

GENERATION_STRATEGIES = ("dense", "hybrid", "reranked")
ANNOTATION_METRICS = (
    "answer_correctness",
    "faithfulness",
    "citation_correctness",
)
ABSTENTION_OUTCOMES = {
    "abstained_correctly",
    "answered_unsupported",
    "partially_hedged",
}
CITATION_COVERAGE_LEVELS = {"complete", "partial", "not_applicable"}


def _write_json_atomic(path: Path, payload: Any) -> None:
    """Write JSON through a sibling temporary file to preserve valid partial output."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(f"{path.suffix}.tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def load_generation_output(path: Path) -> dict[str, Any]:
    """Load one generation result file."""
    with Path(path).open(encoding="utf-8") as input_file:
        payload = json.load(input_file)
    if not isinstance(payload, dict) or not isinstance(payload.get("results"), list):
        raise ValueError(f"Invalid generation output: {path}")
    return payload


def _result_score(result: Any) -> tuple[float, dict[str, Any]]:
    if hasattr(result, "reranker_score"):
        return float(result.reranker_score), {
            "reranker_score": float(result.reranker_score),
            "hybrid_rank": int(result.hybrid_rank),
            "hybrid_rrf_score": float(result.hybrid_rrf_score),
        }
    return float(result.score), {"score": float(result.score)}


def serialize_generated_answer(
    item: dict[str, Any],
    strategy: str,
    generated: GeneratedAnswer,
    latency_ms: float,
) -> dict[str, Any]:
    """Serialize one successful generated answer without altering its content."""
    retrieved_chunks = []
    for rank, (context, result) in enumerate(
        zip(generated.contexts, generated.retrieved_chunks),
        start=1,
    ):
        score, score_fields = _result_score(result)
        retrieved_chunks.append(
            {
                "label": context.label,
                "rank": rank,
                "chunk_id": context.chunk.id,
                "document_id": context.chunk.document_id,
                "source": Path(context.chunk.source).name,
                "chunk_index": context.chunk.chunk_index,
                "score": score,
                **score_fields,
                "text": context.chunk.text,
            }
        )
    return {
        "question_id": item["id"],
        "difficulty": item.get("difficulty", "unsupported"),
        "question": item["question"],
        "reference_answer": item.get("reference_answer"),
        "strategy": strategy,
        "status": "completed",
        "retrieved_chunks": retrieved_chunks,
        "generated_answer": generated.answer,
        "answer_characters": len(generated.answer),
        "citations": [
            {
                "label": citation.label,
                "chunk_id": citation.chunk_id,
                "document_id": citation.document_id,
                "source": Path(citation.source).name,
                "chunk_index": citation.chunk_index,
            }
            for citation in generated.citations
        ],
        "invalid_citation_labels": list(generated.invalid_citation_labels),
        "latency_ms": latency_ms,
        "error": None,
    }


def run_questions(
    items: Sequence[dict[str, Any]],
    strategy: str,
    pipeline: RAGPipeline,
    output_path: Path,
    configuration: dict[str, Any],
    *,
    resume: bool = False,
    overwrite: bool = False,
) -> dict[str, Any]:
    """Generate answers, persist after every item, and safely resume completed work."""
    if strategy not in GENERATION_STRATEGIES:
        raise ValueError(f"Unsupported generation strategy: {strategy}")
    if resume and overwrite:
        raise ValueError("resume and overwrite cannot be used together")
    if output_path.exists() and not (resume or overwrite):
        raise ValueError(
            f"Output already exists: {output_path}; use --resume or --overwrite"
        )

    payload: dict[str, Any] = {
        "strategy": strategy,
        "configuration": configuration,
        "results": [],
    }
    if output_path.exists() and resume:
        payload = load_generation_output(output_path)
        if payload.get("strategy") != strategy:
            raise ValueError("Existing output strategy does not match requested strategy")

    existing = {
        result.get("question_id"): result
        for result in payload["results"]
        if isinstance(result, dict) and isinstance(result.get("question_id"), str)
    }
    ordered_results: list[dict[str, Any]] = []
    for item in items:
        question_id = item["id"]
        previous = existing.get(question_id)
        if previous is not None and previous.get("status") == "completed" and resume:
            ordered_results.append(previous)
            continue

        started = time.perf_counter()
        try:
            generated = pipeline.answer(item["question"])
            latency_ms = (time.perf_counter() - started) * 1000
            result = serialize_generated_answer(
                item,
                strategy,
                generated,
                latency_ms,
            )
        except Exception as error:
            latency_ms = (time.perf_counter() - started) * 1000
            result = {
                "question_id": question_id,
                "difficulty": item.get("difficulty", "unsupported"),
                "question": item["question"],
                "reference_answer": item.get("reference_answer"),
                "strategy": strategy,
                "status": "error",
                "retrieved_chunks": [],
                "generated_answer": None,
                "answer_characters": 0,
                "citations": [],
                "invalid_citation_labels": [],
                "latency_ms": latency_ms,
                "error": f"{type(error).__name__}: {error}",
            }
        ordered_results.append(result)
        print(
            f"[{strategy}] {question_id} {result['status']} "
            f"{len(ordered_results)}/{len(items)} latency_ms={latency_ms:.1f}",
            flush=True,
        )
        payload["results"] = ordered_results + [
            existing[remaining["id"]]
            for remaining in items[len(ordered_results) :]
            if remaining["id"] in existing
        ]
        _write_json_atomic(output_path, payload)

    payload["results"] = ordered_results
    _write_json_atomic(output_path, payload)
    return payload


def build_generation_runtime(
    strategy: str,
    *,
    corpus_path: Path = PROJECT_ROOT / "data" / "raw",
) -> tuple[RAGPipeline, QdrantVectorStore, dict[str, Any]]:
    """Build one frozen retrieval strategy and the existing generation pipeline."""
    if strategy not in GENERATION_STRATEGIES:
        raise ValueError(f"Unsupported generation strategy: {strategy}")
    documents, chunks = build_corpus_inventory(corpus_path)
    vector_store = QdrantVectorStore()
    if not vector_store.collection_exists():
        vector_store.close()
        raise ValueError("Dense Qdrant collection does not exist; rebuild the index")
    if vector_store.count() != len(chunks):
        indexed = vector_store.count()
        vector_store.close()
        raise ValueError(
            f"Qdrant has {indexed} points but frozen corpus has {len(chunks)} chunks"
        )

    dense = DenseRetriever(SentenceTransformerEmbedder(), vector_store)
    retriever: Any = dense
    if strategy in {"hybrid", "reranked"}:
        bm25 = BM25Retriever(list(chunks.values()))
        if bm25.chunk_ids != frozenset(chunks):
            vector_store.close()
            raise ValueError("BM25 chunk IDs do not match the frozen corpus")
        hybrid = HybridRetriever(dense, bm25)
        retriever = hybrid
        if strategy == "reranked":
            retriever = RerankedRetriever(hybrid, CrossEncoderReranker())

    llm_client = OpenAICompatibleLLMClient()
    configuration = {
        "embedding_model": EMBEDDING_MODEL_NAME,
        "bm25_tokenizer": TOKENIZER_DESCRIPTION,
        "dense_candidate_depth": DENSE_CANDIDATE_DEPTH,
        "bm25_candidate_depth": BM25_CANDIDATE_DEPTH,
        "rrf_k": RRF_K,
        "reranker_model": RERANKER_MODEL_NAME,
        "reranker_candidate_depth": RERANKER_CANDIDATE_DEPTH,
        "generation_model": llm_client.model,
        "temperature": llm_client.temperature,
        "context_top_k": GENERATION_CONTEXT_TOP_K,
        "chunk_size": CHUNK_SIZE,
        "chunk_overlap": CHUNK_OVERLAP,
        "qdrant_path": str(QDRANT_PATH.relative_to(PROJECT_ROOT)),
        "qdrant_collection": QDRANT_COLLECTION_NAME,
        "corpus_documents": len(documents),
        "corpus_chunks": len(chunks),
    }
    return (
        RAGPipeline(retriever, llm_client),
        vector_store,
        configuration,
    )


def evaluate_generation(
    strategy: str,
    output_path: Path,
    *,
    dataset_path: Path = PROJECT_ROOT / "evaluation" / "dataset.json",
    resume: bool = False,
    overwrite: bool = False,
    items: Sequence[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Validate inputs, warm the full pipeline, and run one strategy."""
    dataset = list(items) if items is not None else load_dataset(dataset_path)
    pipeline, vector_store, configuration = build_generation_runtime(strategy)
    try:
        if items is None:
            documents, chunks = build_corpus_inventory(PROJECT_ROOT / "data" / "raw")
            validate_dataset(dataset, documents, chunks)
            configuration["evaluation_questions"] = len(dataset)
        else:
            configuration["evaluation_questions"] = len(dataset)
        pipeline.answer(dataset[0]["question"])
        return run_questions(
            dataset,
            strategy,
            pipeline,
            output_path,
            configuration,
            resume=resume,
            overwrite=overwrite,
        )
    finally:
        vector_store.close()


def validate_annotations(
    annotations: dict[str, Any],
    dataset: Sequence[dict[str, Any]],
) -> None:
    """Require complete manual 0/1/2 annotations for every strategy and question."""
    expected_ids = {item["id"] for item in dataset}
    if set(annotations) != expected_ids:
        raise ValueError("Annotation question IDs must exactly match the dataset")
    for question_id, strategies in annotations.items():
        if not isinstance(strategies, dict) or set(strategies) != set(
            GENERATION_STRATEGIES
        ):
            raise ValueError(f"{question_id} must annotate all three strategies")
        for strategy, annotation in strategies.items():
            if not isinstance(annotation, dict):
                raise ValueError(f"{question_id}/{strategy} annotation must be an object")
            for metric in ANNOTATION_METRICS:
                score = annotation.get(metric)
                if isinstance(score, bool) or not isinstance(score, int) or score not in {
                    0,
                    1,
                    2,
                }:
                    raise ValueError(
                        f"{question_id}/{strategy}/{metric} must be 0, 1, or 2"
                    )
            if not isinstance(annotation.get("notes"), str):
                raise ValueError(f"{question_id}/{strategy}/notes must be text")
            if not isinstance(annotation.get("requires_human_review", False), bool):
                raise ValueError(
                    f"{question_id}/{strategy}/requires_human_review must be boolean"
                )
            categories = annotation.get("error_categories", [])
            if not isinstance(categories, list) or not all(
                isinstance(category, str) for category in categories
            ):
                raise ValueError(
                    f"{question_id}/{strategy}/error_categories must be a string list"
                )
            coverage = annotation.get("citation_coverage")
            if coverage not in CITATION_COVERAGE_LEVELS:
                raise ValueError(
                    f"{question_id}/{strategy}/citation_coverage must be complete, "
                    "partial, or not_applicable"
                )


def _score_summary(scores: Iterable[int]) -> dict[str, Any]:
    values = list(scores)
    counts = Counter(values)
    mean = statistics.fmean(values) if values else 0.0
    return {
        "mean": mean,
        "normalized_mean": mean / 2,
        "counts": {str(score): counts[score] for score in (0, 1, 2)},
    }


def aggregate_annotations(
    annotations: dict[str, Any],
    dataset: Sequence[dict[str, Any]],
) -> dict[str, Any]:
    """Aggregate validated manual annotations overall and by question type."""
    validate_annotations(annotations, dataset)
    difficulty_by_id = {item["id"]: item["difficulty"] for item in dataset}
    overall = {
        strategy: {
            metric: _score_summary(
                annotations[question_id][strategy][metric]
                for question_id in annotations
            )
            for metric in ANNOTATION_METRICS
        }
        for strategy in GENERATION_STRATEGIES
    }
    for strategy in GENERATION_STRATEGIES:
        overall[strategy]["citation_coverage"] = dict(
            Counter(
                annotations[question_id][strategy]["citation_coverage"]
                for question_id in annotations
            )
        )
    by_type: dict[str, Any] = {}
    for difficulty in sorted(set(difficulty_by_id.values())):
        ids = [
            question_id
            for question_id, item_difficulty in difficulty_by_id.items()
            if item_difficulty == difficulty
        ]
        by_type[difficulty] = {
            strategy: {
                metric: _score_summary(
                    annotations[question_id][strategy][metric]
                    for question_id in ids
                )
                for metric in ANNOTATION_METRICS
            }
            for strategy in GENERATION_STRATEGIES
        }
        for strategy in GENERATION_STRATEGIES:
            by_type[difficulty][strategy]["citation_coverage"] = dict(
                Counter(
                    annotations[question_id][strategy]["citation_coverage"]
                    for question_id in ids
                )
            )
    return {"overall": overall, "by_question_type": by_type}


def classify_comparison(left: dict[str, Any], right: dict[str, Any]) -> str:
    """Compare annotations lexicographically by correctness, faithfulness, citation."""
    left_scores = tuple(left[metric] for metric in ANNOTATION_METRICS)
    right_scores = tuple(right[metric] for metric in ANNOTATION_METRICS)
    if left_scores > right_scores:
        return "improved"
    if left_scores < right_scores:
        return "regressed"
    return "unchanged"


def comparison_counts(
    annotations: dict[str, Any],
    left_strategy: str,
    right_strategy: str,
) -> dict[str, int]:
    """Count deterministic per-query comparisons between two strategies."""
    counts = Counter(
        classify_comparison(
            strategies[left_strategy],
            strategies[right_strategy],
        )
        for strategies in annotations.values()
    )
    return {
        outcome: counts[outcome]
        for outcome in ("improved", "unchanged", "regressed")
    }


def abstention_accuracy(annotations: Sequence[dict[str, Any]]) -> dict[str, Any]:
    """Calculate correct-abstention frequency from explicit manual outcomes."""
    if not annotations:
        raise ValueError("At least one unsupported annotation is required")
    outcomes = []
    for annotation in annotations:
        outcome = annotation.get("outcome")
        if outcome not in ABSTENTION_OUTCOMES:
            raise ValueError(f"Invalid abstention outcome: {outcome}")
        outcomes.append(outcome)
    correct = outcomes.count("abstained_correctly")
    return {
        "correct_abstentions": correct,
        "questions": len(outcomes),
        "accuracy": correct / len(outcomes),
        "counts": dict(Counter(outcomes)),
    }


def percentile(values: Sequence[float], fraction: float) -> float:
    """Return a linearly interpolated percentile."""
    if not values:
        raise ValueError("At least one latency is required")
    ordered = sorted(values)
    position = (len(ordered) - 1) * fraction
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    weight = position - lower
    return ordered[lower] + (ordered[upper] - ordered[lower]) * weight


def pearson_correlation(left: Sequence[float], right: Sequence[float]) -> float | None:
    """Return Pearson correlation, or None when either input has no variance."""
    if len(left) != len(right) or not left:
        raise ValueError("Correlation inputs must be non-empty and aligned")
    left_mean = statistics.fmean(left)
    right_mean = statistics.fmean(right)
    left_centered = [value - left_mean for value in left]
    right_centered = [value - right_mean for value in right]
    denominator = (
        sum(value * value for value in left_centered)
        * sum(value * value for value in right_centered)
    ) ** 0.5
    if denominator == 0:
        return None
    return sum(
        left_value * right_value
        for left_value, right_value in zip(left_centered, right_centered)
    ) / denominator


def latency_summary(results: Sequence[dict[str, Any]]) -> dict[str, float]:
    """Summarize successful end-to-end generation latencies in milliseconds."""
    successful = [result for result in results if result.get("status") == "completed"]
    values = [float(result["latency_ms"]) for result in successful]
    if not values:
        raise ValueError("No successful generation latencies found")
    characters = [float(result["answer_characters"]) for result in successful]
    return {
        "mean": statistics.fmean(values),
        "median": statistics.median(values),
        "p95": percentile(values, 0.95),
        "mean_answer_characters": statistics.fmean(characters),
        "latency_answer_character_correlation": pearson_correlation(
            values,
            characters,
        ),
    }


def retrieval_generation_analysis(
    annotations: dict[str, Any],
    retrieval_outputs: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    """Relate frozen per-query retrieval metrics to manual generation scores."""
    retrieval_by_strategy = {
        strategy: {query["id"]: query for query in output["queries"]}
        for strategy, output in retrieval_outputs.items()
    }
    by_strategy: dict[str, Any] = {}
    for strategy in GENERATION_STRATEGIES:
        question_ids = list(annotations)
        ndcg_values = [
            retrieval_by_strategy[strategy][question_id]["metrics"]["ndcg_at_5"]
            for question_id in question_ids
        ]
        answer_scores = [
            annotations[question_id][strategy]["answer_correctness"]
            for question_id in question_ids
        ]
        by_strategy[strategy] = {
            "ndcg_answer_correctness_correlation": pearson_correlation(
                ndcg_values,
                answer_scores,
            )
        }

    transitions = {}
    for name, left_strategy, right_strategy in (
        ("hybrid_vs_dense", "hybrid", "dense"),
        ("reranked_vs_hybrid", "reranked", "hybrid"),
    ):
        ndcg_deltas = []
        recall_deltas = []
        answer_deltas = []
        cross_tab: Counter[tuple[str, str]] = Counter()
        for question_id, strategies in annotations.items():
            left_metrics = retrieval_by_strategy[left_strategy][question_id]["metrics"]
            right_metrics = retrieval_by_strategy[right_strategy][question_id]["metrics"]
            ndcg_delta = left_metrics["ndcg_at_5"] - right_metrics["ndcg_at_5"]
            recall_delta = left_metrics["recall_at_5"] - right_metrics["recall_at_5"]
            answer_delta = (
                strategies[left_strategy]["answer_correctness"]
                - strategies[right_strategy]["answer_correctness"]
            )
            ndcg_deltas.append(ndcg_delta)
            recall_deltas.append(recall_delta)
            answer_deltas.append(answer_delta)
            retrieval_direction = (
                "improved"
                if ndcg_delta > 1e-12
                else "regressed"
                if ndcg_delta < -1e-12
                else "unchanged"
            )
            generation_direction = classify_comparison(
                strategies[left_strategy],
                strategies[right_strategy],
            )
            cross_tab[(retrieval_direction, generation_direction)] += 1
        transitions[name] = {
            "mean_ndcg_at_5_delta": statistics.fmean(ndcg_deltas),
            "mean_recall_at_5_delta": statistics.fmean(recall_deltas),
            "mean_answer_correctness_delta": statistics.fmean(answer_deltas),
            "ndcg_delta_answer_delta_correlation": pearson_correlation(
                ndcg_deltas,
                answer_deltas,
            ),
            "cross_tab": {
                retrieval_direction: {
                    generation_direction: cross_tab[
                        (retrieval_direction, generation_direction)
                    ]
                    for generation_direction in (
                        "improved",
                        "unchanged",
                        "regressed",
                    )
                }
                for retrieval_direction in ("improved", "unchanged", "regressed")
            },
        }
    return {"by_strategy": by_strategy, "transitions": transitions}


def build_review_markdown(
    dataset: Sequence[dict[str, Any]],
    outputs: dict[str, dict[str, Any]],
    annotations: dict[str, Any],
    *,
    excerpt_characters: int = 500,
) -> str:
    """Render generated answers, retrieved excerpts, and manual scores for review."""
    validate_annotations(annotations, dataset)
    if set(outputs) != set(GENERATION_STRATEGIES):
        raise ValueError("Review requires Dense, Hybrid, and Reranked outputs")
    results_by_strategy: dict[str, dict[str, dict[str, Any]]] = {}
    expected_ids = [item["id"] for item in dataset]
    for strategy, output in outputs.items():
        if output.get("strategy") != strategy:
            raise ValueError(f"Output strategy mismatch for {strategy}")
        results = {
            result["question_id"]: result
            for result in output.get("results", [])
            if isinstance(result, dict) and "question_id" in result
        }
        if set(results) != set(expected_ids):
            raise ValueError(f"{strategy} output does not match the dataset")
        results_by_strategy[strategy] = results

    lines = [
        "# Generation Evaluation Review",
        "",
        "Scores use the manually reviewed 0–2 rubric. Context excerpts are truncated; raw JSON preserves full text.",
        "",
    ]
    for item in dataset:
        question_id = item["id"]
        lines.extend(
            [
                f"# {question_id}",
                "",
                "## Question",
                "",
                item["question"],
                "",
                "## Reference Answer",
                "",
                item["reference_answer"],
                "",
            ]
        )
        for strategy in GENERATION_STRATEGIES:
            result = results_by_strategy[strategy][question_id]
            annotation = annotations[question_id][strategy]
            lines.extend(
                [
                    "---",
                    "",
                    f"## {strategy.title()}",
                    "",
                    "### Retrieved Context",
                    "",
                ]
            )
            for context in result["retrieved_chunks"]:
                excerpt = " ".join(context["text"].split())
                if len(excerpt) > excerpt_characters:
                    excerpt = f"{excerpt[: excerpt_characters - 1]}…"
                lines.append(
                    f"- {context['label']} source=`{context['source']}` "
                    f"chunk_id=`{context['chunk_id']}` — {excerpt}"
                )
            citations = result["citations"]
            citation_text = (
                ", ".join(
                    f"{citation['label']} -> `{citation['chunk_id']}`"
                    for citation in citations
                )
                if citations
                else "None"
            )
            invalid = result["invalid_citation_labels"]
            lines.extend(
                [
                    "",
                    "### Answer",
                    "",
                    result["generated_answer"] or f"ERROR: {result['error']}",
                    "",
                    "### Citations",
                    "",
                    citation_text,
                    "",
                    f"Invalid labels: {', '.join(invalid) if invalid else 'None'}",
                    "",
                    "### Scores",
                    "",
                    f"- Answer Correctness: {annotation['answer_correctness']}",
                    f"- Faithfulness: {annotation['faithfulness']}",
                    f"- Citation Correctness: {annotation['citation_correctness']}",
                    f"- Requires human review: {annotation.get('requires_human_review', False)}",
                    "",
                    "### Notes",
                    "",
                    annotation["notes"],
                    "",
                ]
            )
    return "\n".join(lines)
