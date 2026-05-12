---
title: Gemma 3 - How to Run Guide
url: https://unsloth.ai/docs/models/tutorials/gemma-3-how-to-run-and-fine-tune.md
source: llms
fetched_at: 2026-04-27T18:14:03.374732011-03:00
rendered_js: false
tags:
    - gemma-3
    - running-guide
    - inference
    - fine-tuning
    - ollama
    - llama-cpp
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Gemma 3 - How to Run Guide

Google's Gemma 3 comes in 270M (new), 1B, 4B, 12B, and 27B sizes. 270M and 1B are text-only; larger models handle text and vision. Unsloth provides GGUFs, running guides, and fine-tuning + [RL](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide) support.

> [!tip] **NEW Aug 14, 2025:** [Gemma 3 (270M) fine-tuning notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_\(270M\).ipynb) and [GGUFs](https://huggingface.co/collections/unsloth/gemma-3-67d12b7e8816ec6efa7e4e5b). See also the [[030-models-tutorials-gemma-3-how-to-run-and-fine-tune-gemma-3n-how-to-run-and-fine-tune|Gemma 3n Guide]].

**Unsloth is the only framework working on float16 machines for Gemma 3 inference and training** (Colab free Tesla T4 GPUs work).

- Fine-tune Gemma 3 (4B) vision: [free Colab notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_\(4B\)-Vision.ipynb)

> [!info] Optimal inference config (per Gemma team): `temperature = 1.0, top_k = 64, top_p = 0.95, min_p = 0.0`

## Unsloth Gemma 3 Uploads (with optimal configs)

| GGUF | Unsloth Dynamic 4-bit Instruct | 16-bit Instruct |
| --- | --- | --- |
| [270M](https://huggingface.co/unsloth/gemma-3-270m-it-GGUF) (new) | [270M](https://huggingface.co/unsloth/gemma-3-270m-it-unsloth-bnb-4bit) | [270M](https://huggingface.co/unsloth/gemma-3-270m-it) |
| [1B](https://huggingface.co/unsloth/gemma-3-1b-it-GGUF) | [1B](https://huggingface.co/unsloth/gemma-3-1b-it-bnb-4bit) | [1B](https://huggingface.co/unsloth/gemma-3-1b) |
| [4B](https://huggingface.co/unsloth/gemma-3-4b-it-GGUF) | [4B](https://huggingface.co/unsloth/gemma-3-4b-it-bnb-4bit) | [4B](https://huggingface.co/unsloth/gemma-3-4b) |
| [12B](https://huggingface.co/unsloth/gemma-3-12b-it-GGUF) | [12B](https://huggingface.co/unsloth/gemma-3-27b-it-unsloth-bnb-4bit) | [12B](https://huggingface.co/unsloth/gemma-3-12b) |
| [27B](https://huggingface.co/unsloth/gemma-3-27b-it-GGUF) | [27B](https://huggingface.co/unsloth/gemma-3-27b-it-bnb-4bit) | [27B](https://huggingface.co/unsloth/gemma-3-27b) |

## Recommended Inference Settings

| Parameter | Value |
| --- | --- |
| Temperature | 1.0 |
| Top_K | 64 |
| Min_P | 0.00 (optional; 0.01 works well; llama.cpp default is 0.1) |
| Top_P | 0.95 |
| Repetition Penalty | 1.0 (disabled in llama.cpp and transformers) |

Chat template:

```text
<bos><start_of_turn>user
Hello!<end_of_turn>
<start_of_turn>model
Hey there!<end_of_turn>
<start_of_turn>user
What is 1+1?<end_of_turn>
<start_of_turn>model\n
```

> [!danger] llama.cpp and other inference engines auto-add `<bos>` -- DO NOT add TWO `<bos>` tokens. Ignore `<bos>` when prompting.

### Running Gemma 3 on Your Phone

Use any mobile app running GGUFs locally on edge devices. After fine-tuning, export to GGUF and run locally. Recommend **Gemma 3 270M** or Gemma 3n for phones due to RAM/thermal constraints.

- [AnythingLLM mobile app](https://github.com/Mintplex-Labs/anything-llm) -- [Android](https://play.google.com/store/apps/details?id=com.anythingllm)
- [ChatterUI](https://github.com/Vali-98/ChatterUI)

> [!success] Replace model name `gemma-3-27b-it-GGUF` with any Gemma model (e.g., `gemma-3-270m-it-GGUF:Q8_K_XL`) in all tutorials.

## Tutorial: How to Run Gemma 3 in Ollama

1. Install Ollama:

```bash
apt-get update
apt-get install pciutils -y
curl -fsSL https://ollama.com/install.sh | sh
```

2. Run the model. Use `ollama serve` in another terminal if it fails. Fixes and suggested params are in `params` in the HF upload:

```bash
ollama run hf.co/unsloth/gemma-3-27b-it-GGUF:Q4_K_XL
```

## Tutorial: How to Run Gemma 3 27B in llama.cpp

1. Build llama.cpp from [GitHub](https://github.com/ggml-org/llama.cpp). Set `-DGGML_CUDA=OFF` for CPU-only or Apple Mac/Metal (Metal is on by default):

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=ON -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-quantize llama-cli llama-gguf-split llama-mtmd-cli
cp llama.cpp/build/bin/llama-* llama.cpp
```

2. Run directly via HF (similar to `ollama run`):

```bash
./llama.cpp/llama-mtmd-cli \
    -hf unsloth/gemma-3-4b-it-GGUF:Q4_K_XL
```

3. **OR** download the model (after `pip install huggingface_hub hf_transfer`). Choose Q4_K_M or other quants (BF16 full precision available). More at: https://huggingface.co/unsloth/gemma-3-27b-it-GGUF

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/gemma-3-27b-it-GGUF",
    local_dir = "unsloth/gemma-3-27b-it-GGUF",
    allow_patterns = ["*Q4_K_XL*", "mmproj-BF16.gguf"], # For Q4_K_M
)
```

4. Conversation mode. Adjust `--threads 32` (CPU threads), `--ctx-size 16384` (Gemma 3 supports 128K context), `--n-gpu-layers 99` (GPU offloading; reduce if OOM; remove for CPU-only):

```bash
./llama.cpp/llama-mtmd-cli \
    --model unsloth/gemma-3-27b-it-GGUF/gemma-3-27b-it-Q4_K_XL.gguf \
    --mmproj unsloth/gemma-3-27b-it-GGUF/mmproj-BF16.gguf \
    --ctx-size 16384 \
    --n-gpu-layers 99 \
    --seed 3407 \
    --prio 2 \
    --temp 1.0 \
    --repeat-penalty 1.0 \
    --min-p 0.01 \
    --top-k 64 \
    --top-p 0.95
```

5. Non-conversation mode (Flappy Bird test):

```bash
./llama.cpp/llama-cli \
    --model unsloth/gemma-3-27b-it-GGUF/gemma-3-27b-it-Q4_K_XL.gguf \
    --ctx-size 16384 \
    --n-gpu-layers 99 \
    --seed 3407 \
    --prio 2 \
    --temp 1.0 \
    --repeat-penalty 1.0 \
    --min-p 0.01 \
    --top-k 64 \
    --top-p 0.95 \
    -no-cnv \
    --prompt "<start_of_turn>user\nCreate a Flappy Bird game in Python. You must include these things:\n1. You must use pygame.\n2. The background color should be randomly chosen and is a light shade. Start with a light blue color.\n3. Pressing SPACE multiple times will accelerate the bird.\n4. The bird's shape should be randomly chosen as a square, circle or triangle. The color should be randomly chosen as a dark color.\n5. Place on the bottom some land colored as dark brown or yellow chosen randomly.\n6. Make a score shown on the top right side. Increment if you pass pipes and don't hit them.\n7. Make randomly spaced pipes with enough space. Color them randomly as dark green or light brown or a dark gray shade.\n8. When you lose, show the best score. Make the text inside the screen. Pressing q or Esc will quit the game. Restarting is pressing SPACE again.\nThe final game should be inside a markdown section in Python. Check your code for errors and fix them before the final markdown section.<end_of_turn>\n<start_of_turn>model\n"
```

> [!danger] Remove `<bos>` -- Gemma 3 auto-adds it.

## Fine-tuning Gemma 3 in Unsloth

**Unsloth is the only framework working on float16 machines for Gemma 3 inference and training** (Colab free Tesla T4 GPUs work).

- [Gemma 3 (270M) notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_\(270M\).ipynb) -- 270M model fine-tuned for chess move prediction
- [Gemma 3 (4B) Text](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_\(4B\).ipynb) or [Vision](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_\(4B\)-Vision.ipynb)
- [[030-models-tutorials-gemma-3-how-to-run-and-fine-tune-gemma-3n-how-to-run-and-fine-tune|Gemma 3n (E4B)]]: [Text](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3N_\(4B\)-Conversational.ipynb) / [Vision](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3N_\(4B\)-Vision.ipynb) / [Audio](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3N_\(4B\)-Audio.ipynb)

> [!warning] Full fine-tune (FFT) on float16 devices: all layers default to float32. Unsloth expects float16 and upcasts dynamically. Fix: run `model.to(torch.float16)` after loading, or use a GPU with bfloat16 support.

### Unsloth Fine-tuning Fixes

Three-part solution:

1. Keep all intermediate activations in bfloat16 (float32 possible but 2x VRAM/RAM via Unsloth's async gradient checkpointing).
2. All matrix multiplies in float16 with tensor cores, manual upcast/downcast (no PyTorch mixed precision autocast).
3. Upcast non-matrix-multiply ops (layernorms) to float32.

## Gemma 3 Fixes Analysis

When using float16 mixed precision, **gradients and activations become infinity** on T4 GPUs, RTX 20x series, and V100 GPUs (float16 tensor cores only). Newer GPUs (RTX 30x+, A100, H100) have bfloat16 tensor cores and are unaffected.

**Root cause:** float16 max is **65504**; bfloat16 max is **10^38**. Both are 16-bit, but float16 allocates more bits for decimal precision while bfloat16 cannot represent fractions well. float32 is too slow for matrix multiplications (4-10x slower than float16).

---

# Agent Instructions: Querying This Documentation

For additional information not on this page, query dynamically via HTTP GET:

```
GET https://unsloth.ai/docs/models/tutorials/gemma-3-how-to-run-and-fine-tune.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language. The response contains a direct answer with relevant excerpts and sources.

#gemma-3 #ollama #llama-cpp #fine-tuning #inference
