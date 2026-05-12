---
title: 'Kimi K2 Thinking: Run Locally Guide'
url: https://unsloth.ai/docs/models/tutorials/kimi-k2-thinking-how-to-run-locally.md
source: llms
fetched_at: 2026-04-27T18:14:16.893487397-03:00
rendered_js: false
word_count: 2172
summary: This document serves as a comprehensive guide for running and optimizing Kimi-K2-Thinking locally, detailing hardware requirements, recommended inference settings, and providing step-by-step instructions on how to run the model using llama.cpp or Python scripts.
tags:
    - kimi-k2-thinking
    - gguf
    - local-inference
    - llm-guide
    - llama-cpp
    - performance-tuning
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Kimi K2 Thinking: Run Locally Guide

Kimi-K2 and **Kimi-K2-Thinking** achieve SOTA performance in knowledge, reasoning, coding, and agentic tasks. Full 1T parameter model = 1.09TB disk. Unsloth Dynamic 1.8-bit = 230GB (-80%): [Kimi-K2-GGUF](https://huggingface.co/unsloth/Kimi-K2-Instruct-GGUF). Thinking GGUFs: [Kimi-K2-Thinking-GGUF](https://huggingface.co/unsloth/Kimi-K2-Thinking-GGUF).

All uploads use Unsloth [[115-basics-unsloth-dynamic-2.0-ggufs|Dynamic 2.0]] for SOTA [[075-basics-unsloth-dynamic-2.0-ggufs-unsloth-dynamic-ggufs-on-aider-polyglot|Aider Polyglot]] and 5-shot MMLU performance.

## Recommended Requirements

**1-bit quant requires 247GB disk.** Only requirement: `disk space + RAM + VRAM >= 247GB`. Less memory = slower but still works via disk offloading.

| Quant | Disk | Notes |
|---|---|---|
| UD-TQ1_0 (1.8-bit) | 247GB | Fits 1x24GB GPU + 256GB RAM with MoE offload; ~1-2 tok/s |
| UD-Q2_K_XL (2-bit) | 360GB | Recommended balance of size and accuracy |
| Q8 | 1.09TB | Requires 8xH200 GPUs |

> [!tip] Memory tip
> For best performance, VRAM + RAM combined should equal the quant size. Otherwise llama.cpp disk offloads via mmap -- slower but functional (e.g. 5-10 tok/s drops to <1 tok/s).

## Kimi-K2-Thinking Guide

Follows Instruct instructions with differences in settings and chat template.

> [!tip] Precision note
> Full precision only needs 4-bit or 5-bit Dynamic GGUFs (e.g. UD_Q4_K_XL) because the model was originally released in INT4 format. Higher-bit quantization is unnecessary in most cases.

### Official Recommended Settings

Per [Moonshot AI](https://huggingface.co/moonshotai/Kimi-K2-Thinking):

- **Temperature = 1.0** (reduce repetition/incoherence)
- **Context length** = 98,304 (up to 256K)
- **min_p = 0.01** (suppress unlikely tokens; llama.cpp default is 0.05)
- Different tools may require different settings

Example chat template for "What is 1+1?":

```
<|im_system|>system<|im_middle|>You are Kimi, an AI assistant created by Moonshot AI.<|im_end|><|im_user|>user<|im_middle|>What is 1+1?<|im_end|><|im_assistant|>assistant<|im_middle|>
```

### Run Kimi K2 Thinking in llama.cpp

#### Step 1 -- Build llama.cpp

Latest `llama.cpp` from [GitHub](https://github.com/ggml-org/llama.cpp). Set `-DGGML_CUDA=OFF` for CPU-only. For Apple Mac/Metal: `-DGGML_CUDA=OFF` (Metal on by default).

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-quantize llama-cli llama-gguf-split llama-mtmd-cli
cp llama.cpp/build/bin/llama-* llama.cpp
```

#### Step 2 -- Run via HF repo

`UD-TQ1_0` is the quantization type. `export LLAMA_CACHE="folder"` to force save location.

```bash
export LLAMA_CACHE="unsloth/Kimi-K2-Thinking-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/Kimi-K2-Thinking-GGUF:UD-TQ1_0 \
    --n-gpu-layers 99 \
    --temp 1.0 \
    --min-p 0.01 \
    --ctx-size 16384 \
    --seed 3407 \
    -ot ".ffn_.*_exps.=CPU"
```

Uses ~8GB GPU memory with MoE offloading. If you have ~360GB combined GPU memory, remove `-ot ".ffn_.*_exps.=CPU"` for maximum speed.

> [!info] MoE offloading options
> `-ot ".ffn_.*_exps.=CPU"` -- offload all MoE layers (least VRAM, default above)
> `-ot ".ffn_(up|down)_exps.=CPU"` -- offload up/down projection MoE layers only
> `-ot ".ffn_(up)_exps.=CPU"` -- offload only up projection MoE layers (more GPU memory needed)
> `-ot "\.(6|7|8|9|[0-9][0-9]|[0-9][0-9][0-9])\.ffn_(gate|up|down)_exps.=CPU"` -- offload gate/up/down MoE layers from layer 6+ only

#### Step 3 -- Download the model

After `pip install huggingface_hub hf_transfer`. **Recommended: 2-bit dynamic quant `UD-Q2_K_XL`** for size/accuracy balance. All versions: [huggingface.co/unsloth/Kimi-K2-Thinking-GGUF](https://huggingface.co/unsloth/Kimi-K2-Thinking-GGUF).

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0" # Can sometimes rate limit, so set to 0 to disable
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Kimi-K2-Thinking-GGUF",
    local_dir = "unsloth/Kimi-K2-Thinking-GGUF",
    allow_patterns = ["*UD-TQ1_0*"], # Use "*UD-Q2_K_XL*" for Dynamic 2bit (381GB)
)
```

> [!info] Stuck downloads
> If downloads get stuck at 90-95%, see [[125-basics-troubleshooting-and-faqs|Troubleshooting & FAQs]]

#### Step 4-5 -- Run with local file

Adjust `--threads -1` (CPU threads, default = max), `--ctx-size 16384` (context), `--n-gpu-layers 99` (GPU offload; combine with MoE CPU offloading for best performance).

```bash
./llama.cpp/llama-cli \
    --model unsloth/Kimi-K2-Thinking-GGUF/UD-TQ1_0/Kimi-K2-Thinking-UD-TQ1_0-00001-of-00006.gguf \
    --n-gpu-layers 99 \
    --temp 1.0 \
    --min_p 0.01 \
    --ctx-size 16384 \
    --seed 3407 \
    -ot ".ffn_.*_exps.=CPU"
```

### No Thinking Tags?

No thinking tags in output is normal/intended. Add `--special` flag to your llama.cpp command to see the thinking token. You may also see `<|im_end|>` at the end -- this is a special token visible when printing special tokens. Set it as a stop string to hide it.

## Deploy with llama-server and OpenAI's completion library

After installing llama.cpp, launch an OpenAI-compatible server:

```bash
./llama.cpp/llama-server \
    --model unsloth/Kimi-K2-Thinking-GGUF/UD-TQ1_0/Kimi-K2-Thinking-UD-TQ1_0-00001-of-00006.gguf \
    --alias "unsloth/Kimi-K2-Thinking" \
    -fa on \
    --n-gpu-layers 999 \
    -ot ".ffn_.*_exps.=CPU" \
    --min_p 0.01 \
    --ctx-size 16384 \
    --port 8001 \
    --jinja
```

Then after `pip install openai`:

```python
from openai import OpenAI
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
    model = "unsloth/Kimi-K2-Thinking",
    messages = [{"role": "user", "content": "What is 2+2?"},],
)
print(completion.choices[0].message.content)
```

## Tokenizer quirks and bug fixes

- **2025-11-07:** Notified Kimi team and fixed the default system prompt `You are Kimi, an AI assistant created by Moonshot AI.` not appearing on first user prompt. See [HF discussion](https://huggingface.co/moonshotai/Kimi-K2-Thinking/discussions/12).
- **2025-07-16:** Kimi K2 updated tokenizer to enable multiple tool calls. [Source](https://x.com/Kimi_Moonshot/status/1945050874067476962).
- **2025-07-18:** Fixed system prompt issue. [Fix discussion](https://huggingface.co/moonshotai/Kimi-K2-Instruct/discussions/28).

**Fix for old checkpoints** -- download the first GGUF split, or apply the fix manually:

```bash
wget https://huggingface.co/unsloth/Kimi-K2-Instruct/raw/main/chat_template.jinja
./llama.cpp ... --chat-template-file /dir/to/chat_template.jinja
```

### Tokenizer regex

Kimi K2's tokenizer is nearly identical to GPT-4o's. Both tokenize numbers in groups of 1-3 digits. Key difference: Kimi handles Han/Chinese characters more extensively. See [tokenization_kimi.py](https://huggingface.co/moonshotai/Kimi-K2-Instruct/blob/main/tokenization_kimi.py) and [llama.cpp source](https://github.com/ggml-org/llama.cpp/blob/55c509daf51d25bfaee9c8b8ce6abff103d4473b/src/llama-vocab.cpp#L400).

```python
pat_str = "|".join(
    [
        r"""[\p{Han}]+""",
        r"""[^\r\n\p{L}\p{N}]?[\p{Lu}\p{Lt}\p{Lm}\p{Lo}\p{M}&&[^\p{Han}]]*[\p{Ll}\p{Lm}\p{Lo}\p{M}&&[^\p{Han}]]+(?i:'s|'t|'re|'ve|'m|'ll|'d)?""",
        r"""[^\r\n\p{L}\p{N}]?[\p{Lu}\p{Lt}\p{Lm}\p{Lo}\p{M}&&[^\p{Han}]]+[\p{Ll}\p{Lm}\p{Lo}\p{M}&&[^\p{Han}]]*(?i:'s|'t|'re|'ve|'m|'ll|'d)?""",
        r"""\p{N}{1,3}""",
        r""" ?[^\s\p{L}\p{N}]+[\r\n]*""",
        r"""\s*[\r\n]+""",
        r"""\s+(?!\S)""",
        r"""\s+""",
    ]
)
```

**Correct EOS token** is `<|im_end|>` (not `[EOS]`) -- fixed in Unsloth model conversions. See [PR #14654](https://github.com/ggml-org/llama.cpp/pull/14654) and [issue #14642](https://github.com/ggml-org/llama.cpp/issues/14642#issuecomment-3067324745).

## Kimi-K2-Instruct Guide

### Official Recommended Settings

Per [Moonshot AI](https://huggingface.co/moonshotai/Kimi-K2-Instruct):

- **Temperature = 0.6** (reduce repetition/incoherence)
- **min_p = 0.01** (suppress unlikely tokens)
- Default system prompt: `You are a helpful assistant`
- Optional (Moonshot suggested): `You are Kimi, an AI assistant created by Moonshot AI.`

### Chat template and prompt format

Kimi Chat uses BOS token. Roles enclosed with `<|im_middle|>`, each with own token (`<|im_system|>`, `<|im_user|>`, `<|im_assistant|>`).

```python
<|im_system|>system<|im_middle|>You are a helpful assistant<|im_end|><|im_user|>user<|im_middle|>What is 1+1?<|im_end|><|im_assistant|>assistant<|im_middle|>2<|im_end|>
```

Separated by newlines:

```
<|im_system|>system<|im_middle|>You are a helpful assistant<|im_end|>
<|im_user|>user<|im_middle|>What is 1+1?<|im_end|>
<|im_assistant|>assistant<|im_middle|>2<|im_end|>
```

### Model uploads

All uploads use Unsloth's calibration dataset optimized for conversational, coding, and reasoning tasks. [BF16 format also available](https://huggingface.co/unsloth/Kimi-K2-Instruct-BF16).

| MoE Bits | Type + Link | Disk Size | Details |
|---|---|---|---|
| 1.66bit | [UD-TQ1_0](https://huggingface.co/unsloth/Kimi-K2-Instruct-GGUF/tree/main/UD-TQ1_0) | **245GB** | 1.92/1.56bit |
| 1.78bit | [UD-IQ1_S](https://huggingface.co/unsloth/Kimi-K2-Instruct-GGUF/tree/main/UD-IQ1_S) | **281GB** | 2.06/1.56bit |
| 1.93bit | [UD-IQ1_M](https://huggingface.co/unsloth/Kimi-K2-Instruct-GGUF/tree/main/UD-IQ1_M) | **304GB** | 2.5/2.06/1.56 |
| 2.42bit | [UD-IQ2_XXS](https://huggingface.co/unsloth/Kimi-K2-Instruct-GGUF/tree/main/UD-IQ2_XXS) | **343GB** | 2.5/2.06bit |
| 2.71bit | [UD-Q2_K_XL](https://huggingface.co/unsloth/Kimi-K2-Instruct-GGUF/tree/main/UD-Q2_K_XL) | **381GB** | 3.5/2.5bit |
| 3.12bit | [UD-IQ3_XXS](https://huggingface.co/unsloth/Kimi-K2-Instruct-GGUF/tree/main/UD-IQ3_XXS) | **417GB** | 3.5/2.06bit |
| 3.5bit | [UD-Q3_K_XL](https://huggingface.co/unsloth/Kimi-K2-Instruct-GGUF/tree/main/UD-Q3_K_XL) | **452GB** | 4.5/3.5bit |
| 4.5bit | [UD-Q4_K_XL](https://huggingface.co/unsloth/Kimi-K2-Instruct-GGUF/tree/main/UD-Q4_K_XL) | **588GB** | 5.5/4.5bit |
| 5.5bit | [UD-Q5_K_XL](https://huggingface.co/unsloth/Kimi-K2-Instruct-GGUF/tree/main/UD-Q5_K_XL) | **732GB** | 6.5/5.5bit |

### Run Instruct in llama.cpp

#### Step 1 -- Build

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-quantize llama-cli llama-gguf-split llama-mtmd-cli
cp llama.cpp/build/bin/llama-* llama.cpp
```

#### Step 2 -- Run via HF repo

`UD-IQ1_S` is the quantization type. For the September 2025 update, change model name from `Kimi-K2-Instruct` to `Kimi-K2-Instruct-0905`. MoE offloading options same as Thinking guide above.

```bash
export LLAMA_CACHE="unsloth/Kimi-K2-Instruct-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/Kimi-K2-Instruct-GGUF:TQ1_0 \
    --n-gpu-layers 99 \
    --temp 0.6 \
    --min-p 0.01 \
    --ctx-size 16384 \
    --seed 3407 \
    -ot ".ffn_.*_exps.=CPU"
```

#### Step 3 -- Download

After `pip install huggingface_hub hf_transfer`. **Recommended: 2-bit `UD-Q2_K_XL`** for size/accuracy balance. All versions: [Kimi-K2-Instruct-GGUF](https://huggingface.co/unsloth/Kimi-K2-Instruct-GGUF).

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0" # Can sometimes rate limit, so set to 0 to disable
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Kimi-K2-Instruct-GGUF",
    local_dir = "unsloth/Kimi-K2-Instruct-GGUF",
    allow_patterns = ["*UD-TQ1_0*"], # Dynamic 1bit (281GB) Use "*UD-Q2_K_XL*" for Dynamic 2bit (381GB)
)
```

#### Step 4-5 -- Run with local file

```bash
./llama.cpp/llama-cli \
    --model unsloth/Kimi-K2-Instruct-GGUF/UD-TQ1_0/Kimi-K2-Instruct-UD-TQ1_0-00001-of-00005.gguf \
    --n-gpu-layers 99 \
    --temp 0.6 \
    --min_p 0.01 \
    --ctx-size 16384 \
    --seed 3407 \
    -ot ".ffn_.*_exps.=CPU"
```

## Flappy Bird + other tests

Kimi K2 one-shots all Unsloth test tasks including Flappy Bird and [[025-models-tutorials-deepseek-r1-0528-how-to-run-locally|Heptagon]] even at 2-bit.

### Flappy Bird prompt

```
Create a Flappy Bird game in Python. You must include these things:
1. You must use pygame.
2. The background color should be randomly chosen and is a light shade. Start with a light blue color.
3. Pressing SPACE multiple times will accelerate the bird.
4. The bird's shape should be randomly chosen as a square, circle or triangle. The color should be randomly chosen as a dark color.
5. Place on the bottom some land colored as dark brown or yellow chosen randomly.
6. Make a score shown on the top right side. Increment if you pass pipes and don't hit them.
7. Make randomly spaced pipes with enough space. Color them randomly as dark green or light brown or a dark gray shade.
8. When you lose, show the best score. Make the text inside the screen. Pressing q or Esc will quit the game. Restarting is pressing SPACE again.
The final game should be inside a markdown section in Python. Check your code for errors and fix them before the final markdown section.
```

### Heptagon prompt

Per [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1j7r47l/i_just_made_an_animation_of_a_ball_bouncing/) -- tests creating a physics engine for balls in a spinning heptagon:

```
Write a Python program that shows 20 balls bouncing inside a spinning heptagon:\n- All balls have the same radius.\n- All balls have a number on it from 1 to 20.\n- All balls drop from the heptagon center when starting.\n- Colors are: #f8b862, #f6ad49, #f39800, #f08300, #ec6d51, #ee7948, #ed6d3d, #ec6800, #ec6800, #ee7800, #eb6238, #ea5506, #ea5506, #eb6101, #e49e61, #e45e32, #e17b34, #dd7a56, #db8449, #d66a35\n- The balls should be affected by gravity and friction, and they must bounce off the rotating walls realistically. There should also be collisions between balls.\n- The material of all the balls determines that their impact bounce height will not exceed the radius of the heptagon, but higher than ball radius.\n- All balls rotate with friction, the numbers on the ball can be used to indicate the spin of the ball.\n- The heptagon is spinning around its center, and the speed of spinning is 360 degrees per 5 seconds.\n- The heptagon size should be large enough to contain all the balls.\n- Do not use the pygame library; implement collision detection algorithms and collision response etc. by yourself. The following Python libraries are allowed: tkinter, math, numpy, dataclasses, typing, sys.\n- All codes should be put in a single Python file.
```

#kimi-k2-thinking #gguf #local-inference #llama-cpp #performance-tuning
