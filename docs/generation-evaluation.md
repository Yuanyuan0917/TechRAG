# Generation Evaluation

## Purpose

Determine whether the frozen Dense, Hybrid, and Reranked retrieval baselines produce measurably different final answers when the question, local Qwen model, prompt, temperature, and top-five context depth remain fixed.

This is a 40-question, single-reviewer portfolio evaluation. It measures association within this controlled run; it does not establish a general causal effect.

## Experimental Setup

Each of the 40 grounded questions was generated once with each retrieval strategy:

```text
Dense top-5    -> Qwen3-8B -> answer + citations
Hybrid top-5   -> Qwen3-8B -> answer + citations
Reranked top-5 -> Qwen3-8B -> answer + citations
```

This produced 120 successful main answers. A separate five-question unsupported set was run with Reranked retrieval only.

Before each strategy's timed run, the runner executed one excluded end-to-end warmup using q001. This loaded and warmed the embedding model, Qdrant path, BM25 index where applicable, CrossEncoder where applicable, and Qwen generation path. The Qwen model was already cached and loaded by the verified MLX-LM server. Model download and initial load are excluded from latency.

## Fixed Variables

- Corpus: 10 documents, 212 deterministic chunks
- Evaluation set: 40 questions (18 fact, 12 multi-chunk, 10 cross-document)
- Chunk size / overlap: 1000 / 200 characters
- Embedding model: `sentence-transformers/all-MiniLM-L6-v2`
- Dense metric: cosine
- Qdrant: local persistent `data/qdrant`, collection `techrag_chunks`
- BM25 tokenizer: `casefold + regex [a-z0-9_]+`
- Dense / BM25 candidate depths: 20 / 20
- Fusion: reciprocal rank fusion, `k=60`
- Reranker: `cross-encoder/ms-marco-MiniLM-L-6-v2`
- Reranker candidate depth: 20
- Generation model: `Qwen/Qwen3-8B-MLX-4bit`
- MLX-LM / MLX: 0.29.1 / 0.29.3
- API: MLX-LM OpenAI-compatible `/v1/chat/completions` on `127.0.0.1:8080`
- Temperature: 0.0
- Context depth: top 5
- Qwen thinking: disabled through server chat-template arguments
- Machine: local MacBook Pro, Apple M5, 24 GB unified memory, arm64
- Python: 3.9.6

The corpus, relevance judgments, retrieval settings, generation prompt, citation labels, and model settings were not changed after results were observed.

## Output and Review Artifacts

- Raw answers: `evaluation/generation/{dense,hybrid,reranked}.json`
- Unsupported answers: `evaluation/generation/unsupported.json`
- Manual annotations: `evaluation/generation_annotations.json`
- Side-by-side review: `evaluation/generation_review.md`
- Reproducible aggregates: `evaluation/generation_summary.json`

Raw files preserve the full generated answer, full top-five chunk text, retrieval scores, parsed citations, invalid labels, answer character count, latency, and errors. The runner saves valid JSON after every question and supports resuming completed output.

## Scoring Rubric and Annotation Method

All 120 answers were directly inspected side by side against the manually grounded reference answer and the exact retrieved top-five context. No lexical-overlap heuristic, Ragas, or LLM-as-judge assigned semantic scores.

- **Answer Correctness:** 2 correct/substantially complete; 1 partially correct or materially incomplete; 0 wrong, unsupported, or failed to answer.
- **Faithfulness:** 2 all material claims supported by supplied top-five context; 1 at least one weak or unsupported material claim; 0 materially unsupported or hallucinated.
- **Citation Correctness:** 2 valid citations materially support claims; 1 partial support or important uncited claims; 0 invalid or misleading support.

Citation coverage is a manual categorical judgment (`complete`, `partial`, or `not_applicable` for abstentions), not a fabricated exact claim ratio. Twenty-one strategy/question annotations with broad synthesis or ambiguous citation support are explicitly flagged for human review.

## Aggregate Results

Means are on the raw 0–2 scale. Parentheses show counts in `score 2 / score 1 / score 0` order.

