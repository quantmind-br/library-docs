---
title: 'Gemma 3n: How to Run & Fine-tune'
url: https://unsloth.ai/docs/models/tutorials/gemma-3-how-to-run-and-fine-tune/gemma-3n-how-to-run-and-fine-tune.md
source: llms
fetched_at: 2026-04-27T18:14:05.87773874-03:00
rendered_js: false
tags:
    - gemma-3n
    - multimodal
    - ollama
    - llama-cpp
    - fine-tuning
    - inference
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Gemma 3n: How to Run & Fine-tune

Google's Gemma 3n multimodal model handles image, audio, video, and text inputs. Available in 2B and 4B sizes, supports 140 languages. Run and fine-tune **Gemma-3n-E4B** and **E2B** locally with [Unsloth](https://github.com/unslothai/unsloth).

> [!tip] Fine-tune Gemma 3n with our [free Colab notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3N_\(4B\)-Conversational.ipynb)

Key specs: **32K context length**, 30s audio input, OCR, ASR, speech translation via prompts.

## Unsloth Gemma 3n Uploads (with optimal configs)

| Dynamic 2.0 GGUF (text only) | Dynamic 4-bit Instruct (to fine-tune) | 16-bit Instruct |
| --- | --- | --- |
| [2B](https://huggingface.co/unsloth/gemma-3n-E2B-it-GGUF) | [2B](https://huggingface.co/unsloth/gemma-3n-E2B-it-unsloth-bnb-4bit) | [2B](https://huggingface.co/unsloth/gemma-3n-E2B-it) |
| [4B](https://huggingface.co/unsloth/gemma-3n-E4B-it-GGUF) | [4B](https://huggingface.co/unsloth/gemma-3n-E4B-it-unsloth-bnb-4bit) | [4B](https://huggingface.co/unsloth/gemma-3n-E4B-it) |

All formats including base models: [HuggingFace collection](https://huggingface.co/collections/unsloth/gemma-3n-685d3874830e49e1c93f9339).

## Running Gemma 3n

Currently only **text format** for inference.

> [!info] GGUF bug fixes for Ollama have been applied. Redownload if using Ollama.

### Official Recommended Settings

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

### Tutorial: How to Run Gemma 3n in Ollama

> [!success] Redownload Gemma 3n quants or remove old ones via Ollama:
> ```bash
> ollama rm hf.co/unsloth/gemma-3n-E4B-it-GGUF:UD-Q4_K_XL
> ollama run hf.co/unsloth/gemma-3n-E4B-it-GGUF:UD-Q4_K_XL
> ```

1. Install Ollama:

```bash
apt-get update
apt-get install pciutils -y
curl -fsSL https://ollama.com/install.sh | sh
```

2. Run the model. Use `ollama serve` in another terminal if it fails. Fixes and suggested params are in `params` in the HF upload:

```bash
ollama run hf.co/unsloth/gemma-3n-E4B-it-GGUF:UD-Q4_K_XL
```

### Tutorial: How to Run Gemma 3n in llama.cpp

> [!info] Thanks to [Xuan-Son Nguyen](https://x.com/ngxson) (Hugging Face) and [Georgi Gerganov](https://x.com/ggerganov) (llama.cpp) for making Gemma 3N work in llama.cpp.

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
./llama.cpp/llama-cli -hf unsloth/gemma-3n-E4B-it-GGUF:UD-Q4_K_XL -ngl 99 --jinja
```

3. **OR** download the model (after `pip install huggingface_hub hf_transfer`):

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/gemma-3n-E4B-it-GGUF",
    local_dir = "unsloth/gemma-3n-E4B-it-GGUF",
    allow_patterns = ["*UD-Q4_K_XL*", "mmproj-BF16.gguf"], # For Q4_K_XL
)
```

4. Run conversation mode. Adjust `--threads 32` (CPU threads), `--ctx-size 32768` (Gemma 3n: 32K context), `--n-gpu-layers 99` (GPU offloading; reduce if OOM; remove for CPU-only):

```bash
./llama.cpp/llama-cli \
    --model unsloth/gemma-3n-E4B-it-GGUF/gemma-3n-E4B-it-UD-Q4_K_XL.gguf \
    --mmproj unsloth/gemma-3n-E4B-it-GGUF/mmproj-BF16.gguf \
    --ctx-size 32768 \
    --n-gpu-layers 99 \
    --seed 3407 \
    --prio 2 \
    --temp 1.0 \
    --repeat-penalty 1.0 \
    --min-p 0.00 \
    --top-k 64 \
    --top-p 0.95
```

5. Non-conversation mode (Flappy Bird test):

```bash
./llama.cpp/llama-cli \
    --model unsloth/gemma-3n-E4B-it-GGUF/gemma-3n-E4B-it-UD-Q4_K_XL.gguf \
    --mmproj unsloth/gemma-3n-E4B-it-GGUF/mmproj-BF16.gguf \
    --ctx-size 32768 \
    --n-gpu-layers 99 \
    --seed 3407 \
    --prio 2 \
    --temp 1.0 \
    --repeat-penalty 1.0 \
    --min-p 0.00 \
    --top-k 64 \
    --top-p 0.95 \
    -no-cnv \
    --prompt "<start_of_turn>user\nCreate a Flappy Bird game in Python. You must include these things:\n1. You must use pygame.\n2. The background color should be randomly chosen and is a light shade. Start with a light blue color.\n3. Pressing SPACE multiple times will accelerate the bird.\n4. The bird's shape should be randomly chosen as a square, circle or triangle. The color should be randomly chosen as a dark color.\n5. Place on the bottom some land colored as dark brown or yellow chosen randomly.\n6. Make a score shown on the top right side. Increment if you pass pipes and don't hit them.\n7. Make randomly spaced pipes with enough space. Color them randomly as dark green or light brown or a dark gray shade.\n8. When you lose, show the best score. Make the text inside the screen. Pressing q or Esc will quit the game. Restarting is pressing SPACE again.\nThe final game should be inside a markdown section in Python. Check your code for errors and fix them before the final markdown section.<end_of_turn>\n<start_of_turn>model\n"
```

> [!danger] Remove `<bos>` -- Gemma 3N auto-adds it.

## Fine-tuning Gemma 3n with Unsloth

Like [[031-models-tutorials-gemma-3-how-to-run-and-fine-tune|Gemma 3]], Gemma 3n has issues on **float16 GPUs (Tesla T4s in Colab)**: NaNs and infinities without patching. [More info below](#infinities-and-nan-gradients-and-activations).

- [Free Colab notebook (text)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3N_\(4B\)-Conversational.ipynb)
- [Audio notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3N_\(4B\)-Audio.ipynb)
- [Vision notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3N_\(4B\)-Vision.ipynb)

Gemma 3n's vision encoder reuses hidden states, which limits [Unsloth's gradient checkpointing](https://unsloth.ai/blog/long-context) on the vision encoder. Unsloth's automatic compiler still optimizes the model.

**Unsloth is the only framework working on float16 machines for Gemma 3n inference and training** (Colab free T4 GPUs work). Training: 1.5x faster, 50% less VRAM, 4x longer context.

Default Colab notebooks fine-tune text layers only. Fine-tuning vision/audio layers requires more VRAM (>15GB). Selective fine-tuning:

```python
model = FastVisionModel.get_peft_model(
    model,
    finetune_vision_layers     = False, # False if not finetuning vision layers
    finetune_language_layers   = True,  # False if not finetuning language layers
    finetune_attention_modules = True,  # False if not finetuning attention layers
    finetune_mlp_modules       = True,  # False if not finetuning MLP layers
)
```

> [!tip] Kaggle competition: best model fine-tuned with Gemma 3n + Unsloth wins $10K. [Details](https://www.kaggle.com/competitions/google-gemma-3n-hackathon).

## Fixes for Gemma 3n

### GGUF Issues & Fixes

Two GGUF-specific issues fixed with help from [Michael](https://github.com/mxyng) (Ollama) and [Xuan](https://x.com/ngxson) (Hugging Face):

1. **`add_shared_kv_layers`** was encoded in `float32` -- complicated for Ollama decoding. Fixed by changing to `uint32`. [PR #14450](https://github.com/ggml-org/llama.cpp/pull/14450).
2. **`per_layer_token_embd`** must be Q8_0 precision -- lower precisions error in Ollama. All quants now use Q8_0 for embeddings (uses more space). [Update](https://huggingface.co/unsloth/gemma-3n-E4B-it-GGUF/discussions/4): Q4_0, Q4_1, Q5_0, Q5_1 also work in Ollama per [Matt](https://huggingface.co/WBB2500), so smaller quants are viable again.

### Infinities and NaN Gradients and Activations

Unlike [[031-models-tutorials-gemma-3-how-to-run-and-fine-tune|Gemma 3]] (where activations exceed float16's max of 65504), **Gemma 3N does not have the activation issue** but still produces infinities on FP16 GPUs (Tesla T4s in Colab).

Analysis of absolute max weight entries shows **Conv2D convolutional weights have much larger magnitudes**. During Conv2D ops, large weights multiply and sum, exceeding float16's max of 65504 (bfloat16's max of 10^38 is fine).

Top Conv2D weights by max value:

| Name | Max |
| --- | --- |
| msfa.ffn.pw\_proj.conv.weight | 98.000000 |
| blocks.2.21.attn.key.down\_conv.weight | 37.000000 |
| blocks.2.32.pw\_exp.conv.weight | 34.750000 |
| blocks.2.30.pw\_exp.conv.weight | 33.750000 |
| blocks.2.34.pw\_exp.conv.weight | 33.750000 |

#### Solution

Naive approach: upcast all Conv2D weights to float32 (increases VRAM). Unsloth instead uses `autocast` to upcast weights and inputs to float32 during accumulation in the matrix multiplication itself, without permanently upcasting weights.

> [!success] Unsloth is the only framework enabling Gemma 3n inference and training on float16 GPUs.

#### Gradient Checkpointing Issues

Gemma 3N's vision encoder reuses hidden states, limiting [Unsloth's gradient checkpointing](https://unsloth.ai/blog/long-context) on the vision encoder. Unsloth's automatic compiler still optimizes the model.

#### Large Losses During Fine-tuning

Starting losses are high (6-7) but decrease quickly. Two hypotheses:

1. Implementation issue (unlikely -- inference works fine).
2. **Multimodal models exhibit this behavior** -- Llama 3.2 Vision starts at 3-4, Pixtral at ~8, Qwen 2.5 VL at ~4. Gemma 3N includes audio which may amplify starting loss. Qwen 2.5 VL 72B Instruct quantized shows perplexity ~30 but performs fine.

## Technical Analysis

### MatFormer Architecture

Gemma 3n uses [Matryoshka Transformer (MatFormer)](https://arxiv.org/abs/2310.07707): each transformer layer nests FFNs of progressively smaller sizes. Training forwards inputs through randomly chosen sub-blocks (sizes `S`, `S/2`, `S/4`, `S/8` etc.), giving every sub-block equal learning chance.

At inference you can:
- Pick a fixed smaller sub-model size (e.g., `S/4` throughout)
- **Mix and match** -- different sub-model sizes per layer, even dynamically per input

Training one model creates exponentially many smaller models with no wasted learning.

The 2B model (E2B) is a sub-network inside the 4B (5.44B) model, achieved by Per Layer Embedding caching and skipping audio/vision components (text-only). Per Layer Embedding can be cached to reduce inference memory.

---

# Agent Instructions: Querying This Documentation

For additional information not on this page, query dynamically via HTTP GET:

```
GET https://unsloth.ai/docs/models/tutorials/gemma-3-how-to-run-and-fine-tune/gemma-3n-how-to-run-and-fine-tune.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language. The response contains a direct answer with relevant excerpts and sources.

#gemma-3n #ollama #llama-cpp #fine-tuning #multimodal
