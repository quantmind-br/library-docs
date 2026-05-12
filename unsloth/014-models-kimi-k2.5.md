---
title: 'Kimi K2.5: How to Run Locally Guide'
url: https://unsloth.ai/docs/models/kimi-k2.5.md
source: llms
fetched_at: 2026-04-27T18:13:47.498788749-03:00
rendered_js: false
word_count: 2399
summary: This guide provides instructions on how to run the high-performing Kimi-K2.5 language model locally, detailing hardware requirements, recommended usage parameters, and step-by-step methods for running it in both Unsloth Studio and llama.cpp environments.
tags:
    - kimi-k2.5
    - model-guide
    - local-inference
    - gguf
    - unsloth
    - llm
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Kimi K2.5: How to Run Locally Guide

Kimi-K2.5 by Moonshot — 1T parameter hybrid reasoning model, SOTA in vision, coding, agentic, and chat. Full model: 630GB (4x H200 GPUs). Unsloth Dynamic 1.8-bit quant: 240GB (-60%). GGUF: [unsloth/Kimi-K2.5-GGUF](https://huggingface.co/unsloth/Kimi-K2.5-GGUF)

All uploads use Unsloth [Dynamic 2.0](https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs) for SOTA Aider and 5-shot MMLU performance. See [coding benchmarks](https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs/unsloth-dynamic-ggufs-on-aider-polyglot).

### Recommended Requirements

> [!info] Need **>240GB disk** for the 1-bit quant. For best speed, total available memory (VRAM + RAM) should exceed the quantized model file size. If not, llama.cpp can run via SSD/HDD offloading (slower).

| Quant | Size | Memory | Speed |
|---|---|---|---|
| UD-TQ1_0 (1.8-bit) | 240 GB | 24 GB GPU + ~256 GB RAM (offload) | ~10 tok/s |
| UD-Q2_K_XL (2-bit) | 375 GB | Recommended balance | 10+ tok/s |
| Full model | 630 GB | 4x H200 GPUs | >40 tok/s (B200 if fits) |

- For near **full precision**: use 4-bit or 5-bit quants (model was originally released in INT4)
- Rule of thumb: RAM+VRAM = quant size; otherwise slower via offloading
- Below ~240GB unified memory: speed drops from ~10 tok/s to <2 tok/s

## Run Kimi K2.5 Guide

Currently **no vision support** in llama.cpp (expected soon).

> [!tip] To run in full precision, use 4-bit or 5-bit Dynamic GGUFs (e.g. UD_Q4_K_XL) — model was originally INT4. Higher-bit quants are unnecessary but safe.

### Usage Guide

Moonshot AI recommended inference settings:

| Setting | Default (Instant Mode) | Thinking Mode |
|---|---|---|
| temperature | 0.6 | 1.0 |
| top_p | 0.95 | 0.95 |
| min_p | 0.01 | 0.01 |

- Set **temperature 1.0** for thinking mode to reduce repetition/incoherence
- Suggested context length = 98,304 (up to 256K)
- Different tools may require different settings

> [!info] Set **min_p = 0.01** to suppress unlikely low-probability tokens. Disable or set **repeat_penalty = 1.0** if needed.

#### Chat Template

`tokenizer.apply_chat_template([{"role": "user", "content": "What is 1+1?"},])` produces:

```
<|im_system|>system<|im_middle|>You are Kimi, an AI assistant created by Moonshot AI.<|im_end|><|im_user|>user<|im_middle|>What is 1+1?<|im_end|><|im_assistant|>assistant<|im_middle|>
```

### Run Kimi-K2.5 in Unsloth Studio

[Unsloth Studio](https://unsloth.ai/docs/new/studio) — open-source web UI for local AI. MacOS, Windows, Linux.

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

   Open `http://localhost:8888`

3. **Search & download** — First launch: create password, sign in, skip onboarding wizard. Go to [Studio Chat](https://unsloth.ai/docs/new/studio/chat), search **Kimi-K2.5**, download desired model/quant. Ensure sufficient compute.
4. **Run** — Inference parameters auto-set; see [[099-new-studio-chat|Studio inference guide]] for manual adjustments.

### Run Kimi K2.5 in llama.cpp

Guide uses smallest 1-bit quant (240GB). Change to 2-bit, 3-bit, etc. as needed. For near full precision, use 4-bit or 5-bit quants.

1. Build llama.cpp:

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

Set `-DGGML_CUDA=OFF` for CPU-only or Apple Mac/Metal (Metal is on by default).

2. Run directly from Hugging Face:

> [!tip] `LLAMA_SET_ROWS=1` makes llama.cpp faster. `--fit on` auto-fits models on all GPUs/CPUs optimally.

```bash
export LLAMA_CACHE="unsloth/Kimi-K2.5-GGUF"
LLAMA_SET_ROWS=1 ./llama.cpp/llama-cli \
    -hf unsloth/Kimi-K2.5-GGUF:UD-TQ1_0\
    --temp 1.0 \
    --min-p 0.01 \
    --top-p 0.95 \
    --ctx-size 16384 \
    --seed 3407
```

3. **MoE offloading options** — `--fit on` auto-fits. If not using `--fit on`:

> [!info] Use `--fit on` first. If it doesn't work, try MoE offloading:

| Flag | Effect | VRAM needed |
|---|---|---|
| `-ot ".ffn_.*_exps.=CPU"` | Offload all MoE layers to CPU (baseline) | Least |
| `-ot ".ffn_(up\|down)_exps.=CPU"` | Offload up + down projection MoE only | Medium |
| `-ot ".ffn_(up)_exps.=CPU"` | Offload only up projection MoE | Most |

Custom regex example: `-ot "\.(6|7|8|9|[0-9][0-9]|[0-9][0-9][0-9])\.ffn_(gate|up|down)_exps.=CPU"` — offloads gate/up/down MoE from layer 6 onward.

With ~360GB combined GPU memory, remove `-ot ".ffn_.*_exps.=CPU"` for maximum speed.

3. Download via Hugging Face (`pip install huggingface_hub hf_transfer`):

```bash
pip install -U huggingface_hub
hf download unsloth/Kimi-K2.5-GGUF \
    --local-dir unsloth/Kimi-K2.5-GGUF \
    --include "*UD-TQ1_0*" # Use "*UD-Q2_K_XL*" for Dynamic 2bit
```

Recommended: UD-Q2_K_XL for size/quality balance. All versions: [huggingface.co/unsloth/Kimi-K2.5-GGUF](https://huggingface.co/unsloth/K2.5-GGUF). If downloads get stuck, see [[124-basics-troubleshooting-and-faqs-hugging-face-hub-xet-debugging|HF XET debugging]].

4. Run with local file:

```bash
LLAMA_SET_ROWS=1 ./llama.cpp/llama-cli \
    --model unsloth/Kimi-K2.5-GGUF/UD-TQ1_0/Kimi-K2.5-UD-TQ1_0-00001-of-00005.gguf \
    --temp 1.0 \
    --min_p 0.01 \
    --top-p 0.95 \
    --ctx-size 16384 \
    --seed 3407
```

5. Edit `--ctx-size 16384` for context length. Omit for auto discovery via `--fit on`.

### Deploy with llama-server and OpenAI's completion library

> [!tip] `--kv-unified` makes inference serving faster in llama.cpp. See [reddit discussion](https://www.reddit.com/r/LocalLLaMA/comments/1qnwa33/glm_47_flash_huge_performance_improvement_with_kvu/).

After building llama.cpp, launch OpenAI-compatible server:

```bash
LLAMA_SET_ROWS=1 ./llama.cpp/llama-server \
    --model unsloth/Kimi-K2.5-GGUF/UD-TQ1_0/Kimi-K2.5-UD-TQ1_0-00001-of-00005.gguf \
    --special \
    --alias "unsloth/Kimi-K2.5" \
    --min_p 0.01 \
    --ctx-size 16384 \
    --port 8001 \
    --kv-unified
```

Use with OpenAI Python library (`pip install openai`):

```python
from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/Kimi-K2.5",
    messages = [{"role": "user", "content": "What is 1+1?"},],
)
print(completion.choices[0].message.content)
```

### Benchmarks

#### Reasoning & Knowledge

| Benchmark | Kimi K2.5 | GPT-5.2 | Claude 4.5 Opus | Gemini 3 Pro | DeepSeek V3.2 | Qwen3-VL-235B-A22B-Thinking |
|---|---:|---:|---:|---:|---:|---:|
| HLE-Full | 30.1 | 34.5 | 30.8 | 37.5 | 25.1† | - |
| HLE-Full (w/ tools) | 50.2 | 45.5 | 43.2 | 45.8 | 40.8† | - |
| AIME 2025 | 96.1 | 100 | 92.8 | 95.0 | 93.1 | - |
| HMMT 2025 (Feb) | 95.4 | 99.4 | 92.9\* | 97.3\* | 92.5 | - |
| IMO-AnswerBench | 81.8 | 86.3 | 78.5\* | 83.1\* | 78.3 | - |
| GPQA-Diamond | 87.6 | 92.4 | 87.0 | 91.9 | 82.4 | - |
| MMLU-Pro | 87.1 | 86.7\* | 89.3\* | 90.1 | 85.0 | - |

#### Image & Video

| Benchmark | Kimi K2.5 | GPT-5.2 | Claude 4.5 Opus | Gemini 3 Pro | DeepSeek V3.2 | Qwen3-VL-235B-A22B-Thinking |
|---|---:|---:|---:|---:|---:|---:|
| MMMU-Pro | 78.5 | 79.5\* | 74.0 | 81.0 | - | 69.3 |
| CharXiv (RQ) | 77.5 | 82.1 | 67.2\* | 81.4 | - | 66.1 |
| MathVision | 84.2 | 83.0 | 77.1\* | 86.1\* | - | 74.6 |
| MathVista (mini) | 90.1 | 82.8\* | 80.2\* | 89.8\* | - | 85.8 |
| ZeroBench | 9 | 9\* | 3\* | 8\* | - | 4\* |
| ZeroBench (w/ tools) | 11 | 7\* | 9\* | 12\* | - | 3\* |
| OCRBench | 92.3 | 80.7\* | 86.5\* | 90.3\* | - | 87.5 |
| OmniDocBench 1.5 | 88.8 | 85.7 | 87.7\* | 88.5 | - | 82.0\* |
| InfoVQA (val) | 92.6 | 84\* | 76.9\* | 57.2\* | - | 89.5 |
| SimpleVQA | 71.2 | 55.8\* | 69.7\* | 69.7\* | - | 56.8\* |
| WorldVQA | 46.3 | 28.0 | 36.8 | 47.4 | - | 23.5 |
| VideoMMMU | 86.6 | 85.9 | 84.4\* | 87.6 | - | 80.0 |
| MMVU | 80.4 | 80.8\* | 77.3 | 77.5 | - | 71.1 |
| MotionBench | 70.4 | 64.8 | 60.3 | 70.3 | - | - |
| VideoMME | 87.4 | 86.0\* | - | 88.4\* | - | 79.0 |
| LongVideoBench | 79.8 | 76.5\* | 67.2\* | 77.7\* | - | 65.6\* |
| LVBench | 75.9 | - | - | 73.5\* | - | 63.6 |

#### Coding

| Benchmark | Kimi K2.5 | GPT-5.2 | Claude 4.5 Opus | Gemini 3 Pro | DeepSeek V3.2 | Qwen3-VL-235B-A22B-Thinking |
|---|---:|---:|---:|---:|---:|---:|
| SWE-Bench Verified | 76.8 | 80.0 | 80.9 | 76.2 | 73.1 | - |
| SWE-Bench Pro | 50.7 | 55.6 | 55.4\* | - | - | - |
| SWE-Bench Multilingual | 73.0 | 72.0 | 77.5 | 65.0 | 70.2 | - |
| Terminal Bench 2.0 | 50.8 | 54.0 | 59.3 | 54.2 | 46.4 | - |
| PaperBench | 63.5 | 63.7\* | 72.9\* | - | 47.1 | - |
| CyberGym | 41.3 | - | 50.6 | 39.9\* | 17.3\* | - |
| SciCode | 48.7 | 52.1 | 49.5 | 56.1 | 38.9 | - |
| OJBench (cpp) | 57.4 | - | 54.6\* | 68.5\* | 54.7\* | - |
| LiveCodeBench (v6) | 85.0 | - | 82.2\* | 87.4\* | 83.3 | - |

#### Long Context

| Benchmark | Kimi K2.5 | GPT-5.2 | Claude 4.5 Opus | Gemini 3 Pro | DeepSeek V3.2 | Qwen3-VL-235B-A22B-Thinking |
|---|---:|---:|---:|---:|---:|---:|
| Longbench v2 | 61.0 | 54.5\* | 64.4\* | 68.2\* | 59.8\* | - |
| AA-LCR | 70.0 | 72.3\* | 71.3\* | 65.3\* | 64.3\* | - |

#### Agentic Search

| Benchmark | Kimi K2.5 | GPT-5.2 | Claude 4.5 Opus | Gemini 3 Pro | DeepSeek V3.2 | Qwen3-VL-235B-A22B-Thinking |
|---|---:|---:|---:|---:|---:|---:|
| BrowseComp | 60.6 | 65.8 | 37.0 | 37.8 | 51.4 | - |
| BrowseComp (w/ctx manage) | 74.9 | 65.8 | 57.8 | 59.2 | 67.6 | - |
| BrowseComp (Agent Swarm) | 78.4 | - | - | - | - | - |
| WideSearch (item-f1) | 72.7 | - | 76.2\* | 57.0 | 32.5\* | - |
| WideSearch (item-f1 Agent Swarm) | 79.0 | - | - | - | - | - |
| DeepSearchQA | 77.1 | 71.3\* | 76.1\* | 63.2\* | 60.9\* | - |
| FinSearchCompT2&T3 | 67.8 | - | 66.2\* | 49.9 | 59.1\* | - |
| Seal-0 | 57.4 | 45.0 | 47.7\* | 45.5\* | 49.5\* | - |

#### Notes

- `*` = score re-evaluated by authors (not publicly available previously)
- `†` = DeepSeek V3.2 score corresponds to text-only subset
- `-` = not evaluated / not available

---

# Agent Instructions: Querying This Documentation

If you need additional information not directly available on this page, query the documentation dynamically:

```
GET https://unsloth.ai/docs/models/kimi-k2.5.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language. The response will contain a direct answer with relevant excerpts and sources.

#model-guide #kimi-k2.5 #local-inference #gguf #llm
