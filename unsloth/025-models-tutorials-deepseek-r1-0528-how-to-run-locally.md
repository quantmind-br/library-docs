---
title: 'DeepSeek-R1-0528: How to Run Locally'
url: https://unsloth.ai/docs/models/tutorials/deepseek-r1-0528-how-to-run-locally.md
source: llms
fetched_at: 2026-04-27T18:14:22.51911908-03:00
rendered_js: false
word_count: 1487
summary: This document provides a comprehensive guide and reference for running, fine-tuning, and utilizing DeepSeek-R1-0528 models. It details various quantized versions (like 1.66-bit) and offers recommended settings and tutorials for deployment in environments like llama.cpp and Ollama.
tags:
    - deepseek-r1
    - llm-model
    - gguf-quantization
    - unsloth
    - local-deployment
    - inference-guide
category: tutorial
optimized: true
optimized_at: 2026-04-27T22:15:00Z
---

# DeepSeek-R1-0528: How to Run Locally

DeepSeek-R1-0528 update to the R1 reasoning model. Full 671B = 715GB disk. Dynamic **1.66-bit** quant = 162GB (80% reduction). GGUF: [DeepSeek-R1-0528-GGUF](https://huggingface.co/unsloth/DeepSeek-R1-0528-GGUF)

Distill via Qwen3 (8B) achieves performance near Qwen3 (235B). Fine-tune Qwen3 distill with Unsloth. Qwen3 GGUF: [DeepSeek-R1-0528-Qwen3-8B-GGUF](https://huggingface.co/unsloth/DeepSeek-R1-0528-Qwen3-8B-GGUF)

All uploads use Unsloth [Dynamic 2.0](https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs) for SOTA 5-shot MMLU and KL Divergence performance -- quantized DeepSeek LLMs with minimal accuracy loss.

> [!tip] NEW: TQ1_0 dynamic 1.66-bit quant -- 162GB. Ideal for 192GB RAM (incl. Mac) and Ollama. Try: `ollama run hf.co/unsloth/DeepSeek-R1-0528-GGUF:TQ1_0`

## Recommended Settings

- **Qwen3-8B distill** -- fits any setup, even 20GB RAM. No prep needed.
- **Full R1-0528 (715GB)** -- needs extra prep. IQ1_S quant fits 1x 24GB GPU (all layers offloaded) at ~5 tok/s with 128GB RAM bonus. Minimum 64GB RAM (1 tok/s without GPU). Optimal: **180GB unified memory or 180GB combined RAM+VRAM** for 5+ tok/s.
- Recommended quants for size/accuracy balance: 2.7bit (Q2_K_XL) or 2.4bit (IQ2_XXS).

> [!tip] For best performance, set VRAM + RAM = size of quant you're downloading.

### Official Recommended Settings (from [DeepSeek](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528))

- **temperature 0.6** -- reduce repetition/incoherence
- **top_p 0.95**
- Run multiple tests and average for reliable evaluation

### Chat template / prompt format

R1-0528 uses the same chat template as original R1. No need to force `.reasoning\n` but you can add it.

```
<｜begin▁of▁sentence｜><｜User｜>What is 1+1?<｜Assistant｜>It's 2.<｜end▁of▁sentence｜><｜User｜>Explain more!<｜Assistant｜>
```

BOS forcibly added; EOS separates each interaction. Counteract double BOS: call `tokenizer.encode(..., add_special_tokens = False)` since chat template auto-adds BOS.

For llama.cpp / GGUF inference, skip BOS (auto-added):

```
<｜User｜>What is 1+1?<｜Assistant｜>
```

The `.reasoning` and `.think` tokens get their own designated tokens.

## Model Uploads

ALL uploads use calibration dataset optimized for conversational, coding, and language tasks.

- **Qwen3 (8B) distill**: [DeepSeek-R1-0528-Qwen3-8B-GGUF](https://huggingface.co/unsloth/DeepSeek-R1-0528-Qwen3-8B-GGUF)
- [IQ4_NL](https://huggingface.co/unsloth/DeepSeek-R1-0528-GGUF/tree/main/IQ4_NL) -- faster for ARM devices
- [Q4_1](https://huggingface.co/unsloth/DeepSeek-R1-0528-GGUF/tree/main/Q4_1) -- faster for Apple devices
- [BF16 format](https://huggingface.co/unsloth/DeepSeek-R1-0528-BF16)
- [FP8 (float8) format](https://huggingface.co/unsloth/DeepSeek-R1-0528)

### Full model quantizations

| MoE Bits | Type + Link | Disk Size | Details |
|----------|------------|-----------|---------|
| 1.66bit | [TQ1_0](https://huggingface.co/unsloth/DeepSeek-R1-0528-GGUF?show_file_info=DeepSeek-R1-0528-UD-TQ1_0.gguf) | **162GB** | 1.92/1.56bit |
| 1.78bit | [IQ1_S](https://huggingface.co/unsloth/DeepSeek-R1-0528-GGUF/tree/main/UD-IQ1_S) | **185GB** | 2.06/1.56bit |
| 1.93bit | [IQ1_M](https://huggingface.co/unsloth/DeepSeek-R1-0528-GGUF/tree/main/UD-IQ1_M) | **200GB** | 2.5/2.06/1.56 |
| 2.42bit | [IQ2_XXS](https://huggingface.co/unsloth/DeepSeek-R1-0528-GGUF/tree/main/UD-IQ2_XXS) | **216GB** | 2.5/2.06bit |
| 2.71bit | [Q2_K_XL](https://huggingface.co/unsloth/DeepSeek-R1-0528-GGUF/tree/main/UD-Q2_K_XL) | **251GB** | 3.5/2.5bit |
| 3.12bit | [IQ3_XXS](https://huggingface.co/unsloth/DeepSeek-R1-0528-GGUF/tree/main/UD-IQ3_XXS) | **273GB** | 3.5/2.06bit |
| 3.5bit | [Q3_K_XL](https://huggingface.co/unsloth/DeepSeek-R1-0528-GGUF/tree/main/UD-Q3_K_XL) | **296GB** | 4.5/3.5bit |
| 4.5bit | [Q4_K_XL](https://huggingface.co/unsloth/DeepSeek-R1-0528-GGUF/tree/main/UD-Q4_K_XL) | **384GB** | 5.5/4.5bit |
| 5.5bit | [Q5_K_XL](https://huggingface.co/unsloth/DeepSeek-R1-0528-GGUF/tree/main/UD-Q5_K_XL) | **481GB** | 6.5/5.5bit |

## Run DeepSeek-R1-0528 Tutorials

### Run in Ollama/Open WebUI

1. Install Ollama (models up to 32B only). For full 720GB model, see [Run Full R1-0528 on Ollama](#run-full-r1-0528-on-ollamaopen-webui).

```bash
apt-get update
apt-get install pciutils -y
curl -fsSL https://ollama.com/install.sh | sh
```

2. Run Qwen3-8B distill. Use `ollama serve` in another terminal if it fails. All fixes and suggested params (temperature etc.) included in `params` in HuggingFace upload.

```bash
ollama run hf.co/unsloth/DeepSeek-R1-0528-Qwen3-8B-GGUF:Q4_K_XL
```

3. **NEW** -- full R1-0528 via TQ1_0 (162GB):

```bash
OLLAMA_MODELS=unsloth_downloaded_models ollama serve &

ollama run hf.co/unsloth/DeepSeek-R1-0528-GGUF:TQ1_0
```

### Run Full R1-0528 on Ollama/Open WebUI

Open WebUI step-by-step for R1: [docs.openwebui.com/tutorials/integrations/deepseekr1-dynamic/](https://docs.openwebui.com/tutorials/integrations/deepseekr1-dynamic/) -- replace R1 with 0528 quant.

**NEW** full model via TQ1_0:

```bash
OLLAMA_MODELS=unsloth_downloaded_models ollama serve &

ollama run hf.co/unsloth/DeepSeek-R1-0528-GGUF:TQ1_0
```

For quants larger than TQ1_0 on Ollama, merge 3 GGUF split files first:

```bash
./llama.cpp/llama-gguf-split --merge \
  DeepSeek-R1-0528-GGUF/DeepSeek-R1-0528-UD-IQ1_S/DeepSeek-R1-0528-UD-IQ1_S-00001-of-00003.gguf \
	merged_file.gguf
```

### Run Qwen3 distilled R1 in llama.cpp

1. For **full 720GB model**, see [Run Full R1-0528 on llama.cpp](#run-full-r1-0528-on-llamacpp). Get latest `llama.cpp` from [GitHub](https://github.com/ggml-org/llama.cpp). Change `-DGGML_CUDA=ON` to `-DGGML_CUDA=OFF` for CPU-only. **Apple Mac / Metal**: set `-DGGML_CUDA=OFF` -- Metal on by default.

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

2. Download and run Qwen3-8B distill directly:

```bash
./llama.cpp/llama-cli -hf unsloth/DeepSeek-R1-0528-Qwen3-8B-GGUF:Q4_K_XL --jinja
```

### Run Full R1-0528 on llama.cpp

1. Build llama.cpp (same as above, with extra targets):

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-quantize llama-cli llama-gguf-split llama-mtmd-cli
cp llama.cpp/build/bin/llama-* llama.cpp
```

2. Run via HuggingFace pull. `(IQ1_S)` = quantization type. Use `export LLAMA_CACHE="folder"` to save to specific location.

> [!tip] MoE offloading: `-ot ".ffn_.*_exps.=CPU"` offloads all MoE layers to CPU -- fits all non-MoE layers on 1 GPU. More GPU memory options:
> - `-ot ".ffn_(up|down)_exps.=CPU"` -- up/down projection MoE layers
> - `-ot ".ffn_(up)_exps.=CPU"` -- only up projection MoE layers
> - `-ot "\.(6|7|8|9|[0-9][0-9]|[0-9][0-9][0-9])\.ffn_(gate|up|down)_exps.=CPU"` -- offload gate/up/down MoE from layer 6+

```bash
export LLAMA_CACHE="unsloth/DeepSeek-R1-0528-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/DeepSeek-R1-0528-GGUF:IQ1_S \
    --cache-type-k q4_0 \
    --threads -1 \
    --n-gpu-layers 99 \
    --prio 3 \
    --temp 0.6 \
    --top-p 0.95 \
    --min-p 0.01 \
    --ctx-size 16384 \
    --seed 3407 \
    -ot ".ffn_.*_exps.=CPU"
```

3. Download via Python (`pip install huggingface_hub hf_transfer`). Recommend **`UD-Q2_K_XL`** (dynamic 2.7bit, 251GB) for size/accuracy balance. More versions: [https://huggingface.co/unsloth/DeepSeek-R1-0528-GGUF](https://huggingface.co/unsloth/DeepSeek-V3-0324-GGUF)

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0" # Can sometimes rate limit, so set to 0 to disable
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/DeepSeek-R1-0528-GGUF",
    local_dir = "unsloth/DeepSeek-R1-0528-GGUF",
    allow_patterns = ["*UD-IQ1_S*"], # Dynamic 1bit (168GB) Use "*UD-Q2_K_XL*" for Dynamic 2bit (251GB)
)
```

4. Run Flappy Bird test (see [[026-models-tutorials-deepseek-r1-how-to-run-locally|DeepSeek R1 1.58bit guide]]).

5. Tune `--threads 32` (CPU threads), `--ctx-size 16384` (context length), `--n-gpu-layers 2` (GPU offloading). Remove GPU flags for CPU-only.

```bash
./llama.cpp/llama-cli \
    --model unsloth/DeepSeek-R1-0528-GGUF/UD-IQ1_S/DeepSeek-R1-0528-UD-IQ1_S-00001-of-00004.gguf \
    --cache-type-k q4_0 \
    --threads -1 \
    --n-gpu-layers 99 \
    --prio 3 \
    --temp 0.6 \
    --top-p 0.95 \
    --min-p 0.01 \
    --ctx-size 16384 \
    --seed 3407 \
    -ot ".ffn_.*_exps.=CPU" \
    -no-cnv \
    --prompt "<｜User｜>Create a Flappy Bird game in Python. You must include these things:\n1. You must use pygame.\n2. The background color should be randomly chosen and is a light shade. Start with a light blue color.\n3. Pressing SPACE multiple times will accelerate the bird.\n4. The bird's shape should be randomly chosen as a square, circle or triangle. The color should be randomly chosen as a dark color.\n5. Place on the bottom some land colored as dark brown or yellow chosen randomly.\n6. Make a score shown on the top right side. Increment if you pass pipes and don't hit them.\n7. Make randomly spaced pipes with enough space. Color them randomly as dark green or light brown or a dark gray shade.\n8. When you lose, show the best score. Make the text inside the screen. Pressing q or Esc will quit the game. Restarting is pressing SPACE again.\nThe final game should be inside a markdown section in Python. Check your code for errors and fix them before the final markdown section.<｜Assistant｜>"
```

## Heptagon Test

Test dynamic quants via [r/Localllama](https://www.reddit.com/r/LocalLLaMA/comments/1j7r47l/i_just_made_an_animation_of_a_ball_bouncing/) -- physics engine simulating balls rotating in a moving enclosed heptagon shape.

<details>
<summary>Full prompt to run the model</summary>

```bash
./llama.cpp/llama-cli \
    --model unsloth/DeepSeek-R1-0528-GGUF/UD-IQ1_S/DeepSeek-R1-0528-UD-IQ1_S-00001-of-00004.gguf \
    --cache-type-k q4_0 \
    --threads -1 \
    --n-gpu-layers 99 \
    --prio 3 \
    --temp 0.6 \
    --top_p 0.95 \
    --min_p 0.01 \
    --ctx-size 16384 \
    --seed 3407 \
    -ot ".ffn_.*_exps.=CPU" \
    -no-cnv \
    --prompt "<｜User｜>Write a Python program that shows 20 balls bouncing inside a spinning heptagon:\n- All balls have the same radius.\n- All balls have a number on it from 1 to 20.\n- All balls drop from the heptagon center when starting.\n- Colors are: #f8b862, #f6ad49, #f39800, #f08300, #ec6d51, #ee7948, #ed6d3d, #ec6800, #ec6800, #ee7800, #eb6238, #ea5506, #ea5506, #eb6101, #e49e61, #e45e32, #e17b34, #dd7a56, #db8449, #d66a35\n- The balls should be affected by gravity and friction, and they must bounce off the rotating walls realistically. There should also be collisions between balls.\n- The material of all the balls determines that their impact bounce height will not exceed the radius of the heptagon, but higher than ball radius.\n- All balls rotate with friction, the numbers on the ball can be used to indicate the spin of the ball.\n- The heptagon is spinning around its center, and the speed of spinning is 360 degrees per 5 seconds.\n- The heptagon size should be large enough to contain all the balls.\n- Do not use the pygame library; implement collision detection algorithms and collision response etc. by yourself. The following Python libraries are allowed: tkinter, math, numpy, dataclasses, typing, sys.\n- All codes should be put in a single Python file.<｜Assistant｜>"
```

</details>

## Fine-tuning DeepSeek-R1-0528 with Unsloth

GRPO notebook with custom reward function for multilingual output -- increases desired-language response rate by 40%+ (example: Indonesian). No language dataset needed.

- [**DeepSeek-R1-0528-Qwen3-8B GRPO notebook**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/DeepSeek_R1_0528_Qwen3_\(8B\)_GRPO.ipynb)

Reward function is fully customizable for other languages, domains, or use cases. Unsloth makes R1-Qwen3 distill fine-tuning 2x faster, uses 70% less VRAM, supports 8x longer context lengths.

---

# Agent Instructions: Querying This Documentation

For additional information not on this page, query dynamically via HTTP GET:

```
GET https://unsloth.ai/docs/models/tutorials/deepseek-r1-0528-how-to-run-locally.md?ask=<question>
```

Question should be specific, self-contained, natural language. Response includes direct answer with relevant excerpts and sources.

#deepseek-r1 #gguf-quantization #local-deployment #llm-inference
