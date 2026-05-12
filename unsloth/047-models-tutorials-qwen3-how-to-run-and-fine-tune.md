---
title: Qwen3 - How to Run & Fine-tune
url: https://unsloth.ai/docs/models/tutorials/qwen3-how-to-run-and-fine-tune.md
source: llms
fetched_at: 2026-04-27T18:13:55.39986379-03:00
rendered_js: false
word_count: 1615
summary: This document serves as a comprehensive guide and reference for utilizing the Qwen3 models, detailing how to run them with optimal performance using Unsloth Dynamic 2.0, and providing instructions on fine-tuning techniques like Reinforcement Learning.
tags:
    - qwen3
    - unsloth
    - fine-tuning
    - llm
    - gguf
    - tutorial
category: guide
optimized: true
optimized_at: 2026-04-27T21:35:00Z
---

# Qwen3 - How to Run & Fine-tune

Qwen3: SOTA reasoning, instruction-following, agent capabilities, multilingual support.

> [!tip] **NEW** (July 2025): [[045-models-tutorials-qwen3-how-to-run-and-fine-tune-qwen3-2507|Qwen-2507]] — latest model update.

All uploads use Unsloth [[115-basics-unsloth-dynamic-2.0-ggufs|Dynamic 2.0]] for SOTA 5-shot MMLU and KL Divergence performance — run and fine-tune quantized Qwen LLMs with minimal accuracy loss.

Native 128K context via YaRN (extends original 40K window). Unsloth supports fine-tuning and [[072-get-started-reinforcement-learning-rl-guide|Reinforcement Learning]] of Qwen3 and Qwen3 MOE — 2x faster, 70% less VRAM, 8x longer context.

Free Colab: [Qwen3 (14B) Reasoning + Conversational](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(14B\)-Reasoning-Conversational.ipynb)

### Qwen3 Unsloth Dynamic 2.0 Uploads

**Dynamic 2.0 GGUF (to run):** 0.6B, 1.7B, 4B, 8B, 14B, 30B-A3B, 32B, 235B-A22B
- Pattern: `unsloth/Qwen3-{SIZE}-GGUF`

**128K Context GGUF:** 4B, 8B, 14B, 30B-A3B, 32B, 235B-A22B
- Pattern: `unsloth/Qwen3-{SIZE}-128K-GGUF`

**Dynamic 4-bit Safetensor (to finetune/deploy):** 0.6B, 1.7B, 4B, 8B, 14B, 30B-A3B, 32B
- Pattern: `unsloth/Qwen3-{SIZE}-unsloth-bnb-4bit`

## Running Qwen3

For 6+ tokens/sec inference, available memory should match or exceed model size (e.g., 30GB 1-bit quant needs ~150GB memory; 180GB Q2_K_XL quant needs ~180GB unified memory/VRAM+RAM).

> [!info] Running with less memory than model size is possible but slower. Sufficient memory is only needed for max throughput.

### Official Recommended Settings

| Parameter | Non-Thinking | Thinking |
|-----------|-------------|----------|
| Temperature | 0.7 | 0.6 |
| Min_P | 0.0 (0.01 works well; llama.cpp default 0.1) | 0.0 |
| Top_P | 0.8 | 0.95 |
| TopK | 20 | 20 |

**Chat template/prompt format:**

```
<|im_start|>user\nWhat is 2+2?<|im_end|>\n<|im_start|>assistant\n
```

> [!tip] For non-thinking mode, enclose ` 3 ` and ` SI ` with nothing:
> ```
> <|im_start|>user\nWhat is 2+2?<|im_end|>\n<|im_start|>assistant\n 3 \n\n SI \n\n
> ```

> [!warning] For thinking-mode, DO NOT use greedy decoding — causes performance degradation and endless repetitions.

### Switching Between Thinking and Non-Thinking Mode

Qwen3 has built-in thinking mode (similar to [[049-models-tutorials-qwq-32b-how-to-run-effectively|QwQ-32B]]). Switching instructions differ by inference engine.

#### llama.cpp and Ollama

Add `/think` or `/no_think` to user prompts or system messages. Model follows the most recent instruction in multi-turn conversations.

