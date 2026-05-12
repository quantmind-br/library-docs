---
title: engine - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/inputs/engine/
source: sitemap
fetched_at: 2026-05-07T21:21:57.917499964-03:00
rendered_js: false
word_count: 708
summary: This document defines the schemas and data structures for engine inputs in vLLM, including support for standard prompts, multi-modal inputs, embeddings, and encoder-decoder model configurations.
tags:
    - vllm
    - llm-engine
    - data-schemas
    - multi-modal
    - embeddings
    - api-reference
category: reference
---

## vllm.inputs.engine [¶](#vllm.inputs.engine "Permanent link")

Schema and utilities for inputs to the engine client (`LLMEngine`/`AsyncLLM`).

## DecoderEngineInput `module-attribute` [¶](#vllm.inputs.engine.DecoderEngineInput "Permanent link")

A rendered [`DecoderPrompt`](https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/#vllm.inputs.llm.DecoderPrompt "            DecoderPrompt            module-attribute   ") which can be passed to `LLMEngine.add_request` or `AsyncLLM.add_request`.

## DecoderOnlyEngineInput `module-attribute` [¶](#vllm.inputs.engine.DecoderOnlyEngineInput "Permanent link")

A rendered [`DecoderOnlyPrompt`](https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/#vllm.inputs.llm.DecoderOnlyPrompt "            DecoderOnlyPrompt            module-attribute   ") which can be passed to `LLMEngine.add_request` or `AsyncLLM.add_request`.

## EncoderInput `module-attribute` [¶](#vllm.inputs.engine.EncoderInput "Permanent link")

A rendered [`EncoderPrompt`](https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/#vllm.inputs.llm.EncoderPrompt "            EncoderPrompt            module-attribute   ") which can be passed to `LLMEngine.add_request` or `AsyncLLM.add_request`.

## EngineInput `module-attribute` [¶](#vllm.inputs.engine.EngineInput "Permanent link")

A rendered [`PromptType`](https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/#vllm.inputs.llm.PromptType "            PromptType            module-attribute   ") which can be passed to `LLMEngine.add_request` or `AsyncLLM.add_request`.

## MultiModalHashes `module-attribute` [¶](#vllm.inputs.engine.MultiModalHashes "Permanent link")

A dictionary containing per-item hashes for each modality.

## MultiModalPlaceholders `module-attribute` [¶](#vllm.inputs.engine.MultiModalPlaceholders "Permanent link")

A dictionary containing per-item placeholder ranges for each modality.

## SingletonInput `module-attribute` [¶](#vllm.inputs.engine.SingletonInput "Permanent link")

A rendered [`SingletonPrompt`](https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/#vllm.inputs.llm.SingletonPrompt "            SingletonPrompt            module-attribute   ") which can be passed to `LLMEngine.add_request` or `AsyncLLM.add_request`.

## EmbedsInput [¶](#vllm.inputs.engine.EmbedsInput "Permanent link")

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

### is\_token\_ids `instance-attribute` [¶](#vllm.inputs.engine.EmbedsInput.is_token_ids "Permanent link")

Per-position mask for mixed-mode inputs. `True` means the position is a real token ID (use the model's embedding layer); `False` means the position uses a pre-computed embedding row from `prompt_embeds`. Length MUST equal `len(prompt_token_ids)`. For pure-embeds inputs this field is absent.

### prompt `instance-attribute` [¶](#vllm.inputs.engine.EmbedsInput.prompt "Permanent link")

The prompt text corresponding to the token IDs, if available.

### prompt\_embeds `instance-attribute` [¶](#vllm.inputs.engine.EmbedsInput.prompt_embeds "Permanent link")

The embeddings of the prompt.

### prompt\_token\_ids `instance-attribute` [¶](#vllm.inputs.engine.EmbedsInput.prompt_token_ids "Permanent link")

Token IDs of the rendered prompt. Only set for mixed-mode inputs (chat completion with `prompt_embeds` content parts). When present, `is_token_ids` MUST also be present and have the same length. For pure-embeds inputs this field is absent.

### type `instance-attribute` [¶](#vllm.inputs.engine.EmbedsInput.type "Permanent link")

The type of input.

## EncoderDecoderInput [¶](#vllm.inputs.engine.EncoderDecoderInput "Permanent link")

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

### arrival\_time `instance-attribute` [¶](#vllm.inputs.engine.EncoderDecoderInput.arrival_time "Permanent link")

The time when the input was received (before rendering).

### decoder\_prompt `instance-attribute` [¶](#vllm.inputs.engine.EncoderDecoderInput.decoder_prompt "Permanent link")

```
decoder_prompt: DecoderEngineInput
```

The inputs for the decoder portion.

### encoder\_prompt `instance-attribute` [¶](#vllm.inputs.engine.EncoderDecoderInput.encoder_prompt "Permanent link")

```
encoder_prompt: EncoderInput
```

The inputs for the encoder portion.

## MultiModalEncDecInput [¶](#vllm.inputs.engine.MultiModalEncDecInput "Permanent link")

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

### encoder\_prompt `instance-attribute` [¶](#vllm.inputs.engine.MultiModalEncDecInput.encoder_prompt "Permanent link")

The prompt text corresponding to the encoder token IDs, if available.

### encoder\_prompt\_token\_ids `instance-attribute` [¶](#vllm.inputs.engine.MultiModalEncDecInput.encoder_prompt_token_ids "Permanent link")

```
encoder_prompt_token_ids: list[int]
```

The processed token IDs of the encoder prompt.

## MultiModalInput [¶](#vllm.inputs.engine.MultiModalInput "Permanent link")

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

### mm\_hashes `instance-attribute` [¶](#vllm.inputs.engine.MultiModalInput.mm_hashes "Permanent link")

```
mm_hashes: MultiModalHashes
```

The hashes of the multi-modal data.

### mm\_kwargs `instance-attribute` [¶](#vllm.inputs.engine.MultiModalInput.mm_kwargs "Permanent link")

```
mm_kwargs: MultiModalKwargsOptionalItems
```

Keyword arguments to be directly passed to the model after batching.

### mm\_placeholders `instance-attribute` [¶](#vllm.inputs.engine.MultiModalInput.mm_placeholders "Permanent link")

```
mm_placeholders: MultiModalPlaceholders
```

For each modality, information about the placeholder tokens in `prompt_token_ids`.

### prompt `instance-attribute` [¶](#vllm.inputs.engine.MultiModalInput.prompt "Permanent link")

The prompt text corresponding to the token IDs, if available.

### prompt\_token\_ids `instance-attribute` [¶](#vllm.inputs.engine.MultiModalInput.prompt_token_ids "Permanent link")

The processed token IDs which includes placeholder tokens.

### type `instance-attribute` [¶](#vllm.inputs.engine.MultiModalInput.type "Permanent link")

The type of input.

## TokensInput [¶](#vllm.inputs.engine.TokensInput "Permanent link")

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

### prompt `instance-attribute` [¶](#vllm.inputs.engine.TokensInput.prompt "Permanent link")

The prompt text corresponding to the token IDs, if available.

### prompt\_token\_ids `instance-attribute` [¶](#vllm.inputs.engine.TokensInput.prompt_token_ids "Permanent link")

The token IDs of the prompt.

### type `instance-attribute` [¶](#vllm.inputs.engine.TokensInput.type "Permanent link")

The type of input.

## \_InputOptions [¶](#vllm.inputs.engine._InputOptions "Permanent link")

Bases: `TypedDict`

Additional options available to all [`SingletonInput`](#vllm.inputs.engine.SingletonInput "            SingletonInput            module-attribute   ") types.

Source code in `vllm/inputs/engine.py`

```
class_InputOptions(TypedDict):
"""
    Additional options available to all
    [`SingletonInput`][vllm.inputs.engine.SingletonInput] types.
    """

    arrival_time: NotRequired[float]
"""The time when the input was received (before rendering)."""

    cache_salt: NotRequired[str]
"""Optional cache salt to be used for prefix caching."""
```

### arrival\_time `instance-attribute` [¶](#vllm.inputs.engine._InputOptions.arrival_time "Permanent link")

The time when the input was received (before rendering).

### cache\_salt `instance-attribute` [¶](#vllm.inputs.engine._InputOptions.cache_salt "Permanent link")

Optional cache salt to be used for prefix caching.

## \_prepare\_decoder\_input\_ids\_for\_generation [¶](#vllm.inputs.engine._prepare_decoder_input_ids_for_generation "Permanent link")

```
_prepare_decoder_input_ids_for_generation(
    decoder_input_ids: list[int],
    decoder_start_token_id: int,
) -> list[int]
```

Prepare `decoder_input_ids` for generation with encoder-decoder models, according to `GenerationMixin._prepare_decoder_input_ids_for_generation()`.

Source: https://github.com/huggingface/transformers/blob/v5.1.0/src/transformers/generation/utils.py

Source code in `vllm/inputs/engine.py`

```
def_prepare_decoder_input_ids_for_generation(
    decoder_input_ids: list[int],
    decoder_start_token_id: int,
) -> list[int]:
"""
    Prepare `decoder_input_ids` for generation with encoder-decoder models,
    according to `GenerationMixin._prepare_decoder_input_ids_for_generation()`.

    Source:
    https://github.com/huggingface/transformers/blob/v5.1.0/src/transformers/generation/utils.py
    """
    if len(decoder_input_ids) == 0 or decoder_input_ids[0] != decoder_start_token_id:
        decoder_input_ids = [decoder_start_token_id] + decoder_input_ids

    return decoder_input_ids
```

## embeds\_input [¶](#vllm.inputs.engine.embeds_input "Permanent link")

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

Construct [`EmbedsInput`](#vllm.inputs.engine.EmbedsInput "            EmbedsInput") from optional values.

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

## tokens\_input [¶](#vllm.inputs.engine.tokens_input "Permanent link")

```
tokens_input(
    prompt_token_ids: list[int],
    *,
    prompt: str | None = None,
    cache_salt: str | None = None,
) -> TokensInput
```

Construct [`TokensInput`](#vllm.inputs.engine.TokensInput "            TokensInput") from optional values.

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