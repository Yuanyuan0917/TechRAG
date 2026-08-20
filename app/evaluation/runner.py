"""Run frozen TechRAG retrieval evaluations."""

from __future__ import annotations

import json
import statistics
import time
from collections import Counter
from pathlib import Path
from typing import Any

from app.config import (
    EMBEDDING_MODEL_NAME,
    PROJECT_ROOT,
    QDRANT_COLLECTION_NAME,
    QDRANT_PATH,
    RERANKER_MODEL_NAME,
)
from app.evaluation.metrics import ndcg_at_k, recall_at_k, reciprocal_rank
from app.ingestion.chunker import chunk_document
from app.ingestion.models import Chunk, Document
from app.ingestion.parser import parse_document
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

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
RETRIEVAL_DEPTH = 10
ALLOWED_DIFFICULTIES = {"fact", "multi_chunk", "cross_document"}


def load_dataset(path: Path) -> list[dict[str, Any]]:
    """Load a JSON evaluation dataset and require a list of questions."""
    with Path(path).open(encoding="utf-8") as dataset_file:
        dataset = json.load(dataset_file)
    if not isinstance(dataset, list):
        raise ValueError("Evaluation dataset must be a JSON list")
    return dataset


def build_corpus_inventory(
    corpus_path: Path,
) -> tuple[dict[str, Document], dict[str, Chunk]]:
    """Parse and chunk the frozen corpus with baseline configuration."""
    documents: dict[str, Document] = {}
    chunks: dict[str, Chunk] = {}
    files = sorted(
        (
            path
            for path in Path(corpus_path).iterdir()
            if path.is_file() and path.suffix.lower() in {".md", ".pdf"}
        ),
        key=lambda path: path.name.casefold(),
    )
    for path in files:
        document = parse_document(path)
        if document.id in documents:
            raise ValueError(f"Duplicate document ID in corpus: {document.id}")
        documents[document.id] = document
        for chunk in chunk_document(
            document,
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
        ):
            if chunk.id in chunks:
                raise ValueError(f"Duplicate chunk ID in corpus: {chunk.id}")
            chunks[chunk.id] = chunk
    return documents, chunks


def validate_dataset(
    dataset: list[dict[str, Any]],
    documents: dict[str, Document],
    chunks: dict[str, Chunk],
) -> None:
    """Fail on malformed or stale ground truth."""
    if not dataset:
        raise ValueError("Evaluation dataset must contain at least one question")

    question_ids: set[str] = set()
    normalized_questions: set[str] = set()
    for position, item in enumerate(dataset, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"Question {position} must be an object")

        question_id = item.get("id")
        question = item.get("question")
        reference_answer = item.get("reference_answer")
        relevant_documents = item.get("relevant_documents")
        relevant_chunks = item.get("relevant_chunks")
        chunk_relevance = item.get("chunk_relevance")
        difficulty = item.get("difficulty")

        if not isinstance(question_id, str) or not question_id:
            raise ValueError(f"Question {position} has an invalid ID")
        if question_id in question_ids:
            raise ValueError(f"Duplicate question ID: {question_id}")
        question_ids.add(question_id)

        if not isinstance(question, str) or not question.strip():
            raise ValueError(f"{question_id} has an empty question")
        normalized_question = " ".join(question.casefold().split())
        if normalized_question in normalized_questions:
            raise ValueError(f"Duplicate question text: {question}")
        normalized_questions.add(normalized_question)

        if not isinstance(reference_answer, str) or not reference_answer.strip():
            raise ValueError(f"{question_id} has an empty reference answer")
        if difficulty not in ALLOWED_DIFFICULTIES:
            raise ValueError(f"{question_id} has invalid difficulty: {difficulty}")
        if not isinstance(relevant_documents, list) or not relevant_documents:
            raise ValueError(f"{question_id} must have relevant documents")
        if len(relevant_documents) != len(set(relevant_documents)):
            raise ValueError(f"{question_id} has duplicate relevant documents")
        if not isinstance(relevant_chunks, list) or not relevant_chunks:
            raise ValueError(f"{question_id} must have relevant chunks")
        if len(relevant_chunks) != len(set(relevant_chunks)):
            raise ValueError(f"{question_id} has duplicate relevant chunks")
        if not isinstance(chunk_relevance, dict):
            raise ValueError(f"{question_id} must have chunk_relevance")
        if set(chunk_relevance) != set(relevant_chunks):
            raise ValueError(
                f"{question_id} chunk_relevance must label every relevant chunk exactly"
            )

        missing_documents = set(relevant_documents) - set(documents)
        if missing_documents:
            raise ValueError(
                f"{question_id} references missing documents: {sorted(missing_documents)}"
            )
        missing_chunks = set(relevant_chunks) - set(chunks)
        if missing_chunks:
            raise ValueError(
                f"{question_id} references missing chunks: {sorted(missing_chunks)}"
            )

        for chunk_id, grade in chunk_relevance.items():
            if not isinstance(grade, int) or grade not in {1, 2}:
                raise ValueError(f"{question_id} has invalid relevance for {chunk_id}")
            if chunks[chunk_id].document_id not in relevant_documents:
                raise ValueError(
                    f"{question_id} labels {chunk_id} outside relevant_documents"
                )


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _aggregate(query_results: list[dict[str, Any]]) -> dict[str, float]:
    return {
        "recall_at_1": _mean(
            [result["metrics"]["recall_at_1"] for result in query_results]
        ),
        "recall_at_5": _mean(
            [result["metrics"]["recall_at_5"] for result in query_results]
        ),
        "recall_at_10": _mean(
            [result["metrics"]["recall_at_10"] for result in query_results]
        ),
        "mrr": _mean([result["metrics"]["reciprocal_rank"] for result in query_results]),
        "ndcg_at_5": _mean(
            [result["metrics"]["ndcg_at_5"] for result in query_results]
        ),
    }


