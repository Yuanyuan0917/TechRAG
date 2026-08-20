# TechRAG

An evaluated RAG system for technical documentation.

**Status:** Early development

The current baseline supports:

```text
Markdown / text-based PDF → deterministic chunking → local embeddings → Qdrant indexing → dense retrieval
```

LLM answer generation, hybrid retrieval, and evaluation are not implemented yet.

The intended pipeline is:

```text
documents → parsing → chunking → indexing → retrieval → generation → citations
```

Later evaluation will compare dense retrieval, hybrid retrieval, and hybrid retrieval with reranking. These components are not yet implemented.
