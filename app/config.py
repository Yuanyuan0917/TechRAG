"""Configuration defaults for TechRAG."""

import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
RERANKER_MODEL_NAME = "cross-encoder/ms-marco-MiniLM-L-6-v2"
QDRANT_PATH = PROJECT_ROOT / "data" / "qdrant"
QDRANT_COLLECTION_NAME = "techrag_chunks"
QDRANT_URL = os.getenv("QDRANT_URL") or None

LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://api.openai.com/v1")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4.1-mini")
GENERATION_CONTEXT_TOP_K = 5
GENERATION_TEMPERATURE = 0.0
