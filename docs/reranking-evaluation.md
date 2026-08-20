# Cross-Encoder Reranking Evaluation

## Purpose

Measure whether cross-encoder reranking improves the early relevance of the frozen Hybrid candidate ranking enough to justify its additional local compute and latency.

## Controlled Variables

The corpus, 212 chunk IDs, 40 questions, 101 graded relevance labels, parser, chunker, chunk size, overlap, dense model, cosine index, BM25 tokenizer, top-20 source depths, RRF `k=60`, and metric implementations were unchanged. Before the reranked run, Dense and Hybrid were rerun and retained their complete frozen JSON hashes:

```text
dataset.json  efc13a01af34b6c7f292b44c6d6e04a8cf7f1e06b7ba5acdd7a56a8c38d0c600
dense.json    509f1272c912be0c5c6f9723d2487ee304f97206880ddd528198d35feacf7e4f
hybrid.json   359df3832415b37fa25124b8cc5953cfcab4234777a67a3911e8ac5e5940077d
```

No model, depth, query, or retrieval parameter was tuned after observing results.

## Reranking Design

```text
Dense top-20 + BM25 top-20
             ↓
          RRF k=60
             ↓
      Hybrid top-20
             ↓
cross-encoder/ms-marco-MiniLM-L-6-v2
             ↓
      Reranked top-10
```

The CrossEncoder scores all 20 `(query, chunk text)` pairs in one prediction call. Reranker scores, original Hybrid ranks, and original RRF scores remain separate in the result file. Exact reranker-score ties use Hybrid rank and then chunk ID. The model and candidate depth were fixed before evaluation.

## Aggregate Results

| Metric | Dense | Hybrid | Reranked | Reranked - Hybrid |
| --- | ---: | ---: | ---: | ---: |
| Recall@1 | 0.247917 | 0.227083 | 0.371667 | +0.144583 |
| Recall@5 | 0.510833 | 0.564167 | 0.682500 | +0.118333 |
| Recall@10 | 0.670000 | 0.681667 | 0.813750 | +0.132083 |
| MRR | 0.590030 | 0.596667 | 0.815417 | +0.218750 |
| nDCG@5 | 0.451834 | 0.476628 | 0.651735 | +0.175107 |

Reranking improved all aggregate metrics. Recall@10 can change even though candidate generation is fixed because the CrossEncoder selects a new top 10 from the unchanged Hybrid top-20; relevant candidates formerly at ranks 11–20 may enter the measured output.

## Results by Question Type

| Type | Metric | Hybrid | Reranked | Delta |
| --- | --- | ---: | ---: | ---: |
| Fact | Recall@5 | 0.666667 | 0.833333 | +0.166667 |
| Fact | MRR | 0.622685 | 0.788889 | +0.166204 |
| Fact | nDCG@5 | 0.549359 | 0.769587 | +0.220228 |
| Multi-chunk | Recall@5 | 0.565278 | 0.616667 | +0.051389 |
| Multi-chunk | MRR | 0.627778 | 0.826389 | +0.198611 |
| Multi-chunk | nDCG@5 | 0.474908 | 0.577186 | +0.102278 |
| Cross-document | Recall@5 | 0.378333 | 0.490000 | +0.111667 |
| Cross-document | MRR | 0.512500 | 0.850000 | +0.337500 |
| Cross-document | nDCG@5 | 0.347775 | 0.529060 | +0.181285 |

All three categories improved in aggregate. Cross-document questions had the largest MRR gain, fact questions had the largest nDCG@5 gain, and multi-chunk questions had the smallest—but still positive—Recall@5 and nDCG@5 gains.

## Per-Query Changes

The same deterministic rule as the Hybrid experiment classifies each query by comparing `(nDCG@5, Recall@5, reciprocal rank)` lexicographically. Reranking improved 22 queries, left 12 unchanged, and regressed 6.

