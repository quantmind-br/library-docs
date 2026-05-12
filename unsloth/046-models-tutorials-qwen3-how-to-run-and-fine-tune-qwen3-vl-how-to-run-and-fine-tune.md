---
title: 'Qwen3-VL: How to Run Guide'
url: https://unsloth.ai/docs/models/tutorials/qwen3-how-to-run-and-fine-tune/qwen3-vl-how-to-run-and-fine-tune.md
source: llms
fetched_at: 2026-04-27T18:13:58.413881168-03:00
rendered_js: false
word_count: 1229
summary: This guide explains how to run and fine-tune Qwen3-VL models, detailing recommended generation settings for both Instruct and Thinking variants across various platforms like llama.cpp and vLLM.
tags:
    - qwen3-vl
    - llm-guide
    - vision-model
    - running-guide
    - fine-tuning
    - hyperparameters
category: guide
optimized: true
optimized_at: 2026-04-27T21:35:00Z
---

# Qwen3-VL: How to Run Guide

Qwen3-VL vision models with **instruct** and **thinking** variants. Dense: 2B, 4B, 8B, 32B. MoE: 30B-A3B, 235B-A22B. The 235B thinking LLM rivals GPT-5 (high) and Gemini 2.5 Pro on vision/coding benchmarks.

Capabilities: vision, video, OCR, 256K context (extensible to 1M).

