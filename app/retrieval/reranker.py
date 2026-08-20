"""Cross-encoder reranking for a fixed Hybrid candidate set."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Sequence

from app.config import RERANKER_MODEL_NAME
from app.ingestion.models import Chunk
from app.retrieval.dense import RetrievalResult

RERANKER_CANDIDATE_DEPTH = 20


@dataclass(frozen=True)
class RerankedResult:
    """A reranked chunk with separate cross-encoder and Hybrid scores."""

    chunk: Chunk
    reranker_score: float
    rank: int
    hybrid_rank: int
    hybrid_rrf_score: float


class CrossEncoderReranker:
    """Lazily load one CrossEncoder and score query-passage pairs in a batch."""

    def __init__(
        self,
        model_name: str = RERANKER_MODEL_NAME,
        model: Any | None = None,
    ) -> None:
        self.model_name = model_name
        self._model = model

    def _get_model(self) -> Any:
        if self._model is None:
            from sentence_transformers import CrossEncoder

            self._model = CrossEncoder(self.model_name)
        return self._model

    def rerank(
        self,
        query: str,
        candidates: Sequence[RetrievalResult],
        top_k: int = 10,
    ) -> list[RerankedResult]:
        """Score and deterministically rerank unique Hybrid candidates."""
        if top_k <= 0:
            raise ValueError("top_k must be greater than 0")
        if not candidates:
            return []

        unique_candidates: list[tuple[int, RetrievalResult]] = []
        seen: set[str] = set()
        for hybrid_rank, candidate in enumerate(candidates, start=1):
            if candidate.chunk.id in seen:
                continue
            seen.add(candidate.chunk.id)
            unique_candidates.append((hybrid_rank, candidate))

        pairs = [(query, candidate.chunk.text) for _, candidate in unique_candidates]
        raw_scores = self._get_model().predict(pairs, show_progress_bar=False)
        scores = [float(score) for score in raw_scores]
        if len(scores) != len(unique_candidates):
            raise ValueError("CrossEncoder returned an unexpected number of scores")

        scored = [
            (
                score,
                hybrid_rank,
                candidate,
            )
            for score, (hybrid_rank, candidate) in zip(scores, unique_candidates)
        ]
        scored.sort(key=lambda item: (-item[0], item[1], item[2].chunk.id))
        return [
            RerankedResult(
                chunk=candidate.chunk,
                reranker_score=score,
                rank=rank,
                hybrid_rank=hybrid_rank,
                hybrid_rrf_score=candidate.score,
            )
            for rank, (score, hybrid_rank, candidate) in enumerate(
                scored[:top_k],
                start=1,
            )
        ]


class RerankedRetriever:
    """Retrieve Hybrid candidates and rerank only that fixed candidate set."""

    def __init__(
        self,
        hybrid_retriever: Any,
        reranker: CrossEncoderReranker,
        candidate_depth: int = RERANKER_CANDIDATE_DEPTH,
    ) -> None:
        if candidate_depth <= 0:
            raise ValueError("candidate_depth must be greater than 0")
        self._hybrid_retriever = hybrid_retriever
        self.reranker = reranker
        self.candidate_depth = candidate_depth

    def retrieve(self, query: str, top_k: int = 10) -> list[RerankedResult]:
        """Return cross-encoder-ranked results from Hybrid top-20 candidates."""
        if top_k <= 0:
            raise ValueError("top_k must be greater than 0")
        candidates = self.retrieve_candidates(query)
        return self.reranker.rerank(query, candidates, top_k=top_k)

    def retrieve_candidates(self, query: str) -> list[RetrievalResult]:
        """Return the fixed-depth Hybrid candidate ranking."""
        return self._hybrid_retriever.retrieve(query, top_k=self.candidate_depth)