def _percentile(values: list[float], percentile: float) -> float:
    """Return a linearly interpolated percentile for non-empty values."""
    ordered = sorted(values)
    position = (len(ordered) - 1) * percentile
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    fraction = position - lower
    return ordered[lower] + (ordered[upper] - ordered[lower]) * fraction


def _latency_summary(values: list[float]) -> dict[str, float]:
    """Summarize milliseconds across the fixed evaluation query set."""
    return {
        "mean": statistics.fmean(values),
        "median": statistics.median(values),
        "p95": _percentile(values, 0.95),
    }


def evaluate_retrieval(
    strategy: str,
    dataset_path: Path = PROJECT_ROOT / "evaluation" / "dataset.json",
    output_path: Path | None = None,
    corpus_path: Path = PROJECT_ROOT / "data" / "raw",
    retrieval_depth: int = RETRIEVAL_DEPTH,
) -> dict[str, Any]:
    """Validate ground truth, evaluate one strategy, and save results."""
    if strategy not in {"dense", "hybrid", "reranked"}:
        raise ValueError(f"Unsupported retrieval strategy: {strategy}")
    if retrieval_depth < 10:
        raise ValueError("retrieval_depth must be at least 10")

    dataset = load_dataset(dataset_path)
    documents, chunks = build_corpus_inventory(corpus_path)
    validate_dataset(dataset, documents, chunks)

    embedder = SentenceTransformerEmbedder()
    vector_store = QdrantVectorStore()
    try:
        if not vector_store.collection_exists():
            raise ValueError("Dense Qdrant collection does not exist; rebuild the index")
        indexed_points = vector_store.count()
        if indexed_points != len(chunks):
            raise ValueError(
                f"Qdrant has {indexed_points} points but frozen corpus has {len(chunks)} chunks"
            )

        dense_retriever = DenseRetriever(embedder, vector_store)
        if strategy in {"hybrid", "reranked"}:
            bm25_retriever = BM25Retriever(list(chunks.values()))
            expected_chunk_ids = frozenset(chunks)
            if bm25_retriever.chunk_ids != expected_chunk_ids:
                raise ValueError("BM25 chunk IDs do not match the frozen corpus")
            hybrid_retriever = HybridRetriever(dense_retriever, bm25_retriever)
            if strategy == "reranked":
                reranker = CrossEncoderReranker()
                reranked_retriever = RerankedRetriever(
                    hybrid_retriever,
                    reranker,
                    candidate_depth=RERANKER_CANDIDATE_DEPTH,
                )
                warmup_question = dataset[0]["question"]
                warmup_candidates = reranked_retriever.retrieve_candidates(
                    warmup_question
                )
                reranker.rerank(
                    warmup_question,
                    warmup_candidates,
                    top_k=retrieval_depth,
                )
            else:
                retriever = hybrid_retriever
        else:
            retriever = dense_retriever

        query_results: list[dict[str, Any]] = []
        hybrid_latencies: list[float] = []
        reranker_latencies: list[float] = []
        end_to_end_latencies: list[float] = []
        for item in dataset:
            hybrid_candidates = None
            query_latency = None
            if strategy == "reranked":
                start = time.perf_counter()
                hybrid_candidates = reranked_retriever.retrieve_candidates(
                    item["question"]
                )
                hybrid_finished = time.perf_counter()
                retrieved = reranker.rerank(
                    item["question"],
                    hybrid_candidates,
                    top_k=retrieval_depth,
                )
                reranker_finished = time.perf_counter()
                hybrid_ms = (hybrid_finished - start) * 1000
                reranker_ms = (reranker_finished - hybrid_finished) * 1000
                end_to_end_ms = (reranker_finished - start) * 1000
                hybrid_latencies.append(hybrid_ms)
                reranker_latencies.append(reranker_ms)
                end_to_end_latencies.append(end_to_end_ms)
                query_latency = {
                    "hybrid": hybrid_ms,
                    "reranker": reranker_ms,
                    "end_to_end": end_to_end_ms,
                }
            else:
                retrieved = retriever.retrieve(
                    item["question"],
                    top_k=retrieval_depth,
                )
            retrieved_ids = [result.chunk.id for result in retrieved]
            relevant_ids = item["relevant_chunks"]
            if strategy == "reranked":
                serialized_retrieved = [
                    {
                        "rank": result.rank,
                        "chunk_id": result.chunk.id,
                        "reranker_score": result.reranker_score,
                        "hybrid_rank": result.hybrid_rank,
                        "hybrid_rrf_score": result.hybrid_rrf_score,
                        "source": Path(result.chunk.source).name,
                    }
                    for result in retrieved
                ]
            else:
                serialized_retrieved = [
                    {
                        "rank": rank,
                        "chunk_id": result.chunk.id,
                        "score": result.score,
                        "source": Path(result.chunk.source).name,
                    }
                    for rank, result in enumerate(retrieved, start=1)
                ]
            query_result = {
                "id": item["id"],
                "difficulty": item["difficulty"],
                "question": item["question"],
                "relevant_chunk_ids": relevant_ids,
                "retrieved": serialized_retrieved,
                "metrics": {
                    "recall_at_1": recall_at_k(retrieved_ids, relevant_ids, 1),
                    "recall_at_5": recall_at_k(retrieved_ids, relevant_ids, 5),
                    "recall_at_10": recall_at_k(retrieved_ids, relevant_ids, 10),
                    "reciprocal_rank": reciprocal_rank(retrieved_ids, relevant_ids),
                    "ndcg_at_5": ndcg_at_k(
                        retrieved_ids,
                        item["chunk_relevance"],
                        5,
                    ),
                },
            }
            if strategy == "reranked":
                query_result["hybrid_candidate_chunk_ids"] = [
                    candidate.chunk.id for candidate in hybrid_candidates
                ]
                query_result["latency_ms"] = query_latency
            query_results.append(query_result)
    finally:
        vector_store.close()

    by_type = {
        difficulty: _aggregate(
            [
                result
                for result in query_results
                if result["difficulty"] == difficulty
            ]
        )
        for difficulty in sorted(ALLOWED_DIFFICULTIES)
    }
    type_counts = Counter(item["difficulty"] for item in dataset)
    for difficulty, metrics in by_type.items():
        metrics["questions"] = type_counts[difficulty]

    configuration: dict[str, Any]
    if strategy in {"hybrid", "reranked"}:
        configuration = {
            "dense_embedding_model": EMBEDDING_MODEL_NAME,
            "dense_similarity": "cosine",
            "dense_candidate_depth": DENSE_CANDIDATE_DEPTH,
            "bm25_candidate_depth": BM25_CANDIDATE_DEPTH,
            "bm25_tokenizer": TOKENIZER_DESCRIPTION,
            "fusion": "rrf",
            "rrf_k": RRF_K,
            "chunk_size": CHUNK_SIZE,
            "chunk_overlap": CHUNK_OVERLAP,
            "qdrant_mode": "local_persistent",
            "qdrant_path": str(QDRANT_PATH.relative_to(PROJECT_ROOT)),
            "collection": QDRANT_COLLECTION_NAME,
            "retrieval_depth": retrieval_depth,
            "corpus_documents": len(documents),
            "corpus_chunks": len(chunks),
            "bm25_chunks": len(bm25_retriever.chunk_ids),
            "evaluation_questions": len(dataset),
        }
        if strategy == "reranked":
            configuration.update(
                {
                    "reranker_model": RERANKER_MODEL_NAME,
                    "reranker_candidate_depth": RERANKER_CANDIDATE_DEPTH,
                }
            )
    else:
        configuration = {
            "embedding_model": EMBEDDING_MODEL_NAME,
            "chunk_size": CHUNK_SIZE,
            "chunk_overlap": CHUNK_OVERLAP,
            "similarity": "cosine",
            "qdrant_mode": "local_persistent",
            "qdrant_path": str(QDRANT_PATH.relative_to(PROJECT_ROOT)),
            "collection": QDRANT_COLLECTION_NAME,
            "retrieval_depth": retrieval_depth,
            "corpus_documents": len(documents),
            "corpus_chunks": len(chunks),
            "evaluation_questions": len(dataset),
        }

    result_strategy = "hybrid_reranked" if strategy == "reranked" else strategy
    results: dict[str, Any] = {
        "strategy": result_strategy,
        "configuration": configuration,
        "aggregate_metrics": _aggregate(query_results),
        "metrics_by_question_type": by_type,
        "queries": query_results,
    }
    if strategy == "reranked":
        results["latency_ms"] = {
            "measurement": "local steady-state after one excluded warmup query",
            "queries": len(dataset),
            "hybrid": _latency_summary(hybrid_latencies),
            "reranker": _latency_summary(reranker_latencies),
            "end_to_end": _latency_summary(end_to_end_latencies),
        }

    if output_path is None:
        result_name = "hybrid_reranked" if strategy == "reranked" else strategy
        output_path = PROJECT_ROOT / "evaluation" / "results" / f"{result_name}.json"
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as output_file:
        json.dump(results, output_file, indent=2)
        output_file.write("\n")
    return results