```
> Who are you /no_think

 3

 SI

I am Qwen, a large-scale language model developed by Alibaba Cloud. [...]

> How many 'r's are in 'strawberries'? /think

 3
Okay, let's see. The user is asking how many times the letter 'r' appears in the word "strawberries". [...]
 SI

The word strawberries contains 3 instances of the letter r. [...]
```

#### transformers and vLLM

**Thinking mode** (`enable_thinking=True`, default):

```python
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=True  # Default is True
)
```

Model generates ` 3 ... SI ` block before the final answer for reasoning/planning.

**Non-thinking mode** (`enable_thinking=False`):

```python
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False  # Disables thinking mode
)
```

Direct responses, no ` 3 ` blocks, no chain-of-thought.

### Ollama: Run Qwen3 Tutorial

1. Install (supports models up to 32B; for 235B-A22B see [below](#running-qwen3-235b-a22b)):

```bash
apt-get update
apt-get install pciutils -y
curl -fsSL https://ollama.com/install.sh | sh
```

2. Run:

```bash
ollama run hf.co/unsloth/Qwen3-8B-GGUF:UD-Q4_K_XL
```

3. Disable thinking with `  </invoke>` in prompt or system prompt.

> [!warning] If looping occurs, Ollama may have set context length to ~2,048. Bump to 32,000 and retry.

### Llama.cpp: Run Qwen3 Tutorial

1. Build llama.cpp. Set `-DGGML_CUDA=OFF` for CPU-only or Apple Metal (on by default):

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

2. Download model (install `pip install huggingface_hub hf_transfer` first):

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Qwen3-14B-GGUF",
    local_dir = "unsloth/Qwen3-14B-GGUF",
    allow_patterns = ["*UD-Q4_K_XL*"],
)
```

3. Run:

```bash
./llama.cpp/llama-cli \
    --model unsloth/Qwen3-14B-GGUF/Qwen3-14B-UD-Q2_K_XL.gguf \
    --ctx-size 16384 \
    --n-gpu-layers 99 \
    -ot ".ffn_.*_exps.=CPU" \
    --seed 3407 \
    --prio 3 \
    --temp 0.6 \
    --min-p 0.0 \
    --top-p 0.95 \
    --top-k 20 \
    -no-cnv
```

Disable thinking with `  </invoke>` in prompt or system prompt.

### Running Qwen3-235B-A22B

1. Follow llama.cpp build steps above.
2. Download:

   ```python
   # !pip install huggingface_hub hf_transfer
   import os
   os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
   from huggingface_hub import snapshot_download
   snapshot_download(
       repo_id = "unsloth/Qwen3-235B-A22B-GGUF",
       local_dir = "unsloth/Qwen3-235B-A22B-GGUF",
       allow_patterns = ["*UD-Q2_K_XL*"],
   )
   ```
3. Run:

```bash
./llama.cpp/llama-cli \
    --model unsloth/Qwen3-235B-A22B-GGUF/Qwen3-235B-A22B-UD-Q2_K_XL.gguf \
    --ctx-size 16384 \
    --n-gpu-layers 99 \
    -ot ".ffn_.*_exps.=CPU" \
    --seed 3407 \
    --prio 3 \
    --temp 0.6 \
    --min-p 0.0 \
    --top-p 0.95 \
    --top-k 20 \
    -no-cnv \
    --prompt "<|im_start|>user\nCreate a Flappy Bird game in Python. You must include these things:\n1. You must use pygame.\n2. The background color should be randomly chosen and is a light shade. Start with a light blue color.\n3. Pressing SPACE multiple times will accelerate the bird.\n4. The bird's shape should be randomly chosen as a square, circle or triangle. The color should be randomly chosen as a dark color.\n5. Place on the bottom some land colored as dark brown or yellow chosen randomly.\n6. Make a score shown on the top right side. Increment if you pass pipes and don't hit them.\n7. Make randomly spaced pipes with enough space. Color them randomly as dark green or light brown or a dark gray shade.\n8. When you lose, show the best score. Make the text inside the screen. Pressing q or Esc will quit the game. Restarting is pressing SPACE again.\nThe final game should be inside a markdown section in Python. Check your code for errors and fix them before the final markdown section.<|im_end|>\n<|im_start|>assistant\n"
```

4. Tune: `--threads 32` for CPU threads, `--ctx-size 16384` for context, `--n-gpu-layers 99` for GPU offloading (reduce if OOM, remove for CPU-only).

> [!tip] Use `-ot ".ffn_.*_exps.=CPU"` to offload all MoE layers to CPU — fits all non-MoE layers on 1 GPU. Customize the regex to fit more layers with more GPU capacity.

## Fine-tuning Qwen3 with Unsloth

2x faster, 70% less VRAM, 8x longer context. Qwen3 (14B) fits on Google Colab 16GB T4.

**Reasoning preservation:** Fine-tuning with non-reasoning data may affect reasoning ability. Use 75% reasoning + 25% non-reasoning data to retain reasoning. The Conversational notebook uses 75% NVIDIA open-math-reasoning + 25% Maxime FineTome (non-reasoning).

Colab notebooks:

- [Qwen3 (14B) Reasoning + Conversational](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(14B\)-Reasoning-Conversational.ipynb) (recommended)
- [Qwen3 (4B) - Advanced GRPO LoRA](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(4B\)-GRPO.ipynb)
- [Qwen3 (14B) Alpaca](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(14B\)-Alpaca.ipynb) (for Base models)

Install/upgrade:

```
pip install --upgrade --force-reinstall --no-cache-dir unsloth unsloth_zoo
```

### Qwen3 MOE Models Fine-tuning

Supports 30B-A3B and 235B-A22B with [[080-basics-faster-moe|Faster MOE]] (2026 update). 30B-A3B works on 17.5GB VRAM. Router layer disabled by default for fine-tuning.

> [!warning] MOE models require downloading the full 16-bit model and converting to 4-bit on the fly (4-bit BnB MOE models can't be imported directly). Ensure sufficient RAM/disk space.

```python
from unsloth import FastModel
import torch
model, tokenizer = FastModel.from_pretrained(
    model_name = "unsloth/Qwen3-30B-A3B",
    max_seq_length = 2048, # Choose any for long context!
    load_in_4bit = True,  # 4 bit quantization to reduce memory
    load_in_8bit = False, # [NEW!] A bit more accurate, uses 2x memory
    full_finetuning = False, # [NEW!] We have full finetuning now!
    # token = "hf_...", # use one if using gated models
)
```

### Notebook Guide

Click Runtime > Run all. Change model name to match HuggingFace (e.g., `unsloth/Qwen3-8B`, `unsloth/Qwen3-0.6B-unsloth-bnb-4bit`).

Key settings:

- **`max_seq_length = 2048`** — context length (Qwen3 supports 40960; 2048 recommended for testing). Unsloth enables 8x longer context fine-tuning.
- **`load_in_4bit = True`** — 4-bit quantization, 4x memory reduction for 16GB GPUs.
- **`full_finetuning = True`** — full finetuning. **`load_in_8bit = True`** — 8-bit finetuning.

See [[064-get-started-fine-tuning-llms-guide|complete fine-tuning guide]] and [[060-get-started-fine-tuning-llms-guide-datasets-guide|datasets guide]] for end-to-end instructions.

### GRPO with Qwen3

Advanced GRPO notebook with proximity-based reward function (closer answers = rewarded) and HuggingFace Open-R1 math dataset. Uses latest vLLM with improved evaluations.

[Qwen3 (4B) - Advanced GRPO LoRA](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(4B\)-GRPO.ipynb)

Covers:

- Enabling reasoning in Qwen3 (Base) + guiding to specific task
- Pre-finetuning to bypass GRPO's formatting-learning tendency
- Improved evaluation accuracy via regex matching
- Custom GRPO templates beyond 'think' (e.g., `<start_working_out></end_working_out>`)
- Proximity-based scoring: closer answers earn more points (e.g., 9 when answer is 10), outliers penalized

#qwen3 #unsloth #fine-tuning #llm #gguf
