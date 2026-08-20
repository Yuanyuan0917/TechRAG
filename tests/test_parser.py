"""Tests for TechRAG document parsing."""

from pathlib import Path

import fitz
import pytest

from app.ingestion.parser import parse_document


def test_markdown_loads_text_and_uses_first_h1(tmp_path: Path) -> None:
    path = tmp_path / "guide.md"
    text = "Introduction\n# Main Title\n\nMarkdown **content**.\n"
    path.write_text(text, encoding="utf-8")

    document = parse_document(path)

    assert document.text == text
    assert document.title == "Main Title"
    assert document.source == path.resolve().as_posix()
    assert document.metadata == {"file_type": "markdown"}


def test_markdown_uses_filename_when_no_h1_exists(tmp_path: Path) -> None:
    path = tmp_path / "fallback-name.md"
    path.write_text("## Only an H2", encoding="utf-8")

    assert parse_document(path).title == "fallback-name"


def test_document_id_is_deterministic(tmp_path: Path) -> None:
    path = tmp_path / "stable.md"
    path.write_text("Stable text", encoding="utf-8")

    assert parse_document(path).id == parse_document(path).id


def test_extensions_are_case_insensitive(tmp_path: Path) -> None:
    path = tmp_path / "upper.MD"
    path.write_text("# Upper", encoding="utf-8")

    assert parse_document(path).title == "Upper"


def test_unsupported_extension_raises(tmp_path: Path) -> None:
    path = tmp_path / "notes.txt"
    path.write_text("text", encoding="utf-8")

    with pytest.raises(ValueError, match="Unsupported file type"):
        parse_document(path)


def test_pdf_extracts_pages_in_order_and_records_page_count(tmp_path: Path) -> None:
    path = tmp_path / "ordered.pdf"
    with fitz.open() as pdf:
        first_page = pdf.new_page()
        first_page.insert_text((72, 72), "First page text")
        second_page = pdf.new_page()
        second_page.insert_text((72, 72), "Second page text")
        pdf.set_metadata({"title": "PDF Title"})
        pdf.save(path)

    document = parse_document(path)

    assert "First page text" in document.text
    assert "Second page text" in document.text
    assert document.text.index("First page text") < document.text.index("Second page text")
    assert document.title == "PDF Title"
    assert document.metadata == {"file_type": "pdf", "page_count": 2}


def test_pdf_without_extractable_text_explains_ocr_limit(tmp_path: Path) -> None:
    path = tmp_path / "image-only.pdf"
    with fitz.open() as pdf:
        pdf.new_page()
        pdf.save(path)

    with pytest.raises(ValueError, match="OCR is not supported"):
        parse_document(path)
