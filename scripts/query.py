"""Query the local TechRAG dense retrieval index."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.retrieval.dense import DenseRetriever
from app.retrieval.embedder import SentenceTransformerEmbedder
from app.retrieval.vector_store import QdrantVectorStore


def _preview(text: str, limit: int = 240) -> str:
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    return f"{text[: limit - 1]}…"


def _argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Search the local dense chunk index.")
    parser.add_argument("query", help="Question or search text")
    parser.add_argument("--top-k", type=int, default=5)
    return parser


def main() -> int:
    """Run a query and print ranked chunk previews."""
    argument_parser = _argument_parser()
    args = argument_parser.parse_args()

    vector_store = QdrantVectorStore()
    try:
        if not vector_store.collection_exists():
            argument_parser.error("Dense index not found; run scripts/ingest.py --index first")

        embedder = SentenceTransformerEmbedder()
        retriever = DenseRetriever(embedder, vector_store)
        results = retriever.retrieve(args.query, top_k=args.top_k)
        for rank, result in enumerate(results, start=1):
            print(f"{rank}. score={result.score:.4f}")
            print(f"   source={Path(result.chunk.source).name}")
            print(f"   chunk_id={result.chunk.id}")
            print(f"   text={_preview(result.chunk.text)}")
    except (OSError, ValueError) as error:
        argument_parser.error(str(error))
    finally:
        vector_store.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
