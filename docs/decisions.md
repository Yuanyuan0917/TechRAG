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

## BM25

- **Choice:** In-process `rank-bm25` over the exact frozen `Chunk` objects.
- **Reason:** Lexical retrieval can complement semantic retrieval in a controlled experiment, especially for exact technical terms and API names.
- **Tokenizer:** Unicode case-folding followed by the standard-library regex `[a-z0-9_]+`; underscores in identifiers such as `score_threshold` are retained.
- **Trade-off:** No stemming, lemmatization, synonym expansion, or advanced preprocessing is used, so lexical variants may not match.

## Reciprocal Rank Fusion

- **Choice:** Fuse dense top-20 and BM25 top-20 rankings with standard Reciprocal Rank Fusion and fixed `k=60`.
- **Reason:** Dense cosine scores and BM25 scores are not directly comparable; rank-based fusion avoids score calibration.
- **Tie-breaking:** Equal fused scores are ordered by deterministic chunk ID.
- **Experimental constraint:** The fusion constant, candidate depths, and tokenization were fixed before evaluation and were not tuned.

## Cross-encoder reranking

- **Choice:** `cross-encoder/ms-marco-MiniLM-L-6-v2` reranks only the Hybrid top-20 candidate set and returns the top 10.
- **Reason:** A cross-encoder jointly scores each query and passage and may improve early ranking precision without changing candidate generation.
- **Trade-off:** It adds model compute and query latency, and cannot recover relevant chunks missing from the Hybrid candidates.
- **Experimental constraint:** One predefined model and candidate depth were evaluated without tuning.

## Generation strategy

- **Retrieval:** Hybrid + Cross-Encoder reranking supplies the top five context chunks.
- **Prompting:** Low-temperature generation is instructed to answer only from supplied context, cite exact labels, and decline unsupported questions.
- **Scope:** One stateless answer is generated per request; no conversation memory or agent loop is used.

## Citation strategy

- Citation labels such as `[C1]` are assigned to retrieved chunks before generation.
- Generated labels are parsed and validated against the supplied context after generation.
- Structured citation provenance comes from retrieved chunk metadata, never from filenames or mappings invented by the LLM.
- Unknown labels are reported as invalid and are never mapped to a chunk.
