"""Dense retrieval over indexed TechRAG chunks."""

from __future__ import annotations

from dataclasses import dataclass

from app.ingestion.models import Chunk
from app.retrieval.embedder import SentenceTransformerEmbedder
from app.retrieval.vector_store import QdrantVectorStore, VectorSearchResult


@dataclass(frozen=True)
class RetrievalResult:
    """A ranked chunk and its cosine similarity score."""

    chunk: Chunk
    score: float


def _chunk_from_result(result: VectorSearchResult) -> Chunk:
    payload = result.payload
    metadata = payload.get("metadata", {})
    if not isinstance(metadata, dict):
        raise ValueError("Stored chunk metadata must be a dictionary")

    return Chunk(
        id=str(payload["chunk_id"]),
        document_id=str(payload["document_id"]),
        text=str(payload["text"]),
        source=str(payload["source"]),
        chunk_index=int(payload["chunk_index"]),
        metadata=dict(metadata),
    )


class DenseRetriever:
    """Embed queries and retrieve ranked chunks from Qdrant."""

    def __init__(
        self,
        embedder: SentenceTransformerEmbedder,
        vector_store: QdrantVectorStore,
    ) -> None:
        self._embedder = embedder
        self._vector_store = vector_store

    def retrieve(self, query: str, top_k: int = 5) -> list[RetrievalResult]:
        """Return the top-k chunks for a query in descending score order."""
        if top_k <= 0:
            raise ValueError("top_k must be greater than 0")

        query_vector = self._embedder.embed_query(query)
        results = self._vector_store.search(query_vector, limit=top_k)
        return [
            RetrievalResult(chunk=_chunk_from_result(result), score=result.score)
            for result in results
        ]
