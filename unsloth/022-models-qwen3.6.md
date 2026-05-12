---
title: Qwen3.6 - How to Run Locally
url: https://unsloth.ai/docs/models/qwen3.6.md
source: llms
fetched_at: 2026-04-27T18:13:29.057652513-03:00
rendered_js: false
word_count: 2160
summary: This document serves as a comprehensive guide on how to run the Qwen3.6 multimodal hybrid-thinking models locally, detailing hardware requirements, recommended inference settings for various modes (Thinking/Instruct), and showcasing features available within Unsloth Studio.
tags:
    - qwen3.6
    - local-inference
    - gguf
    - unsloth-studio
    - model-guide
    - llm-settings
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Qwen3.6 - How to Run Locally

Alibaba's multimodal hybrid-thinking family: **Qwen3.6-27B** and **35B-A3B**. 256K context, 201 languages. Excels in agentic coding, vision, chat. GGUFs use [[115-basics-unsloth-dynamic-2.0-ggufs|Unsloth Dynamic 2.0]] quantization (calibrated on real-world data, important layers upcasted). Supports `developer role` for agentic coding tools. Improved nested-object parsing for tool calling.

## Usage Guide

### Hardware requirements (RAM + VRAM or unified memory)

| Qwen3.6 | 3-bit | 4-bit | 6-bit | 8-bit | BF16 |
| --- | --- | --- | --- | --- | --- |
| **27B** | 15 GB | 18 GB | 24 GB | 30 GB | 55 GB |
| **35B-A3B** | 17 GB | 23 GB | 30 GB | 38 GB | 70 GB |

> [!success]
> Best performance when total memory (VRAM + RAM) exceeds the quantized model file size. llama.cpp can run via SSD/HDD offloading but inference will be slower.

> [!warning]
> **Do NOT use CUDA 13.2** — may produce gibberish outputs. NVIDIA is working on a fix.

To train Qwen3.6, follow the [[020-models-qwen3.5-fine-tune|Qwen3.5 fine-tuning guide]].

### Recommended Settings

- **Max context window:** 262,144 (extendable to 1M via YaRN)
- `presence_penalty = 0.0 to 2.0` — reduces repetitions; higher values may slightly decrease performance
- **Adequate output length:** 32,768 tokens for most queries

> [!info]
> Gibberish output? Context length may be too low. Try `--cache-type-k bf16 --cache-type-v bf16`.

### Thinking mode settings

