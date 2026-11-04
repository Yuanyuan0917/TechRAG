"""Tests for grounded prompting, citation validation, and RAG orchestration."""

from __future__ import annotations

import json
from typing import Sequence

import pytest

from app.generation.citations import parse_citation_labels
from app.generation.llm_client import (
    LLMConfigurationError,
    LLMRequestError,
    OpenAICompatibleLLMClient,
    remove_trailing_special_tokens,
)
from app.generation.prompt_templates import (
    build_generation_messages,
    label_contexts,
)
from app.generation.rag import RAGPipeline
from app.ingestion.models import Chunk
from app.retrieval.reranker import RerankedResult


def _chunk(index: int) -> Chunk:
    return Chunk(
        id=f"chunk_{index}",
        document_id=f"doc_{index // 2}",
        text=f"Technical context {index}.",
        source=f"/documents/source_{index}.md",
        chunk_index=index,
        metadata={"file_type": "markdown"},
    )


def _result(index: int) -> RerankedResult:
    return RerankedResult(
        chunk=_chunk(index),
        reranker_score=float(10 - index),
        rank=index + 1,
        hybrid_rank=index + 2,
        hybrid_rrf_score=0.01,
    )


def test_prompt_labels_contexts_and_includes_provenance_and_question() -> None:
    contexts = label_contexts([_chunk(0), _chunk(1)])

    messages = build_generation_messages("How does it work?", contexts)

    assert [context.label for context in contexts] == ["[C1]", "[C2]"]
    assert "answer only from the provided context" in messages[0]["content"].lower()
    assert "does not contain enough information" in messages[0]["content"]
    assert "cite every supported claim" in messages[0]["content"].lower()
    assert "[C1]" in messages[1]["content"]
    assert "Source: source_0.md" in messages[1]["content"]
    assert "Chunk ID: chunk_1" in messages[1]["content"]
    assert "How does it work?" in messages[1]["content"]


def test_prompt_handles_empty_context_explicitly() -> None:
    messages = build_generation_messages("Unknown question?", [])

    assert "No documentation context was retrieved." in messages[1]["content"]


@pytest.mark.parametrize(
    ("text", "expected_valid", "expected_invalid"),
    [
        ("Supported [C1].", ("[C1]",), ()),
        ("Both [C2][C1].", ("[C2]", "[C1]"), ()),
        ("Repeated [C1], then [C1].", ("[C1]",), ()),
        ("Unknown [C9].", (), ("[C9]",)),
        ("No references.", (), ()),
        ("Malformed C1, [C 1], [c1], and [C].", (), ()),
        ("Valid [C2], invalid [C8], valid [C1].", ("[C2]", "[C1]"), ("[C8]",)),
    ],
)
def test_citation_parser(
    text: str,
    expected_valid: tuple[str, ...],
    expected_invalid: tuple[str, ...],
) -> None:
    parsed = parse_citation_labels(text, {"[C1]", "[C2]"})

    assert parsed.valid_labels == expected_valid
    assert parsed.invalid_labels == expected_invalid


class FakeRetriever:
    def __init__(self, results: Sequence[RerankedResult]) -> None:
        self.results = list(results)
        self.calls: list[tuple[str, int]] = []

    def retrieve(self, question: str, top_k: int) -> list[RerankedResult]:
        self.calls.append((question, top_k))
        return self.results[:top_k]


class FakeLLM:
    def __init__(self, answer: str) -> None:
        self.answer = answer
        self.messages: list[list[dict[str, str]]] = []

    def generate(self, messages: list[dict[str, str]]) -> str:
        self.messages.append(messages)
        return self.answer


def test_rag_pipeline_limits_context_and_maps_valid_citations() -> None:
    retriever = FakeRetriever([_result(index) for index in range(6)])
    llm = FakeLLM("The answer uses two sources [C2][C1].")
    pipeline = RAGPipeline(retriever, llm)

    result = pipeline.answer("Question?")

    assert retriever.calls == [("Question?", 5)]
    assert len(result.retrieved_chunks) == 5
    assert len(result.contexts) == 5
    assert result.answer == llm.answer
    assert [citation.label for citation in result.citations] == ["[C2]", "[C1]"]
    assert result.citations[0].chunk_id == "chunk_1"
    assert result.citations[0].document_id == "doc_0"
    assert result.citations[0].source == "/documents/source_1.md"
    assert result.citations[0].chunk_index == 1
    assert result.invalid_citation_labels == ()
    assert "[C5]" in llm.messages[0][1]["content"]
    assert "chunk_5" not in llm.messages[0][1]["content"]


