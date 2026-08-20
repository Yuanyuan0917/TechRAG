"""Configuration defaults for TechRAG."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
QDRANT_PATH = PROJECT_ROOT / "data" / "qdrant"
QDRANT_COLLECTION_NAME = "techrag_chunks"
