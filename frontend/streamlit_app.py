"""Streamlit frontend for the local TechRAG FastAPI service."""

from __future__ import annotations

import os
from typing import Any

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("TECHRAG_API_URL", "http://127.0.0.1:8000").rstrip("/")
STRATEGY_OPTIONS = {
    "Dense": "dense",
    "Hybrid": "hybrid",
    "Hybrid + Reranker": "reranked",
}
REQUEST_TIMEOUT_SECONDS = 180


def request_query(payload: dict[str, Any]) -> dict[str, Any]:
    """Send one query to FastAPI and raise a readable error on failure."""
    try:
        response = requests.post(
            f"{BACKEND_URL}/query",
            json=payload,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
    except requests.RequestException as error:
        raise RuntimeError(
            f"Could not reach the TechRAG API at {BACKEND_URL}."
        ) from error

    if response.ok:
        return response.json()
    try:
        detail = response.json().get("detail", {})
    except requests.JSONDecodeError:
        detail = {}
    message = detail.get("message") if isinstance(detail, dict) else str(detail)
    raise RuntimeError(message or f"API request failed with status {response.status_code}")


def _render_citations(citations: list[dict[str, Any]]) -> None:
    st.subheader("Citations")
    if not citations:
        st.caption("No validated citations returned.")
        return
    for citation in citations:
        title = (
            f"{citation['label']} · {citation['source']} · "
            f"chunk {citation['chunk_index']}"
        )
        with st.expander(title):
            st.caption(f"Chunk ID: {citation['chunk_id']}")
            st.write(citation["preview"])


def _render_context(chunks: list[dict[str, Any]]) -> None:
    with st.expander("Retrieved Context", expanded=False):
        if not chunks:
            st.caption("No chunks returned.")
            return
        for chunk in chunks:
            st.markdown(
                f"**{chunk['rank']}. {chunk['source']}**  \n"
                f"Score: `{chunk['score']:.4f}` ({chunk['score_type']})  \n"
                f"Chunk ID: `{chunk['chunk_id']}`"
            )
            st.write(chunk["preview"])
            st.divider()


def main() -> None:
    """Render the local stateless TechRAG demo."""
    st.set_page_config(page_title="TechRAG", page_icon="🔎", layout="wide")
    st.title("TechRAG")
    st.caption("Evaluated RAG for Technical Documentation")

    question = st.text_area(
        "Question",
        placeholder="What does score_threshold do?",
        height=110,
    )
    left, middle, right = st.columns([2, 2, 1])
    with left:
        strategy_label = st.selectbox(
            "Retrieval strategy",
            options=list(STRATEGY_OPTIONS),
            index=2,
        )
    with middle:
        generate_answer = st.toggle("Answer + citations", value=True)
        st.caption("Off: retrieval only")
    with right:
        top_k = st.number_input(
            "Top chunks",
            min_value=1,
            max_value=10,
            value=5,
            step=1,
        )

    if not st.button("Ask TechRAG", type="primary"):
        return
    if not question.strip():
        st.warning("Enter a question before submitting.")
        return

    payload = {
        "question": question,
        "strategy": STRATEGY_OPTIONS[strategy_label],
        "generate_answer": generate_answer,
        "top_k": int(top_k),
    }
    try:
        with st.spinner("Running the local pipeline…"):
            result = request_query(payload)
    except RuntimeError as error:
        st.error(str(error))
        return

    st.caption(
        f"Strategy: {strategy_label} · Latency: "
        f"{result['latency_ms'] / 1_000:.2f} s (local request)"
    )
    if generate_answer:
        st.subheader("Answer")
        st.markdown(result["answer"] or "No answer returned.")
        _render_citations(result["citations"])
        if result["invalid_citation_labels"]:
            st.warning(
                "Invalid citation labels returned by the model: "
                + ", ".join(result["invalid_citation_labels"])
            )
    else:
        st.info("Retrieval-only mode: answer generation was not requested.")
    _render_context(result["retrieved_chunks"])


if __name__ == "__main__":
    main()