> [!success]
> Qwen3.6 now has [Preserve Thinking](#thinking-enable-disable--preserve-thinking).

| Setting | General tasks | Precise coding |
| --- | --- | --- |
| temperature | 1.0 | 0.6 |
| top_p | 0.95 | 0.95 |
| top_k | 20 | 20 |
| min_p | 0.0 | 0.0 |
| presence_penalty | 1.5 | 0.0 |
| repeat penalty | disabled or 1.0 | disabled or 1.0 |

```bash
# Thinking - general
temperature=1.0, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=1.5, repetition_penalty=1.0
# Thinking - precise coding
temperature=0.6, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=0.0, repetition_penalty=1.0
```

### Instruct (non-thinking) mode settings

| Setting | General tasks | Reasoning tasks |
| --- | --- | --- |
| temperature | 0.7 | 1.0 |
| top_p | 0.8 | 0.95 |
| top_k | 20 | 20 |
| min_p | 0.0 | 0.0 |
| presence_penalty | 1.5 | 1.5 |
| repeat penalty | disabled or 1.0 | disabled or 1.0 |

> [!warning]
> Disable thinking/reasoning: `--chat-template-kwargs '{"enable_thinking":false}'`

```bash
# Instruct - general
temperature=0.7, top_p=0.8, top_k=20, min_p=0.0, presence_penalty=1.5, repetition_penalty=1.0
# Instruct - reasoning
temperature=1.0, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=1.5, repetition_penalty=1.0
```

## Unsloth Studio Guide

Run and fine-tune in [[097-new-studio|Unsloth Studio]] (MacOS, Windows, Linux). Features: GGUF/safetensor search, self-healing tool calling, web search, code execution, automatic inference tuning, 2x faster training.

1. **Install:**

```bash
# MacOS, Linux, WSL
curl -fsSL https://unsloth.ai/install.sh | sh
# Windows PowerShell
irm https://unsloth.ai/install.ps1 | iex
```

2. **Launch:**

```bash
unsloth studio -H 0.0.0.0 -p 8888
```

Open `http://localhost:8888`.

3. **Search & download** — Go to Studio Chat tab, search "Qwen3.6", download desired model/quant.
4. **Run** — Inference parameters auto-set; edit context length, chat template, and settings manually if needed.

> [!info]
> Currently no Qwen3.6 GGUF works in Ollama due to separate mmproj vision files. Use llama.cpp compatible backends.

## Llama.cpp Guides

Uses Dynamic 4-bit `UD_Q4_K_XL` GGUF variants. Build llama.cpp:

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

Use `-DGGML_CUDA=OFF` for CPU-only or Apple Metal (Metal is on by default).

### Qwen3.6-27B

**Thinking mode (general):**

```bash
export LLAMA_CACHE="unsloth/Qwen3.6-27B-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/Qwen3.6-27B-GGUF:UD-Q4_K_XL \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --presence_penalty=1.5 \
    --min-p 0.00
```

For precise coding: `temperature=0.6, presence-penalty=0.0`

**Non-thinking mode (general):**

```bash
export LLAMA_CACHE="unsloth/Qwen3.6-27B-GGUF"
./llama.cpp/llama-server \
    -hf unsloth/Qwen3.6-27B-GGUF:UD-Q4_K_XL \
    --temp 0.7 \
    --top-p 0.8 \
    --top-k 20 \
    --presence_penalty=1.5 \
    --min-p 0.00 \
    --chat-template-kwargs '{"enable_thinking":false}'
```

For reasoning tasks: `temperature=1.0, top-p=0.95`

### Qwen3.6-35B-A3B

**Thinking mode (general):**

```bash
export LLAMA_CACHE="unsloth/Qwen3.6-35B-A3B-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/Qwen3.6-35B-A3B-GGUF:UD-Q4_K_XL \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --presence_penalty=1.5 \
    --min-p 0.00
```

For precise coding: `temperature=0.6, presence-penalty=0.0`

**Non-thinking mode (general):**

```bash
export LLAMA_CACHE="unsloth/Qwen3.6-35B-A3B-GGUF"
./llama.cpp/llama-server \
    -hf unsloth/Qwen3.6-35B-A3B-GGUF:UD-Q4_K_XL \
    --temp 0.7 \
    --top-p 0.8 \
    --top-k 20 \
    --presence_penalty=1.5 \
    --min-p 0.00 \
    --chat-template-kwargs '{"enable_thinking":false}'
```

For reasoning tasks: `temperature=1.0, top-p=0.95`

### Download GGUF

```bash
hf download unsloth/Qwen3.6-35B-A3B-GGUF \
    --local-dir unsloth/Qwen3.6-35B-A3B-GGUF \
    --include "*mmproj-F16*" \
    --include "*UD-Q4_K_XL*" # Use "*UD-Q2_K_XL*" for Dynamic 2bit
```

Recommend at least 2-bit dynamic quant `UD-Q2_K_XL`. If downloads get stuck, see [[124-basics-troubleshooting-and-faqs-hugging-face-hub-xet-debugging|Hugging Face Hub, XET debugging]].

### Run with mmproj

```bash
./llama.cpp/llama-cli \
    --model unsloth/Qwen3.6-35B-A3B-GGUF/Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf \
    --mmproj unsloth/Qwen3.6-35B-A3B-GGUF/mmproj-F16.gguf \
    --temp 1.0 \
    --top-p 0.95 \
    --min-p 0.00 \
    --presence_penalty=1.5 \
    --top-k 20
```

### Llama-server & OpenAI completion library

Deploy via `llama-server`:

```bash
./llama.cpp/llama-server \
--model unsloth/Qwen3.6-35B-A3B-GGUF/Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf \
    --mmproj unsloth/Qwen3.6-35B-A3B-GGUF/mmproj-F16.gguf \
    --alias "unsloth/Qwen3.6-35B-A3B" \
    --temp 0.6 \
    --top-p 0.95 \
    --ctx-size 16384 \
    --top-k 20 \
    --min-p 0.00 \
    --port 8001
```

Python client:

```python
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/Qwen3.6-35B-A3B",
    messages = [{"role": "user", "content": "Create a Snake game."},],
)
print(completion.choices[0].message.content)
```

## MLX Dynamic Quants (MacOS)

Dynamic 4-bit and 8-bit quants for MacOS. Algorithm still evolving.

**Qwen3.6-27B MLX:**

| [3-bit](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-3bit) | [4-bit](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-4bit) | [MXFP4](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-MXFP4) | [NVFP4](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-NVFP4) | [6-bit](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-6bit) | [8-bit](https://huggingface.co/unsloth/Qwen3.6-27B-MLX-8bit) |
| --- | --- | --- | --- | --- | --- |

**Qwen3.6-35B-A3B MLX:**

| [3-bit](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-UD-MLX-3bit) | [4-bit](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-UD-MLX-4bit) | [8-bit](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MLX-8bit) |
| --- | --- | --- |

```bash
curl -fsSL https://raw.githubusercontent.com/unslothai/unsloth/refs/heads/main/scripts/install_qwen3_6_mlx.sh | sh
source ~/.unsloth/unsloth_qwen3_6_mlx/bin/activate
python -m mlx_vlm.chat --model unsloth/Qwen3.6-27B-UD-MLX-4bit
```

### Qwen3.6-27B MLX benchmarks (lower is better)

| Model | Mean KLD | Median KLD | PPL | P90 KLD | P99.9 KLD | Size |
| --- | --- | --- | --- | --- | --- | --- |
| [8-bit](https://huggingface.co/unsloth/Qwen3.6-27B-MLX-8bit) | 0.0028 | 0.0003 | 4.812 | 0.0019 | 0.192 | 34.7 GB |
| [6-bit](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-6bit) | 0.0037 | 0.0007 | 4.809 | 0.0032 | 0.343 | 30.5 GB |
| [4-bit](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-4bit) | 0.0227 | 0.0053 | 4.821 | 0.0293 | 2.339 | 26.2 GB |
| [NVFP4](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-NVFP4) | 0.0325 | 0.0087 | 4.843 | 0.0466 | 3.693 | 26.2 GB |
| [MXFP4](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-MXFP4) | 0.0479 | 0.0153 | 4.902 | 0.0769 | 4.035 | 25.6 GB |
| [3-bit](https://huggingface.co/unsloth/Qwen3.6-27B-UD-MLX-3bit) | 0.0734 | 0.0223 | 4.976 | 0.1261 | 5.529 | 24.1 GB |

## Thinking: Enable/Disable + Preserve Thinking

**Preserve Thinking** leaves the thinking trace from the previous conversation — increases token usage but may improve accuracy in continued conversations. Unsloth Studio has 'Think' and 'Preserved Thinking' toggles.

Enable preserve thinking in llama.cpp (`true`/`false`):

```bash
--chat-template-kwargs '{"preserve_thinking":true}'
```

Note: use `preserve_thinking` instead of `enable_thinking`/`disable_thinking` for this feature.

### Enable/Disable normal thinking

| llama-server OS | Enable | Disable |
| --- | --- | --- |
| Linux, MacOS, WSL | `--chat-template-kwargs '{"enable_thinking":true}'` | `--chat-template-kwargs '{"enable_thinking":false}'` |
| Windows / Powershell | `--chat-template-kwargs "{\"enable_thinking\":true}"` | `--chat-template-kwargs "{\"enable_thinking\":false}"` |

### Preserve thinking example (Qwen3.6-35B-A3B)

```bash
./llama.cpp/llama-server \
    --model unsloth/Qwen3.6-35B-A3B-GGUF/Qwen3.6-35B-A3B-BF16.gguf \
    --alias "unsloth/Qwen3.6-35B-A3B-GGUF" \
    --temp 0.6 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.00 \
    --port 8001 \
    --chat-template-kwargs '{"preserve_thinking":true}'
```

Python with preserve thinking:

```python
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/Qwen3.6-35B-A3B-GGUF",
    messages = [{"role": "user", "content": "What is 2+2?"},],
)
print(completion.choices[0].message.content)
print(completion.choices[0].message.reasoning_content)
```

## OpenAI Codex & Claude Code

Run via local coding agentic workloads — follow [[077-basics-claude-code|Claude Code]] or [[078-basics-codex|Codex]] guides. Change model name to Qwen3.6 variant, use correct parameters, and point to the `llama-server` endpoint.

## Benchmarks

### Unsloth GGUF Benchmarks

Mean KL Divergence benchmarks for Qwen3.6-35B-A3B GGUFs across providers. Unsloth GGUFs are top-performing in 21 of 22 sizes. Q6_K updated for more Dynamic layers; new `UD-IQ4_NL_XL` quant introduced.

### Official Qwen Benchmarks

See [Qwen3.6-27B](https://unsloth.ai/docs/models/qwen3.6.md) and [Qwen3.6-35B-A3B](https://unsloth.ai/docs/models/qwen3.6.md) official score pages.

---

#qwen3.6 #local-inference #gguf #unsloth-studio #model-guide
