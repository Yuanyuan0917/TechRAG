# Dense Retrieval Baseline Evaluation

## Purpose

Establish a reproducible quantitative baseline for the existing dense retriever before implementing or comparing hybrid retrieval and reranking. No corpus, query, chunking, embedding, similarity, or retrieval setting was tuned after observing the results.

## Dataset

The frozen corpus contains 10 official technical documents and 212 chunks. Source titles, projects, retrieval dates, and commit-pinned URLs are recorded in [`data/SOURCES.md`](../data/SOURCES.md).

The evaluation dataset contains 40 manually written and corpus-grounded questions:

| Type | Questions | Share |
| --- | ---: | ---: |
| Fact | 18 | 45% |
| Multi-chunk | 12 | 30% |
| Cross-document | 10 | 25% |

Each question has a concise reference answer, deterministic relevant document and chunk IDs, and manually assigned chunk relevance. A grade of `2` means the chunk directly answers the question; `1` means it provides material supporting context. The human-readable labels and excerpts are in [`evaluation/dataset_review.md`](../evaluation/dataset_review.md).

Before retrieval, the runner fails on duplicate question IDs or text, unsupported types, missing references, invalid grades, stale document/chunk IDs, and chunk/document mismatches. All 40 questions passed these integrity checks against the frozen corpus.

## Fixed Configuration

| Setting | Value |
| --- | --- |
| Evaluation date | 2026-08-20 |
| Python | 3.9.6 |
| Embedding model | `sentence-transformers/all-MiniLM-L6-v2` |
| Chunk size | 1,000 characters |
| Chunk overlap | 200 characters |
| Similarity | Cosine |
| Qdrant mode | Local persistent |
| Qdrant path | `data/qdrant` |
| Collection | `techrag_chunks` |
| Retrieval depth | 10 |
| Corpus | 10 documents / 212 chunks |
| Questions | 40 |

## Metrics

- **Recall@k:** relevant chunk IDs found in the first `k` results divided by all manually labeled relevant chunk IDs, averaged across questions.
- **MRR:** reciprocal rank of the first relevant chunk within the retrieved top 10, or zero when none is retrieved, averaged across questions.
- **nDCG@5:** DCG divided by ideal DCG at rank 5 using gain `2^relevance - 1` for the manually assigned grades. Duplicate retrieved IDs receive gain only once; a query with no useful gain returns zero rather than NaN.

The primary metrics are Recall@5, MRR, and nDCG@5. Recall@1 and Recall@10 are included for context.

## Results

| Metric | Dense baseline |
| --- | ---: |
| Recall@1 | 0.247917 |
| **Recall@5** | **0.510833** |
| Recall@10 | 0.670000 |
| **MRR** | **0.590030** |
| **nDCG@5** | **0.451834** |

The complete unrounded measurements, scores, rankings, relevant IDs, and per-query metrics are saved in [`evaluation/results/dense.json`](../evaluation/results/dense.json).

## Results by Question Type

| Type | Questions | Recall@1 | Recall@5 | Recall@10 | MRR | nDCG@5 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Fact | 18 | 0.416667 | 0.666667 | 0.777778 | 0.660714 | 0.569863 |
| Multi-chunk | 12 | 0.090278 | 0.412500 | 0.669444 | 0.475694 | 0.360305 |
| Cross-document | 10 | 0.133333 | 0.348333 | 0.476667 | 0.600000 | 0.349219 |

Fact questions retrieved a larger share of their labeled evidence than the other types. Cross-document MRR is higher than its Recall@5 because a relevant chunk often appears early while other relevant chunks from the comparison remain absent. Multi-chunk Recall increases substantially between ranks 5 and 10, but the low Recall@1 reflects that one result cannot cover several labeled passages.

## Failure Cases

### q010 — Qdrant `Match Any`

- **Question:** When does a Qdrant Match Any payload condition succeed?
- **Expected:** `qdrant_filtering.md`, chunk 7 (`chunk_2f181aae2739cf2e7c91798c7d9fd915848089a40f3000874977a2e6c9952cf2`), which states the matching condition.
- **Top results:** filtering frontmatter/overview (`chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9`), general filtering/indexing guidance (`chunk_60e454d80cf03c03c89ebf1b5d7aa74e47c5c50e8430dc07d01b5fda5effa63c`), then a relevance-feedback passage (`chunk_3c9129c52efb9993a4853dbadb153f8d2989efb503d6be55acce38d0578573e0`).
- **Outcome:** no labeled chunk in the top 10.
- **Likely category:** frontmatter/noise and focused passage outside top-k. The official source uses a shortcode where the code example would appear, which may reduce the local evidence available to the embedder.

### q013 — Qdrant `score_threshold`

- **Question:** What does `score_threshold` do in a Qdrant search request?
- **Expected:** `qdrant_vector_search.md`, chunk 10 (`chunk_2ab6cbd06f6e3de15c08df1239957715b8eb194bb2ba9477b596d1a5ad62d9d0`).
- **Top results:** two score/feedback passages from `qdrant_search_relevance.md` (`chunk_3c9129c52efb9993a4853dbadb153f8d2989efb503d6be55acce38d0578573e0`, `chunk_b961831acdd857595db006f11518f4d6a5d8d7ac9e998de92d4b79a17d0bb86e`), followed by a nearby vector-search behavior chunk (`chunk_3d93bcaf4f196c4eaba319b53eeade0bf30987fe7add0e6be4ecac0b2f10c9a1`).
- **Outcome:** no labeled chunk in the top 10.
- **Likely category:** semantic ambiguity. General score-related passages outranked the precise parameter definition.

