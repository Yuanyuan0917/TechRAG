# Dense Retrieval Smoke Test

## Purpose

Validate the current dense retrieval baseline on a small real technical-document corpus before building formal evaluation infrastructure. This is a qualitative smoke test, not a benchmark.

## Environment

- Date: 2026-08-20
- Python: 3.9.6
- Embedding model: `sentence-transformers/all-MiniLM-L6-v2`
- Model availability: cache directory existed before the run; no model-weight download was observed, but online Hugging Face metadata access was required for indexing
- Vector store: Qdrant local persistent mode
- Collection: `techrag_chunks`
- Qdrant path: `data/qdrant/`
- Similarity metric: cosine
- Chunk size: 1000 characters
- Chunk overlap: 200 characters
- Query `top_k`: 5
- Corpus size: 4 documents, 64,184 parsed characters
- Number of chunks: 81
- Indexed Qdrant points: 81

## Corpus

The corpus contains four commit-pinned official Markdown documents from Sentence Transformers, Qdrant, and FastAPI. Full provenance is recorded in [`data/SOURCES.md`](../data/SOURCES.md).

| File | Parsed characters | Chunks |
| --- | ---: | ---: |
| `fastapi_dependencies.md` | 9,768 | 12 |
| `qdrant_filtering.md` | 22,311 | 28 |
| `qdrant_search_relevance.md` | 14,745 | 19 |
| `sentence_transformers_overview.md` | 17,360 | 22 |
| **Total** | **64,184** | **81** |

All four documents parsed successfully. No empty or anomalously large document was found.

## Commands

Ingestion inspection:

```bash
.venv/bin/python scripts/ingest.py data/raw/
```

Reset, embedding, and indexing:

```bash
.venv/bin/python scripts/ingest.py data/raw/ --index --reset-index
```

The first sandboxed indexing attempt could not resolve `huggingface.co` for model metadata and was interrupted during retries. The identical command succeeded with network access enabled. Stored count was confirmed with:

```bash
.venv/bin/python -c "from app.retrieval.vector_store import QdrantVectorStore; store=QdrantVectorStore(); print(store.collection_name, store.count()); store.close()"
```

Queries used the real cached model with network access disabled after successful indexing:

```bash
env HF_HUB_OFFLINE=1 .venv/bin/python scripts/query.py "How do you create embeddings with Sentence Transformers?" --top-k 5
```

```bash
env HF_HUB_OFFLINE=1 .venv/bin/python scripts/query.py "What do Qdrant must, should, and must_not filtering clauses mean?" --top-k 5
```

```bash
env HF_HUB_OFFLINE=1 .venv/bin/python scripts/query.py "How can Qdrant match payload values with Match Any or Match Except?" --top-k 5
```

```bash
env HF_HUB_OFFLINE=1 .venv/bin/python scripts/query.py "How does Qdrant Formula Query use $score and payload values for score boosting?" --top-k 5
```

```bash
env HF_HUB_OFFLINE=1 .venv/bin/python scripts/query.py "How can search results be restricted by business rules that vectors cannot represent?" --top-k 5
```

```bash
env HF_HUB_OFFLINE=1 .venv/bin/python scripts/query.py "How does FastAPI supply shared database connections or authentication requirements to path operations?" --top-k 5
```

```bash
env HF_HUB_OFFLINE=1 .venv/bin/python scripts/query.py "What is the difference between embedding models and CrossEncoder reranker models?" --top-k 5
```

```bash
env HF_HUB_OFFLINE=1 .venv/bin/python scripts/query.py "How are similarity scores used to order search results?" --top-k 5
```

```bash
env HF_HUB_OFFLINE=1 .venv/bin/python scripts/query.py "How can metadata influence search results or application behavior?" --top-k 5
```

```bash
env HF_HUB_OFFLINE=1 .venv/bin/python scripts/query.py "What does Depends do and how are dependencies included in OpenAPI?" --top-k 5
```

Validation:

```bash
env PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest
env PYTHONPYCACHEPREFIX=/private/tmp/techrag-corpus-pycache .venv/bin/python -m compileall app scripts tests
git diff --check
.venv/bin/python -m pip check
git check-ignore -v data/qdrant/
git status
git diff
```

## Query Results

### Query 1

**Query:** How do you create embeddings with Sentence Transformers?

**Top results:**