| ID | Type | Change | Delta Recall@5 | Delta RR | Delta nDCG@5 |
| --- | --- | --- | ---: | ---: | ---: |
| q001 | fact | Improved | +0.000000 | +0.500000 | +0.369070 |
| q002 | fact | Regressed | +0.000000 | -0.500000 | -0.101646 |
| q003 | fact | Improved | +0.000000 | -0.050000 | +0.201018 |
| q004 | fact | Regressed | +0.000000 | +0.000000 | -0.055152 |
| q005 | fact | Improved | +1.000000 | +0.375000 | +0.630930 |
| q006 | fact | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q007 | fact | Improved | +0.500000 | +1.000000 | +0.826235 |
| q008 | fact | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q009 | fact | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q010 | fact | Improved | +0.000000 | +0.166667 | +0.000000 |
| q011 | fact | Improved | +0.500000 | +0.000000 | +0.724588 |
| q012 | fact | Improved | +0.000000 | +0.500000 | +0.369070 |
| q013 | fact | Improved | +1.000000 | +0.500000 | +0.630930 |
| q014 | fact | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q015 | fact | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q016 | fact | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q017 | fact | Improved | +0.000000 | +0.500000 | +0.369070 |
| q018 | fact | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q019 | multi_chunk | Regressed | +0.000000 | -0.250000 | -0.132382 |
| q020 | multi_chunk | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q021 | multi_chunk | Regressed | +0.000000 | +0.000000 | -0.024804 |
| q022 | multi_chunk | Improved | +0.000000 | +0.500000 | +0.131381 |
| q023 | multi_chunk | Improved | +0.000000 | +0.166667 | +0.000000 |
| q024 | multi_chunk | Improved | +0.500000 | +0.500000 | +0.532868 |
| q025 | multi_chunk | Improved | -0.333333 | +0.666667 | +0.085630 |
| q026 | multi_chunk | Improved | +0.250000 | +0.000000 | +0.325028 |
| q027 | multi_chunk | Regressed | +0.000000 | +0.000000 | -0.096807 |
| q028 | multi_chunk | Improved | +0.000000 | +0.000000 | +0.040877 |
| q029 | multi_chunk | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q030 | multi_chunk | Improved | +0.200000 | +0.800000 | +0.365540 |
| q031 | cross-document | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q032 | cross-document | Improved | +0.000000 | +0.500000 | +0.190129 |
| q033 | cross-document | Regressed | +0.000000 | +0.000000 | -0.293106 |
| q034 | cross-document | Improved | +0.333333 | +0.750000 | +0.396575 |
| q035 | cross-document | Improved | +0.000000 | +0.500000 | +0.212011 |
| q036 | cross-document | Unchanged | +0.000000 | +0.000000 | +0.000000 |
| q037 | cross-document | Improved | +0.333333 | +0.875000 | +0.556298 |
| q038 | cross-document | Improved | +0.200000 | +0.000000 | +0.265480 |
| q039 | cross-document | Improved | +0.250000 | +0.750000 | +0.485459 |
| q040 | cross-document | Unchanged | +0.000000 | +0.000000 | +0.000000 |

The label does not imply that every metric moved in the same direction. For example, q025 improved graded early ordering while retrieving one fewer relevant chunk in its top five.

## Previously Observed Hybrid Regressions

| Query | Outcome after reranking | Evidence |
| --- | --- | --- |
| q005, unknown-length batching | Repaired | Relevant chunk moved from rank 8 to rank 2; Recall@5 rose from 0 to 1. |
| q020, sync/async FastAPI dependencies | Not repaired by primary rule | Recall@5, RR, and nDCG@5 were unchanged; the second relevant chunk did enter the top 10, raising Recall@10 from 0.5 to 1. |
| q012, cosine optimization | Repaired | Relevant chunk moved from rank 2 to rank 1; RR and nDCG@5 reached 1. |
| q038, fusion versus reranking | Repaired | Recall@5 rose from 0.2 to 0.4 and nDCG@5 gained 0.265480. |
| q039, Pipeline versus TEI | Repaired | First relevant rank moved from 4 to 1; Recall@5 rose from 0.5 to 0.75 and nDCG@5 gained 0.485459. |

## Candidate-Ceiling Analysis

A **candidate-generation failure** means relevant evidence is absent from Hybrid top-20 and cannot be recovered by the CrossEncoder. A **reranking failure** means relevant evidence is available in Hybrid top-20 but remains outside the desired final rank range.

