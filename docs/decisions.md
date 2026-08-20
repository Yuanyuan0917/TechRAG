# Design Decisions

This document records architectural and experimental decisions made during the project.

Each decision should eventually answer:

- What was chosen?
- Why was it chosen?
- What alternatives were considered?
- What trade-offs were accepted?

## Baseline chunking

- **Choice:** Fixed-size character chunking with overlap.
- **Reason:** It provides a simple and controlled baseline.
- **Alternative deferred:** Semantic or token-aware chunking.
- **Trade-off:** Chunk boundaries may split semantic units, but behavior is deterministic and easy to evaluate.

## Embedding baseline

- **Choice:** `sentence-transformers/all-MiniLM-L6-v2`.
- **Reason:** It is a lightweight local baseline suitable for semantic retrieval.
- **Trade-off:** It is not necessarily state of the art, but is fast and reproducible.
- **Deferred:** Model comparison will wait until after baseline evaluation, if it is needed.

## Vector store

- **Choice:** Qdrant in local persistent mode for development.
- **Reason:** It is a production-relevant vector database while remaining easy to run locally.
- **Point IDs:** Deterministic UUIDv5 values derived from stable chunk IDs; the original chunk ID remains in the payload.
- **Deferred:** Remote or containerized deployment.
