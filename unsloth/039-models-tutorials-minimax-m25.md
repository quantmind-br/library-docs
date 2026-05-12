---
title: 'MiniMax-M2.5: How to Run Guide'
url: https://unsloth.ai/docs/models/tutorials/minimax-m25.md
source: llms
fetched_at: 2026-04-27T18:14:00.735914275-03:00
rendered_js: false
word_count: 956
summary: This document serves as a comprehensive guide to running the MiniMax-M2.5 Large Language Model, detailing recommended settings, quantization options (like 3-bit GGUF), and providing step-by-step tutorials for deployment using llama.cpp, Llama-server, or directly via OpenAI's API.
tags:
    - llm-guide
    - minimax-m2.5
    - gguf-quantization
    - llama-cpp
    - api-usage
    - unsloth
category: guide
optimized: true
optimized_at: 2026-04-27T22:00:00Z
---

# MiniMax-M2.5: How to Run Guide

MiniMax-M2.5: 230B params (10B active), 200K context. Unquantized bf16: 457GB. Unsloth Dynamic 3-bit GGUF: **101GB (-62%)** — [MiniMax-M2.5 GGUF](https://huggingface.co/unsloth/MiniMax-M2.5-GGUF). Uses [[115-basics-unsloth-dynamic-2.0-ggufs|Unsloth Dynamic 2.0]] — 3-bit has important layers upcasted to 8/16-bit.

Scores: SWE-Bench Verified 80.2%, Multi-SWE-Bench 51.3%, BrowseComp 76.3%.

> [!tip] Unsloth GGUF quants benchmarked on 750-prompt mixed suite — see benchmarks below.

## Hardware Fit

| Quant | Size | Fits |
|---|---|---|
| UD-Q3_K_XL (3-bit dynamic) | 101GB | 128GB unified Mac (~20+ tok/s); 1x16GB GPU + 96GB RAM (25+ tok/s) |
| 2-bit quants | smaller | 96GB device |
| Q8_0 (8-bit) | 243GB | 256GB RAM/Mac (~10+ tok/s) |

> [!tip] Total memory (VRAM + RAM) should exceed quantized model size. llama.cpp can offload to SSD/HDD but inference will be slower.

## Recommended Settings (MiniMax)

- **temperature = 1.0**, **top_p = 0.95**, **top_k = 40**
- **Max context window:** 196,608
- **Min_P = 0.01** (default might be 0.05)
- **repeat penalty = 1.0** or disabled
- Default system prompt:

```
You are a helpful assistant. Your name is MiniMax-M2.5 and is built by MiniMax.
```

## Run in llama.cpp

Tutorials below use the 3-bit [UD-Q3_K_XL](https://huggingface.co/unsloth/MiniMax-M2.5-GGUF?show_file_info=UD-Q3_K_XL%2FMiniMax-M2.5-UD-Q3_K_XL-00001-of-00004.gguf) quant (fits 128GB RAM).

### 1. Build llama.cpp

From [GitHub](https://github.com/ggml-org/llama.cpp). Use `-DGGML_CUDA=OFF` for CPU-only or Apple Mac (Metal on by default).

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

### 2. Quick run via HuggingFace

```bash
export LLAMA_CACHE="unsloth/MiniMax-M2.5-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/MiniMax-M2.5-GGUF:UD-Q3_K_XL \
    --ctx-size 16384 \
    --flash-attn on \
    --temp 1.0 \
    --top-p 0.95 \
    --min-p 0.01 \
    --top-k 40
```

### 3. Download model

Requires `pip install huggingface_hub hf_transfer`. If downloads get stuck, see [[124-basics-troubleshooting-and-faqs-hugging-face-hub-xet-debugging]].

```bash
hf download unsloth/MiniMax-M2.5-GGUF \
    --local-dir unsloth/MiniMax-M2.5-GGUF \
    --include "*UD-Q3_K_XL*" # Use "*Q8_0*" for 8-bit
```

### 4. Run with local file

Adjust `--threads 32` (CPU threads), `--ctx-size 16384` (max 200K), `--n-gpu-layers 2` (GPU offload; adjust if OOM; remove for CPU-only).

```bash
./llama.cpp/llama-cli \
    --model unsloth/MiniMax-M2.5-GGUF/UD-Q3_K_XL/MiniMax-M2.5-UD-Q3_K_XL-00001-of-00004.gguf \
    --temp 1.0 \
    --top-p 0.95 \
    --min-p 0.01 \
    --top-k 40 \
    --ctx-size 16384 \
    --seed 3407
```

## Llama-server & OpenAI API

Deploy for production via `llama-server` (run in tmux):

```bash
./llama.cpp/llama-server \
    --model unsloth/MiniMax-M2.5-GGUF/UD-Q3_K_XL/MiniMax-M2.5-UD-Q3_K_XL-00001-of-00004.gguf \
    --alias "unsloth/MiniMax-M2.5" \
    --prio 3 \
    --temp 1.0 \
    --top-p 0.95 \
    --min-p 0.01 \
    --top-k 40 \
    --ctx-size 16384 \
    --port 8001
```

Then connect via OpenAI client (`pip install openai`):

```python
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/MiniMax-M2.5",
    messages = [{"role": "user", "content": "Create a Snake game."},],
)
print(completion.choices[0].message.content)
```

## Benchmarks

### Unsloth GGUF Benchmarks

[Benjamin Marie (third-party)](https://x.com/bnjmn_marie/status/2027043753484021810/photo/1) benchmarked MiniMax-M2.5 using Unsloth GGUFs on a 750-prompt mixed suite (LiveCodeBench v6, MMLU Pro, GPQA, Math500), reporting overall accuracy and relative error increase vs. original.

- **Best quality/size tradeoff: `unsloth UD-Q4_K_XL`** — closest to original: only 6.0 points down, +22.8% more errors.
- Other Unsloth Q4 quants perform closely (~64.5-64.9 accuracy): `IQ4_NL`, `MXFP4_MOE`, `UD-IQ2_XXS` (~33-35% more errors).
- Unsloth GGUFs outperform non-Unsloth GGUFs (e.g. `lmstudio-community - Q4_K_M`, `AesSedai - IQ3_S`), despite being 8GB smaller.

### Official Benchmarks

| Benchmark | MiniMax-M2.5 | MiniMax-M2.1 | Claude Opus 4.5 | Claude Opus 4.6 | Gemini 3 Pro | GPT-5.2 (thinking) |
|---|---|---|---|---|---|---|
| AIME25 | 86.3 | 83.0 | 91.0 | 95.6 | 96.0 | 98.0 |
| GPQA-D | 85.2 | 83.0 | 87.0 | 90.0 | 91.0 | 90.0 |
| SciCode | 44.4 | 41.0 | 50.0 | 52.0 | 56.0 | 52.0 |
| IFBench | 70.0 | 70.0 | 58.0 | 53.0 | 70.0 | 75.0 |
| AA-LCR | 69.5 | 62.0 | 74.0 | 71.0 | 71.0 | 73.0 |
| SWE-Bench Verified | 80.2 | 74.0 | 80.9 | 80.8 | 78.0 | 80.0 |
| SWE-Bench Pro | 55.4 | 49.7 | 56.9 | 55.4 | 54.1 | 55.6 |
| Terminal Bench 2 | 51.7 | 47.9 | 53.4 | 55.1 | 54.0 | 54.0 |
| HLE w/o tools | 19.4 | 22.2 | 28.4 | 30.7 | 37.2 | 31.4 |
| Multi-SWE-Bench | 51.3 | 47.2 | 50.0 | 50.3 | 42.7 | — |
| SWE-Bench Multilingual | 74.1 | 71.9 | 77.5 | 77.8 | 65.0 | 72.0 |
| VIBE-Pro (AVG) | 54.2 | 42.4 | 55.2 | 55.6 | 36.9 | — |
| BrowseComp (w/ctx) | 76.3 | 62.0 | 67.8 | 84.0 | 59.2 | 65.8 |
| Wide Search | 70.3 | 63.2 | 76.2 | 79.4 | 57.0 | — |
| RISE | 50.2 | 34.0 | 50.5 | 62.5 | 36.8 | 50.0 |
| BFCL multi-turn | 76.8 | 37.4 | 68.0 | 63.3 | 61.0 | — |
| Tau^2 Telecom | 97.8 | 87.0 | 98.2 | 99.3 | 98.0 | 98.7 |
| MEWC | 74.4 | 55.6 | 82.1 | 89.8 | 78.7 | 41.3 |
| GDPval-MM | 59.0 | 24.6 | 61.1 | 73.5 | 28.1 | 54.5 |
| Finance Modeling | 21.6 | 17.3 | 30.1 | 33.2 | 15.0 | 20.0 |

#minimax-m2.5 #gguf #llama-cpp #inference #api
