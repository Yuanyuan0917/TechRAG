"""Embedded or server-based Qdrant storage for TechRAG chunks."""

from __future__ import annotations

import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from qdrant_client import QdrantClient, models

from app.config import QDRANT_COLLECTION_NAME, QDRANT_PATH, QDRANT_URL
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
    """Manage one Qdrant collection, using embedded storage unless a URL is set."""

    def __init__(
        self,
        path: Path | None = None,
        collection_name: str = QDRANT_COLLECTION_NAME,
        *,
        url: str | None = None,
    ) -> None:
        # An explicit path must keep native callers/tests isolated from a server
        # configured for other application processes in the same environment.
        if path is None and url is None:
            url = QDRANT_URL
        self.path = Path(path) if path is not None else QDRANT_PATH
        self.collection_name = collection_name
        self._client = (
            QdrantClient(url=url, timeout=10.0)
            if url
            else QdrantClient(path=str(self.path))
        )

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

    def chunk_ids(self) -> frozenset[str]:
        """Read stored chunk IDs to detect a stale or differently rooted corpus."""
        chunk_ids: set[str] = set()
        offset = None
        while True:
            points, offset = self._client.scroll(
                collection_name=self.collection_name,
                limit=256,
                offset=offset,
                with_payload=["chunk_id"],
                with_vectors=False,
            )
            for point in points:
                chunk_id = (point.payload or {}).get("chunk_id")
                if not isinstance(chunk_id, str):
                    raise ValueError("Indexed point is missing a valid chunk_id")
                chunk_ids.add(chunk_id)
            if offset is None:
                return frozenset(chunk_ids)

    def close(self) -> None:
        """Close the Qdrant client."""
        self._client.close()
