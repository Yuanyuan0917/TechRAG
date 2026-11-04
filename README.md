# TechRAG

An evaluated RAG system for technical documentation.

**Status:** Early development

The current project supports:

```text
Markdown / text-based PDF → deterministic chunking → local embeddings → Qdrant indexing → retrieval evaluation
```

It experimentally compares Dense Retrieval, Dense + BM25 + Reciprocal Rank Fusion, and Hybrid + Cross-Encoder Reranking. On the frozen 40-question evaluation, reranking increased Hybrid MRR from `0.596667` to `0.815417` and nDCG@5 from `0.476628` to `0.651735`, with additional local CPU latency.

The test-backed generation pipeline uses selected-strategy top-k chunks, an OpenAI-compatible chat-completions endpoint, grounded prompting, and validated chunk-level citations. Configure `LLM_API_KEY`, `LLM_BASE_URL`, and `LLM_MODEL` locally to run real answer generation.

The intended pipeline is:

```text
documents → parsing → chunking → indexing → retrieval → generation → citations
```

The frozen retrieval and generation evaluations are documented under `docs/`.

## Local Demo

Install dependencies and configure the local environment once:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
cp -n .env.example .env
```

For local MLX-LM, set `LLM_API_KEY` in `.env` to a non-empty local-only value
such as `local-mlx`. It is only used to form the OpenAI-compatible authorization
header; it is not a hosted API secret.

Start each service in a separate terminal. Terminal 1 runs Qwen with thinking
disabled, matching the evaluated generation configuration:

```bash
source .venv/bin/activate
mlx_lm.server \
  --model Qwen/Qwen3-8B-MLX-4bit \
  --host 127.0.0.1 \
  --port 8080 \
  --chat-template-args '{"enable_thinking":false}'
```

Terminal 2 runs FastAPI:

```bash
source .venv/bin/activate
uvicorn app.api.main:app \
  --host 127.0.0.1 \
  --port 8000 \
  --reload
```

Terminal 3 runs Streamlit:

```bash
source .venv/bin/activate
streamlit run frontend/streamlit_app.py
```

Open `http://localhost:8501`. The first query can be slower while local models
load. Retrieval-only mode works without Qwen/MLX-LM; answer generation requires
the Qwen server.

The API exposes `GET /health` for lightweight process health and `POST /query`
for queries. `/health` does not check model or index readiness. Query requests
accept `dense`, `hybrid`, or `reranked` (default), with `top_k` from 1 to 10
(default 5). Set `generate_answer` to `false` for retrieval-only responses with
`answer: null` and empty citations. Missing LLM configuration or an unavailable
LLM service produces HTTP 503 with `generation_unavailable`; retrieval/index
failures produce HTTP 503 with `retrieval_unavailable`. Input validation failures
return HTTP 422.

This demo is intended for local use on macOS with Apple Silicon and has no
authentication. Run one API process: local Qdrant requires exclusive access, and
pipeline requests execute serially on one worker thread. Stop the API before
running indexing or evaluation commands that open the same Qdrant directory.
An existing index is required; if needed, run
`python scripts/ingest.py data/raw/ --index` before starting the API.
Reported `latency_ms` measures pipeline execution, including lazy initialization,
but excludes executor queue time and HTTP transport. It is not production latency.

The frontend reads `TECHRAG_API_URL`, defaulting to
`http://127.0.0.1:8000`. A direct API request is:

```bash
curl -X POST http://127.0.0.1:8000/query \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What does score_threshold do?",
    "strategy": "reranked",
    "generate_answer": true,
    "top_k": 5
  }'
```

## Docker Compose Demo

Prerequisites: Docker Desktop for Mac running with Compose v2 or later, the
repository's corpus present under `data/raw/`, and internet access on the first
image build and model download. Linux containers use Python 3.11 and CPU
embeddings/reranking; MLX-LM stays on the Apple Silicon host. Runtime dependencies
are pinned separately under `docker/`; the native `requirements.txt` is unchanged.

Compose runs `frontend → api → qdrant` on its private network. Only the API
(`127.0.0.1:8000`) and UI (`127.0.0.1:8501`) are published to the host. The
frontend uses `http://api:8000`, and the API uses `QDRANT_URL=http://qdrant:6333`.
Native use still defaults to embedded Qdrant when `QDRANT_URL` is unset.
To select a server for native commands, export `QDRANT_URL` before startup;
Compose supplies it directly to the API container. An explicit local database
path in Python callers takes precedence over the environment URL default.

### Build and initialize retrieval data

Run from the repository root:

```bash
docker compose config --quiet
docker compose build
docker compose up -d --wait qdrant
docker compose run --rm api python scripts/ingest.py data/raw/ --index
docker compose up -d --wait
```

Open `http://localhost:8501`, or check the API with
`curl http://127.0.0.1:8000/health`. Qdrant, API, and frontend have health checks;
API health is process health and does not mean the corpus has been indexed.
An empty Qdrant service alone cannot answer retrieval requests: until indexing
completes, `/query` returns structured HTTP 503 `retrieval_unavailable`.

`data/raw/` is mounted read-only at `/app/data/raw` for both indexing and API
containers. Indexing uses the existing parser, 1000/200 character chunking,
MiniLM embeddings, and deterministic upserts. BM25 is rebuilt in memory from
that same mounted corpus on API initialization. No corpus or evaluation dataset
is copied into either image. Models download only at runtime into a shared
`huggingface_cache` named volume; the first indexing/reranked query is slower.

