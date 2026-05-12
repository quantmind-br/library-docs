---
title: MiniMax-M2.7 - How to Run Locally
url: https://unsloth.ai/docs/models/minimax-m27.md
source: llms
fetched_at: 2026-04-27T18:13:39.989157651-03:00
rendered_js: false
word_count: 1310
summary: This document provides a comprehensive guide on how to run the open MiniMax-M2.7 model locally, detailing optimal settings for performance and providing step-by-step instructions for both Unsloth Studio and llama.cpp environments.
tags:
    - minimax-m2.7
    - local-inference
    - gguf-quantization
    - unsloth
    - llama-cpp
    - model-running
    - performance-guide
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:42:00Z
---

# MiniMax-M2.7 - How to Run Locally

MiniMax-M2.7: 230B parameters (10B active), 200K context window, successor to [[039-models-tutorials-minimax-m25|MiniMax-M2.5]]. SOTA in SWE-Pro (56.22%) and Terminal Bench 2 (57.0%). Unquantized bf16 = 457GB; [[115-basics-unsloth-dynamic-2.0-ggufs|Dynamic 4-bit]] = 108GB (-60%). GGUF: [MiniMax-M2.7-GGUF](https://huggingface.co/unsloth/MiniMax-M2.7-GGUF)

## Usage Guide

| Quant | Disk | Fits On | Speed |
|-------|------|---------|-------|
| `UD-IQ4_XS` (4-bit dynamic) | 108 GB | 128GB unified memory Mac | ~15+ tok/s |
| `UD-IQ4_XS` + 1x16GB GPU + 96GB RAM | 108 GB | Desktop with GPU | 25+ tok/s |
| `Q8_0` (8-bit, near full precision) | 243 GB | 256GB RAM device/Mac | 15+ tok/s |

> [!tip] Total available memory (VRAM + RAM) should exceed the quant file size. If not, llama.cpp offloads to SSD/HDD but inference is slower.

### Recommended Settings

| Parameter | Value |
|-----------|-------|
| `temperature` | 1.0 |
| `top_p` | 0.95 |
| `top_k` | 40 |
| Max context window | 196,608 |

Default system prompt: `You are a helpful assistant. Your name is MiniMax-M2.7 and is built by MiniMax.`

> [!warning] Do NOT use CUDA 13.2 to run any model — may cause gibberish or poor outputs. NVIDIA is working on a fix.

## Run MiniMax-M2.7 Tutorials

### Unsloth Studio

[[097-new-studio|Unsloth Studio]] — open-source web UI for local AI. Auto-offloads to RAM, detects multi-GPU.

1. **Install** (MacOS/Linux/WSL):

```bash
curl -fsSL https://unsloth.ai/install.sh | sh
```

Windows PowerShell:

```bash
irm https://unsloth.ai/install.ps1 | iex
```

2. **Launch**:

```bash
unsloth studio -H 0.0.0.0 -p 8888
```

Open `http://localhost:8888`. Create a password on first launch.

3. **Download**: Search for **MiniMax-M2.7** in Studio Chat tab. Choose `UD-IQ4_XS` or other quants (e.g., `UD-Q4_K_XL`). If downloads get stuck, see [[124-basics-troubleshooting-and-faqs-hugging-face-hub-xet-debugging|HF XET debugging]].

4. **Run**: Inference parameters auto-set; editable manually. See [[099-new-studio-chat|Studio inference guide]].

### llama.cpp

1. **Build** llama.cpp (set `-DGGML_CUDA=OFF` for CPU-only or Apple Metal):

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

2. **Run from HF**:

```bash
export LLAMA_CACHE="unsloth/MiniMax-M2.7-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/MiniMax-M2.7-GGUF:UD-IQ4_XS \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 40
```

3. **Download** (`pip install huggingface_hub hf_transfer`):

```bash
hf download unsloth/MiniMax-M2.7-GGUF \
    --local-dir unsloth/MiniMax-M2.7-GGUF \
    --include "*UD-IQ4_XS*" # Use "*Q8_0*" for 8-bit
```

4. **Conversation mode** (adjust `--threads`, `--ctx-size`, `--n-gpu-layers` as needed):

```bash
./llama.cpp/llama-cli \
    --model unsloth/MiniMax-M2.7-GGUF/UD-IQ4_XS/MiniMax-M2.7-UD-IQ4_XS-00001-of-00004.gguf \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 40
```

### llama-server & OpenAI API

Deploy for production via `llama-server`:

```bash
./llama.cpp/llama-server \
    --model unsloth/MiniMax-M2.7-GGUF/UD-IQ4_XS/MiniMax-M2.7-UD-IQ4_XS-00001-of-00004.gguf \
    --alias "unsloth/MiniMax-M2.7" \
    --prio 3 \
    --temp 1.0 \
    --top-p 0.95 \
    --min-p 0.01 \
    --top-k 40 \
    --port 8001
```

Then with `pip install openai`:

```python
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/MiniMax-M2.7",
    messages = [{"role": "user", "content": "Create a Snake game."},],
)
print(completion.choices[0].message.content)
```

## Benchmarks

### GGUF Benchmarks (KLD 99%)

Key findings from [Benjamin Marie's third-party benchmark](https://x.com/bnjmn_marie/status/2027043753484021810/photo/1) (750-prompt mixed suite: LiveCodeBench v6, MMLU Pro, GPQA, Math500):

- **Best quality/size tradeoff**: `unsloth UD-Q4_K_XL` — only 6.0 points down from original, +22.8% more errors
- **Other Q4 quants cluster** (~64.5-64.9 accuracy): `IQ4_NL`, `MXFP4_MOE`, `UD-IQ2_XXS` all ~33-35% more errors
- Unsloth GGUFs significantly outperform non-Unsloth GGUFs (e.g., `lmstudio-community Q4_K_M`, `AesSedai IQ3_S`) despite being 8GB smaller

M2.7 GGUF benchmarks are very similar to M2.5 (same architecture).

#minimax-m2.7 #local-inference #gguf-quantization #llama-cpp #unsloth
