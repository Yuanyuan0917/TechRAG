"""Document chunking utilities for TechRAG."""

from __future__ import annotations

import hashlib

from app.ingestion.models import Chunk, Document


def _chunk_id(
    document_id: str,
    chunk_index: int,
    chunk_size: int,
    chunk_overlap: int,
) -> str:
    """Build a deterministic identifier for a chunking configuration."""
    identifier = f"{document_id}:{chunk_index}:{chunk_size}:{chunk_overlap}"
    digest = hashlib.sha256(identifier.encode("utf-8")).hexdigest()
    return f"chunk_{digest}"


def chunk_document(
    document: Document,
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
) -> list[Chunk]:
    """Split a document into fixed-size character chunks with overlap."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")
    if chunk_overlap < 0:
        raise ValueError("chunk_overlap must be greater than or equal to 0")
    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be smaller than chunk_size")

    chunks: list[Chunk] = []
    step = chunk_size - chunk_overlap

    for start in range(0, len(document.text), step):
        text = document.text[start : start + chunk_size]
        if not text:
            continue

        chunk_index = len(chunks)
        metadata = dict(document.metadata)
        metadata.update(
            {
                "document_id": document.id,
                "source": document.source,
                "chunk_index": chunk_index,
            }
        )
        chunks.append(
            Chunk(
                id=_chunk_id(
                    document.id,
                    chunk_index,
                    chunk_size,
                    chunk_overlap,
                ),
                document_id=document.id,
                text=text,
                source=document.source,
                chunk_index=chunk_index,
                metadata=metadata,
            )
        )

        if start + chunk_size >= len(document.text):
            break

    return chunks
