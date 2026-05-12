---
title: Pooling Models - vLLM
url: https://docs.vllm.ai/en/latest/models/pooling_models/
source: sitemap
fetched_at: 2026-05-07T21:15:00.066881534-03:00
rendered_js: false
word_count: 1652
summary: This document provides an overview of pooling models in vLLM, explaining the different task granularities, pooling strategies, and scoring types supported for classification and embedding tasks.
tags:
    - vllm
    - pooling-models
    - nlp
    - embeddings
    - classification
    - transformers
    - model-inference
category: concept
---

[](https://github.com/vllm-project/vllm/edit/main/docs/models/pooling_models/README.md "Edit this page")

Note

We currently support pooling models primarily for convenience. This is not guaranteed to provide any performance

improvements over using Hugging Face Transformers or Sentence Transformers directly.

```
We plan to optimize pooling models in vLLM. Please comment on [:octicons-mark-github-16: Issue #21796](https://github.com/vllm-project/vllm/issues/21796) if you have any suggestions!
```

## What are pooling models?[¶](#what-are-pooling-models "Permanent link")

Natural Language Processing (NLP) can be primarily divided into the following two types of tasks:

- Natural Language Understanding (NLU)
- Natural Language Generation (NLG)

The generative models supported by vLLM cover a variety of task types, such as the large language models (LLMs) we are familiar with, multimodal models (VLM) that handle multimodal inputs like images, videos, and audio, speech-to-text transcription models, and real-time models that support streaming input. Their common feature is the ability to generate text. Taking it a step further, vLLM-Omni supports the generation of multimodal content, including images, videos, and audio.

As the capabilities of generative models continue to improve, the boundaries of these models are also constantly expanding. However, certain application scenarios still require specialized small language models to efficiently complete specific tasks. These models typically have the following characteristics:

- They do not require content generation.
- They only need to perform very limited functions, without requiring strong generalization, creativity, or high intelligence.
- They demand extremely low latency and may operate on cost-constrained hardware.
- Text-only models typically have fewer than 1 billion parameters, while multimodal models generally have fewer than 10 billion parameters.

Although these models are relatively small in scale, they are still based on the Transformer architecture, similar or even identical to the most advanced large language models today. Many recently released pooling models are also fine-tuned from large language models, allowing them to benefit from the continuous improvements in large models. This architecture similarity enables them to reuse much of vLLM’s infrastructure. If compatible, we would be happy to help them leverage the latest features of vLLM as well.

### Sequence-wise Task and Token-wise Task[¶](#sequence-wise-task-and-token-wise-task "Permanent link")

The key distinction between sequence-wise task and token-wise task lies in their output granularity: sequence-wise task produces a single result for an entire input sequence, whereas token-wise task yields a result for each individual token within the sequence.

Many Pooling models support both (sequence) task and token task. When the default pooling task (e.g. a sequence-wise task) is not what you want, you need to manually specify (e.g. a token-wise task) via `PoolerConfig(task=<task>)` offline or `--pooler-config.task <task>` online.

Of course, we also have "plugin" tasks that allow users to customize input and output processors. For more information, please refer to [IO Processor Plugins](https://docs.vllm.ai/en/latest/design/io_processor_plugins/).

### Pooling Tasks[¶](#pooling-tasks "Permanent link")

Pooling Tasks Granularity Outputs `classify` (see note) Sequence-wise probability vector of classes for each sequence `embed` Sequence-wise vector representations for each sequence `token_classify` Token-wise probability vector of classes for each token `token_embed` Token-wise vector representations for each token

Note

Within classification tasks, there is a specialized subcategory: Cross-encoder (aka reranker) models. These models

are a subset of classification models that accept two prompts as input and output num\_labels equal to 1.

### Pooling Types[¶](#pooling-types "Permanent link")

Pooling Tasks Granularity Description `CLS` pooling Sequence-wise For BERT‑like (bidirectional self‑attention) models, CLS pooling is used by default. This means the last\_hidden\_states corresponding to the first token (the \[CLS] token) is taken as the output. `LAST` pooling Sequence-wise For GPT‑like (causal self‑attention) models, LAST pooling is used by default. This means the last\_hidden\_states corresponding to the last token is taken as the output. `MEAN` pooling Sequence-wise Many studies have shown that averaging the last\_hidden\_states over all input tokens performs better on certain downstream tasks. Therefore, more and more models are using MEAN pooling. `ALL` pooling Token-wise Outputs the last\_hidden\_states for all input tokens. `STEP` pooling Token-wise Filters and outputs the last\_hidden\_states corresponding to the token IDs returned by returned\_token\_ids.

### Score Types[¶](#score-types "Permanent link")

The scoring models is designed to compute similarity scores between two input prompts. It supports three model types (aka `score_type`): `cross-encoder`, `late-interaction`, and `bi-encoder`.

Pooling Tasks Granularity Outputs Score Types scoring function `classify` (see note) Sequence-wise reranker score for each sequence `cross-encoder` linear classifier `embed` Sequence-wise vector representations for each sequence `bi-encoder` cosine similarity `token_classify` Token-wise probability vector of classes for each token N/A N/A `token_embed` Token-wise vector representations for each token `late-interaction` late interaction(MaxSim)

Note

Only when a classification model outputs num\_labels equal to 1 can it be used as a scoring model and have its scoring API enabled.

### Pooling Usages[¶](#pooling-usages "Permanent link")

Pooling Usages Description Classification Usages Predicting which predefined category, class, or label best corresponds to a given input. Embedding Usages Converts unstructured data (text, images, audio, etc.) into structured numerical vectors (embeddings). Token Classification Usages Token-wise classification Token Embedding Usages Token-wise embedding Reward Usages Evaluates the quality of outputs generated by a language model, acting as a proxy for human preferences. Scoring Usages Computes similarity scores between two inputs. It supports three model types (aka `score_type`): `cross-encoder`, `late-interaction`, and `bi-encoder`. Plugins Usages Allow users to customize input and output processors. For more information, please refer to [IO Processor Plugins](https://docs.vllm.ai/en/latest/design/io_processor_plugins/).

We also have some special models that support multiple pooling tasks, or have specific usage scenarios, or support special inputs and outputs.

For more detailed information, please refer to the link below.

- [Classification Usages](https://docs.vllm.ai/en/latest/models/pooling_models/classify/)
- [Embedding Usages](https://docs.vllm.ai/en/latest/models/pooling_models/embed/)
- [Token Classification Usages](https://docs.vllm.ai/en/latest/models/pooling_models/token_classify/)
- [Token Embedding Usages](https://docs.vllm.ai/en/latest/models/pooling_models/token_embed/)
- [Reward Usages](https://docs.vllm.ai/en/latest/models/pooling_models/reward/)
- [Scoring Usages](https://docs.vllm.ai/en/latest/models/pooling_models/scoring/)
- [Specific Model Examples](https://docs.vllm.ai/en/latest/models/pooling_models/specific_models/)

## Offline Inference[¶](#offline-inference "Permanent link")

Each pooling model in vLLM supports one or more of these tasks according to [Pooler.get\_supported\_tasks](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/pooler/#vllm.model_executor.layers.pooler.Pooler.get_supported_tasks "            get_supported_tasks            abstractmethod   "), enabling the corresponding APIs.

### Offline APIs corresponding to pooling usages[¶](#offline-apis-corresponding-to-pooling-usages "Permanent link")

Pooling Usages Dedicated API Pooling task for `LLM.encode` API Score Types scoring function Classification Usages `LLM.classify(...)` `classify` `cross-encoder` (see note) linear classifier Embedding Usages `LLM.embed(...)` `embed` `bi-encoder` cosine similarity Token Classification Usages N/A `token_classify` N/A N/A Token Embedding Usages N/A `token_embed` `late-interaction` late interaction(MaxSim) Reward Usages N/A `classify` & `token_classify` N/A N/A Scoring Usages `LLM.score(...)` N/A N/A N/A Plugins Usages N/A `plugin` N/A N/A

Note

Only when a classification model outputs num\_labels equal to 1 can it be used as a scoring model and have its scoring API enabled.

### `LLM.classify`[¶](#llmclassify "Permanent link")

The [classify](https://docs.vllm.ai/en/latest/api/vllm/#vllm.LLM.classify "            classify") method outputs a probability vector for each prompt. It is primarily designed for [classification models](https://docs.vllm.ai/en/latest/models/pooling_models/classify/). For more information about `LLM.embed`, see [this page](https://docs.vllm.ai/en/latest/models/pooling_models/classify/#offline-inference).

### `LLM.embed`[¶](#llmembed "Permanent link")

The [embed](https://docs.vllm.ai/en/latest/api/vllm/#vllm.LLM.embed "            embed") method outputs an embedding vector for each prompt. It is primarily designed for [embedding models](https://docs.vllm.ai/en/latest/models/pooling_models/embed/). For more information about `LLM.embed`, see [this page](https://docs.vllm.ai/en/latest/models/pooling_models/embed/#offline-inference).

### `LLM.score`[¶](#llmscore "Permanent link")

The [score](https://docs.vllm.ai/en/latest/api/vllm/#vllm.LLM.score "            score") method outputs similarity scores between sentence pairs. It is primarily designed for [score models](https://docs.vllm.ai/en/latest/models/pooling_models/scoring/).

### `LLM.encode`[¶](#llmencode "Permanent link")

The [encode](https://docs.vllm.ai/en/latest/api/vllm/#vllm.LLM.encode "            encode") method is available to all pooling models in vLLM.

Please use one of the more specific methods or set the task directly when using `LLM.encode`, refer to the [table above](#offline-apis-corresponding-to-pooling-usages).

### Examples[¶](#examples "Permanent link")

```
fromvllmimport LLM

llm = LLM(model="intfloat/e5-small", runner="pooling")
(output,) = llm.encode("Hello, my name is", pooling_task="embed")

data = output.outputs.data
print(f"Data: {data!r}")
```

## Online Serving[¶](#online-serving "Permanent link")

Our online Server provides endpoints that correspond to the offline APIs:

- Corresponding to `LLM.embed`:
  
  - [Cohere Embed API](https://docs.vllm.ai/en/latest/models/pooling_models/embed/#cohere-embed-api) (`/v2/embed`)
  - [Openai-compatible Embeddings API](https://docs.vllm.ai/en/latest/models/pooling_models/embed/#openai-compatible-embeddings-api) (`/v1/embeddings`)
- Corresponding to `LLM.classify`:
  
  - [Classification API](https://docs.vllm.ai/en/latest/models/pooling_models/classify/#online-serving)(`/classify`)
- Corresponding to `LLM.score`:
  
  - [Score API](https://docs.vllm.ai/en/latest/models/pooling_models/scoring/#score-api)(`/score`)
  - [Rerank API](https://docs.vllm.ai/en/latest/models/pooling_models/scoring/#rerank-api) (`/rerank`, `/v1/rerank`, `/v2/rerank`)
- Pooling API (`/pooling`) is similar to `LLM.encode`, being applicable to all types of pooling models.

The following introduces the Pooling API. For other APIs, please refer to the link above.

### Pooling API[¶](#pooling-api "Permanent link")

Our Pooling API (`/pooling`) is similar to `LLM.encode`, being applicable to all types of pooling models.

The input format is the same as [Embeddings API](https://docs.vllm.ai/en/latest/models/pooling_models/embed/#openai-compatible-embeddings-api), but the output data can contain an arbitrary nested list, not just a 1-D list of floats.

Please use one of the more specific APIs or set the task directly when using the Pooling API, refer to the [table above](#offline-apis-corresponding-to-pooling-usages).

Code examples:

- [Online example](https://github.com/vllm-project/vllm/blob/main/examples/pooling/reward/token_reward_online.py)
- [Offline example](https://github.com/vllm-project/vllm/blob/main/examples/pooling/reward/token_reward_offline.py)

### Examples[¶](#examples_1 "Permanent link")

```
# start a supported embeddings model server with `vllm serve`, e.g.
# vllm serve intfloat/e5-small
importrequests

host = "localhost"
port = "8000"
model_name = "intfloat/e5-small"

api_url = f"http://{host}:{port}/pooling"

prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]
prompt = {"model": model_name, "input": prompts, "task": "embed"}

response = requests.post(api_url, json=prompt)

for output in response.json()["data"]:
    data = output["data"]
    print(f"Data: {data!r} (size={len(data)})")
```

## Configuration[¶](#configuration "Permanent link")

In vLLM, pooling models implement the [VllmModelForPooling](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/#vllm.model_executor.models.VllmModelForPooling "            VllmModelForPooling") interface. These models use a [Pooler](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/pooler/#vllm.model_executor.layers.pooler.Pooler "            Pooler") to extract the final hidden states of the input before returning them.

### Model Runner[¶](#model-runner "Permanent link")

Run a model in pooling mode via the option `--runner pooling`.

Tip

There is no need to set this option in the vast majority of cases as vLLM can automatically detect the appropriate model runner via `--runner auto`.

### Model Conversion[¶](#model-conversion "Permanent link")

vLLM can adapt models for various pooling tasks via the option `--convert <type>`.

If `--runner pooling` has been set (manually or automatically) but the model does not implement the [VllmModelForPooling](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/#vllm.model_executor.models.VllmModelForPooling "            VllmModelForPooling") interface, vLLM will attempt to automatically convert the model according to the architecture names shown in the table below.

Architecture `--convert` Supported pooling tasks `*ForTextEncoding`, `*EmbeddingModel`, `*Model` `embed` `token_embed`, `embed` `*ForRewardModeling`, `*RewardModel` `embed` `token_embed`, `embed` `*For*Classification`, `*ClassificationModel` `classify` `token_classify`, `classify`

Tip

You can explicitly set `--convert <type>` to specify how to convert the model.

### Pooler Configuration[¶](#pooler-configuration "Permanent link")

#### Predefined models[¶](#predefined-models "Permanent link")

If the [Pooler](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/pooler/#vllm.model_executor.layers.pooler.Pooler "            Pooler") defined by the model accepts `pooler_config`, you can override some of its attributes via the `--pooler-config` option.

#### Converted models[¶](#converted-models "Permanent link")

If the model has been converted via `--convert` (see above), the pooler assigned to each task has the following attributes by default:

Task Pooling Type Normalization Softmax `embed` `LAST` ✅︎ ❌ `classify` `LAST` ❌ ✅︎

When loading [Sentence Transformers](https://huggingface.co/sentence-transformers) models, its Sentence Transformers configuration file (`modules.json`) takes priority over the model's defaults.

You can further customize this via the `--pooler-config` option, which takes priority over both the model's and Sentence Transformers' defaults.

## Removed Features[¶](#removed-features "Permanent link")

### Encode task[¶](#encode-task "Permanent link")

We have split the `encode` task into two more specific token-wise tasks: `token_embed` and `token_classify`:

- `token_embed` is the same as `embed`, using normalization as the activation.
- `token_classify` is the same as `classify`, by default using softmax as the activation.

Pooling models now support token-wise task.

- Extracting hidden states prefers using `token_embed` task.
- Named Entity Recognition (NER) and reward models prefers using `token_classify` task.

### Score task[¶](#score-task "Permanent link")

`score` task have has been removed in v0.21, use `classify` instead. Only when a classification model outputs num\_labels equal to 1 can it be used as a scoring model and have its scoring API enabled.

### Pooling multitask support[¶](#pooling-multitask-support "Permanent link")

Pooling multitask support has been removed in v0.21. When the default pooling task is not what you want, you need to manually specify it via `PoolerConfig(task=<task>)` offline or `--pooler-config.task <task>` online.