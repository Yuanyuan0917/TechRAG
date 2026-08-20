# Local Generation Smoke Test

## Purpose

Validate the existing TechRAG retrieval, generation, and citation pipeline with a real local language model. This is a qualitative smoke test, not a generation-quality evaluation.

## Environment

- Date: 2026-08-20
- Hardware: local MacBook Pro, Apple M5, 24 GB unified memory
- Architecture: `arm64`
- Python: 3.9.6
- MLX-LM: 0.29.1
- MLX: 0.29.3
- Model: `Qwen/Qwen3-8B-MLX-4bit`
- Server URL: `http://127.0.0.1:8080/v1`
- Retrieval: Dense + BM25, reciprocal rank fusion, CrossEncoder reranking
- Generation context: reranked top 5
- Temperature: 0.0
- Qwen thinking: disabled with MLX-LM server chat-template arguments

The model was not previously cached. MLX-LM downloaded the approximately 4.35 GB model payload to the Hugging Face user cache; the resulting cache directory occupies approximately 4.1 GB. The model was fully loaded before query timing began.

MLX-LM 0.29.1 uses port 8080 by default, so this run used 8080 instead of the example port 8000. The server warned that its development server is not recommended for production; it was used only on the loopback interface for this local smoke test.

## Server Verification

The `GET /v1/models` endpoint listed `Qwen/Qwen3-8B-MLX-4bit`. A minimal `POST /v1/chat/completions` request accepted that model and returned HTTP 200 with `server ready<|im_end|>`.

The server exposes the trailing Qwen `<|im_end|>` control token in non-streaming response content. A standard OpenAI-compatible `stop` value did not suppress it in MLX-LM 0.29.1. TechRAG's provider-neutral client was not changed to strip a Qwen-specific token, so the exact generated answers below retain it.

## Commands

```bash
git status
git branch --show-current
.venv/bin/python --version
uname -m
.venv/bin/python -m pip install -U mlx-lm
.venv/bin/python -m pip check
.venv/bin/python -m mlx_lm server --model Qwen/Qwen3-8B-MLX-4bit --chat-template-args '{"enable_thinking":false}'
curl --fail --silent --show-error http://127.0.0.1:8080/v1/models
curl --fail --silent --show-error http://127.0.0.1:8080/v1/chat/completions -H 'Content-Type: application/json' --data-binary '{"model":"Qwen/Qwen3-8B-MLX-4bit","messages":[{"role":"user","content":"Reply with exactly: server ready"}],"temperature":0,"max_tokens":16}'
.venv/bin/python scripts/query.py "<question>" --strategy reranked --answer --show-context
.venv/bin/python -m pytest
PYTHONPYCACHEPREFIX=/tmp/techrag-pycache .venv/bin/python -m compileall -q app scripts tests
git diff --check
.venv/bin/python -m pip check
shasum -a 256 evaluation/dataset.json evaluation/results/dense.json evaluation/results/hybrid.json evaluation/results/hybrid_reranked.json
git check-ignore -v .env data/qdrant/
```

## Query 1

**Type:** fact (`q013`)

**Question:** What does score_threshold do in a Qdrant search request?

### Retrieved context

- [C1] source=`qdrant_vector_search.md`, chunk_id=`chunk_3d93bcaf4f196c4eaba319b53eeade0bf30987fe7add0e6be4ecac0b2f10c9a1`
- [C2] source=`qdrant_vector_search.md`, chunk_id=`chunk_2ab6cbd06f6e3de15c08df1239957715b8eb194bb2ba9477b596d1a5ad62d9d0`
- [C3] source=`qdrant_search_relevance.md`, chunk_id=`chunk_ed248c511d1913d3202c71270c2938ff8cf3d546ee4ed54b96fe84e69542c796`
- [C4] source=`qdrant_search_relevance.md`, chunk_id=`chunk_660999ac8beb0abeddcf77b8c65216c4074858f63979d8a66830712df0c7859c`
- [C5] source=`qdrant_search_relevance.md`, chunk_id=`chunk_b961831acdd857595db006f11518f4d6a5d8d7ac9e998de92d4b79a17d0bb86e`

### Generated answer

> The `score_threshold` parameter in a Qdrant search request is used to exclude results with a score worse than the given threshold. It filters out results that do not meet the specified similarity score, which can be based on the used metric. This parameter may exclude lower or higher scores depending on the metric, as higher scores of the Euclidean metric are considered more distant and thus excluded [C1][C2].<|im_end|>

### Parsed citations

- [C1] -> chunk_id=`chunk_3d93bcaf4f196c4eaba319b53eeade0bf30987fe7add0e6be4ecac0b2f10c9a1`
- [C2] -> chunk_id=`chunk_2ab6cbd06f6e3de15c08df1239957715b8eb194bb2ba9477b596d1a5ad62d9d0`

### Invalid citations

None.

### Manual assessment

- Grounding: Good
- Citation syntax validity: Good
- Citation semantic correctness: Good
- Unsupported-claim behavior: Good

