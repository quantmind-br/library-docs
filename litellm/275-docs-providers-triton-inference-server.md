---
title: Triton Inference Server | liteLLM
url: https://docs.litellm.ai/docs/providers/triton-inference-server
source: sitemap
fetched_at: 2026-01-21T19:50:32.646690155-03:00
rendered_js: false
word_count: 75
summary: This document explains how to use LiteLLM to interface with NVIDIA Triton Inference Server for chat completions and embedding models. It covers routing requests to specific Triton endpoints including /generate, /infer, and /embeddings.
tags:
    - triton-inference-server
    - litellm
    - chat-completion
    - embeddings
    - nvidia
    - api-integration
category: guide
---

LiteLLM supports Embedding Models on Triton Inference Servers

PropertyDetailsDescriptionNVIDIA Triton Inference ServerProvider Route on LiteLLM`triton/`Supported Operations`/chat/completion`, `/completion`, `/embedding`Supported Triton endpoints`/infer`, `/generate`, `/embeddings`Link to Provider Doc[Triton Inference Server ↗](https://developer.nvidia.com/triton-inference-server)

## Triton `/generate` - Chat Completion[​](#triton-generate---chat-completion "Direct link to triton-generate---chat-completion")

- SDK
- PROXY

Use the `triton/` prefix to route to triton server

```
from litellm import completion
response = completion(
    model="triton/llama-3-8b-instruct",
    messages=[{"role":"user","content":"who are u?"}],
    max_tokens=10,
    api_base="http://localhost:8000/generate",
)
```

## Triton `/infer` - Chat Completion[​](#triton-infer---chat-completion "Direct link to triton-infer---chat-completion")

- SDK
- PROXY

Use the `triton/` prefix to route to triton server

```
from litellm import completion


response = completion(
    model="triton/llama-3-8b-instruct",
    messages=[{"role":"user","content":"who are u?"}],
    max_tokens=10,
    api_base="http://localhost:8000/infer",
)
```

## Triton `/embeddings` - Embedding[​](#triton-embeddings---embedding "Direct link to triton-embeddings---embedding")

- SDK
- PROXY

Use the `triton/` prefix to route to triton server

```
from litellm import embedding
import os

response =await litellm.aembedding(
    model="triton/<your-triton-model>",
    api_base="https://your-triton-api-base/triton/embeddings",# /embeddings endpoint you want litellm to call on your server
input=["good morning from litellm"],
)
```