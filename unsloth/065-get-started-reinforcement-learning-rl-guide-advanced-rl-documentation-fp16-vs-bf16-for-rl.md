---
title: FP16 vs BF16 for RL
url: https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/advanced-rl-documentation/fp16-vs-bf16-for-rl.md
source: llms
fetched_at: 2026-04-27T18:13:18.089507393-03:00
rendered_js: false
word_count: 316
summary: This document compares Float16 (FP16) and Bfloat16 (BF16) precision for reinforcement learning tasks, detailing why FP16 is often more stable, and provides instructions on how to implement float16 within Unsloth RL setups.
tags:
    - fp16
    - bf16
    - reinforcement-learning
    - stability
    - unsloth-rl
    - dtype
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# FP16 vs BF16 for RL

## Float16 vs Bfloat16

Paper "[Defeating the Training-Inference Mismatch via FP16](https://arxiv.org/pdf/2510.26788)" shows float16 is dramatically better than bfloat16 for RL. Degradation worsens with longer generation length. Unsloth investigation [confirms](https://x.com/danielhanchen/status/1985557028295827482) float16 is more stable with much smaller gradient norms than bfloat16.

Key findings:
- FP16 reduces training-inference mismatch vs. BF16
- Longer generations amplify BF16 instability
- Newer/more expensive GPUs show less KL divergence between inference and training

## A100 Cascade Attention Bug

Older vLLM versions (before 0.11.0) had broken attention mechanisms for A100 and similar GPUs ([ref1](https://x.com/RichardYRLi/status/1984858850143715759), [ref2](https://yingru.notion.site/When-Speed-Kills-Stability-Demystifying-RL-Collapse-from-the-Training-Inference-Mismatch-271211a558b7808d8b12d403fd15edda)). Update vLLM. Unsloth disables cascade attention by default during RL if an older vLLM version is detected.

## Using float16 in Unsloth RL

Set `dtype = torch.float16` — Unsloth handles the rest.

```python
from unsloth import FastLanguageModel
import torch
max_seq_length = 2048 # Can increase for longer reasoning traces
lora_rank = 32 # Larger rank = smarter, but slower

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Qwen3-4B-Base",
    max_seq_length = max_seq_length,
    load_in_4bit = False, # False for LoRA 16bit
    fast_inference = True, # Enable vLLM fast inference
    max_lora_rank = lora_rank,
    gpu_memory_utilization = 0.9, # Reduce if out of memory

    dtype = torch.float16, # Use torch.float16, torch.bfloat16
)
```

#fp16 #bf16 #reinforcement-learning #unsloth #rl
