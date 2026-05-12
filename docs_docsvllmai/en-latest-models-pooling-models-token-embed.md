---
title: Token Embedding Usages - vLLM
url: https://docs.vllm.ai/en/latest/models/pooling_models/token_embed/
source: sitemap
fetched_at: 2026-05-07T21:15:06.828121127-03:00
rendered_js: false
word_count: 457
summary: This document explains how to perform token-level embedding tasks in vLLM, including configuration for offline and online APIs, supported model architectures, and use cases like multi-vector retrieval and late interaction.
tags:
    - vllm
    - token-embedding
    - multi-vector-retrieval
    - late-interaction
    - model-serving
    - inference-api
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/models/pooling_models/token_embed.md "Edit this page")

## Summary[¶](#summary "Permanent link")

- Model Usage: Token classification models
- Pooling Tasks: `token_embed`
- Offline APIs:
  
  - `LLM.encode(..., pooling_task="token_embed")`
- Online APIs:
  
  - Pooling API (`/pooling`)

The difference between the (sequence) embedding task and the token embedding task is that (sequence) embedding outputs one embedding for each sequence, while token embedding outputs an embedding for each token.

Many embedding models support both (sequence) embedding and token embedding. For further details on (sequence) embedding, please refer to [this page](https://docs.vllm.ai/en/latest/models/pooling_models/embed/).

Note

Pooling multitask support is deprecated and will be removed in v0.20. When the default pooling task (embed) is not what you want, you need to manually specify it via `PoolerConfig(task="token_embed")` offline or `--pooler-config.task token_embed` online.

## Typical Use Cases[¶](#typical-use-cases "Permanent link")

### Multi-Vector Retrieval[¶](#multi-vector-retrieval "Permanent link")

For implementation examples, see:

Offline: [examples/pooling/token\_embed/multi\_vector\_retrieval\_offline.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/token_embed/multi_vector_retrieval_offline.py)

Online: [examples/pooling/token\_embed/multi\_vector\_retrieval\_online.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/token_embed/multi_vector_retrieval_online.py)

### Late interaction[¶](#late-interaction "Permanent link")

Similarity scores can be computed using late interaction between two input prompts via the score API. For more information, see [Score API](https://docs.vllm.ai/en/latest/models/pooling_models/scoring/).

Models of any architecture can be converted into embedding models using `--convert embed`. Token embedding can then be used to extract the last hidden states from these models.

## Supported Models[¶](#supported-models "Permanent link")

### Text-only Models[¶](#text-only-models "Permanent link")

Architecture Models Example HF Models [LoRA](https://docs.vllm.ai/en/latest/features/lora/) [PP](https://docs.vllm.ai/en/latest/serving/parallelism_scaling/) [`ColBERTLfm2Model`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/colbert/#vllm.model_executor.models.colbert.ColBERTLfm2Model "            ColBERTLfm2Model") LFM2 `LiquidAI/LFM2-ColBERT-350M` [`ColBERTModernBertModel`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/colbert/#vllm.model_executor.models.colbert.ColBERTModernBertModel "            ColBERTModernBertModel") ModernBERT `lightonai/GTE-ModernColBERT-v1` [`ColBERTJinaRobertaModel`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/colbert/#vllm.model_executor.models.colbert.ColBERTJinaRobertaModel "            ColBERTJinaRobertaModel") Jina XLM-RoBERTa `jinaai/jina-colbert-v2` `HF_ColBERT` BERT `answerdotai/answerai-colbert-small-v1`, `colbert-ir/colbertv2.0` `*Model`C, `*ForCausalLM`C, etc. Generative models N/A * *

### Multimodal Models[¶](#multimodal-models "Permanent link")

Note

For more information about multimodal models inputs, see [this page](https://docs.vllm.ai/en/latest/models/supported_models/#list-of-multimodal-language-models).

Architecture Models Inputs Example HF Models [LoRA](https://docs.vllm.ai/en/latest/features/lora/) [PP](https://docs.vllm.ai/en/latest/serving/parallelism_scaling/) [`ColModernVBertForRetrieval`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/colmodernvbert/#vllm.model_executor.models.colmodernvbert.ColModernVBertForRetrieval "            ColModernVBertForRetrieval") ColModernVBERT T / I `ModernVBERT/colmodernvbert-merged` `ColPaliForRetrieval` ColPali T / I `vidore/colpali-v1.3-hf` `ColQwen3` Qwen3-VL T / I `TomoroAI/tomoro-colqwen3-embed-4b`, `TomoroAI/tomoro-colqwen3-embed-8b` `ColQwen3_5` ColQwen3.5 T + I + V `athrael-soju/colqwen3.5-4.5B-v3` `OpsColQwen3Model` Qwen3-VL T / I `OpenSearch-AI/Ops-Colqwen3-4B`, `OpenSearch-AI/Ops-Colqwen3-8B` `Qwen3VLNemotronEmbedModel` Qwen3-VL T / I `nvidia/nemotron-colembed-vl-4b-v2`, `nvidia/nemotron-colembed-vl-8b-v2` ✅︎ ✅︎ `*ForConditionalGeneration`C, `*ForCausalLM`C, etc. Generative models * N/A * *

C Automatically converted into an embedding model via `--convert embed`. ([details](https://docs.vllm.ai/en/latest/models/pooling_models/#model-conversion))  
\* Feature support is the same as that of the original model.

If your model is not in the above list, we will try to automatically convert the model using [as\_embedding\_model](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/adapters/#vllm.model_executor.models.adapters.as_embedding_model "            as_embedding_model").

### Special models[¶](#special-models "Permanent link")

Architecture Models Example HF Models [LoRA](https://docs.vllm.ai/en/latest/features/lora/) [PP](https://docs.vllm.ai/en/latest/serving/parallelism_scaling/) `JinaForRanking` Qwen3-based `jinaai/jina-reranker-v3`

jina-reranker-v3 is a listwise document reranker model with a novel `last but not late interaction` architecture. More information can be found at: [examples/pooling/token\_embed/jina\_reranker\_v3\_offline.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/token_embed/jina_reranker_v3_offline.py)

## Offline Inference[¶](#offline-inference "Permanent link")

### Pooling Parameters[¶](#pooling-parameters "Permanent link")

The following [pooling parameters](https://docs.vllm.ai/en/latest/api/vllm/#vllm.PoolingParams "            PoolingParams") are supported.

```
    use_activation: bool | None = None
    dimensions: int | None = None
```

### `LLM.encode`[¶](#llmencode "Permanent link")

The [encode](https://docs.vllm.ai/en/latest/api/vllm/#vllm.LLM.encode "            encode") method is available to all pooling models in vLLM.

Set `pooling_task="token_embed"` when using `LLM.encode` for token embedding Models:

```
fromvllmimport LLM

llm = LLM(model="answerdotai/answerai-colbert-small-v1", runner="pooling")
(output,) = llm.encode("Hello, my name is", pooling_task="token_embed")

data = output.outputs.data
print(f"Data: {data!r}")
```

### `LLM.score`[¶](#llmscore "Permanent link")

The [score](https://docs.vllm.ai/en/latest/api/vllm/#vllm.LLM.score "            score") method outputs similarity scores between sentence pairs.

All models that support token embedding task also support using the score API to compute similarity scores by calculating the late interaction of two input prompts.

```
fromvllmimport LLM

llm = LLM(model="answerdotai/answerai-colbert-small-v1", runner="pooling")
(output,) = llm.score(
    "What is the capital of France?",
    "The capital of Brazil is Brasilia.",
)

score = output.outputs.score
print(f"Score: {score}")
```

## Online Serving[¶](#online-serving "Permanent link")

Please refer to the [pooling API](https://docs.vllm.ai/en/latest/models/pooling_models/#pooling-api) and use `"task":"token_embed"`.

## More examples[¶](#more-examples "Permanent link")

More examples can be found here: [examples/pooling/token\_embed](https://github.com/vllm-project/vllm/tree/main/examples/pooling/token_embed)

## Supported Features[¶](#supported-features "Permanent link")

Token embedding features should be consistent with (sequence) embedding. For more information, see [this page](https://docs.vllm.ai/en/latest/models/pooling_models/embed/#supported-features).