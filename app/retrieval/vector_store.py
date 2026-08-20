"""Local Qdrant vector storage for TechRAG chunks."""

from __future__ import annotations

import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from qdrant_client import QdrantClient, models

from app.config import QDRANT_COLLECTION_NAME, QDRANT_PATH
from app.ingestion.models import Chunk


@dataclass(frozen=True)
class VectorSearchResult:
    """A scored payload returned by Qdrant."""

    score: float
    payload: dict[str, object]


def _point_id(chunk_id: str) -> str:
    """Convert a stable chunk ID to a deterministic Qdrant-compatible UUID."""
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"techrag:chunk:{chunk_id}"))


class QdrantVectorStore:
    """Manage one local Qdrant collection for dense chunk vectors."""

    def __init__(
        self,
        path: Path = QDRANT_PATH,
        collection_name: str = QDRANT_COLLECTION_NAME,
    ) -> None:
        self.path = Path(path)
        self.collection_name = collection_name
        self._client = QdrantClient(path=str(self.path))

    def initialize_collection(self, vector_size: int, reset: bool = False) -> None:
        """Create the cosine collection, optionally replacing it explicitly."""
        if vector_size <= 0:
            raise ValueError("vector_size must be greater than 0")

        if reset and self.collection_exists():
            self._client.delete_collection(self.collection_name)

        if not self.collection_exists():
            self._client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(
                    size=vector_size,
                    distance=models.Distance.COSINE,
                ),
            )
            return

        vectors_config = self._client.get_collection(
            self.collection_name
        ).config.params.vectors
        if not isinstance(vectors_config, models.VectorParams):
            raise ValueError("Named vectors are not supported by this baseline")
        if vectors_config.size != vector_size:
            raise ValueError(
                f"Collection vector size is {vectors_config.size}, expected {vector_size}. "
                "Reset the collection explicitly before changing embedding models."
            )
        if vectors_config.distance != models.Distance.COSINE:
            raise ValueError("Existing collection does not use cosine similarity")

    def collection_exists(self) -> bool:
        """Return whether the configured collection exists."""
        return self._client.collection_exists(self.collection_name)

    def upsert(
        self,
        chunks: Sequence[Chunk],
        vectors: Sequence[Sequence[float]],
    ) -> int:
        """Insert or update chunks using deterministic point IDs."""
        if len(chunks) != len(vectors):
            raise ValueError("chunks and vectors must have the same length")
        if not chunks:
            return 0

        points = [
            models.PointStruct(
                id=_point_id(chunk.id),
                vector=[float(value) for value in vector],
                payload={
                    "chunk_id": chunk.id,
                    "document_id": chunk.document_id,
                    "text": chunk.text,
                    "source": chunk.source,
                    "chunk_index": chunk.chunk_index,
                    "metadata": chunk.metadata,
                },
            )
            for chunk, vector in zip(chunks, vectors)
        ]
        self._client.upsert(
            collection_name=self.collection_name,
            points=points,
            wait=True,
        )
        return len(points)

    def search(
        self,
        query_vector: Sequence[float],
        limit: int,
    ) -> list[VectorSearchResult]:
        """Search the collection and return ranked payloads with scores."""
        if limit <= 0:
            raise ValueError("limit must be greater than 0")

        response = self._client.query_points(
            collection_name=self.collection_name,
            query=[float(value) for value in query_vector],
            limit=limit,
            with_payload=True,
            with_vectors=False,
        )
        return [
            VectorSearchResult(
                score=float(point.score),
                payload=dict(point.payload or {}),
            )
            for point in response.points
        ]

    def count(self) -> int:
        """Return the number of indexed points."""
        return self._client.count(self.collection_name, exact=True).count

    def close(self) -> None:
        """Close the local Qdrant client."""
        self._client.close()
