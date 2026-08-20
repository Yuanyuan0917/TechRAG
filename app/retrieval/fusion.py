"""Rank-based fusion for retrieval results."""

from __future__ import annotations

from typing import Sequence, Union

from app.ingestion.models import Chunk
from app.retrieval.bm25 import BM25Result
from app.retrieval.dense import RetrievalResult

RankedResult = Union[RetrievalResult, BM25Result]


def reciprocal_rank_fusion(
    rankings: Sequence[Sequence[RankedResult]],
    *,
    rrf_k: int = 60,
    top_k: int | None = None,
) -> list[RetrievalResult]:
    """Fuse rankings by chunk ID using RRF and chunk-ID tie-breaking."""
    if rrf_k <= 0:
        raise ValueError("rrf_k must be greater than 0")
    if top_k is not None and top_k <= 0:
        raise ValueError("top_k must be greater than 0")

    scores: dict[str, float] = {}
    chunks: dict[str, Chunk] = {}
    for ranking in rankings:
        seen_in_ranking: set[str] = set()
        unique_rank = 0
        for result in ranking:
            chunk_id = result.chunk.id
            if chunk_id in seen_in_ranking:
                continue
            seen_in_ranking.add(chunk_id)
            unique_rank += 1
            existing = chunks.get(chunk_id)
            if existing is not None and existing != result.chunk:
                raise ValueError(f"Conflicting chunks share ID: {chunk_id}")
            chunks[chunk_id] = result.chunk
            scores[chunk_id] = scores.get(chunk_id, 0.0) + 1.0 / (
                rrf_k + unique_rank
            )

    fused = [
        RetrievalResult(chunk=chunks[chunk_id], score=score)
        for chunk_id, score in scores.items()
    ]
    fused.sort(key=lambda result: (-result.score, result.chunk.id))
    return fused if top_k is None else fused[:top_k]
