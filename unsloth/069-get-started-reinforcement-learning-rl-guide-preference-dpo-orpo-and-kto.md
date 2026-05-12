---
title: Preference Optimization Training - DPO, ORPO & KTO
url: https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/preference-dpo-orpo-and-kto.md
source: llms
fetched_at: 2026-04-27T18:13:19.681793162-03:00
rendered_js: false
word_count: 168
summary: This document details various preference optimization techniques—DPO, ORPO, KTO, and PPO—and how they are implemented using Unsloth. It provides links to runnable Google Colab notebooks and shows a detailed Python code snippet for training a DPO model.
tags:
    - dpo-optimization
    - orpo-training
    - kto-reinforcement
    - unsloth-toolkit
    - preference-learning
    - rl-guide
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Preference Optimization Training - DPO, ORPO & KTO

DPO, ORPO, PPO, and KTO Reward Modelling all work with Unsloth.

## Notebooks

- [GRPO notebooks](https://unsloth.ai/docs/unsloth-notebooks#grpo-reasoning-rl-notebooks)
- [ORPO notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3_\(8B\)-ORPO.ipynb)
- [DPO Zephyr notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Zephyr_\(7B\)-DPO.ipynb)
- [KTO notebook](https://colab.research.google.com/drive/1MRgGtLWuZX4ypSfGguFgC-IblTvO2ivM?usp=sharing)
- [SimPO notebook](https://colab.research.google.com/drive/1Hs5oQDovOay4mFA6Y9lQhVJ8TnbFLFh2?usp=sharing)

Referenced in HF TRL official docs: [SFT](https://huggingface.co/docs/trl/main/en/sft_trainer#accelerate-fine-tuning-2x-using-unsloth), [DPO](https://huggingface.co/docs/trl/main/en/dpo_trainer#accelerate-dpo-fine-tuning-using-unsloth).

## DPO Code

```python
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0" # Optional set GPU device ID

from unsloth import FastLanguageModel, PatchDPOTrainer
from unsloth import is_bfloat16_supported
PatchDPOTrainer()
import torch
from trl import DPOTrainer, DPOConfig  # Changed from TrainingArguments

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/zephyr-sft-bnb-4bit",
    max_seq_length = max_seq_length,
    dtype = None,
    load_in_4bit = True,
)

# Do model patching and add fast LoRA weights
model = FastLanguageModel.get_peft_model(
    model,
    r = 64,
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 64,
    lora_dropout = 0, # Supports any, but = 0 is optimized
    bias = "none",    # Supports any, but = "none" is optimized
    # [NEW] "unsloth" uses 30% less VRAM, fits 2x larger batch sizes!
    use_gradient_checkpointing = "unsloth", # True or "unsloth" for very long context
    random_state = 3407,
    max_seq_length = max_seq_length,
)

dpo_trainer = DPOTrainer(
    model = model,
    ref_model = None,
    args = DPOConfig( # Use DPOConfig
        per_device_train_batch_size = 4,
        gradient_accumulation_steps = 8,
        warmup_ratio = 0.1,
        num_train_epochs = 3,
        fp16 = not is_bfloat16_supported(),
        bf16 = is_bfloat16_supported(),
        logging_steps = 1,
        optim = "adamw_8bit",
        seed = 42,
        output_dir = "outputs",
    ),
    beta = 0.1,
    train_dataset = YOUR_DATASET_HERE,
    # eval_dataset = YOUR_DATASET_HERE,
    tokenizer = tokenizer,
    max_length = 1024,
    max_prompt_length = 512,
)

dpo_trainer.train()
```

#dpo #orpo #kto #preference-learning #unsloth #rl
