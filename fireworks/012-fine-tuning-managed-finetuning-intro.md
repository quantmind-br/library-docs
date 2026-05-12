---
title: Managed Fine-Tuning Overview - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/managed-finetuning-intro
source: sitemap
fetched_at: 2026-04-27T20:15:50.037955302-03:00
rendered_js: false
word_count: 158
summary: This document explains the capabilities of Fireworks AI for data handling and configuration, detailing methods like Free Reinforcement Fine-Tuning and efficient LoRA-based tuning.
tags:
    - reinforcement-fine-tuning
    - lora-tuning
    - model-training
    - fireworks-ai
    - llm-tuning
    - data-configuration
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Give Fireworks your data and configuration. The platform handles scheduling, training, checkpointing, and model output.

## Free Reinforcement Fine-Tuning

When creating a Reinforcement Fine-Tuning job in the UI, use the "Free tuning" filter in the model selection area.

> [!info]
> For SFT and DPO pricing, see the [pricing page](https://fireworks.ai/pricing).

## Supported models

Fine-tuning is supported for most major open source model families including DeepSeek, Qwen, Kimi, and Llama — up to large state-of-the-art models like Kimi K2 0905 and DeepSeek V3.1.

View all fine-tunable models:

- [Model Library for text models](https://app.fireworks.ai/models?filter=LLM&tunable=true)
- [Vision models](https://app.fireworks.ai/models?filter=vision&tunable=true)

## LoRA-based tuning

Managed fine-tuning uses [**Low-Rank Adaptation (LoRA)**](https://arxiv.org/abs/2106.09685) — a small adapter that modifies the base model's behavior without retraining all weights. This approach is:

- **Faster and cheaper** — train models in hours, not days
- **Easy to deploy** — deploy LoRA addons instantly on Fireworks
- **Flexible** — run [[038-fine-tuning-deploying-loras#multi-lora-deployment|multiple LoRAs]] on a single base model deployment

#lora-tuning #reinforcement-fine-tuning #model-training
