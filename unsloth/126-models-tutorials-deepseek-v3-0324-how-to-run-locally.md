---
title: 'DeepSeek-V3-0324: How to Run Locally'
url: https://unsloth.ai/docs/models/tutorials/deepseek-v3-0324-how-to-run-locally.md
source: llms
fetched_at: 2026-04-27T18:14:34.401472127-03:00
rendered_js: false
word_count: 1129
summary: This document serves as a tutorial and reference guide detailing how users can run the DeepSeek-V3-0324 large language model locally, providing recommended quantization settings, inference parameters, and step-by-step instructions using llama.cpp.
tags:
    - deepseek-v3
    - local-inference
    - llama-cpp
    - model-quantization
    - llm-guide
    - unsloth
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# DeepSeek-V3-0324: How to Run Locally

> [!info] See [DeepSeek-R1-0528](025-models-tutorials-deepseek-r1-0528-how-to-run-locally.md) (May 28 2025 update) for faster/more efficient DeepSeek inference.

DeepSeek-V3-0324 is the March 2025 update to V3. Benchmarks vs previous V3: MMLU-Pro +5.3% (81.2%), GPQA +9.3%, AIME +19.8%, LiveCodeBench +10.0%.

The model is **671B parameters** (MoE). Below are quantized GGUF options:

