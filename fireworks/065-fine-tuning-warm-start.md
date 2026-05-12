---
title: Fine Tuning Warm Start
url: https://docs.fireworks.ai/fine-tuning/warm-start
source: sitemap
fetched_at: 2026-04-27T20:18:34.512650003-03:00
rendered_js: false
word_count: 96
summary: This document explains how Fireworks supports training using the warm start feature, allowing users to continue Reinforcement Fine Tuning (RFT) from already trained models rather than beginning training from scratch.
tags:
    - fireworks-training
    - rft
    - warm-start
    - fine-tuning
    - sft-to-rft
    - model-workflow
category: tutorial
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Fireworks supports RFT training on already-fine-tuned models. Upload models to Fireworks and use the warm start option to continue training (e.g. from an SFT LoRA) with RFT, rather than starting from scratch with a base model.

## When to use warm start

Use the `--warm-start-from` flag when you want to:

- Start RFT from an SFT model trained with Fireworks
- Continue training from an existing fine-tuned LoRA adapter uploaded to Fireworks

## Basic usage

```bash
eval-protocol create rft \
  --warm-start-from accounts/your-account/models/<SFT_MODEL_ID> \
  --output-model <RFT_MODEL_ID>
```

## SFT to RFT workflow

> [!tip]
> For an end-to-end walkthrough, see [[002-fine-tuning-training-api-introduction|Fine Tuning Training Api Introduction]].

#warm-start #fine-tuning #rft
