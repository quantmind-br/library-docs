---
title: Get Model Info
url: https://lmstudio.ai/docs/python/model-info/get-model-info
source: sitemap
fetched_at: 2026-04-07T21:27:37.516131262-03:00
rendered_js: false
word_count: 44
summary: This document explains how to access general information and metadata about a loaded language model instance using a dedicated function call.
tags:
    - model-metadata
    - instance-info
    - llm-reference
    - qwen2
    - embedding-model
category: reference
---

You can access general information and metadata about a model itself from a loaded instance of that model.

In the below examples, the LLM reference can be replaced with an embedding model reference without requiring any other changes.

## Example output[](#example-output "Link to 'Example output'")

```

LlmInstanceInfo.from_dict({
  "architecture": "qwen2",
  "contextLength": 4096,
  "displayName": "Qwen2.5 7B Instruct 1M",
  "format": "gguf",
  "identifier": "qwen2.5-7b-instruct",
  "instanceReference": "lpFZPBQjhSZPrFevGyY6Leq8",
  "maxContextLength": 1010000,
  "modelKey": "qwen2.5-7b-instruct-1m",
  "paramsString": "7B",
  "path": "lmstudio-community/Qwen2.5-7B-Instruct-1M-GGUF/Qwen2.5-7B-Instruct-1M-Q4_K_M.gguf",
  "sizeBytes": 4683073888,
  "trainedForToolUse": true,
  "type": "llm",
  "vision": false
})
```