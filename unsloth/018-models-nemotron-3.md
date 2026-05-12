---
title: NVIDIA Nemotron 3 Nano - How To Run Guide
url: https://unsloth.ai/docs/models/nemotron-3.md
source: llms
fetched_at: 2026-04-27T18:13:41.616281987-03:00
rendered_js: false
word_count: 1883
summary: This guide explains how to run and utilize the NVIDIA Nemotron-3 family of models, specifically detailing configurations for Nemotron-3-Nano-4B. It provides instructions for running the model locally using Unsloth Studio or via llama.cpp with recommended inference parameters and chat templates.
tags:
    - nemotron-3
    - llm-guide
    - unsloth-studio
    - inference
    - model-running
    - gpu-optimization
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# NVIDIA Nemotron 3 Nano - How To Run Guide

**Nemotron-3-Nano-4B** — 4B open hybrid MoE model following [[017-models-nemotron-3-nemotron-3-super|Nemotron-3-Super-120B-A12B]] and Nemotron-3-Nano-30B-A3B. Designed for fast coding, math, and agentic workloads. **1M-token context** window.

| Model | RAM required | Notes |
|---|---|---|
| Nemotron-3-Nano-4B | 5 GB (4-bit ~3 GB, 8-bit ~5 GB) | Runs on RAM, VRAM, or unified memory |
| Nemotron-3-Nano-30B-A3B | 24 GB (4-bit ~24 GB, 8-bit ~36 GB) | Fine-tunable locally via [[001-get-started-readme|Unsloth]] |

GGUFs: [Nemotron-3-Nano-4B-GGUF](https://huggingface.co/unsloth/NVIDIA-Nemotron-3-Nano-4B-GGUF) | [Nemotron-3-Nano-30B-A3B-GGUF](https://huggingface.co/unsloth/Nemotron-3-Nano-30B-A3B-GGUF)

> [!note] GGUF sizing note
> Some GGUFs end up similar in size because the model architecture (like [[013-models-gpt-oss-how-to-run-and-fine-tune|gpt-oss]]) has dimensions not divisible by 128, so parts can't be quantized to lower bits.

## Inference Settings

| Use-case | `temperature` | `top_p` |
|---|---|---|
| General chat/instruction | 1.0 | 1.0 |
| Tool calling | 0.6 | 0.95 |

- `max_new_tokens`: 32,768–262,144 (standard); increase for deep reasoning/long-form as RAM allows
- Some GGUFs similar in size due to architecture dimensions not divisible by 128

### Chat Template

```python
tokenizer.apply_chat_template([
    {"role" : "user", "content" : "What is 1+1?"},
    {"role" : "assistant", "content" : "2"},
    {"role" : "user", "content" : "What is 2+2?"}
    ], add_generation_prompt = True, tokenize = False,
)
```

> [!tip] NoPE positional embeddings
> Model trained with NoPE — only need to change `max_position_embeddings`. No explicit positional embeddings, so YaRN isn't needed.

#### Nemotron 3 Chat Template Format

```
<|im_start|>system\n<|im_end|>\n<|im_start|>user\nWhat is 1+1?<|im_end|>\n<|im_start|>assistant\n繁2<|im_end|>\n<|im_start|>user\nWhat is 2+2?<|im_end|>\n<|im_start|>assistant\n繁\n
```

> [!info] Reasoning tokens
> Nemotron 3 uses `繁` (token ID 12) and `沁` (token ID 13) for reasoning. Use `--special` to see tokens in llama.cpp; `--verbose-prompt` may be needed to see `繁` since it's prepended.

## Run Nemotron-3-Nano-4B

### Unsloth Studio Guide

1. **Install** — MacOS, Linux, WSL:
   ```bash
   curl -fsSL https://unsloth.ai/install.sh | sh
   ```
   Windows PowerShell:
   ```bash
   irm https://unsloth.ai/install.ps1 | iex
   ```

2. **Launch** — all platforms:
   ```bash
   unsloth studio -H 0.0.0.0 -p 8888
   ```
   Open `http://localhost:8888`.

3. **Download** — create password on first launch, skip onboarding wizard. In Studio Chat tab, search "Nemotron-3-Nano-4B" and download desired quant.

4. **Run** — inference parameters auto-set; manually adjustable. See [[099-new-studio-chat|Studio inference guide]].

### Llama.cpp Tutorial

#### Build llama.cpp

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

Set `-DGGML_CUDA=OFF` for CPU-only inference.

#### Hugging Face Direct Pull

General instruction:
```bash
./llama.cpp/llama-cli \
    -hf unsloth/NVIDIA-Nemotron-3-Nano-4B-GGUF:Q8_0 \
    --ctx-size 16384 \
    --temp 1.0 --top-p 1.0
```

Tool calling:
```bash
./llama.cpp/llama-cli \
    -hf unsloth/NVIDIA-Nemotron-3-Nano-4B-GGUF:Q8_0 \
    --ctx-size 32768 \
    --temp 0.6 --top-p 0.95
```

#### Download Model

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/NVIDIA-Nemotron-3-Nano-4B-GGUF",
    local_dir = "unsloth/NVIDIA-Nemotron-3-Nano-4B-GGUF",
    allow_patterns = ["*Q8_0*"],
)
```

#### Run Conversation Mode

```bash
./llama.cpp/llama-cli \
    --model unsloth/NVIDIA-Nemotron-3-Nano-4B-GGUF/NVIDIA-Nemotron-3-Nano-4B-Q8_0.gguf \
    --ctx-size 16384 \
    --seed 3407 \
    --prio 2 \
    --temp 0.6 \
    --top-p 0.95