| MoE Bits | Type    | Disk Size | Accuracy  | Link | Details        |
| -------- | ------- | --------- | --------- | ---- | -------------- |
| 1.78bit  | IQ1_S   | **173GB** | Ok        | [Link](https://huggingface.co/unsloth/DeepSeek-V3-0324-GGUF/tree/main/UD-IQ1_S) | 2.06/1.56bit  |
| 1.93bit  | IQ1_M   | **183GB** | Fair      | [Link](https://huggingface.co/unsloth/DeepSeek-V3-0324-GGUF/tree/main/UD-IQ1_M) | 2.5/2.06/1.56 |
| 2.42bit  | IQ2_XXS | **203GB** | **Suggested** | [Link](https://huggingface.co/unsloth/DeepSeek-V3-0324-GGUF/tree/main/UD-IQ2_XXS) | 2.5/2.06bit   |
| 2.71bit  | Q2_K_XL | **231GB** | **Suggested** | [Link](https://huggingface.co/unsloth/DeepSeek-V3-0324-GGUF/tree/main/UD-Q2_K_XL) | 3.5/2.5bit    |
| 3.5bit   | Q3_K_XL | **320GB** | Great     | [Link](https://huggingface.co/unsloth/DeepSeek-V3-0324-GGUF/tree/main/UD-Q3_K_XL) | 4.5/3.5bit    |
| 4.5bit   | Q4_K_XL | **406GB** | Best      | [Link](https://huggingface.co/unsloth/DeepSeek-V3-0324-GGUF/tree/main/UD-Q4_K_XL) | 5.5/4.5bit    |

> [!tip] Original float8 upload is 715GB. Q4_K_M halves to ~404GB; dynamic 1.78bit fits ~151GB. **Recommended: 2.7bit (`UD-Q2_K_XL`) for size/accuracy balance. 2.4bit also works well.**

## Official Recommended Settings

Per [DeepSeek](https://huggingface.co/deepseek-ai/DeepSeek-V3-0324):

- **Temperature 0.3** (0.0 for coding — [DeepSeek docs](https://api-docs.deepseek.com/quick_start/parameter_settings))
- Min_P: 0.00 (optional; 0.01 works well; llama.cpp default is 0.1)
- Chat template: `<|User|>prompt<|Assistant|>`
- BOS token `<|begin of sentence|>` auto-added during tokenization — do NOT add manually
- Optional system prompt (Chinese): `该助手为DeepSeek Chat，由深度求索公司创造。\n今天是3月24日，星期一。` → `The assistant is DeepSeek Chat, created by DeepSeek.\nToday is Monday, March 24th.`
- **KV cache quantization: use 8bit, NOT 4bit** — 4bit is noticeably worse

## Tutorial: Run DeepSeek-V3 in llama.cpp

### 1. Build llama.cpp

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-quantize llama-cli llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

> [!warning] `-DGGML_CUDA=ON` takes ~5 min to compile; CPU-only ~1 min. Precompiled binaries available.
> Set `-DGGML_CUDA=OFF` for CPU-only or Apple Mac/Metal (Metal is on by default).

### 2. Download Model

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/DeepSeek-V3-0324-GGUF-UD",
    local_dir = "unsloth/DeepSeek-V3-0324-GGUF-UD",
    allow_patterns = ["*UD-Q2_K_XL*"], # Dynamic 2.7bit (230GB) Use "*UD-IQ_S*" for Dynamic 1.78bit (151GB)
)
```

More versions: <https://huggingface.co/unsloth/DeepSeek-V3-0324-GGUF>

### 3. Run Flappy Bird Test

See [[116-models-tutorials-deepseek-r1-how-to-run-locally-deepseek-r1-dynamic-1.58-bit.md|DeepSeek R1 1.58-bit Dynamic Quant]] for test methodology.

```bash
./llama.cpp/llama-cli \
    --model unsloth/DeepSeek-V3-0324-GGUF-UD/blob/main/UD-Q2_K_XL/DeepSeek-V3-0324-UD-Q2_K_XL-00001-of-00006.gguf \
    --cache-type-k q8_0 \
    --threads 20 \
    --n-gpu-layers 2 \
    -no-cnv \
    --prio 3 \
    --temp 0.3 \
    --min-p 0.01 \
    --ctx-size 4096 \
    --seed 3407 \
    --prompt "<|User|>Create a Flappy Bird game in Python. You must include these things:\n1. You must use pygame.\n2. The background color should be randomly chosen and is a light shade. Start with a light blue color.\n3. Pressing SPACE multiple times will accelerate the bird.\n4. The bird's shape should be randomly chosen as a square, circle or triangle. The color should be randomly chosen as a dark color.\n5. Place on the bottom some land colored as dark brown or yellow chosen randomly.\n6. Make a score shown on the top right side. Increment if you pass pipes and don't hit them.\n7. Make randomly spaced pipes with enough space. Color them randomly as dark green or light brown or a dark gray shade.\n8. When you lose, show the best score. Make the text inside the screen. Pressing q or Esc will quit the game. Restarting is pressing SPACE again.\nThe final game should be inside a markdown section in Python. Check your code for errors and fix them before the final markdown section.<|Assistant|>"
```

- `--threads 32` — adjust for CPU thread count
- `--ctx-size 16384` — context length
- `--n-gpu-layers 2` — GPU offload layers (reduce if OOM; remove for CPU-only)
- `--cache-type-k q8_0` — use 8bit KV cache (not 4bit)

### 4. GPU Offload Reference

DeepSeek-V3 has 61 layers. Offload counts by GPU (round down; reduce by 1 if OOM):

| Quant   | File Size | 24GB GPU | 80GB GPU | 2x80GB GPU |
| ------- | --------- | -------- | -------- | ---------- |
| 1.73bit | 173GB     | 5        | 25       | 56         |
| 2.22bit | 183GB     | 4        | 22       | 49         |
| 2.51bit | 212GB     | 2        | 19       | 32         |

### Running on Mac / Apple Devices

Reduce `--n-gpu-layers` if OOM. 128GB unified memory machine can offload ~59 layers.

```bash
./llama.cpp/llama-cli \
    --model DeepSeek-R1-GGUF/DeepSeek-V3-0324-UD-IQ1_S/DeepSeek-V3-0324-UD-IQ1_S-00001-of-00003.gguf \
    --cache-type-k q4_0 \
    --threads 16 \
    --prio 2 \
    --temp 0.6 \
    --ctx-size 8192 \
    --seed 3407 \
    --n-gpu-layers 59 \
    -no-cnv \
    --prompt "<|User|>Create a Flappy Bird game in Python.<|Assistant|>"
```

## Heptagon Test

Physics engine test from [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1j7r47l/i_just_made_an_animation_of_a_ball_bouncing/) — 20 balls bouncing in a spinning heptagon.

```bash
./llama.cpp/llama-cli \
    --model unsloth/DeepSeek-V3-0324-GGUF-UD/blob/main/UD-Q2_K_XL/DeepSeek-V3-0324-UD-Q2_K_XL-00001-of-00006.gguf \
    --cache-type-k q8_0 \
    --threads 20 \
    --n-gpu-layers 2 \
    -no-cnv \
    --prio 3 \
    --temp 0.3 \
    --min_p 0.01 \
    --ctx-size 4096 \
    --seed 3407 \
    --prompt "<|User|>Write a Python program that shows 20 balls bouncing inside a spinning heptagon:\n- All balls have the same radius.\n- All balls have a number on it from 1 to 20.\n- All balls drop from the heptagon center when starting.\n- Colors are: #f8b862, #f6ad49, #f39800, #f08300, #ec6d51, #ee7948, #ed6d3d, #ec6800, #ec6800, #ee7800, #eb6238, #ea5506, #ea5506, #eb6101, #e49e61, #e45e32, #e17b34, #dd7a56, #db8449, #d66a35\n- The balls should be affected by gravity and friction, and they must bounce off the rotating walls realistically. There should also be collisions between balls.\n- The material of all the balls determines that their impact bounce height will not exceed the radius of the heptagon, but higher than ball radius.\n- All balls rotate with friction, the numbers on the ball can be used to indicate the spin of the ball.\n- The heptagon is spinning around its center, and the speed of spinning is 360 degrees per 5 seconds.\n- The heptagon size should be large enough to contain all the balls.\n- Do not use the pygame library; implement collision detection algorithms and collision response etc. by yourself. The following Python libraries are allowed: tkinter, math, numpy, dataclasses, typing, sys.\n- All codes should be put in a single Python file.<|Assistant|>"
```

| Version               | Result |
| --------------------- | ------ |
| Non-dynamic 2bit      | Fails (seizure warning) |
| Dynamic 2bit (2.7bit) | Solves correctly |
| Original float8       | Reference baseline |

The dynamic 2.7bit quant (230GB) solves the heptagon puzzle while non-dynamic 2bit fails.

## Extra Findings and Tips

1. **KV cache**: Use `q8_0` cache quantization. 4bit degrades generation quality per empirical tests.
2. **`down_proj` sensitivity**: Extremely sensitive to quantization. Minimum 3bits for `down_proj` matrices (dynamic quants previously used 2bits).
3. **Flash Attention**: llama.cpp FA backend gives faster decoding. Compile with `-DGGML_CUDA_FA_ALL_QUANTS=ON`. Set CUDA architecture via `-DCMAKE_CUDA_ARCHITECTURES="80"` ([GPU list](https://developer.nvidia.com/cuda-gpus)) to reduce compile time.
4. **`min_p=0.01`**: Sufficient; llama.cpp defaults to 0.1 which is unnecessary given 0.3 temperature. DeepSeek recommends 0.0 for coding tasks.

#deepseek-v3 #local-inference #llama-cpp #model-quantization
