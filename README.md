# TechRAG

An evaluated RAG system for technical documentation.

**Status:** Early development

The current project supports:

```text
Markdown / text-based PDF → deterministic chunking → local embeddings → Qdrant indexing → retrieval evaluation
```

It experimentally compares Dense Retrieval, Dense + BM25 + Reciprocal Rank Fusion, and Hybrid + Cross-Encoder Reranking. On the frozen 40-question evaluation, reranking increased Hybrid MRR from `0.596667` to `0.815417` and nDCG@5 from `0.476628` to `0.651735`, with additional local CPU latency. LLM answer generation is not implemented yet.

The intended pipeline is:

```text
documents → parsing → chunking → indexing → retrieval → generation → citations
```

Later work may use these measured retrieval strategies as inputs to answer generation and citation experiments.