Twelve questions were missing at least one labeled chunk from Hybrid top-20: q007, q023, q029, q030, q033, q034, q035, q036, q037, q038, q039, and q040. Most retained some relevant candidates, so reranking could still improve partial coverage. q036 was the only complete candidate failure: all four relevant chunks were absent, and reranked Recall@10 remained zero.

| Previously unresolved query | Hybrid top-20 evidence | Reranked result | Diagnosis |
| --- | --- | --- | --- |
| q010, `Match Any` | Relevant at candidate rank 12 | Final rank 6 | Improved at top 10, but unresolved top-five ranking failure. |
| q013, `score_threshold` | Relevant at candidate rank 13 | Final rank 2 | Ranking failure repaired. |
| q023, TEI startup/querying | One of two relevant chunks at candidate rank 12 | Final rank 6 | Partial candidate failure plus unresolved top-five ranking failure. |
| q036, business-signal rescoring | No relevant candidate | No relevant final result | Complete candidate-generation failure. |
| q037, reproducible evaluation guidance | One of three relevant chunks at candidate rank 8 | Final rank 1 | Available evidence reranked successfully; two labels remain outside the candidate set. |

Thus, q010 and q023 are not top-10 failures anymore, but their available relevant chunks remain just below the top five. q036 cannot be repaired by reranking without changing candidate generation.

## Reranking Regressions

Six queries regressed under the stated rule:

- q002 moved its first relevant FastAPI `Depends` chunk from rank 1 to 2.
- q004 retained both relevant Pipeline device chunks in the top five, but the second moved from rank 2 to 4, reducing graded nDCG.
- q019 moved two relevant FastAPI dependency-flow chunks from ranks 2/3 to 4/5.
- q021 kept three relevant batching chunks in the top five but reordered them less favorably; the fourth fell outside the top 10.
- q027 increased Recall@10 from 0.75 to 1 but produced a less favorable graded top-five ordering.
- q033 increased Recall@10 from 0.5 to 0.75, but promoted lower-grade TEI evidence over the higher-grade local-versus-serving comparison evidence, reducing nDCG@5 by 0.293106.

These are ranking regressions, not candidate-generation failures. Their causes are inferred from ranks and relevance grades; this run does not establish a causal mechanism.

## Latency

One warmup query loaded and warmed the CrossEncoder and retrieval path and was excluded. The same 40 evaluation queries were then timed with `time.perf_counter()`. The p95 is linearly interpolated. Measurements were taken on the local arm64 macOS 26.5.2 machine with the CrossEncoder running on CPU.

| Stage | Mean (ms) | Median (ms) | p95 (ms) |
| --- | ---: | ---: | ---: |
| Hybrid retrieval | 24.840 | 5.525 | 99.979 |
| Cross-encoder reranker | 141.750 | 124.907 | 227.243 |
| End-to-end | 166.589 | 136.251 | 370.236 |

The reranker added approximately 141.75 ms mean latency in this local run and dominated steady-state end-to-end time. These are single-machine development measurements, not production benchmarks; no concurrency or repeated-trial confidence interval was measured.

The model was not cached initially and was downloaded during the formal run. Model download and initialization occurred before the excluded warmup completed and are not included above. The subsequent CLI smoke test used the cached model.

## Interpretation

The experiment answers the early-relevance question positively on this frozen dataset: relative to Hybrid, Recall@1 gained 0.144583, MRR gained 0.218750, and nDCG@5 gained 0.175107. Improvements occurred across every question type, 22 queries improved, and four of five highlighted Hybrid regressions were repaired.

This quality gain came with approximately 142 ms mean additional local CPU latency. The measured trade-off supports retaining reranking as the accuracy-oriented retrieval configuration and proceeding with it for later answer-generation experiments. It does not establish that reranking should be mandatory for latency-sensitive production paths.

## Limitations

- The evaluation contains 40 single-annotator questions over 10 documents.
- Latency comes from one warmed local run on one machine and includes normal system variability.
- CrossEncoder scores are model-specific and are not calibrated probabilities.
- Hybrid top-20 imposes a hard evidence ceiling; 12 questions lack at least one labeled candidate.
- Only one predefined reranker and candidate depth were evaluated, with no tuning or alternate model comparison.
- No statistical significance, production throughput, concurrency, answer generation, or citation quality was evaluated.
