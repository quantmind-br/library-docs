---
title: Fine Tuning Overview - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/finetuning-intro
source: sitemap
fetched_at: 2026-04-27T20:12:46.313603994-03:00
rendered_js: false
word_count: 453
summary: 'This document explains the two primary methods for fine-tuning models using Fireworks: Managed Fine-Tuning and the Training API, detailing when to use each approach based on specific needs like loss function customization or control level.'
tags:
    - fine-tuning
    - managed-training
    - training-api
    - sft
    - dpo
    - lora
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Fireworks fine-tunes models to improve quality and performance for your product use cases without building or maintaining training infrastructure.

## Two approaches

| Feature | Managed Fine-Tuning | Training API |
|---------|---------------------|--------------|
| **Control** | Configuration-driven | Full Python loop control |
| **Objectives** | Built-in SFT, DPO, RFT | Any custom loss function |
| **Tuning method** | LoRA | Full-parameter or LoRA |
| **Inference during training** | Not available | Hotload + sample mid-training |
| **Interface** | UI, firectl, REST API | Python API |
| **Best for** | Production fine-tuning | Research, custom RL, hybrid losses |

## SFT vs. RFT

**Supervised Fine-Tuning (SFT)** — provide a dataset with labeled "good" outputs. Works well when:

- You have ~1000+ high-quality labeled examples
- The dataset covers most input scenarios
- Tasks are straightforward (classification, content extraction)

SFT may struggle when your dataset is small, lacks ground-truth outputs, or the task requires multi-step reasoning.

**Reinforcement Fine-Tuning (RFT)** — provide a grader function to score model outputs. The model is iteratively trained to maximize the score.

## When to use the Training API

Switch from managed fine-tuning to [[002-fine-tuning-training-api-introduction|the Training API]] when you need:

- **Custom loss functions** — hybrid GRPO + DPO, custom reward shaping, or non-standard objectives
- **Full-parameter tuning** — update all model weights instead of a LoRA adapter
- **Inference-in-the-loop evaluation** — hotload checkpoints onto a serving deployment and sample mid-training
- **Per-step control** — custom gradient accumulation, dynamic learning rate schedules, or algorithm research

### Capability comparison

| Capability | Managed RFT | Training API |
|------------|-------------|--------------|
| Launch training | CLI or UI | Python script |
| Loss functions | Built-in (`grpo`, `dapo`, `gspo-token`) | Any custom loss via `forward_backward_custom` |
| Training loop | Fully managed | You write the loop |
| Per-step diagnostics | Dashboard (reward, loss, rollouts) | Full Python access to all metrics |
| Zero-variance filtering | Automatic | You implement |
| Checkpoint management | Automatic | You control via `save_weights_for_sampler_ext` |

### Migrating to Training API

The Training API lets you implement your own training loop while keeping the same GPU infrastructure — use it for custom loss functions, richer diagnostics, or algorithm experimentation.

### MoE models and Routing Replay

For Mixture-of-Experts (MoE) models like Kimi K2 (384 experts), **Routing Replay** stabilizes training by caching expert routing assignments from the reference policy's forward pass and replaying them during training. This ensures the same experts process the same tokens in both passes, reducing gradient noise from routing changes.

Routing Replay is available in the Training API via the `loss_fn_inputs` mechanism — pass routing matrices from the reference forward pass into the training datum.

#fine-tuning #managed-training #training-api
