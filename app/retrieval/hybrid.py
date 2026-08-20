"""Hybrid dense and BM25 retrieval with reciprocal rank fusion."""

from __future__ import annotations

from app.retrieval.bm25 import BM25Retriever
from app.retrieval.dense import DenseRetriever, RetrievalResult
from app.retrieval.fusion import reciprocal_rank_fusion

DENSE_CANDIDATE_DEPTH = 20
BM25_CANDIDATE_DEPTH = 20
RRF_K = 60


class HybridRetriever:
    """Run fixed-depth dense and BM25 retrieval and fuse their rankings."""

    def __init__(
        self,
        dense_retriever: DenseRetriever,
        bm25_retriever: BM25Retriever,
        *,
        dense_candidate_depth: int = DENSE_CANDIDATE_DEPTH,
        bm25_candidate_depth: int = BM25_CANDIDATE_DEPTH,
        rrf_k: int = RRF_K,
    ) -> None:
        if dense_candidate_depth <= 0 or bm25_candidate_depth <= 0:
            raise ValueError("candidate depths must be greater than 0")
        if rrf_k <= 0:
            raise ValueError("rrf_k must be greater than 0")
        self._dense_retriever = dense_retriever
        self._bm25_retriever = bm25_retriever
        self.dense_candidate_depth = dense_candidate_depth
        self.bm25_candidate_depth = bm25_candidate_depth
        self.rrf_k = rrf_k

    def retrieve(self, query: str, top_k: int = 5) -> list[RetrievalResult]:
        """Return top-k RRF-fused chunks for a query."""
        if top_k <= 0:
            raise ValueError("top_k must be greater than 0")

        dense_results = self._dense_retriever.retrieve(
            query,
            top_k=self.dense_candidate_depth,
        )
        bm25_results = self._bm25_retriever.retrieve(
            query,
            top_k=self.bm25_candidate_depth,
        )
        return reciprocal_rank_fusion(
            [dense_results, bm25_results],
            rrf_k=self.rrf_k,
            top_k=top_k,
        )
