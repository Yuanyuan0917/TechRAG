# TechRAG

An evaluated RAG system for technical documentation.

**Status:** Early development

The current project supports:

```text
Markdown / text-based PDF → deterministic chunking → local embeddings → Qdrant indexing → retrieval evaluation
```

It experimentally compares Dense Retrieval with Dense + BM25 + Reciprocal Rank Fusion. LLM answer generation and reranking are not implemented yet; no strategy is assumed superior without measured evaluation results.

The intended pipeline is:

```text
documents → parsing → chunking → indexing → retrieval → generation → citations
```

Later work may compare the measured retrieval baselines with reranking.
