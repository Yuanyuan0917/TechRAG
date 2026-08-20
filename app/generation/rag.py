"""Explicit retrieval-to-answer orchestration with validated citations."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from app.config import GENERATION_CONTEXT_TOP_K
from app.generation.citations import parse_citation_labels
from app.generation.prompt_templates import (
    LabeledContext,
    build_generation_messages,
    label_contexts,
)
from app.retrieval.reranker import RerankedResult


@dataclass(frozen=True)
class Citation:
    """Validated provenance for one citation label."""

    label: str
    chunk_id: str
    document_id: str
    source: str
    chunk_index: int


@dataclass(frozen=True)
class GeneratedAnswer:
    """An LLM answer and provenance derived from retrieved context."""

    answer: str
    citations: tuple[Citation, ...]
    invalid_citation_labels: tuple[str, ...]
    retrieved_chunks: tuple[RerankedResult, ...]
    contexts: tuple[LabeledContext, ...]


class RAGPipeline:
    """Retrieve top contexts, generate an answer, and validate citations."""

    def __init__(
        self,
        retriever: Any,
        llm_client: Any,
        context_top_k: int = GENERATION_CONTEXT_TOP_K,
    ) -> None:
        if context_top_k <= 0:
            raise ValueError("context_top_k must be greater than 0")
        self._retriever = retriever
        self._llm_client = llm_client
        self.context_top_k = context_top_k

    def answer(self, question: str) -> GeneratedAnswer:
        """Generate a grounded answer from reranked top-k context chunks."""
        if not question.strip():
            raise ValueError("question must not be empty")
        retrieved = self._retriever.retrieve(question, top_k=self.context_top_k)
        contexts = label_contexts([result.chunk for result in retrieved])
        messages = build_generation_messages(question, contexts)
        answer = self._llm_client.generate(messages)

        context_by_label = {context.label: context for context in contexts}
        parsed = parse_citation_labels(answer, context_by_label)
        citations = tuple(
            Citation(
                label=label,
                chunk_id=context_by_label[label].chunk.id,
                document_id=context_by_label[label].chunk.document_id,
                source=context_by_label[label].chunk.source,
                chunk_index=context_by_label[label].chunk.chunk_index,
            )
            for label in parsed.valid_labels
        )
        return GeneratedAnswer(
            answer=answer,
            citations=citations,
            invalid_citation_labels=parsed.invalid_labels,
            retrieved_chunks=tuple(retrieved),
            contexts=tuple(contexts),
        )