1. source=`sentence_transformers_overview.md`
   score=0.6935
   chunk_id=`chunk_30cbd154b92eedaf317578819825a0bf77465f5dc606df6bcc4bf4e679fee357`
   preview=ode, Codex, Cursor, Gemini CLI, ...)? Install the [`train-sentence-transformers`](skills/) Hugging Face Agent Skill via `hf skills add train-sentence-transformers [--claude] [--global]` and ask your agent to fine-tune a model on your data.…

2. source=`sentence_transformers_overview.md`
   score=0.6731
   chunk_id=`chunk_b8e00336e349a014f2a034f36498de7b65a2f63853969a38942bace3ba755af0`
   preview=ransformers ``` See [Installation](https://www.sbert.net/docs/installation.html) in the docs for uv, conda, source, and editable installs, CUDA setup, and extras (`[image]`, `[audio]`, `[video]`, `[train]`, `[onnx]`, `[openvino]`, `[dev]`)…

3. source=`sentence_transformers_overview.md`
   score=0.6654
   chunk_id=`chunk_b651190dc991598f552ad3b5c19153cb5143cc5b30867ce73d946efe43655fec`
   preview=ditionally, it is easy to train or finetune your own [embedding models](https://sbert.net/docs/sentence_transformer/training_overview.html), [reranker models](https://sbert.net/docs/cross_encoder/training_overview.html), [sparse encoder mo…

4. source=`sentence_transformers_overview.md`
   score=0.6583
   chunk_id=`chunk_f3fa2e0592d516eeea1bf6b31bc155faa1cbc5c35843247cf70ee1a7e7135ca0`
   preview=Vector Encoder models ([quickstart](https://sbert.net/docs/quickstart.html#multi-vector-encoder)). This unlocks a wide range of applications, including [semantic search](https://sbert.net/examples/applications/semantic-search/README.html),…

5. source=`sentence_transformers_overview.md`
   score=0.6565
   chunk_id=`chunk_b669baf1a3cf055bcc60e0d91cc47ab840b3e4ac084887bb9104a831908f5104`
   preview=ginally developed by the [Ubiquitous Knowledge Processing (UKP) Lab](https://www.ukp.tu-darmstadt.de/) at TU Darmstadt. We're grateful for their foundational work and continued contributions to the field. > This repository contains experim…

**Manual assessment:** Partial

**Notes:** The correct Sentence Transformers document occupies all five ranks, and the embedding example is near the top, but an agent-skill chunk ranks first.

### Query 2

**Query:** What do Qdrant must, should, and must_not filtering clauses mean?

**Top results:**

1. source=`qdrant_filtering.md`
   score=0.5531
   chunk_id=`chunk_60e454d80cf03c03c89ebf1b5d7aa74e47c5c50e8430dc07d01b5fda5effa63c`
   preview=uirements: stock availability, user location, or desired price range. <aside role="status"> For performant filtering, create <a href="/documentation/manage-data/indexing/#payload-index">payload indexes</a> for the fields you plan to filter…

2. source=`qdrant_filtering.md`
   score=0.4918
   chunk_id=`chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9`
   preview=--- title: Filtering short_description: "Combine vector similarity with payload filters in Qdrant to enforce business rules and refine search results." description: "Filter Qdrant search results with payload conditions on metadata and IDs,…

3. source=`qdrant_filtering.md`
   score=0.4694
   chunk_id=`chunk_c4ee9e989a7808f00c5a4966fa1be673254072a3e0bbea0446590bd1e08feebf`
   preview=ense, `must_not` is equivalent to the expression `(NOT A) AND (NOT B) AND (NOT C)`. Example: {{< code-snippet path="/documentation/headless/snippets/scroll-points/with-must-not-filter/" >}} Filtered points would be: ```json [ { "id": 5, "c…

4. source=`qdrant_filtering.md`
   score=0.4319
   chunk_id=`chunk_67dfc506017e8700771afc3d03c08e33123053c97c1815e07c3f73b32fdb059b`
   preview=rray element within the payload. Nested filters work in the same way as if the nested filter was applied to a single element of the array at a time. Parent document is considered to match the condition if at least one element of the array …

5. source=`qdrant_filtering.md`
   score=0.3814
   chunk_id=`chunk_10f7f680ea1f254d70ca96b95847982ed72e3c166d190625d6967dcf39eb46ca`
   preview=s://qdrant.tech/documentation"`, but the prefix `"qdrant"` does not. Matching is byte-wise and, for valid UTF-8 strings, therefore character-wise. It is also case-sensitive, consistent with exact keyword matching. Unlike [Full Text Match](…

**Manual assessment:** Good

**Notes:** Filtering documentation dominates the ranking; the clause overview and `must_not` explanation are both present near the top.

### Query 3

**Query:** How can Qdrant match payload values with Match Any or Match Except?

**Top results:**

1. source=`qdrant_filtering.md`
   score=0.6776
   chunk_id=`chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9`
   preview=--- title: Filtering short_description: "Combine vector similarity with payload filters in Qdrant to enforce business rules and refine search results." description: "Filter Qdrant search results with payload conditions on metadata and IDs,…

2. source=`qdrant_filtering.md`
   score=0.6261
   chunk_id=`chunk_60e454d80cf03c03c89ebf1b5d7aa74e47c5c50e8430dc07d01b5fda5effa63c`
   preview=uirements: stock availability, user location, or desired price range. <aside role="status"> For performant filtering, create <a href="/documentation/manage-data/indexing/#payload-index">payload indexes</a> for the fields you plan to filter…

3. source=`qdrant_filtering.md`
   score=0.5592
   chunk_id=`chunk_67dfc506017e8700771afc3d03c08e33123053c97c1815e07c3f73b32fdb059b`
   preview=rray element within the payload. Nested filters work in the same way as if the nested filter was applied to a single element of the array at a time. Parent document is considered to match the condition if at least one element of the array …

4. source=`qdrant_filtering.md`
   score=0.5256
   chunk_id=`chunk_1171fd126b59204972d153645236057db9c263eee8ad304b7407cd897ac5b7f7`
   preview=/documentation/manage-data/payload/#keyword) and [integer](/documentation/manage-data/payload/#integer) payloads. Example: {{< code-snippet path="/documentation/headless/snippets/filter-condition/match-except/" >}} In this example, the con…

5. source=`qdrant_filtering.md`
   score=0.5221
   chunk_id=`chunk_10f7f680ea1f254d70ca96b95847982ed72e3c166d190625d6967dcf39eb46ca`
   preview=s://qdrant.tech/documentation"`, but the prefix `"qdrant"` does not. Matching is byte-wise and, for valid UTF-8 strings, therefore character-wise. It is also case-sensitive, consistent with exact keyword matching. Unlike [Full Text Match](…

**Manual assessment:** Partial

**Notes:** All results come from the correct filtering document, but the focused Match Except chunk appears at rank 4 behind broader filtering chunks.

### Query 4

**Query:** How does Qdrant Formula Query use $score and payload values for score boosting?

**Top results:**

1. source=`qdrant_search_relevance.md`
   score=0.7061
   chunk_id=`chunk_3c9129c52efb9993a4853dbadb153f8d2989efb503d6be55acce38d0578573e0`
   preview=by the retriever. - `score`, the feedback score. 3. A definition of the formula that modifies retrieval based on the feedback (`strategy`). {{< code-snippet path="/documentation/headless/snippets/query-points-explore/relevance-feedback-nai…

2. source=`qdrant_search_relevance.md`
   score=0.6837
   chunk_id=`chunk_660999ac8beb0abeddcf77b8c65216c4074858f63979d8a66830712df0c7859c`
   preview=on: - Dynamic payload values - Conditions - Scores of prefetches To express the formula, the syntax uses objects to identify each element. Taking the documentation example, the request would look like this: {{< code-snippet path="/document…

3. source=`qdrant_search_relevance.md`
   score=0.6320
   chunk_id=`chunk_b961831acdd857595db006f11518f4d6a5d8d7ac9e998de92d4b79a17d0bb86e`
   preview=rieved results: | Point ID | Retriever Similarity | Feedback Score | | --- | --- | --- | | 111 | 0.89 | 0.68 | | 222 | 0.81 | 0.72 | | 333 | 0.77 | 0.61 | The feedback model considers the second result with ID 222 to be the most relevant, …

4. source=`qdrant_search_relevance.md`
   score=0.5997
   chunk_id=`chunk_bb20c5f5bfb22110eba747193115f96a505aa25132e576bf4327f6fbb0dc96e4`
   preview=aive-strategy) need to be customized for each triplet of retriever, feedback model, and collection. To get these 3 weights adapted to your setup, use [our open source Python package](https://pypi.org/project/qdrant-relevance-feedback/). <a…

5. source=`qdrant_search_relevance.md`
   score=0.5870
   chunk_id=`chunk_ed248c511d1913d3202c71270c2938ff8cf3d546ee4ed54b96fe84e69542c796`
   preview=--- title: Search Relevance short_description: "Tune Qdrant search relevance with custom scoring, payload-based ranking, and business-aware result ordering." description: "Tune search relevance in Qdrant by adjusting scoring, applying payl…

**Manual assessment:** Good

**Notes:** The search-relevance document fills the ranking, with the Formula Query details at rank 2; rank 1 is adjacent relevance-feedback material.

### Query 5

**Query:** How can search results be restricted by business rules that vectors cannot represent?

**Top results:**

1. source=`qdrant_filtering.md`
   score=0.4503
   chunk_id=`chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9`
   preview=--- title: Filtering short_description: "Combine vector similarity with payload filters in Qdrant to enforce business rules and refine search results." description: "Filter Qdrant search results with payload conditions on metadata and IDs,…

2. source=`qdrant_search_relevance.md`
   score=0.4453
   chunk_id=`chunk_03bc9339b320b54d706ca43b51c994a8d156c2437019eec56e8ecdd1416ff6b0`
   preview=business logic needs to be considered for ranking the final list of results. A quick example is [our own documentation search bar](https://github.com/qdrant/page-search). It has vectors for every part of the documentation site. If one were…

3. source=`qdrant_search_relevance.md`
   score=0.4073
   chunk_id=`chunk_dac54b8a64f99694d50519695bd723cf6014b1c28324228976f4af25c6b5ce66`
   preview=ermine the relevance of search results. --- The idea behind using relevance feedback-based retrieval is the following: 1. Run a basic nearest neighbors search. Let's call its results **Retriever Similarity** and the algorithm behind this s…

4. source=`qdrant_search_relevance.md`
   score=0.3974
   chunk_id=`chunk_ed248c511d1913d3202c71270c2938ff8cf3d546ee4ed54b96fe84e69542c796`
   preview=--- title: Search Relevance short_description: "Tune Qdrant search relevance with custom scoring, payload-based ranking, and business-aware result ordering." description: "Tune search relevance in Qdrant by adjusting scoring, applying payl…

5. source=`qdrant_search_relevance.md`
   score=0.3930
   chunk_id=`chunk_b908b95dfb4b9f2acf68df5ba7d2336e5837f914484882b2075d1e793e151b66`
   preview=vector. This means that the response will not be ordered by score, but rather by the order of selection of MMR. ## Relevance Feedback *Available as of 1.17* Relevance feedback distills signals from current search results into the next retr…

**Manual assessment:** Good

**Notes:** The filtering overview that directly discusses non-vector business requirements ranks first, followed by related business-aware ranking material.

### Query 6

**Query:** How does FastAPI supply shared database connections or authentication requirements to path operations?

**Top results:**

1. source=`fastapi_dependencies.md`
   score=0.5491
   chunk_id=`chunk_84db9f7209fe38a87fab17a30d3360a38009d1b7df4b9450217ebb3c7ff19105`
   preview=ction system makes **FastAPI** compatible with: * all the relational databases * NoSQL databases * external packages * external APIs * authentication and authorization systems * API usage monitoring systems * response data injection system…

2. source=`fastapi_dependencies.md`
   score=0.5203
   chunk_id=`chunk_4acf3cdaa3c378a4eaa3f33b9fde2a2e5c7ccdc44c12e15e71153ae1c1042ed5`
   preview=* injectables * components ## **FastAPI** plug-ins { #fastapi-plug-ins } Integrations and "plug-ins" can be built using the **Dependency Injection** system. But in fact, there is actually **no need to create "plug-ins"**, as by using depen…

3. source=`fastapi_dependencies.md`
   score=0.4875
   chunk_id=`chunk_e20b19f85be3bb2ad4a48e82dbde5b128d82ad6a46633de0bdeeb6626ef8b134`
   preview=)`. And that function takes parameters in the same way that *path operation functions* do. /// tip You'll see what other "things", apart from functions, can be used as dependencies in the next chapter. /// Whenever a new request arrives, *…

4. source=`fastapi_dependencies.md`
   score=0.4866
   chunk_id=`chunk_1aedfeace05dc6386f5efa0b4c517ad926ce622e25a40c3a79120b71e65723c1`
   preview=ge } If you look at it, *path operation functions* are declared to be used whenever a *path* and *operation* matches, and then **FastAPI** takes care of calling the function with the correct parameters, extracting the data from the request…

5. source=`fastapi_dependencies.md`
   score=0.4595
   chunk_id=`chunk_650291a57f062c2b9952069182c54be8e1b246992c87b738659aa622aa60bb72`
   preview=# Dependencies { #dependencies } **FastAPI** has a very powerful but intuitive **<dfn title="also known as components, resources, providers, services, injectables">Dependency Injection</dfn>** system. It is designed to be very simple to us…

**Manual assessment:** Good

**Notes:** All results come from FastAPI dependencies, with database/authentication compatibility and dependency mechanics ranked first and near the top.

### Query 7

**Query:** What is the difference between embedding models and CrossEncoder reranker models?

**Top results:**

1. source=`sentence_transformers_overview.md`
   score=0.5736
   chunk_id=`chunk_464bc98da7e8879d2635d9eb9580dc9f94c6582d606c2a654f4a90d3c65ddc1d`
   preview=cument_embeddings) print(scores) # tensor([[9.6037, 9.4055]]) ``` ## Pre-Trained Models We provide a large list of pretrained models for more than 100 languages. Some models are general purpose models, while others produce embeddings for s…

2. source=`sentence_transformers_overview.md`
   score=0.5477
   chunk_id=`chunk_41c5dd4ee9ff890e5e9b8ad1643b1a0ba92fe0c806443d81296513b468450d11`
   preview=- Multi-Vector (Late Interaction) Models - [Multi-Vector Encoder > Training Overview](https://www.sbert.net/docs/multi_vector_encoder/training_overview.html) - [Training examples on GitHub](https://github.com/huggingface/sentence-transform…

3. source=`sentence_transformers_overview.md`
   score=0.5314
   chunk_id=`chunk_865469e0360fadf03d8d8ac585b7cfb077109928466d6666db47fdf7bde73c36`
   preview=loss functions](https://www.sbert.net/docs/package_reference/sparse_encoder/losses.html) for sparse embedding models, allowing you to tune models specifically for semantic search, paraphrase mining, semantic similarity comparison, clusteri…

4. source=`sentence_transformers_overview.md`
   score=0.5192
   chunk_id=`chunk_3119cb0c2a7b12e9cd954a6e8b47d18c24c3626e3d3e791e1573d0435ddfa0da`
   preview=shape) # => (3, 384) ``` And that's already it. We now have numpy arrays with the embeddings, one for each text. We can use these to compute similarities. ```python similarities = model.similarity(embeddings, embeddings) print(similarities…

5. source=`sentence_transformers_overview.md`
   score=0.5088
   chunk_id=`chunk_4fb86452a7511b3fc9d93d27bb07c748a6377ba1f0dae6da3a4eb2af37009e06`
   preview=go=pypi&style=flat&color=green)][#pypi-package] --> <!--- BADGES: END ---> # Sentence Transformers: Embeddings, Retrieval, and Reranking This framework provides an easy method to compute embeddings for accessing, using, and training state-…

**Manual assessment:** Partial

**Notes:** The correct Sentence Transformers source fills the top five, but the comparison is fragmented across embedding and reranker chunks rather than surfaced as one direct explanation.

### Query 8

**Query:** How are similarity scores used to order search results?

**Top results:**

1. source=`qdrant_search_relevance.md`
   score=0.5867
   chunk_id=`chunk_b908b95dfb4b9f2acf68df5ba7d2336e5837f914484882b2075d1e793e151b66`
   preview=vector. This means that the response will not be ordered by score, but rather by the order of selection of MMR. ## Relevance Feedback *Available as of 1.17* Relevance feedback distills signals from current search results into the next retr…

2. source=`qdrant_search_relevance.md`
   score=0.5788
   chunk_id=`chunk_ed248c511d1913d3202c71270c2938ff8cf3d546ee4ed54b96fe84e69542c796`
   preview=--- title: Search Relevance short_description: "Tune Qdrant search relevance with custom scoring, payload-based ranking, and business-aware result ordering." description: "Tune search relevance in Qdrant by adjusting scoring, applying payl…

3. source=`qdrant_search_relevance.md`
   score=0.5195
   chunk_id=`chunk_dac54b8a64f99694d50519695bd723cf6014b1c28324228976f4af25c6b5ce66`
   preview=ermine the relevance of search results. --- The idea behind using relevance feedback-based retrieval is the following: 1. Run a basic nearest neighbors search. Let's call its results **Retriever Similarity** and the algorithm behind this s…

4. source=`qdrant_search_relevance.md`
   score=0.5140
   chunk_id=`chunk_03bc9339b320b54d706ca43b51c994a8d156c2437019eec56e8ecdd1416ff6b0`
   preview=business logic needs to be considered for ranking the final list of results. A quick example is [our own documentation search bar](https://github.com/qdrant/page-search). It has vectors for every part of the documentation site. If one were…

5. source=`qdrant_search_relevance.md`
   score=0.5113
   chunk_id=`chunk_b961831acdd857595db006f11518f4d6a5d8d7ac9e998de92d4b79a17d0bb86e`
   preview=rieved results: | Point ID | Retriever Similarity | Feedback Score | | --- | --- | --- | | 111 | 0.89 | 0.68 | | 222 | 0.81 | 0.72 | | 333 | 0.77 | 0.61 | The feedback model considers the second result with ID 222 to be the most relevant, …

**Manual assessment:** Good

**Notes:** All results come from Qdrant search relevance and discuss score-based ordering or explicit alternatives such as MMR.

### Query 9

**Query:** How can metadata influence search results or application behavior?

**Top results:**

1. source=`qdrant_search_relevance.md`
   score=0.3887
   chunk_id=`chunk_dac54b8a64f99694d50519695bd723cf6014b1c28324228976f4af25c6b5ce66`
   preview=ermine the relevance of search results. --- The idea behind using relevance feedback-based retrieval is the following: 1. Run a basic nearest neighbors search. Let's call its results **Retriever Similarity** and the algorithm behind this s…

2. source=`qdrant_search_relevance.md`
   score=0.3818
   chunk_id=`chunk_03bc9339b320b54d706ca43b51c994a8d156c2437019eec56e8ecdd1416ff6b0`
   preview=business logic needs to be considered for ranking the final list of results. A quick example is [our own documentation search bar](https://github.com/qdrant/page-search). It has vectors for every part of the documentation site. If one were…

3. source=`sentence_transformers_overview.md`
   score=0.3602
   chunk_id=`chunk_1a2ea5c65a9dbe1477bb5fe1bfd0a98f9d5740b308ff45b61acefa9e68f0c188`
   preview=ions/semantic_textual_similarity/README.html) - **Semantic Search** - [Dense Search](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) - [Sparse Search](https://www.sbert.net/examples/sparse_enco…

4. source=`qdrant_search_relevance.md`
   score=0.3580
   chunk_id=`chunk_b908b95dfb4b9f2acf68df5ba7d2336e5837f914484882b2075d1e793e151b66`
   preview=vector. This means that the response will not be ordered by score, but rather by the order of selection of MMR. ## Relevance Feedback *Available as of 1.17* Relevance feedback distills signals from current search results into the next retr…

5. source=`qdrant_search_relevance.md`
   score=0.3172
   chunk_id=`chunk_ed248c511d1913d3202c71270c2938ff8cf3d546ee4ed54b96fe84e69542c796`
   preview=--- title: Search Relevance short_description: "Tune Qdrant search relevance with custom scoring, payload-based ranking, and business-aware result ordering." description: "Tune search relevance in Qdrant by adjusting scoring, applying payl…

**Manual assessment:** Partial

**Notes:** Business-aware relevance material is retrieved, but the generic wording does not surface the Qdrant filtering document in the top five.

### Query 10

**Query:** What does Depends do and how are dependencies included in OpenAPI?

**Top results:**

1. source=`fastapi_dependencies.md`
   score=0.5921
   chunk_id=`chunk_bb8ad8fb21de94977a41c262b82ebae2ae96d4542e03cd1fbd746e0e652b1b85`
   preview=ions. You can use `async def` or normal `def`. And you can declare dependencies with `async def` inside of normal `def` *path operation functions*, or `def` dependencies inside of `async def` *path operation functions*, etc. It doesn't mat…

2. source=`fastapi_dependencies.md`
   score=0.4699
   chunk_id=`chunk_1aedfeace05dc6386f5efa0b4c517ad926ce622e25a40c3a79120b71e65723c1`
   preview=ge } If you look at it, *path operation functions* are declared to be used whenever a *path* and *operation* matches, and then **FastAPI** takes care of calling the function with the correct parameters, extracting the data from the request…

3. source=`fastapi_dependencies.md`
   score=0.4658
   chunk_id=`chunk_84db9f7209fe38a87fab17a30d3360a38009d1b7df4b9450217ebb3c7ff19105`
   preview=ction system makes **FastAPI** compatible with: * all the relational databases * NoSQL databases * external packages * external APIs * authentication and authorization systems * API usage monitoring systems * response data injection system…

4. source=`fastapi_dependencies.md`
   score=0.4482
   chunk_id=`chunk_650291a57f062c2b9952069182c54be8e1b246992c87b738659aa622aa60bb72`
   preview=# Dependencies { #dependencies } **FastAPI** has a very powerful but intuitive **<dfn title="also known as components, resources, providers, services, injectables">Dependency Injection</dfn>** system. It is designed to be very simple to us…

5. source=`fastapi_dependencies.md`
   score=0.4436
   chunk_id=`chunk_4acf3cdaa3c378a4eaa3f33b9fde2a2e5c7ccdc44c12e15e71153ae1c1042ed5`
   preview=* injectables * components ## **FastAPI** plug-ins { #fastapi-plug-ins } Integrations and "plug-ins" can be built using the **Dependency Injection** system. But in fact, there is actually **no need to create "plug-ins"**, as by using depen…

**Manual assessment:** Good

**Notes:** All results come from FastAPI dependencies; the top chunk spans dependency execution behavior and the OpenAPI integration section.

## Observations

- Direct topic queries consistently selected the expected source document.
- Paraphrased business-rule and dependency-injection queries retrieved the intended topic without exact source wording.
- Narrow API terminology was less consistently ordered: the Match Except passage ranked fourth, and Formula Query details ranked second behind adjacent relevance-feedback content.
- Fixed-size character chunks frequently begin or end mid-word or mid-sentence, which makes previews harder to interpret.
- Markdown frontmatter, badges, repository navigation, and Hugo shortcode placeholders remain in the indexed source. Broad frontmatter chunks sometimes rank above focused body chunks.
- The ambiguous metadata query retrieved business-aware search-relevance content but did not retrieve the filtering document in its top five.
- These ten observations are too small and manually selected to support any general retrieval-quality claim.

## Issues Found

- A pre-cached Sentence Transformers model still triggered Hugging Face metadata requests. Sandbox DNS caused the first indexing attempt to retry until interrupted; indexing succeeded unchanged once network access was enabled.
- Source-site markup and unresolved documentation shortcodes add retrieval noise.
- The runtime emits a non-failing urllib3 LibreSSL warning. Tests also emit non-failing PyMuPDF SWIG deprecation warnings.
- No parser, embedding, indexing, point-count, or query execution failure remained after network access was enabled.

## Potential Future Improvements

- Evaluate frontmatter/site-markup cleanup as a controlled preprocessing variant.
- Compare structure-aware or token-aware chunking only after formal baseline measurements exist.
- Add an explicitly documented offline-model loading mode for reproducible disconnected runs.

No baseline setting was changed in response to these observations.

## Baseline Status

The current dense pipeline is technically ready to proceed to formal evaluation: real documents passed through parsing, deterministic chunking, real MiniLM embedding, persistent Qdrant indexing, and top-k retrieval with matching chunk/point counts. This status reflects pipeline operability only; retrieval quality has not been established or compared with alternatives.

## Validation Results

- Corpus inspection: 4 documents, 81 chunks, no parser failures.
- Qdrant count: 81 points, matching the indexed chunk count.
- Query execution: 10 of 10 commands completed with five ranked results each.
- Qualitative judgments: 6 Good, 4 Partial, 0 Poor.
- Tests: 24 passed; 6 non-failing dependency warnings.
- Python compilation: passed.
- `git diff --check`: passed.
- `pip check`: no broken requirements.
- `data/qdrant/`: ignored by Git.

