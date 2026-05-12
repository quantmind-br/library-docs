---
title: Model Resolution - vLLM
url: https://docs.vllm.ai/en/latest/configuration/model_resolution/
source: sitemap
fetched_at: 2026-05-07T21:11:14.284513732-03:00
rendered_js: false
word_count: 114
summary: This document explains how vLLM resolves HuggingFace model architectures and provides instructions for overriding configuration settings when automatic resolution fails.
tags:
    - vllm
    - model-loading
    - configuration
    - hugging-face
    - architecture-resolution
    - hf-overrides
category: configuration
---

[](https://github.com/vllm-project/vllm/edit/main/docs/configuration/model_resolution.md "Edit this page")

vLLM loads HuggingFace-compatible models by inspecting the `architectures` field in `config.json` of the model repository and finding the corresponding implementation that is registered to vLLM. Nevertheless, our model resolution may fail for the following reasons:

- The `config.json` of the model repository lacks the `architectures` field.
- Unofficial repositories refer to a model using alternative names which are not recorded in vLLM.
- The same architecture name is used for multiple models, creating ambiguity as to which model should be loaded.

To fix this, explicitly specify the model architecture by passing `config.json` overrides to the `hf_overrides` option. For example:

```
fromvllmimport LLM

llm = LLM(
    model="cerebras/Cerebras-GPT-1.3B",
    hf_overrides={"architectures": ["GPT2LMHeadModel"]},  # GPT-2
)
```

Our [list of supported models](https://docs.vllm.ai/en/latest/models/supported_models/) shows the model architectures that are recognized by vLLM.