---
title: 'Qwen3-2507: Run Locally Guide'
url: https://unsloth.ai/docs/models/tutorials/qwen3-how-to-run-and-fine-tune/qwen3-2507.md
source: llms
fetched_at: 2026-04-27T18:13:59.271009209-03:00
rendered_js: false
word_count: 2235
summary: This guide details how to run and optimize Qwen3-2507 models (including 4B, 30B, and 235B variants) locally, providing specific best practices and tutorials for Instruct and Thinking modes using tools like Unsloth, Ollama, and llama.cpp.
tags:
    - qwen3-2507
    - run-locally
    - model-guide
    - instruct-thinking
    - unsloth
    - llama-cpp
category: guide
optimized: true
optimized_at: 2026-04-27T21:25:00Z
---

# Qwen3-2507: Run Locally Guide

Qwen released July 2025 updates for [Qwen3](047-models-tutorials-qwen3-how-to-run-and-fine-tune.md) 4B, 30B and 235B models, with "thinking" and "non-thinking" variants:

- **Non-thinking (Instruct)**: Qwen3-30B-A3B-Instruct-2507, Qwen3-235B-A22B-Instruct-2507 — 256K context, improved instruction following, multilingual, alignment
- **Thinking**: Qwen3-30B-A3B-Thinking-2507, Qwen3-235B-A22B-Thinking-2507 — SOTA in logic, math, science, coding, academic tasks

