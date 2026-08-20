"""Run a frozen TechRAG retrieval evaluation."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.evaluation.runner import evaluate_retrieval


def _argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate retrieval strategies.")
    parser.add_argument(
        "--strategy",
        choices=("dense", "hybrid", "reranked"),
        default="dense",
    )
    parser.add_argument(
        "--output",
        type=Path,
    )
    return parser


def main() -> int:
    """Run evaluation and print aggregate metrics."""
    args = _argument_parser().parse_args()
    result_name = "hybrid_reranked" if args.strategy == "reranked" else args.strategy
    output_path = args.output or (
        PROJECT_ROOT / "evaluation" / "results" / f"{result_name}.json"
    )
    results = evaluate_retrieval(args.strategy, output_path=output_path)
    metrics = results["aggregate_metrics"]

    print(f"Strategy: {results['strategy']}")
    print(f"Questions: {len(results['queries'])}")
    print()
    print(f"Recall@1: {metrics['recall_at_1']:.6f}")
    print(f"Recall@5: {metrics['recall_at_5']:.6f}")
    print(f"Recall@10: {metrics['recall_at_10']:.6f}")
    print(f"MRR: {metrics['mrr']:.6f}")
    print(f"nDCG@5: {metrics['ndcg_at_5']:.6f}")
    print()
    print(f"Saved: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