### Notes

The labeled evaluation chunk was retrieved as C2. The answer reflects the documented metric-dependent threshold direction. End-to-end CLI latency was approximately 22.60 seconds.

## Query 2

**Type:** multi_chunk (`q025`)

**Question:** Compare Qdrant's must, should, and must_not filtering clauses.

### Retrieved context

- [C1] source=`qdrant_filtering.md`, chunk_id=`chunk_c4ee9e989a7808f00c5a4966fa1be673254072a3e0bbea0446590bd1e08feebf`
- [C2] source=`qdrant_filtering.md`, chunk_id=`chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9`
- [C3] source=`qdrant_filtering.md`, chunk_id=`chunk_46234ee4cf4574915dc7c0c65e651d1e6ebe240ff12ef1e9e4c9dac9a43895e8`
- [C4] source=`qdrant_filtering.md`, chunk_id=`chunk_10f7f680ea1f254d70ca96b95847982ed72e3c166d190625d6967dcf39eb46ca`
- [C5] source=`qdrant_filtering.md`, chunk_id=`chunk_67dfc506017e8700771afc3d03c08e33123053c97c1815e07c3f73b32fdb059b`

### Generated answer

> Qdrant's filtering clauses `must`, `should`, and `must_not` are used to define conditions for filtering search results. Here's a comparison:
>
> 1. **`must`**: This clause is used to specify conditions that must be satisfied for a point to be included in the results. It is equivalent to the logical AND operator, meaning all conditions within `must` must be true for the point to be included [C1][C3].
>
> 2. **`should`**: This clause is used to specify conditions that should be satisfied, but it is equivalent to the logical OR operator. This means that at least one of the conditions within `should` needs to be true for the point to be included in the results [C3].
>
> 3. **`must_not`**: This clause is used to specify conditions that must not be satisfied. It is equivalent to the logical NOT operator applied to each condition within `must_not`, meaning all conditions within `must_not` must be false for the point to be included in the results [C1][C3].
>
> These clauses can be combined and nested to create complex filtering conditions, allowing for precise control over which points are returned in search results.<|im_end|>

### Parsed citations

- [C1] -> chunk_id=`chunk_c4ee9e989a7808f00c5a4966fa1be673254072a3e0bbea0446590bd1e08feebf`
- [C3] -> chunk_id=`chunk_46234ee4cf4574915dc7c0c65e651d1e6ebe240ff12ef1e9e4c9dac9a43895e8`

### Invalid citations

None.

### Manual assessment

- Grounding: Good
- Citation syntax validity: Good
- Citation semantic correctness: Good
- Unsupported-claim behavior: Partial

### Notes

The three clause descriptions are supported by the supplied filtering chunks. The final sentence about combining and nesting is uncited, so citation completeness is imperfect even though no invalid label was emitted. End-to-end CLI latency was approximately 27.90 seconds.

## Query 3

**Type:** cross_document (`q039`)

**Question:** When would an application use a Transformers Pipeline directly instead of a Text Embeddings Inference server?

### Retrieved context

- [C1] source=`huggingface_text_embeddings_inference.md`, chunk_id=`chunk_88acf2e84e52b7fc08a9e4d8c192e58752cf204ff470b0e62090af7b9d041c5e`
- [C2] source=`huggingface_pipeline_tutorial.md`, chunk_id=`chunk_64c08ef9caee05d1cd40f44ee39c612dd1e8c9398f90bce428cfd0cd4b2c662a`
- [C3] source=`huggingface_pipeline_tutorial.md`, chunk_id=`chunk_27822ef34f658c4cd363f1944247289ac26fda50bd962373b2fee1a78bcfbc01`
- [C4] source=`huggingface_text_embeddings_inference.md`, chunk_id=`chunk_45e5cbdf579dcb31c0aa2de3736dbf6936c507a56b191bdf3aa9411328fd3651`
- [C5] source=`huggingface_pipeline_tutorial.md`, chunk_id=`chunk_d1180e8d6ffd5cce2f77e63f9a9f9f1332b94b7582a8c9c029a86e012847ea45`

### Generated answer

> An application would use a Transformers Pipeline directly instead of a Text Embeddings Inference server when the application requires fine-grained control over the model execution, such as when running on local hardware (e.g., Macs with Apple Silicon) or when deploying in environments where lightweight and quick setup is essential [C2]. Additionally, if the application needs to process inputs in a batch or requires specific configurations like using half-precision weights for memory optimization, the Transformers Pipeline provides these capabilities directly [C3]. The Transformers Pipeline is also suitable for scenarios where the application needs to integrate with other systems or workflows without the overhead of deploying a dedicated server [C2].<|im_end|>

### Parsed citations

- [C2] -> chunk_id=`chunk_64c08ef9caee05d1cd40f44ee39c612dd1e8c9398f90bce428cfd0cd4b2c662a`
- [C3] -> chunk_id=`chunk_27822ef34f658c4cd363f1944247289ac26fda50bd962373b2fee1a78bcfbc01`

