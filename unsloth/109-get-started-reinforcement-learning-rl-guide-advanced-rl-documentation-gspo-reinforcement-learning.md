---
title: GSPO Reinforcement Learning
url: https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/advanced-rl-documentation/gspo-reinforcement-learning.md
source: llms
fetched_at: 2026-04-27T18:13:15.944884412-03:00
rendered_js: false
word_count: 358
summary: This document introduces GSPO, a variant of GRPO developed by the Qwen team at Alibaba, which modifies how importance weights are applied in reinforcement learning. Instead of weighting individual tokens, GSPO assigns importance to the entire sequence likelihood for improved scaling.
tags:
    - gspo-reinforcement
    - grpo-variant
    - sequence-likelihood
    - rl-algorithm
    - unsloth-ai
    - importance-sampling
category: concept
optimized: true
optimized_at: 2026-04-27T21:15:00Z
---

# GSPO Reinforcement Learning

GSPO is a variant of [GRPO](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/..#from-rlhf-ppo-to-grpo-and-rlvr) by the Qwen team at Alibaba. Key insight: GRPO applies importance weights per-token, but advantages don't scale per-token. GSPO assigns importance on the **sequence likelihood** rather than individual token likelihoods.

GSPO notebooks: [gpt-oss-20b](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(20B\)-GRPO.ipynb), [Qwen2.5-VL](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen2_5_7B_VL_GRPO.ipynb). Source: [arxiv.org/abs/2507.18071](https://arxiv.org/abs/2507.18071).

## GRPO vs GSPO

### GRPO (Equation 1)

Advantages scale each row into token logprobs before summing. Each token gets the same scaling even though the advantage was computed for the entire sequence -- a mismatch.

### GSPO (Equation 2)

Logprob ratios for each sequence are **summed and exponentiated first**, then the resulting sequence ratios are row-wise multiplied by advantages. Importance is correctly applied at the sequence level.

## Enabling GSPO in Unsloth

Set `importance_sampling_level = "sequence"` in the GRPO config:

```python
training_args = GRPOConfig(
    output_dir = "vlm-grpo-unsloth",
    per_device_train_batch_size = 8,
    gradient_accumulation_steps = 4,
    learning_rate = 5e-6,
    adam_beta1 = 0.9,
    adam_beta2 = 0.99,
    weight_decay = 0.1,
    warmup_ratio = 0.1,
    lr_scheduler_type = "cosine",
    optim = "adamw_8bit",
    # beta = 0.00,
    epsilon = 3e-4,
    epsilon_high = 4e-4,
    num_generations = 8,
    max_prompt_length = 1024,
    max_completion_length = 1024,
    log_completions = False,
    max_grad_norm = 0.1,
    temperature = 0.9,
    # report_to = "none", # Set to "wandb" if you want to log to Weights & Biases
    num_train_epochs = 2, # For a quick test run, increase for full training
    report_to = "none"

    # GSPO is below:
    importance_sampling_level = "sequence",

    # Dr GRPO / GAPO etc
    loss_type = "dr_grpo",
)
```

#reinforcement-learning #gspo #grpo #unsloth
