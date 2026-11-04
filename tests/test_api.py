"""API tests using deterministic retrieval and generation fakes."""

from __future__ import annotations

from types import SimpleNamespace
from typing import Any

import pytest
from fastapi.testclient import TestClient

from app.api.main import create_app
from app.api.routes_query import TechRAGService
from app.generation.llm_client import LLMRequestError
from app.ingestion.models import Chunk


class FakeRetriever:
    def __init__(self, strategy: str) -> None:
        self.strategy = strategy
        self.calls: list[tuple[str, int]] = []

    def retrieve(self, query: str, top_k: int = 5) -> list[Any]:
        self.calls.append((query, top_k))
        chunks = [
            Chunk(
                id=f"chunk_{index}",
                document_id="document_1",
                text=f"Relevant technical context number {index}.",
                source=f"/private/local/corpus/source_{index}.md",
                chunk_index=index,
                metadata={"file_type": "markdown"},
            )
            for index in range(top_k)
        ]
        if self.strategy == "reranked":
            return [
                SimpleNamespace(
                    chunk=chunk,
                    reranker_score=0.9 - index / 10,
                    hybrid_rank=index + 2,
                    hybrid_rrf_score=0.03 - index / 100,
                )
                for index, chunk in enumerate(chunks)
            ]
        return [
            SimpleNamespace(chunk=chunk, score=0.9 - index / 10)
            for index, chunk in enumerate(chunks)
        ]


class FakeLLMClient:
    def generate(self, _: Any) -> str:
        return "The grounded answer uses the first context [C1]."


class UnavailableLLMClient:
    def generate(self, _: Any) -> str:
        raise LLMRequestError("connection refused")


def _service(llm_client: Any | None = None) -> TechRAGService:
    retrievers = {
        strategy: FakeRetriever(strategy)
        for strategy in ("dense", "hybrid", "reranked")
    }
    client = llm_client or FakeLLMClient()
    return TechRAGService(
        retrievers=retrievers,
        llm_client_factory=lambda: client,
    )


@pytest.fixture
def client() -> Any:
    with TestClient(create_app(_service())) as test_client:
        yield test_client


def test_health_is_lightweight(client: TestClient) -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_retrieval_only_query_returns_ranked_sanitized_chunks(
    client: TestClient,
) -> None:
    response = client.post(
        "/query",
        json={
            "question": "What does score threshold do?",
            "strategy": "dense",
            "generate_answer": False,
            "top_k": 2,
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["answer"] is None
    assert body["citations"] == []
    assert body["invalid_citation_labels"] == []
    assert [chunk["rank"] for chunk in body["retrieved_chunks"]] == [1, 2]
    assert body["retrieved_chunks"][0]["score_type"] == "cosine"
    assert body["retrieved_chunks"][0]["source"] == "source_0.md"
    assert "/private/" not in response.text


def test_generated_query_serializes_validated_citations(
    client: TestClient,
) -> None:
    response = client.post(
        "/query",
        json={
            "question": "Explain the technical context.",
            "strategy": "reranked",
            "generate_answer": True,
            "top_k": 2,
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["strategy"] == "reranked"
    assert body["answer"] == "The grounded answer uses the first context [C1]."
    assert body["invalid_citation_labels"] == []
    assert body["citations"] == [
        {
            "label": "[C1]",
            "chunk_id": "chunk_0",
            "document_id": "document_1",
            "source": "source_0.md",
            "chunk_index": 0,
            "preview": "Relevant technical context number 0.",
        }
    ]
    first_chunk = body["retrieved_chunks"][0]
    assert first_chunk["score_type"] == "cross_encoder"
    assert first_chunk["hybrid_rank"] == 2
    assert first_chunk["hybrid_rrf_score"] == pytest.approx(0.03)


@pytest.mark.parametrize(
    "payload",
    [
        {"question": "Question", "strategy": "unknown"},
        {"question": "   ", "strategy": "dense"},
        {"question": "Question", "strategy": "dense", "top_k": 0},
        {"question": "Question", "strategy": "dense", "top_k": 11},
    ],
)
def test_invalid_query_input_returns_validation_error(
    client: TestClient,
    payload: dict[str, Any],
) -> None:
    response = client.post("/query", json=payload)

    assert response.status_code == 422


def test_generation_unavailable_returns_structured_503() -> None:
    with TestClient(create_app(_service(UnavailableLLMClient()))) as client:
        response = client.post(
            "/query",
            json={
                "question": "Explain the technical context.",
                "strategy": "reranked",
                "generate_answer": True,
            },
        )

    assert response.status_code == 503
    assert response.json()["detail"]["code"] == "generation_unavailable"


def test_retrieval_only_does_not_initialize_llm() -> None:
    retrievers = {
        strategy: FakeRetriever(strategy)
        for strategy in ("dense", "hybrid", "reranked")
    }

    def fail_if_called() -> Any:
        raise AssertionError("LLM client must not be initialized")

    service = TechRAGService(
        retrievers=retrievers,
        llm_client_factory=fail_if_called,
    )
    with TestClient(create_app(service)) as client:
        response = client.post(
            "/query",
            json={
                "question": "Retrieve relevant context.",
                "strategy": "hybrid",
                "generate_answer": False,
            },
        )

    assert response.status_code == 200
    assert response.json()["answer"] is None


@pytest.mark.parametrize("generate_answer", [False, True])
def test_retrieval_failure_returns_503_in_both_modes(generate_answer: bool) -> None:
    class UnavailableRetriever:
        def retrieve(self, query: str, top_k: int = 5) -> list[Any]:
            raise OSError("Cannot read /private/local/qdrant/index")

    service = TechRAGService(
        retrievers={"dense": UnavailableRetriever()},
        llm_client_factory=FakeLLMClient,
    )
    with TestClient(create_app(service)) as client:
        response = client.post(
            "/query",
            json={
                "question": "Find the relevant documentation.",
                "strategy": "dense",
                "generate_answer": generate_answer,
            },
        )

    assert response.status_code == 503
    assert response.json()["detail"]["code"] == "retrieval_unavailable"
    assert "/private/" not in response.text
