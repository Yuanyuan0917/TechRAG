"""Query the local TechRAG dense or hybrid retrieval index."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.evaluation.runner import build_corpus_inventory
from app.retrieval.bm25 import BM25Retriever
from app.retrieval.dense import DenseRetriever
from app.retrieval.embedder import SentenceTransformerEmbedder
from app.retrieval.hybrid import HybridRetriever
from app.retrieval.vector_store import QdrantVectorStore


def _preview(text: str, limit: int = 240) -> str:
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    return f"{text[: limit - 1]}…"


def _argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Search the local chunk index.")
    parser.add_argument("query", help="Question or search text")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument(
        "--strategy",
        choices=("dense", "hybrid"),
        default="dense",
    )
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
        dense_retriever = DenseRetriever(embedder, vector_store)
        if args.strategy == "hybrid":
            _, chunks = build_corpus_inventory(PROJECT_ROOT / "data" / "raw")
            bm25_retriever = BM25Retriever(list(chunks.values()))
            if bm25_retriever.chunk_ids != frozenset(chunks):
                raise ValueError("BM25 chunk IDs do not match the frozen corpus")
            retriever = HybridRetriever(dense_retriever, bm25_retriever)
        else:
            retriever = dense_retriever
        results = retriever.retrieve(args.query, top_k=args.top_k)
        for rank, result in enumerate(results, start=1):
            score_label = "rrf_score" if args.strategy == "hybrid" else "score"
            print(f"{rank}. {score_label}={result.score:.4f}")
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
