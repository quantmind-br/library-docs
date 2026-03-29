---
title: Ollama-Compatible API — SGLang
url: https://docs.sglang.io/basic_usage/ollama_api.html
source: crawler
fetched_at: 2026-02-04T08:46:40.68303284-03:00
rendered_js: false
word_count: 112
summary: This document explains how to use SGLang as an Ollama-compatible inference backend, enabling the use of the Ollama CLI and Python library for model interaction.
tags:
    - sglang
    - ollama-api
    - inference-backend
    - python-client
    - llm-serving
category: guide
---

## Contents

## Ollama-Compatible API[#](#ollama-compatible-api "Link to this heading")

SGLang provides Ollama API compatibility, allowing you to use the Ollama CLI and Python library with SGLang as the inference backend.

## Prerequisites[#](#prerequisites "Link to this heading")

```
# Install the Ollama Python library (for Python client usage)
pipinstallollama
```

> **Note**: You don’t need the Ollama server installed - SGLang acts as the backend. You only need the `ollama` CLI or Python library as the client.

## Endpoints[#](#endpoints "Link to this heading")

## Quick Start[#](#quick-start "Link to this heading")

### 1. Launch SGLang Server[#](#launch-sglang-server "Link to this heading")

```
python-msglang.launch_server\
--modelQwen/Qwen2.5-1.5B-Instruct\
--port30001\
--host0.0.0.0
```

> **Note**: The model name used with `ollama run` must match exactly what you passed to `--model`.

### 2. Use Ollama CLI[#](#use-ollama-cli "Link to this heading")

```
# List available models
OLLAMA_HOST=http://localhost:30001ollamalist

# Interactive chat
OLLAMA_HOST=http://localhost:30001ollamarun"Qwen/Qwen2.5-1.5B-Instruct"
```

If connecting to a remote server behind a firewall:

```
# SSH tunnel
ssh-L30001:localhost:30001user@gpu-server-N&

# Then use Ollama CLI as above
OLLAMA_HOST=http://localhost:30001ollamalist
```

### 3. Use Ollama Python Library[#](#use-ollama-python-library "Link to this heading")

```
importollama

client = ollama.Client(host='http://localhost:30001')

# Non-streaming
response = client.chat(
    model='Qwen/Qwen2.5-1.5B-Instruct',
    messages=[{'role': 'user', 'content': 'Hello!'}]
)
print(response['message']['content'])

# Streaming
stream = client.chat(
    model='Qwen/Qwen2.5-1.5B-Instruct',
    messages=[{'role': 'user', 'content': 'Tell me a story'}],
    stream=True
)
for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
```

## Smart Router[#](#smart-router "Link to this heading")

For intelligent routing between local Ollama (fast) and remote SGLang (powerful) using an LLM judge, see the [Smart Router documentation](https://github.com/sgl-project/sglang/blob/main/python/sglang/srt/entrypoints/ollama/README.md).

## Summary[#](#summary "Link to this heading")