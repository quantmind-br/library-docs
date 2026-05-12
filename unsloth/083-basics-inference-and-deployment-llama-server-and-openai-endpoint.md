---
title: llama-server & OpenAI endpoint Deployment Guide
url: https://unsloth.ai/docs/basics/inference-and-deployment/llama-server-and-openai-endpoint.md
source: llms
fetched_at: 2026-04-27T18:14:53.025914496-03:00
rendered_js: false
word_count: 507
summary: Deploy Devstral-2 via llama-server and expose as an OpenAI-compatible endpoint.
tags:
    - llama-server
    - openai-deployment
    - devstral-2
    - model-serving
    - ggml
    - inference
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# llama-server & OpenAI endpoint Deployment Guide

Deploys Devstral-2 via `llama-server` with an OpenAI-compatible endpoint. See [[027-models-tutorials-devstral-2|Devstral 2]] for model details.

## Build llama.cpp

Clone from [GitHub](https://github.com/ggml-org/llama.cpp). Set `-DGGML_CUDA=OFF` for CPU-only. Apple Mac/Metal: set `-DGGML_CUDA=OFF` (Metal is on by default).

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

## Download model

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Devstral-2-123B-Instruct-2512-GGUF",
    local_dir = "Devstral-2-123B-Instruct-2512-GGUF",
    allow_patterns = ["*UD-Q2_K_XL*", "*mmproj-F16*"],
)
```

## Deploy with llama-server

Run in a separate terminal (e.g. tmux):

```bash
./llama.cpp/llama-server \
    --model Devstral-Small-2-24B-Instruct-2512-GGUF/Devstral-Small-2-24B-Instruct-2512-UD-Q4_K_XL.gguf \
    --mmproj Devstral-Small-2-24B-Instruct-2512-GGUF/mmproj-F16.gguf \
    --alias "unsloth/Devstral-Small-2-24B-Instruct-2512" \
    --threads -1 \
    --n-gpu-layers 999 \
    --prio 3 \
    --min_p 0.01 \
    --ctx-size 16384 \
    --port 8001 \
    --jinja
```

## Query via OpenAI SDK

```bash
pip install openai
```

```python
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/Devstral-Small-2-24B-Instruct-2512",
    messages = [{"role": "user", "content": "What is 2+2?"},],
)
print(completion.choices[0].message.content)
```

For speculative decoding and other arguments, see <https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md>.

## llama-server quirks

> [!warning] `--jinja` system message injection
> When using `--jinja`, llama-server appends this system message if tools are supported:
> `Respond in JSON format, either with tool_call (a request to call tools) or with response reply to the user's request`
>
> This can break fine-tunes. Use `--no-jinja` to disable, but `tools` becomes unsupported.
>
> Example: FunctionGemma's system prompt `You are a model that can do function calling with the following functions` becomes:
> `You are a model that can do function calling with the following functions\n\nRespond in JSON format, either with tool_call (a request to call tools) or with response reply to the user's request`
>
> Fix: add the tool-calling prompt explicitly for all fine-tunes.
>
> Tracked at <https://github.com/ggml-org/llama.cpp/issues/18323>. See also [llama.cpp chat.cpp](https://github.com/ggml-org/llama.cpp/blob/12ee1763a6f6130ce820a366d220bbadff54b818/common/chat.cpp#L849).

## Tool Calling

See [[095-basics-tool-calling-guide-for-local-llms|Tool Calling Guide for Local LLMs]].

#inference #llama-server #openai #deployment #gguf
