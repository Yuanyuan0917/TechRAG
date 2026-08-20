"""Document parsing utilities for TechRAG."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

from app.ingestion.models import Document


def _normalize_source(path: Path) -> str:
    """Return a stable, absolute representation of a source path."""
    return path.expanduser().resolve().as_posix()


def _document_id(source: str) -> str:
    """Build a deterministic identifier from a normalized source path."""
    digest = hashlib.sha256(source.encode("utf-8")).hexdigest()
    return f"doc_{digest}"


def _markdown_title(text: str, path: Path) -> str:
    """Use the first H1 heading, falling back to the filename stem."""
    for line in text.splitlines():
        match = re.match(r"^#\s+(.+?)\s*#*\s*$", line.strip())
        if match:
            return match.group(1)
    return path.stem


def _parse_markdown(path: Path, source: str) -> Document:
    text = path.read_text(encoding="utf-8")
    return Document(
        id=_document_id(source),
        text=text,
        source=source,
        title=_markdown_title(text, path),
        metadata={"file_type": "markdown"},
    )


def _parse_pdf(path: Path, source: str) -> Document:
    import fitz

    with fitz.open(path) as pdf:
        page_text = [page.get_text() for page in pdf]
        page_count = pdf.page_count
        metadata_title = ((pdf.metadata or {}).get("title") or "").strip()

    text = "\n".join(page_text)
    if not text.strip():
        raise ValueError(
            f"No extractable text found in PDF '{path}'. "
            "Scanned or image-only PDFs are currently out of scope; OCR is not supported."
        )

    return Document(
        id=_document_id(source),
        text=text,
        source=source,
        title=metadata_title or path.stem,
        metadata={"file_type": "pdf", "page_count": page_count},
    )


def parse_document(path: Path) -> Document:
    """Parse a supported file into a document."""
    path = Path(path)
    source = _normalize_source(path)
    extension = path.suffix.lower()

    if extension == ".md":
        return _parse_markdown(path, source)
    if extension == ".pdf":
        return _parse_pdf(path, source)

    raise ValueError(
        f"Unsupported file type '{path.suffix or '<none>'}'. Supported extensions: .md, .pdf."
    )
