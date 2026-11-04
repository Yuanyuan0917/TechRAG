# Architecture

The local demo keeps the UI and application pipeline separated by an HTTP API:

```text
                  Streamlit
                      ↓ HTTP
                   FastAPI
                      ↓
          Selected retrieval strategy
            ├─ dense: Dense
            ├─ hybrid: Dense + BM25 → RRF
            └─ reranked: Dense + BM25 → RRF → CrossEncoder
                              ↓
                         Top-k Context
                              ↓
               Qwen3-8B (when generation is requested)
                              ↓
                   Answer + Validated Citations
```

FastAPI reuses application-scoped retrieval components. The Streamlit frontend
only calls the API and does not import retrieval or generation internals.

`GET /health` reports process health without loading models. `POST /query` uses
the selected strategy for both retrieval-only and generated responses. Retrieval
and the local Qdrant lifecycle share a single worker thread; the LLM client is
initialized only for generation requests. Retrieval-only responses bypass Qwen.
Unavailable retrieval or LLM services return structured HTTP 503 errors. The
local demo runs as one API process and does not provide authentication or
production deployment infrastructure.