### Invalid citations

None.

### Manual assessment

- Grounding: Partial
- Citation syntax validity: Good
- Citation semantic correctness: Partial
- Unsupported-claim behavior: Poor

### Notes

The answer uses Pipeline documentation but does not cite either supplied TEI chunk when making the comparison. Claims about lightweight setup, workflow integration, and dedicated-server overhead are not clearly established by C2 or C3. The hardware and batching details are more directly supported. End-to-end CLI latency was approximately 21.92 seconds.

## Query 4

**Type:** unsupported

**Question:** What is TechRAG's production uptime SLA?

### Retrieved context

- [C1] source=`huggingface_text_embeddings_inference.md`, chunk_id=`chunk_88acf2e84e52b7fc08a9e4d8c192e58752cf204ff470b0e62090af7b9d041c5e`
- [C2] source=`huggingface_text_embeddings_inference.md`, chunk_id=`chunk_91886f8dfcacd49ebef6dff8176cb02b7e42ce717d47fd6ceeedc343f7d9f183`
- [C3] source=`qdrant_vector_search.md`, chunk_id=`chunk_c009ce573faa73149f54c4673a75779ef3616b8e15f771968c3ebfe2423c94fb`
- [C4] source=`huggingface_text_embeddings_inference.md`, chunk_id=`chunk_7ffa981170563b610d3194fc459ad18eb4b7afe658436477626e3525af35ff93`
- [C5] source=`qdrant_search_relevance.md`, chunk_id=`chunk_bbafb92a600de310fa17d990a4e3bcd44bdf6a709fb9e9b347bdd507f8b68ac3`

### Generated answer

> The provided documentation does not contain enough information to answer this reliably.<|im_end|>

### Parsed citations

None.

### Invalid citations

None.

### Manual assessment

- Grounding: Good
- Citation syntax validity: Good
- Citation semantic correctness: Good
- Unsupported-claim behavior: Good

### Notes

The retrieved chunks do not describe TechRAG's production SLA. The model used the prescribed insufficient-context response and did not fabricate a value or citation. End-to-end CLI latency was approximately 15.38 seconds.

## Performance Observation

The measured wall times were 22.60, 27.90, 21.92, and 15.38 seconds on the local MacBook Pro M5 / 24 GB after the Qwen model was downloaded and loaded. These are end-to-end CLI times and include per-process embedding and reranker initialization plus retrieval, prompt processing, generation, citation parsing, and printing. Isolated generation-only latency was not instrumented, so these values are upper bounds rather than model benchmarks. Model download and server model-load time are excluded.

## Citation Checks

- Every parsed `[C#]` label mapped to one of the supplied top-five chunks.
- No unknown citation label was emitted or silently accepted.
- Query 1's citations plausibly support its threshold claims.
- Query 2's citations plausibly support the clause descriptions, but the final general claim is uncited.
- Query 3 has valid citation syntax but only partial semantic support for its comparative recommendations.
- Query 4 correctly has no citations because it abstains.

## Validation

- `python -m pytest`: 71 passed, 6 warnings.
- `python -m compileall app scripts tests`: passed.
- `git diff --check`: passed.
- `pip check`: no broken requirements found.
- `.env`: ignored by `.gitignore`.
- `data/qdrant/`: ignored by `.gitignore`.
- Hugging Face/MLX model cache: outside the repository and untracked.

Frozen baseline SHA-256 values remained unchanged:

- Evaluation dataset: `efc13a01af34b6c7f292b44c6d6e04a8cf7f1e06b7ba5acdd7a56a8c38d0c600`
- Dense results: `509f1272c912be0c5c6f9723d2487ee304f97206880ddd528198d35feacf7e4f`
- Hybrid results: `359df3832415b37fa25124b8cc5953cfcab4234777a67a3911e8ac5e5940077d`
- Reranked results: `82817ac4e2221ed4c1fe6f2f5fe62b80ffa559bbd4c5a86d91c1f46f7c56e1ab`

## Observations and Manual Review

- The real local model completed the full retrieval-to-citation pipeline for all four queries.
- Grounding judgments: 3 Good, 1 Partial, 0 Poor.
- Overall citation-validity judgments: 2 Good, 2 Partial, 0 Poor when syntax, semantics, and completeness are considered together.
- The unsupported-query behavior was Good: the model abstained without citations.
- Cross-document comparative generation needs formal evaluation; one smoke result contained plausible but weakly supported recommendations.
- MLX-LM 0.29.1's visible `<|im_end|>` response suffix needs a compatibility decision. Adding provider-specific cleanup to TechRAG was intentionally deferred.
- The recurring `urllib3` LibreSSL warning is unrelated to generation correctness but should be reviewed if this Python 3.9 environment will make external HTTPS requests.

This smoke test establishes technical end-to-end operability only. It does not establish generation quality.
