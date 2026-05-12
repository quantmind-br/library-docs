---
title: 'Tutorial: How to Fine-tune gpt-oss'
url: https://unsloth.ai/docs/models/gpt-oss-how-to-run-and-fine-tune/tutorial-how-to-fine-tune-gpt-oss.md
source: llms
fetched_at: 2026-04-27T18:13:52.912818566-03:00
rendered_js: false
word_count: 2206
summary: This tutorial guides the user through the process of fine-tuning a custom gpt-oss model, detailing methods for training either locally or within Google Colab. It covers setup, configuration parameters like sequence length and LoRA settings, and data preparation using multilingual datasets.
tags:
    - gpt-oss
    - fine-tuning
    - unsloth
    - colab
    - lora
    - llm-training
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:38:00Z
---

# Tutorial: How to Fine-tune gpt-oss

Fine-tune gpt-oss with Unsloth either [locally](#local-gpt-oss-fine-tuning) or free via [Google Colab](#colab-gpt-oss-fine-tuning).

> [!tip] Aug 28 update
> You can now export QLoRA fine-tuned gpt-oss to llama.cpp, vLLM, HF etc.
> [Unsloth Flex Attention](https://unsloth.ai/docs/models/long-context-gpt-oss-training#introducing-unsloth-flex-attention-support) enables >8x longer context, >50% less VRAM, >1.5x faster training.

> **Quickstart:** [Colab notebook for gpt-oss-20b](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(20B\)-Fine-tuning.ipynb)

**Performance vs other FA2 implementations:** 1.5x faster training, 70% less VRAM, 10x longer context — no accuracy loss.

**VRAM requirements:**

| Mode | gpt-oss-20b | gpt-oss-120b |
|------|-------------|--------------|
| QLoRA | 14 GB | 65 GB |
| BF16 LoRA | 44 GB | 210 GB |

## Colab gpt-oss Fine-tuning

Use our [Colab notebooks](https://unsloth.ai/docs/get-started/unsloth-notebooks). Run cells top to bottom; use **Run all** first pass. If a cell errors, re-run it.

### Step 1 — Install Unsloth (Colab)

First cell installs Unsloth and prints GPU/memory info.

### Step 2 — Configure gpt-oss and Reasoning Effort

Load **`gpt-oss-20b`** using Unsloth's [linearized version](https://unsloth.ai/docs/models/gpt-oss-how-to-run-and-fine-tune/..#making-efficient-gpt-oss-fine-tuning-work) (no other version works).

- **`max_seq_length = 1024`** — recommended for quick testing
- **`load_in_4bit = True`** — set `False` for LoRA (needs >=43GB VRAM); MUST also set `model_name = "unsloth/gpt-oss-20b-BF16"`

Note: dtype is explicitly set to `float32` for correct training behavior.

### Step 3 — Fine-tuning Hyperparameters (LoRA)

Adds LoRA adapters (~1% of parameters trained). See [LoRA hyperparameters guide](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide/lora-hyperparameters-guide) for details.

> [!info] Monitor training loss to avoid [overfitting](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide/lora-hyperparameters-guide#avoiding-overfitting-and-underfitting). Don't set values too high.

### Step 4 — Try Inference

Notebook has a "Reasoning Effort" section demonstrating gpt-oss inference. Optional — you'll run the model again after fine-tuning.

### Step 5 — Data Preparation

Uses [`HuggingFaceH4/Multilingual-Thinking`](https://huggingface.co/datasets/HuggingFaceH4/Multilingual-Thinking) — chain-of-thought reasoning examples translated from English into 4 languages. Same dataset as OpenAI's fine-tuning cookbook.

**Reasoning effort** controls reasoning depth: `low` (default), `medium`, or `high`.

```python
tokenizer.apply_chat_template(
    text,
    tokenize = False,
    add_generation_prompt = False,
    reasoning_effort = "medium",
)
```

Format dataset with gpt-oss prompt:

```python
from unsloth.chat_templates import standardize_sharegpt
dataset = standardize_sharegpt(dataset)
dataset = dataset.map(formatting_prompts_func, batched = True,)
```

gpt-oss uses [OpenAI Harmony format](https://github.com/openai/harmony) with tags: `<|start|>`, `<|message|>`, `<|return|>`.

> [!info] Unsloth fixes the chat template — see [technical details](https://x.com/danielhanchen/status/1953901104150065544).

See [dataset guide](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide/datasets-guide) for custom data adaptation.

### Step 6 — Train the Model

Pre-selected hyperparameters for optimal results. Example trains 60 steps; for full run set `num_train_epochs=1` and `max_steps=None`. Monitor loss — should decrease over time.

### Step 7 — Inference: Run Your Trained Model

Modify instruction/input, leave output blank. Example tests French reasoning via system prompt matching dataset structure.

### Step 8 — Save/Export Your Model

Export formats:

- **MXFP4** via `save_method="mxfp4"` — 75% less disk, 50% less VRAM, 5-10x faster merge, faster GGUF conversion
- **bf16** via `save_method="merged_16bit"` (on-demand MXFP4 dequantization)

> [!tip] Saving/merging QLoRA models to GGUF is now supported for other frameworks (HF, llama.cpp).

```python
model.save_pretrained_merged(save_directory, tokenizer, save_method="mxfp4")
```

```python
model.push_to_hub_merged(repo_name, tokenizer=tokenizer, token= hf_token, save_method="mxfp4")
```

#### Saving to Llama.cpp

1. Build llama.cpp (`-DGGML_CUDA=OFF` for CPU-only):

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cp
```

2. Convert MXFP4 merged model:

```bash
python3 llama.cpp/convert_hf_to_gguf.py gpt-oss-finetuned-merged/ --outfile gpt-oss-finetuned-mxfp4.gguf
```

3. Run inference (recommended: `temperature=1.0`, `top_p=1.0`, `top_k=0`):

```bash
llama.cpp/llama-cli --model gpt-oss-finetuned-mxfp4.gguf \
    --jinja -ngl 99 --threads -1 --ctx-size 16384 \
    --temp 1.0 --top-p 1.0 --top-k 0 \
     -p "The meaning to life and the universe is"
```

## Local gpt-oss Fine-tuning

gpt-oss-20b fine-tuning works on 14GB VRAM; recommend >=16GB for stability.

> [!info] Download our Colab [notebooks](https://unsloth.ai/docs/get-started/unsloth-notebooks) and adapt for local use. Also available via [Docker image](https://unsloth.ai/docs/models/qwen3-coder-next).

### Step 1 — Install Unsloth Locally

Ensure [compatibility](https://unsloth.ai/docs/get-started/fine-tuning-for-beginners/unsloth-requirements). `pip install unsloth` won't work — need latest PyTorch/Triton:

```python
# We're installing the latest Torch, Triton, OpenAI's Triton kernels, Transformers and Unsloth!
!pip install --upgrade -qqq uv
try: import numpy; install_numpy = f"numpy=={numpy.__version__}"
except: install_numpy = "numpy"
!uv pip install -qqq \
    "torch>=2.8.0" "triton>=3.4.0" {install_numpy} \
    "unsloth_zoo[base] @ git+https://github.com/unslothai/unsloth-zoo" \
    "unsloth[base] @ git+https://github.com/unslothai/unsloth" \
    torchvision bitsandbytes \
    git+https://github.com/huggingface/transformers \
    git+https://github.com/triton-lang/triton.git@05b2c186c1b6c9a08375389d5efe9cb4c401c075#subdirectory=python/triton_kernels
```

### Step 2 — Configure gpt-oss and Reasoning Effort

Load **`gpt-oss-20b`** via [linearized version](https://unsloth.ai/docs/models/gpt-oss-how-to-run-and-fine-tune/..#making-efficient-gpt-oss-fine-tuning-work) (required for QLoRA).

- **`max_seq_length = 2048`** — recommended for testing
- **`load_in_4bit = True`** — `False` for LoRA (>=43GB VRAM); MUST also use `model_name = "unsloth/gpt-oss-20b-BF16"`

```python
from unsloth import FastLanguageModel
import torch
max_seq_length = 1024
dtype = None

# 4bit pre quantized models we support for 4x faster downloading + no OOMs.
fourbit_models = [
    "unsloth/gpt-oss-20b-unsloth-bnb-4bit", # 20B model using bitsandbytes 4bit quantization
    "unsloth/gpt-oss-120b-unsloth-bnb-4bit",
    "unsloth/gpt-oss-20b", # 20B model using MXFP4 format
    "unsloth/gpt-oss-120b",
] # More models at https://huggingface.co/unsloth

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/gpt-oss-20b",
    dtype = dtype, # None for auto detection
    max_seq_length = max_seq_length, # Choose any for long context!
    load_in_4bit = True,  # 4 bit quantization to reduce memory
    full_finetuning = False, # [NEW!] We have full finetuning now!
    # token = "hf_...", # use one if using gated models
)
```

### Step 3 — Fine-tuning Hyperparameters (LoRA)

```python
model = FastLanguageModel.get_peft_model(
    model,
    r = 8, # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 16,
    lora_dropout = 0, # Supports any, but = 0 is optimized
    bias = "none",    # Supports any, but = "none" is optimized
    # [NEW] "unsloth" uses 30% less VRAM, fits 2x larger batch sizes!
    use_gradient_checkpointing = "unsloth", # True or "unsloth" for very long context
    random_state = 3407,
    use_rslora = False,  # We support rank stabilized LoRA
    loftq_config = None, # And LoftQ
)
```

### Step 4 — Data Preparation

```python
def formatting_prompts_func(examples):
    convos = examples["messages"]
    texts = [tokenizer.apply_chat_template(convo, tokenize = False, add_generation_prompt = False) for convo in convos]
    return { "text" : texts, }
pass

from datasets import load_dataset

dataset = load_dataset("HuggingFaceH4/Multilingual-Thinking", split="train")
dataset
```

Apply reasoning effort and format:

```python
tokenizer.apply_chat_template(
    text,
    tokenize = False,
    add_generation_prompt = False,
    reasoning_effort = "medium",
)
```

```python
from unsloth.chat_templates import standardize_sharegpt
dataset = standardize_sharegpt(dataset)
dataset = dataset.map(formatting_prompts_func, batched = True,)
```

### Step 5 — Train the Model

```python
from trl import SFTConfig, SFTTrainer
trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    args = SFTConfig(
        per_device_train_batch_size = 1,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
        # num_train_epochs = 1, # Set this for 1 full training run.
        max_steps = 30,
        learning_rate = 2e-4,
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir = "outputs",
        report_to = "none", # Use this for WandB etc
    ),
)
```

Monitor loss — should decrease over time.

### Step 6 — Inference: Run Your Trained Model

```python
messages = [
    {"role": "system", "content": "reasoning language: French\n\nYou are a helpful assistant that can solve mathematical problems."},
    {"role": "user", "content": "Solve x^5 + 3x^4 - 10 = 3."},
]
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt = True,
    return_tensors = "pt",
    return_dict = True,
    reasoning_effort = "medium",
).to(model.device)
from transformers import TextStreamer
_ = model.generate(**inputs, max_new_tokens = 2048, streamer = TextStreamer(tokenizer))
```

### Step 7 — Save and Export Your Model

Export with on-demand MXFP4 dequantization:

```python
model.save_pretrained_merged(save_directory, tokenizer)
```

```python
model.push_to_hub_merged(repo_name, tokenizer=tokenizer, token= hf_token)
```

#### Saving to Llama.cpp

1. Build llama.cpp:

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cp
```

2. Convert and quantize:

```bash
python3 llama.cpp/convert_hf_to_gguf.py gpt-oss-finetuned-merged/ --outfile gpt-oss-finetuned.gguf
llama.cpp/llama-quantize gpt-oss-finetuned.gguf  gpt-oss-finetuned-Q8_0.gguf Q8_0
```

3. Run inference:

```bash
llama.cpp/llama-cli --model gpt-oss-finetuned-Q8_0.gguf \
    --jinja -ngl 99 --threads -1 --ctx-size 16384 \
    --temp 1.0 --top-p 1.0 --top-k 0 \
     -p "The meaning to life and the universe is"
```

## FAQ

**Q: Can I export to HF, llama.cpp GGUF, or vLLM?**
Yes — see [saving to GGUF/vLLM](https://unsloth.ai/docs/models/long-context-gpt-oss-training#new-saving-to-gguf-vllm-after-gpt-oss-training).

**Q: Can I do fp4 or MXFP4 training?**
No. No framework supports fp4/MXFP4 training. Unsloth is the only framework supporting QLoRA 4-bit fine-tuning for gpt-oss (4x less VRAM).

**Q: Can I export to MXFP4 format after training?**
No — no library/framework supports this currently.

**Q: Can I do RL/GRPO with gpt-oss?**
Yes. Unsloth supports RL for gpt-oss with GRPO/GSPO. Works on free Kaggle notebook with fastest RL inference. See [[009-models-gpt-oss-how-to-run-and-fine-tune-gpt-oss-reinforcement-learning-tutorial-how-to-train-gpt-oss-with-rl|Tutorial: How to Train gpt-oss with RL]].

Acknowledgement: thanks to [Eyera](https://huggingface.co/Orenguteng) for contributing to this guide.

---

# Agent Instructions: Querying This Documentation

If you need additional information not on this page, query dynamically via:

```
GET https://unsloth.ai/docs/models/gpt-oss-how-to-run-and-fine-tune/tutorial-how-to-fine-tune-gpt-oss.md?ask=<question>
```

The question should be specific, self-contained, and in natural language. Returns a direct answer with relevant excerpts and sources.

#gpt-oss #fine-tuning #lora #colab #unsloth