[Unsloth](https://github.com/unslothai/unsloth) supports Qwen3-VL fine-tuning and [[071-get-started-reinforcement-learning-rl-guide-vision-reinforcement-learning-vlm-rl|RL]]. Free [[046-models-tutorials-qwen3-how-to-run-and-fine-tune-qwen3-vl-how-to-run-and-fine-tune|Qwen3-VL (8B) training notebooks on Colab]].

## Running Qwen3-VL

### Recommended Settings

| Parameter | Instruct | Thinking |
|-----------|----------|----------|
| Temperature | 0.7 | 1.0 |
| Top_P | 0.8 | 0.95 |
| presence_penalty | 1.5 | 0.0 |
| Top_K | 20 | 20 |
| Output Length | 32768 (up to 256K) | 40960 (up to 256K) |

Source: [Qwen3-VL GitHub](https://github.com/QwenLM/Qwen3-VL/tree/main?tab=readme-ov-file#generation-hyperparameters).

**Instruct env vars:**

```bash
export greedy='false'
export seed=3407
export top_p=0.8
export top_k=20
export temperature=0.7
export repetition_penalty=1.0
export presence_penalty=1.5
export out_seq_length=32768
```

**Thinking env vars:**

```bash
export greedy='false'
export seed=1234
export top_p=0.95
export top_k=20
export temperature=1.0
export repetition_penalty=1.0
export presence_penalty=0.0
export out_seq_length=40960
```

### Chat Template Bug Fix

llama.cpp broke after the 2nd turn on Thinking models due to a chat template error:

```
terminate called after throwing an instance of 'std::runtime_error'
  what():  Value is not callable: null at row 63, column 78:
            {%- if ' SI ' in content %}
                {%- set reasoning_content = ((content.split(' SI ')|first).rstrip('\n').split(' 3 ')|last).lstrip('\n') %}
                                                                             ^
```

Unsloth fixed the Thinking chat template and re-uploaded all Thinking quants. Other quants will still fail after the 2nd conversation turn.

### Qwen3-VL Unsloth Uploads

GGUF support in llama.cpp since 30 Oct 2025.

**Dynamic GGUFs (to run):** 2B-Instruct, 2B-Thinking, 4B-Instruct, 4B-Thinking, 8B-Instruct, 8B-Thinking, 30B-Instruct, 30B-Thinking, 32B-Instruct, 32B-Thinking, 235B-A22B-Instruct, 235B-A22B-Thinking
- [HuggingFace org](https://huggingface.co/unsloth) — pattern: `unsloth/Qwen3-VL-{SIZE}-{VARIANT}-GGUF`

**4-bit BnB Unsloth Dynamic (to finetune):** 2B-Instruct, 2B-Thinking, 4B-Instruct, 4B-Thinking, 8B-Instruct, 8B-Thinking, 32B-Instruct, 32B-Thinking
- Pattern: `unsloth/Qwen3-VL-{SIZE}-{VARIANT}-unsloth-bnb-4bit`

**16-bit full-precision:** 2B-Instruct, 4B-Instruct, 4B-Thinking, 8B-Instruct, 8B-Thinking, 30B-Instruct, 30B-Thinking, 32B-Instruct, 32B-Thinking, 235B-A22B-Thinking, 235B-A22B-Instruct
- Pattern: `unsloth/Qwen3-VL-{SIZE}-{VARIANT}`

### Llama.cpp: Run Qwen3-VL Tutorial

1. Build llama.cpp. Set `-DGGML_CUDA=OFF` for CPU-only or Apple Metal (on by default):

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first
cp llama.cpp/build/bin/llama-* llama.cpp
```

2. Download test images:

```bash
wget https://raw.githubusercontent.com/unslothai/unsloth/refs/heads/main/images/unsloth%20made%20with%20love.png -O unsloth.png
wget https://files.worldwildlife.org/wwfcmsprod/images/Sloth_Sitting_iStock_3_12_2014/story_full_width/8l7pbjmj29_iStock_000011145477Large_mini__1_.jpg -O picture.png
```

3. Run 8B Instruct via llama.cpp auto-download:

```bash
./llama.cpp/llama-mtmd-cli \
    -hf unsloth/Qwen3-VL-8B-Instruct-GGUF:UD-Q4_K_XL \
    --n-gpu-layers 99 \
    --jinja \
    --top-p 0.8 \
    --top-k 20 \
    --temp 0.7 \
    --min-p 0.0 \
    --flash-attn on \
    --presence-penalty 1.5 \
    --ctx-size 8192
```

4. Inside the CLI: load images with `/image PATH` (e.g., `/image unsloth.png`), then ask questions.

5. For large models, download via HuggingFace (faster than llama.cpp auto-downloader):

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id   = "unsloth/Qwen3-VL-8B-Instruct-GGUF", # Or "unsloth/Qwen3-VL-8B-Thinking-GGUF"
    local_dir = "unsloth/Qwen3-VL-8B-Instruct-GGUF", # Or "unsloth/Qwen3-VL-8B-Thinking-GGUF"
    allow_patterns = ["*UD-Q4_K_XL*", "*mmproj-F16*"],
)
```

6. Run downloaded model — **Instruct:**

```bash
./llama.cpp/llama-mtmd-cli \
    --model unsloth/Qwen3-VL-8B-Instruct-GGUF/Qwen3-VL-8B-Instruct-UD-Q4_K_XL.gguf \
    --mmproj unsloth/Qwen3-VL-8B-Instruct-GGUF/mmproj-F16.gguf \
    --n-gpu-layers 99 \
    --jinja \
    --top-p 0.8 \
    --top-k 20 \
    --temp 0.7 \
    --min-p 0.0 \
    --flash-attn on \
    --presence-penalty 1.5 \
    --ctx-size 8192
```

7. **Thinking:**

```bash
./llama.cpp/llama-mtmd-cli \
    --model unsloth/Qwen3-VL-8B-Thinking-GGUF/Qwen3-VL-8B-Thinking-UD-Q4_K_XL.gguf \
    --mmproj unsloth/Qwen3-VL-8B-Thinking-GGUF/mmproj-F16.gguf \
    --n-gpu-layers 99 \
    --jinja \
    --top-p 0.95 \
    --top-k 20 \
    --temp 1.0 \
    --min-p 0.0 \
    --flash-attn on \
    --presence-penalty 0.0 \
    --ctx-size 8192
```

### Running Qwen3-VL-235B-A22B and Qwen3-VL-30B-A3B

1. Follow llama.cpp build steps above.
2. Download the model:

   ```python
   # !pip install huggingface_hub hf_transfer
   import os
   os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
   from huggingface_hub import snapshot_download
   snapshot_download(
       repo_id = "unsloth/Qwen3-VL-235B-A22B-Instruct-GGUF",
       local_dir = "unsloth/Qwen3-VL-235B-A22B-Instruct-GGUF",
       allow_patterns = ["*UD-Q2_K_XL*", "*mmproj-F16*"],
   )
   ```
3. Run — **Instruct:**

```bash
./llama.cpp/llama-mtmd-cli \
    --model unsloth/Qwen3-VL-235B-A22B-Instruct-GGUF/UD-Q2_K_XL/Qwen3-VL-235B-A22B-Instruct-UD-Q2_K_XL-00001-of-00002.gguf \
    --mmproj unsloth/Qwen3-VL-235B-A22B-Instruct-GGUF/mmproj-F16.gguf
    --jinja \
    --top-p 0.8 \
    --top-k 20 \
    --temp 0.7 \
    --min-p 0.0 \
    --flash-attn on \
    --presence-penalty 1.5 \
    --ctx-size 8192 \
```

4. Run — **Thinking:**

```bash
./llama.cpp/llama-mtmd-cli \
    --model unsloth/Qwen3-VL-235B-A22B-Thinking-GGUF/UD-Q2_K_XL/Qwen3-VL-235B-A22B-Thinking-UD-Q2_K_XL-00001-of-00002.gguf \
    --mmproj unsloth/Qwen3-VL-235B-A22B-Thinking-GGUF/mmproj-F16.gguf \
    --n-gpu-layers 99 \
    --jinja \
    --top-p 0.95 \
    --top-k 20 \
    --temp 1.0 \
    --min-p 0.0 \
    --flash-attn on \
    --presence-penalty 0.0 \
    --ctx-size 8192 \
    -ot ".ffn_.*_exps.=CPU"
```

5. Tune: `--ctx-size 16384` for context length, `--n-gpu-layers 99` for GPU offloading (reduce if OOM). Remove for CPU-only.

> [!tip] `--fit on` (added 15 Dec 2025) maximizes GPU+CPU usage. Use `-ot ".ffn_.*_exps.=CPU"` to offload all MoE layers to CPU, fitting non-MoE layers on 1 GPU. Customize the regex to fit more layers if GPU capacity allows.

### Docker: Run Qwen3-VL

```bash
docker model pull hf.co/unsloth/Qwen3-VL-8B-Instruct-GGUF:UD-Q4_K_XL
```

Or Docker's own Qwen3-VL model:

```bash
docker model run ai/qwen3-vl
```

## Fine-tuning Qwen3-VL

Unsloth fine-tunes Qwen3-VL (including 32B/235B) for vision, video, and object detection. 1.7x faster, 60% less VRAM, 8x longer context, no accuracy loss.

Colab notebooks (free, 8B):

- [Normal SFT fine-tuning](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_VL_\(8B\)-Vision.ipynb)
- [GRPO/GSPO RL](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_VL_\(8B\)-Vision-GRPO.ipynb) — trains VLM to solve math from image input via RL

> [!tip] Saving Qwen3-VL to GGUF now works (llama.cpp supported it). Swap 8B for 2B, 32B etc. as needed.

Integrates [[068-get-started-reinforcement-learning-rl-guide-memory-efficient-rl|Unsloth Standby]] for memory-efficient RL with minimal speed degradation. See [[071-get-started-reinforcement-learning-rl-guide-vision-reinforcement-learning-vlm-rl|VLM GRPO guide]] for full RL training details.

### Multi-image Training

Replace `ds.map(convert_to_conversation)` with a list comprehension to avoid dataset standardization/arrow processing:

```python
# Instead of:
ds_converted = ds.map(convert_to_conversation)

# Use:
ds_converted = [convert_to_converation(sample) for sample in dataset]
```

Using `.map()` triggers strict arrow processing rules that complicate multi-image definitions.

#qwen3-vl #vision-model #llm #fine-tuning #unsloth
