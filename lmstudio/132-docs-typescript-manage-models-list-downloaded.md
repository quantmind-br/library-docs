---
title: List Local Models
url: https://lmstudio.ai/docs/typescript/manage-models/list-downloaded
source: sitemap
fetched_at: 2026-04-07T21:28:55.754956239-03:00
rendered_js: false
word_count: 50
summary: This document explains how to use the `listLocalModels` method within the `LMStudioClient` object to programmatically list all models available on a local machine. The output format mimics the command-line tool's listing.
tags:
    - lmstudioclient
    - local-models
    - list-methods
    - model-listing
category: reference
---

You can iterate through locally available models using the `listLocalModels` method.

## Available Model on the Local Machine[](#available-model-on-the-local-machine "Link to 'Available Model on the Local Machine'")

`listLocalModels` lives under the `system` namespace of the `LMStudioClient` object.

This will give you results equivalent to using [`lms ls`](https://lmstudio.ai/docs/cli/ls) in the CLI.

### Example output:[](#example-output)

```

[
  {
    "type": "llm",
    "modelKey": "qwen2.5-7b-instruct",
    "format": "gguf",
    "displayName": "Qwen2.5 7B Instruct",
    "path": "lmstudio-community/Qwen2.5-7B-Instruct-GGUF/Qwen2.5-7B-Instruct-Q4_K_M.gguf",
    "sizeBytes": 4683073952,
    "paramsString": "7B",
    "architecture": "qwen2",
    "vision": false,
    "trainedForToolUse": true,
    "maxContextLength": 32768
  },
  {
    "type": "embedding",
    "modelKey": "text-embedding-nomic-embed-text-v1.5@q4_k_m",
    "format": "gguf",
    "displayName": "Nomic Embed Text v1.5",
    "path": "nomic-ai/nomic-embed-text-v1.5-GGUF/nomic-embed-text-v1.5.Q4_K_M.gguf",
    "sizeBytes": 84106624,
    "architecture": "nomic-bert",
    "maxContextLength": 2048
  }
]
```