def evaluate_dense(
    dataset_path: Path = PROJECT_ROOT / "evaluation" / "dataset.json",
    output_path: Path = PROJECT_ROOT / "evaluation" / "results" / "dense.json",
    corpus_path: Path = PROJECT_ROOT / "data" / "raw",
    retrieval_depth: int = RETRIEVAL_DEPTH,
) -> dict[str, Any]:
    """Run the frozen dense evaluation."""
    return evaluate_retrieval(
        "dense",
        dataset_path=dataset_path,
        output_path=output_path,
        corpus_path=corpus_path,
        retrieval_depth=retrieval_depth,
    )


def evaluate_hybrid(
    dataset_path: Path = PROJECT_ROOT / "evaluation" / "dataset.json",
    output_path: Path = PROJECT_ROOT / "evaluation" / "results" / "hybrid.json",
    corpus_path: Path = PROJECT_ROOT / "data" / "raw",
    retrieval_depth: int = RETRIEVAL_DEPTH,
) -> dict[str, Any]:
    """Run dense plus BM25 retrieval fused with RRF."""
    return evaluate_retrieval(
        "hybrid",
        dataset_path=dataset_path,
        output_path=output_path,
        corpus_path=corpus_path,
        retrieval_depth=retrieval_depth,
    )


def evaluate_reranked(
    dataset_path: Path = PROJECT_ROOT / "evaluation" / "dataset.json",
    output_path: Path = PROJECT_ROOT / "evaluation" / "results" / "hybrid_reranked.json",
    corpus_path: Path = PROJECT_ROOT / "data" / "raw",
    retrieval_depth: int = RETRIEVAL_DEPTH,
) -> dict[str, Any]:
    """Run Hybrid top-20 followed by cross-encoder reranking."""
    return evaluate_retrieval(
        "reranked",
        dataset_path=dataset_path,
        output_path=output_path,
        corpus_path=corpus_path,
        retrieval_depth=retrieval_depth,
    )
