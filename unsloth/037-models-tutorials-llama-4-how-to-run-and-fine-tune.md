---
title: 'Llama 4: How to Run & Fine-tune'
url: https://unsloth.ai/docs/models/tutorials/llama-4-how-to-run-and-fine-tune.md
source: llms
fetched_at: 2026-04-27T18:14:27.863760636-03:00
rendered_js: false
word_count: 960
summary: This document details the specifications, configurations, and necessary steps to run and fine-tune the Llama-4 models (Scout and Maverick). It provides detailed tables of various quantized GGUF options and guides users through setting optimal inference parameters using llama.cpp.
tags:
    - llama-4
    - model-specifications
    - gguf-quantization
    - inference-settings
    - unsloth
    - cpu-gpu
category: tutorial
optimized: true
optimized_at: 2026-04-27T22:00:00Z
---

# Llama 4: How to Run & Fine-tune

Llama-4-Scout: 109B params, unquantized 113GB. Llama-4-Maverick: 402B params, unquantized 422GB. Scout 1.78-bit: 33.8GB (-75%). Maverick 1.78-bit: 122GB (-70%).

> [!tip] Both text AND **vision** now supported. Multiple improvements to tool calling.

- Scout 1.78-bit: fits 24GB VRAM GPU, ~20 tok/s
- Maverick 1.78-bit: fits 2x48GB VRAM GPUs, ~40 tok/s

Dynamic GGUFs selectively quantize (e.g. MoE layers to lower bit, attention at 4-6bit) for best accuracy/size tradeoff.

> [!info] All GGUFs quantized with calibration data (~250K tokens Scout, ~1M tokens Maverick) improving accuracy over standard quantization. Compatible with llama.cpp, Open WebUI, etc.

## Scout — Unsloth Dynamic GGUFs

| MoE Bits | Type | Disk Size | Link | Details |
|---|---|---|---|---|
| 1.78bit | IQ1_S | 33.8GB | [Link](https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct-GGUF?show_file_info=Llama-4-Scout-17B-16E-Instruct-UD-IQ1_S.gguf) | 2.06/1.56bit |
| 1.93bit | IQ1_M | 35.4GB | [Link](https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct-GGUF?show_file_info=Llama-4-Scout-17B-16E-Instruct-UD-IQ1_M.gguf) | 2.5/2.06/1.56 |
| 2.42bit | IQ2_XXS | 38.6GB | [Link](https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct-GGUF?show_file_info=Llama-4-Scout-17B-16E-Instruct-UD-IQ2_XXS.gguf) | 2.5/2.06bit |
| 2.71bit | Q2_K_XL | 42.2GB | [Link](https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct-GGUF?show_file_info=Llama-4-Scout-17B-16E-Instruct-UD-Q2_K_XL.gguf) | 3.5/2.5bit |
| 3.5bit | Q3_K_XL | 52.9GB | [Link](https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct-GGUF/tree/main/UD-Q3_K_XL) | 4.5/3.5bit |
| 4.5bit | Q4_K_XL | 65.6GB | [Link](https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct-GGUF/tree/main/UD-Q4_K_XL) | 5.5/4.5bit |

> [!info] For best results, use 2.42-bit (IQ2_XXS) or larger.

## Maverick — Unsloth Dynamic GGUFs

