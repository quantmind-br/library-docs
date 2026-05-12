---
title: Classification Usages - vLLM
url: https://docs.vllm.ai/en/latest/models/pooling_models/classify/
source: sitemap
fetched_at: 2026-05-07T21:15:00.972899236-03:00
rendered_js: false
word_count: 988
summary: This document describes the sequence classification capabilities in vLLM, including supported model architectures, API usage, and the distinction between standard classification and cross-encoder reranker models.
tags:
    - vllm
    - sequence-classification
    - cross-encoder
    - reranker
    - multimodal-models
    - machine-learning
category: reference
---

[](https://github.com/vllm-project/vllm/edit/main/docs/models/pooling_models/classify.md "Edit this page")

Classification involves predicting which predefined category, class, or label best corresponds to a given input.

## Summary[¶](#summary "Permanent link")

- Model Usage: (sequence) classification
- Pooling Task: `classify`
- Offline APIs:
  
  - `LLM.classify(...)`
  - `LLM.encode(..., pooling_task="classify")`
- Online APIs:
  
  - [Classification API](https://docs.vllm.ai/en/latest/models/pooling_models/classify/#online-serving) (`/classify`)
  - Pooling API (`/pooling`)

The key distinction between (sequence) classification and token classification lies in their output granularity: (sequence) classification produces a single result for an entire input sequence, whereas token classification yields a result for each individual token within the sequence.

Many classification models support both (sequence) classification and token classification. For further details on token classification, please refer to [this page](https://docs.vllm.ai/en/latest/models/pooling_models/token_classify/).

Only when a classification model outputs num\_labels equal to 1 can it be used as a scoring model and have its scoring API enabled, please refer to [this page](https://docs.vllm.ai/en/latest/models/pooling_models/scoring/).

## Typical Use Cases[¶](#typical-use-cases "Permanent link")

### Classification[¶](#classification "Permanent link")

The most fundamental application of classification models is to categorize input data into predefined classes.

## Supported Models[¶](#supported-models "Permanent link")

### Text-only Models[¶](#text-only-models "Permanent link")

Architecture Models Example HF Models [LoRA](https://docs.vllm.ai/en/latest/features/lora/) [PP](https://docs.vllm.ai/en/latest/serving/parallelism_scaling/) `ErnieForSequenceClassification` BERT-like Chinese ERNIE `Forrest20231206/ernie-3.0-base-zh-cls` [`GPT2ForSequenceClassification`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/gpt2/#vllm.model_executor.models.gpt2.GPT2ForSequenceClassification "            GPT2ForSequenceClassification") GPT2 `nie3e/sentiment-polish-gpt2-small` `Qwen2ForSequenceClassification`C Qwen2-based `jason9693/Qwen2.5-1.5B-apeach` `*Model`C, `*ForCausalLM`C, etc. Generative models N/A * *

### Multimodal Models[¶](#multimodal-models "Permanent link")

Note

For more information about multimodal models inputs, see [this page](https://docs.vllm.ai/en/latest/models/supported_models/#list-of-multimodal-language-models).

Architecture Models Inputs Example HF Models [LoRA](https://docs.vllm.ai/en/latest/features/lora/) [PP](https://docs.vllm.ai/en/latest/serving/parallelism_scaling/) `Qwen2_5_VLForSequenceClassification`C Qwen2\_5\_VL-based T + IE+ + VE+ `muziyongshixin/Qwen2.5-VL-7B-for-VideoCls` `*ForConditionalGeneration`C, `*ForCausalLM`C, etc. Generative models * N/A * *

C Automatically converted into a classification model via `--convert classify`. ([details](https://docs.vllm.ai/en/latest/models/pooling_models/#model-conversion))  
\* Feature support is the same as that of the original model.

If your model is not in the above list, we will try to automatically convert the model using [as\_seq\_cls\_model](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/adapters/#vllm.model_executor.models.adapters.as_seq_cls_model "            as_seq_cls_model"). By default, the class probabilities are extracted from the softmaxed hidden state corresponding to the last token.

### Cross-encoder Models[¶](#cross-encoder-models "Permanent link")

Cross-encoder (aka reranker) models are a subset of classification models that accept two prompts as input and output num\_labels equal to 1. Most classification models can also be used as [cross-encoder models](https://docs.vllm.ai/en/latest/models/pooling_models/scoring/#cross-encoder-models). For more information on cross-encoder models, please refer to [this page](https://docs.vllm.ai/en/latest/models/pooling_models/scoring/).

#### Text-only Models[¶](#text-only-models_1 "Permanent link")

Architecture Models Example HF Models Score template (see note) [LoRA](https://docs.vllm.ai/en/latest/features/lora/) [PP](https://docs.vllm.ai/en/latest/serving/parallelism_scaling/) `BertForSequenceClassification` BERT-based `cross-encoder/ms-marco-MiniLM-L-6-v2`, etc. N/A `GemmaForSequenceClassification` Gemma-based `BAAI/bge-reranker-v2-gemma`(see note), etc. [bge-reranker-v2-gemma.jinja](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/template/bge-reranker-v2-gemma.jinja) ✅︎ ✅︎ `GteNewForSequenceClassification` mGTE-TRM (see note) `Alibaba-NLP/gte-multilingual-reranker-base`, etc. N/A `LlamaBidirectionalForSequenceClassification`C Llama-based with bidirectional attention `nvidia/llama-nemotron-rerank-1b-v2`, etc. [nemotron-rerank.jinja](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/template/nemotron-rerank.jinja) ✅︎ ✅︎ `ModernBertForSequenceClassification` ModernBERT-based `Alibaba-NLP/gte-reranker-modernbert-base`, etc. N/A `Qwen2ForSequenceClassification`C Qwen2-based `mixedbread-ai/mxbai-rerank-base-v2`(see note), etc. [mxbai\_rerank\_v2.jinja](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/template/mxbai_rerank_v2.jinja) ✅︎ ✅︎ `Qwen3ForSequenceClassification`C Qwen3-based `tomaarsen/Qwen3-Reranker-0.6B-seq-cls`, `Qwen/Qwen3-Reranker-0.6B`(see note), etc. [qwen3\_reranker.jinja](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/template/qwen3_reranker.jinja) ✅︎ ✅︎ `RobertaForSequenceClassification` RoBERTa-based `cross-encoder/quora-roberta-base`, etc. N/A `XLMRobertaForSequenceClassification` XLM-RoBERTa-based `BAAI/bge-reranker-v2-m3`, etc. N/A `*Model`C, `*ForCausalLM`C, etc. Generative models N/A N/A * *

C Automatically converted into a classification model via `--convert classify`. ([details](https://docs.vllm.ai/en/latest/models/pooling_models/#model-conversion))  
\* Feature support is the same as that of the original model.

Note

Load the official original `BAAI/bge-reranker-v2-gemma` by using the following command.

```
vllmserveBAAI/bge-reranker-v2-gemma--hf_overrides'{"architectures": ["GemmaForSequenceClassification"],"classifier_from_token": ["Yes"],"method": "no_post_processing"}'
```

Note

The second-generation GTE model (mGTE-TRM) is named `NewForSequenceClassification`. The name `NewForSequenceClassification` is too generic, you should set `--hf-overrides '{"architectures": ["GteNewForSequenceClassification"]}'` to specify the use of the `GteNewForSequenceClassification` architecture.

Note

Load the official original `mxbai-rerank-v2` by using the following command.

```
vllmservemixedbread-ai/mxbai-rerank-base-v2--hf_overrides'{"architectures": ["Qwen2ForSequenceClassification"],"classifier_from_token": ["0", "1"], "method": "from_2_way_softmax"}'
```

#### Multimodal Models[¶](#multimodal-models_1 "Permanent link")

Note

For more information about multimodal models inputs, see [this page](https://docs.vllm.ai/en/latest/models/supported_models/#list-of-multimodal-language-models).

Architecture Models Inputs Example HF Models [LoRA](https://docs.vllm.ai/en/latest/features/lora/) [PP](https://docs.vllm.ai/en/latest/serving/parallelism_scaling/) `JinaVLForSequenceClassification` JinaVL-based T + IE+ `jinaai/jina-reranker-m0`, etc. ✅︎ ✅︎ `LlamaNemotronVLForSequenceClassification` Llama Nemotron Reranker + SigLIP T + IE+ `nvidia/llama-nemotron-rerank-vl-1b-v2` `Qwen3VLForSequenceClassification` Qwen3-VL-Reranker T + IE+ + VE+ `Qwen/Qwen3-VL-Reranker-2B`(see note), etc. ✅︎ ✅︎

C Automatically converted into a classification model via `--convert classify`. ([details](https://docs.vllm.ai/en/latest/models/pooling_models/#model-conversion))  
\* Feature support is the same as that of the original model.

Note

Similar to Qwen3-Reranker, you need to use the following `--hf_overrides` to load the official original `Qwen3-VL-Reranker`.

```
vllmserveQwen/Qwen3-VL-Reranker-2B--hf_overrides'{"architectures": ["Qwen3VLForSequenceClassification"],"classifier_from_token": ["no", "yes"],"is_original_qwen3_reranker": true}'
```

### Reward Models[¶](#reward-models "Permanent link")

Using (sequence) classification models as reward models. For more information, see [Reward Models](https://docs.vllm.ai/en/latest/models/pooling_models/reward/).

Architecture Models Example HF Models [LoRA](https://docs.vllm.ai/en/latest/features/lora/) [PP](https://docs.vllm.ai/en/latest/serving/parallelism_scaling/) `JambaForSequenceClassification` Jamba `ai21labs/Jamba-tiny-reward-dev`, etc. ✅︎ ✅︎ `Qwen3ForSequenceClassification`C Qwen3-based `Skywork/Skywork-Reward-V2-Qwen3-0.6B`, etc. ✅︎ ✅︎ `LlamaForSequenceClassification`C Llama-based `Skywork/Skywork-Reward-V2-Llama-3.2-1B`, etc. ✅︎ ✅︎ `*Model`C, `*ForCausalLM`C, etc. Generative models N/A * *

C Automatically converted into a classification model via `--convert classify`. ([details](https://docs.vllm.ai/en/latest/models/pooling_models/#model-conversion))

If your model is not in the above list, we will try to automatically convert the model using [as\_seq\_cls\_model](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/adapters/#vllm.model_executor.models.adapters.as_seq_cls_model "            as_seq_cls_model"). By default, the class probabilities are extracted from the softmaxed hidden state corresponding to the last token.

## Offline Inference[¶](#offline-inference "Permanent link")

### Pooling Parameters[¶](#pooling-parameters "Permanent link")

The following [pooling parameters](https://docs.vllm.ai/en/latest/api/vllm/#vllm.PoolingParams "            PoolingParams") are supported.

```
    use_activation: bool | None = None
```

### `LLM.classify`[¶](#llmclassify "Permanent link")

The [classify](https://docs.vllm.ai/en/latest/api/vllm/#vllm.LLM.classify "            classify") method outputs a probability vector for each prompt.

```
fromvllmimport LLM

llm = LLM(model="jason9693/Qwen2.5-1.5B-apeach", runner="pooling")
(output,) = llm.classify("Hello, my name is")

probs = output.outputs.probs
print(f"Class Probabilities: {probs!r} (size={len(probs)})")
```

A code example can be found here: [examples/basic/offline\_inference/classify.py](https://github.com/vllm-project/vllm/blob/main/examples/basic/offline_inference/classify.py)

### `LLM.encode`[¶](#llmencode "Permanent link")

The [encode](https://docs.vllm.ai/en/latest/api/vllm/#vllm.LLM.encode "            encode") method is available to all pooling models in vLLM.

Set `pooling_task="classify"` when using `LLM.encode` for classification Models:

```
fromvllmimport LLM

llm = LLM(model="jason9693/Qwen2.5-1.5B-apeach", runner="pooling")
(output,) = llm.encode("Hello, my name is", pooling_task="classify")

data = output.outputs.data
print(f"Data: {data!r}")
```

## Online Serving[¶](#online-serving "Permanent link")

### Classification API[¶](#classification-api "Permanent link")

Online `/classify` API is similar to `LLM.classify`.

#### Completion Parameters[¶](#completion-parameters "Permanent link")

The following Classification API parameters are supported:

Code

```
    model: str | None = None
    user: str | None = None
    input: list[int] | list[list[int]] | str | list[str]
```

The following extra parameters are supported:

Code

```
    truncate_prompt_tokens: Annotated[int, Field(ge=-1)] | None = None
    truncation_side: Literal["left", "right"] | None = Field(
        default=None,
        description=(
            "Which side to truncate from when truncate_prompt_tokens is active. "
            "'right' keeps the first N tokens. "
            "'left' keeps the last N tokens."
        ),
    )
    request_id: str = Field(
        default_factory=random_uuid,
        description=(
            "The request_id related to this request. If the caller does "
            "not set it, a random_uuid will be generated. This id is used "
            "through out the inference process and return in response."
        ),
    )
    priority: int = Field(
        default=0,
        ge=-(2**63),
        le=2**63 - 1,
        description=(
            "The priority of the request (lower means earlier handling; "
            "default: 0). Any priority other than 0 will raise an error "
            "if the served model does not use priority scheduling."
        ),
    )
    mm_processor_kwargs: dict[str, Any] | None = Field(
        default=None,
        description="Additional kwargs to pass to the HF processor.",
    )
    cache_salt: str | None = Field(
        default=None,
        description=(
            "If specified, the prefix cache will be salted with the provided "
            "string to prevent an attacker to guess prompts in multi-user "
            "environments. The salt should be random, protected from "
            "access by 3rd parties, and long enough to be "
            "unpredictable (e.g., 43 characters base64-encoded, corresponding "
            "to 256 bit)."
        ),
    )
    add_special_tokens: bool = Field(
        default=True,
        description=(
            "If true (the default), special tokens (e.g. BOS) will be added to "
            "the prompt."
        ),
    )
    use_activation: bool | None = Field(
        default=None,
        description="Whether to use activation for the pooler outputs. "
        "`None` uses the pooler's default, which is `True` in most cases.",
    )
```

#### Chat Parameters[¶](#chat-parameters "Permanent link")

For chat-like input (i.e. if `messages` is passed), the following parameters are supported:

Code

```
    model: str | None = None
    user: str | None = None
    messages: list[ChatCompletionMessageParam]
```

these extra parameters are supported instead:

Code

```
    truncate_prompt_tokens: Annotated[int, Field(ge=-1)] | None = None
    truncation_side: Literal["left", "right"] | None = Field(
        default=None,
        description=(
            "Which side to truncate from when truncate_prompt_tokens is active. "
            "'right' keeps the first N tokens. "
            "'left' keeps the last N tokens."
        ),
    )
    request_id: str = Field(
        default_factory=random_uuid,
        description=(
            "The request_id related to this request. If the caller does "
            "not set it, a random_uuid will be generated. This id is used "
            "through out the inference process and return in response."
        ),
    )
    priority: int = Field(
        default=0,
        ge=-(2**63),
        le=2**63 - 1,
        description=(
            "The priority of the request (lower means earlier handling; "
            "default: 0). Any priority other than 0 will raise an error "
            "if the served model does not use priority scheduling."
        ),
    )
    mm_processor_kwargs: dict[str, Any] | None = Field(
        default=None,
        description="Additional kwargs to pass to the HF processor.",
    )
    cache_salt: str | None = Field(
        default=None,
        description=(
            "If specified, the prefix cache will be salted with the provided "
            "string to prevent an attacker to guess prompts in multi-user "
            "environments. The salt should be random, protected from "
            "access by 3rd parties, and long enough to be "
            "unpredictable (e.g., 43 characters base64-encoded, corresponding "
            "to 256 bit)."
        ),
    )
    add_generation_prompt: bool = Field(
        default=False,
        description=(
            "If true, the generation prompt will be added to the chat template. "
            "This is a parameter used by chat template in tokenizer config of the "
            "model."
        ),
    )
    continue_final_message: bool = Field(
        default=False,
        description=(
            "If this is set, the chat will be formatted so that the final "
            "message in the chat is open-ended, without any EOS tokens. The "
            "model will continue this message rather than starting a new one. "
            'This allows you to "prefill" part of the model\'s response for it. '
            "Cannot be used at the same time as `add_generation_prompt`."
        ),
    )
    add_special_tokens: bool = Field(
        default=False,
        description=(
            "If true, special tokens (e.g. BOS) will be added to the prompt "
            "on top of what is added by the chat template. "
            "For most models, the chat template takes care of adding the "
            "special tokens so this should be set to false (as is the "
            "default)."
        ),
    )
    chat_template: str | None = Field(
        default=None,
        description=(
            "A Jinja template to use for this conversion. "
            "As of transformers v4.44, default chat template is no longer "
            "allowed, so you must provide a chat template if the tokenizer "
            "does not define one."
        ),
    )
    chat_template_kwargs: dict[str, Any] | None = Field(
        default=None,
        description=(
            "Additional keyword args to pass to the template renderer. "
            "Will be accessible by the chat template."
        ),
    )
    media_io_kwargs: dict[str, dict[str, Any]] | None = Field(
        default=None,
        description=(
            "Additional kwargs to pass to the media IO connectors, "
            "keyed by modality. Merged with engine-level media_io_kwargs."
        ),
    )
    use_activation: bool | None = Field(
        default=None,
        description="Whether to use activation for the pooler outputs. "
        "`None` uses the pooler's default, which is `True` in most cases.",
    )
```

#### Example Requests[¶](#example-requests "Permanent link")

Code example: [examples/pooling/classify/classification\_online.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/classify/classification_online.py)

You can classify multiple texts by passing an array of strings:

```
curl-v"http://127.0.0.1:8000/classify"\
-H"Content-Type: application/json"\
-d'{
    "model": "jason9693/Qwen2.5-1.5B-apeach",
    "input": [
      "Loved the new café—coffee was great.",
      "This update broke everything. Frustrating."
    ]
  }'
```

Response

```
{
"id":"classify-7c87cac407b749a6935d8c7ce2a8fba2",
"object":"list",
"created":1745383065,
"model":"jason9693/Qwen2.5-1.5B-apeach",
"data":[
{
"index":0,
"label":"Default",
"probs":[
0.565970778465271,
0.4340292513370514
],
"num_classes":2
},
{
"index":1,
"label":"Spoiled",
"probs":[
0.26448777318000793,
0.7355121970176697
],
"num_classes":2
}
],
"usage":{
"prompt_tokens":20,
"total_tokens":20,
"completion_tokens":0,
"prompt_tokens_details":null
}
}
```

You can also pass a string directly to the `input` field:

```
curl-v"http://127.0.0.1:8000/classify"\
-H"Content-Type: application/json"\
-d'{
    "model": "jason9693/Qwen2.5-1.5B-apeach",
    "input": "Loved the new café—coffee was great."
  }'
```

Response

```
{
"id":"classify-9bf17f2847b046c7b2d5495f4b4f9682",
"object":"list",
"created":1745383213,
"model":"jason9693/Qwen2.5-1.5B-apeach",
"data":[
{
"index":0,
"label":"Default",
"probs":[
0.565970778465271,
0.4340292513370514
],
"num_classes":2
}
],
"usage":{
"prompt_tokens":10,
"total_tokens":10,
"completion_tokens":0,
"prompt_tokens_details":null
}
}
```

## More examples[¶](#more-examples "Permanent link")

More examples can be found here: [examples/pooling/classify](https://github.com/vllm-project/vllm/tree/main/examples/pooling/classify)

## Supported Features[¶](#supported-features "Permanent link")

### Enable/disable activation[¶](#enabledisable-activation "Permanent link")

You can enable or disable activation via `use_activation`.

### Problem type (e.g. `multi_label_classification`)[¶](#problem-type-eg-multi_label_classification "Permanent link")

You can modify the `problem_type` via problem\_type in the Hugging Face config. The supported problem types are: `single_label_classification`, `multi_label_classification`, and `regression`.

Implement alignment with transformers [ForSequenceClassificationLoss](https://github.com/huggingface/transformers/blob/57bb6db6ee4cfaccc45b8d474dfad5a17811ca60/src/transformers/loss/loss_utils.py#L92).

### Affine Score Calibration[¶](#affine-score-calibration "Permanent link")

Affine Score Calibration, also known as [Platt Scaling](https://en.wikipedia.org/wiki/Platt_scaling) (Platt, 1999), is the most widely used method for calibrating classifier outputs into well-calibrated probabilities.

The calibration follows the transformation:

`activation((logit - logit_mean) / logit_sigma)`

Parameter Default Description `logit_mean` `None` Mean subtracted from logits (centers scores) `logit_sigma` `None` Standard deviation used to scale logits after mean subtraction

The computation order is as follows:

```
logits -= logit_mean   # subtract mean (center scores)
logits /= logit_sigma  # divide by sigma (scale)
logits = activation(logits)  # e.g. sigmoid
```

Example configuration:

```
--pooler-config'{"use_activation": true, "logit_mean": 4.5, "logit_sigma": 1.0}'
```

## Removed Features[¶](#removed-features "Permanent link")

### Remove softmax from PoolingParams[¶](#remove-softmax-from-poolingparams "Permanent link")

We have already removed `softmax` and `activation` from PoolingParams. Instead, use `use_activation`, since we allow `classify` and `token_classify` to use any activation function.

### Remove `logit_bias` and `logit_scale`[¶](#remove-logit_bias-and-logit_scale "Permanent link")

`logit_bias` and `logit_scale` are deprecated aliases for `logit_mean` and `logit_sigma` respectively. When using `logit_scale`, it is automatically converted to `logit_sigma = 1/logit_scale`. These deprecated parameters will be removed in v0.21.