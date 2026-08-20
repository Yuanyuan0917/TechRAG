"""Run resumable real-model generation evaluation for one retrieval strategy."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.evaluation.generation import evaluate_generation
from app.evaluation.runner import load_dataset


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strategy",
        required=True,
        choices=("dense", "hybrid", "reranked"),
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--resume", action="store_true")
    mode.add_argument("--overwrite", action="store_true")
    parser.add_argument(
        "--unsupported",
        action="store_true",
        help="Run the separate unsupported set; requires reranked strategy",
    )
    return parser


def main() -> int:
    """Run one generation evaluation and print completion counts."""
    parser = _parser()
    args = parser.parse_args()
    if args.unsupported and args.strategy != "reranked":
        parser.error("--unsupported requires --strategy reranked")

    items = None
    if args.unsupported:
        items = load_dataset(PROJECT_ROOT / "evaluation" / "unsupported_questions.json")
        output_path = PROJECT_ROOT / "evaluation" / "generation" / "unsupported.json"
    else:
        output_path = (
            PROJECT_ROOT / "evaluation" / "generation" / f"{args.strategy}.json"
        )
    result = evaluate_generation(
        args.strategy,
        output_path,
        resume=args.resume,
        overwrite=args.overwrite,
        items=items,
    )
    counts = {
        "completed": sum(
            item.get("status") == "completed" for item in result["results"]
        ),
        "errors": sum(item.get("status") == "error" for item in result["results"]),
    }
    print(json.dumps({"output": str(output_path), **counts}, indent=2))
    return 0 if counts["errors"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
