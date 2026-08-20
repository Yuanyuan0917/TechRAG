"""Data models for the TechRAG ingestion pipeline."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Document:
    """A source document loaded for ingestion."""

    id: str
    text: str
    source: str
    title: str | None = None
    metadata: dict[str, object] = field(default_factory=dict)


@dataclass
class Chunk:
    """A fixed-size slice of an ingested document."""

    id: str
    document_id: str
    text: str
    source: str
    chunk_index: int
    metadata: dict[str, object] = field(default_factory=dict)
