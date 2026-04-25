---
title: List Downloaded Models
url: https://lmstudio.ai/docs/python/manage-models/list-downloaded
source: sitemap
fetched_at: 2026-04-07T21:31:32.759323627-03:00
rendered_js: false
word_count: 70
summary: This document explains how to iterate through locally available models and use the provided listing results to obtain full SDK handles for loaded model instances.
tags:
    - local-models
    - llm-studio-server
    - model-listing
    - sdk-handle
    - model-iteration
category: guide
---

You can iterate through locally available models using the downloaded model listing methods.

The listing results offer `.model()` and `.load_new_instance()` methods, which allow the downloaded model reference to be converted in the full SDK handle for a loaded model.

## Available Models on the LM Studio Server[](#available-models-on-the-lm-studio-server "Link to 'Available Models on the LM Studio Server'")

This will give you results equivalent to using [`lms ls`](https://lmstudio.ai/docs/cli/ls) in the CLI.

### Example output:[](#example-output)

```

DownloadedLlm(model_key='qwen2.5-7b-instruct-1m', display_name='Qwen2.5 7B Instruct 1M', architecture='qwen2', vision=False)
DownloadedEmbeddingModel(model_key='text-embedding-nomic-embed-text-v1.5', display_name='Nomic Embed Text v1.5', architecture='nomic-bert')
```