[Unsloth](https://github.com/unslothai/unsloth) supports fine-tuning and [[072-get-started-reinforcement-learning-rl-guide|RL]] of Qwen3-2507 — 2x faster, 70% less VRAM, 8x longer context.

#### Unsloth Dynamic 2.0 GGUFs

| Model | GGUFs |
|---|---|
| Qwen3-**4B-2507** | [Instruct](https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF) / [Thinking](https://huggingface.co/unsloth/Qwen3-4B-Thinking-2507-GGUF) |
| Qwen3-**30B-A3B**-2507 | [Instruct](#instruct-qwen3-30b-a3b-instruct-2507) / [Thinking](https://huggingface.co/unsloth/Qwen3-30B-A3B-Thinking-2507-GGUF) |
| Qwen3-**235B-A22B**-2507 | [Instruct](https://huggingface.co/unsloth/Qwen3-235B-A22B-Instruct-2507-GGUF) / [Thinking](https://huggingface.co/unsloth/Qwen3-235B-A22B-Thinking-2507-GGUF) |

## Best Practices

> [!important] Settings differ between Thinking and Instruct
> Thinking: `temp=0.6, top_p=0.95`. Instruct: `temp=0.7, top_p=0.8`.

| Setting | Instruct | Thinking |
|---|---|---|
| Temperature | 0.7 | 0.6 |
| Min_P | 0.00 (llama.cpp default 0.1) | 0.00 (llama.cpp default 0.1) |
| Top_P | 0.80 | 0.95 |
| TopK | 20 | 20 |
| presence_penalty | 0.0–2.0 (optional, reduces repetitions) | 0.0–2.0 (optional, reduces repetitions) |

**Output length**: 32,768 tokens adequate for most queries.

Chat template (Thinking has `thought` blocks; Instruct does not):

```
<|im_start|>user
Hey there!<|im_end|>
<|im_start|>assistant
What is 1+1?<|im_end|>
<|im_start|>user
2<|im_end|>
<|im_start|>assistant
```

## Run Qwen3-30B-A3B-2507 Tutorials

### Instruct: Qwen3-30B-A3B-Instruct-2507

Non-thinking model; no `thinking=False` needed, no thinking blocks generated.

#### Best Practices

- `temperature=0.7`, `top_p=0.8`, `top_k=20`, `min_p=0.0`
- `presence_penalty` 0.0–2.0 (try 1.0 for repetitions)
- Context: up to 262,144 natively; set 32,768 for less RAM

#### Ollama: Run Qwen3-30B-A3B-Instruct-2507

1. Install ollama (models up to 32B):

```bash
apt-get update
apt-get install pciutils -y
curl -fsSL https://ollama.com/install.sh | sh
```

2. Run (call `ollama serve` in another terminal if it fails):

```bash
ollama run hf.co/unsloth/Qwen3-30B-A3B-Instruct-2507-GGUF:UD-Q4_K_XL
```

#### Llama.cpp: Run Qwen3-30B-A3B-Instruct-2507

1. Build llama.cpp. Set `-DGGML_CUDA=OFF` for CPU-only or Apple Mac/Metal:

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

2. Pull from HuggingFace:

```bash
./llama.cpp/llama-cli \
    -hf unsloth/Qwen3-30B-A3B-Instruct-2507-GGUF:Q4_K_XL \
    --jinja -ngl 99 --ctx-size 32768 \
    --temp 0.7 --min-p 0.0 --top-p 0.80 --top-k 20 --presence-penalty 1.0
```

3. Download via Python (`pip install huggingface_hub hf_transfer`):

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Qwen3-30B-A3B-Instruct-2507-GGUF",
    local_dir = "unsloth/Qwen3-30B-A3B-Instruct-2507-GGUF",
    allow_patterns = ["*UD-Q4_K_XL*"],
)
```

### Thinking: Qwen3-30B-A3B-Thinking-2507

Thinking mode only; 256K context natively. Default chat template adds `thought` automatically; output shows closing tag only.

#### Best Practices

- `temperature=0.6`, `top_p=0.95`, `top_k=20`, `min_p=0.0`
- `presence_penalty` 0.0–2.0 (try 1.0)
- Context: up to 262,144 natively; set 32,768 for less RAM

#### Ollama: Run Qwen3-30B-A3B-Thinking-2507

1. Install ollama (models up to 32B; for 235B-A22B [see below](#run-qwen3-235b-a22b-instruct-2507-tutorials)):

```bash
apt-get update
apt-get install pciutils -y
curl -fsSL https://ollama.com/install.sh | sh
```

2. Run:

```bash
ollama run hf.co/unsloth/Qwen3-30B-A3B-Thinking-2507-GGUF:UD-Q4_K_XL
```

#### Llama.cpp: Run Qwen3-30B-A3B-Thinking-2507

1. Build llama.cpp:

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

2. Pull from HuggingFace:

```bash
./llama.cpp/llama-cli \
    -hf unsloth/Qwen3-30B-A3B-Thinking-2507-GGUF:Q4_K_XL \
    --jinja -ngl 99 --ctx-size 32768 \
    --temp 0.6 --min-p 0.0 --top-p 0.95 --top-k 20 --presence-penalty 1.0
```

3. Download via Python (`pip install huggingface_hub hf_transfer`):

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Qwen3-30B-A3B-Thinking-2507-GGUF",
    local_dir = "unsloth/Qwen3-30B-A3B-Thinking-2507-GGUF",
    allow_patterns = ["*UD-Q4_K_XL*"],
)
```

## Run Qwen3-235B-A22B-2507 Tutorials

### Thinking: Qwen3-235B-A22B-Thinking-2507

Thinking mode only; 256K context natively.

#### Best Practices

- `temperature=0.6`, `top_k=20`, `min_p=0.0`, `top_p=0.95`
- `presence_penalty` 0.0–2.0 (try 1.0)
- Output length: 32,768 tokens

#### Llama.cpp: Run Qwen3-235B-A22B-Thinking-2507

> [!tip] Full precision available
> Use `Q8_K_XL`, `Q8_0` or `BF16` checkpoints.

1. Build llama.cpp:

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

2. Pull directly:

```bash
./llama.cpp/llama-cli \
    -hf unsloth/Qwen3-235B-A22B-Thinking-2507-GGUF:Q2_K_XL \
    --ctx-size 16384 \
    --n-gpu-layers 99 \
    -ot ".ffn_.*_exps.=CPU" \
    --temp 0.6 \
    --min-p 0.0 \
    --top-p 0.95 \
    --top-k 20 \
    --presence-penalty 1.0
```

3. Download via Python (`pip install huggingface_hub hf_transfer`):

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0" # Can sometimes rate limit, so set to 0 to disable
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Qwen3-235B-A22B-Thinking-2507-GGUF",
    local_dir = "unsloth/Qwen3-235B-A22B-Thinking-2507-GGUF",
    allow_patterns = ["*UD-Q2_K_XL*"],
)
```

4. Run and try any prompt.

5. Tuning: `--threads -1` (CPU threads), `--ctx-size 262114` (context length), `--n-gpu-layers 99` (GPU offloading; adjust if OOM; remove for CPU-only).

> [!tip] MoE offloading
> `-ot ".ffn_.*_exps.=CPU"` offloads all MoE layers to CPU, fitting non-MoE on 1 GPU. Customize regex for more GPU capacity.

```bash
./llama.cpp/llama-cli \
    --model unsloth/Qwen3-235B-A22B-Thinking-2507-GGUF/UD-Q2_K_XL/Qwen3-235B-A22B-Thinking-2507-UD-Q2_K_XL-00001-of-00002.gguf \
    --ctx-size 16384 \
    --n-gpu-layers 99 \
    -ot ".ffn_.*_exps.=CPU" \
    --seed 3407 \
    --temp 0.6 \
    --min-p 0.0 \
    --top-p 0.95 \
    --top-k 20
    --presence-penalty 1.0
```

### Instruct: Qwen3-235B-A22B-Instruct-2507

Non-thinking model; no `thinking=False` needed.

#### Best Practices

1. **Sampling**: `temperature=0.7`, `top_p=0.8`, `top_k=20`, `min_p=0.0`; `presence_penalty` 0.0–2.0
2. **Output length**: 16,384 tokens for instruct models
3. **Standardize output** when benchmarking:
   - Math: include `Please reason step by step, and put your final answer within \boxed{}.`
   - Multiple-choice: `"answer": "C"` JSON structure

#### Llama.cpp: Run Qwen3-235B-A22B-Instruct-2507

> [!info] Full precision available
> Use `Q8_K_XL`, `Q8_0` or `BF16` checkpoints.

1. Build llama.cpp:

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

2. Pull directly:

```bash
./llama.cpp/llama-cli \
    -hf unsloth/Qwen3-235B-A22B-Instruct-2507-GGUF:Q2_K_XL \
    --ctx-size 16384 \
    --n-gpu-layers 99 \
    -ot ".ffn_.*_exps.=CPU" \
    --temp 0.7 \
    --min-p 0.0 \
    --top-p 0.8 \
    --top-k 20 \
    --repeat-penalty 1.0
```

3. Download via Python (`pip install huggingface_hub hf_transfer`):

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0" # Can sometimes rate limit, so set to 0 to disable
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Qwen3-235B-A22B-Instruct-2507-GGUF",
    local_dir = "unsloth/Qwen3-235B-A22B-Instruct-2507-GGUF",
    allow_patterns = ["*UD-Q2_K_XL*"],
)
```

4. Run and try any prompt. Tune: `--threads -1`, `--ctx-size 262114`, `--n-gpu-layers 99`.

> [!tip] MoE offloading
> `-ot ".ffn_.*_exps.=CPU"` offloads all MoE layers to CPU. Customize regex for more GPU capacity.

```bash
./llama.cpp/llama-cli \
    --model unsloth/Qwen3-235B-A22B-Instruct-2507-GGUF/UD-Q2_K_XL/Qwen3-235B-A22B-Instruct-2507-UD-Q2_K_XL-00001-of-00002.gguf \
    --ctx-size 16384 \
    --n-gpu-layers 99 \
    -ot ".ffn_.*_exps.=CPU" \
    --temp 0.7 \
    --min-p 0.0 \
    --top-p 0.8 \
    --top-k 20
```

### Improving Generation Speed

With more VRAM, offload more MoE layers:

- `-ot ".ffn_.*_exps.=CPU"` — all MoE to CPU (fits non-MoE on 1 GPU)
- `-ot ".ffn_(up|down)_exps.=CPU"` — up and down projection MoE (more GPU mem)
- `-ot ".ffn_(up)_exps.=CPU"` — up projection MoE only (most GPU mem)
- `-ot "\.(6|7|8|9|[0-9][0-9]|[0-9][0-9][0-9])\.ffn_(gate|up|down)_exps.=CPU"` — gate/up/down MoE from layer 6+ (customizable)

[Latest llama.cpp](https://github.com/ggml-org/llama.cpp/pull/14363) adds high throughput mode via `llama-parallel` ([docs](https://github.com/ggml-org/llama.cpp/tree/master/examples/parallel)). **KV cache quantization to 4bits** also reduces VRAM/RAM movement.

### How to Fit Long Context (256K to 1M)

**KV cache quantization** reduces K and V caches to lower bits, cutting memory and potentially speeding up generation.

K quantization options (default `f16`): `f32, f16, bf16, q8_0, q4_0, q4_1, iq4_nl, q5_0, q5_1`

Use `_1` variants (e.g. `--cache-type-k q4_1`) for increased accuracy (slightly slower).

For V cache quantization, compile llama.cpp with Flash Attention: `-DGGML_CUDA_FA_ALL_QUANTS=ON`, then `--flash-attn` + `--cache-type-v q4_1`.

## Fine-tuning Qwen3-2507 with Unsloth

Unsloth makes Qwen3 and Qwen3-2507 fine-tuning 2x faster, 70% less VRAM, 8x longer context. 30B requires ~40GB A100 for QLoRA (4-bit). Cannot fit in Colab free 16GB GPUs.

Use the [Qwen3 (14B) Reasoning + Conversational notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(14B\)-Reasoning-Conversational.ipynb) and replace the dataset.

Install latest Unsloth:

```bash
pip install --upgrade --force-reinstall --no-cache-dir unsloth unsloth_zoo
```

### Qwen3-2507 MOE Models Fine-tuning

MOE support: 30B-A3B and 235B-A22B. 30B-A3B works on 30GB VRAM. Router layer disabled by default for fine-tuning.

**Qwen3-2507-4B notebooks**: [Thinking](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(4B\)-Thinking.ipynb) / [Instruct](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(4B\)-Instruct.ipynb)

30B-A3B fits in 30GB VRAM but requires downloading full 16-bit model and converting to 4-bit on-the-fly for QLoRA (due to BnB MOE import issues).

> [!warning] Use `FastModel`, not `FastLanguageModel` for MOE fine-tuning.

```python
from unsloth import FastModel
import torch
model, tokenizer = FastModel.from_pretrained(
    model_name = "unsloth/Qwen3-30B-A3B-Instruct-2507",
    max_seq_length = 2048, # Choose any for long context!
    load_in_4bit = True,  # 4 bit quantization to reduce memory
    load_in_8bit = False, # [NEW!] A bit more accurate, uses 2x memory
    full_finetuning = False, # [NEW!] We have full finetuning now!
    # token = "hf_...", # use one if using gated models
)
```

#qwen3-2507 #local-inference #fine-tuning #llama-cpp #ollama #moe
