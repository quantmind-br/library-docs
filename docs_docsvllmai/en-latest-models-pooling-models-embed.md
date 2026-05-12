---
title: Embedding Usages - vLLM
url: https://docs.vllm.ai/en/latest/models/pooling_models/embed/
source: sitemap
fetched_at: 2026-05-07T21:15:02.074520906-03:00
rendered_js: false
word_count: 1550
summary: This document provides an overview of using embedding models in vLLM, detailing supported architectures, API interfaces for offline and online usage, and specific configuration requirements for text and multimodal models.
tags:
    - vllm
    - embedding-models
    - model-serving
    - natural-language-processing
    - machine-learning-infrastructure
    - api-integration
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/models/pooling_models/embed.md "Edit this page")

Embedding models are a class of machine learning models designed to transform unstructured data—such as text, images, or audio—into a structured numerical representation known as an embedding.

## Summary[¶](#summary "Permanent link")

- Model Usage: (sequence) embedding
- Pooling Task: `embed`
- Offline APIs:
  
  - `LLM.embed(...)`
  - `LLM.encode(..., pooling_task="embed")`
  - `LLM.score(...)`
- Online APIs:
  
  - [Cohere Embed API](https://docs.vllm.ai/en/latest/models/pooling_models/embed/#cohere-embed-api) (`/v2/embed`)
  - [Openai-compatible Embeddings API](https://docs.vllm.ai/en/latest/models/pooling_models/embed/#openai-compatible-embeddings-api) (`/v1/embeddings`)
  - Pooling API (`/pooling`)

The primary distinction between (sequence) embedding and token embedding lies in their output granularity: (sequence) embedding produces a single embedding vector for an entire input sequence, whereas token embedding generates an embedding for each individual token within the sequence.

Many embedding models support both (sequence) embedding and token embedding. For further details on token embedding, please refer to [this page](https://docs.vllm.ai/en/latest/models/pooling_models/token_embed/).

## Typical Use Cases[¶](#typical-use-cases "Permanent link")

### Embedding[¶](#embedding "Permanent link")

The most basic use case of embedding models is to embed the inputs, e.g. for RAG.

### Pairwise Similarity[¶](#pairwise-similarity "Permanent link")

You can compute pairwise similarity scores to build a similarity matrix using the [Score API](https://docs.vllm.ai/en/latest/models/pooling_models/scoring/).

## Supported Models[¶](#supported-models "Permanent link")

### Text-only Models[¶](#text-only-models "Permanent link")

Architecture Models Example HF Models [LoRA](https://docs.vllm.ai/en/latest/features/lora/) [PP](https://docs.vllm.ai/en/latest/serving/parallelism_scaling/) `BertModel` BERT-based `BAAI/bge-base-en-v1.5`, `Snowflake/snowflake-arctic-embed-xs`, etc. [`BertSpladeSparseEmbeddingModel`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/bert/#vllm.model_executor.models.bert.BertSpladeSparseEmbeddingModel "            BertSpladeSparseEmbeddingModel") SPLADE `naver/splade-v3` `ErnieModel` BERT-like Chinese ERNIE `shibing624/text2vec-base-chinese-sentence` `Gemma2Model`C Gemma 2-based `BAAI/bge-multilingual-gemma2`, etc. ✅︎ ✅︎ `Gemma3TextModel`C Gemma 3-based `google/embeddinggemma-300m`, etc. ✅︎ ✅︎ [`GritLM`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/gritlm/#vllm.model_executor.models.gritlm.GritLM "            GritLM") GritLM `parasail-ai/GritLM-7B-vllm`. ✅︎ ✅︎ `GteModel` Arctic-Embed-2.0-M `Snowflake/snowflake-arctic-embed-m-v2.0`. `GteNewModel` mGTE-TRM (see note) `Alibaba-NLP/gte-multilingual-base`, etc. [`JinaEmbeddingsV5Model`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/jina/#vllm.model_executor.models.jina.JinaEmbeddingsV5Model "            JinaEmbeddingsV5Model")C Qwen3-based with task-specific LoRA adapters `jinaai/jina-embeddings-v5-text-small` (see note) ✅︎ ✅︎ `LlamaBidirectionalModel`C Llama-based with bidirectional attention `nvidia/llama-nemotron-embed-1b-v2`, etc. ✅︎ ✅︎ `LlamaModel`C, `LlamaForCausalLM`C, `MistralModel`C, etc. Llama-based `intfloat/e5-mistral-7b-instruct`, etc. ✅︎ ✅︎ `ModernBertModel` ModernBERT-based `Alibaba-NLP/gte-modernbert-base`, etc. `NomicBertModel` Nomic BERT `nomic-ai/nomic-embed-text-v1`, `nomic-ai/nomic-embed-text-v2-moe`, `Snowflake/snowflake-arctic-embed-m-long`, etc. `Qwen2Model`C, `Qwen2ForCausalLM`C Qwen2-based `ssmits/Qwen2-7B-Instruct-embed-base` (see note), `Alibaba-NLP/gte-Qwen2-7B-instruct` (see note), etc. ✅︎ ✅︎ `Qwen3Model`C, `Qwen3ForCausalLM`C Qwen3-based `Qwen/Qwen3-Embedding-0.6B`, etc. ✅︎ ✅︎ `RobertaModel`, `RobertaForMaskedLM` RoBERTa-based `sentence-transformers/all-roberta-large-v1`, etc. [`VoyageQwen3BidirectionalEmbedModel`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/voyage/#vllm.model_executor.models.voyage.VoyageQwen3BidirectionalEmbedModel "            VoyageQwen3BidirectionalEmbedModel")C Voyage Qwen3-based with bidirectional attention `voyageai/voyage-4-nano`, etc. ✅︎ ✅︎ `XLMRobertaModel` XLMRobertaModel-based `BAAI/bge-m3` (see note), `intfloat/multilingual-e5-base`, `jinaai/jina-embeddings-v3` (see note), etc. `*Model`C, `*ForCausalLM`C, etc. Generative models N/A * *

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

### Multimodal Models[¶](#multimodal-models "Permanent link")

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

The following [pooling parameters](https://docs.vllm.ai/en/latest/api/vllm/#vllm.PoolingParams "            PoolingParams") are supported.

```
    use_activation: bool | None = None
    dimensions: int | None = None
```

### `LLM.embed`[¶](#llmembed "Permanent link")

The [embed](https://docs.vllm.ai/en/latest/api/vllm/#vllm.LLM.embed "            embed") method outputs an embedding vector for each prompt.

```
fromvllmimport LLM

llm = LLM(model="intfloat/e5-small", runner="pooling")
(output,) = llm.embed("Hello, my name is")

embeds = output.outputs.embedding
print(f"Embeddings: {embeds!r} (size={len(embeds)})")
```

A code example can be found here: [examples/basic/offline\_inference/embed.py](https://github.com/vllm-project/vllm/blob/main/examples/basic/offline_inference/embed.py)

### `LLM.encode`[¶](#llmencode "Permanent link")

The [encode](https://docs.vllm.ai/en/latest/api/vllm/#vllm.LLM.encode "            encode") method is available to all pooling models in vLLM.

Set `pooling_task="embed"` when using `LLM.encode` for embedding Models:

```
fromvllmimport LLM

llm = LLM(model="intfloat/e5-small", runner="pooling")
(output,) = llm.encode("Hello, my name is", pooling_task="embed")

data = output.outputs.data
print(f"Data: {data!r}")
```

### `LLM.score`[¶](#llmscore "Permanent link")

The [score](https://docs.vllm.ai/en/latest/api/vllm/#vllm.LLM.score "            score") method outputs similarity scores between sentence pairs.

All models that support embedding task also support using the score API to compute similarity scores by calculating the cosine similarity of two input prompt's embeddings.

```
fromvllmimport LLM

llm = LLM(model="intfloat/e5-small", runner="pooling")
(output,) = llm.score(
    "What is the capital of France?",
    "The capital of Brazil is Brasilia.",
)

score = output.outputs.score
print(f"Score: {score}")
```

## Online Serving[¶](#online-serving "Permanent link")

### OpenAI-Compatible Embeddings API[¶](#openai-compatible-embeddings-api "Permanent link")

Our Embeddings API is compatible with [OpenAI's Embeddings API](https://platform.openai.com/docs/api-reference/embeddings); you can use the [official OpenAI Python client](https://github.com/openai/openai-python) to interact with it.

Code example: [examples/pooling/embed/openai\_embedding\_client.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/embed/openai_embedding_client.py)

#### Completion Parameters[¶](#completion-parameters "Permanent link")

The following Classification API parameters are supported:

Code

```
    model: str | None = None
    user: str | None = None
    input: list[int] | list[list[int]] | str | list[str]
    encoding_format: EncodingFormat = "float"
    dimensions: int | None = None
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
    embed_dtype: EmbedDType = Field(
        default="float32",
        description=(
            "What dtype to use for encoding. Default to using float32 for base64 "
            "encoding to match the OpenAI python client behavior. "
            "This parameter will affect base64 and binary_response."
        ),
    )
    endianness: Endianness = Field(
        default="native",
        description=(
            "What endianness to use for encoding. Default to using native for "
            "base64 encoding to match the OpenAI python client behavior."
            "This parameter will affect base64 and binary_response."
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
    encoding_format: EncodingFormat = "float"
    dimensions: int | None = None
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
    embed_dtype: EmbedDType = Field(
        default="float32",
        description=(
            "What dtype to use for encoding. Default to using float32 for base64 "
            "encoding to match the OpenAI python client behavior. "
            "This parameter will affect base64 and binary_response."
        ),
    )
    endianness: Endianness = Field(
        default="native",
        description=(
            "What endianness to use for encoding. Default to using native for "
            "base64 encoding to match the OpenAI python client behavior."
            "This parameter will affect base64 and binary_response."
        ),
    )
    use_activation: bool | None = Field(
        default=None,
        description="Whether to use activation for the pooler outputs. "
        "`None` uses the pooler's default, which is `True` in most cases.",
    )
```

#### Examples[¶](#examples "Permanent link")

If the model has a [chat template](https://docs.vllm.ai/en/latest/serving/openai_compatible_server/#chat-template), you can replace `inputs` with a list of `messages` (same schema as [Chat API](https://docs.vllm.ai/en/latest/serving/openai_compatible_server/#chat-api)) which will be treated as a single prompt to the model. Here is a convenience function for calling the API while retaining OpenAI's type annotations:

Code

```
fromopenaiimport OpenAI
fromopenai._typesimport NOT_GIVEN, NotGiven
fromopenai.types.chatimport ChatCompletionMessageParam
fromopenai.types.create_embedding_responseimport CreateEmbeddingResponse

defcreate_chat_embeddings(
    client: OpenAI,
    *,
    messages: list[ChatCompletionMessageParam],
    model: str,
    encoding_format: Union[Literal["base64", "float"], NotGiven] = NOT_GIVEN,
) -> CreateEmbeddingResponse:
    return client.post(
        "/embeddings",
        cast_to=CreateEmbeddingResponse,
        body={"messages": messages, "model": model, "encoding_format": encoding_format},
    )
```

##### Multi-modal inputs[¶](#multi-modal-inputs "Permanent link")

You can pass multi-modal inputs to embedding models by defining a custom chat template for the server and passing a list of `messages` in the request. Refer to the examples below for illustration.

VLM2VecDSE-Qwen2-MRL

To serve the model:

```
vllmserveTIGER-Lab/VLM2Vec-Full--runnerpooling\
--trust-remote-code\
--max-model-len4096\
--chat-templateexamples/pooling/embed/template/vlm2vec_phi3v.jinja
```

Important

Since VLM2Vec has the same model architecture as Phi-3.5-Vision, we have to explicitly pass `--runner pooling` to run this model in embedding mode instead of text generation mode.

The custom chat template is completely different from the original one for this model, and can be found here: [examples/pooling/embed/template/vlm2vec\_phi3v.jinja](https://github.com/vllm-project/vllm/blob/main/examples/pooling/embed/template/vlm2vec_phi3v.jinja)

Since the request schema is not defined by OpenAI client, we post a request to the server using the lower-level `requests` library:

Code

```
fromopenaiimport OpenAI
client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="EMPTY",
)
image_url = "https://vllm-public-assets.s3.us-west-2.amazonaws.com/vision_model_images/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"

response = create_chat_embeddings(
    client,
    model="TIGER-Lab/VLM2Vec-Full",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "image_url", "image_url": {"url": image_url}},
                {"type": "text", "text": "Represent the given image."},
            ],
        }
    ],
    encoding_format="float",
)

print("Image embedding output:", response.data[0].embedding)
```

To serve the model:

```
vllmserveMrLight/dse-qwen2-2b-mrl-v1--runnerpooling\
--trust-remote-code\
--max-model-len8192\
--chat-templateexamples/pooling/embed/template/dse_qwen2_vl.jinja
```

Important

`MrLight/dse-qwen2-2b-mrl-v1` requires a placeholder image of the minimum image size for text query embeddings. See the full code example below for details.

Full example: [examples/pooling/embed/vision\_embedding\_online.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/embed/vision_embedding_online.py)

### Cohere Embed API[¶](#cohere-embed-api "Permanent link")

Our API is also compatible with [Cohere's Embed v2 API](https://docs.cohere.com/reference/embed) which adds support for some modern embedding feature such as truncation, output dimensions, embedding types, and input types. This endpoint works with any embedding model (including multimodal models).

#### Cohere Embed API request parameters[¶](#cohere-embed-api-request-parameters "Permanent link")

Parameter Type Required Description `model` string Yes Model name `input_type` string No Prompt prefix key (model-dependent, see below) `texts` list\[string] No Text inputs (use one of `texts`, `images`, or `inputs`) `images` list\[string] No Base64 data URI images `inputs` list\[object] No Mixed text and image content objects `embedding_types` list\[string] No Output types (default: `["float"]`) `output_dimension` int No Truncate embeddings to this dimension (Matryoshka) `truncate` string No `END`, `START`, or `NONE` (default: `END`)

#### Text embedding[¶](#text-embedding "Permanent link")

```
curl-XPOST"http://localhost:8000/v2/embed"\
-H"Content-Type: application/json"\
-d'{
    "model": "Snowflake/snowflake-arctic-embed-m-v1.5",
    "input_type": "query",
    "texts": ["Hello world", "How are you?"],
    "embedding_types": ["float"]
  }'
```

Response

```
{
"id":"embd-...",
"embeddings":{
"float":[
[0.012,-0.034,...],
[0.056,0.078,...]
]
},
"texts":["Hello world","How are you?"],
"meta":{
"api_version":{"version":"2"},
"billed_units":{"input_tokens":12}
}
}
```

#### Mixed text and image inputs[¶](#mixed-text-and-image-inputs "Permanent link")

For multimodal models, you can embed images by passing base64 data URIs. The `inputs` field accepts a list of objects with mixed text and image content:

```
curl-XPOST"http://localhost:8000/v2/embed"\
-H"Content-Type: application/json"\
-d'{
    "model": "google/siglip-so400m-patch14-384",
    "inputs": [
      {
        "content": [
          {"type": "text", "text": "A photo of a cat"},
          {"type": "image_url", "image_url": {"url": "data:image/png;base64,iVBOR..."}}
        ]
      }
    ],
    "embedding_types": ["float"]
  }'
```

#### Embedding types[¶](#embedding-types "Permanent link")

The `embedding_types` parameter controls the output format. Multiple types can be requested in a single call:

Type Description `float` Raw float32 embeddings (default) `binary` Bit-packed signed binary `ubinary` Bit-packed unsigned binary `base64` Little-endian float32 encoded as base64

```
curl-XPOST"http://localhost:8000/v2/embed"\
-H"Content-Type: application/json"\
-d'{
    "model": "Snowflake/snowflake-arctic-embed-m-v1.5",
    "input_type": "query",
    "texts": ["What is machine learning?"],
    "embedding_types": ["float", "binary"]
  }'
```

Response

```
{
"id":"embd-...",
"embeddings":{
"float":[[0.012,-0.034,...]],
"binary":[[42,-117,...]]
},
"texts":["What is machine learning?"],
"meta":{
"api_version":{"version":"2"},
"billed_units":{"input_tokens":8}
}
}
```

#### Truncation[¶](#truncation "Permanent link")

The `truncate` parameter controls how inputs exceeding the model's maximum sequence length are handled:

Value Behavior `END` (default) Keep the first tokens, drop the end `START` Keep the last tokens, drop the beginning `NONE` Return an error if the input is too long

#### Input type and prompt prefixes[¶](#input-type-and-prompt-prefixes "Permanent link")

The `input_type` field selects a prompt prefix to prepend to each text input. The available values depend on the model:

- **Models with `task_instructions` in `config.json`** : The keys from the `task_instructions` dict are the valid `input_type` values and the corresponding value is prepended to each text.
- **Models with `config_sentence_transformers.json` prompts**: The keys from the `prompts` dict are the valid `input_type` values. For example, `Snowflake/snowflake-arctic-embed-xs` defines `"query"`, so setting `input_type: "query"` prepends `"Represent this sentence for searching relevant passages: "`.
- **Other models**: `input_type` is not accepted and will raise a validation error if passed.

## More examples[¶](#more-examples "Permanent link")

More examples can be found here: [examples/pooling/embed](https://github.com/vllm-project/vllm/tree/main/examples/pooling/embed)

## Supported Features[¶](#supported-features "Permanent link")

### Enable/disable normalize[¶](#enabledisable-normalize "Permanent link")

You can enable or disable normalize via `use_activation`.

### Matryoshka Embeddings[¶](#matryoshka-embeddings "Permanent link")

[Matryoshka Embeddings](https://sbert.net/examples/sentence_transformer/training/matryoshka/README.html#matryoshka-embeddings) or [Matryoshka Representation Learning (MRL)](https://arxiv.org/abs/2205.13147) is a technique used in training embedding models. It allows users to trade off between performance and cost.

Warning

Not all embedding models are trained using Matryoshka Representation Learning. To avoid misuse of the `dimensions` parameter, vLLM returns an error for requests that attempt to change the output dimension of models that do not support Matryoshka Embeddings.

For example, setting `dimensions` parameter while using the `BAAI/bge-m3` model will result in the following error.

```
{"object":"error","message":"Model \"BAAI/bge-m3\" does not support matryoshka representation, changing output dimensions will lead to poor results.","type":"BadRequestError","param":null,"code":400}
```

#### Manually enable Matryoshka Embeddings[¶](#manually-enable-matryoshka-embeddings "Permanent link")

There is currently no official interface for specifying support for Matryoshka Embeddings. In vLLM, if `is_matryoshka` is `True` in `config.json`, you can change the output dimension to arbitrary values. Use `matryoshka_dimensions` to control the allowed output dimensions.

For models that support Matryoshka Embeddings but are not recognized by vLLM, manually override the config using `hf_overrides={"is_matryoshka": True}` or `hf_overrides={"matryoshka_dimensions": [<allowed output dimensions>]}` (offline), or `--hf-overrides '{"is_matryoshka": true}'` or `--hf-overrides '{"matryoshka_dimensions": [<allowed output dimensions>]}'` (online).

Here is an example to serve a model with Matryoshka Embeddings enabled.

```
vllmserveSnowflake/snowflake-arctic-embed-m-v1.5--hf-overrides'{"matryoshka_dimensions":[256]}'
```

#### Offline Inference[¶](#offline-inference_1 "Permanent link")

You can change the output dimensions of embedding models that support Matryoshka Embeddings by using the dimensions parameter in [PoolingParams](https://docs.vllm.ai/en/latest/api/vllm/#vllm.PoolingParams "            PoolingParams").

```
fromvllmimport LLM, PoolingParams

llm = LLM(
    model="jinaai/jina-embeddings-v3",
    runner="pooling",
    trust_remote_code=True,
)
outputs = llm.embed(
    ["Follow the white rabbit."],
    pooling_params=PoolingParams(dimensions=32),
)
print(outputs[0].outputs)
```

A code example can be found here: [examples/pooling/embed/embed\_matryoshka\_fy\_offline.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/embed/embed_matryoshka_fy_offline.py)

#### Online Inference[¶](#online-inference "Permanent link")

Use the following command to start the vLLM server.

```
vllmservejinaai/jina-embeddings-v3--trust-remote-code
```

You can change the output dimensions of embedding models that support Matryoshka Embeddings by using the dimensions parameter.

```
curlhttp://127.0.0.1:8000/v1/embeddings\
-H'accept: application/json'\
-H'Content-Type: application/json'\
-d'{
    "input": "Follow the white rabbit.",
    "model": "jinaai/jina-embeddings-v3",
    "encoding_format": "float",
    "dimensions": 32
  }'
```

Expected output:

```
{"id":"embd-5c21fc9a5c9d4384a1b021daccaf9f64","object":"list","created":1745476417,"model":"jinaai/jina-embeddings-v3","data":[{"index":0,"object":"embedding","embedding":[-0.3828125,-0.1357421875,0.03759765625,0.125,0.21875,0.09521484375,-0.003662109375,0.1591796875,-0.130859375,-0.0869140625,-0.1982421875,0.1689453125,-0.220703125,0.1728515625,-0.2275390625,-0.0712890625,-0.162109375,-0.283203125,-0.055419921875,-0.0693359375,0.031982421875,-0.04052734375,-0.2734375,0.1826171875,-0.091796875,0.220703125,0.37890625,-0.0888671875,-0.12890625,-0.021484375,-0.0091552734375,0.23046875]}],"usage":{"prompt_tokens":8,"total_tokens":8,"completion_tokens":0,"prompt_tokens_details":null}}
```

An OpenAI client example can be found here: [examples/pooling/embed/openai\_embedding\_matryoshka\_fy\_client.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/embed/openai_embedding_matryoshka_fy_client.py)

## Removed Features[¶](#removed-features "Permanent link")

### Remove `normalize` from PoolingParams[¶](#remove-normalize-from-poolingparams "Permanent link")

We have already removed `normalize` from PoolingParams, use `use_activation` instead.