# Hybrid Retrieval Evaluation

## Purpose

Measure whether BM25 lexical retrieval adds value to the frozen dense baseline when the two rankings are combined with Reciprocal Rank Fusion (RRF). This is a controlled comparison on the same 10 documents, 212 chunks, 40 questions, and manually graded relevance labels.

## Controlled Variables

The corpus, parser, chunker, 1,000-character chunk size, 200-character overlap, `sentence-transformers/all-MiniLM-L6-v2` model, Qdrant cosine index, evaluation questions, relevance labels, retrieval metrics, and final evaluation depth of 10 were unchanged. The complete dense result file had the same SHA-256 hash before and after its required rerun:

```text
509f1272c912be0c5c6f9723d2487ee304f97206880ddd528198d35feacf7e4f
```

No parameter search or post-result tuning was performed.

## Hybrid Design

- BM25 implementation: in-process `rank-bm25` over the same 212 `Chunk` objects used to construct the dense corpus.
- Tokenizer: Unicode case-folding followed by `[a-z0-9_]+`. This removes simple punctuation while retaining underscores in identifiers such as `score_threshold`; it performs no stemming, lemmatization, or expansion.
- Candidate rankings: Dense top-20 and BM25 top-20.
- Fusion: standard `sum(1 / (60 + rank))` by deterministic chunk ID.
- Deduplication: a chunk contributes at most once per source ranking.
- Tie-breaking: descending RRF score, then ascending chunk ID.
- Final evaluation ranking: top-10 fused chunks.

The runner verifies that the BM25 index contains exactly the frozen corpus chunk-ID set before evaluation.

## Aggregate Results

| Metric | Dense | Hybrid | Delta |
| --- | ---: | ---: | ---: |
| Recall@1 | 0.247917 | 0.227083 | -0.020833 |
| Recall@5 | 0.510833 | 0.564167 | +0.053333 |
| Recall@10 | 0.670000 | 0.681667 | +0.011667 |
| MRR | 0.590030 | 0.596667 | +0.006637 |
| nDCG@5 | 0.451834 | 0.476628 | +0.024793 |

Hybrid improved four aggregate metrics, including the three primary metrics, but reduced Recall@1. The changes are not uniform across question types.

## Results by Question Type

| Type | Metric | Dense | Hybrid | Delta |
| --- | --- | ---: | ---: | ---: |
| Fact | Recall@5 | 0.666667 | 0.666667 | +0.000000 |
| Fact | MRR | 0.660714 | 0.622685 | -0.038029 |
| Fact | nDCG@5 | 0.569863 | 0.549359 | -0.020504 |
| Multi-chunk | Recall@5 | 0.412500 | 0.565278 | +0.152778 |
| Multi-chunk | MRR | 0.475694 | 0.627778 | +0.152083 |
| Multi-chunk | nDCG@5 | 0.360305 | 0.474908 | +0.114604 |
| Cross-document | Recall@5 | 0.348333 | 0.378333 | +0.030000 |
| Cross-document | MRR | 0.600000 | 0.512500 | -0.087500 |
| Cross-document | nDCG@5 | 0.349219 | 0.347775 | -0.001443 |

The aggregate gain is driven primarily by multi-chunk questions. Fact Recall@5 was unchanged while its ranking-sensitive metrics fell. Cross-document coverage rose slightly, but early-rank quality did not improve.

## Per-Query Changes

Classification compares per-query `(nDCG@5, Recall@5, reciprocal rank)` lexicographically: nDCG@5 is primary, then Recall@5, then first-relevant rank. This gives one deterministic label while retaining each metric delta below. By this rule, 13 queries improved, 17 were unchanged, and 10 regressed.

| ID | Type | Change | Delta Recall@5 | Delta RR | Delta nDCG@5 |
| --- | --- | --- | ---: | ---: | ---: |
| q001 | fact | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q002 | fact | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q003 | fact | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q004 | fact | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q005 | fact | Regressed | -1.000000 | -0.208333 | -0.500000 |
| q006 | fact | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q007 | fact | Regressed | +0.000000 | -0.142857 | +0.000000 |
| q008 | fact | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q009 | fact | Improved | +1.000000 | +0.833333 | +1.000000 |
| q010 | fact | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q011 | fact | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q012 | fact | Regressed | +0.000000 | -0.500000 | -0.369070 |
| q013 | fact | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q014 | fact | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q015 | fact | Regressed | +0.000000 | -0.166667 | -0.130930 |
| q016 | fact | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q017 | fact | Regressed | +0.000000 | -0.500000 | -0.369070 |
| q018 | fact | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q019 | multi_chunk | Improved | +0.000000 | +0.000000 | +0.012855 |
| q020 | multi_chunk | Regressed | -0.500000 | +0.000000 | -0.386853 |
| q021 | multi_chunk | Regressed | +0.000000 | +0.000000 | -0.137012 |
| q022 | multi_chunk | Improved | +0.333333 | +0.250000 | +0.252339 |
| q023 | multi_chunk | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q024 | multi_chunk | Improved | +0.500000 | +0.375000 | +0.386853 |
| q025 | multi_chunk | Improved | +0.666667 | +0.000000 | +0.383649 |
| q026 | multi_chunk | Improved | +0.000000 | +0.750000 | +0.097764 |
| q027 | multi_chunk | Improved | +0.500000 | +0.000000 | +0.359434 |
| q028 | multi_chunk | Improved | +0.333333 | +0.000000 | +0.234639 |
| q029 | multi_chunk | Improved | +0.000000 | +0.500000 | +0.192744 |
| q030 | multi_chunk | Regressed | +0.000000 | -0.050000 | -0.021170 |
| q031 | cross_document | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q032 | cross_document | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q033 | cross_document | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q034 | cross_document | Improved | +0.000000 | -0.750000 | +0.054152 |
| q035 | cross_document | Improved | +0.250000 | +0.000000 | +0.170083 |
| q036 | cross_document | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q037 | cross_document | Improved | +0.000000 | +0.125000 | +0.000000 |
| q038 | cross_document | Regressed | -0.200000 | +0.000000 | -0.208046 |
| q039 | cross_document | Regressed | +0.250000 | -0.750000 | -0.094001 |
| q040 | cross_document | Improved | +0.000000 | +0.500000 | +0.063376 |