| Strategy | Answer Correctness | Faithfulness | Citation Correctness |
| --- | ---: | ---: | ---: |
| Dense | 1.250 (21 / 8 / 11) | 1.950 (38 / 2 / 0) | 1.825 (35 / 3 / 2) |
| Hybrid | 1.475 (26 / 7 / 7) | 1.800 (33 / 6 / 1) | 1.800 (33 / 6 / 1) |
| Reranked | 1.575 (26 / 11 / 3) | 1.900 (36 / 4 / 0) | 1.800 (32 / 8 / 0) |

Normalized answer correctness is 0.625 Dense, 0.7375 Hybrid, and 0.7875 Reranked. The number of fully correct answers is the same for Hybrid and Reranked (26); reranking primarily converts four Hybrid score-0 failures into partial answers, while also changing some individual outcomes in both directions.

### Deltas

| Comparison | Answer Correctness | Faithfulness | Citation Correctness |
| --- | ---: | ---: | ---: |
| Hybrid - Dense | +0.225 | -0.150 | -0.025 |
| Reranked - Hybrid | +0.100 | +0.100 | +0.000 |
| Reranked - Dense | +0.325 | -0.050 | -0.025 |

Higher answer correctness did not produce monotonic faithfulness or citation gains. Hybrid answers were longer and attempted more synthesis, which sometimes answered questions Dense abstained on but also introduced unsupported claims.

## Results by Question Type

| Type | Strategy | Answer Correctness | Faithfulness | Citation Correctness |
| --- | --- | ---: | ---: | ---: |
| Fact (18) | Dense | 1.444 | 2.000 | 2.000 |
|  | Hybrid | 1.500 | 1.833 | 1.833 |
|  | Reranked | 1.778 | 2.000 | 1.889 |
| Multi-chunk (12) | Dense | 1.250 | 2.000 | 1.667 |
|  | Hybrid | 1.583 | 1.917 | 1.917 |
|  | Reranked | 1.583 | 1.833 | 1.667 |
| Cross-document (10) | Dense | 0.900 | 1.800 | 1.700 |
|  | Hybrid | 1.300 | 1.600 | 1.600 |
|  | Reranked | 1.200 | 1.800 | 1.800 |

Reranking has its clearest generation benefit on fact questions. It does not improve mean multi-chunk correctness over Hybrid and lowers multi-chunk faithfulness/citation means in these manual judgments. Cross-document correctness is highest for Hybrid, while Reranked recovers faithfulness and citation support but abstains or synthesizes incompletely on several questions.

## Frozen Retrieval and Generation Together

| Strategy | Recall@5 | MRR | nDCG@5 | Answer Correctness | Faithfulness | Citation Correctness |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Dense | 0.510833 | 0.590030 | 0.451834 | 1.250 | 1.950 | 1.825 |
| Hybrid | 0.564167 | 0.596667 | 0.476628 | 1.475 | 1.800 | 1.800 |
| Reranked | 0.682500 | 0.815417 | 0.651735 | 1.575 | 1.900 | 1.800 |

Across questions within each strategy, Pearson correlation between nDCG@5 and answer correctness was 0.617 Dense, 0.625 Hybrid, and 0.481 Reranked. These positive associations show that better-ranked evidence often accompanies better answers, but ranking quality alone does not determine generation quality.

## Dense vs Hybrid vs Reranked

Per-question comparison uses lexicographic priority:

1. Answer Correctness
2. Faithfulness
3. Citation Correctness

| Comparison | Improved | Unchanged | Regressed |
| --- | ---: | ---: | ---: |
| Hybrid vs Dense | 11 | 26 | 3 |
| Reranked vs Hybrid | 10 | 21 | 9 |

For Hybrid versus Dense, mean nDCG@5 increased by 0.024793 and answer correctness by 0.225; their per-query deltas had Pearson correlation 0.574. Of 12 questions with improved nDCG, generation improved on 8 and was unchanged on 4.

For Reranked versus Hybrid, mean nDCG@5 increased by 0.175107 but answer correctness only by 0.100; delta correlation was 0.356. Among 20 questions with improved nDCG, generation improved on 7, was unchanged on 10, and regressed on 3. Six retrieval nDCG regressions corresponded to 4 generation regressions and 2 unchanged results. Better early ranking therefore propagated inconsistently.

