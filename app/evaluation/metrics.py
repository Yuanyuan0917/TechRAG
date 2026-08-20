"""Pure ranking metrics for retrieval evaluation."""

from __future__ import annotations

import math
from collections.abc import Collection, Mapping, Sequence


def _validate_k(k: int) -> None:
    if k <= 0:
        raise ValueError("k must be greater than 0")


def recall_at_k(
    retrieved_ids: Sequence[str],
    relevant_ids: Collection[str],
    k: int,
) -> float:
    """Return the fraction of all relevant IDs found in the first k ranks."""
    _validate_k(k)
    relevant = set(relevant_ids)
    if not relevant:
        return 0.0
    retrieved = set(retrieved_ids[:k])
    return len(retrieved & relevant) / len(relevant)


def reciprocal_rank(
    retrieved_ids: Sequence[str],
    relevant_ids: Collection[str],
) -> float:
    """Return the reciprocal rank of the first relevant retrieved ID."""
    relevant = set(relevant_ids)
    if not relevant:
        return 0.0
    for rank, chunk_id in enumerate(retrieved_ids, start=1):
        if chunk_id in relevant:
            return 1.0 / rank
    return 0.0


def mean_reciprocal_rank(
    rankings: Sequence[Sequence[str]],
    relevant_sets: Sequence[Collection[str]],
) -> float:
    """Return mean reciprocal rank across aligned query rankings."""
    if len(rankings) != len(relevant_sets):
        raise ValueError("rankings and relevant_sets must have the same length")
    if not rankings:
        return 0.0
    return sum(
        reciprocal_rank(ranking, relevant)
        for ranking, relevant in zip(rankings, relevant_sets)
    ) / len(rankings)


def ndcg_at_k(
    retrieved_ids: Sequence[str],
    relevance: Mapping[str, int],
    k: int,
) -> float:
    """Return graded nDCG@k using gain 2**relevance - 1."""
    _validate_k(k)
    positive_relevance = {
        chunk_id: grade
        for chunk_id, grade in relevance.items()
        if grade > 0
    }
    if not positive_relevance:
        return 0.0

    seen: set[str] = set()
    dcg = 0.0
    for rank, chunk_id in enumerate(retrieved_ids[:k], start=1):
        if chunk_id in seen:
            grade = 0
        else:
            seen.add(chunk_id)
            grade = positive_relevance.get(chunk_id, 0)
        dcg += (2**grade - 1) / math.log2(rank + 1)

    ideal_grades = sorted(positive_relevance.values(), reverse=True)[:k]
    idcg = sum(
        (2**grade - 1) / math.log2(rank + 1)
        for rank, grade in enumerate(ideal_grades, start=1)
    )
    return dcg / idcg if idcg else 0.0