def test_rag_pipeline_exposes_invalid_and_missing_citations() -> None:
    retriever = FakeRetriever([_result(0)])
    invalid_result = RAGPipeline(
        retriever,
        FakeLLM("Supported [C1], invented [C9]."),
    ).answer("Question?")
    no_citation_result = RAGPipeline(
        retriever,
        FakeLLM("Answer without a citation."),
    ).answer("Question?")

    assert [citation.label for citation in invalid_result.citations] == ["[C1]"]
    assert invalid_result.invalid_citation_labels == ("[C9]",)
    assert no_citation_result.citations == ()
    assert no_citation_result.invalid_citation_labels == ()


def test_insufficient_context_response_passes_through() -> None:
    message = (
        "The provided documentation does not contain enough information to answer "
        "this reliably."
    )
    result = RAGPipeline(FakeRetriever([]), FakeLLM(message)).answer("Unknown?")

    assert result.answer == message
    assert result.citations == ()
    assert result.retrieved_chunks == ()


def test_llm_client_requires_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("LLM_API_KEY", raising=False)
    monkeypatch.setattr("app.generation.llm_client.load_dotenv", lambda: False)

    with pytest.raises(LLMConfigurationError, match="LLM_API_KEY"):
        OpenAICompatibleLLMClient(api_key="")


def test_llm_client_sends_chat_request_and_returns_text(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, object] = {}

    class FakeResponse:
        def __enter__(self) -> "FakeResponse":
            return self

        def __exit__(self, *args: object) -> None:
            return None

        def read(self) -> bytes:
            return b'{"choices":[{"message":{"content":" grounded answer "}}]}'

    def fake_urlopen(request: object, timeout: float) -> FakeResponse:
        captured["request"] = request
        captured["timeout"] = timeout
        return FakeResponse()

    monkeypatch.setattr("app.generation.llm_client.load_dotenv", lambda: False)
    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)
    client = OpenAICompatibleLLMClient(
        api_key="test-key",
        base_url="https://llm.example/v1/",
        model="test-model",
        timeout=12.0,
    )

    answer = client.generate([{"role": "user", "content": "Question"}])

    request = captured["request"]
    payload = json.loads(request.data.decode("utf-8"))
    assert answer == "grounded answer"
    assert request.full_url == "https://llm.example/v1/chat/completions"
    assert request.get_header("Authorization") == "Bearer test-key"
    assert payload == {
        "model": "test-model",
        "messages": [{"role": "user", "content": "Question"}],
        "temperature": 0.0,
    }
    assert captured["timeout"] == 12.0


def test_llm_client_normalizes_transport_errors(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def unavailable(*_: object, **__: object) -> object:
        raise OSError("connection unavailable")

    monkeypatch.setattr("app.generation.llm_client.load_dotenv", lambda: False)
    monkeypatch.setattr("urllib.request.urlopen", unavailable)
    client = OpenAICompatibleLLMClient(
        api_key="test-key",
        base_url="http://127.0.0.1:8080/v1",
        model="test-model",
    )

    with pytest.raises(LLMRequestError, match="connection unavailable"):
        client.generate([{"role": "user", "content": "Question"}])


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("Grounded answer.<|im_end|>", "Grounded answer."),
        ("Grounded answer. <|endoftext|>  ", "Grounded answer."),
        ("Grounded answer.<|im_end|><|im_end|>", "Grounded answer."),
        ("Mention <|im_end|> inside the answer.", "Mention <|im_end|> inside the answer."),
    ],
)
def test_remove_trailing_special_tokens(raw: str, expected: str) -> None:
    assert remove_trailing_special_tokens(raw) == expected
