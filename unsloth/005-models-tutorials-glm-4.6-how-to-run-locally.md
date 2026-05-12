---
title: 'GLM-4.6: Run Locally Guide'
url: https://unsloth.ai/docs/models/tutorials/glm-4.6-how-to-run-locally.md
source: llms
fetched_at: 2026-04-27T18:14:17.917066113-03:00
rendered_js: false
word_count: 1921
summary: This document serves as a guide explaining how to run GLM-4.6 and the smaller GLM-4.6V-Flash models locally, detailing necessary setup steps, configuration fixes like the required `--jinja` flag for llama.cpp, and providing recommended inference settings.
tags:
    - glm-4.6
    - local-inference
    - gguf
    - unsloth
    - llm-guide
    - chat-template
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# GLM-4.6: Run Locally Guide

GLM-4.6 and **GLM-4.6V-Flash** (9B, released Dec 2025 with vision support) are Z.ai reasoning models with SOTA coding/agent performance and improved chat.

- **Full 355B** — 400GB disk; **Unsloth Dynamic 2-bit GGUF** — 135GB (−75%). [GLM-4.6-GGUF](https://huggingface.co/unsloth/GLM-4.6-GGUF)
- All uploads use Unsloth [[115-basics-unsloth-dynamic-2.0-ggufs|Dynamic 2.0]] for SOTA 5-shot MMLU and Aider performance.

> [!warning] Must use `--jinja` for llama.cpp quants
> Unsloth fixed chat template bugs for GLM-4.6. Without `--jinja`, multi-turn conversations break (second prompt onward). Non-Unsloth GGUFs still have this issue.

## Unsloth Chat Template & Bug Fixes

Fixed a bug where the second prompt in GGUFs wouldn't work. With Unsloth's chat template, conversations beyond the second work correctly. Some tool-calling issues remain — reported to the GLM team.

## GLM 4.6V Flash Quirks and Fixes

> [!info] GLM-4.6V-Flash may reason in Chinese
> Not unique to Unsloth quants — all providers' BF16/Q8_0 quants do this. Fix: use system prompt `"Respond in English and reason in English"`.

**Without system prompt** — reasons in Chinese:

```bash
./llama.cpp/llama-cli -hf unsloth/GLM-4.6V-Flash-GGUF:BF16 \
    --jinja --temp 0.8 --top-p 0.6 --top-k 2 --repeat-penalty 1.1 --min-p 0.0 --seed 3407 \
    --prompt "Create a Flappy Bird game in Python" --system-prompt "Respond in English"
```

**With `"Respond in English and reason in English"`** — reasoning and output in English:

```bash
./llama.cpp/llama-cli -hf unsloth/GLM-4.6V-Flash-GGUF:BF16 \
    --jinja --temp 0.8 --top-p 0.6 --top-k 2 --repeat-penalty 1.1 --min-p 0.0 --seed 3407 \
    --prompt "Create a Flappy Bird game in Python" \
    --system-prompt "Respond in English and reason in English"
```

## Usage Guide

UD-Q2_K_XL (2-bit dynamic quant) uses 135GB disk — works in **1x24GB GPU + 128GB RAM** with MoE offloading. UD-TQ1 (1-bit) **works natively in Ollama**.

> [!warning] Must use `--jinja` for llama.cpp quants
> Enables correct fixed chat templates. Incorrect results without it.

4-bit quants fit in **1x40GB GPU** (MoE offloaded to RAM). ~5 tok/s with 165GB+ RAM. Recommended: 205GB+ RAM for 4-bit.

> [!tip] VRAM + RAM = quant size (best performance)
> If not, SSD offloading works with llama.cpp (slower inference).

## Recommended Settings

| GLM-4.6V-Flash | GLM-4.6 |
|---|---|
| **temperature = 0.8** | **temperature = 1.0** |
| **top_p = 0.6** (recommended) | **top_p = 0.95** (recommended for coding) |
| **top_k = 2** (recommended) | **top_k = 40** (recommended for coding) |
| **128K context length** or less | **200K context length** or less |
| **repeat_penalty = 1.1** | |
| **max_generate_tokens = 16,384** | **max_generate_tokens = 16,384** |

- Use `--jinja` for llama.cpp — chat template fixes included.

## Run GLM-4.6 Tutorials

Guides for [GLM-4.6V-Flash](#glm-4.6v-flash) and [GLM-4.6](#glm-4.6).

### GLM-4.6V-Flash

> [!success] NEW as of Dec 16, 2025: GLM-4.6-V now has vision support!

#### Run in llama.cpp

**1. Build llama.cpp** — [GitHub](https://github.com/ggml-org/llama.cpp). `-DGGML_CUDA=OFF` for CPU-only. Metal (Apple) on by default.

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

**2. Run directly** — `:Q8_K_XL` is the quant type. Use `export LLAMA_CACHE="folder"` to force save location. Max 128K context.

```bash
export LLAMA_CACHE="unsloth/GLM-4.6V-Flash-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/GLM-4.6V-Flash-GGUF:UD-Q8_K_XL \
    --n-gpu-layers 99 \
    --jinja \
    --ctx-size 16384 \
    --flash-attn on \
    --temp 0.8 \
    --top-p 0.6 \
    --top-k 2 \
    --repeat_penalty 1.1 \
    -ot ".ffn_.*_exps.=CPU"
```

**3. Download via Hugging Face:**

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0" # Can sometimes rate limit, so set to 0 to disable
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/GLM-4.6V-Flash-GGUF",
    local_dir = "unsloth/GLM-4.6V-Flash-GGUF",
    allow_patterns = ["*UD-Q8_K_XL*"],
)
```

### GLM-4.6

#### Run in Ollama

**1. Install:**

```bash
apt-get update
apt-get install pciutils -y
curl -fsSL https://ollama.com/install.sh | sh
```

**2. Run:**

```
OLLAMA_MODELS=unsloth ollama serve &

OLLAMA_MODELS=unsloth ollama run hf.co/unsloth/GLM-4.6-GGUF:TQ1_0
```

**3. Other quants** — merge split GGUF files first:

```bash
./llama.cpp/llama-gguf-split --merge \
  GLM-4.6-GGUF/GLM-4.6-UD-Q2_K_XL/GLM-4.6-UD-Q2_K_XL-00001-of-00003.gguf \
	merged_file.gguf
```

```bash
OLLAMA_MODELS=unsloth ollama serve &

OLLAMA_MODELS=unsloth ollama run merged_file.gguf
```

#### Run in llama.cpp

**1. Build llama.cpp** — [GitHub](https://github.com/ggml-org/llama.cpp). `-DGGML_CUDA=OFF` for CPU-only.

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggerganov/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-quantize llama-cli llama-gguf-split llama-mtmd-cli llama-server
cp llama.cpp/build/bin/llama-* llama.cpp
```

**2. Run directly** — `:Q2_K_XL` quant type. Use `export LLAMA_CACHE="folder"` to force save location. Max 128K context.

> [!tip] MoE offloading via `-ot` regex
> - `-ot ".ffn_.*_exps.=CPU"` — all MoE layers to CPU (least VRAM)
> - `-ot ".ffn_(up|down)_exps.=CPU"` — up+down projection
> - `-ot ".ffn_(up)_exps.=CPU"` — up projection only (most VRAM)
> - Custom: `-ot "\.(6|7|8|9|[0-9][0-9]|[0-9][0-9][0-9])\.ffn_(gate|up|down)_exps.=CPU"` — from layer 6+

```bash
export LLAMA_CACHE="unsloth/GLM-4.6-GGUF"
./llama.cpp/llama-cli \
    --model GLM-4.6-GGUF/UD-Q2_K_XL/GLM-4.6-UD-Q2_K_XL-00001-of-00003.gguf \
    --n-gpu-layers 99 \
    --jinja \
    --ctx-size 16384 \
    --flash-attn on \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 40 \
    -ot ".ffn_.*_exps.=CPU"
```

**3. Download via Hugging Face** — recommend **2.7-bit dynamic quant `UD-Q2_K_XL`** for size/accuracy balance.

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0" # Can sometimes rate limit, so set to 0 to disable
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/GLM-4.6-GGUF",
    local_dir = "unsloth/GLM-4.6-GGUF",
    allow_patterns = ["*UD-Q2_K_XL*"], # Dynamic 2bit Use "*UD-TQ1_0*" for Dynamic 1bit
)
```

**4. Run from local file** — adjust `--threads`, `--ctx-size`, `--n-gpu-layers` as needed.

```bash
./llama.cpp/llama-cli \
    --model unsloth/GLM-4.6-GGUF/UD-Q2_K_XL/GLM-4.6-UD-Q2_K_XL-00001-of-00003.gguf \
    --jinja \
    --n-gpu-layers 99 \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 40 \
    --ctx-size 16384 \
    --seed 3407 \
    -ot ".ffn_.*_exps.=CPU"
```

### Deploy with llama-server and OpenAI completion library

```bash
./llama.cpp/llama-server \
    --model unsloth/GLM-4.6-GGUF/UD-Q2_K_XL/GLM-4.6-UD-Q2_K_XL-00001-of-00003.gguf \
    --alias "unsloth/GLM-4.6" \
    --n-gpu-layers 999 \
    -ot ".ffn_.*_exps.=CPU" \
    --prio 3 \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 40 \
    --ctx-size 16384 \
    --port 8001 \
    --jinja
```

Then use OpenAI Python library (`pip install openai`):

```python
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/GLM-4.6",
    messages = [{"role": "user", "content": "What is 2+2?"},],
)
print(completion.choices[0].message.content)
```

### Model Uploads

All uploads use Unsloth calibration dataset optimized for conversational, coding, and language tasks.

Also uploaded [IQ4_NL](https://huggingface.co/unsloth/DeepSeek-V3.1-GGUF/tree/main/IQ4_NL) (ARM) and [Q4_1](https://huggingface.co/unsloth/DeepSeek-V3.1-GGUF/tree/main/Q4_1) (Apple) for faster inference on those devices.

| MoE Bits | Type + Link | Disk Size | Details |
|---|---|---|---|
| 1.66 | [TQ1_0](https://huggingface.co/unsloth/GLM-4.6-GGUF?show_file_info=GLM-4.6-UD-TQ1_0.gguf) | **84GB** | 1.92/1.56bit |
| 1.78 | [IQ1_S](https://huggingface.co/unsloth/GLM-4.6-GGUF/tree/main/UD-IQ1_S) | **96GB** | 2.06/1.56bit |
| 1.93 | [IQ1_M](https://huggingface.co/unsloth/GLM-4.6-GGUF/tree/main/UD-IQ1_M) | **107GB** | 2.5/2.06/1.56 |
| 2.42 | [IQ2_XXS](https://huggingface.co/unsloth/GLM-4.6-GGUF/tree/main/UD-IQ2_XXS) | **115GB** | 2.5/2.06bit |
| 2.71 | [Q2_K_XL](https://huggingface.co/unsloth/GLM-4.6-GGUF/tree/main/UD-Q2_K_XL) | **135GB** | 3.5/2.5bit |
| 3.12 | [IQ3_XXS](https://huggingface.co/unsloth/GLM-4.6-GGUF/tree/main/UD-IQ3_XXS) | **145GB** | 3.5/2.06bit |
| 3.5 | [Q3_K_XL](https://huggingface.co/unsloth/GLM-4.6-GGUF/tree/main/UD-Q3_K_XL) | **158GB** | 4.5/3.5bit |
| 4.5 | [Q4_K_XL](https://huggingface.co/unsloth/GLM-4.6-GGUF/tree/main/UD-Q4_K_XL) | **204GB** | 5.5/4.5bit |
| 5.5 | [Q5_K_XL](https://huggingface.co/unsloth/GLM-4.6-GGUF/tree/main/UD-Q5_K_XL) | **252GB** | 6.5/5.5bit |

### Improving generation speed

MoE offloading `-ot` options (more VRAM = fewer layers offloaded):
- `-ot ".ffn_.*_exps.=CPU"` — all MoE layers (least VRAM)
- `-ot ".ffn_(up|down)_exps.=CPU"` — up+down projection
- `-ot ".ffn_(up)_exps.=CPU"` — up projection only
- Custom regex: `-ot "\.(6|7|8|9|[0-9][0-9]|[0-9][0-9][0-9])\.ffn_(gate|up|down)_exps.=CPU"` — from layer 6+

High throughput mode: `llama-parallel` ([docs](https://github.com/ggml-org/llama.cpp/tree/master/examples/parallel)). KV cache quantization to 4-bit reduces VRAM/RAM movement and speeds generation.

### How to fit long context (full 200K)

**KV cache quantization** reduces K/V caches to lower bits, enabling longer context and faster generation.

K quant options (default `f16`): `f32, f16, bf16, q8_0, q4_0, q4_1, iq4_nl, q5_0, q5_1`

- Use `_1` variants (`q4_1, q5_1`) for better accuracy (slightly slower).

V cache quantization requires **Flash Attention**: compile llama.cpp with `-DGGML_CUDA_FA_ALL_QUANTS=ON`, use `--flash-attn`.

V quant options: `f32, f16, bf16, q8_0, q4_0, q4_1, iq4_nl, q5_0, q5_1`

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://unsloth.ai/docs/models/tutorials/glm-4.6-how-to-run-locally.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

#glm-4-6 #local-inference #gguf #unsloth #chat-template