The classification is a summary, not a claim that every metric moved in the same direction. For example, q034 improved nDCG@5 while its first relevant result moved lower, and q039 retrieved more relevant chunks in the top five while its graded ordering worsened.

## Gains

- **q009, air-gapped TEI deployment:** Recall@5 rose from 0 to 1, reciprocal rank from 0.166667 to 1, and nDCG@5 from 0 to 1. The relevant chunk was BM25 rank 1, plausibly benefiting from the distinctive phrase “air-gapped.”
- **q024, TEI reranker deployment:** Recall@5 gained 0.5 and nDCG@5 gained 0.386853. BM25 promoted a TEI passage containing “Using Re-rankers models,” matching product-specific terminology.
- **q025, `must`/`should`/`must_not`:** Recall@5 rose from 0.333333 to 1. Exact clause names plausibly contributed to the lexical gain.
- **q027, grouped chunk hits and document metadata:** Recall@5 gained 0.5 and nDCG@5 gained 0.359434; more of the related Qdrant passages entered the top five.
- **q022 and q028:** hybrid recovered additional multi-part evidence about Pipeline hardware/memory settings and Qdrant coarse-to-fine prefetches.

These examples support a limited claim that lexical retrieval can add useful candidates for exact or product-specific language. They do not establish that all terminology-heavy queries improve.

## Regressions

- **q005, batching with unknown sequence lengths:** the relevant dense chunk was rank 3 but was absent from BM25 top-20 and moved to hybrid rank 8. Recall@5 fell from 1 to 0. Overlap among other batching-related chunks appears to have promoted broader passages.
- **q020, synchronous/asynchronous dependencies:** two relevant dense chunks became only one relevant top-five hybrid chunk, reducing Recall@5 by 0.5 and nDCG@5 by 0.386853.
- **q012, cosine optimization:** the directly relevant chunk moved from rank 1 to rank 2; nDCG@5 fell by 0.369070.
- **q038, fusion versus retrieve-and-rerank:** Recall@5 fell by 0.2 and nDCG@5 by 0.208046. Repeated fusion terminology promoted related hybrid-query passages but reduced coverage of all labeled comparison evidence.
- **q039, Pipeline versus TEI:** Recall@5 increased by 0.25, but the highest-grade evidence moved down, lowering reciprocal rank by 0.75 and nDCG@5 by 0.094001. This is a mixed result classified as a regression because graded ordering is primary.

These causes are hypotheses based on the observed candidate text and ranks; the experiment does not isolate each causal factor.

## Failure Cases

| Prior dense failure | Dense | Hybrid | Candidate evidence |
| --- | --- | --- | --- |
| q010, `Match Any` | No relevant top-10 | No relevant top-10 | Relevant chunk was BM25 rank 5 but fused rank 12. |
| q013, `score_threshold` | No relevant top-10 | No relevant top-10 | Relevant chunk was BM25 rank 5 but fused rank 13. |
| q023, TEI startup/querying | No relevant top-10 | No relevant top-10 | One relevant chunk was BM25 rank 5 but fused rank 12. |
| q036, business-signal rescoring | No relevant top-10 | No relevant top-10 | No relevant chunk appeared in either top-20 candidate list. |
| q037, reproducible evaluation guidance | No relevant top-10 | Relevant at rank 8 | Relevant chunk was BM25 rank 1; Recall@10 became 0.333333 and reciprocal rank 0.125, while Recall@5 and nDCG@5 remained zero. |

RRF rewards agreement between rankings. A lexical-only relevant chunk at rank 5 can remain below chunks appearing moderately high in both source rankings. This explains why BM25 candidate recovery did not automatically translate into final top-10 recovery for q010, q013, and q023.

## Interpretation

Hybrid increased aggregate Recall@5 by 0.053333 and nDCG@5 by 0.024793, with its clearest gains on multi-chunk questions. However, Recall@1 fell by 0.020833, fact ranking quality declined, and 10 individual queries regressed under the stated classification. The measured evidence therefore supports Hybrid as a broader candidate-retrieval comparison point, not as an unqualified replacement for Dense.

The combination of added coverage and unstable early ordering provides a concrete reason to test reranking next under the same frozen evaluation. It does not guarantee that reranking will improve results.

## Limitations

- The corpus has only 10 documents and 40 single-annotator questions.
- BM25 uses deliberately minimal tokenization and no linguistic normalization.
- Candidate depths and RRF `k` are fixed design choices, not optimized values.
- Final metrics inspect only the top 10; some lexical-only relevant candidates fused just below that boundary.
- RRF source-specific ranks are not stored in the normal result JSON; candidate ranks in this analysis were inspected from the same fixed retrievers after evaluation.
- Latency was not measured. Adding benchmark fields to the frozen dense artifact was avoided, and this experiment focuses on retrieval effectiveness rather than local-machine timing.
- No statistical significance or production-performance claim is made.
