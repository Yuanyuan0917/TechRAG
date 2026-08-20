"""Query the local TechRAG dense, hybrid, or reranked retrieval index."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.evaluation.runner import build_corpus_inventory
from app.generation.llm_client import (
    LLMConfigurationError,
    LLMRequestError,
    OpenAICompatibleLLMClient,
)
from app.generation.rag import RAGPipeline
from app.retrieval.bm25 import BM25Retriever
from app.retrieval.dense import DenseRetriever
from app.retrieval.embedder import SentenceTransformerEmbedder
from app.retrieval.hybrid import HybridRetriever
from app.retrieval.reranker import CrossEncoderReranker, RerankedRetriever
from app.retrieval.vector_store import QdrantVectorStore


def _preview(text: str, limit: int = 240) -> str:
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    return f"{text[: limit - 1]}…"


def _argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Search the local chunk index.")
    parser.add_argument("query", help="Question or search text")
    parser.add_argument(
        "--top-k",
        type=int,
        default=5,
        help="Retrieval-only result count; answer context always uses configured top-5",
    )
    parser.add_argument(
        "--strategy",
        choices=("dense", "hybrid", "reranked"),
        default="dense",
    )
    parser.add_argument(
        "--answer",
        action="store_true",
        help="Generate a grounded answer from reranked top-5 chunks",
    )
    parser.add_argument(
        "--show-context",
        action="store_true",
        help="Show citation context previews with a generated answer",
    )
    return parser


def main() -> int:
    """Run a query and print ranked chunk previews."""
    argument_parser = _argument_parser()
    args = argument_parser.parse_args()
    if args.answer and args.strategy != "reranked":
        argument_parser.error("--answer requires --strategy reranked")
    if args.show_context and not args.answer:
        argument_parser.error("--show-context requires --answer")

    llm_client = None
    if args.answer:
        try:
            llm_client = OpenAICompatibleLLMClient()
        except LLMConfigurationError as error:
            argument_parser.error(str(error))

    vector_store = QdrantVectorStore()
    try:
        if not vector_store.collection_exists():
            argument_parser.error("Dense index not found; run scripts/ingest.py --index first")

        embedder = SentenceTransformerEmbedder()
        dense_retriever = DenseRetriever(embedder, vector_store)
        if args.strategy in {"hybrid", "reranked"}:
            _, chunks = build_corpus_inventory(PROJECT_ROOT / "data" / "raw")
            bm25_retriever = BM25Retriever(list(chunks.values()))
            if bm25_retriever.chunk_ids != frozenset(chunks):
                raise ValueError("BM25 chunk IDs do not match the frozen corpus")
            hybrid_retriever = HybridRetriever(dense_retriever, bm25_retriever)
            if args.strategy == "reranked":
                retriever = RerankedRetriever(
                    hybrid_retriever,
                    CrossEncoderReranker(),
                )
            else:
                retriever = hybrid_retriever
        else:
            retriever = dense_retriever
        if args.answer:
            generated = RAGPipeline(retriever, llm_client).answer(args.query)
            print("Answer:")
            print(generated.answer)
            print()
            print("Citations:")
            if generated.citations:
                for citation in generated.citations:
                    print(
                        f"{citation.label} source={Path(citation.source).name}"
                    )
                    print(f"     chunk_id={citation.chunk_id}")
                    print(f"     document_id={citation.document_id}")
                    print(f"     chunk_index={citation.chunk_index}")
            else:
                print("(none)")
            if generated.invalid_citation_labels:
                print()
                print(
                    "Invalid citation labels: "
                    + ", ".join(generated.invalid_citation_labels)
                )
            if args.show_context:
                print()
                print("Contexts:")
                for context in generated.contexts:
                    print(
                        f"{context.label} source={Path(context.chunk.source).name} "
                        f"chunk_id={context.chunk.id}"
                    )
                    print(f"     text={_preview(context.chunk.text)}")
            return 0

        results = retriever.retrieve(args.query, top_k=args.top_k)
        for rank, result in enumerate(results, start=1):
            if args.strategy == "reranked":
                print(f"{rank}. reranker_score={result.reranker_score:.4f}")
                print(f"   hybrid_rank={result.hybrid_rank}")
                print(f"   hybrid_rrf_score={result.hybrid_rrf_score:.4f}")
            else:
                score_label = "rrf_score" if args.strategy == "hybrid" else "score"
                print(f"{rank}. {score_label}={result.score:.4f}")
            print(f"   source={Path(result.chunk.source).name}")
            print(f"   chunk_id={result.chunk.id}")
            print(f"   text={_preview(result.chunk.text)}")
    except (LLMConfigurationError, LLMRequestError, OSError, ValueError) as error:
        argument_parser.error(str(error))
    finally:
        vector_store.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
