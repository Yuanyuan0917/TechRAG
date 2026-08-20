# Dense Evaluation Dataset Review

This review renders the manually assigned ground truth from `evaluation/dataset.json`. Relevance labels are human judgments based on the frozen 1000-character chunks: **2** directly answers the question; **1** is materially useful supporting context.

## q001

**Type:** fact

**Question:** What does dependency injection mean in FastAPI?

**Reference answer:** A path operation declares what it needs, and FastAPI provides or injects those dependencies, enabling shared logic, database connections, and security requirements with less repetition.

**Relevant documents:**

- `doc_97add4ed2c662b4c580315e5bd07e009a5f6858dff61e42e572ebd5832f07d6f` (`fastapi_dependencies.md`)

**Relevant chunks:**

- `chunk_650291a57f062c2b9952069182c54be8e1b246992c87b738659aa622aa60bb72`
  - Source: `fastapi_dependencies.md`, chunk 0
  - Short excerpt: # Dependencies { #dependencies } **FastAPI** has a very powerful but intuitive **<dfn title="also known as components, resources, providers, services, injectables">Dependency Injection</dfn>** system. It is designed to b…
  - Relevance: 2

## q002

**Type:** fact

**Question:** How does FastAPI know what to do with a callable passed to Depends?

**Reference answer:** The developer passes the callable to Depends; FastAPI analyzes its parameters like a path operation function and calls it with the required values for each request, without separate registration.

**Relevant documents:**

- `doc_97add4ed2c662b4c580315e5bd07e009a5f6858dff61e42e572ebd5832f07d6f` (`fastapi_dependencies.md`)

**Relevant chunks:**

- `chunk_8410fc104cbba877f60c62dfba703377315027111519f18f84210962f5b41419`
  - Source: `fastapi_dependencies.md`, chunk 3
  - Short excerpt: to at least 0.95.1 before using `Annotated`. /// ### Import `Depends` { #import-depends } {* ../../docs_src/dependencies/tutorial001_an_py310.py hl[3] *} ### Declare the dependency, in the "dependant" { #declare-the-depe…
  - Relevance: 2
- `chunk_e20b19f85be3bb2ad4a48e82dbde5b128d82ad6a46633de0bdeeb6626ef8b134`
  - Source: `fastapi_dependencies.md`, chunk 4
  - Short excerpt: )`. And that function takes parameters in the same way that *path operation functions* do. /// tip You'll see what other "things", apart from functions, can be used as dependencies in the next chapter. /// Whenever a new…
  - Relevance: 1

## q003

**Type:** fact

**Question:** How are dependency requirements represented in FastAPI's generated API documentation?

**Reference answer:** Parameters, validations, and requirements declared by dependencies and sub-dependencies are added to the OpenAPI schema and shown in the interactive documentation.

**Relevant documents:**

- `doc_97add4ed2c662b4c580315e5bd07e009a5f6858dff61e42e572ebd5832f07d6f` (`fastapi_dependencies.md`)

**Relevant chunks:**

- `chunk_bb8ad8fb21de94977a41c262b82ebae2ae96d4542e03cd1fbd746e0e652b1b85`
  - Source: `fastapi_dependencies.md`, chunk 7
  - Short excerpt: ions. You can use `async def` or normal `def`. And you can declare dependencies with `async def` inside of normal `def` *path operation functions*, or `def` dependencies inside of `async def` *path operation functions*, …
  - Relevance: 2
- `chunk_1aedfeace05dc6386f5efa0b4c517ad926ce622e25a40c3a79120b71e65723c1`
  - Source: `fastapi_dependencies.md`, chunk 8
  - Short excerpt: ge } If you look at it, *path operation functions* are declared to be used whenever a *path* and *operation* matches, and then **FastAPI** takes care of calling the function with the correct parameters, extracting the da…
  - Relevance: 1

## q004

**Type:** fact

**Question:** How can a Transformers Pipeline be assigned to CPU, GPU, or Apple Silicon?

**Reference answer:** Configure the Pipeline device, using the supported device identifier or an Accelerate device map so model weights are placed on suitable hardware.

**Relevant documents:**

- `doc_416c540cf133e4b620ffd26993838ac4fd5cbcf8219c196756bdf5f2765ed937` (`huggingface_pipeline_tutorial.md`)

**Relevant chunks:**

- `chunk_956b19cd3a6b8048a2c00f1088a52574ecffeafe6100e43c2fb73481eba55f87`
  - Source: `huggingface_pipeline_tutorial.md`, chunk 6
  - Short excerpt: imizing performance. This section introduces you to some of the more important parameters. ### Device [`Pipeline`] is compatible with many hardware types, including GPUs, CPUs, Apple Silicon, and more. Configure the hard…
  - Relevance: 2
- `chunk_fb426b5076f1819e1d1683752c9b7c36b1eca1967d6ac8d3076b1db374082653`
  - Source: `huggingface_pipeline_tutorial.md`, chunk 7
  - Short excerpt: cally choose how to load and store the model weights on the appropriate device. This is especially useful if you have multiple devices. Accelerate loads and stores the model weights on the fastest device first, and then …
  - Relevance: 1

## q005

**Type:** fact

**Question:** Why does the Transformers documentation caution against batching inputs with unknown sequence lengths?

**Reference answer:** Uneven sequence lengths can introduce heavy padding, reduce throughput, and cause out-of-memory failures, so batching should be measured and guarded with OOM checks.

**Relevant documents:**

- `doc_416c540cf133e4b620ffd26993838ac4fd5cbcf8219c196756bdf5f2765ed937` (`huggingface_pipeline_tutorial.md`)

**Relevant chunks:**

- `chunk_d3f2f420bb384f0afacf3b983021a087d8ab05cbdf9c81bf72ff031cdc1aced0`
  - Source: `huggingface_pipeline_tutorial.md`, chunk 11
  - Short excerpt: PU. 4. Don't batch inference if you don't know the `sequence_length` of your data. Measure performance, iteratively add to `sequence_length`, and include out-of-memory (OOM) checks to recover from failures. 5. Do batch i…
  - Relevance: 2

## q006

**Type:** fact

**Question:** How can the default pretrained model used by a Transformers Pipeline be replaced?

**Reference answer:** Pass the desired model identifier through the Pipeline model parameter instead of relying on the task's default pretrained model and preprocessor.

**Relevant documents:**

- `doc_416c540cf133e4b620ffd26993838ac4fd5cbcf8219c196756bdf5f2765ed937` (`huggingface_pipeline_tutorial.md`)

**Relevant chunks:**

- `chunk_d1180e8d6ffd5cce2f77e63f9a9f9f1332b94b7582a8c9c029a86e012847ea45`
  - Source: `huggingface_pipeline_tutorial.md`, chunk 2
  - Short excerpt: is configured to use a default pretrained model and preprocessor, but this can be overridden with the `model` parameter if you want to use a different model. For example, to use the [`TextGenerationPipeline`] with [Gemma…
  - Relevance: 2

## q007

**Type:** fact

**Question:** What is Hugging Face Text Embeddings Inference designed to serve?

**Reference answer:** Text Embeddings Inference is a production-oriented toolkit for deploying and serving open-source text embedding and sequence-classification models with features such as dynamic batching and observability.

**Relevant documents:**

- `doc_804c8377e1908e9583942234825e7b5df1e3d0528aff172b36538e5a542bf6b0` (`huggingface_text_embeddings_inference.md`)

**Relevant chunks:**

- `chunk_88acf2e84e52b7fc08a9e4d8c192e58752cf204ff470b0e62090af7b9d041c5e`
  - Source: `huggingface_text_embeddings_inference.md`, chunk 2
  - Short excerpt: - [AMD Instinct GPUs (ROCm)](#amd-instinct-gpus-rocm-experimental) - [Examples](#examples) Text Embeddings Inference (TEI) is a toolkit for deploying and serving open source text embeddings and sequence classification mo…
  - Relevance: 2
- `chunk_91886f8dfcacd49ebef6dff8176cb02b7e42ce717d47fd6ceeedc343f7d9f183`
  - Source: `huggingface_text_embeddings_inference.md`, chunk 3
  - Short excerpt: lt-api) * [Safetensors](https://github.com/huggingface/safetensors) weight loading * [ONNX](https://github.com/onnx/onnx) weight loading * Production ready (distributed tracing with Open Telemetry, Prometheus metrics) ##…
  - Relevance: 1

## q008

**Type:** fact

**Question:** What does the max_batch_tokens setting control in Text Embeddings Inference?

**Reference answer:** It limits the total potential tokens in a batch, controlling how many requests of different token lengths can fit together to maximize hardware utilization.

**Relevant documents:**

- `doc_804c8377e1908e9583942234825e7b5df1e3d0528aff172b36538e5a542bf6b0` (`huggingface_text_embeddings_inference.md`)

**Relevant chunks:**

- `chunk_870cf142bf9cc251ba5e0810dc36c41d88729b3bdcecca2196e6ea56d01d8097`
  - Source: `huggingface_text_embeddings_inference.md`, chunk 14
  - Short excerpt: CH_TOKENS> **IMPORTANT** This is one critical control to allow maximum usage of the available hardware. This represents the total amount of potential tokens within a batch. For `max_batch_tokens=1000`, you could fit `10`…
  - Relevance: 2

## q009

**Type:** fact

**Question:** How does Text Embeddings Inference support deployment in an air-gapped environment?

**Reference answer:** Download the model weights in advance, mount them into the container as a volume, and start TEI with the mounted local model path.

**Relevant documents:**

- `doc_804c8377e1908e9583942234825e7b5df1e3d0528aff172b36538e5a542bf6b0` (`huggingface_text_embeddings_inference.md`)

**Relevant chunks:**

- `chunk_2d0088f75d30dcdfcd5ec4714df26baea721dd35fdcaa7f340f18eef255232e7`
  - Source: `huggingface_text_embeddings_inference.md`, chunk 25
  - Short excerpt: r run --gpus all -e HF_TOKEN=$token -p 8080:80 -v $volume:/data --pull always ghcr.io/huggingface/text-embeddings-inference:cuda-1.9 --model-id $model ``` ### Air gapped deployment To deploy Text Embeddings Inference in …
  - Relevance: 2

