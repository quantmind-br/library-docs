---
title: Multi-GPU Fine-tuning with Unsloth
url: https://unsloth.ai/docs/basics/multi-gpu-training-with-unsloth.md
source: llms
fetched_at: 2026-04-27T18:14:58.580008011-03:00
rendered_js: false
word_count: 313
summary: This document explains how to leverage multi-GPU setups for fine-tuning with Unsloth, detailing methods like DDP and FSDP that can be used immediately.
tags:
    - multi-gpu
    - unsloth
    - fine-tuning
    - ddp
    - accelerate
    - fsdp
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Multi-GPU Fine-tuning with Unsloth

Unsloth supports multi-GPU setups through Accelerate and DeepSpeed, enabling **FSDP** and **DDP** parallelism. See the [[092-basics-multi-gpu-training-with-unsloth-ddp|DDP multi-GPU guide]] for detailed instructions.

## DDP Quick Start

1. Create your training script as `train.py` (e.g. from [Unsloth training scripts](https://github.com/unslothai/notebooks/tree/main/python_scripts))
2. Run via Accelerate or torchrun:

   ```bash
   accelerate launch train.py
   # or
   torchrun --nproc_per_node N_GPUS train.py
   ```

   Replace `N_GPUS` with the number of GPUs.

## Pipeline / Model Splitting

If a single GPU lacks VRAM to load a large model (e.g. Llama 70B), Unsloth splits the model across GPUs using `device_map = "balanced"`:

```python
from unsloth import FastLanguageModel
model, tokenizer = FastLanguageModel.from_pretrained(
    "unsloth/Llama-3.3-70B-Instruct",
    load_in_4bit = True,
    device_map = "balanced",
)
```

## Examples

- [[038-models-tutorials-magistral-how-to-run-and-fine-tune|Magistral-2509 Kaggle notebook]] — uses multi-GPU to fit the 24B parameter model
- [[092-basics-multi-gpu-training-with-unsloth-ddp|DDP guide]] — full DDP setup walkthrough

## Status

Official simplified multi-GPU support is in progress. Track progress at [GitHub issue #2435](https://github.com/unslothai/unsloth/issues/2435).

#multi-gpu #fine-tuning #ddp #fsdp #accelerate
