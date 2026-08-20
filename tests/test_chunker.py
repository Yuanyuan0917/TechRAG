"""Tests for TechRAG document chunking."""


def test_chunker_module_imports() -> None:
    """Verify that the chunker skeleton can be imported."""
    from app.ingestion import chunker

    assert chunker.__doc__
