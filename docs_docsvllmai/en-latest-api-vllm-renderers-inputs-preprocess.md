---
title: preprocess - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/renderers/inputs/preprocess/
source: sitemap
fetched_at: 2026-05-07T21:35:24.320743143-03:00
rendered_js: false
word_count: 140
summary: This module provides utility functions and type definitions for parsing, validating, and standardizing model input prompts into dictionary formats before tokenization.
tags:
    - input-preprocessing
    - data-normalization
    - prompt-parsing
    - vllm-internals
    - schema-validation
category: reference
---

## vllm.renderers.inputs.preprocess [¶](#vllm.renderers.inputs.preprocess "Permanent link")

Schemas and utilities for preprocessing inputs.

## DecoderDictPrompt `module-attribute` [¶](#vllm.renderers.inputs.preprocess.DecoderDictPrompt "Permanent link")

A [`DecoderPrompt`](https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/#vllm.inputs.llm.DecoderPrompt "            DecoderPrompt            module-attribute   ") that has been standardized into a dictionary.

## DecoderOnlyDictPrompt `module-attribute` [¶](#vllm.renderers.inputs.preprocess.DecoderOnlyDictPrompt "Permanent link")

A [`DecoderOnlyPrompt`](https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/#vllm.inputs.llm.DecoderOnlyPrompt "            DecoderOnlyPrompt            module-attribute   ") that has been standardized into a dictionary.

## DictPrompt `module-attribute` [¶](#vllm.renderers.inputs.preprocess.DictPrompt "Permanent link")

A [`PromptType`](https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/#vllm.inputs.llm.PromptType "            PromptType            module-attribute   ") that has been standardized into a dictionary.

## EncoderDictPrompt `module-attribute` [¶](#vllm.renderers.inputs.preprocess.EncoderDictPrompt "Permanent link")

A [`EncoderPrompt`](https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/#vllm.inputs.llm.EncoderPrompt "            EncoderPrompt            module-attribute   ") that has been standardized into a dictionary.

## SingletonDictPrompt `module-attribute` [¶](#vllm.renderers.inputs.preprocess.SingletonDictPrompt "Permanent link")

A [`SingletonPrompt`](https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/#vllm.inputs.llm.SingletonPrompt "            SingletonPrompt            module-attribute   ") that has been standardized into a dictionary.

## EncoderDecoderDictPrompt [¶](#vllm.renderers.inputs.preprocess.EncoderDecoderDictPrompt "Permanent link")

Bases: `TypedDict`

A [`EncoderDecoderPrompt`](https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/#vllm.inputs.llm.EncoderDecoderPrompt "            EncoderDecoderPrompt            module-attribute   ") that has been standardized into a dictionary.

Source code in `vllm/renderers/inputs/preprocess.py`

```
classEncoderDecoderDictPrompt(TypedDict):
"""
    A [`EncoderDecoderPrompt`][vllm.inputs.llm.EncoderDecoderPrompt]
    that has been standardized into a dictionary.
    """

    encoder_prompt: EncoderDictPrompt

    decoder_prompt: DecoderDictPrompt | None
```

## \_validate\_prompt\_dict [¶](#vllm.renderers.inputs.preprocess._validate_prompt_dict "Permanent link")

Reject malformed dict prompts before renderer tokenization.

Source code in `vllm/renderers/inputs/preprocess.py`

```
def_validate_prompt_dict(prompt: Mapping[str, object]) -> None:
"""Reject malformed dict prompts before renderer tokenization."""
    if (
        "prompt" not in prompt
        or "prompt_token_ids" in prompt
        or "prompt_embeds" in prompt
    ):
        return

    if not isinstance(prompt["prompt"], str):
        raise TypeError("Prompt text should be a string")
```

## parse\_dec\_only\_prompt [¶](#vllm.renderers.inputs.preprocess.parse_dec_only_prompt "Permanent link")

Parse a prompt for a decoder-only model and normalize it to a dictionary.

Source code in `vllm/renderers/inputs/preprocess.py`

```
defparse_dec_only_prompt(prompt: PromptType | object) -> DecoderOnlyDictPrompt:
"""
    Parse a prompt for a decoder-only model and normalize it to a dictionary.
    """
    if isinstance(prompt, str):
        return TextPrompt(prompt=prompt)

    if isinstance(prompt, list):
        if not is_list_of(prompt, int):
            raise TypeError("Token prompt should be a list of integers")

        return TokensPrompt(prompt_token_ids=prompt)

    if isinstance(prompt, dict):
        if "encoder_prompt" in prompt:
            raise TypeError("Cannot pass encoder-decoder prompt to decoder-only models")

        _validate_prompt_dict(prompt)

        if (
            "prompt" in prompt
            or "prompt_token_ids" in prompt
            or "prompt_embeds" in prompt
        ):
            return prompt  # type: ignore[return-value]

        raise TypeError("Prompt dictionary must contain text, tokens, or embeddings")

    raise TypeError("Prompt should be a string, list of tokens, or dictionary")
```

## parse\_enc\_dec\_prompt [¶](#vllm.renderers.inputs.preprocess.parse_enc_dec_prompt "Permanent link")

Parse a prompt for an encoder-decoder model and normalize it to a dictionary.

Source code in `vllm/renderers/inputs/preprocess.py`

```
defparse_enc_dec_prompt(prompt: PromptType | object) -> EncoderDecoderDictPrompt:
"""
    Parse a prompt for an encoder-decoder model and normalize it to a dictionary.
    """
    if isinstance(prompt, dict) and "encoder_prompt" in prompt:
        enc_prompt = prompt["encoder_prompt"]  # type: ignore[typeddict-item]
        dec_prompt = prompt["decoder_prompt"]  # type: ignore[typeddict-item]
    else:
        enc_prompt = prompt
        dec_prompt = None

    return EncoderDecoderDictPrompt(
        encoder_prompt=_parse_enc_prompt(enc_prompt),
        decoder_prompt=None if dec_prompt is None else _parse_dec_prompt(dec_prompt),
    )
```