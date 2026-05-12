---
title: Scoring Usages - vLLM
url: https://docs.vllm.ai/en/latest/models/pooling_models/scoring/
source: sitemap
fetched_at: 2026-05-07T21:15:03.818814064-03:00
rendered_js: false
word_count: 1613
summary: This document outlines the usage and configuration of vLLM models designed to compute similarity scores between prompts using cross-encoder, late-interaction, and bi-encoder architectures.
tags:
    - vllm
    - model-inference
    - reranking
    - cross-encoder
    - late-interaction
    - bi-encoder
    - similarity-scoring
category: reference
---

[](https://github.com/vllm-project/vllm/edit/main/docs/models/pooling_models/scoring.md "Edit this page")

The score models is designed to compute similarity scores between two input prompts. It supports three model types (aka `score_type`): `cross-encoder`, `late-interaction`, and `bi-encoder`.

Note

vLLM handles only the model inference component of RAG pipelines (such as embedding generation and reranking). For higher-level RAG orchestration, you should leverage integration frameworks like [LangChain](https://github.com/langchain-ai/langchain).

## Summary[¶](#summary "Permanent link")

- Model Usage: Scoring
- Pooling Task:

Score Types Pooling Tasks scoring function `cross-encoder` `classify` (see note) linear classifier `late-interaction` `token_embed` late interaction(MaxSim) `bi-encoder` `embed` cosine similarity

- Offline APIs:
  
  - `LLM.score`
- Online APIs:
  
  - [Score API](https://docs.vllm.ai/en/latest/models/pooling_models/scoring/#score-api) (`/score`)
  - [Rerank API](https://docs.vllm.ai/en/latest/models/pooling_models/scoring/#rerank-api) (`/rerank`, `/v1/rerank`, `/v2/rerank`)

Note

Only when a classification model outputs num\_labels equal to 1 can it be used as a scoring model and have its scoring API enabled.

## Supported Models[¶](#supported-models "Permanent link")

### Cross-encoder models[¶](#cross-encoder-models "Permanent link")

[Cross-encoder](https://www.sbert.net/examples/applications/cross-encoder/README.html) (aka reranker) models are a subset of classification models that accept two prompts as input and output num\_labels equal to 1.

#### Text-only Models[¶](#text-only-models "Permanent link")

Architecture Models Example HF Models Score template (see note) [LoRA](https://docs.vllm.ai/en/latest/features/lora/) [PP](https://docs.vllm.ai/en/latest/serving/parallelism_scaling/) [`BertForSequenceClassification`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/bert/#vllm.model_executor.models.bert.BertForSequenceClassification "            BertForSequenceClassification") BERT-based `cross-encoder/ms-marco-MiniLM-L-6-v2`, etc. N/A `GemmaForSequenceClassification` Gemma-based `BAAI/bge-reranker-v2-gemma`(see note), etc. [bge-reranker-v2-gemma.jinja](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/template/bge-reranker-v2-gemma.jinja) ✅︎ ✅︎ `GteNewForSequenceClassification` mGTE-TRM (see note) `Alibaba-NLP/gte-multilingual-reranker-base`, etc. N/A `LlamaBidirectionalForSequenceClassification`C Llama-based with bidirectional attention `nvidia/llama-nemotron-rerank-1b-v2`, etc. [nemotron-rerank.jinja](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/template/nemotron-rerank.jinja) ✅︎ ✅︎ `ModernBertForSequenceClassification` ModernBERT-based `Alibaba-NLP/gte-reranker-modernbert-base`, etc. N/A `Qwen2ForSequenceClassification`C Qwen2-based `mixedbread-ai/mxbai-rerank-base-v2`(see note), etc. [mxbai\_rerank\_v2.jinja](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/template/mxbai_rerank_v2.jinja) ✅︎ ✅︎ `Qwen3ForSequenceClassification`C Qwen3-based `tomaarsen/Qwen3-Reranker-0.6B-seq-cls`, `Qwen/Qwen3-Reranker-0.6B`(see note), etc. [qwen3\_reranker.jinja](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/template/qwen3_reranker.jinja) ✅︎ ✅︎ [`RobertaForSequenceClassification`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/roberta/#vllm.model_executor.models.roberta.RobertaForSequenceClassification "            RobertaForSequenceClassification") RoBERTa-based `cross-encoder/quora-roberta-base`, etc. N/A `XLMRobertaForSequenceClassification` XLM-RoBERTa-based `BAAI/bge-reranker-v2-m3`, etc. N/A `*Model`C, `*ForCausalLM`C, etc. Generative models N/A N/A * *

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

#### Multimodal Models[¶](#multimodal-models "Permanent link")

Note

For more information about multimodal models inputs, see [this page](https://docs.vllm.ai/en/latest/models/supported_models/#list-of-multimodal-language-models).

Architecture Models Inputs Example HF Models [LoRA](https://docs.vllm.ai/en/latest/features/lora/) [PP](https://docs.vllm.ai/en/latest/serving/parallelism_scaling/) `JinaVLForSequenceClassification` JinaVL-based T + IE+ `jinaai/jina-reranker-m0`, etc. ✅︎ ✅︎ [`LlamaNemotronVLForSequenceClassification`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/nemotron_vl/#vllm.model_executor.models.nemotron_vl.LlamaNemotronVLForSequenceClassification "            LlamaNemotronVLForSequenceClassification") Llama Nemotron Reranker + SigLIP T + IE+ `nvidia/llama-nemotron-rerank-vl-1b-v2` `Qwen3VLForSequenceClassification` Qwen3-VL-Reranker T + IE+ + VE+ `Qwen/Qwen3-VL-Reranker-2B`(see note), etc. ✅︎ ✅︎

C Automatically converted into a classification model via `--convert classify`. ([details](https://docs.vllm.ai/en/latest/models/pooling_models/#model-conversion))  
\* Feature support is the same as that of the original model.

Note

Similar to Qwen3-Reranker, you need to use the following `--hf_overrides` to load the official original `Qwen3-VL-Reranker`.

```
vllmserveQwen/Qwen3-VL-Reranker-2B--hf_overrides'{"architectures": ["Qwen3VLForSequenceClassification"],"classifier_from_token": ["no", "yes"],"is_original_qwen3_reranker": true}'
```

### Late-interaction models[¶](#late-interaction-models "Permanent link")

All models that support token embedding task also support using the score API to compute similarity scores by calculating the late interaction of two input prompts. See [this page](https://docs.vllm.ai/en/latest/models/pooling_models/token_embed/) for more information about token embedding models.

### Text-only Models[¶](#text-only-models_1 "Permanent link")

Architecture Models Example HF Models [LoRA](https://docs.vllm.ai/en/latest/features/lora/) [PP](https://docs.vllm.ai/en/latest/serving/parallelism_scaling/) `ColBERTLfm2Model` LFM2 `LiquidAI/LFM2-ColBERT-350M` `ColBERTModernBertModel` ModernBERT `lightonai/GTE-ModernColBERT-v1` `ColBERTJinaRobertaModel` Jina XLM-RoBERTa `jinaai/jina-colbert-v2` `HF_ColBERT` BERT `answerdotai/answerai-colbert-small-v1`, `colbert-ir/colbertv2.0` `*Model`C, `*ForCausalLM`C, etc. Generative models N/A * *

### Multimodal Models[¶](#multimodal-models_1 "Permanent link")

Note

For more information about multimodal models inputs, see [this page](https://docs.vllm.ai/en/latest/models/supported_models/#list-of-multimodal-language-models).

Architecture Models Inputs Example HF Models [LoRA](https://docs.vllm.ai/en/latest/features/lora/) [PP](https://docs.vllm.ai/en/latest/serving/parallelism_scaling/) `ColModernVBertForRetrieval` ColModernVBERT T / I `ModernVBERT/colmodernvbert-merged` `ColPaliForRetrieval` ColPali T / I `vidore/colpali-v1.3-hf` `ColQwen3` Qwen3-VL T / I `TomoroAI/tomoro-colqwen3-embed-4b`, `TomoroAI/tomoro-colqwen3-embed-8b` `ColQwen3_5` ColQwen3.5 T + I + V `athrael-soju/colqwen3.5-4.5B-v3` `OpsColQwen3Model` Qwen3-VL T / I `OpenSearch-AI/Ops-Colqwen3-4B`, `OpenSearch-AI/Ops-Colqwen3-8B` `Qwen3VLNemotronEmbedModel` Qwen3-VL T / I `nvidia/nemotron-colembed-vl-4b-v2`, `nvidia/nemotron-colembed-vl-8b-v2` ✅︎ ✅︎ `*ForConditionalGeneration`C, `*ForCausalLM`C, etc. Generative models * N/A * *

C Automatically converted into an embedding model via `--convert embed`. ([details](https://docs.vllm.ai/en/latest/models/pooling_models/#model-conversion))  
\* Feature support is the same as that of the original model.

If your model is not in the above list, we will try to automatically convert the model using [as\_embedding\_model](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/adapters/#vllm.model_executor.models.adapters.as_embedding_model "            as_embedding_model").

### Special models[¶](#special-models "Permanent link")

Architecture Models Example HF Models [LoRA](https://docs.vllm.ai/en/latest/features/lora/) [PP](https://docs.vllm.ai/en/latest/serving/parallelism_scaling/) `JinaForRanking` Qwen3-based `jinaai/jina-reranker-v3`

jina-reranker-v3 is a listwise document reranker model with a novel `last but not late interaction` architecture. More information can be found at: [examples/pooling/token\_embed/jina\_reranker\_v3\_offline.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/token_embed/jina_reranker_v3_offline.py)

### Bi-encoder[¶](#bi-encoder "Permanent link")

All models that support embedding task also support using the score API to compute similarity scores by calculating the cosine similarity of two input prompt's embeddings. See [this page](https://docs.vllm.ai/en/latest/models/pooling_models/embed/) for more information about embedding models.

### Text-only Models[¶](#text-only-models_2 "Permanent link")

Architecture Models Example HF Models [LoRA](https://docs.vllm.ai/en/latest/features/lora/) [PP](https://docs.vllm.ai/en/latest/serving/parallelism_scaling/) `BertModel` BERT-based `BAAI/bge-base-en-v1.5`, `Snowflake/snowflake-arctic-embed-xs`, etc. `BertSpladeSparseEmbeddingModel` SPLADE `naver/splade-v3` `ErnieModel` BERT-like Chinese ERNIE `shibing624/text2vec-base-chinese-sentence` `Gemma2Model`C Gemma 2-based `BAAI/bge-multilingual-gemma2`, etc. ✅︎ ✅︎ `Gemma3TextModel`C Gemma 3-based `google/embeddinggemma-300m`, etc. ✅︎ ✅︎ `GritLM` GritLM `parasail-ai/GritLM-7B-vllm`. ✅︎ ✅︎ `GteModel` Arctic-Embed-2.0-M `Snowflake/snowflake-arctic-embed-m-v2.0`. `GteNewModel` mGTE-TRM (see note) `Alibaba-NLP/gte-multilingual-base`, etc. `JinaEmbeddingsV5Model`C Qwen3-based with task-specific LoRA adapters `jinaai/jina-embeddings-v5-text-small` (see note) ✅︎ ✅︎ `LlamaBidirectionalModel`C Llama-based with bidirectional attention `nvidia/llama-nemotron-embed-1b-v2`, etc. ✅︎ ✅︎ `LlamaModel`C, `LlamaForCausalLM`C, `MistralModel`C, etc. Llama-based `intfloat/e5-mistral-7b-instruct`, etc. ✅︎ ✅︎ `ModernBertModel` ModernBERT-based `Alibaba-NLP/gte-modernbert-base`, etc. `NomicBertModel` Nomic BERT `nomic-ai/nomic-embed-text-v1`, `nomic-ai/nomic-embed-text-v2-moe`, `Snowflake/snowflake-arctic-embed-m-long`, etc. `Qwen2Model`C, `Qwen2ForCausalLM`C Qwen2-based `ssmits/Qwen2-7B-Instruct-embed-base` (see note), `Alibaba-NLP/gte-Qwen2-7B-instruct` (see note), etc. ✅︎ ✅︎ `Qwen3Model`C, `Qwen3ForCausalLM`C Qwen3-based `Qwen/Qwen3-Embedding-0.6B`, etc. ✅︎ ✅︎ `RobertaModel`, `RobertaForMaskedLM` RoBERTa-based `sentence-transformers/all-roberta-large-v1`, etc. `VoyageQwen3BidirectionalEmbedModel`C Voyage Qwen3-based with bidirectional attention `voyageai/voyage-4-nano`, etc. ✅︎ ✅︎ `XLMRobertaModel` XLMRobertaModel-based `BAAI/bge-m3` (see note), `intfloat/multilingual-e5-base`, `jinaai/jina-embeddings-v3` (see note), etc. `*Model`C, `*ForCausalLM`C, etc. Generative models N/A * *

Note

The second-generation GTE model (mGTE-TRM) is named `NewModel`. The name `NewModel` is too generic, you should set `--hf-overrides '{"architectures": ["GteNewModel"]}'` to specify the use of the `GteNewModel` architecture.

Note

`ssmits/Qwen2-7B-Instruct-embed-base` has an improperly defined Sentence Transformers config. You need to manually set mean pooling by passing `--pooler-config '{"pooling_type": "MEAN"}'`.

Note

The `BAAI/bge-m3` model comes with extra weights for sparse and colbert embeddings, See [this page](https://docs.vllm.ai/en/latest/models/pooling_models/specific_models/#baaibge-m3) for more information.

Note

`jinaai/jina-embeddings-v3` supports multiple tasks through LoRA, while vllm temporarily only supports text-matching tasks by merging LoRA weights.

Note

`jinaai/jina-embeddings-v5-text-small` ships with four task-specific LoRA adapters (`retrieval`, `text-matching`, `classification`, `clustering`). vLLM merges the selected adapter into the base weights at load time. Choose the task with `--hf-overrides '{"jina_task": "<task>"}'`; the default is `retrieval`.

### Multimodal Models[¶](#multimodal-models_2 "Permanent link")

Note

For more information about multimodal models inputs, see [this page](https://docs.vllm.ai/en/latest/models/supported_models/#list-of-multimodal-language-models).

Architecture Models Inputs Example HF Models [LoRA](https://docs.vllm.ai/en/latest/features/lora/) [PP](https://docs.vllm.ai/en/latest/serving/parallelism_scaling/) `CLIPModel` CLIP T / I `openai/clip-vit-base-patch32`, `openai/clip-vit-large-patch14`, etc. `LlamaNemotronVLModel` Llama Nemotron Embedding + SigLIP T + I `nvidia/llama-nemotron-embed-vl-1b-v2` `LlavaNextForConditionalGeneration`C LLaVA-NeXT-based T / I `royokong/e5-v` ✅︎ `Phi3VForCausalLM`C Phi-3-Vision-based T + I `TIGER-Lab/VLM2Vec-Full` ✅︎ `Qwen3VLForConditionalGeneration`C Qwen3-VL T + I + V `Qwen/Qwen3-VL-Embedding-2B`, etc. ✅︎ ✅︎ `SiglipModel` SigLIP, SigLIP2 T / I `google/siglip-base-patch16-224`, `google/siglip2-base-patch16-224` `*ForConditionalGeneration`C, `*ForCausalLM`C, etc. Generative models * N/A * *

C Automatically converted into an embedding model via `--convert embed`. ([details](https://docs.vllm.ai/en/latest/models/pooling_models/#model-conversion))  
\* Feature support is the same as that of the original model.

If your model is not in the above list, we will try to automatically convert the model using [as\_embedding\_model](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/adapters/#vllm.model_executor.models.adapters.as_embedding_model "            as_embedding_model"). By default, the embeddings of the whole prompt are extracted from the normalized hidden state corresponding to the last token.

Note

Although vLLM supports automatically converting models of any architecture into embedding models via --convert embed, to get the best results, you should use pooling models that are specifically trained as such.

## Offline Inference[¶](#offline-inference "Permanent link")

### Pooling Parameters[¶](#pooling-parameters "Permanent link")

The following [pooling parameters](https://docs.vllm.ai/en/latest/api/vllm/#vllm.PoolingParams "            PoolingParams") are only supported by cross-encoder models and do not work for late-interaction and bi-encoder models.

```
    use_activation: bool | None = None
```

### `LLM.score`[¶](#llmscore "Permanent link")

The [score](https://docs.vllm.ai/en/latest/api/vllm/#vllm.LLM.score "            score") method outputs similarity scores between sentence pairs.

```
fromvllmimport LLM

llm = LLM(model="BAAI/bge-reranker-v2-m3", runner="pooling")
(output,) = llm.score(
    "What is the capital of France?",
    "The capital of Brazil is Brasilia.",
)

score = output.outputs.score
print(f"Score: {score}")
```

A code example can be found here: [examples/basic/offline\_inference/score.py](https://github.com/vllm-project/vllm/blob/main/examples/basic/offline_inference/score.py)

## Online Serving[¶](#online-serving "Permanent link")

### Score API[¶](#score-api "Permanent link")

Our Score API (`/score`) is similar to `LLM.score`, compute similarity scores between two input prompts.

#### Parameters[¶](#parameters "Permanent link")

The following Score API parameters are supported:

```
    model: str | None = None
    user: str | None = None
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
    use_activation: bool | None = Field(
        default=None,
        description="Whether to use activation for the pooler outputs. "
        "`None` uses the pooler's default, which is `True` in most cases.",
    )
    max_tokens_per_query: int = Field(
        default=0,
        description=(
            "Maximum number of tokens per query. Queries longer than "
            "this will be truncated to this length. 0 means no "
            "query-level truncation is applied."
        ),
    )
    max_tokens_per_doc: int = Field(
        default=0,
        description=(
            "Maximum number of tokens per document. Documents longer than "
            "this will be truncated to this length. 0 means no "
            "document-level truncation is applied (only truncate_prompt_tokens "
            "applies to the combined query+document)."
        ),
    )
    queries: ScoreInput | list[ScoreInput]
    documents: ScoreInput | list[ScoreInput]
```

#### Examples[¶](#examples "Permanent link")

##### Single inference[¶](#single-inference "Permanent link")

You can pass a string to both `queries` and `documents`, forming a single sentence pair.

```
curl-X'POST'\
'http://127.0.0.1:8000/score'\
-H'accept: application/json'\
-H'Content-Type: application/json'\
-d'{
  "model": "BAAI/bge-reranker-v2-m3",
  "encoding_format": "float",
  "queries": "What is the capital of France?",
  "documents": "The capital of France is Paris."
}'
```

Response

```
{
"id":"score-request-id",
"object":"list",
"created":693447,
"model":"BAAI/bge-reranker-v2-m3",
"data":[
{
"index":0,
"object":"score",
"score":1
}
],
"usage":{}
}
```

##### Batch inference[¶](#batch-inference "Permanent link")

You can pass a string to `queries` and a list to `documents`, forming multiple sentence pairs where each pair is built from `queries` and a string in `documents`. The total number of pairs is `len(documents)`.

Request

```
curl-X'POST'\
'http://127.0.0.1:8000/score'\
-H'accept: application/json'\
-H'Content-Type: application/json'\
-d'{
  "model": "BAAI/bge-reranker-v2-m3",
  "queries": "What is the capital of France?",
  "documents": [
    "The capital of Brazil is Brasilia.",
    "The capital of France is Paris."
  ]
}'
```

Response

```
{
"id":"score-request-id",
"object":"list",
"created":693570,
"model":"BAAI/bge-reranker-v2-m3",
"data":[
{
"index":0,
"object":"score",
"score":0.001094818115234375
},
{
"index":1,
"object":"score",
"score":1
}
],
"usage":{}
}
```

You can pass a list to both `queries` and `documents`, forming multiple sentence pairs where each pair is built from a string in `queries` and the corresponding string in `documents` (similar to `zip()`). The total number of pairs is `len(documents)`.

Request

```
curl-X'POST'\
'http://127.0.0.1:8000/score'\
-H'accept: application/json'\
-H'Content-Type: application/json'\
-d'{
  "model": "BAAI/bge-reranker-v2-m3",
  "encoding_format": "float",
  "queries": [
    "What is the capital of Brazil?",
    "What is the capital of France?"
  ],
  "documents": [
    "The capital of Brazil is Brasilia.",
    "The capital of France is Paris."
  ]
}'
```

Response

```
{
"id":"score-request-id",
"object":"list",
"created":693447,
"model":"BAAI/bge-reranker-v2-m3",
"data":[
{
"index":0,
"object":"score",
"score":1
},
{
"index":1,
"object":"score",
"score":1
}
],
"usage":{}
}
```

##### Multi-modal inputs[¶](#multi-modal-inputs "Permanent link")

You can pass multi-modal inputs to scoring models by passing `content` including a list of multi-modal input (image, etc.) in the request. Refer to the examples below for illustration.

JinaVL-Reranker

To serve the model:

```
vllmservejinaai/jina-reranker-m0
```

Since the request schema is not defined by OpenAI client, we post a request to the server using the lower-level `requests` library:

Code

```
importrequests

response = requests.post(
    "http://localhost:8000/v1/score",
    json={
        "model": "jinaai/jina-reranker-m0",
        "queries": "slm markdown",
        "documents": [
            {
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://raw.githubusercontent.com/jina-ai/multimodal-reranker-test/main/handelsblatt-preview.png"
                        },
                    }
                ],
            },
            {
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://raw.githubusercontent.com/jina-ai/multimodal-reranker-test/main/handelsblatt-preview.png"
                        },
                    }
                ]
            },
        ],
    },
)
response.raise_for_status()
response_json = response.json()
print("Scoring output:", response_json["data"][0]["score"])
print("Scoring output:", response_json["data"][1]["score"])
```

Full example:

- [examples/pooling/score/vision\_score\_api\_online.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/vision_score_api_online.py)
- [examples/pooling/score/vision\_rerank\_api\_online.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/vision_rerank_api_online.py)

### Rerank API[¶](#rerank-api "Permanent link")

`/rerank`, `/v1/rerank`, and `/v2/rerank` APIs are compatible with both [Jina AI's rerank API interface](https://jina.ai/reranker/) and [Cohere's rerank API interface](https://docs.cohere.com/v2/reference/rerank) to ensure compatibility with popular open-source tools.

Code example: [examples/pooling/score/rerank\_api\_online.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/rerank_api_online.py)

#### Parameters[¶](#parameters_1 "Permanent link")

The following rerank api parameters are supported:

```
    model: str | None = None
    user: str | None = None
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
    use_activation: bool | None = Field(
        default=None,
        description="Whether to use activation for the pooler outputs. "
        "`None` uses the pooler's default, which is `True` in most cases.",
    )
    max_tokens_per_query: int = Field(
        default=0,
        description=(
            "Maximum number of tokens per query. Queries longer than "
            "this will be truncated to this length. 0 means no "
            "query-level truncation is applied."
        ),
    )
    max_tokens_per_doc: int = Field(
        default=0,
        description=(
            "Maximum number of tokens per document. Documents longer than "
            "this will be truncated to this length. 0 means no "
            "document-level truncation is applied (only truncate_prompt_tokens "
            "applies to the combined query+document)."
        ),
    )
    query: ScoreInput
    documents: ScoreInput | list[ScoreInput]
    top_n: int = Field(default_factory=lambda: 0)
```

#### Examples[¶](#examples_1 "Permanent link")

Note that the `top_n` request parameter is optional and will default to the length of the `documents` field. Result documents will be sorted by relevance, and the `index` property can be used to determine original order.

Request

```
curl-X'POST'\
'http://127.0.0.1:8000/v1/rerank'\
-H'accept: application/json'\
-H'Content-Type: application/json'\
-d'{
  "model": "BAAI/bge-reranker-base",
  "query": "What is the capital of France?",
  "documents": [
    "The capital of Brazil is Brasilia.",
    "The capital of France is Paris.",
    "Horses and cows are both animals"
  ]
}'
```

Response

```
{
"id":"rerank-fae51b2b664d4ed38f5969b612edff77",
"model":"BAAI/bge-reranker-base",
"usage":{
"total_tokens":56
},
"results":[
{
"index":1,
"document":{
"text":"The capital of France is Paris."
},
"relevance_score":0.99853515625
},
{
"index":0,
"document":{
"text":"The capital of Brazil is Brasilia."
},
"relevance_score":0.0005860328674316406
}
]
}
```

## More examples[¶](#more-examples "Permanent link")

More examples can be found here: [examples/pooling/score](https://github.com/vllm-project/vllm/tree/main/examples/pooling/score)

## Supported Features[¶](#supported-features "Permanent link")

AS cross-encoder models are a subset of classification models that accept two prompts as input and output num\_labels equal to 1, cross-encoder features should be consistent with (sequence) classification. For more information, see [this page](https://docs.vllm.ai/en/latest/models/pooling_models/classify/#supported-features).

### Score Template[¶](#score-template "Permanent link")

Score templates are supported for **cross-encoder** models only. If you are using an **embedding** model for scoring, vLLM does not apply a score template.

Some scoring models require a specific prompt format to work correctly. You can specify a custom score template using the `--chat-template` parameter (see [Chat Template](https://docs.vllm.ai/en/latest/serving/openai_compatible_server/#chat-template)).

Like chat templates, the score template receives a `messages` list. For scoring, each message has a `role` attribute—either `"query"` or `"document"`. For the usual kind of point-wise cross-encoder, you can expect exactly two messages: one query and one document. To access the query and document content, use Jinja's `selectattr` filter:

- **Query**: `{{ (messages | selectattr("role", "eq", "query") | first).content }}`
- **Document**: `{{ (messages | selectattr("role", "eq", "document") | first).content }}`

This approach is more robust than index-based access (`messages[0]`, `messages[1]`) because it selects messages by their semantic role. It also avoids assumptions about message ordering if additional message types are added to `messages` in the future.

Example template file: [examples/pooling/score/template/nemotron-rerank.jinja](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/template/nemotron-rerank.jinja)

### Enable/disable activation[¶](#enabledisable-activation "Permanent link")

You can enable or disable activation via `use_activation` only works for cross-encoder models.