"""Run the local TechRAG ingestion pipeline."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.ingestion.chunker import chunk_document
from app.ingestion.parser import parse_document

SUPPORTED_EXTENSIONS = {".md", ".pdf"}


def _input_files(input_path: Path) -> list[Path]:
    """Return supported input files without recursing into directories."""
    if input_path.is_file():
        return [input_path]
    if input_path.is_dir():
        return sorted(
            (
                path
                for path in input_path.iterdir()
                if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
            ),
            key=lambda path: path.name.casefold(),
        )
    raise ValueError(f"Input path does not exist: {input_path}")


def _argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Parse and chunk Markdown or text-based PDF documents."
    )
    parser.add_argument("path", type=Path, help="A document or non-recursive directory")
    parser.add_argument("--chunk-size", type=int, default=1000)
    parser.add_argument("--chunk-overlap", type=int, default=200)
    return parser


def main() -> int:
    """Parse command-line input and print ingestion summaries."""
    argument_parser = _argument_parser()
    args = argument_parser.parse_args()

    try:
        files = _input_files(args.path)
        total_chunks = 0
        for path in files:
            document = parse_document(path)
            chunks = chunk_document(
                document,
                chunk_size=args.chunk_size,
                chunk_overlap=args.chunk_overlap,
            )
            total_chunks += len(chunks)
            print(f"Loaded: {path.name}")
            print(f"Document ID: {document.id}")
            print(f"Characters: {len(document.text)}")
            print(f"Chunks: {len(chunks)}")

        print(f"Documents: {len(files)}")
        print(f"Chunks: {total_chunks}")
    except (OSError, ValueError) as error:
        argument_parser.error(str(error))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
