"""FastAPI request and response schemas for TechRAG queries."""

from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, Field, field_validator

RetrievalStrategy = Literal["dense", "hybrid", "reranked"]


class QueryRequest(BaseModel):
    """A single stateless TechRAG query."""

    question: str = Field(max_length=2_000)
    strategy: RetrievalStrategy = "reranked"
    generate_answer: bool = True
    top_k: int = Field(default=5, ge=1, le=10)

    @field_validator("question")
    @classmethod
    def question_must_not_be_blank(cls, value: str) -> str:
        """Reject blank input while preserving the user's original wording."""
        if not value.strip():
            raise ValueError("question must not be empty")
        return value


class HealthResponse(BaseModel):
    """Lightweight process health response."""

    status: Literal["ok"] = "ok"


class CitationResponse(BaseModel):
    """One validated citation and its display provenance."""

    label: str
    chunk_id: str
    document_id: str
    source: str
    chunk_index: int
    preview: str


class RetrievedChunkResponse(BaseModel):
    """One ranked retrieval result without its embedding vector."""

    rank: int
    chunk_id: str
    document_id: str
    source: str
    chunk_index: int
    score: float
    score_type: Literal["cosine", "rrf", "cross_encoder"]
    preview: str
    hybrid_rank: Optional[int] = None
    hybrid_rrf_score: Optional[float] = None


class QueryResponse(BaseModel):
    """A retrieval-only or grounded-generation response."""

    question: str
    strategy: RetrievalStrategy
    answer: Optional[str]
    citations: list[CitationResponse]
    invalid_citation_labels: list[str]
    retrieved_chunks: list[RetrievedChunkResponse]
    latency_ms: float = Field(ge=0)
