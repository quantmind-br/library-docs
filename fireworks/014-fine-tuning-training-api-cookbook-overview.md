---
title: The Cookbook
url: https://docs.fireworks.ai/fine-tuning/training-api/cookbook/overview
source: sitemap
fetched_at: 2026-04-27T20:15:42.787558217-03:00
rendered_js: false
word_count: 282
summary: This document introduces the Fireworks Cookbook, a collection of training recipes built on top of the Training API that allows users to quickly implement complex, config-driven training loops. It details installation, available recipe types (like RL, SFT, DPO), and provides quick code examples for usage.
tags:
    - cookbook
    - training-recipes
    - fine-tuning
    - api-utilities
    - rl-optimization
    - sft
category: guide
optimized: true
optimized_at: 2026-04-27T23:27:00Z
---
The [Fireworks Cookbook](https://github.com/fw-ai/cookbook/tree/main/training) is a collection of training recipes and utilities built on top of the [[002-fine-tuning-training-api-introduction]]. It provides config-driven training loops that handle trainer provisioning, data loading, tokenization, gradient accumulation, checkpointing, and cleanup automatically.

> [!note]
> The cookbook is **optional** — everything it does can be done with the API directly. Use the cookbook when you want a working training loop quickly; use the API when you need full control.

## Installation

```bash
git clone https://github.com/fw-ai/cookbook.git
cd cookbook/training && pip install -e .
export FIREWORKS_API_KEY="your-api-key"
```

## Available recipes

| Recipe | Module | Use case |
|--------|--------|----------|
| **RL** | `training.recipes.rl_loop` | On-policy and off-policy RL with GRPO, importance sampling, DAPO, DRO, GSPO, CISPO |
| **IGPO** | `training.recipes.igpo_loop` | Information Gain-based Policy Optimization — turn-level IG rewards for multi-turn agents (extends GRPO) |
| **DPO** | `training.recipes.dpo_loop` | Direct preference optimization from chosen/rejected pairs |
| **SFT** | `training.recipes.sft_loop` | Supervised fine-tuning with cross-entropy loss |
| **ORPO** | `training.recipes.orpo_loop` | Odds ratio preference optimization |

All recipes follow the same pattern: import `Config` and `main`, set your config, and call `main(cfg)`. Launch examples use `infra=InfraConfig(training_shape_id=...)` — that training shape ID is usually the only shape-specific input needed. See [[061-fine-tuning-training-api-training-shapes]] for field-level details.

## Quick example: SFT

```python
from training.recipes.sft_loop import Config, main
from training.utils import InfraConfig

cfg = Config(
    log_path="./sft_quickstart",
    base_model="accounts/fireworks/models/qwen3-8b",
    dataset="/path/to/training_data.jsonl",
    tokenizer_model="Qwen/Qwen3-8B",
    max_seq_len=4096,
    epochs=1,
    batch_size=4,
    infra=InfraConfig(
        training_shape_id="accounts/fireworks/trainingShapes/qwen3-8b-128k-h200",
    ),
)

main(cfg)
```

## Quick example: GRPO

```python
from training.recipes.rl_loop import Config, main
from training.utils import DeployConfig, InfraConfig, WeightSyncConfig

cfg = Config(
    log_path="./grpo_quickstart",
    base_model="accounts/fireworks/models/qwen3-8b",
    dataset="/path/to/prompts.jsonl",
    max_rows=100,
    infra=InfraConfig(
        training_shape_id="accounts/fireworks/trainingShapes/qwen3-8b-128k-h200",
    ),
    deployment=DeployConfig(
        deployment_id="grpo-serving",
        tokenizer_model="Qwen/Qwen3-8B",
    ),
    weight_sync=WeightSyncConfig(weight_sync_interval=1),
)

main(cfg)
```

## W&B logging

All cookbook recipes accept a `WandBConfig` to stream metrics to [Weights & Biases](https://wandb.ai):

```python
from training.utils import WandBConfig

cfg = Config(
    # ... same config as above ...
    wandb=WandBConfig(
        entity="my-team",
        project="grpo-experiment",
        run_name="qwen3-8b-sft-v1",  # optional, auto-generated if omitted
    ),
)

main(cfg)
```

## Vision-language model support

All recipes support VLM fine-tuning. Use a VLM training shape and tokenizer, and provide multimodal datasets with `image_url` content. See [[062-fine-tuning-training-api-vision-inputs]] for dataset format and examples.

## Next steps

- [[051-fine-tuning-training-api-cookbook-rl]] — full GRPO walkthrough with reward functions
- [[050-fine-tuning-training-api-cookbook-dpo]] — preference optimization with pairwise data
- [[052-fine-tuning-training-api-cookbook-sft]] — supervised fine-tuning
- [[062-fine-tuning-training-api-vision-inputs]] — fine-tune VLMs with image and text data