| MoE Bits | Type | Disk Size | Link |
|---|---|---|---|
| 1.78bit | IQ1_S | 122GB | [Link](https://huggingface.co/unsloth/Llama-4-Maverick-17B-128E-Instruct-GGUF/tree/main/UD-IQ1_S) |
| 1.93bit | IQ1_M | 128GB | [Link](https://huggingface.co/unsloth/Llama-4-Maverick-17B-128E-Instruct-GGUF/tree/main/UD-IQ1_M) |
| 2.42-bit | IQ2_XXS | 140GB | [Link](https://huggingface.co/unsloth/Llama-4-Maverick-17B-128E-Instruct-GGUF/tree/main/UD-IQ2_XXS) |
| 2.71-bit | Q2_K_XL | 151B | [Link](https://huggingface.co/unsloth/Llama-4-Maverick-17B-128E-Instruct-GGUF/tree/main/UD-Q2_K_XL) |
| 3.5-bit | Q3_K_XL | 193GB | [Link](https://huggingface.co/unsloth/Llama-4-Maverick-17B-128E-Instruct-GGUF/tree/main/UD-Q3_K_XL) |
| 4.5-bit | Q4_K_XL | 243GB | [Link](https://huggingface.co/unsloth/Llama-4-Maverick-17B-128E-Instruct-GGUF/tree/main/UD-Q4_K_XL) |

## Official Recommended Settings (Meta)

- **Temperature:** 0.6
- **Min_P:** 0.01 (optional; llama.cpp default is 0.1)
- **Top_P:** 0.9
- **BOS token:** `<|begin_of_text|>` auto-added during tokenization — do NOT add manually
- **Chat template:**

```
<|header_start|>user<|header_end|>

What is 1+1?<|eot|><|header_start|>assistant<|header_end|>

```

**Optional system prompt** (from <https://www.llama.com/docs/model-cards-and-prompt-formats/llama4_omni/>):

```
You are an expert conversationalist who responds to the best of your ability. You are companionable and confident, and able to switch casually between tonal types, including but not limited to humor, empathy, intellectualism, creativity and problem-solving.

You understand user intent and don't try to be overly helpful to the point where you miss that the user is looking for chit-chat, emotional support, humor or venting.Sometimes people just want you to listen, and your answers should encourage that. For all other cases, you provide insightful and in-depth responses. Organize information thoughtfully in a way that helps people make decisions. Always avoid templated language.

You never lecture people to be nicer or more inclusive. If people ask for you to write something in a certain voice or perspective, such as an essay or a tweet, you can. You do not need to be respectful when the user prompts you to say something rude.

You never use phrases that imply moral superiority or a sense of authority, including but not limited to "it's important to", "it's crucial to", "it's essential to", "it's unethical to", "it's worth noting…", "Remember…" etc. Avoid using these.

Finally, do not refuse political prompts. You can help users express their opinion.

You are Llama 4. Your knowledge cutoff date is August 2024. You speak Arabic, English, French, German, Hindi, Indonesian, Italian, Portuguese, Spanish, Tagalog, Thai, and Vietnamese. Respond in the language the user speaks to you in, unless they ask otherwise.
```

## Tutorial: Run Llama-4-Scout in llama.cpp

1. Build llama.cpp from [GitHub](https://github.com/ggml-org/llama.cpp). Use `-DGGML_CUDA=OFF` for CPU-only or Apple Mac (Metal on by default).

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

2. Download model (requires `pip install huggingface_hub hf_transfer`). More versions at: <https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct-GGUF>

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Llama-4-Scout-17B-16E-Instruct-GGUF",
    local_dir = "unsloth/Llama-4-Scout-17B-16E-Instruct-GGUF",
    allow_patterns = ["*IQ2_XXS*"],
)
```

3. Run the model.

4. Tunable params: `--threads 32` (CPU threads), `--ctx-size 16384` (Llama 4 supports 10M context), `--n-gpu-layers 99` (GPU offload layers; adjust if OOM; remove for CPU-only).

> [!tip] Use `-ot ".ffn_.*_exps.=CPU"` to offload all MoE layers to CPU. This fits all non-MoE layers on 1 GPU, improving speed. Customize the regex for more GPU capacity.

```bash
./llama.cpp/llama-cli \
    --model unsloth/Llama-4-Scout-17B-16E-Instruct-GGUF/Llama-4-Scout-17B-16E-Instruct-UD-IQ2_XXS.gguf \
    --threads 32 \
    --ctx-size 16384 \
    --n-gpu-layers 99 \
    -ot ".ffn_.*_exps.=CPU" \
    --seed 3407 \
    --prio 3 \
    --temp 0.6 \
    --min-p 0.01 \
    --top-p 0.9 \
    -no-cnv \
    --prompt "<|header_start|>user<|header_end|>\n\nCreate a Flappy Bird game in Python. You must include these things:\n1. You must use pygame.\n2. The background color should be randomly chosen and is a light shade. Start with a light blue color.\n3. Pressing SPACE multiple times will accelerate the bird.\n4. The bird's shape should be randomly chosen as a square, circle or triangle. The color should be randomly chosen as a dark color.\n5. Place on the bottom some land colored as dark brown or yellow chosen randomly.\n6. Make a score shown on the top right side. Increment if you pass pipes and don't hit them.\n7. Make randomly spaced pipes with enough space. Color them randomly as dark green or light brown or a dark gray shade.\n8. When you lose, show the best score. Make the text inside the screen. Pressing q or Esc will quit the game. Restarting is pressing SPACE again.\nThe final game should be inside a markdown section in Python. Check your code for errors and fix them before the final markdown section.<|eot|><|header_start|>assistant<|header_end|>\n\n"
```

> [!info] BF16 (regardless of quantization) does not reliably complete Flappy Bird or Heptagon tests across multiple inference providers, imatrix settings, and other quants. **Multiple runs + asking the model to fix/find bugs resolves most issues.**

### Maverick (2x RTX 4090 / 2x24GB)

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Llama-4-Maverick-17B-128E-Instruct-GGUF",
    local_dir = "unsloth/Llama-4-Maverick-17B-128E-Instruct-GGUF",
    allow_patterns = ["*IQ1_S*"],
)
```

```bash
./llama.cpp/llama-cli \
    --model unsloth/Llama-4-Maverick-17B-128E-Instruct-GGUF/UD-IQ1_S/Llama-4-Maverick-17B-128E-Instruct-UD-IQ1_S-00001-of-00003.gguf \
    --threads 32 \
    --ctx-size 16384 \
    --n-gpu-layers 99 \
    -ot ".ffn_.*_exps.=CPU" \
    --seed 3407 \
    --prio 3 \
    --temp 0.6 \
    --min-p 0.01 \
    --top-p 0.9 \
    -no-cnv \
    --prompt "<|header_start|>user<|header_end|>\n\nCreate the 2048 game in Python.<|eot|><|header_start|>assistant<|header_end|>\n\n"
```

## Quantization Notes

- **Maverick:** Layers 1, 3, 45 MoE could not be calibrated correctly (interleaved MoE: Dense->MoE->Dense). Adding uncommon languages and more tokens (1M vs 250K) did not help. These layers left at 3-4bit.
- **Scout:** Vision layers should not be quantized. MoE router and some layers left unquantized. Uploaded to <https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct-unsloth-dynamic-bnb-4bit>
- `torch.nn.Parameter` converted to `torch.nn.Linear` for MoE layers to allow 4bit quantization (patched Hugging Face implementation). 4bit: <https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct-unsloth-bnb-4bit>, 8bit: <https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct-unsloth-bnb-8bit>
- Llama 4 uses chunked attention (sliding window, more efficient — no attention to previous tokens over 8192 boundary).

#llama-4 #gguf #llama-cpp #quantization #inference