## Retrieval-to-Generation Effects

Clear propagation successes include:

- q003: Reranking moves the exact FastAPI OpenAPI passage into context; Dense and Hybrid abstain, Reranked scores 2.
- q009: Dense lacks air-gapped deployment evidence and abstains; Hybrid and Reranked retrieve it and score 2.
- q024: Dense abstains, Hybrid has a fragmented rerank example (score 1), and Reranked supplies the complete endpoint/payload (score 2).
- q030: Dense and Hybrid answer the wrong scaling question; Reranked surfaces optimized semantic search and ANN evidence and scores 2.
- q034: Dense abstains; Hybrid and Reranked provide the cross-document Sentence Transformers-to-Qdrant path and score 2.

Cases where retrieval improved but generation did not include:

- q027: Reranked nDCG regresses and its answer incorrectly locates the `document_id` payload index.
- q033: Reranked has more TEI evidence but loses the complementary local-embedding comparison and abstains.
- q037: Reranked raises nDCG by 0.556298 and surfaces one labeled chunk, but missing complementary evidence leads to abstention for all strategies.
- q039: Reranked substantially improves retrieval metrics, yet the model makes weakly supported comparative recommendations and remains score 1.

Generation also succeeded despite imperfect retrieval on q038: Dense and Hybrid produce correct fusion-versus-reranking distinctions, though their faithfulness and citations are only partial because the exact two-stage evidence is weak.

## Candidate-Generation Failure Analysis

The prior fixed-candidate analysis identified 12 questions missing at least one labeled chunk from Hybrid top-20: q007, q023, q029, q030, q033, q034, q035, q036, q037, q038, q039, and q040.

- **q036 is the complete candidate ceiling.** All four relevant chunks are absent from Hybrid top-20, all retrieval strategies have Recall@5/nDCG@5 of zero at the Reranked stage, and every answer scores 0. Dense answers filtering, Hybrid answers prefetch/filtering/relevance feedback, and Reranked invents a generic `score` parameter instead of explaining Formula Query composition.
- **q023 is a partial ceiling plus top-five ranking failure.** A relevant TEI chunk remains at candidate/final rank 6. Dense abstains, Hybrid answers the wrong local SentenceTransformer workflow, and Reranked can explain container launch but not the embedding request.
- **q037 retains only one of three relevant chunks.** Reranking promotes it to rank 1, but the fixed-split/reproducible-sampling synthesis remains impossible from top five and Qwen abstains.
- **q033 and q040 lack complementary cross-document evidence.** Answers either abstain or characterize only one side of the comparison.

These failures are attributable primarily to missing evidence before generation, not to prompt or model tuning.

## Generation Failures Despite Sufficient Context

- q005 Dense/Reranked cite the correct batching passage but omit padding and throughput degradation.
- q014 all strategies retrieve the pagination passages but omit the underlying arbitrary-Nth-neighbor/large-offset cost.
- q027 Reranked receives the lookup design but states that the payload index belongs on the documents collection.
- q033 Hybrid receives material from both systems yet adds unsupported small-scale/scalability recommendations and remains incomplete.
- q038 Dense/Hybrid answer correctly but cite weak evidence for the retrieve-and-rerank half.
- q039 every strategy receives both Pipeline and TEI material, but each makes comparative recommendations beyond the supplied text.

These are incomplete synthesis, unsupported-claim, or citation-mapping failures after useful context was available.

## Citation Analysis

No generated answer contained an invalid `[C#]` label. Citation correctness still differed semantically:

- Dense: 35 score-2, 3 score-1, 2 score-0
- Hybrid: 33 score-2, 6 score-1, 1 score-0
- Reranked: 32 score-2, 8 score-1, 0 score-0

Manual citation coverage counts were:

| Strategy | Complete | Partial | Not applicable (abstention) |
| --- | ---: | ---: | ---: |
| Dense | 29 | 2 | 9 |
| Hybrid | 36 | 1 | 3 |
| Reranked | 35 | 3 | 2 |

Observed failure patterns include irrelevant-but-valid labels (q008 Reranked), citations attached to the wrong filter concept (q010 Hybrid), unrelated nested-filter support (q026 Dense), important uncited conclusions (q025 and q039), and valid labels that only weakly support a cross-document recommendation (q033, q038, q039, q040).

