"""Tests for TechRAG document chunking."""

import pytest


from app.ingestion.chunker import chunk_document
from app.ingestion.models import Document


def _document(text: str) -> Document:
    return Document(
        id="doc_test",
        text=text,
        source="/documents/test.md",
        title="Test",
        metadata={"file_type": "markdown"},
    )


def test_short_document_produces_one_chunk() -> None:
    chunks = chunk_document(_document("short text"), chunk_size=20, chunk_overlap=5)

    assert len(chunks) == 1
    assert chunks[0].text == "short text"


def test_long_document_produces_overlapping_chunks_in_order() -> None:
    chunks = chunk_document(_document("abcdefghij"), chunk_size=6, chunk_overlap=2)

    assert [chunk.text for chunk in chunks] == ["abcdef", "efghij"]
    assert chunks[0].text[-2:] == chunks[1].text[:2]
    assert [chunk.chunk_index for chunk in chunks] == [0, 1]


def test_chunk_provenance_is_preserved() -> None:
    chunk = chunk_document(_document("content"), chunk_size=10, chunk_overlap=0)[0]

    assert chunk.document_id == "doc_test"
    assert chunk.source == "/documents/test.md"
    assert chunk.metadata == {
        "file_type": "markdown",
        "document_id": "doc_test",
        "source": "/documents/test.md",
        "chunk_index": 0,
    }


def test_chunk_ids_are_deterministic() -> None:
    document = _document("abcdefghij")

    first = chunk_document(document, chunk_size=6, chunk_overlap=2)
    second = chunk_document(document, chunk_size=6, chunk_overlap=2)

    assert [chunk.id for chunk in first] == [chunk.id for chunk in second]


@pytest.mark.parametrize("chunk_size", [0, -1])
def test_invalid_chunk_size_raises(chunk_size: int) -> None:
    with pytest.raises(ValueError, match="chunk_size"):
        chunk_document(_document("text"), chunk_size=chunk_size, chunk_overlap=0)


@pytest.mark.parametrize("chunk_overlap", [-1, 5, 6])
def test_invalid_overlap_raises(chunk_overlap: int) -> None:
    with pytest.raises(ValueError, match="chunk_overlap"):
        chunk_document(_document("text"), chunk_size=5, chunk_overlap=chunk_overlap)


def test_empty_document_produces_no_chunks() -> None:
    assert chunk_document(_document(""), chunk_size=10, chunk_overlap=2) == []


def test_repeated_execution_returns_identical_chunks() -> None:
    document = _document("repeatable content")

    assert chunk_document(document, 8, 2) == chunk_document(document, 8, 2)