## q010

**Type:** fact

**Question:** When does a Qdrant Match Any payload condition succeed?

**Reference answer:** It succeeds when the stored keyword or integer value equals any configured value; for an array, at least one stored element must match one of them.

**Relevant documents:**

- `doc_1713ab05743cc108791b3eea9872aed4153364e83ba8337235146d6e25b302a9` (`qdrant_filtering.md`)

**Relevant chunks:**

- `chunk_2f181aae2739cf2e7c91798c7d9fd915848089a40f3000874977a2e6c9952cf2`
  - Source: `qdrant_filtering.md`, chunk 7
  - Short excerpt: er](/documentation/manage-data/payload/#integer) payloads. Example: {{< code-snippet path="/documentation/headless/snippets/filter-condition/match-any/" >}} In this example, the condition will be satisfied if the stored …
  - Relevance: 2

## q011

**Type:** fact

**Question:** Why would a Qdrant nested object filter be needed for an array of objects?

**Reference answer:** It ensures all conditions are evaluated against the same array element instead of allowing different elements to satisfy different conditions.

**Relevant documents:**

- `doc_1713ab05743cc108791b3eea9872aed4153364e83ba8337235146d6e25b302a9` (`qdrant_filtering.md`)

**Relevant chunks:**

- `chunk_3af51a31bbbc0f3575860a94af5242bdcc036b967b34a316676f6be760688823`
  - Source: `qdrant_filtering.md`, chunk 12
  - Short excerpt: and likes=true on `diet[1].likes` - the "diplodocus" matches food=meat on `diet[1].food` and likes=true on `diet[0].likes` To retrieve only the points which are matching the conditions on an array element basis, that is …
  - Relevance: 2
- `chunk_67dfc506017e8700771afc3d03c08e33123053c97c1815e07c3f73b32fdb059b`
  - Source: `qdrant_filtering.md`, chunk 13
  - Short excerpt: rray element within the payload. Nested filters work in the same way as if the nested filter was applied to a single element of the array at a time. Parent document is considered to match the condition if at least one el…
  - Relevance: 1

## q012

**Type:** fact

**Question:** How does Qdrant optimize cosine similarity calculations for stored vectors?

**Reference answer:** Qdrant normalizes each vector once when it is added to the collection, then uses a dot-product-style comparison during search.

**Relevant documents:**

- `doc_3f18686b3efe2fa035065d587481604931b8a3da8ba0c41e1d56bf801231058d` (`qdrant_vector_search.md`)

**Relevant chunks:**

- `chunk_c009ce573faa73149f54c4673a75779ef3616b8e15f771968c3ebfe2423c94fb`
  - Source: `qdrant_vector_search.md`, chunk 4
  - Short excerpt: sup>*Available as of v1.7</sup></i> The most typical metric used in similarity learning models is the cosine metric. ![Embeddings](/docs/cos.png) Qdrant counts this metric in 2 steps, due to which a higher search speed i…
  - Relevance: 2

## q013

**Type:** fact

**Question:** What does score_threshold do in a Qdrant search request?

**Reference answer:** It removes results whose scores are worse than the threshold, with the direction of worse depending on the configured distance metric.

**Relevant documents:**

- `doc_3f18686b3efe2fa035065d587481604931b8a3da8ba0c41e1d56bf801231058d` (`qdrant_vector_search.md`)

**Relevant chunks:**

- `chunk_2ab6cbd06f6e3de15c08df1239957715b8eb194bb2ba9477b596d1a5ad62d9d0`
  - Source: `qdrant_vector_search.md`, chunk 10
  - Short excerpt: can use `score_threshold` parameter of the search query. It will exclude all results with a score worse than the given. <aside role="status">This parameter may exclude lower or higher scores depending on the used metric.…
  - Relevance: 2

## q014

**Type:** fact

**Question:** Why can large offset pagination be unreliable for HNSW vector search?

**Reference answer:** HNSW is not designed to retrieve an arbitrary Nth neighbor without first retrieving earlier neighbors, so offsets can be expensive and may duplicate or skip points as the index changes.

**Relevant documents:**

- `doc_3f18686b3efe2fa035065d587481604931b8a3da8ba0c41e1d56bf801231058d` (`qdrant_vector_search.md`)

**Relevant chunks:**

- `chunk_4c30c5813d4188f2e9a8f618747134e97e40551a428c6df398f0eff1ae227033`
  - Source: `qdrant_vector_search.md`, chunk 17
  - Short excerpt: ery-points/with-offset/" >}} This is equivalent to retrieving the 11th page with 10 records per page. <aside role="alert">Large offset values may cause performance issues</aside> Vector-based retrieval in general, and th…
  - Relevance: 2
- `chunk_add09af55ae85b47c39406570995c783b243b6072562555b84ea4ea6dd3789be`
  - Source: `qdrant_vector_search.md`, chunk 18
  - Short excerpt: s. As a result, paginating with `offset` can return the same point on multiple pages or skip points entirely. There are several ways to work around this: #### Client-Side Pagination Retrieve a large batch in a single req…
  - Relevance: 1

## q015

**Type:** fact

**Question:** How does reciprocal rank fusion reward a document appearing in multiple result lists?

**Reference answer:** RRF sums contributions based on the document's rank in each result list, so documents near the top of one or several rankings receive larger fused scores.

**Relevant documents:**

- `doc_9c43d9706c0c1cdeca2b66726c352e1c4c664b3524573835ff114d769fe1a982` (`qdrant_hybrid_queries.md`)

**Relevant chunks:**

- `chunk_daae9d216ea721d25578ad69396dc72af20d7267122445f9bdbae428f05d3178`
  - Source: `qdrant_hybrid_queries.md`, chunk 3
  - Short excerpt: y and boosts those that appear closer to the top in multiple sets of results. The score of a document is calculated using its rank in each result set: $$ score(d\in D) = \sum_{r_d\in R(d)} \frac{1}{k + \frac{r_d + 1}{w_r…
  - Relevance: 2

## q016

**Type:** fact

**Question:** How does Qdrant's distribution-based score fusion normalize retriever scores?

**Reference answer:** DBSF uses each result set's score distribution to map scores into a comparable range before summing them; it is stateless and derives limits from the current query's returned points.

**Relevant documents:**

- `doc_9c43d9706c0c1cdeca2b66726c352e1c4c664b3524573835ff114d769fe1a982` (`qdrant_hybrid_queries.md`)

**Relevant chunks:**

- `chunk_2d04fab5dc6136820f1389a9fca36d962bd7d97d40115917270aa10060c0cfaf`
  - Source: `qdrant_hybrid_queries.md`, chunk 7
  - Short excerpt: etune when your retrievers change (new embedding model, new chunking), when your corpus drifts substantially, or on a fixed cadence with a fresh eval sample. ### Distribution-Based Score Fusion (DBSF) _Available as of v1…
  - Relevance: 2
- `chunk_26913a5d189a92dae0d4904f6f0f081337e8bf6258880e38a5025ccb5370aeb1`
  - Source: `qdrant_hybrid_queries.md`, chunk 8
  - Short excerpt: because each retriever contributes on the same comparable range. <aside role="status"><code>dbsf</code> is stateless and computes its normalization limits from each query's returned points, not from all the scores it has…
  - Relevance: 1

## q017

**Type:** fact

**Question:** What problem is semantic search intended to solve beyond literal keyword matching?

**Reference answer:** Semantic search tries to understand query and corpus meaning, allowing relevant matches despite synonyms, abbreviations, and misspellings.

**Relevant documents:**

- `doc_bf81b73c4b2c1bf01ca9d5f719272ec97efe4277e50d97585dc73cece6d3be1f` (`sentence_transformers_semantic_search.md`)

**Relevant chunks:**

- `chunk_0cdf74730e2d2bcb881afbfa93d5df579c1cf1b0778741bb2209ba2663f81456`
  - Source: `sentence_transformers_semantic_search.md`, chunk 0
  - Short excerpt: # Semantic Search Semantic search seeks to improve search accuracy by understanding the semantic meaning of the search query and the corpus to search over. Semantic search can also perform well given synonyms, abbreviati…
  - Relevance: 2

## q018

**Type:** fact

**Question:** What efficiency and quality trade-off does a CrossEncoder reranker introduce?

**Reference answer:** A CrossEncoder can substantially improve the final ordering of candidates but is too slow to score a very large corpus, so an efficient retriever first narrows the candidate set.

**Relevant documents:**

- `doc_222c62b30b8afbccb200e15c27755f8bdc8824ed40c5eaae8555358848f64c69` (`sentence_transformers_retrieve_rerank.md`)

**Relevant chunks:**

- `chunk_4ee9dba9bb33730e7f356d40e3da399bdac00a5b2006e46e251f2fd68c4b5f17`
  - Source: `sentence_transformers_retrieve_rerank.md`, chunk 3
  - Short excerpt: r The retriever has to be efficient for large document collections with millions of entries. However, it might return irrelevant candidates. A re-ranker based on a Cross-Encoder can substantially improve the final result…
  - Relevance: 2

## q019

**Type:** multi_chunk

**Question:** Describe the path from declaring a FastAPI dependency to receiving its value during a request.

**Reference answer:** A callable declares parameters like a path operation, it is passed to Depends in a dependent function, FastAPI resolves and calls it for each request, and injects its return value while reusing the declarations for validation and documentation.

**Relevant documents:**

- `doc_97add4ed2c662b4c580315e5bd07e009a5f6858dff61e42e572ebd5832f07d6f` (`fastapi_dependencies.md`)

**Relevant chunks:**

- `chunk_650291a57f062c2b9952069182c54be8e1b246992c87b738659aa622aa60bb72`
  - Source: `fastapi_dependencies.md`, chunk 0
  - Short excerpt: # Dependencies { #dependencies } **FastAPI** has a very powerful but intuitive **<dfn title="also known as components, resources, providers, services, injectables">Dependency Injection</dfn>** system. It is designed to b…
  - Relevance: 1
- `chunk_8410fc104cbba877f60c62dfba703377315027111519f18f84210962f5b41419`
  - Source: `fastapi_dependencies.md`, chunk 3
  - Short excerpt: to at least 0.95.1 before using `Annotated`. /// ### Import `Depends` { #import-depends } {* ../../docs_src/dependencies/tutorial001_an_py310.py hl[3] *} ### Declare the dependency, in the "dependant" { #declare-the-depe…
  - Relevance: 2
- `chunk_e20b19f85be3bb2ad4a48e82dbde5b128d82ad6a46633de0bdeeb6626ef8b134`
  - Source: `fastapi_dependencies.md`, chunk 4
  - Short excerpt: )`. And that function takes parameters in the same way that *path operation functions* do. /// tip You'll see what other "things", apart from functions, can be used as dependencies in the next chapter. /// Whenever a new…
  - Relevance: 2

## q020

**Type:** multi_chunk

**Question:** How do synchronous and asynchronous dependencies interact with path operations, and how are their requirements exposed?

**Reference answer:** FastAPI permits def and async def dependencies with either def or async def path operations, handles their execution, and integrates their declared requirements into OpenAPI and interactive docs.

**Relevant documents:**

- `doc_97add4ed2c662b4c580315e5bd07e009a5f6858dff61e42e572ebd5832f07d6f` (`fastapi_dependencies.md`)

**Relevant chunks:**

- `chunk_bb8ad8fb21de94977a41c262b82ebae2ae96d4542e03cd1fbd746e0e652b1b85`
  - Source: `fastapi_dependencies.md`, chunk 7
  - Short excerpt: ions. You can use `async def` or normal `def`. And you can declare dependencies with `async def` inside of normal `def` *path operation functions*, or `def` dependencies inside of `async def` *path operation functions*, …
  - Relevance: 2
- `chunk_1aedfeace05dc6386f5efa0b4c517ad926ce622e25a40c3a79120b71e65723c1`
  - Source: `fastapi_dependencies.md`, chunk 8
  - Short excerpt: ge } If you look at it, *path operation functions* are declared to be used whenever a *path* and *operation* matches, and then **FastAPI** takes care of calling the function with the correct parameters, extracting the da…
  - Relevance: 2

## q021

**Type:** multi_chunk

**Question:** What practical guidance does the Transformers Pipeline documentation give for deciding whether to batch inference?

**Reference answer:** Benchmark on the target hardware and data, use batch_size only when throughput benefits, account for padding and sequence lengths, and add OOM safeguards because batching can either accelerate or severely degrade inference.

**Relevant documents:**

- `doc_416c540cf133e4b620ffd26993838ac4fd5cbcf8219c196756bdf5f2765ed937` (`huggingface_pipeline_tutorial.md`)

**Relevant chunks:**

- `chunk_27822ef34f658c4cd363f1944247289ac26fda50bd962373b2fee1a78bcfbc01`
  - Source: `huggingface_pipeline_tutorial.md`, chunk 8
  - Short excerpt: from transformers import pipeline pipeline = pipeline(task="text-generation", model="google/gemma-2-2b", device="mps") pipeline("the secret to baking a really good cake is ") ``` </hfoption> </hfoptions> ### Batch infere…
  - Relevance: 1
- `chunk_598e09799a745d467c11a11c175ee994d48b165376c92cdefb623fa59627a7c8`
  - Source: `huggingface_pipeline_tutorial.md`, chunk 9
  - Short excerpt: device pipeline = pipeline(task="text-generation", model="google/gemma-2-2b", device=device, batch_size=2) pipeline(["the secret to baking a really good cake is", "a baguette is", "paris is the", "hotdogs are"]) [[{'gene…
  - Relevance: 1
- `chunk_46d56a255d1e286050a88cffde66dcf5cc823f9a5db6c306c0492336c7c7c29e`
  - Source: `huggingface_pipeline_tutorial.md`, chunk 10
  - Short excerpt: e = Accelerator().device # KeyDataset is a utility that returns the item in the dict returned by the dataset dataset = datasets.load_dataset("stanfordnlp/imdb", name="plain_text", split="unsupervised") pipeline = pipelin…
  - Relevance: 1
- `chunk_d3f2f420bb384f0afacf3b983021a087d8ab05cbdf9c81bf72ff031cdc1aced0`
  - Source: `huggingface_pipeline_tutorial.md`, chunk 11
  - Short excerpt: PU. 4. Don't batch inference if you don't know the `sequence_length` of your data. Measure performance, iteratively add to `sequence_length`, and include out-of-memory (OOM) checks to recover from failures. 5. Do batch i…
  - Relevance: 2

## q022

**Type:** multi_chunk

**Question:** How can Transformers Pipeline place a large model across hardware and reduce its memory requirements?

**Reference answer:** It can use Accelerate device mapping to distribute weights across available devices and lower-precision dtypes such as float16 or bfloat16 when supported to reduce memory use.

**Relevant documents:**

- `doc_416c540cf133e4b620ffd26993838ac4fd5cbcf8219c196756bdf5f2765ed937` (`huggingface_pipeline_tutorial.md`)

**Relevant chunks:**

- `chunk_fb426b5076f1819e1d1683752c9b7c36b1eca1967d6ac8d3076b1db374082653`
  - Source: `huggingface_pipeline_tutorial.md`, chunk 7
  - Short excerpt: cally choose how to load and store the model weights on the appropriate device. This is especially useful if you have multiple devices. Accelerate loads and stores the model weights on the fastest device first, and then …
  - Relevance: 2
- `chunk_225eb5db3693cb0136dbb65555425525067c8e7c038456a523bd705494271f76`
  - Source: `huggingface_pipeline_tutorial.md`, chunk 19
  - Short excerpt: 00): yield f"My example {i}" pipeline = pipeline(model="openai-community/gpt2", device=0) generated_characters = 0 for out in pipeline(data()): generated_characters += len(out[0]["generated_text"]) ``` ## Large models [A…
  - Relevance: 2
- `chunk_bade1d6d82717854c1d75addf0de233af7770a6c25a08b83fbaff88432cb1fa3`
  - Source: `huggingface_pipeline_tutorial.md`, chunk 20
  - Short excerpt: especially for larger ones. If your hardware supports it, you can enable torch.bfloat16 instead for more range. > [!TIP] > Inputs are internally converted to torch.float16 and it only works for models with a PyTorch back…
  - Relevance: 1

## q023

**Type:** multi_chunk

**Question:** What steps and configuration are involved in starting Text Embeddings Inference and requesting an embedding?

**Reference answer:** Start the appropriate TEI container with a model ID and mounted cache or model data, expose its port, then POST input text as JSON to the embed endpoint; compatible model IDs or local model directories can be used.

**Relevant documents:**

- `doc_804c8377e1908e9583942234825e7b5df1e3d0528aff172b36538e5a542bf6b0` (`huggingface_text_embeddings_inference.md`)

**Relevant chunks:**

- `chunk_932fdb9a277cfdeff13cdb952d4e871597fa55623430b160efcb15548536c9a3`
  - Source: `huggingface_text_embeddings_inference.md`, chunk 10
  - Short excerpt: ghts every run docker run --gpus all -p 8080:80 -v $volume:/data --pull always ghcr.io/huggingface/text-embeddings-inference:cuda-1.9 --model-id $model ``` And then you can make requests like ```bash curl 127.0.0.1:8080/…
  - Relevance: 2
- `chunk_bb5d240b51ad3e3deb3234193c79abecc9464d11ac6f6c21ecd5f316b8ccdccd`
  - Source: `huggingface_text_embeddings_inference.md`, chunk 11
  - Short excerpt: The Hugging Face model ID, can be any model listed on <https://huggingface.co/models> with the `text-embeddings-inference` tag (meaning it's compatible with Text Embeddings Inference). Alternatively, the specified ID can…
  - Relevance: 1

## q024

**Type:** multi_chunk

**Question:** How are reranker models deployed and queried through Text Embeddings Inference?

**Reference answer:** TEI supports sequence-classification cross-encoders as rerankers; launch a compatible reranker model, then POST a query and candidate texts to the rerank endpoint to receive similarity-based ranks.

**Relevant documents:**

- `doc_804c8377e1908e9583942234825e7b5df1e3d0528aff172b36538e5a542bf6b0` (`huggingface_text_embeddings_inference.md`)

**Relevant chunks:**

- `chunk_664c8b82b3110def99b5d756e8e43359f9ac5c1d8e6e2ba669bc03944617bf62`
  - Source: `huggingface_text_embeddings_inference.md`, chunk 26
  - Short excerpt: gs-inference:cuda-1.9 --model-id /data/Qwen3-Embedding-0.6B ``` ### Using Re-rankers models `text-embeddings-inference` v0.4.0 added support for CamemBERT, RoBERTa, XLM-RoBERTa, and GTE Sequence Classification models. Re…
  - Relevance: 2
- `chunk_f4d2887c85245189307680a3dc340510b9ff3096e825399fac5e4bd4e873d43a`
  - Source: `huggingface_text_embeddings_inference.md`, chunk 27
  - Short excerpt: pull always ghcr.io/huggingface/text-embeddings-inference:cuda-1.9 --model-id $model ``` And then you can rank the similarity between a query and a list of texts with: ```bash curl 127.0.0.1:8080/rerank \ -X POST \ -d '{…
  - Relevance: 2

## q025

**Type:** multi_chunk

**Question:** Compare Qdrant's must, should, and must_not filtering clauses.

**Reference answer:** must requires every listed condition like AND, should requires at least one like OR, and must_not requires none of the listed conditions to match; clauses can be combined and nested.

**Relevant documents:**

- `doc_1713ab05743cc108791b3eea9872aed4153364e83ba8337235146d6e25b302a9` (`qdrant_filtering.md`)

**Relevant chunks:**

- `chunk_09e6d8556030eaaddb06afe2568a4ba025b04a46d5a8b30b1a163c800da4000a`
  - Source: `qdrant_filtering.md`, chunk 2
  - Short excerpt: he following payload: ```json [ { "id": 1, "city": "London", "color": "green" }, { "id": 2, "city": "London", "color": "red" }, { "id": 3, "city": "London", "color": "blue" }, { "id": 4, "city": "Berlin", "color": "red" …
  - Relevance: 2
- `chunk_46234ee4cf4574915dc7c0c65e651d1e6ebe240ff12ef1e9e4c9dac9a43895e8`
  - Source: `qdrant_filtering.md`, chunk 3
  - Short excerpt: ide `should` is satisfied. In this sense, `should` is equivalent to the operator `OR`. Example: {{< code-snippet path="/documentation/headless/snippets/scroll-points/with-should-filter/" >}} Filtered points would be: ```…
  - Relevance: 2
- `chunk_c4ee9e989a7808f00c5a4966fa1be673254072a3e0bbea0446590bd1e08feebf`
  - Source: `qdrant_filtering.md`, chunk 4
  - Short excerpt: ense, `must_not` is equivalent to the expression `(NOT A) AND (NOT B) AND (NOT C)`. Example: {{< code-snippet path="/documentation/headless/snippets/scroll-points/with-must-not-filter/" >}} Filtered points would be: ```j…
  - Relevance: 2

## q026

**Type:** multi_chunk

**Question:** How does Qdrant filter nested fields and ensure conditions match within one array element?

**Reference answer:** Dot notation addresses nested fields and [] projects values through arrays, while a nested object filter scopes all conditions to each individual array element and accepts a parent when one element satisfies them together.

**Relevant documents:**

- `doc_1713ab05743cc108791b3eea9872aed4153364e83ba8337235146d6e25b302a9` (`qdrant_filtering.md`)

**Relevant chunks:**

- `chunk_48adabf5d9956c31112353e70866084cdad60b384495ae2f9fa1bdf4eb078bdb`
  - Source: `qdrant_filtering.md`, chunk 9
  - Short excerpt: n.github.io/jq/manual/#Basicfilters) project. Suppose we have a set of points with the following payload: ```json [ { "id": 1, "country": { "name": "Germany", "cities": [ { "name": "Berlin", "population": 3.7, "sightseei…
  - Relevance: 1
- `chunk_bf5ff7d6646dd386ce55f4a6a43b5127af79536d6b79c07f888e01b0f571f128`
  - Source: `qdrant_filtering.md`, chunk 10
  - Short excerpt: , "Universal Studios Japan"] } ] } } ] ``` You can search on a nested field using a dot notation. {{< code-snippet path="/documentation/headless/snippets/scroll-points/with-filter-on-nested-fields/" >}} You can also sear…
  - Relevance: 2
- `chunk_3af51a31bbbc0f3575860a94af5242bdcc036b967b34a316676f6be760688823`
  - Source: `qdrant_filtering.md`, chunk 12
  - Short excerpt: and likes=true on `diet[1].likes` - the "diplodocus" matches food=meat on `diet[1].food` and likes=true on `diet[0].likes` To retrieve only the points which are matching the conditions on an array element basis, that is …
  - Relevance: 2
- `chunk_67dfc506017e8700771afc3d03c08e33123053c97c1815e07c3f73b32fdb059b`
  - Source: `qdrant_filtering.md`, chunk 13
  - Short excerpt: rray element within the payload. Nested filters work in the same way as if the nested filter was applied to a single element of the array at a time. Parent document is considered to match the condition if at least one el…
  - Relevance: 1

## q027

**Type:** multi_chunk

**Question:** How can Qdrant group chunk-level search hits by document and attach document-level metadata without duplicating it on every chunk?

**Reference answer:** Store document_id on chunk points, group search hits by that field, keep titles or abstracts once in a separate document collection, and use with_lookup to attach the matching document payload.

**Relevant documents:**

- `doc_3f18686b3efe2fa035065d587481604931b8a3da8ba0c41e1d56bf801231058d` (`qdrant_vector_search.md`)

**Relevant chunks:**

- `chunk_76f1595996b9fc24a98741c470092b714dbcc142a4d3e31b2ed722e1ab00d59a`
  - Source: `qdrant_vector_search.md`, chunk 20
  - Short excerpt: en you have multiple points for the same item, and you want to avoid redundancy of the same item in the results. For example, if you have a large document split into multiple chunks, and you want to search or [recommend]…
  - Relevance: 2
- `chunk_6233fd013f990d7e934e558a3374c2e58d2cb5e47aa09191ace849a4ac11ab75`
  - Source: `qdrant_vector_search.md`, chunk 21
  - Short excerpt: ument_id": "a" }, "vector": [0.2] }, { "id": 3, "payload": { "chunk_part": 0, "document_id": 123 }, "vector": [0.79] }, { "id": 4, "payload": { "chunk_part": 1, "document_id": 123 }, "vector": [0.75] }, { "id": 5, "paylo…
  - Relevance: 1
- `chunk_77726f764418f4461cf31408602cf67433f3c4751ad59efa23a10e2c1ab614bb`
  - Source: `qdrant_vector_search.md`, chunk 25
  - Short excerpt: <aside role="status">Store only document-level metadata (e.g., titles, abstracts) in the lookup collection, not chunks or duplicated data.</aside> Set up the two collections. `chunks` holds one point per chunk with its o…
  - Relevance: 2
- `chunk_87346f39468b342c5af8df04c039b2317abfb529aee8e4a69504c1c523bc4067`
  - Source: `qdrant_vector_search.md`, chunk 26
  - Short excerpt: ` value from each chunk. - The id types must match. A string `group_by` value against integer point ids returns an empty `lookup` field with no error. - Group ids without a matching point in `documents` get an empty `loo…
  - Relevance: 2

## q028

**Type:** multi_chunk

**Question:** How does Qdrant use prefetches for a coarse-to-fine multi-stage search?

**Reference answer:** Prefetch subqueries first produce candidates using cheaper or smaller representations, and the main query then scores or rescoring those candidates with a more accurate representation; prefetch limits must supply enough candidates.

**Relevant documents:**

- `doc_9c43d9706c0c1cdeca2b66726c352e1c4c664b3524573835ff114d769fe1a982` (`qdrant_hybrid_queries.md`)

**Relevant chunks:**

- `chunk_b25a05265a1716f196444b59a292327a26563d7a47e76d73082e3cc0e1b106d7`
  - Source: `qdrant_hybrid_queries.md`, chunk 1
  - Short excerpt: an one stage. Qdrant has a flexible and universal interface to make this possible, called `Query API` ([API reference](https://api.qdrant.tech/api-reference/search/query-points)). The main component for making the combin…
  - Relevance: 2
- `chunk_0747f054593e6ff29eae3d2a19fb6cf0583a927b697268ef68143f7abf346728`
  - Source: `qdrant_hybrid_queries.md`, chunk 11
  - Short excerpt: expensive to compute. Splitting the search into two stages is a known technique to mitigate this effect: - First, use a smaller and cheaper representation to get a large list of candidates. - Then, re-score the candidate…
  - Relevance: 2
- `chunk_560b3b4dc3257bcef98fab21ba8bd718e1813e942ec476deee63c715b860f225`
  - Source: `qdrant_hybrid_queries.md`, chunk 12
  - Short excerpt: get="_blank">ColBERT</a>. To get the best of all worlds, Qdrant has a convenient interface to perform the queries in stages, such that the coarse results are fetched first, and then they are refined later with larger vec…
  - Relevance: 2

## q029

**Type:** multi_chunk

**Question:** How should query and document encoding differ for symmetric versus asymmetric semantic search?

**Reference answer:** Symmetric search uses similarly sized query and corpus texts, while asymmetric search maps short queries to longer answer passages; recommended models may use encode_query and encode_document so prompts and routing reflect those roles.

**Relevant documents:**

- `doc_bf81b73c4b2c1bf01ca9d5f719272ec97efe4277e50d97585dc73cece6d3be1f` (`sentence_transformers_semantic_search.md`)

**Relevant chunks:**

- `chunk_06250ca9a7eb20a7e85ee596dc60d6dbf214a16dc22dad20af72bca7e991a9f0`
  - Source: `sentence_transformers_semantic_search.md`, chunk 1
  - Short excerpt: ## Symmetric vs. Asymmetric Semantic Search A **critical distinction** for your setup is *symmetric* vs. *asymmetric semantic search*: - For **symmetric semantic search** your query and the entries in your corpus are of …
  - Relevance: 2
- `chunk_17a5d8f499175342dcfadb660c2c918b02ad3c9f1fd440f03589f9858a11ba69`
  - Source: `sentence_transformers_semantic_search.md`, chunk 2
  - Short excerpt: **asymmetric semantic search**, you usually have a **short query** (like a question or some keywords) and you want to find a longer paragraph answering the query. An example would be a query like *"What is Python"* and y…
  - Relevance: 2
- `chunk_eda42c71fd82000acf67de25aba3eda328149d54470916926e22c7859420ca8e`
  - Source: `sentence_transformers_semantic_search.md`, chunk 3
  - Short excerpt: o use :meth:`SentenceTransformer.encode_query <sentence_transformers.sentence_transformer.model.SentenceTransformer.encode_query>` to encode your queries and :meth:`SentenceTransformer.encode_document <sentence_transform…
  - Relevance: 2
- `chunk_810ee57ef050d3e1d6aaa73ffc7e6d8d51ca9b11454f0a45e649d5bc90810485`
  - Source: `sentence_transformers_semantic_search.md`, chunk 4
  - Short excerpt: , it uses a predefined "query" or "document" prompt, if specified in the model's ``prompts`` dictionary. 2. It sets the ``task`` to "document". If the model has a :class:`~sentence_transformers.base.modules.Router` modul…
  - Relevance: 1

## q030

**Type:** multi_chunk

**Question:** What options does Sentence Transformers describe for scaling semantic search beyond a manual in-memory implementation?

**Reference answer:** Use the optimized semantic_search utility for suitable corpora, keep query and corpus embeddings on the same GPU when possible, or use approximate-nearest-neighbor/vector systems such as FAISS, Annoy, HNSWlib, Elasticsearch, or OpenSearch for larger corpora.

**Relevant documents:**

- `doc_bf81b73c4b2c1bf01ca9d5f719272ec97efe4277e50d97585dc73cece6d3be1f` (`sentence_transformers_semantic_search.md`)

**Relevant chunks:**

- `chunk_293b419bb31d44e5b59d6b65009b2708fa24711d3372d2db12d3ea963c260721`
  - Source: `sentence_transformers_semantic_search.md`, chunk 9
  - Short excerpt: ased on artificial neural networks with representation learning. .. literalinclude:: semantic_search.py ``` ## Optimized Implementation ```{eval-rst} Instead of implementing semantic search by yourself, you can use the :…
  - Relevance: 2
- `chunk_bb8e3f0d06c7af0619a884ab227019958efbf2131176dd7e32325fadb6c8cd64`
  - Source: `sentence_transformers_semantic_search.md`, chunk 10
  - Short excerpt: antic_search` method, it is advisable to have the ``query_embeddings`` as well as the ``corpus_embeddings`` on the same GPU-device. This significantly boost the performance. Further, we can normalize the corpus embedding…
  - Relevance: 1
- `chunk_e7cb4194151d952f056f76892bf3babf9c012b6cb75a5b8aa2fe83551fba3122`
  - Source: `sentence_transformers_semantic_search.md`, chunk 11
  - Short excerpt: arch](https://www.elastic.co/elasticsearch/) has the possibility to [index dense vectors](https://www.elastic.co/what-is/vector-search) and to use them for document scoring. We can easily index embedding vectors, store o…
  - Relevance: 1
- `chunk_ce3b9c13747da4f724510d997079023a5dc5e4a9b81e945ed4c53fbf79bc2f79`
  - Source: `sentence_transformers_semantic_search.md`, chunk 12
  - Short excerpt: fficient similarity search using approximate nearest neighbor algorithms. OpenSearch can be used to implement both traditional keyword-based search (BM25) and semantic search, making it possible to compare and combine bo…
  - Relevance: 1
- `chunk_effe795c19ee0c01b9ae4ebe9b5ff8c26444740a20befb28c3555ed12092f4ca`
  - Source: `sentence_transformers_semantic_search.md`, chunk 13
  - Short excerpt: s partitioned into smaller fractions of similar embeddings. This index can be searched efficiently and the embeddings with the highest similarity (the nearest neighbors) can be retrieved within milliseconds, even if you …
  - Relevance: 2

## q031

**Type:** cross_document

**Question:** Why can dense semantic retrieval find matches that lexical search misses?

**Reference answer:** Dense semantic retrieval compares learned meaning representations and can match synonyms, abbreviations, and misspellings, whereas lexical retrieval depends on literal query-word matches and may miss equivalent wording.

**Relevant documents:**

- `doc_bf81b73c4b2c1bf01ca9d5f719272ec97efe4277e50d97585dc73cece6d3be1f` (`sentence_transformers_semantic_search.md`)
- `doc_222c62b30b8afbccb200e15c27755f8bdc8824ed40c5eaae8555358848f64c69` (`sentence_transformers_retrieve_rerank.md`)

**Relevant chunks:**

- `chunk_0cdf74730e2d2bcb881afbfa93d5df579c1cf1b0778741bb2209ba2663f81456`
  - Source: `sentence_transformers_semantic_search.md`, chunk 0
  - Short excerpt: # Semantic Search Semantic search seeks to improve search accuracy by understanding the semantic meaning of the search query and the corpus to search over. Semantic search can also perform well given synonyms, abbreviati…
  - Relevance: 2
- `chunk_9ac8a4dcfbb4f61f931863f6ff5b68726298a893cd95f332bb806225fcdf8a38`
  - Source: `sentence_transformers_retrieve_rerank.md`, chunk 2
  - Short excerpt: w.elastic.co/elasticsearch/)), or we can use a bi-encoder which is implemented in Sentence Transformers. Lexical search looks for literal matches of the query words in your document collection. It will not recognize syno…
  - Relevance: 2

## q032

**Type:** cross_document

**Question:** How does a bi-encoder and CrossEncoder two-stage retrieval pipeline work?

**Reference answer:** A fast bi-encoder independently embeds the query and corpus to retrieve a candidate set; a slower CrossEncoder then scores query-candidate pairs and reranks the best candidates for final presentation.

**Relevant documents:**

- `doc_222c62b30b8afbccb200e15c27755f8bdc8824ed40c5eaae8555358848f64c69` (`sentence_transformers_retrieve_rerank.md`)
- `doc_bf81b73c4b2c1bf01ca9d5f719272ec97efe4277e50d97585dc73cece6d3be1f` (`sentence_transformers_semantic_search.md`)

**Relevant chunks:**

- `chunk_b695c1d3749ee3365c1077023f0b3aeb3d24ae1e9b34e53e47288ee8f69f3b10`
  - Source: `sentence_transformers_retrieve_rerank.md`, chunk 0
  - Short excerpt: # Retrieve & Re-Rank In [Semantic Search](../semantic-search/README.md) we have shown how to use SentenceTransformer to compute embeddings for queries, sentences, and paragraphs and how to use this for semantic search. F…
  - Relevance: 1
- `chunk_974c0df1918ac55b24e97853137d247ce88e7ef3583b33dcc8bb30fa3f5e26b7`
  - Source: `sentence_transformers_retrieve_rerank.md`, chunk 1
  - Short excerpt: sible hits which are potentially relevant for the query. For the retrieval, we can use either lexical search, e.g. with a vector engine like Elasticsearch, or we can use dense retrieval with a :class:`~sentence_transform…
  - Relevance: 2
- `chunk_4ee9dba9bb33730e7f356d40e3da399bdac00a5b2006e46e251f2fd68c4b5f17`
  - Source: `sentence_transformers_retrieve_rerank.md`, chunk 3
  - Short excerpt: r The retriever has to be efficient for large document collections with millions of entries. However, it might return irrelevant candidates. A re-ranker based on a Cross-Encoder can substantially improve the final result…
  - Relevance: 2
- `chunk_f77f5aa237e8adacaeb1cf4105e66b9737c7a3c1d1df3ff7cccf290b7a2c5ad0`
  - Source: `sentence_transformers_semantic_search.md`, chunk 18
  - Short excerpt: a.ipynb) ]: This script uses the [Retrieve & Re-rank](../retrieve_rerank/README.md) strategy and is an example for an **asymmetric search task**. We split all Wikipedia articles into paragraphs and encode them with a bi-…
  - Relevance: 1

## q033

**Type:** cross_document

**Question:** How do local SentenceTransformer embedding calls differ from serving embeddings with Text Embeddings Inference?

**Reference answer:** SentenceTransformer loads a model in the Python process and returns arrays from encode, while TEI runs compatible models as a serving system and exposes endpoints such as /embed with batching and operational features.

**Relevant documents:**

- `doc_da10badd8e53f12427e79c26045c803ee25ee0e4bc0cd79a88904bbd8e8ec593` (`sentence_transformers_overview.md`)
- `doc_804c8377e1908e9583942234825e7b5df1e3d0528aff172b36538e5a542bf6b0` (`huggingface_text_embeddings_inference.md`)

**Relevant chunks:**

- `chunk_b8e00336e349a014f2a034f36498de7b65a2f63853969a38942bace3ba755af0`
  - Source: `sentence_transformers_overview.md`, chunk 4
  - Short excerpt: ransformers ``` See [Installation](https://www.sbert.net/docs/installation.html) in the docs for uv, conda, source, and editable installs, CUDA setup, and extras (`[image]`, `[audio]`, `[video]`, `[train]`, `[onnx]`, `[o…
  - Relevance: 2
- `chunk_3119cb0c2a7b12e9cd954a6e8b47d18c24c3626e3d3e791e1573d0435ddfa0da`
  - Source: `sentence_transformers_overview.md`, chunk 5
  - Short excerpt: shape) # => (3, 384) ``` And that's already it. We now have numpy arrays with the embeddings, one for each text. We can use these to compute similarities. ```python similarities = model.similarity(embeddings, embeddings)…
  - Relevance: 2
- `chunk_88acf2e84e52b7fc08a9e4d8c192e58752cf204ff470b0e62090af7b9d041c5e`
  - Source: `huggingface_text_embeddings_inference.md`, chunk 2
  - Short excerpt: - [AMD Instinct GPUs (ROCm)](#amd-instinct-gpus-rocm-experimental) - [Examples](#examples) Text Embeddings Inference (TEI) is a toolkit for deploying and serving open source text embeddings and sequence classification mo…
  - Relevance: 1
- `chunk_932fdb9a277cfdeff13cdb952d4e871597fa55623430b160efcb15548536c9a3`
  - Source: `huggingface_text_embeddings_inference.md`, chunk 10
  - Short excerpt: ghts every run docker run --gpus all -p 8080:80 -v $volume:/data --pull always ghcr.io/huggingface/text-embeddings-inference:cuda-1.9 --model-id $model ``` And then you can make requests like ```bash curl 127.0.0.1:8080/…
  - Relevance: 2

## q034

**Type:** cross_document

**Question:** How are embeddings and cosine similarity used from Sentence Transformers through Qdrant search?

**Reference answer:** Sentence Transformers encodes text into numeric vectors whose similarity can be compared; Qdrant stores those vectors, normalizes them for cosine distance when inserted, and retrieves nearest vectors by similarity.

**Relevant documents:**

- `doc_da10badd8e53f12427e79c26045c803ee25ee0e4bc0cd79a88904bbd8e8ec593` (`sentence_transformers_overview.md`)
- `doc_bf81b73c4b2c1bf01ca9d5f719272ec97efe4277e50d97585dc73cece6d3be1f` (`sentence_transformers_semantic_search.md`)
- `doc_3f18686b3efe2fa035065d587481604931b8a3da8ba0c41e1d56bf801231058d` (`qdrant_vector_search.md`)

**Relevant chunks:**

- `chunk_3119cb0c2a7b12e9cd954a6e8b47d18c24c3626e3d3e791e1573d0435ddfa0da`
  - Source: `sentence_transformers_overview.md`, chunk 5
  - Short excerpt: shape) # => (3, 384) ``` And that's already it. We now have numpy arrays with the embeddings, one for each text. We can use these to compute similarities. ```python similarities = model.similarity(embeddings, embeddings)…
  - Relevance: 2
- `chunk_701b073b904ebc87cbe31d2e2de19a6bb2a018e74fb783926ce68044560a9f0a`
  - Source: `sentence_transformers_semantic_search.md`, chunk 5
  - Short excerpt: mantic search with a manual implementation by computing the embeddings for the corpus with :meth:`SentenceTransformer.encode_document <sentence_transformers.sentence_transformer.model.SentenceTransformer.encode_document>…
  - Relevance: 1
- `chunk_c009ce573faa73149f54c4673a75779ef3616b8e15f771968c3ebfe2423c94fb`
  - Source: `qdrant_vector_search.md`, chunk 4
  - Short excerpt: sup>*Available as of v1.7</sup></i> The most typical metric used in similarity learning models is the cosine metric. ![Embeddings](/docs/cos.png) Qdrant counts this metric in 2 steps, due to which a higher search speed i…
  - Relevance: 2

## q035

**Type:** cross_document

**Question:** What is the difference between filtering Qdrant candidates and boosting their final ranking with metadata?

**Reference answer:** Filtering uses payload or ID conditions to include or exclude candidates according to constraints, while formula-based score boosting keeps candidates but adjusts their ranking using payload values, conditions, or prefetch scores.

**Relevant documents:**

- `doc_1713ab05743cc108791b3eea9872aed4153364e83ba8337235146d6e25b302a9` (`qdrant_filtering.md`)
- `doc_e0b54fd30a8994f981c5d01994cd97f3dcb6ab4d668c0726a607ee2a6bcd65d9` (`qdrant_search_relevance.md`)

**Relevant chunks:**

- `chunk_3a6dc08677006a4600ef6a9b8c49e1bd5b915581b73365b774d69a524563f3f9`
  - Source: `qdrant_filtering.md`, chunk 0
  - Short excerpt: --- title: Filtering short_description: "Combine vector similarity with payload filters in Qdrant to enforce business rules and refine search results." description: "Filter Qdrant search results with payload conditions o…
  - Relevance: 2
- `chunk_60e454d80cf03c03c89ebf1b5d7aa74e47c5c50e8430dc07d01b5fda5effa63c`
  - Source: `qdrant_filtering.md`, chunk 1
  - Short excerpt: uirements: stock availability, user location, or desired price range. <aside role="status"> For performant filtering, create <a href="/documentation/manage-data/indexing/#payload-index">payload indexes</a> for the fields…
  - Relevance: 1
- `chunk_03bc9339b320b54d706ca43b51c994a8d156c2437019eec56e8ecdd1416ff6b0`
  - Source: `qdrant_search_relevance.md`, chunk 1
  - Short excerpt: business logic needs to be considered for ranking the final list of results. A quick example is [our own documentation search bar](https://github.com/qdrant/page-search). It has vectors for every part of the documentatio…
  - Relevance: 2
- `chunk_660999ac8beb0abeddcf77b8c65216c4074858f63979d8a66830712df0c7859c`
  - Source: `qdrant_search_relevance.md`, chunk 2
  - Short excerpt: on: - Dynamic payload values - Conditions - Scores of prefetches To express the formula, the syntax uses objects to identify each element. Taking the documentation example, the request would look like this: {{< code-snip…
  - Relevance: 2

## q036

**Type:** cross_document

**Question:** How can Qdrant apply business signals after a hybrid retrieval stage?

**Reference answer:** Fuse prefetched retriever results, then use a Formula Query to compose a final score from fused scores, payload fields, conditions, and optional decay terms, calibrated so business signals do not dominate unintentionally.

**Relevant documents:**

- `doc_9c43d9706c0c1cdeca2b66726c352e1c4c664b3524573835ff114d769fe1a982` (`qdrant_hybrid_queries.md`)
- `doc_e0b54fd30a8994f981c5d01994cd97f3dcb6ab4d668c0726a607ee2a6bcd65d9` (`qdrant_search_relevance.md`)

**Relevant chunks:**

- `chunk_a7ed49b61fa12fd52b85a03f1fbc25e6de3bb6daba60e853c0edc5909a5bc4da`
  - Source: `qdrant_hybrid_queries.md`, chunk 13
  - Short excerpt: e-snippet path="/documentation/headless/snippets/query-points/hybrid-rescoring-multivector/" >}} You can combine all of these techniques in a single query: {{< code-snippet path="/documentation/headless/snippets/query-po…
  - Relevance: 2
- `chunk_68fead02254360d99f7653254b8ad4865b2a5f2a88a56eed779ce1f3b88d4bec`
  - Source: `qdrant_hybrid_queries.md`, chunk 14
  - Short excerpt: -decay/" >}} <aside role="status">Calibrate the decay weight against the scale of your fused <code>$score</code>. RRF scores are small (sums of <code>1/(k+rank)</code> terms), while decay functions return values in <code…
  - Relevance: 2
- `chunk_660999ac8beb0abeddcf77b8c65216c4074858f63979d8a66830712df0c7859c`
  - Source: `qdrant_search_relevance.md`, chunk 2
  - Short excerpt: on: - Dynamic payload values - Conditions - Scores of prefetches To express the formula, the syntax uses objects to identify each element. Taking the documentation example, the request would look like this: {{< code-snip…
  - Relevance: 2
- `chunk_6d7706c757314b6b3748e0b8626fb8919385688cd9d5872c5b558f8b077e2b7c`
  - Source: `qdrant_search_relevance.md`, chunk 5
  - Short excerpt: nd no defined default, a default value of `0.0` is used. <aside role="status"> **Considerations when using formula queries:** - Formula queries can only be used as a rescoring step. - Formula results are always sorted in…
  - Relevance: 1

## q037

**Type:** cross_document

**Question:** What corpus guidance helps keep retrieval evaluation reproducible and avoids tuning bias?

**Reference answer:** Use fixed query/relevance splits so parameters are tuned and measured on different data, retest when retrievers or corpora change, and use reproducible sampling rather than fresh random samples when constructing evaluation subsets.

**Relevant documents:**

- `doc_9c43d9706c0c1cdeca2b66726c352e1c4c664b3524573835ff114d769fe1a982` (`qdrant_hybrid_queries.md`)
- `doc_3f18686b3efe2fa035065d587481604931b8a3da8ba0c41e1d56bf801231058d` (`qdrant_vector_search.md`)

**Relevant chunks:**

- `chunk_2a106c2dfaf96b7f2e68d71f3125c76a6a3e0f3cbe501a36ad0c34fb654cd5e1`
  - Source: `qdrant_hybrid_queries.md`, chunk 6
  - Short excerpt: ry-points/hybrid-rrf-weights/" >}} Weights are a configuration choice, not something you can tune arbitrarily. The most reliable way to set them is by testing on your data. - **With an eval set (queries paired with known…
  - Relevance: 2
- `chunk_2d04fab5dc6136820f1389a9fca36d962bd7d97d40115917270aa10060c0cfaf`
  - Source: `qdrant_hybrid_queries.md`, chunk 7
  - Short excerpt: etune when your retrievers change (new embedding model, new chunking), when your corpus drifts substantially, or on a fixed cadence with a fresh eval sample. ### Distribution-Based Score Fusion (DBSF) _Available as of v1…
  - Relevance: 1
- `chunk_898688bf990e34cdc55f47c24c42ca0a948d72069a895f6ab9b13b0ff55631ae`
  - Source: `qdrant_vector_search.md`, chunk 29
  - Short excerpt: or providing entry points for exploration. Random sampling API is a part of [Universal Query API](#query-api) and can be used in the same way as regular search API. {{< code-snippet path="/documentation/headless/snippets…
  - Relevance: 2

## q038

**Type:** cross_document

**Question:** How does rank or score fusion differ from candidate retrieve-and-rerank?

**Reference answer:** Fusion combines rankings or normalized scores from multiple retrievers into one ordering, while retrieve-and-rerank uses a fast first-stage retriever to select candidates and a more accurate model to rescore those candidates.

**Relevant documents:**

- `doc_9c43d9706c0c1cdeca2b66726c352e1c4c664b3524573835ff114d769fe1a982` (`qdrant_hybrid_queries.md`)
- `doc_222c62b30b8afbccb200e15c27755f8bdc8824ed40c5eaae8555358848f64c69` (`sentence_transformers_retrieve_rerank.md`)

**Relevant chunks:**

- `chunk_daae9d216ea721d25578ad69396dc72af20d7267122445f9bdbae428f05d3178`
  - Source: `qdrant_hybrid_queries.md`, chunk 3
  - Short excerpt: y and boosts those that appear closer to the top in multiple sets of results. The score of a document is calculated using its rank in each result set: $$ score(d\in D) = \sum_{r_d\in R(d)} \frac{1}{k + \frac{r_d + 1}{w_r…
  - Relevance: 2
- `chunk_2d04fab5dc6136820f1389a9fca36d962bd7d97d40115917270aa10060c0cfaf`
  - Source: `qdrant_hybrid_queries.md`, chunk 7
  - Short excerpt: etune when your retrievers change (new embedding model, new chunking), when your corpus drifts substantially, or on a fixed cadence with a fresh eval sample. ### Distribution-Based Score Fusion (DBSF) _Available as of v1…
  - Relevance: 1
- `chunk_0747f054593e6ff29eae3d2a19fb6cf0583a927b697268ef68143f7abf346728`
  - Source: `qdrant_hybrid_queries.md`, chunk 11
  - Short excerpt: expensive to compute. Splitting the search into two stages is a known technique to mitigate this effect: - First, use a smaller and cheaper representation to get a large list of candidates. - Then, re-score the candidate…
  - Relevance: 1
- `chunk_4ee9dba9bb33730e7f356d40e3da399bdac00a5b2006e46e251f2fd68c4b5f17`
  - Source: `sentence_transformers_retrieve_rerank.md`, chunk 3
  - Short excerpt: r The retriever has to be efficient for large document collections with millions of entries. However, it might return irrelevant candidates. A re-ranker based on a Cross-Encoder can substantially improve the final result…
  - Relevance: 2
- `chunk_5d1888374f003ec75ae4929befb69aa3e999258614424b03ea635ad632144185`
  - Source: `sentence_transformers_retrieve_rerank.md`, chunk 4
  - Short excerpt: 100 possible candidates which are then re-ranked by the Cross-Encoder. ## Example Scripts - **[retrieve_rerank_simple_wikipedia.ipynb](retrieve_rerank_simple_wikipedia.ipynb)** [ [Colab Version](https://colab.research.go…
  - Relevance: 1

## q039

**Type:** cross_document

**Question:** When would an application use a Transformers Pipeline directly instead of a Text Embeddings Inference server?

**Reference answer:** Pipeline provides in-process task inference with configurable models and task parameters, while TEI is intended to deploy embedding or sequence-classification models behind a high-performance service API with batching and production observability.

**Relevant documents:**

- `doc_416c540cf133e4b620ffd26993838ac4fd5cbcf8219c196756bdf5f2765ed937` (`huggingface_pipeline_tutorial.md`)
- `doc_804c8377e1908e9583942234825e7b5df1e3d0528aff172b36538e5a542bf6b0` (`huggingface_text_embeddings_inference.md`)

**Relevant chunks:**

- `chunk_64c08ef9caee05d1cd40f44ee39c612dd1e8c9398f90bce428cfd0cd4b2c662a`
  - Source: `huggingface_pipeline_tutorial.md`, chunk 1
  - Short excerpt: werful inference API that is readily available for a variety of machine learning tasks with any model from the Hugging Face [Hub](https://hf.co/models). Tailor the [`Pipeline`] to your task with task specific parameters …
  - Relevance: 2
- `chunk_d1180e8d6ffd5cce2f77e63f9a9f9f1332b94b7582a8c9c029a86e012847ea45`
  - Source: `huggingface_pipeline_tutorial.md`, chunk 2
  - Short excerpt: is configured to use a default pretrained model and preprocessor, but this can be overridden with the `model` parameter if you want to use a different model. For example, to use the [`TextGenerationPipeline`] with [Gemma…
  - Relevance: 1
- `chunk_88acf2e84e52b7fc08a9e4d8c192e58752cf204ff470b0e62090af7b9d041c5e`
  - Source: `huggingface_text_embeddings_inference.md`, chunk 2
  - Short excerpt: - [AMD Instinct GPUs (ROCm)](#amd-instinct-gpus-rocm-experimental) - [Examples](#examples) Text Embeddings Inference (TEI) is a toolkit for deploying and serving open source text embeddings and sequence classification mo…
  - Relevance: 2
- `chunk_932fdb9a277cfdeff13cdb952d4e871597fa55623430b160efcb15548536c9a3`
  - Source: `huggingface_text_embeddings_inference.md`, chunk 10
  - Short excerpt: ghts every run docker run --gpus all -p 8080:80 -v $volume:/data --pull always ghcr.io/huggingface/text-embeddings-inference:cuda-1.9 --model-id $model ``` And then you can make requests like ```bash curl 127.0.0.1:8080/…
  - Relevance: 1

## q040

**Type:** cross_document

**Question:** How do the Sentence Transformers and TEI documents characterize reranker models?

**Reference answer:** Both describe rerankers as CrossEncoder or sequence-classification models that score a query together with candidate text; they improve candidate ordering but operate after a smaller candidate set has been retrieved.

**Relevant documents:**

- `doc_222c62b30b8afbccb200e15c27755f8bdc8824ed40c5eaae8555358848f64c69` (`sentence_transformers_retrieve_rerank.md`)
- `doc_804c8377e1908e9583942234825e7b5df1e3d0528aff172b36538e5a542bf6b0` (`huggingface_text_embeddings_inference.md`)
- `doc_da10badd8e53f12427e79c26045c803ee25ee0e4bc0cd79a88904bbd8e8ec593` (`sentence_transformers_overview.md`)

**Relevant chunks:**

- `chunk_4ee9dba9bb33730e7f356d40e3da399bdac00a5b2006e46e251f2fd68c4b5f17`
  - Source: `sentence_transformers_retrieve_rerank.md`, chunk 3
  - Short excerpt: r The retriever has to be efficient for large document collections with millions of entries. However, it might return irrelevant candidates. A re-ranker based on a Cross-Encoder can substantially improve the final result…
  - Relevance: 2
- `chunk_664c8b82b3110def99b5d756e8e43359f9ac5c1d8e6e2ba669bc03944617bf62`
  - Source: `huggingface_text_embeddings_inference.md`, chunk 26
  - Short excerpt: gs-inference:cuda-1.9 --model-id /data/Qwen3-Embedding-0.6B ``` ### Using Re-rankers models `text-embeddings-inference` v0.4.0 added support for CamemBERT, RoBERTa, XLM-RoBERTa, and GTE Sequence Classification models. Re…
  - Relevance: 2
- `chunk_f4d2887c85245189307680a3dc340510b9ff3096e825399fac5e4bd4e873d43a`
  - Source: `huggingface_text_embeddings_inference.md`, chunk 27
  - Short excerpt: pull always ghcr.io/huggingface/text-embeddings-inference:cuda-1.9 --model-id $model ``` And then you can rank the similarity between a query and a list of texts with: ```bash curl 127.0.0.1:8080/rerank \ -X POST \ -d '{…
  - Relevance: 1
- `chunk_4fb86452a7511b3fc9d93d27bb07c748a6377ba1f0dae6da3a4eb2af37009e06`
  - Source: `sentence_transformers_overview.md`, chunk 1
  - Short excerpt: go=pypi&style=flat&color=green)][#pypi-package] --> <!--- BADGES: END ---> # Sentence Transformers: Embeddings, Retrieval, and Reranking This framework provides an easy method to compute embeddings for accessing, using, …
  - Relevance: 1
