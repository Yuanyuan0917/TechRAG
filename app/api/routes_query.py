"""Thin query routes backed by the existing TechRAG pipeline."""

from __future__ import annotations

import asyncio
import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Callable, Mapping

from fastapi import APIRouter, Depends, HTTPException, Request, status

from app.config import PROJECT_ROOT
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

from .schemas import (
    CitationResponse,
    HealthResponse,
    QueryRequest,
    QueryResponse,
    RetrievedChunkResponse,
    RetrievalStrategy,
)

LOGGER = logging.getLogger(__name__)
PREVIEW_CHARACTERS = 360


class RetrievalUnavailableError(RuntimeError):
    """Raised when the local corpus or Qdrant index cannot serve retrieval."""


class GenerationExecutionError(RuntimeError):
    """Raised when generation fails outside expected LLM availability errors."""


class _GuardedRetriever:
    """Preserve retrieval errors across the existing generation pipeline boundary."""

    def __init__(self, retriever: Any) -> None:
        self._retriever = retriever

    def retrieve(self, query: str, top_k: int = 5) -> list[Any]:
        try:
            return self._retriever.retrieve(query, top_k=top_k)
        except Exception as error:
            raise RetrievalUnavailableError(
                "Retrieval failed. Verify the local Qdrant index."
            ) from error


def _preview(text: str, limit: int = PREVIEW_CHARACTERS) -> str:
    """Return a compact, single-line display preview."""
    compact = " ".join(text.split())
    if len(compact) <= limit:
        return compact
    return f"{compact[: limit - 1]}…"


def _serialize_retrieved_chunk(
    result: Any,
    rank: int,
    strategy: RetrievalStrategy,
) -> RetrievedChunkResponse:
    chunk = result.chunk
    if strategy == "reranked":
        score = float(result.reranker_score)
        score_type = "cross_encoder"
        hybrid_rank = int(result.hybrid_rank)
        hybrid_rrf_score = float(result.hybrid_rrf_score)
    else:
        score = float(result.score)
        score_type = "rrf" if strategy == "hybrid" else "cosine"
        hybrid_rank = None
        hybrid_rrf_score = None
    return RetrievedChunkResponse(
        rank=rank,
        chunk_id=chunk.id,
        document_id=chunk.document_id,
        source=Path(chunk.source).name,
        chunk_index=chunk.chunk_index,
        score=score,
        score_type=score_type,
        preview=_preview(chunk.text),
        hybrid_rank=hybrid_rank,
        hybrid_rrf_score=hybrid_rrf_score,
    )


