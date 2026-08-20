"""Local sentence-transformer embeddings for TechRAG."""

from __future__ import annotations

from typing import Any

from app.config import EMBEDDING_MODEL_NAME


class SentenceTransformerEmbedder:
    """Load one sentence-transformer model and expose batch/query embedding."""

    def __init__(
        self,
        model_name: str = EMBEDDING_MODEL_NAME,
        model: Any | None = None,
    ) -> None:
        if model is None:
            from sentence_transformers import SentenceTransformer

            model = SentenceTransformer(model_name)

        self.model_name = model_name
        self._model = model
        self._model.eval()

        dimension = self._model.get_sentence_embedding_dimension()
        if not isinstance(dimension, int) or dimension <= 0:
            raise ValueError("Embedding model must report a positive vector dimension")
        self.vector_size = dimension

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        """Embed a batch of texts without pre-normalizing the vectors."""
        if not texts:
            return []

        embeddings = self._model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=False,
            show_progress_bar=False,
        )
        return [
            [float(value) for value in embedding]
            for embedding in embeddings
        ]

    def embed_query(self, query: str) -> list[float]:
        """Embed one dense-retrieval query."""
        return self.embed_texts([query])[0]
