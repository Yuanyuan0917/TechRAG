"""Tests for resumable generation evaluation and manual score aggregation."""

from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

import pytest

from app.evaluation.generation import (
    abstention_accuracy,
    aggregate_annotations,
    classify_comparison,
    run_questions,
    serialize_generated_answer,
    validate_annotations,
)
from app.generation.prompt_templates import LabeledContext
from app.generation.rag import Citation, GeneratedAnswer
from app.ingestion.models import Chunk


def _chunk(index: int) -> Chunk:
    return Chunk(
        id=f"chunk_{index}",
        document_id="doc_1",
        text=f"Context {index}",
        source=f"/tmp/source_{index}.md",
        chunk_index=index,
        metadata={},
    )


def _generated(answer: str = "Answer [C1].") -> GeneratedAnswer:
    chunk = _chunk(0)
    result = SimpleNamespace(chunk=chunk, score=0.75)
    return GeneratedAnswer(
        answer=answer,
        citations=(
            Citation(
                label="[C1]",
                chunk_id=chunk.id,
                document_id=chunk.document_id,
                source=chunk.source,
                chunk_index=chunk.chunk_index,
            ),
        ),
        invalid_citation_labels=(),
        retrieved_chunks=(result,),
        contexts=(LabeledContext(label="[C1]", chunk=chunk),),
    )


class FakePipeline:
    def __init__(self, *, fail_on: str | None = None) -> None:
        self.fail_on = fail_on
        self.calls: list[str] = []

    def answer(self, question: str) -> GeneratedAnswer:
        self.calls.append(question)
        if question == self.fail_on:
            raise RuntimeError("local server unavailable")
        return _generated(f"Answer to {question} [C1].")


def _dataset() -> list[dict[str, object]]:
    return [
        {
            "id": "q001",
            "question": "Question one?",
            "reference_answer": "Reference one.",
            "difficulty": "fact",
        },
        {
            "id": "q002",
            "question": "Question two?",
            "reference_answer": "Reference two.",
            "difficulty": "multi_chunk",
        },
    ]


def _annotations(score: int = 2) -> dict[str, object]:
    return {
        item["id"]: {
            strategy: {
                "answer_correctness": score,
                "faithfulness": score,
                "citation_correctness": score,
                "notes": "Reviewed against answer and context.",
                "requires_human_review": False,
                "error_categories": [],
                "citation_coverage": "complete",
            }
            for strategy in ("dense", "hybrid", "reranked")
        }
        for item in _dataset()
    }


def test_result_serialization_preserves_answer_context_and_provenance() -> None:
    item = _dataset()[0]

    result = serialize_generated_answer(item, "dense", _generated(), 12.5)

    assert result["status"] == "completed"
    assert result["generated_answer"] == "Answer [C1]."
    assert result["retrieved_chunks"][0]["text"] == "Context 0"
    assert result["retrieved_chunks"][0]["score"] == 0.75
    assert result["citations"][0]["chunk_id"] == "chunk_0"
    assert result["latency_ms"] == 12.5


def test_resume_skips_completed_results(tmp_path: Path) -> None:
    output_path = tmp_path / "dense.json"
    first_pipeline = FakePipeline()
    run_questions(
        _dataset(),
        "dense",
        first_pipeline,
        output_path,
        {"model": "fake"},
    )
    second_pipeline = FakePipeline()

    result = run_questions(
        _dataset(),
        "dense",
        second_pipeline,
        output_path,
        {"model": "fake"},
        resume=True,
    )

    assert first_pipeline.calls == ["Question one?", "Question two?"]
    assert second_pipeline.calls == []
    assert [item["question_id"] for item in result["results"]] == ["q001", "q002"]


def test_error_is_recorded_and_retried_on_resume(tmp_path: Path) -> None:
    output_path = tmp_path / "dense.json"
    failed = run_questions(
        _dataset(),
        "dense",
        FakePipeline(fail_on="Question two?"),
        output_path,
        {},
    )
    assert failed["results"][1]["status"] == "error"
    assert "RuntimeError" in failed["results"][1]["error"]

    retry = FakePipeline()
    completed = run_questions(
        _dataset(),
        "dense",
        retry,
        output_path,
        {},
        resume=True,
    )

    assert retry.calls == ["Question two?"]
    assert all(item["status"] == "completed" for item in completed["results"])


def test_annotation_schema_rejects_invalid_score() -> None:
    annotations = _annotations()
    annotations["q001"]["dense"]["faithfulness"] = 3

    with pytest.raises(ValueError, match="must be 0, 1, or 2"):
        validate_annotations(annotations, _dataset())


def test_aggregate_scores_overall_and_by_type() -> None:
    annotations = _annotations()
    annotations["q002"]["dense"]["answer_correctness"] = 0

    summary = aggregate_annotations(annotations, _dataset())

    dense_correctness = summary["overall"]["dense"]["answer_correctness"]
    assert dense_correctness["mean"] == 1.0
    assert dense_correctness["counts"] == {"0": 1, "1": 0, "2": 1}
    assert (
        summary["by_question_type"]["fact"]["dense"]["answer_correctness"][
            "mean"
        ]
        == 2.0
    )


def test_abstention_metric() -> None:
    summary = abstention_accuracy(
        [
            {"outcome": "abstained_correctly"},
            {"outcome": "partially_hedged"},
            {"outcome": "abstained_correctly"},
        ]
    )

    assert summary["correct_abstentions"] == 2
    assert summary["accuracy"] == pytest.approx(2 / 3)


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        ((2, 0, 0), (1, 2, 2), "improved"),
        ((2, 2, 1), (2, 1, 2), "improved"),
        ((1, 2, 2), (2, 0, 0), "regressed"),
        ((2, 2, 2), (2, 2, 2), "unchanged"),
    ],
)
def test_comparison_classification(
    left: tuple[int, int, int],
    right: tuple[int, int, int],
    expected: str,
) -> None:
    def annotation(scores: tuple[int, int, int]) -> dict[str, int]:
        return dict(zip(
            ("answer_correctness", "faithfulness", "citation_correctness"),
            scores,
        ))

    assert classify_comparison(annotation(left), annotation(right)) == expected
