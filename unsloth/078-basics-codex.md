---
title: How to Run Local LLMs with OpenAI Codex
url: https://unsloth.ai/docs/basics/codex.md
source: llms
fetched_at: 2026-04-27T18:14:57.578609452-03:00
rendered_js: false
word_count: 764
summary: This guide provides a comprehensive tutorial on how to run local Large Language Models (LLMs) with the OpenAI Codex CLI by leveraging open-source tools like llama.cpp and Unsloth, detailing setup, model downloading, server deployment, and final configuration.
tags:
    - local-llms
    - openai-codex
    - llama-cpp
    - unsloth
    - gguf
    - api-setup
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# How to Run Local LLMs with OpenAI Codex

Connect open LLMs to the [Codex CLI](https://github.com/openai/codex) entirely locally. Works with any OpenAI/API-compatible local model (DeepSeek, Qwen, Gemma, etc.).

This tutorial uses [[003-models-glm-4.7-flash|GLM-4.7-Flash]] (30B MoE, agentic + coding) on 24GB VRAM. Swap in any model from [[050-models-tutorials|LLM tutorials]].

Model quantization: [Unsloth Dynamic GGUFs](https://open-2v.gitbook.com/url/preview/site_mXXTe/~/revisions/NYG3pIjIP3JF6zgJgfjl/basics/unsloth-dynamic-2.0-ggufs) (UD-Q4_K_XL recommended).

Runtime: [`llama.cpp`](https://github.com/ggml-org/llama.cpp) — serves models via a single OpenAI-compatible HTTP endpoint.

## Setup

### Install llama.cpp

Build from source with GPU bindings. Set `-DGGML_CUDA=OFF` for CPU-only or Apple Metal (Metal is auto-enabled):

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev git-all -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

### Download Model

Via `huggingface_hub` (install: `pip install huggingface_hub hf_transfer`). See [[114-get-started-unsloth-model-catalog|Unsloth Model Catalog]] for all GGUF uploads. If downloads stall, see [[124-basics-troubleshooting-and-faqs-hugging-face-hub-xet-debugging|XET debugging]].

```python
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id = "unsloth/GLM-4.7-Flash-GGUF",
    local_dir = "unsloth/GLM-4.7-Flash-GGUF",
    allow_patterns = ["*UD-Q4_K_XL*"],
)
```

> [!tip] You can substitute `unsloth/Qwen3-Coder-Next-GGUF` — see [[019-models-qwen3-coder-next|Qwen3-Coder-Next]].

### Start llama-server

Serves on port 8001. Fits in 24GB GPU (RTX 4090, uses ~23GB). Uses KV cache quantization (`q8_0`) to reduce VRAM.

```bash
./llama.cpp/llama-server \
    --model unsloth/GLM-4.7-Flash-GGUF/GLM-4.7-Flash-UD-Q4_K_XL.gguf \
    --alias "unsloth/GLM-4.7-Flash" \
    --temp 1.0 \
    --top-p 0.95 \
    --min-p 0.01 \
    --port 8001 \
    --kv-unified \
    --cache-type-k q8_0 --cache-type-v q8_0 \
    --flash-attn on \
    --batch-size 4096 --ubatch-size 1024 \
    --ctx-size 131072
```

> [!tip] Disable thinking for GLM-4.7-Flash to improve agentic coding performance. Add to llama-server command:
> `--chat-template-kwargs "{\"enable_thinking\": false}"`

## OpenAI Codex CLI Configuration

### Install

**Mac (Homebrew):**

```bash
brew install --cask codex
```

**Linux (NPM):**

```bash
apt update
apt install nodejs npm -y
npm install -g @openai/codex
```

### Configure

First run `codex` to login, then create `~/.codex/config.toml` (or `%USERPROFILE%\.codex\config.toml` on Windows):

```toml
[model_providers.llama_cpp]
name = "llama_cpp API"
base_url = "http://localhost:8001/v1"
wire_api = "responses"
stream_idle_timeout_ms = 10000000
```

### Run

```bash
codex --model unsloth/GLM-4.7-Flash -c model_provider=llama_cpp --search
```

Or with unrestricted code execution (**bypasses all approvals**):

```bash
codex --model unsloth/GLM-4.7-Flash -c model_provider=llama_cpp --search --dangerously-bypass-approvals-and-sandbox
```

> [!warning] `wire_api = "chat"` support is being removed by OpenAI. Use `wire_api = "responses"` — but as of 2026-01-29 it may error with: `{"error":{"code":400,"message":"'type' of tool must be 'function'"}}`.

### Test Prompt

```
You can only work in the cwd project/. Do not search for AGENTS.md - this is it. Install Unsloth via a virtual environment via uv. See https://unsloth.ai/docs/get-started/install/pip-install on how (get it and read). Then do a simple Unsloth finetuning run described in https://github.com/unslothai/unsloth. You have access to 1 GPU.
```

#local-llm #openai-codex #llama-cpp #unsloth #gguf
