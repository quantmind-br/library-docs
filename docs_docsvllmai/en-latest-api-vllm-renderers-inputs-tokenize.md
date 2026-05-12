---
title: tokenize - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/renderers/inputs/tokenize/
source: sitemap
fetched_at: 2026-05-07T21:35:24.989706916-03:00
rendered_js: false
word_count: 35
summary: This document defines the schemas and structures for handling tokenized input prompts within the vLLM library, specifically covering standard and encoder-decoder configurations.
tags:
    - vllm
    - tokenization
    - input-schemas
    - encoder-decoder
    - typed-dict
    - python-api
category: reference
---

## vllm.renderers.inputs.tokenize [¶](#vllm.renderers.inputs.tokenize "Permanent link")

Schemas and utilities for tokenization inputs.

## TokPrompt `module-attribute` [¶](#vllm.renderers.inputs.tokenize.TokPrompt "Permanent link")

A [`DictPrompt`](https://docs.vllm.ai/en/latest/api/vllm/renderers/inputs/preprocess/#vllm.renderers.inputs.preprocess.DictPrompt "            DictPrompt            module-attribute   ") that has been tokenized.

## EncoderDecoderTokPrompt [¶](#vllm.renderers.inputs.tokenize.EncoderDecoderTokPrompt "Permanent link")

Bases: `TypedDict`

A [`EncoderDecoderDictPrompt`](https://docs.vllm.ai/en/latest/api/vllm/renderers/inputs/preprocess/#vllm.renderers.inputs.preprocess.EncoderDecoderDictPrompt "            EncoderDecoderDictPrompt") that has been tokenized.

Source code in `vllm/renderers/inputs/tokenize.py`

```
classEncoderDecoderTokPrompt(TypedDict):
"""
    A
    [`EncoderDecoderDictPrompt`][vllm.renderers.inputs.preprocess.EncoderDecoderDictPrompt]
    that has been tokenized.
    """

    encoder_prompt: EncoderTokPrompt

    decoder_prompt: DecoderTokPrompt | None
```