class TechRAGService:
    """Reuse the existing retrieval models and construct cheap per-query pipelines."""

    def __init__(
        self,
        *,
        retrievers: Mapping[str, Any] | None = None,
        llm_client_factory: Callable[[], Any] = OpenAICompatibleLLMClient,
    ) -> None:
        self._retrievers = dict(retrievers) if retrievers is not None else None
        self._llm_client_factory = llm_client_factory
        self._llm_client: Any | None = None
        self._vector_store: QdrantVectorStore | None = None
        self._initialization_lock = threading.Lock()
        self._executor = ThreadPoolExecutor(
            max_workers=1,
            thread_name_prefix="techrag-runtime",
        )

    def _build_retrievers(self) -> dict[str, Any]:
        vector_store: QdrantVectorStore | None = None
        try:
            _, chunks = build_corpus_inventory(PROJECT_ROOT / "data" / "raw")
            vector_store = QdrantVectorStore()
            if not vector_store.collection_exists():
                raise ValueError(
                    "Dense index not found; run scripts/ingest.py --index first"
                )
            indexed_points = vector_store.count()
            if indexed_points != len(chunks):
                raise ValueError(
                    f"Qdrant contains {indexed_points} points but the corpus has "
                    f"{len(chunks)} chunks; rebuild the index"
                )
            if vector_store.chunk_ids() != frozenset(chunks):
                raise ValueError(
                    "Qdrant chunk IDs do not match the mounted corpus; rebuild "
                    "the index from the same runtime path"
                )

            dense = DenseRetriever(SentenceTransformerEmbedder(), vector_store)
            bm25 = BM25Retriever(list(chunks.values()))
            if bm25.chunk_ids != frozenset(chunks):
                raise ValueError("BM25 chunk IDs do not match the local corpus")
            hybrid = HybridRetriever(dense, bm25)
            reranked = RerankedRetriever(hybrid, CrossEncoderReranker())
        except Exception as error:
            if vector_store is not None:
                vector_store.close()
            raise RetrievalUnavailableError(
                "Retrieval is unavailable. Verify the local corpus and Qdrant index."
            ) from error

        self._vector_store = vector_store
        return {"dense": dense, "hybrid": hybrid, "reranked": reranked}

    def _get_retriever(self, strategy: RetrievalStrategy) -> Any:
        if self._retrievers is None:
            with self._initialization_lock:
                if self._retrievers is None:
                    self._retrievers = self._build_retrievers()
        return self._retrievers[strategy]

    def _get_llm_client(self) -> Any:
        if self._llm_client is None:
            with self._initialization_lock:
                if self._llm_client is None:
                    self._llm_client = self._llm_client_factory()
        return self._llm_client

    def query(self, query_request: QueryRequest) -> QueryResponse:
        """Execute one retrieval or generation request and serialize its provenance."""
        started = time.perf_counter()
        retriever = _GuardedRetriever(self._get_retriever(query_request.strategy))

        if query_request.generate_answer:
            try:
                generated = RAGPipeline(
                    retriever,
                    self._get_llm_client(),
                    context_top_k=query_request.top_k,
                ).answer(query_request.question)
            except (RetrievalUnavailableError, LLMConfigurationError, LLMRequestError):
                raise
            except Exception as error:
                raise GenerationExecutionError(
                    "Answer generation failed unexpectedly."
                ) from error
            results = list(generated.retrieved_chunks)
            answer = generated.answer
            invalid_labels = list(generated.invalid_citation_labels)
        else:
            results = retriever.retrieve(
                query_request.question,
                top_k=query_request.top_k,
            )
            answer = None
            invalid_labels = []

        retrieved_chunks = [
            _serialize_retrieved_chunk(result, rank, query_request.strategy)
            for rank, result in enumerate(results, start=1)
        ]
        retrieved_by_id = {chunk.chunk_id: chunk for chunk in retrieved_chunks}
        citations = []
        if query_request.generate_answer:
            citations = [
                CitationResponse(
                    label=citation.label,
                    chunk_id=citation.chunk_id,
                    document_id=citation.document_id,
                    source=Path(citation.source).name,
                    chunk_index=citation.chunk_index,
                    preview=(
                        retrieved_by_id[citation.chunk_id].preview
                        if citation.chunk_id in retrieved_by_id
                        else ""
                    ),
                )
                for citation in generated.citations
            ]

        return QueryResponse(
            question=query_request.question,
            strategy=query_request.strategy,
            answer=answer,
            citations=citations,
            invalid_citation_labels=invalid_labels,
            retrieved_chunks=retrieved_chunks,
            latency_ms=(time.perf_counter() - started) * 1_000,
        )

    async def query_async(self, query_request: QueryRequest) -> QueryResponse:
        """Run pipeline work on the service's single reusable model thread."""
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(self._executor, self.query, query_request)

    def _close_resources(self) -> None:
        if self._vector_store is not None:
            self._vector_store.close()
            self._vector_store = None

    async def close(self) -> None:
        """Close Qdrant on its owning thread and stop the runtime executor."""
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(self._executor, self._close_resources)
        self._executor.shutdown(wait=True)


def get_query_service(request: Request) -> TechRAGService:
    """Return the application-scoped query service."""
    return request.app.state.query_service


router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    """Report process health without loading models or querying the index."""
    return HealthResponse()


@router.post("/query", response_model=QueryResponse)
async def query(
    query_request: QueryRequest,
    service: TechRAGService = Depends(get_query_service),
) -> QueryResponse:
    """Run the selected existing retrieval strategy, optionally with generation."""
    try:
        return await service.query_async(query_request)
    except RetrievalUnavailableError as error:
        LOGGER.exception("TechRAG retrieval request failed")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={"code": "retrieval_unavailable", "message": str(error)},
        ) from error
    except (LLMConfigurationError, LLMRequestError) as error:
        LOGGER.warning("TechRAG generation unavailable: %s", error)
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={
                "code": "generation_unavailable",
                "message": (
                    "Answer generation is unavailable. Start MLX-LM and verify the "
                    "local LLM environment settings."
                ),
            },
        ) from error
    except GenerationExecutionError as error:
        LOGGER.exception("TechRAG generation request failed")
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail={"code": "generation_failed", "message": str(error)},
        ) from error
    except Exception as error:
        LOGGER.exception("Unexpected TechRAG API failure")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "code": "internal_error",
                "message": "The query failed unexpectedly.",
            },
        ) from error
