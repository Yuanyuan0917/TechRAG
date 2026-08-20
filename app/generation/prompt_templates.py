"""Grounded prompt construction for TechRAG answer generation."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from app.ingestion.models import Chunk


@dataclass(frozen=True)
class LabeledContext:
    """A retrieved chunk with its prompt-local citation label."""

    label: str
    chunk: Chunk


def label_contexts(chunks: Sequence[Chunk]) -> list[LabeledContext]:
    """Assign deterministic citation labels in retrieval order."""
    return [
        LabeledContext(label=f"[C{index}]", chunk=chunk)
        for index, chunk in enumerate(chunks, start=1)
    ]


def build_generation_messages(
    question: str,
    contexts: Sequence[LabeledContext],
) -> list[dict[str, str]]:
    """Build strict grounding instructions and labeled context messages."""
    if not question.strip():
        raise ValueError("question must not be empty")

    if contexts:
        context_text = "\n\n".join(
            (
                f"{context.label}\n"
                f"Source: {Path(context.chunk.source).name}\n"
                f"Chunk ID: {context.chunk.id}\n"
                f"Text:\n{context.chunk.text}"
            )
            for context in contexts
        )
    else:
        context_text = "No documentation context was retrieved."

    system_message = (
        "You answer questions about technical documentation. Answer only from the "
        "provided context. Do not add unsupported claims. Cite every supported claim "
        "with the exact context labels provided, such as [C1] or [C1][C3]. Never "
        "invent, alter, or cite a label that is not in the context. If the context "
        "does not support a reliable answer, respond: 'The provided documentation "
        "does not contain enough information to answer this reliably.' Keep the "
        "answer concise and technical."
    )
    user_message = f"Documentation context:\n\n{context_text}\n\nQuestion:\n{question}"
    return [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ]
