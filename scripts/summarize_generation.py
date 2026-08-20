"""Validate manual generation annotations and build reproducible summaries."""

from __future__ import annotations

import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.evaluation.generation import (
    GENERATION_STRATEGIES,
    abstention_accuracy,
    aggregate_annotations,
    build_review_markdown,
    comparison_counts,
    latency_summary,
    load_generation_output,
    retrieval_generation_analysis,
    validate_annotations,
)
from app.evaluation.runner import load_dataset


def main() -> int:
    """Write the review Markdown and print machine-readable aggregate results."""
    dataset = load_dataset(PROJECT_ROOT / "evaluation" / "dataset.json")
    annotation_path = PROJECT_ROOT / "evaluation" / "generation_annotations.json"
    annotations = json.loads(annotation_path.read_text(encoding="utf-8"))
    validate_annotations(annotations, dataset)
    outputs = {
        strategy: load_generation_output(
            PROJECT_ROOT / "evaluation" / "generation" / f"{strategy}.json"
        )
        for strategy in GENERATION_STRATEGIES
    }
    unsupported_annotations = json.loads(
        (
            PROJECT_ROOT / "evaluation" / "unsupported_annotations.json"
        ).read_text(encoding="utf-8")
    )
    summary = aggregate_annotations(annotations, dataset)
    summary["comparisons"] = {
        "reranked_vs_hybrid": comparison_counts(
            annotations,
            "reranked",
            "hybrid",
        ),
        "hybrid_vs_dense": comparison_counts(
            annotations,
            "hybrid",
            "dense",
        ),
    }
    summary["latency_ms"] = {
        strategy: latency_summary(output["results"])
        for strategy, output in outputs.items()
    }
    summary["abstention"] = abstention_accuracy(unsupported_annotations)
    retrieval_paths = {
        "dense": PROJECT_ROOT / "evaluation" / "results" / "dense.json",
        "hybrid": PROJECT_ROOT / "evaluation" / "results" / "hybrid.json",
        "reranked": (
            PROJECT_ROOT / "evaluation" / "results" / "hybrid_reranked.json"
        ),
    }
    retrieval_outputs = {
        strategy: json.loads(path.read_text(encoding="utf-8"))
        for strategy, path in retrieval_paths.items()
    }
    summary["retrieval_generation"] = retrieval_generation_analysis(
        annotations,
        retrieval_outputs,
    )

    review = build_review_markdown(dataset, outputs, annotations)
    (PROJECT_ROOT / "evaluation" / "generation_review.md").write_text(
        review,
        encoding="utf-8",
    )
    summary_path = PROJECT_ROOT / "evaluation" / "generation_summary.json"
    summary_path.write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
