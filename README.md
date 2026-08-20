# TechRAG

An evaluated RAG system for technical documentation.

**Status:** Early development

Ingestion currently supports Markdown, text-based PDFs, and fixed-size character chunking with overlap.

The intended pipeline is:

```text
documents → parsing → chunking → indexing → retrieval → generation → citations
```

Later evaluation will compare dense retrieval, hybrid retrieval, and hybrid retrieval with reranking. These components are not yet implemented.
