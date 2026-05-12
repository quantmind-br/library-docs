---
title: Token Classification Usages - vLLM
url: https://docs.vllm.ai/en/latest/models/pooling_models/token_classify/
source: sitemap
fetched_at: 2026-05-07T21:15:05.819859642-03:00
rendered_js: false
word_count: 429
summary: This document explains how to perform token-level classification in vLLM by utilizing the token_classify pooling task for both offline inference and online serving.
tags:
    - token-classification
    - pooling-models
    - vllm
    - offline-inference
    - online-serving
    - machine-learning
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/models/pooling_models/token_classify.md "Edit this page")

## Summary[¶](#summary "Permanent link")

- Model Usage: token classification
- Pooling Tasks: `token_classify`
- Offline APIs:
  
  - `LLM.encode(..., pooling_task="token_classify")`
- Online APIs:
  
  - Pooling API (`/pooling`)

The key distinction between (sequence) classification and token classification lies in their output granularity: (sequence) classification produces a single result for an entire input sequence, whereas token classification yields a result for each individual token within the sequence.

Many classification models support both (sequence) classification and token classification. For further details on (sequence) classification, please refer to [this page](https://docs.vllm.ai/en/latest/models/pooling_models/classify/).

Note

Pooling multitask support is deprecated and will be removed in v0.20. When the default pooling task (classify) is not what you want, you need to manually specify it via `PoolerConfig(task="token_classify")` offline or `--pooler-config.task token_classify` online.

## Typical Use Cases[¶](#typical-use-cases "Permanent link")

### Named Entity Recognition (NER)[¶](#named-entity-recognition-ner "Permanent link")

For implementation examples, see:

Offline: [examples/pooling/token\_classify/ner\_offline.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/token_classify/ner_offline.py)

Online: [examples/pooling/token\_classify/ner\_online.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/token_classify/ner_online.py)

### Forced Alignment[¶](#forced-alignment "Permanent link")

Forced alignment takes audio and reference text as input and produces word-level timestamps.

Offline: [examples/pooling/token\_classify/forced\_alignment\_offline.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/token_classify/forced_alignment_offline.py)

### Sparse retrieval (lexical matching)[¶](#sparse-retrieval-lexical-matching "Permanent link")

The BAAI/bge-m3 model leverages token classification for sparse retrieval. For more information, see [this page](https://docs.vllm.ai/en/latest/models/pooling_models/specific_models/#baaibge-m3).

## Supported Models[¶](#supported-models "Permanent link")

Architecture Models Example HF Models [LoRA](https://docs.vllm.ai/en/latest/features/lora/) [PP](https://docs.vllm.ai/en/latest/serving/parallelism_scaling/) `BertForTokenClassification` bert-based `boltuix/NeuroBERT-NER` (see note), etc. `ErnieForTokenClassification` BERT-like Chinese ERNIE `gyr66/Ernie-3.0-base-chinese-finetuned-ner` `ModernBertForTokenClassification` ModernBERT-based `disham993/electrical-ner-ModernBERT-base` `Qwen3ForTokenClassification`C Qwen3-based `bd2lcco/Qwen3-0.6B-finetuned` `*Model`C, `*ForCausalLM`C, etc. Generative models N/A * *

C Automatically converted into a classification model via `--convert classify`. ([details](https://docs.vllm.ai/en/latest/models/pooling_models/#model-conversion)) * Feature support is the same as that of the original model.

If your model is not in the above list, we will try to automatically convert the model using [as\_seq\_cls\_model](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/adapters/#vllm.model_executor.models.adapters.as_seq_cls_model "            as_seq_cls_model"). By default, the class probabilities are extracted from the softmaxed hidden state corresponding to the last token.

### Multimodal Models[¶](#multimodal-models "Permanent link")

Note

For more information about multimodal models inputs, see [this page](https://docs.vllm.ai/en/latest/models/supported_models/#list-of-multimodal-language-models).

Architecture Models Inputs Example HF Models [LoRA](https://docs.vllm.ai/en/latest/features/lora/) [PP](https://docs.vllm.ai/en/latest/serving/parallelism_scaling/) [`Qwen3ASRForcedAlignerForTokenClassification`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/qwen3_asr_forced_aligner/#vllm.model_executor.models.qwen3_asr_forced_aligner.Qwen3ASRForcedAlignerForTokenClassification "            Qwen3ASRForcedAlignerForTokenClassification") Qwen3-ForcedAligner T + A+ `Qwen/Qwen3-ForcedAligner-0.6B` (see note) ✅︎

### Reward Models[¶](#reward-models "Permanent link")

Using token classification models as reward models. For details on reward models, see [Reward Models](https://docs.vllm.ai/en/latest/models/pooling_models/reward/).

Architecture Models Example HF Models [LoRA](https://docs.vllm.ai/en/latest/features/lora/) [PP](https://docs.vllm.ai/en/latest/serving/parallelism_scaling/) `InternLM2ForRewardModel` InternLM2-based `internlm/internlm2-1_8b-reward`, `internlm/internlm2-7b-reward`, etc. ✅︎ ✅︎ `Qwen2ForRewardModel` Qwen2-based `Qwen/Qwen2.5-Math-RM-72B`, etc. ✅︎ ✅︎ `*Model`C, `*ForCausalLM`C, etc. Generative models N/A * *

C Automatically converted into a classification model via `--convert classify`. ([details](https://docs.vllm.ai/en/latest/models/pooling_models/#model-conversion))

If your model is not in the above list, we will try to automatically convert the model using [as\_seq\_cls\_model](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/adapters/#vllm.model_executor.models.adapters.as_seq_cls_model "            as_seq_cls_model").

## Offline Inference[¶](#offline-inference "Permanent link")

### Pooling Parameters[¶](#pooling-parameters "Permanent link")

The following [pooling parameters](https://docs.vllm.ai/en/latest/api/vllm/#vllm.PoolingParams "            PoolingParams") are supported.

```
    use_activation: bool | None = None
```

### `LLM.encode`[¶](#llmencode "Permanent link")

The [encode](https://docs.vllm.ai/en/latest/api/vllm/#vllm.LLM.encode "            encode") method is available to all pooling models in vLLM.

Set `pooling_task="token_classify"` when using `LLM.encode` for token classification Models:

```
fromvllmimport LLM

llm = LLM(model="boltuix/NeuroBERT-NER", runner="pooling")
(output,) = llm.encode("Hello, my name is", pooling_task="token_classify")

data = output.outputs.data
print(f"Data: {data!r}")
```

## Online Serving[¶](#online-serving "Permanent link")

Please refer to the [pooling API](https://docs.vllm.ai/en/latest/models/pooling_models/#pooling-api) and use `"task":"token_classify"`.

## More examples[¶](#more-examples "Permanent link")

More examples can be found here: [examples/pooling/token\_classify](https://github.com/vllm-project/vllm/tree/main/examples/pooling/token_classify)

## Supported Features[¶](#supported-features "Permanent link")

Token classification features should be consistent with (sequence) classification. For more information, see [this page](https://docs.vllm.ai/en/latest/models/pooling_models/classify/#supported-features).