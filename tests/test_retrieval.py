"""Tests for the TechRAG dense retrieval baseline."""

from pathlib import Path
from typing import Any

import pytest

from app.ingestion.models import Chunk
from app.retrieval.dense import DenseRetriever
from app.retrieval.embedder import SentenceTransformerEmbedder
from app.retrieval.vector_store import QdrantVectorStore


class FakeSentenceTransformer:
    """Small deterministic stand-in for SentenceTransformer."""

    def __init__(self) -> None:
        self.eval_calls = 0
        self.encode_calls: list[dict[str, object]] = []

    def eval(self) -> None:
        self.eval_calls += 1

    def get_sentence_embedding_dimension(self) -> int:
        return 2

    def encode(self, texts: list[str], **kwargs: object) -> list[list[float]]:
        self.encode_calls.append({"texts": texts, **kwargs})
        return [[float(len(text)), float(text.count("a"))] for text in texts]


def _chunk(chunk_id: str, text: str, chunk_index: int) -> Chunk:
    return Chunk(
        id=chunk_id,
        document_id="doc_test",
        text=text,
        source="/documents/test.md",
        chunk_index=chunk_index,
        metadata={"file_type": "markdown"},
    )


def _store(path: Path) -> QdrantVectorStore:
    store = QdrantVectorStore(path=path)
    store.initialize_collection(vector_size=2)
    return store


def test_embedder_interface_and_shapes_without_model_download() -> None:
    model = FakeSentenceTransformer()
    embedder = SentenceTransformerEmbedder(model=model)

    assert embedder.vector_size == 2
    assert embedder.embed_texts(["a", "abcd"]) == [[1.0, 1.0], [4.0, 1.0]]
    assert embedder.embed_query("query") == [5.0, 0.0]
    assert embedder.embed_texts([]) == []
    assert model.eval_calls == 1
    assert model.encode_calls[0]["normalize_embeddings"] is False


def test_collection_initialization_and_repeated_upsert_are_idempotent(
    tmp_path: Path,
) -> None:
    store = _store(tmp_path / "qdrant")
    chunks = [_chunk("chunk_a", "alpha", 0), _chunk("chunk_b", "beta", 1)]
    vectors = [[1.0, 0.0], [0.0, 1.0]]
    try:
        assert store.collection_exists()
        assert store.upsert(chunks, vectors) == 2
        assert store.upsert(chunks, vectors) == 2
        assert store.count() == 2
    finally:
        store.close()


def test_search_is_ranked_and_payload_survives_round_trip(tmp_path: Path) -> None:
    store = _store(tmp_path / "qdrant")
    chunks = [_chunk("chunk_a", "alpha", 0), _chunk("chunk_b", "beta", 1)]
    try:
        store.upsert(chunks, [[1.0, 0.0], [0.0, 1.0]])
        results = store.search([1.0, 0.0], limit=2)

        assert [result.payload["chunk_id"] for result in results] == [
            "chunk_a",
            "chunk_b",
        ]
        assert results[0].score > results[1].score
        assert results[0].payload == {
            "chunk_id": "chunk_a",
            "document_id": "doc_test",
            "text": "alpha",
            "source": "/documents/test.md",
            "chunk_index": 0,
            "metadata": {"file_type": "markdown"},
        }
    finally:
        store.close()


class FakeEmbedder:
    def embed_query(self, query: str) -> list[float]:
        return [1.0, 0.0]


def test_dense_retriever_returns_ranked_chunks_and_respects_top_k(
    tmp_path: Path,
) -> None:
    store = _store(tmp_path / "qdrant")
    chunks = [_chunk("chunk_a", "alpha", 0), _chunk("chunk_b", "beta", 1)]
    try:
        store.upsert(chunks, [[1.0, 0.0], [0.0, 1.0]])
        retriever = DenseRetriever(FakeEmbedder(), store)  # type: ignore[arg-type]

        results = retriever.retrieve("alpha question", top_k=1)

        assert len(results) == 1
        assert results[0].chunk == chunks[0]
        assert isinstance(results[0].score, float)
    finally:
        store.close()


@pytest.mark.parametrize("top_k", [0, -1])
def test_dense_retriever_rejects_invalid_top_k(top_k: int) -> None:
    retriever = DenseRetriever(FakeEmbedder(), None)  # type: ignore[arg-type]

    with pytest.raises(ValueError, match="top_k"):
        retriever.retrieve("query", top_k=top_k)
