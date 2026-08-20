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
cp .env.example .env
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
