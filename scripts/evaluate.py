"""Run the frozen TechRAG dense retrieval evaluation."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.evaluation.runner import evaluate_dense


def _argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate dense retrieval.")
    parser.add_argument(
        "--output",
        type=Path,
        default=PROJECT_ROOT / "evaluation" / "results" / "dense.json",
    )
    return parser


def main() -> int:
    """Run evaluation and print aggregate metrics."""
    args = _argument_parser().parse_args()
    results = evaluate_dense(output_path=args.output)
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
    print(f"Saved: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
