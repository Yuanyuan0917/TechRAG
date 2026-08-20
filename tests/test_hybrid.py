"""Tests for BM25 retrieval, RRF, and hybrid orchestration."""

from __future__ import annotations

import pytest

from app.ingestion.models import Chunk
from app.retrieval.bm25 import BM25Result, BM25Retriever, tokenize
from app.retrieval.dense import RetrievalResult
from app.retrieval.fusion import reciprocal_rank_fusion
from app.retrieval.hybrid import HybridRetriever


def _chunk(chunk_id: str, text: str, chunk_index: int) -> Chunk:
    return Chunk(
        id=chunk_id,
        document_id="doc_test",
        text=text,
        source="/documents/test.md",
        chunk_index=chunk_index,
        metadata={"file_type": "markdown"},
    )


def _dense_result(chunk: Chunk, score: float = 1.0) -> RetrievalResult:
    return RetrievalResult(chunk=chunk, score=score)


def _bm25_result(chunk: Chunk, rank: int, score: float = 1.0) -> BM25Result:
    return BM25Result(chunk=chunk, score=score, rank=rank)


def test_tokenizer_is_case_insensitive_and_preserves_underscores() -> None:
    assert tokenize("Use SCORE_threshold, then Match-Any!") == [
        "use",
        "score_threshold",
        "then",
        "match",
        "any",
    ]


def test_bm25_indexes_chunks_and_ranks_lexical_match_with_provenance() -> None:
    chunks = [
        _chunk("chunk_a", "cosine vector similarity", 0),
        _chunk("chunk_b", "score_threshold filters search results", 1),
        _chunk("chunk_c", "dependency injection tutorial", 2),
    ]
    retriever = BM25Retriever(chunks)

    results = retriever.retrieve("How does score_threshold work?", top_k=1)

    assert retriever.chunk_ids == {"chunk_a", "chunk_b", "chunk_c"}
    assert len(results) == 1
    assert results[0].chunk == chunks[1]
    assert results[0].rank == 1
    assert results[0].chunk.metadata == {"file_type": "markdown"}


def test_bm25_is_deterministic_across_repeated_construction() -> None:
    chunks = [
        _chunk("chunk_b", "alpha beta", 1),
        _chunk("chunk_a", "alpha gamma", 0),
        _chunk("chunk_c", "delta", 2),
    ]

    first = BM25Retriever(chunks).retrieve("alpha", top_k=3)
    second = BM25Retriever(chunks).retrieve("alpha", top_k=3)

    assert [(result.chunk.id, result.score) for result in first] == [
        (result.chunk.id, result.score) for result in second
    ]


@pytest.mark.parametrize("top_k", [0, -1])
def test_bm25_rejects_invalid_top_k(top_k: int) -> None:
    retriever = BM25Retriever([_chunk("chunk_a", "alpha", 0)])

    with pytest.raises(ValueError, match="top_k"):
        retriever.retrieve("alpha", top_k=top_k)


def test_rrf_identical_rankings_have_expected_scores() -> None:
    first = _chunk("chunk_a", "alpha", 0)
    second = _chunk("chunk_b", "beta", 1)
    ranking = [_dense_result(first), _dense_result(second)]

    fused = reciprocal_rank_fusion([ranking, ranking], rrf_k=60)

    assert [result.chunk.id for result in fused] == ["chunk_a", "chunk_b"]
    assert fused[0].score == pytest.approx(2 / 61)
    assert fused[1].score == pytest.approx(2 / 62)


def test_rrf_handles_disjoint_and_single_ranking_results_with_stable_ties() -> None:
    first = _chunk("chunk_b", "beta", 1)
    second = _chunk("chunk_a", "alpha", 0)

    fused = reciprocal_rank_fusion(
        [[_dense_result(first)], [_bm25_result(second, rank=1)]],
        rrf_k=60,
    )

    assert [result.chunk.id for result in fused] == ["chunk_a", "chunk_b"]
    assert fused[0].score == fused[1].score == pytest.approx(1 / 61)


def test_rrf_combines_overlap_and_ignores_duplicate_ids_per_ranking() -> None:
    first = _chunk("chunk_a", "alpha", 0)
    second = _chunk("chunk_b", "beta", 1)
    fused = reciprocal_rank_fusion(
        [
            [_dense_result(first), _dense_result(first), _dense_result(second)],
            [_bm25_result(second, rank=1)],
        ],
        rrf_k=10,
    )

    assert [result.chunk.id for result in fused] == ["chunk_b", "chunk_a"]
    assert fused[0].score == pytest.approx(1 / 12 + 1 / 11)
    assert fused[1].score == pytest.approx(1 / 11)


@pytest.mark.parametrize(
    ("rrf_k", "top_k"),
    [(0, None), (-1, None), (60, 0), (60, -1)],
)
def test_rrf_rejects_invalid_configuration(rrf_k: int, top_k: int | None) -> None:
    with pytest.raises(ValueError):
        reciprocal_rank_fusion([], rrf_k=rrf_k, top_k=top_k)


class FakeRetriever:
    def __init__(self, results: list[RetrievalResult] | list[BM25Result]) -> None:
        self.results = results
        self.calls: list[tuple[str, int]] = []

    def retrieve(
        self,
        query: str,
        top_k: int,
    ) -> list[RetrievalResult] | list[BM25Result]:
        self.calls.append((query, top_k))
        return self.results[:top_k]


def test_hybrid_fuses_results_without_duplicates_and_preserves_provenance() -> None:
    first = _chunk("chunk_a", "alpha", 0)
    second = _chunk("chunk_b", "beta", 1)
    third = _chunk("chunk_c", "gamma", 2)
    dense = FakeRetriever([_dense_result(first), _dense_result(second)])
    bm25 = FakeRetriever(
        [_bm25_result(second, rank=1), _bm25_result(third, rank=2)]
    )
    retriever = HybridRetriever(  # type: ignore[arg-type]
        dense,
        bm25,
        dense_candidate_depth=2,
        bm25_candidate_depth=2,
        rrf_k=60,
    )

    first_run = retriever.retrieve("query", top_k=2)
    second_run = retriever.retrieve("query", top_k=2)

    assert [result.chunk.id for result in first_run] == ["chunk_b", "chunk_a"]
    assert first_run == second_run
    assert len({result.chunk.id for result in first_run}) == 2
    assert first_run[0].chunk == second
    assert dense.calls == [("query", 2), ("query", 2)]
    assert bm25.calls == [("query", 2), ("query", 2)]


def test_hybrid_rejects_invalid_top_k() -> None:
    retriever = HybridRetriever(  # type: ignore[arg-type]
        FakeRetriever([]),
        FakeRetriever([]),
    )

    with pytest.raises(ValueError, match="top_k"):
        retriever.retrieve("query", top_k=0)
