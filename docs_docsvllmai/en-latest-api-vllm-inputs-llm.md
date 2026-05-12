---
title: llm - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/
source: sitemap
fetched_at: 2026-05-07T21:21:58.607719157-03:00
rendered_js: false
word_count: 847
summary: This document defines the schema and data structures used for constructing LLM input prompts, including specifications for decoder-only, encoder-decoder, and multi-modal models.
tags:
    - vllm
    - llm-input
    - schema-definition
    - multi-modal
    - prompt-engineering
    - token-embeddings
category: reference
---

Schema and utilities for input prompts to the LLM API.

## DecoderOnlyPrompt `module-attribute` [¶](#vllm.inputs.llm.DecoderOnlyPrompt "Permanent link")

Schema of a prompt for a decoder-only model:

- A text prompt (string or [`TextPrompt`](#vllm.inputs.llm.TextPrompt "            TextPrompt"))
- A tokenized prompt (list of token IDs, or [`TokensPrompt`](#vllm.inputs.llm.TokensPrompt "            TokensPrompt"))
- An embeddings prompt ([`EmbedsPrompt`](#vllm.inputs.llm.EmbedsPrompt "            EmbedsPrompt"))

For encoder-decoder models, passing a singleton prompt is shorthand for passing `ExplicitEncoderDecoderPrompt(encoder_prompt=prompt, decoder_prompt=None)`.

## DecoderPrompt `module-attribute` [¶](#vllm.inputs.llm.DecoderPrompt "Permanent link")

Schema of a prompt for the decoder part of an encoder-decoder model:

- A text prompt (string or [`TextPrompt`](#vllm.inputs.llm.TextPrompt "            TextPrompt"))
- A tokenized prompt (list of token IDs, or [`TokensPrompt`](#vllm.inputs.llm.TokensPrompt "            TokensPrompt"))

Note

Multi-modal inputs are not supported for decoder prompts.

## EncoderDecoderPrompt `module-attribute` [¶](#vllm.inputs.llm.EncoderDecoderPrompt "Permanent link")

Schema for a prompt for an encoder-decoder model.

You can pass a singleton encoder prompt, in which case the decoder prompt is considered to be `None` (i.e., infer automatically).

## EncoderPrompt `module-attribute` [¶](#vllm.inputs.llm.EncoderPrompt "Permanent link")

Schema of a prompt for the encoder part of a encoder-decoder model:

- A text prompt (string or [`TextPrompt`](#vllm.inputs.llm.TextPrompt "            TextPrompt"))
- A tokenized prompt (list of token IDs, or [`TokensPrompt`](#vllm.inputs.llm.TokensPrompt "            TokensPrompt"))

## ModalityData `module-attribute` [¶](#vllm.inputs.llm.ModalityData "Permanent link")

Either a single data item, or a list of data items. Can only be None if UUID is provided.

The number of data items allowed per modality is restricted by `--limit-mm-per-prompt`.

## MultiModalDataDict `module-attribute` [¶](#vllm.inputs.llm.MultiModalDataDict "Permanent link")

A dictionary containing an entry for each modality type to input.

The built-in modalities are defined by [`MultiModalDataBuiltins`](#vllm.inputs.llm.MultiModalDataBuiltins "            MultiModalDataBuiltins").

## MultiModalUUIDDict `module-attribute` [¶](#vllm.inputs.llm.MultiModalUUIDDict "Permanent link")

A dictionary containing user-provided UUIDs for items in each modality. If a UUID for an item is not provided, its entry will be `None` and MultiModalHasher will compute a hash for the item.

The UUID will be used to identify the item for all caching purposes (input processing caching, embedding caching, prefix caching, etc).

## PromptType `module-attribute` [¶](#vllm.inputs.llm.PromptType "Permanent link")

Schema for any prompt, regardless of model type.

This is the input format accepted by most [`LLM`](https://docs.vllm.ai/en/latest/api/vllm/entrypoints/llm/#vllm.entrypoints.llm.LLM "            LLM") APIs.

## SingletonPrompt `module-attribute` [¶](#vllm.inputs.llm.SingletonPrompt "Permanent link")

Schema for a single prompt. This is as opposed to a data structure which encapsulates multiple prompts, such as [`ExplicitEncoderDecoderPrompt`](#vllm.inputs.llm.ExplicitEncoderDecoderPrompt "            ExplicitEncoderDecoderPrompt").

## DataPrompt [¶](#vllm.inputs.llm.DataPrompt "Permanent link")

Bases: `_PromptOptions`

Represents generic inputs that are converted to [`PromptType`](#vllm.inputs.llm.PromptType "            PromptType            module-attribute   ") by IO processor plugins.

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

### data `instance-attribute` [¶](#vllm.inputs.llm.DataPrompt.data "Permanent link")

The input data.

### data\_format `instance-attribute` [¶](#vllm.inputs.llm.DataPrompt.data_format "Permanent link")

The input data format.

## EmbedsPrompt [¶](#vllm.inputs.llm.EmbedsPrompt "Permanent link")

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

### prompt `instance-attribute` [¶](#vllm.inputs.llm.EmbedsPrompt.prompt "Permanent link")

The prompt text corresponding to the token embeddings, if available.

### prompt\_embeds `instance-attribute` [¶](#vllm.inputs.llm.EmbedsPrompt.prompt_embeds "Permanent link")

The embeddings of the prompt.

### prompt\_is\_token\_ids `instance-attribute` [¶](#vllm.inputs.llm.EmbedsPrompt.prompt_is_token_ids "Permanent link")

Per-position mask, `True` uses the real token ID, `False` uses the corresponding entry from `prompt_embeds`. Must be the same length as `prompt_token_ids` when both are set.

### prompt\_token\_ids `instance-attribute` [¶](#vllm.inputs.llm.EmbedsPrompt.prompt_token_ids "Permanent link")

Token IDs for mixed-mode inputs (chat completion with `prompt_embeds` content parts). The tokens at positions where `prompt_is_token_ids` is `False` are placeholder tokens that get replaced by entries from `prompt_embeds` in the forward pass.

## ExplicitEncoderDecoderPrompt [¶](#vllm.inputs.llm.ExplicitEncoderDecoderPrompt "Permanent link")

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

### decoder\_prompt `instance-attribute` [¶](#vllm.inputs.llm.ExplicitEncoderDecoderPrompt.decoder_prompt "Permanent link")

```
decoder_prompt: DecoderPrompt | None
```

The prompt for the decoder part of the model.

Passing `None` will cause the prompt to be inferred automatically.

### encoder\_prompt `instance-attribute` [¶](#vllm.inputs.llm.ExplicitEncoderDecoderPrompt.encoder_prompt "Permanent link")

```
encoder_prompt: EncoderPrompt
```

The prompt for the encoder part of the model.

## MultiModalDataBuiltins [¶](#vllm.inputs.llm.MultiModalDataBuiltins "Permanent link")

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

### audio `instance-attribute` [¶](#vllm.inputs.llm.MultiModalDataBuiltins.audio "Permanent link")

The input audio(s).

### image `instance-attribute` [¶](#vllm.inputs.llm.MultiModalDataBuiltins.image "Permanent link")

The input image(s).

### video `instance-attribute` [¶](#vllm.inputs.llm.MultiModalDataBuiltins.video "Permanent link")

The input video(s).

### vision\_chunk `instance-attribute` [¶](#vllm.inputs.llm.MultiModalDataBuiltins.vision_chunk "Permanent link")

The input visual atom(s) - unified modality for images and video chunks.

## TextPrompt [¶](#vllm.inputs.llm.TextPrompt "Permanent link")

Bases: `_PromptOptions`

Schema for a text prompt.

Source code in `vllm/inputs/llm.py`

```
classTextPrompt(_PromptOptions):
"""Schema for a text prompt."""

    prompt: str
"""The input text to be tokenized before passing to the model."""
```

### prompt `instance-attribute` [¶](#vllm.inputs.llm.TextPrompt.prompt "Permanent link")

The input text to be tokenized before passing to the model.

## TokensPrompt [¶](#vllm.inputs.llm.TokensPrompt "Permanent link")

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

### prompt `instance-attribute` [¶](#vllm.inputs.llm.TokensPrompt.prompt "Permanent link")

The prompt text corresponding to the token IDs, if available.

### prompt\_token\_ids `instance-attribute` [¶](#vllm.inputs.llm.TokensPrompt.prompt_token_ids "Permanent link")

A list of token IDs to pass to the model.

### token\_type\_ids `instance-attribute` [¶](#vllm.inputs.llm.TokensPrompt.token_type_ids "Permanent link")

A list of token type IDs to pass to the cross encoder model.

## \_PromptOptions [¶](#vllm.inputs.llm._PromptOptions "Permanent link")

Bases: `TypedDict`

Additional options available to all [`SingletonPrompt`](#vllm.inputs.llm.SingletonPrompt "            SingletonPrompt            module-attribute   ") types.

Source code in `vllm/inputs/llm.py`

```
class_PromptOptions(TypedDict):
"""
    Additional options available to all
    [`SingletonPrompt`][vllm.inputs.llm.SingletonPrompt] types.
    """

    multi_modal_data: NotRequired[MultiModalDataDict | None]
"""
    Optional multi-modal data to pass to the model,
    if the model supports it.
    """

    mm_processor_kwargs: NotRequired[dict[str, Any] | None]
"""
    Optional multi-modal processor kwargs to be forwarded to the
    multimodal input mapper & processor. Note that if multiple modalities
    have registered mappers etc for the model being considered, we attempt
    to pass the mm_processor_kwargs to each of them.
    """

    multi_modal_uuids: NotRequired[MultiModalUUIDDict]
"""
    Optional user-specified UUIDs for multimodal items, mapped by modality.
    Lists must match the number of items per modality and may contain `None`.
    For `None` entries, the hasher will compute IDs automatically; non-None
    entries override the default hashes for caching, and MUST be unique per
    multimodal item.
    """

    cache_salt: NotRequired[str]
"""
    Optional cache salt to be used for prefix caching.
    """
```

### cache\_salt `instance-attribute` [¶](#vllm.inputs.llm._PromptOptions.cache_salt "Permanent link")

Optional cache salt to be used for prefix caching.

### mm\_processor\_kwargs `instance-attribute` [¶](#vllm.inputs.llm._PromptOptions.mm_processor_kwargs "Permanent link")

Optional multi-modal processor kwargs to be forwarded to the multimodal input mapper & processor. Note that if multiple modalities have registered mappers etc for the model being considered, we attempt to pass the mm\_processor\_kwargs to each of them.

### multi\_modal\_data `instance-attribute` [¶](#vllm.inputs.llm._PromptOptions.multi_modal_data "Permanent link")

Optional multi-modal data to pass to the model, if the model supports it.

### multi\_modal\_uuids `instance-attribute` [¶](#vllm.inputs.llm._PromptOptions.multi_modal_uuids "Permanent link")

Optional user-specified UUIDs for multimodal items, mapped by modality. Lists must match the number of items per modality and may contain `None`. For `None` entries, the hasher will compute IDs automatically; non-None entries override the default hashes for caching, and MUST be unique per multimodal item.