"""Tests for retrieval metrics and evaluation data validation."""

from __future__ import annotations

import math

import pytest

from app.evaluation.metrics import (
    mean_reciprocal_rank,
    ndcg_at_k,
    recall_at_k,
    reciprocal_rank,
)


def test_recall_at_k_perfect_ranking() -> None:
    assert recall_at_k(["a", "b"], {"a", "b"}, 2) == 1.0


def test_recall_at_k_handles_multiple_relevant_and_k_bounds() -> None:
    ranking = ["x", "a", "b"]

    assert recall_at_k(ranking, {"a", "b"}, 1) == 0.0
    assert recall_at_k(ranking, {"a", "b"}, 2) == 0.5
    assert recall_at_k(ranking, {"a", "b"}, 10) == 1.0


def test_recall_at_k_returns_zero_without_hits_or_relevant_items() -> None:
    assert recall_at_k(["x"], {"a"}, 5) == 0.0
    assert recall_at_k(["x"], set(), 5) == 0.0


@pytest.mark.parametrize("k", [0, -1])
def test_metrics_reject_invalid_k(k: int) -> None:
    with pytest.raises(ValueError, match="k"):
        recall_at_k(["a"], {"a"}, k)
    with pytest.raises(ValueError, match="k"):
        ndcg_at_k(["a"], {"a": 1}, k)


def test_reciprocal_rank_uses_first_relevant_rank() -> None:
    assert reciprocal_rank(["x", "y", "a", "b"], {"a", "b"}) == 1 / 3
    assert reciprocal_rank(["x"], {"a"}) == 0.0


def test_mean_reciprocal_rank_matches_expected_mean() -> None:
    rankings = [["a"], ["x", "b"], ["x"]]
    relevant = [{"a"}, {"b"}, {"c"}]

    assert mean_reciprocal_rank(rankings, relevant) == 0.5


def test_mean_reciprocal_rank_requires_aligned_inputs() -> None:
    with pytest.raises(ValueError, match="same length"):
        mean_reciprocal_rank([["a"]], [])


def test_ndcg_perfect_graded_ranking_is_one() -> None:
    assert ndcg_at_k(["high", "partial"], {"high": 2, "partial": 1}, 2) == 1.0


def test_ndcg_degraded_ordering_is_lower() -> None:
    relevance = {"high": 2, "partial": 1}
    perfect = ndcg_at_k(["high", "partial"], relevance, 2)
    degraded = ndcg_at_k(["partial", "high"], relevance, 2)

    assert degraded < perfect
    assert degraded == pytest.approx(
        (1 + 3 / math.log2(3)) / (3 + 1 / math.log2(3))
    )


def test_ndcg_handles_no_hits_empty_relevance_and_duplicate_ids() -> None:
    assert ndcg_at_k(["x"], {"a": 2}, 5) == 0.0
    assert ndcg_at_k(["a"], {}, 5) == 0.0
    assert ndcg_at_k(["a", "a"], {"a": 2}, 2) == 1.0