### q023 — Starting and querying Text Embeddings Inference

- **Question:** What steps and configuration are involved in starting Text Embeddings Inference and requesting an embedding?
- **Expected:** TEI chunks 10 and 11 (`chunk_932fdb9a277cfdeff13cdb952d4e871597fa55623430b160efcb15548536c9a3`, `chunk_bb5d240b51ad3e3deb3234193c79abecc9464d11ac6f6c21ecd5f316b8ccdccd`) covering container startup, request, and model ID.
- **Top results:** three Sentence Transformers overview chunks about embedding models and local examples (`chunk_3f5df0268c752247091a3728d871f54b99d5caeba3db70efd302359a8c6756cc`, `chunk_30cbd154b92eedaf317578819825a0bf77465f5dc606df6bcc4bf4e679fee357`, `chunk_464bc98da7e8879d2635d9eb9580dc9f94c6582d606c2a654f4a90d3c65ddc1d`).
- **Outcome:** no labeled chunk in the top 10.
- **Likely category:** cross-document confusion and lexical mismatch. The query's broad embedding language matched model overview material more strongly than the deployment commands.

### q036 — Business signals after hybrid retrieval

- **Question:** How can Qdrant apply business signals after a hybrid retrieval stage?
- **Expected:** four chunks across hybrid-query and search-relevance documents describing fusion, formula rescoring, payload/condition inputs, and calibration: `chunk_a7ed49b61fa12fd52b85a03f1fbc25e6de3bb6daba60e853c0edc5909a5bc4da`, `chunk_68fead02254360d99f7653254b8ad4865b2a5f2a88a56eed779ce1f3b88d4bec`, `chunk_660999ac8beb0abeddcf77b8c65216c4074858f63979d8a66830712df0c7859c`, and `chunk_6d7706c757314b6b3748e0b8626fb8919385688cd9d5872c5b558f8b077e2b7c`.
- **Top results:** a related feedback-model passage (`chunk_b961831acdd857595db006f11518f4d6a5d8d7ac9e998de92d4b79a17d0bb86e`), a broad Query API passage (`chunk_b25a05265a1716f196444b59a292327a26563d7a47e76d73082e3cc0e1b106d7`), and another feedback-score passage (`chunk_3c9129c52efb9993a4853dbadb153f8d2989efb503d6be55acce38d0578573e0`).
- **Outcome:** none of the four labeled chunks appeared in the top 10, although the returned material was topically related.
- **Likely category:** semantic ambiguity and cross-document confusion. The broad wording admits several Qdrant rescoring mechanisms.

### q037 — Reproducible evaluation guidance

- **Question:** What corpus guidance helps keep retrieval evaluation reproducible and avoids tuning bias?
- **Expected:** three chunks across Qdrant hybrid-query and vector-search documents covering fixed evaluation splits, retesting, and reproducible sampling: `chunk_2a106c2dfaf96b7f2e68d71f3125c76a6a3e0f3cbe501a36ad0c34fb654cd5e1`, `chunk_2d04fab5dc6136820f1389a9fca36d962bd7d97d40115917270aa10060c0cfaf`, and `chunk_898688bf990e34cdc55f47c24c42ca0a948d72069a895f6ab9b13b0ff55631ae`.
- **Top results:** Sentence Transformers example-dataset and retrieve/rerank passages (`chunk_62596d162f72d39a62714058316f7eb1a0267f72501b85a8e0e03255e16d13d2`, `chunk_b695c1d3749ee3365c1077023f0b3aeb3d24ae1e9b34e53e47288ee8f69f3b10`, `chunk_5d1888374f003ec75ae4929befb69aa3e999258614424b03ea635ad632144185`).
- **Outcome:** no labeled chunk in the top 10.
- **Likely category:** lexical mismatch. The terms “corpus” and “evaluation” favored dataset/example material rather than the more specific evaluation-process guidance. This explanation is a hypothesis based on the retrieved text.

## Observations

- Recall rises from 0.510833 at rank 5 to 0.670000 at rank 10, so a material portion of labeled evidence is retrieved late rather than entirely absent.
- Fact questions have the strongest measured Recall@5 and nDCG@5. Multi-chunk and cross-document questions expose evidence-coverage limitations more clearly.
- Broad or related passages can rank ahead of narrowly relevant parameter definitions. This is visible in the `Match Any` and `score_threshold` failures and is consistent with the earlier smoke-test observation about broad/frontmatter chunks.
- Cross-document questions can have a strong first relevant hit but incomplete coverage; this explains the gap between cross-document MRR (0.600000) and Recall@5 (0.348333).
- Fixed-size boundaries and source-site shortcodes remain visible in labeled and retrieved chunks. Their precise causal impact cannot be isolated by this evaluation alone.

These results describe only this frozen corpus and label set; they do not establish general retrieval quality or superiority over another method.

## Limitations

- The corpus is intentionally small and limited to 10 AI/ML engineering documents.
- Relevance judgments were made manually by one annotator and require independent review.
- Some questions have multiple relevant chunks, so query-level recall is sensitive to annotation breadth.
- MRR is truncated at retrieval depth 10.
- No confidence intervals, statistical significance tests, or alternate retrieval baselines are included.
- Stored official Markdown includes frontmatter, shortcodes, and fixed-size boundary artifacts from the unchanged ingestion baseline.

## Next Step

Use this frozen dataset, corpus, configuration, and result schema as the comparison point for a separately implemented hybrid retrieval experiment. Keep the dense result unchanged, evaluate the new strategy on the same labels, and inspect per-type and per-query deltas before considering any tuning.
