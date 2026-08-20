"""Deterministic citation-label extraction and validation."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Collection

_CITATION_PATTERN = re.compile(r"\[C\d+\]")


@dataclass(frozen=True)
class CitationParseResult:
    """Valid and invalid labels found in generated text."""

    valid_labels: tuple[str, ...]
    invalid_labels: tuple[str, ...]


def parse_citation_labels(
    text: str,
    valid_labels: Collection[str],
) -> CitationParseResult:
    """Extract exact labels, deduplicate them, and preserve first-seen order."""
    allowed = set(valid_labels)
    valid: list[str] = []
    invalid: list[str] = []
    seen: set[str] = set()
    for match in _CITATION_PATTERN.finditer(text):
        label = match.group(0)
        if label in seen:
            continue
        seen.add(label)
        if label in allowed:
            valid.append(label)
        else:
            invalid.append(label)
    return CitationParseResult(tuple(valid), tuple(invalid))
