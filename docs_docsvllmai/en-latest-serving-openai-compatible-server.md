---
title: OpenAI-Compatible Server - vLLM
url: https://docs.vllm.ai/en/latest/serving/openai_compatible_server/
source: sitemap
fetched_at: 2026-05-07T21:15:13.161499416-03:00
rendered_js: false
word_count: 2019
summary: This document explains how to use vLLM's HTTP server to deploy models using OpenAI-compatible APIs and custom endpoints, including guidance on chat templates and server configuration.
tags:
    - vllm
    - openai-api
    - model-serving
    - inference
    - chat-template
    - http-server
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/serving/openai_compatible_server.md "Edit this page")

vLLM provides an HTTP server that implements OpenAI's [Completions API](https://platform.openai.com/docs/api-reference/completions), [Chat API](https://platform.openai.com/docs/api-reference/chat), and more! This functionality lets you serve models and interact with them using an HTTP client.

In your terminal, you can [install](https://docs.vllm.ai/en/latest/getting_started/installation/) vLLM, then start the server with the [`vllm serve`](https://docs.vllm.ai/en/latest/configuration/serve_args/) command. (You can also use our [Docker](https://docs.vllm.ai/en/latest/deployment/docker/) image.)

```
vllmserveNousResearch/Meta-Llama-3-8B-Instruct\
--dtypeauto\
--api-keytoken-abc123
```

To call the server, in your preferred text editor, create a script that uses an HTTP client. Include any messages that you want to send to the model. Then run that script. Below is an example script using the [official OpenAI Python client](https://github.com/openai/openai-python).

Code

```
fromopenaiimport OpenAI
client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="token-abc123",
)

completion = client.chat.completions.create(
    model="NousResearch/Meta-Llama-3-8B-Instruct",
    messages=[
        {"role": "user", "content": "Hello!"},
    ],
)

print(completion.choices[0].message)
```

Tip

vLLM supports some parameters that are not supported by OpenAI, `top_k` for example. You can pass these parameters to vLLM using the OpenAI client in the `extra_body` parameter of your requests, i.e. `extra_body={"top_k": 50}` for `top_k`.

Important

By default, the server applies `generation_config.json` from the Hugging Face model repository if it exists. This means the default values of certain sampling parameters can be overridden by those recommended by the model creator.

To disable this behavior, please pass `--generation-config vllm` when launching the server.

## Supported APIs[¶](#supported-apis "Permanent link")

We currently support the following OpenAI APIs:

- [Completions API](#completions-api) (`/v1/completions`)
  
  - Only applicable to [text generation models](https://docs.vllm.ai/en/latest/models/generative_models/).
  - *Note: `suffix` parameter is not supported.*
- [Responses API](#responses-api) (`/v1/responses`)
  
  - Only applicable to [text generation models](https://docs.vllm.ai/en/latest/models/generative_models/).
- [Chat Completions API](#chat-api) (`/v1/chat/completions`)
  
  - Only applicable to [text generation models](https://docs.vllm.ai/en/latest/models/generative_models/) with a [chat template](https://docs.vllm.ai/en/latest/serving/openai_compatible_server/#chat-template).
  - *Note: `user` parameter is ignored.*
  - *Note:* Setting the `parallel_tool_calls` parameter to `false` ensures vLLM only returns zero or one tool call per request. Setting it to `true` (the default) allows returning more than one tool call per request. There is no guarantee more than one tool call will be returned if this is set to `true`, as that behavior is model dependent and not all models are designed to support parallel tool calls.
- [Embeddings API](https://docs.vllm.ai/en/latest/models/pooling_models/embed/#openai-compatible-embeddings-api) (`/v1/embeddings`)
  
  - Only applicable to [embedding models](https://docs.vllm.ai/en/latest/models/pooling_models/embed/).
- [Transcriptions API](#transcriptions-api) (`/v1/audio/transcriptions`)
  
  - Only applicable to [Automatic Speech Recognition (ASR) models](https://docs.vllm.ai/en/latest/models/supported_models/#transcription).
- [Translation API](#translations-api) (`/v1/audio/translations`)
  
  - Only applicable to [Automatic Speech Recognition (ASR) models](https://docs.vllm.ai/en/latest/models/supported_models/#transcription).
- [Realtime API](#realtime-api) (`/v1/realtime`)
  
  - Only applicable to [Automatic Speech Recognition (ASR) models](https://docs.vllm.ai/en/latest/models/supported_models/#realtime-transcription).

In addition, we have the following custom APIs:

- [Tokenizer API](#tokenizer-api) (`/tokenize`, `/detokenize`)
  
  - Applicable to any model with a tokenizer.
- [pooling API](https://docs.vllm.ai/en/latest/models/pooling_models/#pooling-api) (`/pooling`)
  
  - Applicable to all [pooling models](https://docs.vllm.ai/en/latest/models/pooling_models/).
- [Classification API](https://docs.vllm.ai/en/latest/models/pooling_models/classify/#classification-api) (`/classify`)
  
  - Only applicable to [classification models](https://docs.vllm.ai/en/latest/models/pooling_models/classify/).
- [Cohere Embed API](https://docs.vllm.ai/en/latest/models/pooling_models/embed/#cohere-embed-api) (`/v2/embed`)
  
  - Compatible with [Cohere's Embed API](https://docs.cohere.com/reference/embed)
  - Works with any [embedding model](https://docs.vllm.ai/en/latest/models/pooling_models/embed/#supported-models), including multimodal models.
- [Score API](https://docs.vllm.ai/en/latest/models/pooling_models/scoring/#score-api) (`/score`, `/v1/score`)
  
  - Applicable to [score models](https://docs.vllm.ai/en/latest/models/pooling_models/scoring/) (cross-encoder, bi-encoder, late-interaction).
- [Generative Scoring API](#generative-scoring-api) (`/generative_scoring`)
  
  - Applicable to [CausalLM models](https://docs.vllm.ai/en/latest/models/generative_models/) (task `"generate"`).
  - Computes next-token probabilities for specified `label_token_ids`.
- [Rerank API](https://docs.vllm.ai/en/latest/models/pooling_models/scoring/#rerank-api) (`/rerank`, `/v1/rerank`, `/v2/rerank`)
  
  - Implements [Jina AI's v1 rerank API](https://jina.ai/reranker/)
  - Also compatible with [Cohere's v1 & v2 rerank APIs](https://docs.cohere.com/v2/reference/rerank)
  - Jina and Cohere's APIs are very similar; Jina's includes extra information in the rerank endpoint's response.

## Chat Template[¶](#chat-template "Permanent link")

In order for the language model to support chat protocol, vLLM requires the model to include a chat template in its tokenizer configuration. The chat template is a Jinja2 template that specifies how roles, messages, and other chat-specific tokens are encoded in the input.

An example chat template for `NousResearch/Meta-Llama-3-8B-Instruct` can be found [here](https://llama.com/docs/model-cards-and-prompt-formats/meta-llama-3/#prompt-template-for-meta-llama-3)

Some models do not provide a chat template even though they are instruction/chat fine-tuned. For those models, you can manually specify their chat template in the `--chat-template` parameter with the file path to the chat template, or the template in string form. Without a chat template, the server will not be able to process chat and all chat requests will error.

```
vllmserve<model>--chat-template./path-to-chat-template.jinja
```

vLLM community provides a set of chat templates for popular models. You can find them under the [examples](https://github.com/vllm-project/vllm/tree/main/examples) directory.

With the inclusion of multi-modal chat APIs, the OpenAI spec now accepts chat messages in a new format which specifies both a `type` and a `text` field. An example is provided below:

```
completion = client.chat.completions.create(
    model="NousResearch/Meta-Llama-3-8B-Instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Classify this sentiment: vLLM is wonderful!"},
            ],
        },
    ],
)
```

Most chat templates for LLMs expect the `content` field to be a string, but there are some newer models like `meta-llama/Llama-Guard-3-1B` that expect the content to be formatted according to the OpenAI schema in the request. vLLM provides best-effort support to detect this automatically, which is logged as a string like *"Detected the chat template content format to be..."*, and internally converts incoming requests to match the detected format, which can be one of:

- `"string"`: A string.
  
  - Example: `"Hello world"`
- `"openai"`: A list of dictionaries, similar to OpenAI schema.
  
  - Example: `[{"type": "text", "text": "Hello world!"}]`

If the result is not what you expect, you can set the `--chat-template-content-format` CLI argument to override which format to use.

vLLM supports a set of parameters that are not part of the OpenAI API. In order to use them, you can pass them as extra parameters in the OpenAI client. Or directly merge them into the JSON payload if you are using HTTP call directly.

```
completion = client.chat.completions.create(
    model="NousResearch/Meta-Llama-3-8B-Instruct",
    messages=[
        {"role": "user", "content": "Classify this sentiment: vLLM is wonderful!"},
    ],
    extra_body={
        "structured_outputs": {"choice": ["positive", "negative"]},
    },
)
```

Only `X-Request-Id` HTTP request header is supported for now. It can be enabled with `--enable-request-id-headers`.

Code

```
completion = client.chat.completions.create(
    model="NousResearch/Meta-Llama-3-8B-Instruct",
    messages=[
        {"role": "user", "content": "Classify this sentiment: vLLM is wonderful!"},
    ],
    extra_headers={
        "x-request-id": "sentiment-classification-00001",
    },
)
print(completion._request_id)

completion = client.completions.create(
    model="NousResearch/Meta-Llama-3-8B-Instruct",
    prompt="A robot may not injure a human being",
    extra_headers={
        "x-request-id": "completion-test",
    },
)
print(completion._request_id)
```

## Offline API Documentation[¶](#offline-api-documentation "Permanent link")

The FastAPI `/docs` endpoint requires an internet connection by default. To enable offline access in air-gapped environments, use the `--enable-offline-docs` flag:

```
vllmserveNousResearch/Meta-Llama-3-8B-Instruct--enable-offline-docs
```

## API Reference[¶](#api-reference "Permanent link")

### Completions API[¶](#completions-api "Permanent link")

Our Completions API is compatible with [OpenAI's Completions API](https://platform.openai.com/docs/api-reference/completions); you can use the [official OpenAI Python client](https://github.com/openai/openai-python) to interact with it.

Code example: [examples/basic/online\_serving/openai\_completion\_client.py](https://github.com/vllm-project/vllm/blob/main/examples/basic/online_serving/openai_completion_client.py)

The following [sampling parameters](https://docs.vllm.ai/en/latest/api/#inference-parameters) are supported.

Code

```
    use_beam_search: bool = False
    top_k: int | None = None
    min_p: float | None = None
    repetition_penalty: float | None = None
    length_penalty: float = 1.0
    stop_token_ids: list[int] | None = []
    include_stop_str_in_output: bool = False
    ignore_eos: bool = False
    min_tokens: int = 0
    skip_special_tokens: bool = True
    spaces_between_special_tokens: bool = True
    truncate_prompt_tokens: Annotated[int, Field(ge=-1, le=_INT64_MAX)] | None = None
    allowed_token_ids: list[int] | None = None
    prompt_logprobs: int | None = None
```

The following extra parameters are supported:

Code

```
    prompt_embeds: bytes | list[bytes] | None = None
    add_special_tokens: bool = Field(
        default=True,
        description=(
            "If true (the default), special tokens (e.g. BOS) will be added to "
            "the prompt."
        ),
    )
    response_format: AnyResponseFormat | None = Field(
        default=None,
        description=(
            "Similar to chat completion, this parameter specifies the format "
            "of output. Only {'type': 'json_object'}, {'type': 'json_schema'}"
            ", {'type': 'structural_tag'}, or {'type': 'text' } is supported."
        ),
    )
    structured_outputs: StructuredOutputsParams | None = Field(
        default=None,
        description="Additional kwargs for structured outputs",
    )
    priority: int = Field(
        default=0,
        ge=_INT64_MIN,
        le=_INT64_MAX,
        description=(
            "The priority of the request (lower means earlier handling; "
            "default: 0). Any priority other than 0 will raise an error "
            "if the served model does not use priority scheduling."
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

    return_tokens_as_token_ids: bool | None = Field(
        default=None,
        description=(
            "If specified with 'logprobs', tokens are represented "
            " as strings of the form 'token_id:{token_id}' so that tokens "
            "that are not JSON-encodable can be identified."
        ),
    )
    return_token_ids: bool | None = Field(
        default=None,
        description=(
            "If specified, the result will include token IDs alongside the "
            "generated text. In streaming mode, prompt_token_ids is included "
            "only in the first chunk, and token_ids contains the delta tokens "
            "for each chunk. This is useful for debugging or when you "
            "need to map generated text back to input tokens."
        ),
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

    kv_transfer_params: dict[str, Any] | None = Field(
        default=None,
        description="KVTransfer parameters used for disaggregated serving.",
    )

    vllm_xargs: dict[str, str | int | float] | None = Field(
        default=None,
        description=(
            "Additional request parameters with string or "
            "numeric values, used by custom extensions."
        ),
    )

    repetition_detection: RepetitionDetectionParams | None = Field(
        default=None,
        description="Parameters for detecting repetitive N-gram patterns "
        "in output tokens. If such repetition is detected, generation will "
        "be ended early. LLMs can sometimes generate repetitive, unhelpful "
        "token patterns, stopping only when they hit the maximum output length "
        "(e.g. 'abcdabcdabcd...' or '\\emoji \\emoji \\emoji ...'). This feature "
        "can detect such behavior and terminate early, saving time and tokens.",
    )
```

### Chat API[¶](#chat-api "Permanent link")

Our Chat API is compatible with [OpenAI's Chat Completions API](https://platform.openai.com/docs/api-reference/chat); you can use the [official OpenAI Python client](https://github.com/openai/openai-python) to interact with it.

We support both [Vision](https://platform.openai.com/docs/guides/vision)- and [Audio](https://platform.openai.com/docs/guides/audio?audio-generation-quickstart-example=audio-in)-related parameters; see our [Multimodal Inputs](https://docs.vllm.ai/en/latest/features/multimodal_inputs/) guide for more information.

- *Note: `image_url.detail` parameter is not supported.*

Code example: [examples/basic/online\_serving/openai\_chat\_completion\_client.py](https://github.com/vllm-project/vllm/blob/main/examples/basic/online_serving/openai_chat_completion_client.py)

The following [sampling parameters](https://docs.vllm.ai/en/latest/api/#inference-parameters) are supported.

Code

```
    use_beam_search: bool = False
    top_k: int | None = None
    min_p: float | None = None
    repetition_penalty: float | None = None
    length_penalty: float = 1.0
    stop_token_ids: list[int] | None = []
    include_stop_str_in_output: bool = False
    ignore_eos: bool = False
    min_tokens: int = 0
    skip_special_tokens: bool = True
    spaces_between_special_tokens: bool = True
    truncate_prompt_tokens: Annotated[int, Field(ge=-1, le=_INT64_MAX)] | None = None
    prompt_logprobs: int | None = None
    allowed_token_ids: list[int] | None = None
    bad_words: list[str] = Field(default_factory=list)
```

The following extra parameters are supported:

Code

```
    echo: bool = Field(
        default=False,
        description=(
            "If true, the new message will be prepended with the last message "
            "if they belong to the same role."
        ),
    )
    add_generation_prompt: bool = Field(
        default=True,
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
    documents: list[dict[str, str]] | None = Field(
        default=None,
        description=(
            "A list of dicts representing documents that will be accessible to "
            "the model if it is performing RAG (retrieval-augmented generation)."
            " If the template does not support RAG, this argument will have no "
            "effect. We recommend that each document should be a dict containing "
            '"title" and "text" keys.'
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
    mm_processor_kwargs: dict[str, Any] | None = Field(
        default=None,
        description=("Additional kwargs to pass to the HF processor."),
    )
    structured_outputs: StructuredOutputsParams | None = Field(
        default=None,
        description="Additional kwargs for structured outputs",
    )
    priority: int = Field(
        default=0,
        ge=_INT64_MIN,
        le=_INT64_MAX,
        description=(
            "The priority of the request (lower means earlier handling; "
            "default: 0). Any priority other than 0 will raise an error "
            "if the served model does not use priority scheduling."
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

    return_tokens_as_token_ids: bool | None = Field(
        default=None,
        description=(
            "If specified with 'logprobs', tokens are represented "
            " as strings of the form 'token_id:{token_id}' so that tokens "
            "that are not JSON-encodable can be identified."
        ),
    )
    return_token_ids: bool | None = Field(
        default=None,
        description=(
            "If specified, the result will include token IDs alongside the "
            "generated text. In streaming mode, prompt_token_ids is included "
            "only in the first chunk, and token_ids contains the delta tokens "
            "for each chunk. This is useful for debugging or when you "
            "need to map generated text back to input tokens."
        ),
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

    kv_transfer_params: dict[str, Any] | None = Field(
        default=None,
        description="KVTransfer parameters used for disaggregated serving.",
    )

    vllm_xargs: dict[str, str | int | float | list[str | int | float]] | None = Field(
        default=None,
        description=(
            "Additional request parameters with (list of) string or "
            "numeric values, used by custom extensions."
        ),
    )

    repetition_detection: RepetitionDetectionParams | None = Field(
        default=None,
        description="Parameters for detecting repetitive N-gram patterns "
        "in output tokens. If such repetition is detected, generation will "
        "be ended early. LLMs can sometimes generate repetitive, unhelpful "
        "token patterns, stopping only when they hit the maximum output length "
        "(e.g. 'abcdabcdabcd...' or '\\emoji \\emoji \\emoji ...'). This feature "
        "can detect such behavior and terminate early, saving time and tokens.",
    )
```

### Responses API[¶](#responses-api "Permanent link")

Our Responses API is compatible with [OpenAI's Responses API](https://platform.openai.com/docs/api-reference/responses); you can use the [official OpenAI Python client](https://github.com/openai/openai-python) to interact with it.

Code example: [examples/online\_serving/openai\_responses\_client\_with\_tools.py](https://github.com/vllm-project/vllm/blob/main/examples/tool_calling/openai_responses_client_with_tools.py)

The following extra parameters in the request object are supported:

Code

```
    request_id: str = Field(
        default_factory=lambda: f"resp_{random_uuid()}",
        description=(
            "The request_id related to this request. If the caller does "
            "not set it, a random_uuid will be generated. This id is used "
            "through out the inference process and return in response."
        ),
    )
    media_io_kwargs: dict[str, dict[str, Any]] | None = Field(
        default=None,
        description=(
            "Additional kwargs to pass to the media IO connectors, "
            "keyed by modality. Merged with engine-level media_io_kwargs."
        ),
    )
    mm_processor_kwargs: dict[str, Any] | None = Field(
        default=None,
        description=("Additional kwargs to pass to the HF processor."),
    )
    priority: int = Field(
        default=0,
        ge=_INT64_MIN,
        le=_INT64_MAX,
        description=(
            "The priority of the request (lower means earlier handling; "
            "default: 0). Any priority other than 0 will raise an error "
            "if the served model does not use priority scheduling."
        ),
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

    enable_response_messages: bool = Field(
        default=False,
        description=(
            "Dictates whether or not to return messages as part of the "
            "response object. Currently only supported for non-background."
        ),
    )
    # similar to input_messages / output_messages in ResponsesResponse
    # we take in previous_input_messages (ie in harmony format)
    # this cannot be used in conjunction with previous_response_id
    # TODO: consider supporting non harmony messages as well
    previous_input_messages: list[OpenAIHarmonyMessage | dict] | None = None
    structured_outputs: StructuredOutputsParams | None = Field(
        default=None,
        description="Additional kwargs for structured outputs",
    )

    repetition_penalty: float | None = None
    seed: int | None = Field(None, ge=_INT64_MIN, le=_INT64_MAX)
    stop: str | list[str] | None = []
    ignore_eos: bool = False
    vllm_xargs: dict[str, str | int | float | list[str | int | float]] | None = Field(
        default=None,
        description=(
            "Additional request parameters with (list of) string or "
            "numeric values, used by custom extensions."
        ),
    )
    kv_transfer_params: dict[str, Any] | None = Field(
        default=None,
        description="KVTransfer parameters used for disaggregated serving.",
    )
```

The following extra parameters in the response object are supported:

Code

```
    # These are populated when enable_response_messages is set to True
    # NOTE: custom serialization is needed
    # see serialize_input_messages and serialize_output_messages
    input_messages: ResponseInputOutputMessage | None = Field(
        default=None,
        description=(
            "If enable_response_messages, we can show raw token input to model."
        ),
    )
    output_messages: ResponseInputOutputMessage | None = Field(
        default=None,
        description=(
            "If enable_response_messages, we can show raw token output of model."
        ),
    )
```

### Transcriptions API[¶](#transcriptions-api "Permanent link")

Our Transcriptions API is compatible with [OpenAI's Transcriptions API](https://platform.openai.com/docs/api-reference/audio/createTranscription); you can use the [official OpenAI Python client](https://github.com/openai/openai-python) to interact with it.

Note

To use the Transcriptions API, please install with extra audio dependencies using `pip install vllm[audio]`.

Code example: [examples/speech\_to\_text/openai/openai\_transcription\_client.py](https://github.com/vllm-project/vllm/blob/main/examples/speech_to_text/openai/openai_transcription_client.py)

NOTE: beam search is currently supported in the transcriptions endpoint for encoder-decoder multimodal models, e.g., whisper, but highly inefficient as work for handling the encoder/decoder cache is actively ongoing. This is an active point of ongoing optimization and will be handled properly in the very near future.

#### API Enforced Limits[¶](#api-enforced-limits "Permanent link")

Set the maximum audio file size (in MB) that VLLM will accept, via the `VLLM_MAX_AUDIO_CLIP_FILESIZE_MB` environment variable. Default is 25 MB.

#### Uploading Audio Files[¶](#uploading-audio-files "Permanent link")

The Transcriptions API supports uploading audio files in various formats including FLAC, MP3, MP4, MPEG, MPGA, M4A, OGG, WAV, and WEBM.

**Using OpenAI Python Client:**

Code

```
fromopenaiimport OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="token-abc123",
)

# Upload audio file from disk
with open("audio.mp3", "rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        model="openai/whisper-large-v3-turbo",
        file=audio_file,
        language="en",
        response_format="verbose_json",
    )

print(transcription.text)
```

**Using curl with multipart/form-data:**

Code

```
curl-XPOST"http://localhost:8000/v1/audio/transcriptions"\
-H"Authorization: Bearer token-abc123"\
-F"[email protected]"\
-F"model=openai/whisper-large-v3-turbo"\
-F"language=en"\
-F"response_format=verbose_json"
```

**Supported Parameters:**

- `file`: The audio file to transcribe (required)
- `model`: The model to use for transcription (required)
- `language`: The language code (e.g., "en", "zh") (optional)
- `prompt`: Optional text to guide the transcription style (optional)
- `response_format`: Format of the response ("json", "text") (optional)
- `temperature`: Sampling temperature between 0 and 1 (optional)

For the complete list of supported parameters including sampling parameters and vLLM extensions, see the [protocol definitions](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/protocol.py#L2182).

**Response Format:**

For `verbose_json` response format:

Code

```
{
"text":"Hello, this is a transcription of the audio file.",
"language":"en",
"duration":5.42,
"segments":[
{
"id":0,
"seek":0,
"start":0.0,
"end":2.5,
"text":"Hello, this is a transcription",
"tokens":[50364,938,428,307,275,28347],
"temperature":0.0,
"avg_logprob":-0.245,
"compression_ratio":1.235,
"no_speech_prob":0.012
}
]
}
```

Currently “verbose\_json” response format doesn’t support no\_speech\_prob.

The following [sampling parameters](https://docs.vllm.ai/en/latest/api/#inference-parameters) are supported.

Code

```
    use_beam_search: bool = False
"""Whether or not beam search should be used."""

    n: int = 1
"""The number of beams to be used in beam search."""

    length_penalty: float = 1.0
"""Length penalty to be used for beam search."""

    include_stop_str_in_output: bool = False
"""Whether to include the stop strings in output text."""

    temperature: float = Field(default=0.0)
"""The sampling temperature, between 0 and 1.

    Higher values like 0.8 will make the output more random, while lower values
    like 0.2 will make it more focused / deterministic. If set to 0, the model
    will use [log probability](https://en.wikipedia.org/wiki/Log_probability)
    to automatically increase the temperature until certain thresholds are hit.
    """

    top_p: float | None = None
"""Enables nucleus (top-p) sampling, where tokens are selected from the
    smallest possible set whose cumulative probability exceeds `p`.
    """

    top_k: int | None = None
"""Limits sampling to the `k` most probable tokens at each step."""

    min_p: float | None = None
"""Filters out tokens with a probability lower than `min_p`, ensuring a
    minimum likelihood threshold during sampling.
    """

    seed: int | None = Field(None, ge=_LONG_INFO.min, le=_LONG_INFO.max)
"""The seed to use for sampling."""

    frequency_penalty: float | None = 0.0
"""The frequency penalty to use for sampling."""

    repetition_penalty: float | None = None
"""The repetition penalty to use for sampling."""

    presence_penalty: float | None = 0.0
"""The presence penalty to use for sampling."""

    max_completion_tokens: int | None = None
"""The maximum number of tokens to generate."""
```

The following extra parameters are supported:

Code

```
    # Flattened stream option to simplify form data.
    stream_include_usage: bool | None = False
    stream_continuous_usage_stats: bool | None = False

    vllm_xargs: dict[str, str | int | float | bool] | None = Field(
        default=None,
        description=(
            "Additional request parameters with string or "
            "numeric values, used by custom extensions."
        ),
    )
```

### Translations API[¶](#translations-api "Permanent link")

Our Translation API is compatible with [OpenAI's Translations API](https://platform.openai.com/docs/api-reference/audio/createTranslation); you can use the [official OpenAI Python client](https://github.com/openai/openai-python) to interact with it. Whisper models can translate audio from one of the 55 non-English supported languages into English. Please mind that the popular `openai/whisper-large-v3-turbo` model does not support translating.

Note

To use the Translation API, please install with extra audio dependencies using `pip install vllm[audio]`.

Code example: [examples/speech\_to\_text/openai/openai\_translation\_client.py](https://github.com/vllm-project/vllm/blob/main/examples/speech_to_text/openai/openai_translation_client.py)

The following [sampling parameters](https://docs.vllm.ai/en/latest/api/#inference-parameters) are supported.

```
    use_beam_search: bool = False
"""Whether or not beam search should be used."""

    n: int = 1
"""The number of beams to be used in beam search."""

    length_penalty: float = 1.0
"""Length penalty to be used for beam search."""

    include_stop_str_in_output: bool = False
"""Whether to include the stop strings in output text."""

    seed: int | None = Field(None, ge=_LONG_INFO.min, le=_LONG_INFO.max)
"""The seed to use for sampling."""

    temperature: float = Field(default=0.0)
"""The sampling temperature, between 0 and 1.

    Higher values like 0.8 will make the output more random, while lower values
    like 0.2 will make it more focused / deterministic. If set to 0, the model
    will use [log probability](https://en.wikipedia.org/wiki/Log_probability)
    to automatically increase the temperature until certain thresholds are hit.
    """
```

The following extra parameters are supported:

```
    language: str | None = None
"""The language of the input audio we translate from.

    Supplying the input language in
    [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format
    will improve accuracy.
    """

    hotwords: str | None = None
"""
    hotwords refers to a list of important words or phrases that the model
    should pay extra attention to during transcription.
    """

    to_language: str | None = None
"""The language of the input audio we translate to.

    Please note that this is not supported by all models, refer to the specific
    model documentation for more details.
    For instance, Whisper only supports `to_language=en`.
    """

    stream: bool | None = False
"""Custom field not present in the original OpenAI definition. When set,
    it will enable output to be streamed in a similar fashion as the Chat
    Completion endpoint.
    """
    # Flattened stream option to simplify form data.
    stream_include_usage: bool | None = False
    stream_continuous_usage_stats: bool | None = False

    max_completion_tokens: int | None = None
"""The maximum number of tokens to generate."""
```

### Realtime API[¶](#realtime-api "Permanent link")

The Realtime API provides WebSocket-based streaming audio transcription, allowing real-time speech-to-text as audio is being recorded.

Note

To use the Realtime API, please install with extra audio dependencies using `uv pip install vllm[audio]`.

#### Audio Format[¶](#audio-format "Permanent link")

Audio must be sent as base64-encoded PCM16 audio at 16kHz sample rate, mono channel.

#### Protocol Overview[¶](#protocol-overview "Permanent link")

1. Client connects to `ws://host/v1/realtime`
2. Server sends `session.created` event
3. Client optionally sends `session.update` with model/params
4. Client sends `input_audio_buffer.commit` when ready
5. Client sends `input_audio_buffer.append` events with base64 PCM16 chunks
6. Server sends `transcription.delta` events with incremental text
7. Server sends `transcription.done` with final text + usage
8. Repeat from step 5 for next utterance
9. Optionally, client sends input\_audio\_buffer.commit with final=True to signal audio input is finished. Useful when streaming audio files

#### Client → Server Events[¶](#client-server-events "Permanent link")

Event Description `input_audio_buffer.append` Send base64-encoded audio chunk: `{"type": "input_audio_buffer.append", "audio": "<base64>"}` `input_audio_buffer.commit` Trigger transcription processing or end: `{"type": "input_audio_buffer.commit", "final": bool}` `session.update` Configure session: `{"type": "session.update", "model": "model-name"}`

#### Server → Client Events[¶](#server-client-events "Permanent link")

Event Description `session.created` Connection established with session ID and timestamp `transcription.delta` Incremental transcription text: `{"type": "transcription.delta", "delta": "text"}` `transcription.done` Final transcription with usage stats `error` Error notification with message and optional code

#### Example Clients[¶](#example-clients "Permanent link")

- [openai\_realtime\_client.py](https://github.com/vllm-project/vllm/tree/main/examples/online_serving/openai_realtime_client.py) - Upload and transcribe an audio file
- [openai\_realtime\_microphone\_client.py](https://github.com/vllm-project/vllm/tree/main/examples/online_serving/openai_realtime_microphone_client.py) - Gradio demo for live microphone transcription

### Tokenizer API[¶](#tokenizer-api "Permanent link")

Our Tokenizer API is a simple wrapper over [HuggingFace-style tokenizers](https://huggingface.co/docs/transformers/en/main_classes/tokenizer). It consists of two endpoints:

- `/tokenize` corresponds to calling `tokenizer.encode()`.
- `/detokenize` corresponds to calling `tokenizer.decode()`.

### Generative Scoring API[¶](#generative-scoring-api "Permanent link")

The `/generative_scoring` endpoint uses a CausalLM model (e.g., Llama, Qwen, Mistral) to compute the probability of specified token IDs appearing as the next token. Each item (document) is concatenated with the query to form a prompt, and the model predicts how likely each label token is as the next token after that prompt. This lets you score items against a query — for example, asking "Is this the capital of France?" and scoring each city by how likely the model is to answer "Yes".

This endpoint is automatically available when the server is started with a generative model (task `"generate"`). It is separate from the pooling-based [Score API](https://docs.vllm.ai/en/latest/models/pooling_models/scoring/#score-api), which uses cross-encoder, bi-encoder, or late-interaction models.

**Requirements:**

- The `label_token_ids` parameter is **required** and must contain **at least 1 token ID**.
- When 2 label tokens are provided, the score equals `P(label_token_ids[0]) / (P(label_token_ids[0]) + P(label_token_ids[1]))` (softmax over the two labels).
- When more labels are provided, the score is the softmax-normalized probability of the first label token across all label tokens.

#### Example[¶](#example "Permanent link")

```
curl-XPOSThttp://localhost:8000/generative_scoring\
-H"Content-Type: application/json"\
-d'{
    "model": "Qwen/Qwen3-0.6B",
    "query": "Is this city the capital of France?",
    "items": ["Paris", "London", "Berlin"],
    "label_token_ids": [9454, 2753]
  }'
```

Here, each item is appended to the query to form prompts like `"Is this city the capital of France? Paris"`, `"... London"`, etc. The model then predicts the next token, and the score reflects the probability of "Yes" (token 9454) vs "No" (token 2753).

Response

```
{
"id":"generative-scoring-abc123",
"object":"list",
"created":1234567890,
"model":"Qwen/Qwen3-0.6B",
"data":[
{"index":0,"object":"score","score":0.95},
{"index":1,"object":"score","score":0.12},
{"index":2,"object":"score","score":0.08}
],
"usage":{"prompt_tokens":45,"total_tokens":48,"completion_tokens":3}
}
```

#### How it works[¶](#how-it-works "Permanent link")

1. **Prompt Construction**: For each item, builds `prompt = query + item` (or `item + query` if `item_first=true`)
2. **Forward Pass**: Runs the model on each prompt to get next-token logits
3. **Probability Extraction**: Extracts logprobs for the specified `label_token_ids`
4. **Softmax Normalization**: Applies softmax over only the label tokens (when `apply_softmax=true`)
5. **Score**: Returns the normalized probability of the first label token

#### Finding Token IDs[¶](#finding-token-ids "Permanent link")

To find the token IDs for your labels, use the tokenizer:

```
fromtransformersimport AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-0.6B")
yes_id = tokenizer.encode("Yes", add_special_tokens=False)[0]
no_id = tokenizer.encode("No", add_special_tokens=False)[0]
print(f"Yes: {yes_id}, No: {no_id}")
```

## Ray Serve LLM[¶](#ray-serve-llm "Permanent link")

Ray Serve LLM enables scalable, production-grade serving of the vLLM engine. It integrates tightly with vLLM and extends it with features such as auto-scaling, load balancing, and back-pressure.

Key capabilities:

- Exposes an OpenAI-compatible HTTP API as well as a Pythonic API.
- Scales from a single GPU to a multi-node cluster without code changes.
- Provides observability and autoscaling policies through Ray dashboards and metrics.

The following example shows how to deploy a large model like DeepSeek R1 with Ray Serve LLM: [examples/ray\_serving/ray\_serve\_deepseek.py](https://github.com/vllm-project/vllm/blob/main/examples/ray_serving/ray_serve_deepseek.py).

Learn more about Ray Serve LLM with the official [Ray Serve LLM documentation](https://docs.ray.io/en/latest/serve/llm/index.html).