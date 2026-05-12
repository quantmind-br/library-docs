---
title: inputs - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/renderers/inputs/
source: sitemap
fetched_at: 2026-05-07T21:35:23.797699099-03:00
rendered_js: false
word_count: 125
summary: This document defines the schema structures for standardized dictionary-based prompts and their tokenized variations used within the vLLM rendering process.
tags:
    - data-schemas
    - prompt-engineering
    - tokenization
    - vllm-framework
    - input-preprocessing
category: reference
---

Modules:

Name Description `preprocess`

Schemas and utilities for preprocessing inputs.

`tokenize`

Schemas and utilities for tokenization inputs.

## DecoderDictPrompt `module-attribute` [¶](#vllm.renderers.inputs.DecoderDictPrompt "Permanent link")

A [`DecoderPrompt`](https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/#vllm.inputs.llm.DecoderPrompt "            DecoderPrompt            module-attribute   ") that has been standardized into a dictionary.

## DecoderOnlyDictPrompt `module-attribute` [¶](#vllm.renderers.inputs.DecoderOnlyDictPrompt "Permanent link")

A [`DecoderOnlyPrompt`](https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/#vllm.inputs.llm.DecoderOnlyPrompt "            DecoderOnlyPrompt            module-attribute   ") that has been standardized into a dictionary.

## DictPrompt `module-attribute` [¶](#vllm.renderers.inputs.DictPrompt "Permanent link")

A [`PromptType`](https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/#vllm.inputs.llm.PromptType "            PromptType            module-attribute   ") that has been standardized into a dictionary.

## EncoderDictPrompt `module-attribute` [¶](#vllm.renderers.inputs.EncoderDictPrompt "Permanent link")

A [`EncoderPrompt`](https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/#vllm.inputs.llm.EncoderPrompt "            EncoderPrompt            module-attribute   ") that has been standardized into a dictionary.

## SingletonDictPrompt `module-attribute` [¶](#vllm.renderers.inputs.SingletonDictPrompt "Permanent link")

A [`SingletonPrompt`](https://docs.vllm.ai/en/latest/api/vllm/inputs/llm/#vllm.inputs.llm.SingletonPrompt "            SingletonPrompt            module-attribute   ") that has been standardized into a dictionary.

## TokPrompt `module-attribute` [¶](#vllm.renderers.inputs.TokPrompt "Permanent link")

A [`DictPrompt`](https://docs.vllm.ai/en/latest/api/vllm/renderers/inputs/preprocess/#vllm.renderers.inputs.preprocess.DictPrompt "            DictPrompt            module-attribute   ") that has been tokenized.

## EncoderDecoderDictPrompt [¶](#vllm.renderers.inputs.EncoderDecoderDictPrompt "Permanent link")

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

## EncoderDecoderTokPrompt [¶](#vllm.renderers.inputs.EncoderDecoderTokPrompt "Permanent link")

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