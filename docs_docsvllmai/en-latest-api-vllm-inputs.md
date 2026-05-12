---
title: inputs - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/inputs/
source: sitemap
fetched_at: 2026-05-07T21:21:57.478129542-03:00
rendered_js: false
word_count: 1158
summary: This document defines the schema and data structures used for processing model inputs, including prompts, multimodal data, and token embeddings, within the vLLM engine.
tags:
    - vllm
    - input-schema
    - prompt-types
    - multimodal-data
    - embeddings
    - data-structures
category: reference
---

Modules:

Name Description `engine`

Schema and utilities for inputs to the engine client (`LLMEngine`/`AsyncLLM`).

`llm`

Schema and utilities for input prompts to the LLM API.

`preprocess`

## DecoderOnlyEngineInput `module-attribute` [¶](#vllm.inputs.DecoderOnlyEngineInput "Permanent link")

A rendered [`DecoderOnlyPrompt`](https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/#vllm.inputs.llm.DecoderOnlyPrompt "            DecoderOnlyPrompt            module-attribute   ") which can be passed to `LLMEngine.add_request` or `AsyncLLM.add_request`.

## EngineInput `module-attribute` [¶](#vllm.inputs.EngineInput "Permanent link")

A rendered [`PromptType`](https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/#vllm.inputs.llm.PromptType "            PromptType            module-attribute   ") which can be passed to `LLMEngine.add_request` or `AsyncLLM.add_request`.

## ModalityData `module-attribute` [¶](#vllm.inputs.ModalityData "Permanent link")

Either a single data item, or a list of data items. Can only be None if UUID is provided.

The number of data items allowed per modality is restricted by `--limit-mm-per-prompt`.

## MultiModalDataDict `module-attribute` [¶](#vllm.inputs.MultiModalDataDict "Permanent link")

A dictionary containing an entry for each modality type to input.

The built-in modalities are defined by [`MultiModalDataBuiltins`](https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/#vllm.inputs.llm.MultiModalDataBuiltins "            MultiModalDataBuiltins").

## MultiModalHashes `module-attribute` [¶](#vllm.inputs.MultiModalHashes "Permanent link")

A dictionary containing per-item hashes for each modality.

## MultiModalPlaceholders `module-attribute` [¶](#vllm.inputs.MultiModalPlaceholders "Permanent link")

A dictionary containing per-item placeholder ranges for each modality.

## MultiModalUUIDDict `module-attribute` [¶](#vllm.inputs.MultiModalUUIDDict "Permanent link")

A dictionary containing user-provided UUIDs for items in each modality. If a UUID for an item is not provided, its entry will be `None` and MultiModalHasher will compute a hash for the item.

The UUID will be used to identify the item for all caching purposes (input processing caching, embedding caching, prefix caching, etc).

## PromptType `module-attribute` [¶](#vllm.inputs.PromptType "Permanent link")

Schema for any prompt, regardless of model type.

This is the input format accepted by most [`LLM`](https://docs.vllm.ai/en/latest/api/vllm/entrypoints/llm/#vllm.entrypoints.llm.LLM "            LLM") APIs.

## SingletonInput `module-attribute` [¶](#vllm.inputs.SingletonInput "Permanent link")

A rendered [`SingletonPrompt`](https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/#vllm.inputs.llm.SingletonPrompt "            SingletonPrompt            module-attribute   ") which can be passed to `LLMEngine.add_request` or `AsyncLLM.add_request`.

## SingletonPrompt `module-attribute` [¶](#vllm.inputs.SingletonPrompt "Permanent link")

Schema for a single prompt. This is as opposed to a data structure which encapsulates multiple prompts, such as [`ExplicitEncoderDecoderPrompt`](https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/#vllm.inputs.llm.ExplicitEncoderDecoderPrompt "            ExplicitEncoderDecoderPrompt").

## DataPrompt [¶](#vllm.inputs.DataPrompt "Permanent link")

Bases: `_PromptOptions`

Represents generic inputs that are converted to [`PromptType`](https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/#vllm.inputs.llm.PromptType "            PromptType            module-attribute   ") by IO processor plugins.

Source code in `vllm/inputs/llm.py`

```
classDataPrompt(_PromptOptions):
"""
    Represents generic inputs that are converted to
    [`PromptType`][vllm.inputs.llm.PromptType] by IO processor plugins.
    """

    data: Any
"""The input data."""

    data_format: str
"""The input data format."""
```

### data `instance-attribute` [¶](#vllm.inputs.DataPrompt.data "Permanent link")

The input data.

### data\_format `instance-attribute` [¶](#vllm.inputs.DataPrompt.data_format "Permanent link")

The input data format.

## EmbedsInput [¶](#vllm.inputs.EmbedsInput "Permanent link")

Bases: `_InputOptions`

Represents embeddings-based input to the engine.

Source code in `vllm/inputs/engine.py`

```
classEmbedsInput(_InputOptions):
"""Represents embeddings-based input to the engine."""

    type: Literal["embeds"]
"""The type of input."""

    prompt_embeds: "torch.Tensor"
"""The embeddings of the prompt."""

    prompt: NotRequired[str]
"""The prompt text corresponding to the token IDs, if available."""

    prompt_token_ids: NotRequired[list[int]]
"""Token IDs of the rendered prompt. Only set for mixed-mode inputs
    (chat completion with `prompt_embeds` content parts). When present,
    `is_token_ids` MUST also be present and have the same length. 
    For pure-embeds inputs this field is absent."""

    is_token_ids: NotRequired[list[bool]]
"""Per-position mask for mixed-mode inputs. `True` means the position
    is a real token ID (use the model's embedding layer); `False` means
    the position uses a pre-computed embedding row from `prompt_embeds`.
    Length MUST equal `len(prompt_token_ids)`.
    For pure-embeds inputs this field is absent."""
```

### is\_token\_ids `instance-attribute` [¶](#vllm.inputs.EmbedsInput.is_token_ids "Permanent link")

Per-position mask for mixed-mode inputs. `True` means the position is a real token ID (use the model's embedding layer); `False` means the position uses a pre-computed embedding row from `prompt_embeds`. Length MUST equal `len(prompt_token_ids)`. For pure-embeds inputs this field is absent.

### prompt `instance-attribute` [¶](#vllm.inputs.EmbedsInput.prompt "Permanent link")

The prompt text corresponding to the token IDs, if available.

### prompt\_embeds `instance-attribute` [¶](#vllm.inputs.EmbedsInput.prompt_embeds "Permanent link")

The embeddings of the prompt.

### prompt\_token\_ids `instance-attribute` [¶](#vllm.inputs.EmbedsInput.prompt_token_ids "Permanent link")

Token IDs of the rendered prompt. Only set for mixed-mode inputs (chat completion with `prompt_embeds` content parts). When present, `is_token_ids` MUST also be present and have the same length. For pure-embeds inputs this field is absent.

### type `instance-attribute` [¶](#vllm.inputs.EmbedsInput.type "Permanent link")

The type of input.

## EmbedsPrompt [¶](#vllm.inputs.EmbedsPrompt "Permanent link")

Bases: `_PromptOptions`

Schema for a prompt provided via token embeddings.

Source code in `vllm/inputs/llm.py`

```
classEmbedsPrompt(_PromptOptions):
"""Schema for a prompt provided via token embeddings."""

    prompt_embeds: "torch.Tensor"
"""The embeddings of the prompt."""

    prompt: NotRequired[str]
"""The prompt text corresponding to the token embeddings, if available."""

    prompt_token_ids: NotRequired[list[int]]
"""Token IDs for mixed-mode inputs (chat completion with
    `prompt_embeds` content parts). The tokens at positions where 
    `prompt_is_token_ids` is `False` are placeholder tokens that 
    get replaced by entries from `prompt_embeds` in the forward pass."""

    prompt_is_token_ids: NotRequired[list[bool]]
"""Per-position mask, `True` uses the real token ID, `False` uses
    the corresponding entry from `prompt_embeds`. 
    Must be the same length as `prompt_token_ids` when both are set."""
```

### prompt `instance-attribute` [¶](#vllm.inputs.EmbedsPrompt.prompt "Permanent link")

The prompt text corresponding to the token embeddings, if available.

### prompt\_embeds `instance-attribute` [¶](#vllm.inputs.EmbedsPrompt.prompt_embeds "Permanent link")

The embeddings of the prompt.

### prompt\_is\_token\_ids `instance-attribute` [¶](#vllm.inputs.EmbedsPrompt.prompt_is_token_ids "Permanent link")

Per-position mask, `True` uses the real token ID, `False` uses the corresponding entry from `prompt_embeds`. Must be the same length as `prompt_token_ids` when both are set.

### prompt\_token\_ids `instance-attribute` [¶](#vllm.inputs.EmbedsPrompt.prompt_token_ids "Permanent link")

Token IDs for mixed-mode inputs (chat completion with `prompt_embeds` content parts). The tokens at positions where `prompt_is_token_ids` is `False` are placeholder tokens that get replaced by entries from `prompt_embeds` in the forward pass.

## EncoderDecoderInput [¶](#vllm.inputs.EncoderDecoderInput "Permanent link")

Bases: `TypedDict`

A rendered [`EncoderDecoderPrompt`](https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/#vllm.inputs.llm.EncoderDecoderPrompt "            EncoderDecoderPrompt            module-attribute   ") which can be passed to `LLMEngine.add_request` or `AsyncLLM.add_request`.

Source code in `vllm/inputs/engine.py`

```
classEncoderDecoderInput(TypedDict):
"""
    A rendered [`EncoderDecoderPrompt`][vllm.inputs.llm.EncoderDecoderPrompt]
    which can be passed to `LLMEngine.add_request` or `AsyncLLM.add_request`.
    """

    type: Literal["enc_dec"]

    encoder_prompt: EncoderInput
"""The inputs for the encoder portion."""

    decoder_prompt: DecoderEngineInput
"""The inputs for the decoder portion."""

    arrival_time: NotRequired[float]
"""The time when the input was received (before rendering)."""
```

### arrival\_time `instance-attribute` [¶](#vllm.inputs.EncoderDecoderInput.arrival_time "Permanent link")

The time when the input was received (before rendering).

### decoder\_prompt `instance-attribute` [¶](#vllm.inputs.EncoderDecoderInput.decoder_prompt "Permanent link")

The inputs for the decoder portion.

### encoder\_prompt `instance-attribute` [¶](#vllm.inputs.EncoderDecoderInput.encoder_prompt "Permanent link")

The inputs for the encoder portion.

## ExplicitEncoderDecoderPrompt [¶](#vllm.inputs.ExplicitEncoderDecoderPrompt "Permanent link")

Bases: `TypedDict`

Schema for a pair of encoder and decoder singleton prompts.

Note

This schema is not valid for decoder-only models.

Source code in `vllm/inputs/llm.py`

```
classExplicitEncoderDecoderPrompt(TypedDict):
"""
    Schema for a pair of encoder and decoder singleton prompts.

    Note:
        This schema is not valid for decoder-only models.
    """

    encoder_prompt: EncoderPrompt
"""The prompt for the encoder part of the model."""

    decoder_prompt: DecoderPrompt | None
"""
    The prompt for the decoder part of the model.

    Passing `None` will cause the prompt to be inferred automatically.
    """
```

### decoder\_prompt `instance-attribute` [¶](#vllm.inputs.ExplicitEncoderDecoderPrompt.decoder_prompt "Permanent link")

The prompt for the decoder part of the model.

Passing `None` will cause the prompt to be inferred automatically.

### encoder\_prompt `instance-attribute` [¶](#vllm.inputs.ExplicitEncoderDecoderPrompt.encoder_prompt "Permanent link")

The prompt for the encoder part of the model.

## MultiModalDataBuiltins [¶](#vllm.inputs.MultiModalDataBuiltins "Permanent link")

Bases: `TypedDict`

Type annotations for modality types predefined by vLLM.

Source code in `vllm/inputs/llm.py`

```
@final
classMultiModalDataBuiltins(TypedDict, total=False):
"""Type annotations for modality types predefined by vLLM."""

    image: ModalityData["ImageItem"]
"""The input image(s)."""

    video: ModalityData["VideoItem"]
"""The input video(s)."""

    audio: ModalityData["AudioItem"]
"""The input audio(s)."""

    vision_chunk: ModalityData["VisionChunk"]
"""The input visual atom(s) - unified modality for images and video chunks."""
```

### audio `instance-attribute` [¶](#vllm.inputs.MultiModalDataBuiltins.audio "Permanent link")

The input audio(s).

### image `instance-attribute` [¶](#vllm.inputs.MultiModalDataBuiltins.image "Permanent link")

The input image(s).

### video `instance-attribute` [¶](#vllm.inputs.MultiModalDataBuiltins.video "Permanent link")

The input video(s).

### vision\_chunk `instance-attribute` [¶](#vllm.inputs.MultiModalDataBuiltins.vision_chunk "Permanent link")

The input visual atom(s) - unified modality for images and video chunks.

## MultiModalEncDecInput [¶](#vllm.inputs.MultiModalEncDecInput "Permanent link")

Bases: `MultiModalInput`

Represents multi-modal input to the engine for encoder-decoder models.

Note

Even text-only encoder-decoder models are currently implemented as multi-modal models for convenience. (Example: https://github.com/vllm-project/bart-plugin)

Source code in `vllm/inputs/engine.py`

```
classMultiModalEncDecInput(MultiModalInput):
"""
    Represents multi-modal input to the engine for encoder-decoder models.

    Note:
        Even text-only encoder-decoder models are currently implemented
        as multi-modal models for convenience.
        (Example: https://github.com/vllm-project/bart-plugin)
    """

    encoder_prompt_token_ids: list[int]
"""The processed token IDs of the encoder prompt."""

    encoder_prompt: NotRequired[str]
"""The prompt text corresponding to the encoder token IDs, if available."""
```

### encoder\_prompt `instance-attribute` [¶](#vllm.inputs.MultiModalEncDecInput.encoder_prompt "Permanent link")

The prompt text corresponding to the encoder token IDs, if available.

### encoder\_prompt\_token\_ids `instance-attribute` [¶](#vllm.inputs.MultiModalEncDecInput.encoder_prompt_token_ids "Permanent link")

```
encoder_prompt_token_ids: list[int]
```

The processed token IDs of the encoder prompt.

## MultiModalInput [¶](#vllm.inputs.MultiModalInput "Permanent link")

Bases: `_InputOptions`

Represents multi-modal input to the engine.

Source code in `vllm/inputs/engine.py`

```
classMultiModalInput(_InputOptions):
"""Represents multi-modal input to the engine."""

    type: Literal["multimodal"]
"""The type of input."""

    prompt_token_ids: list[int]
"""The processed token IDs which includes placeholder tokens."""

    prompt: NotRequired[str]
"""The prompt text corresponding to the token IDs, if available."""

    mm_kwargs: "MultiModalKwargsOptionalItems"
"""Keyword arguments to be directly passed to the model after batching."""

    mm_hashes: MultiModalHashes
"""The hashes of the multi-modal data."""

    mm_placeholders: MultiModalPlaceholders
"""
    For each modality, information about the placeholder tokens in
    `prompt_token_ids`.
    """
```

### mm\_hashes `instance-attribute` [¶](#vllm.inputs.MultiModalInput.mm_hashes "Permanent link")

The hashes of the multi-modal data.

### mm\_kwargs `instance-attribute` [¶](#vllm.inputs.MultiModalInput.mm_kwargs "Permanent link")

```
mm_kwargs: MultiModalKwargsOptionalItems
```

Keyword arguments to be directly passed to the model after batching.

### mm\_placeholders `instance-attribute` [¶](#vllm.inputs.MultiModalInput.mm_placeholders "Permanent link")

For each modality, information about the placeholder tokens in `prompt_token_ids`.

### prompt `instance-attribute` [¶](#vllm.inputs.MultiModalInput.prompt "Permanent link")

The prompt text corresponding to the token IDs, if available.

### prompt\_token\_ids `instance-attribute` [¶](#vllm.inputs.MultiModalInput.prompt_token_ids "Permanent link")

The processed token IDs which includes placeholder tokens.

### type `instance-attribute` [¶](#vllm.inputs.MultiModalInput.type "Permanent link")

The type of input.

## TextPrompt [¶](#vllm.inputs.TextPrompt "Permanent link")

Bases: `_PromptOptions`

Schema for a text prompt.

Source code in `vllm/inputs/llm.py`

```
classTextPrompt(_PromptOptions):
"""Schema for a text prompt."""

    prompt: str
"""The input text to be tokenized before passing to the model."""
```

### prompt `instance-attribute` [¶](#vllm.inputs.TextPrompt.prompt "Permanent link")

The input text to be tokenized before passing to the model.

## TokensInput [¶](#vllm.inputs.TokensInput "Permanent link")

Bases: `_InputOptions`

Represents token-based input to the engine.

Source code in `vllm/inputs/engine.py`

```
classTokensInput(_InputOptions):
"""Represents token-based input to the engine."""

    type: Literal["token"]
"""The type of input."""

    prompt_token_ids: list[int]
"""The token IDs of the prompt."""

    prompt: NotRequired[str]
"""The prompt text corresponding to the token IDs, if available."""
```

### prompt `instance-attribute` [¶](#vllm.inputs.TokensInput.prompt "Permanent link")

The prompt text corresponding to the token IDs, if available.

### prompt\_token\_ids `instance-attribute` [¶](#vllm.inputs.TokensInput.prompt_token_ids "Permanent link")

The token IDs of the prompt.

### type `instance-attribute` [¶](#vllm.inputs.TokensInput.type "Permanent link")

The type of input.

## TokensPrompt [¶](#vllm.inputs.TokensPrompt "Permanent link")

Bases: `_PromptOptions`

Schema for a tokenized prompt.

Source code in `vllm/inputs/llm.py`

```
classTokensPrompt(_PromptOptions):
"""Schema for a tokenized prompt."""

    prompt_token_ids: list[int]
"""A list of token IDs to pass to the model."""

    prompt: NotRequired[str]
"""The prompt text corresponding to the token IDs, if available."""

    token_type_ids: NotRequired[list[int]]
"""A list of token type IDs to pass to the cross encoder model."""
```

### prompt `instance-attribute` [¶](#vllm.inputs.TokensPrompt.prompt "Permanent link")

The prompt text corresponding to the token IDs, if available.

### prompt\_token\_ids `instance-attribute` [¶](#vllm.inputs.TokensPrompt.prompt_token_ids "Permanent link")

A list of token IDs to pass to the model.

### token\_type\_ids `instance-attribute` [¶](#vllm.inputs.TokensPrompt.token_type_ids "Permanent link")

A list of token type IDs to pass to the cross encoder model.

## embeds\_input [¶](#vllm.inputs.embeds_input "Permanent link")

```
embeds_input(
    prompt_embeds: Tensor,
    *,
    prompt: str | None = None,
    cache_salt: str | None = None,
    prompt_token_ids: list[int] | None = None,
    is_token_ids: list[bool] | None = None,
) -> EmbedsInput
```

Construct [`EmbedsInput`](https://docs.vllm.ai/en/latest/api/vllm/inputs/engine/#vllm.inputs.engine.EmbedsInput "            EmbedsInput") from optional values.

Source code in `vllm/inputs/engine.py`

```
defembeds_input(
    prompt_embeds: "torch.Tensor",
    *,
    prompt: str | None = None,
    cache_salt: str | None = None,
    prompt_token_ids: list[int] | None = None,
    is_token_ids: list[bool] | None = None,
) -> EmbedsInput:
"""
    Construct [`EmbedsInput`][vllm.inputs.engine.EmbedsInput]
    from optional values.
    """
    inputs = EmbedsInput(type="embeds", prompt_embeds=prompt_embeds)

    if prompt is not None:
        inputs["prompt"] = prompt
    if cache_salt is not None:
        inputs["cache_salt"] = cache_salt
    if prompt_token_ids is not None:
        inputs["prompt_token_ids"] = prompt_token_ids
    if is_token_ids is not None:
        inputs["is_token_ids"] = is_token_ids

    return inputs
```

## tokens\_input [¶](#vllm.inputs.tokens_input "Permanent link")

```
tokens_input(
    prompt_token_ids: list[int],
    *,
    prompt: str | None = None,
    cache_salt: str | None = None,
) -> TokensInput
```

Construct [`TokensInput`](https://docs.vllm.ai/en/latest/api/vllm/inputs/engine/#vllm.inputs.engine.TokensInput "            TokensInput") from optional values.

Source code in `vllm/inputs/engine.py`

```
deftokens_input(
    prompt_token_ids: list[int],
    *,
    prompt: str | None = None,
    cache_salt: str | None = None,
) -> TokensInput:
"""
    Construct [`TokensInput`][vllm.inputs.engine.TokensInput]
    from optional values.
    """
    inputs = TokensInput(type="token", prompt_token_ids=prompt_token_ids)

    if prompt is not None:
        inputs["prompt"] = prompt
    if cache_salt is not None:
        inputs["cache_salt"] = cache_salt

    return inputs
```