```

> [!warning] Context window
> Ensure hardware can handle >256K context. Setting to 1M may trigger CUDA OOM — default is 262,144.

## Run Nemotron-3-Nano-30B-A3B

### Unsloth Studio Guide

1. **Install** — MacOS, Linux, WSL:
   ```bash
   curl -fsSL https://unsloth.ai/main/install.sh | sh
   ```
   Windows PowerShell:
   ```bash
   irm https://unsloth.ai/install.ps1 | iex
   ```

2. **Setup** (one-time) — auto-installs Node.js (nvm), builds frontend, installs Python deps, builds llama.cpp with CUDA.

> [!warning] First install takes 5-10 min (llama.cpp compilation). Do not cancel.

> [!info] WSL users: prompted for `sudo` password for build deps (`cmake`, `git`, `libcurl4-openssl-dev`).

3. **Launch** — MacOS, Linux, WSL:
   ```bash
   source unsloth_studio/bin/activate
   unsloth studio -H 0.0.0.0 -p 8888
   ```
   Windows PowerShell:
   ```bash
   & .\unsloth_studio\Scripts\unsloth.exe studio -H 0.0.0.0 -p 8888
   ```
   Open `http://localhost:8888`.

4. **Download** — search "Nemotron-3-Nano-30B-A3B" in Studio Chat.

5. **Run** — inference auto-set; see [[099-new-studio-chat|Studio inference guide]].

### Llama.cpp Tutorial

#### Build llama.cpp

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

Set `-DGGML_CUDA=OFF` for CPU-only. For Apple Mac/Metal: set `-DGGML_CUDA=OFF` — Metal on by default.

#### Hugging Face Direct Pull

General instruction:
```bash
./llama.cpp/llama-cli \
    -hf unsloth/Nemotron-3-Nano-30B-A3B-GGUF:UD-Q4_K_XL \
    --ctx-size 32768 \
    --temp 1.0 --top-p 1.0
```

Tool calling:
```bash
./llama.cpp/llama-cli \
    -hf unsloth/Nemotron-3-Nano-30B-A3B-GGUF:UD-Q4_K_XL \
    --ctx-size 32768 \
    --temp 0.6 --top-p 0.95
```

#### Download Model

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Nemotron-3-Nano-30B-A3B-GGUF",
    local_dir = "unsloth/Nemotron-3-Nano-30B-A3B-GGUF",
    allow_patterns = ["*UD-Q4_K_XL*"],
)
```

#### Run Conversation Mode

```bash
./llama.cpp/llama-cli \
    --model unsloth/Nemotron-3-Nano-30B-A3B-GGUF/Nemotron-3-Nano-30B-A3B-UD-Q4_K_XL.gguf \
    --ctx-size 16384 \
    --seed 3407 \
    --prio 2 \
    --temp 0.6 \
    --top-p 0.95
```

## Fine-tuning Nemotron 3 and RL

All Nemotron models supported (Super and Nano). 4B fits on free Colab GPU; 30B does not. 16-bit LoRA fine-tuning uses ~**60GB VRAM**.

- [Nemotron-3-Nano-30B-A3B SFT LoRA notebook (80GB A100 Colab)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Nemotron-3-Nano-30B-A3B_A100.ipynb)

> [!warning] MoE fine-tuning
> Router layer fine-tuning disabled by default (not recommended). To maintain reasoning capabilities, use dataset with >=75% reasoning + <=25% non-reasoning examples.

### Reinforcement Learning + NeMo Gym

Single-turn rollout RL training via [NVIDIA NeMo Gym](https://github.com/NVIDIA-NeMo/Gym/pull/492) for math, coding, tool-use domains:

- [NeMo Gym Sudoku RL notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/nemo_gym_sudoku.ipynb)
- [NeMo Gym Multi-Environment RL notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/NeMo-Gym-Multi-Environment.ipynb)

> [!tip] NVIDIA Developer blog collab
> [How to Fine-Tune an LLM on NVIDIA GPUs With Unsloth](https://blogs.nvidia.com/blog/rtx-ai-garage-fine-tuning-unsloth-dgx-spark/)

## Llama-server Serving & Deployment

Deploy Nemotron-3-Nano-30B-A3B via `llama-server`:

```bash
./llama.cpp/llama-server \
    --model unsloth/Nemotron-3-Nano-30B-A3B-GGUF/Nemotron-3-Nano-30B-A3B-UD-Q4_K_XL.gguf \
    --alias "unsloth/Nemotron-3-Nano-30B-A3B" \
    --prio 3 \
    --min_p 0.01 \
    --temp 0.6 \
    --top-p 0.95 \
    --ctx-size 16384 \
    --port 8001
```

Client usage (`pip install openai`):

```python
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/Nemotron-3-Nano-30B-A3B",
    messages = [{"role": "user", "content": "What is 2+2?"},],
)
print(completion.choices[0].message.content)
```

## Benchmarks

- Nemotron-3-Nano-4B: best performing model for its size, including throughput.
- Nemotron-3-Nano-30B-A3B: best performing across all benchmarks, including throughput.

## Agent Instructions: Querying This Documentation

```
GET https://unsloth.ai/docs/models/nemotron-3.md?ask=<question>
```

#nemotron-3 #llm-guide #inference #gguf #fine-tuning
