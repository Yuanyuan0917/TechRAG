"""Tests for cross-encoder reranking without model downloads."""

from __future__ import annotations

from typing import Sequence

import pytest

from app.ingestion.models import Chunk
from app.retrieval.dense import RetrievalResult
from app.retrieval.reranker import CrossEncoderReranker, RerankedRetriever


def _chunk(chunk_id: str, text: str, chunk_index: int) -> Chunk:
    return Chunk(
        id=chunk_id,
        document_id="doc_test",
        text=text,
        source="/documents/test.md",
        chunk_index=chunk_index,
        metadata={"file_type": "markdown"},
    )


def _candidate(chunk_id: str, text: str, rank: int) -> RetrievalResult:
    return RetrievalResult(
        chunk=_chunk(chunk_id, text, rank - 1),
        score=1.0 / (60 + rank),
    )


class FakeCrossEncoder:
    def __init__(self, scores_by_text: dict[str, float]) -> None:
        self.scores_by_text = scores_by_text
        self.calls: list[list[tuple[str, str]]] = []

    def predict(
        self,
        pairs: list[tuple[str, str]],
        show_progress_bar: bool,
    ) -> list[float]:
        assert show_progress_bar is False
        self.calls.append(pairs)
        return [self.scores_by_text[text] for _, text in pairs]


def test_reranker_reorders_candidates_and_preserves_provenance() -> None:
    candidates = [
        _candidate("chunk_a", "lower", 1),
        _candidate("chunk_b", "higher", 2),
    ]
    model = FakeCrossEncoder({"lower": 0.1, "higher": 0.9})
    reranker = CrossEncoderReranker(model=model)

    results = reranker.rerank("query", candidates, top_k=2)

    assert [result.chunk.id for result in results] == ["chunk_b", "chunk_a"]
    assert [result.rank for result in results] == [1, 2]
    assert results[0].reranker_score == 0.9
    assert results[0].hybrid_rank == 2
    assert results[0].hybrid_rrf_score == candidates[1].score
    assert results[0].chunk.metadata == {"file_type": "markdown"}
    assert model.calls == [[("query", "lower"), ("query", "higher")]]


def test_reranker_respects_top_k_and_is_deterministic() -> None:
    candidates = [
        _candidate("chunk_a", "alpha", 1),
        _candidate("chunk_b", "beta", 2),
    ]
    reranker = CrossEncoderReranker(
        model=FakeCrossEncoder({"alpha": 0.2, "beta": 0.8})
    )

    assert reranker.rerank("query", candidates, top_k=1) == reranker.rerank(
        "query", candidates, top_k=1
    )
    assert len(reranker.rerank("query", candidates, top_k=1)) == 1


def test_reranker_ties_use_hybrid_rank_then_chunk_id() -> None:
    candidates = [
        _candidate("chunk_b", "beta", 1),
        _candidate("chunk_a", "alpha", 2),
    ]
    reranker = CrossEncoderReranker(
        model=FakeCrossEncoder({"alpha": 0.5, "beta": 0.5})
    )

    results = reranker.rerank("query", candidates, top_k=2)

    assert [result.chunk.id for result in results] == ["chunk_b", "chunk_a"]


def test_reranker_handles_empty_candidates_without_loading_model() -> None:
    reranker = CrossEncoderReranker()

    assert reranker.rerank("query", [], top_k=10) == []
    assert reranker._model is None


@pytest.mark.parametrize("top_k", [0, -1])
def test_reranker_rejects_invalid_top_k(top_k: int) -> None:
    with pytest.raises(ValueError, match="top_k"):
        CrossEncoderReranker().rerank("query", [], top_k=top_k)


class FakeHybridRetriever:
    def __init__(self, candidates: Sequence[RetrievalResult]) -> None:
        self.candidates = list(candidates)
        self.calls: list[tuple[str, int]] = []

    def retrieve(self, query: str, top_k: int) -> list[RetrievalResult]:
        self.calls.append((query, top_k))
        return self.candidates[:top_k]


def test_reranked_retriever_uses_hybrid_candidates_and_removes_duplicates() -> None:
    first = _candidate("chunk_a", "alpha", 1)
    second = _candidate("chunk_b", "beta", 2)
    hybrid = FakeHybridRetriever([first, first, second])
    reranker = CrossEncoderReranker(
        model=FakeCrossEncoder({"alpha": 0.1, "beta": 0.9})
    )
    retriever = RerankedRetriever(hybrid, reranker, candidate_depth=20)

    results = retriever.retrieve("query", top_k=2)

    assert hybrid.calls == [("query", 20)]
    assert [result.chunk.id for result in results] == ["chunk_b", "chunk_a"]
    assert len({result.chunk.id for result in results}) == 2


def test_reranked_retriever_rejects_invalid_top_k() -> None:
    retriever = RerankedRetriever(
        FakeHybridRetriever([]),
        CrossEncoderReranker(model=FakeCrossEncoder({})),
    )

    with pytest.raises(ValueError, match="top_k"):
        retriever.retrieve("query", top_k=0)
