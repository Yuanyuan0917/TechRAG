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

## Docker Compose runtime

```text
Browser → Streamlit container → FastAPI container → Qdrant server container
                                     │                    │
                                     │              qdrant_storage volume
                                     │
                                     ├─ BM25 from read-only /app/data/raw
                                     ├─ MiniLM / CrossEncoder (CPU)
                                     │       └─ huggingface_cache volume
                                     └─ host.docker.internal:8080
                                                ↓
                                      macOS MLX-LM / Qwen3-8B
```

API and indexing commands mount the same corpus at the same container path.
Indexing is explicit and uses the existing ingestion CLI; server readiness does
not imply a collection exists. The API validates collection size and chunk IDs
before constructing the shared retrievers, and missing/mismatched data returns
HTTP 503. BM25 stays in memory and must be refreshed by restarting the API after
corpus changes. No retrieval or generation algorithm changes for container use.

`QDRANT_URL` selects server mode; an unset value preserves native embedded mode.
The container index and the native embedded database are separate: source-path
hashes differ across environments, so the Compose corpus is indexed from within
Compose. Frozen native evaluation artifacts remain untouched.

Compose provides health checks, persistent Qdrant/model-cache volumes, and
private service networking. It publishes only loopback API/UI ports. Runtime
source is copied into images; corpus, datasets, weights, `.env`, and database
files are excluded from the build context. MLX-LM remains an external host
service; retrieval-only execution does not initialize an LLM client. See the
README for initialization, restart, and data-preserving shutdown commands.