The Qdrant server stores its collection in the `qdrant_storage` named volume,
separate from the native `data/qdrant/` embedded database. Subsequent starts reuse
the volume; indexing is not repeated automatically. Repeating the indexing
command on an unchanged corpus upserts the same points without duplicates.

Document IDs currently include normalized source paths, so a host-built index
cannot simply be copied into this container workflow. Index inside Compose to
keep dense and BM25 IDs consistent. The API checks both count and chunk IDs and
returns HTTP 503 on a mismatch. Frozen evaluation datasets/results retain their
original host IDs and are not regenerated for this demo. Existing Compose data
can be restored by reattaching the same named volume with the same corpus and
container path. For a fresh volume, rebuild with the indexing command above.

If corpus files are added, removed, or replaced, stop the API, explicitly rebuild
the demo collection, and restart the API to refresh its in-memory BM25 index:

```bash
docker compose stop api frontend
docker compose run --rm api python scripts/ingest.py data/raw/ --index --reset-index
docker compose up -d --wait
```

`--reset-index` deletes and recreates the configured **demo collection**. Use it
only when intentionally rebuilding; normal startup never resets stored data.

### Host MLX-LM and configuration

Retrieval-only mode works with MLX-LM stopped. For generated answers, start the
host server in a separate terminal, bound only to localhost:

```bash
source .venv/bin/activate
mlx_lm.server \
  --model Qwen/Qwen3-8B-MLX-4bit \
  --host 127.0.0.1 \
  --port 8080 \
  --chat-template-args '{"enable_thinking":false}'
```

The API defaults to `http://host.docker.internal:8080/v1`, Docker Desktop's
[host-service address](https://docs.docker.com/desktop/features/networking/networking-how-tos/).
The localhost binding worked through Docker Desktop during the smoke test and
keeps the unauthenticated model service off the LAN. macOS firewall settings
must permit Docker Desktop's connection.
If MLX-LM is unavailable, generation requests return HTTP 503
`generation_unavailable` and retrieval-only requests remain available.

Compose reads these optional variables from the shell or root `.env` at runtime:

| Variable | Compose default |
| --- | --- |
| `TECHRAG_DOCKER_LLM_BASE_URL` | `http://host.docker.internal:8080/v1` |
| `LLM_MODEL` | `Qwen/Qwen3-8B-MLX-4bit` |
| `LLM_API_KEY` | `local-mlx` (local compatibility header) |
| `TECHRAG_API_PORT` | `8000` |
| `TECHRAG_UI_PORT` | `8501` |

The Docker-specific LLM URL avoids accidentally using native
`LLM_BASE_URL=http://127.0.0.1:8080/v1` inside the container. `.env` is never
copied into an image, and the frontend receives no LLM credentials. The existing
API request example above works with the Compose stack unchanged.

### Stop and limitations

```bash
docker compose down
```

This stops/removes service containers and the network while retaining Qdrant
and Hugging Face volumes. Do not add `--volumes` if you want to keep that data.
Images, caches, and named volumes consume Docker Desktop disk space.

This is a local demo with one API worker, no authentication/TLS, no automatic
corpus synchronization, and no production deployment guarantees. Image versions
and direct runtime dependencies are pinned; transitive dependencies are not a
complete lockfile. Linux CPU results/timings are not asserted to reproduce the
frozen native evaluation. The default host connectivity targets Docker Desktop
on macOS; other Docker installations may require a different host-service URL.

## Continuous Integration

[The test workflow](.github/workflows/test.yml) runs on pull requests targeting
`main` and pushes to `main`, using Ubuntu 24.04 and Python 3.11. It runs the full
pytest suite, Python compilation, dependency consistency and whitespace checks,
workflow YAML parsing, and Docker Compose configuration validation. It does not
start containers or perform deployment.

CI installs CPU PyTorch and `requirements-ci.txt`, which reuses the API/frontend
Linux dependency manifests and adds test tools. MLX-LM is excluded because it
runs on the macOS host. Tests use fake embedding/reranking models, fake LLM
clients, temporary Qdrant storage, and generated document fixtures. No real API
keys, corpus, persistent database, GPU, or model weights are required. Hugging
Face offline mode and pytest socket blocking prevent accidental model/network
access; Unix sockets remain allowed for in-process async API tests.

The workflow has read-only repository permissions, pins actions to commit SHAs,
and caches pip packages keyed by the dependency manifests/workflow. It does not
cache model weights, `.env`, or Qdrant data. Installing dependencies still needs
network access; real inference remains a separate local smoke test.

To reproduce the checks on Linux with Python 3.11 and Docker Compose installed:

```bash
python3.11 -m venv .venv-ci
source .venv-ci/bin/activate
python -m pip install torch==2.8.0 --index-url https://download.pytorch.org/whl/cpu
python -m pip install -r requirements-ci.txt
HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 LLM_API_KEY= QDRANT_URL= \
  python -m pytest --disable-socket --allow-unix-socket
python -m compileall -q app scripts frontend tests
python -m pip check
git diff --check
python -c "from pathlib import Path; import yaml; yaml.safe_load(Path('.github/workflows/test.yml').read_text())"
docker compose --env-file .env.example config --quiet
```
