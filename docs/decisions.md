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
