"""In-process BM25 retrieval over TechRAG chunks."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Sequence

from rank_bm25 import BM25Okapi

from app.ingestion.models import Chunk

TOKENIZER_DESCRIPTION = "casefold + regex [a-z0-9_]+"
_TOKEN_PATTERN = re.compile(r"[a-z0-9_]+")


def tokenize(text: str) -> list[str]:
    """Tokenize English technical text deterministically."""
    return _TOKEN_PATTERN.findall(text.casefold())


@dataclass(frozen=True)
class BM25Result:
    """A BM25-ranked chunk with its lexical score and one-based rank."""

    chunk: Chunk
    score: float
    rank: int


class BM25Retriever:
    """Build and query a BM25 index over an immutable chunk sequence."""

    def __init__(self, chunks: Sequence[Chunk]) -> None:
        self._chunks = list(chunks)
        chunk_ids = [chunk.id for chunk in self._chunks]
        if len(chunk_ids) != len(set(chunk_ids)):
            raise ValueError("BM25 corpus contains duplicate chunk IDs")
        self.chunk_ids = frozenset(chunk_ids)
        tokenized_corpus = [tokenize(chunk.text) for chunk in self._chunks]
        self._index = BM25Okapi(tokenized_corpus) if tokenized_corpus else None

    def retrieve(self, query: str, top_k: int = 5) -> list[BM25Result]:
        """Return deterministic top-k BM25 results."""
        if top_k <= 0:
            raise ValueError("top_k must be greater than 0")
        if self._index is None:
            return []

        scores = self._index.get_scores(tokenize(query))
        ranked = sorted(
            zip(self._chunks, scores),
            key=lambda item: (-float(item[1]), item[0].id),
        )[:top_k]
        return [
            BM25Result(chunk=chunk, score=float(score), rank=rank)
            for rank, (chunk, score) in enumerate(ranked, start=1)
        ]
