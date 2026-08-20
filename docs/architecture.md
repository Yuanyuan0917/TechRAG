# Architecture

The local demo keeps the UI and application pipeline separated by an HTTP API:

```text
                  Streamlit
                      ↓ HTTP
                   FastAPI
                      ↓
                   TechRAG
       ┌──────────────┼──────────────┐
       ↓              ↓              ↓
    Dense           BM25         Reranker
       \              /              |
        └────── RRF ─────────────────┘
                      ↓
                  Top Context
                      ↓
                  Qwen3-8B
                      ↓
             Answer + Citations
```

FastAPI reuses application-scoped retrieval components. The Streamlit frontend
only calls the API and does not import retrieval or generation internals.
