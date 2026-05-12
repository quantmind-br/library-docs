---
title: Qwen3.5 Fine-tuning Guide
url: https://unsloth.ai/docs/models/qwen3.5/fine-tune.md
source: llms
fetched_at: 2026-04-27T18:13:36.417724341-03:00
rendered_js: false
word_count: 1316
summary: This guide explains how to fine-tune the Qwen3.5 model family using Unsloth, detailing various methods like LoRA and Full Fine-Tuning (FFT) across different model sizes, including support for vision and reinforcement learning tasks.
tags:
    - qwen3-5
    - fine-tuning
    - unsloth
    - lora
    - model-training
    - multilingual
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Qwen3.5 Fine-tuning Guide

Fine-tune the [Qwen3.5](https://unsloth.ai/docs/models/qwen3.5) family (0.8B, 2B, 4B, 9B, 27B, 35B-A3B, 122B-A10B) with [Unsloth](https://github.com/unslothai/unsloth). Supports vision, text, and [RL](#reinforcement-learning-rl) fine-tuning.

- **Performance:** 1.5x faster training, 50% less VRAM vs FA2
- **bf16 LoRA VRAM:** 0.8B: 3GB, 2B: 5GB, 4B: 10GB, 9B: 22GB, 27B: 56GB, 35B-A3B: 74GB
- **Languages:** 201 supported
- **Full fine-tuning (FFT)** works but uses 4x more VRAM
- **Reasoning preservation:** Mix reasoning-style examples with direct answers (min 75% reasoning), or emit reasoning fully
- **Export:** GGUF (llama.cpp/Ollama) or [[090-basics-inference-and-deployment-vllm-guide|vLLM]]

### Free Colab notebooks

| [Qwen3.5-**0.8B**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_\(0_8B\)_Vision.ipynb) | [Qwen3.5-**2B**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_\(2B\)_Vision.ipynb) | [Qwen3.5-**4B**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_\(4B\)_Vision.ipynb) | [Qwen3.5-4B **GRPO**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_\(4B\)_Vision_GRPO.ipynb) |
| --- | --- | --- | --- |

A100 notebooks: [Qwen3.5-27B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen_3_5_27B_A100\(80GB\).ipynb), [Qwen3.5-35B-A3B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_MoE.ipynb)

### Update before fine-tuning

**Unsloth Studio:**

```bash
unsloth studio update
```

**Code-based:**

```bash
pip install --upgrade --force-reinstall --no-cache-dir unsloth unsloth_zoo
```

> [!warning]
> - Requires `transformers v5`. Unsloth uses it by default (except Colab).
> - Slower-than-usual training is normal — Qwen3.5 uses custom Mamba Triton kernels; compilation takes longer, especially on T4 GPUs.
> - **QLoRA (4-bit) not recommended** for any Qwen3.5 model (MoE or dense) due to higher-than-normal quantization differences.

## MoE fine-tuning (35B, 122B)

For **Qwen3.5-35B-A3B / 122B-A10B / 397B-A17B**:

- [Qwen3.5-35B-A3B (A100) notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_MoE.ipynb)
- ~12x faster [MoE training update](https://unsloth.ai/docs/basics/faster-moe) with >35% less VRAM and ~6x longer context
- **Use bf16 setups** (LoRA or FFT); MoE QLoRA 4-bit not recommended (BitsandBytes limitations)
- Unsloth MoE kernels enabled by default; switch backend with `UNSLOTH_MOE_BACKEND`
- Router-layer fine-tuning disabled by default for stability
- **122B-A10B** bf16 LoRA: 256GB VRAM; multi-GPU: add `device_map = "balanced"` or follow [[093-basics-multi-gpu-training-with-unsloth|Multi-GPU Guide]]

## Quickstart

### Unsloth Studio Guide

Run and fine-tune in [[097-new-studio|Unsloth Studio]] (MacOS, Windows, Linux). Features: 2x faster training, 70% less VRAM, GGUF/safetensor search, self-healing tool calling, web search, code execution, automatic inference tuning.

1. **Install** — MacOS/Linux/WSL:

```bash
curl -fsSL https://unsloth.ai/install.sh | sh
```

Windows PowerShell:

```bash
irm https://unsloth.ai/install.ps1 | iex
```

2. **Launch:**

```bash
unsloth studio -H 0.0.0.0 -p 8888
```

Open `http://localhost:8888`.

3. **Train** — Search for Qwen3.5, select model/dataset, adjust hyperparameters and context length.
4. **Monitor** — Training loss should decrease steadily; model auto-saves.
5. **Export** — GGUF, safetensor, etc.

### Unsloth Core (code-based)

Minimal SFT recipe for text-only fine-tuning. See [[096-basics-vision-fine-tuning|Vision Fine-tuning]] for multimodal.

> [!info]
> Qwen3.5 is a "Causal Language Model with Vision Encoder" (unified VLM). Install vision deps (`torchvision`, `pillow`) if needed. Keep Transformers up-to-date.
>
> **GRPO** works if you disable fast vLLM inference and use Unsloth inference instead. Follow [[071-get-started-reinforcement-learning-rl-guide-vision-reinforcement-learning-vlm-rl|Vision RL]] notebook examples.

```python
from unsloth import FastLanguageModel
import torch
from datasets import load_dataset
from trl import SFTTrainer, SFTConfig

max_seq_length = 2048  # start small; scale up after it works

# Example dataset (replace with yours). Needs a "text" column.
url = "https://huggingface.co/datasets/laion/OIG/resolve/main/unified_chip2.jsonl"
dataset = load_dataset("json", data_files={"train": url}, split="train")

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "Qwen/Qwen3.5-27B",
    max_seq_length = max_seq_length,
    load_in_4bit = False,     # MoE QLoRA not recommended, dense 27B is fine
    load_in_16bit = True,     # bf16/16-bit LoRA
    full_finetuning = False,
)

model = FastLanguageModel.get_peft_model(
    model,
    r = 16,
    target_modules = [
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_proj", "up_proj", "down_proj",
    ],
    lora_alpha = 16,
    lora_dropout = 0,
    bias = "none",
    # "unsloth" checkpointing is intended for very long context + lower VRAM
    use_gradient_checkpointing = "unsloth",
    random_state = 3407,
    max_seq_length = max_seq_length,
)

trainer = SFTTrainer(
    model = model,
    train_dataset = dataset,
    tokenizer = tokenizer,
    args = SFTConfig(
        max_seq_length = max_seq_length,
        per_device_train_batch_size = 1,
        gradient_accumulation_steps = 4,
        warmup_steps = 10,
        max_steps = 100,
        logging_steps = 1,
        output_dir = "outputs_qwen35",
        optim = "adamw_8bit",
        seed = 3407,
        dataset_num_proc = 1,
    ),
)

trainer.train()
```

> [!info]
> **If OOM:**
> - Drop `per_device_train_batch_size` to **1** and/or reduce `max_seq_length`
> - Keep `use_gradient_checkpointing="unsloth"` on (reduces VRAM, extends context)

**MoE loader example (bf16 LoRA):**

```python
import os
import torch
from unsloth import FastModel

model, tokenizer = FastModel.from_pretrained(
    model_name = "unsloth/Qwen3.5-35B-A3B",
    max_seq_length = 2048,
    load_in_4bit = False,     # MoE QLoRA not recommended, dense 27B is fine
    load_in_16bit = True,     # bf16/16-bit LoRA
    full_finetuning = False,
)
```

Attach LoRA adapters and train similarly to the SFT example above.

## Vision fine-tuning

Unsloth supports [[096-basics-vision-fine-tuning|vision fine-tuning]] for multimodal Qwen3.5 models. Use the notebooks below and change model names as needed.

| [Qwen3.5-**0.8B**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_\(0_8B\)_Vision.ipynb) | [Qwen3.5-**2B**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_\(2B\)_Vision.ipynb) | [Qwen3.5-**4B**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_\(4B\)_Vision.ipynb) | Qwen3.5-**9B** |
| --- | --- | --- | --- |

- [Qwen3-VL GRPO/GSPO RL notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_VL_\(8B\)-Vision-GRPO.ipynb) (change model name to Qwen3.5-4B etc.)

**Layer selection for vision fine-tuning:** Choose which parts to fine-tune — vision layers, language layers, attention/MLP modules. All enabled by default.

```python
model = FastVisionModel.get_peft_model(
    model,
    finetune_vision_layers     = True, # False if not finetuning vision layers
    finetune_language_layers   = True, # False if not finetuning language layers
    finetune_attention_modules = True, # False if not finetuning attention layers
    finetune_mlp_modules       = True, # False if not finetuning MLP layers

    r = 16,                           # The larger, the higher the accuracy, but might overfit
    lora_alpha = 16,                  # Recommended alpha == r at least
    lora_dropout = 0,
    bias = "none",
    random_state = 3407,
    use_rslora = False,               # We support rank stabilized LoRA
    loftq_config = None,               # And LoftQ
    target_modules = "all-linear",    # Optional now! Can specify a list if needed
    modules_to_save=[
        "lm_head",
        "embed_tokens",
    ],
)
```

For multi-image training, see [[096-basics-vision-fine-tuning|multi-image vision guide]].

## Reinforcement Learning (RL)

Train Qwen3.5 with RL, GSPO, GRPO via [free notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_\(4B\)_Vision_GRPO.ipynb).

Works with Unsloth inference (not vLLM) — set `fast_inference=False`:

```python
from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Qwen3.5-4B",
    fast_inference=False,
)
```

## Saving / export

Export guides: [[101-new-studio-export|Unsloth Studio]], [[086-basics-inference-and-deployment-saving-to-gguf|llama.cpp]], [[090-basics-inference-and-deployment-vllm-guide|vLLM]], [[083-basics-inference-and-deployment-llama-server-and-openai-endpoint|llama-server]], [[087-basics-inference-and-deployment-saving-to-ollama|Ollama]]

### Save to GGUF

```python
model.save_pretrained_gguf("directory", tokenizer, quantization_method = "q4_k_m")
model.save_pretrained_gguf("directory", tokenizer, quantization_method = "q8_0")
model.save_pretrained_gguf("directory", tokenizer, quantization_method = "f16")
```

Push to Hugging Face:

```python
model.push_to_hub_gguf("hf_username/directory", tokenizer, quantization_method = "q4_k_m")
model.push_to_hub_gguf("hf_username/directory", tokenizer, quantization_method = "q8_0")
```

> [!warning]
> If the exported model behaves worse in another runtime, the most common cause is **wrong chat template / EOS token** at inference time — use the same chat template you trained with.

### Save to vLLM

> [!warning]
> vLLM `0.16.0` does not support Qwen3.5. Wait for `0.170` or try Nightly.

16-bit merge:

```python
model.save_pretrained_merged("finetuned_model", tokenizer, save_method = "merged_16bit")
## OR to upload to HuggingFace:
model.push_to_hub_merged("hf/model", tokenizer, save_method = "merged_16bit", token = "")
```

LoRA adapters only:

```python
model.save_pretrained("finetuned_lora")
tokenizer.save_pretrained("finetuned_lora")
```

Or builtin function:

```python
model.save_pretrained_merged("finetuned_model", tokenizer, save_method = "lora")
## OR to upload to HuggingFace
model.push_to_hub_merged("hf/model", tokenizer, save_method = "lora", token = "")
```

More: [[091-basics-inference-and-deployment|Inference & Deployment]], [[086-basics-inference-and-deployment-saving-to-gguf|Saving to GGUF]], [[101-new-studio-export|Export]], [[090-basics-inference-and-deployment-vllm-guide|vLLM Guide]]

---

#fine-tuning #qwen3-5 #unsloth #lora #multilingual