## Abstention Results

All five separate unsupported questions received the exact insufficient-context response and no citations:

```text
correct abstentions / unsupported questions = 5 / 5 = 1.000
```

The unsupported set covers production SLA, cloud region, monthly infrastructure cost, executive identity, and customer-support phone number. It is not mixed into the 40-question correctness benchmark.

## Error Taxonomy

Applied evidence-backed categories include:

- **candidate generation failure:** q023, q033, q034, q036, q037, q040 and related partial ceilings
- **ranking failure:** relevant chunks outside top five causing q003, q005, q009, q010, q024, and q030 failures in weaker strategies
- **context fragmentation/noise:** truncated endpoint or mixed-topic evidence in q023, q024, q036, q038
- **incomplete synthesis:** q005, q007, q011, q014, q019, q023, q026, q028, q040
- **missing/weak citation support:** q002, q008, q019, q020, q023, q025–q027, q033, q036, q038–q040
- **unsupported generation claim:** q007, q010, q023, q027, q033, q036, q039
- **cross-document synthesis failure:** q023, q033, q036, q039, q040
- **incorrect abstention:** grounded questions where available context was absent or not synthesized
- **correct abstention:** all five separate unsupported questions

## Latency and Generation Length

Steady-state end-to-end latency includes retrieval, prompt construction, local generation, citation parsing, and serialization. Measurements are from the local MacBook Pro M5 / 24 GB and are not production benchmarks.

| Strategy | Mean (ms) | Median (ms) | p95 (ms) | Mean answer chars | Latency/length correlation |
| --- | ---: | ---: | ---: | ---: | ---: |
| Dense | 11,217.8 | 10,756.3 | 15,809.2 | 406.6 | 0.871 |
| Hybrid | 12,070.0 | 11,980.2 | 17,943.3 | 550.9 | 0.864 |
| Reranked | 12,482.3 | 11,681.7 | 18,925.7 | 520.2 | 0.904 |

Answer length is strongly correlated with latency in every strategy, so the observed timing differences cannot be assigned solely to retrieval overhead. No concurrency, repeated-trial interval, or production throughput was measured.

## Cases Requiring Human Review

The following 21 annotations are explicitly flagged rather than treated as definitive: q023 Hybrid/Reranked; q026 Dense/Hybrid; q027 Reranked; q033 Hybrid/Reranked; q036 all strategies; q037 all strategies; q038 Dense/Hybrid; q039 all strategies; and q040 all strategies.

The flags concentrate on cross-document synthesis, candidate ceilings, and semantic citation support. A second human reviewer should adjudicate these before treating small metric differences as stable.

## Limitations

- One manual reviewer assigned the initial semantic scores; no inter-annotator agreement is available.
- Forty questions over ten documents is useful for portfolio evidence but too small for broad generalization.
- Reference answers and relevance labels are frozen but still reflect one manually designed dataset.
- One local Qwen generation was recorded per strategy/question; no repeated-generation variance was measured.
- The experiment compares retrieval strategies, not alternate prompts, context depths, or models.
- Citation coverage is categorical because exact material-claim segmentation was judged too subjective to automate robustly.
- Correlations and deltas are descriptive and do not prove causality.

## Conclusion

The evidence supports a limited claim: on this frozen dataset, stronger retrieval is associated with higher mean answer correctness. Hybrid improves over Dense by 0.225 and Reranked improves over Hybrid by 0.100 on the 0–2 scale, while retrieval nDCG@5 rises at each stage.

The evidence does **not** support the stronger claim that every retrieval improvement produces a better final answer. Reranked versus Hybrid has nearly balanced per-query changes (10 improved, 9 regressed), multi-chunk correctness is unchanged, cross-document correctness regresses, and faithfulness/citation quality is not monotonic. Candidate evidence remains a hard ceiling, while synthesis and citation failures can occur even with useful context.

The portfolio conclusion should therefore be: better retrieval improved aggregate answer correctness, especially for fact questions, but answer generation remains an independent failure surface that requires separate evaluation and human review.
