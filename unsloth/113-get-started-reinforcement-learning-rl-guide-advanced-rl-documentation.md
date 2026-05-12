---
title: Advanced Reinforcement Learning Documentation
url: https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/advanced-rl-documentation.md
source: llms
fetched_at: 2026-04-27T18:13:14.416791739-03:00
rendered_js: false
word_count: 1280
summary: This document provides detailed documentation on various advanced hyperparameters for Reinforcement Learning (RL) processes, specifically focusing on GRPO implementation with Unsloth. It covers settings related to training algorithms, generation sampling, and batch/throughput management.
tags:
    - reinforcement-learning
    - grpo
    - training-parameters
    - generation-settings
    - batch-size
    - unsloth
category: reference
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Advanced Reinforcement Learning Documentation

GRPO with Unsloth: training, generation, and batch/throughput parameters.

## Training Parameters

- **`beta`** *(float, default 0.0)* — KL coefficient. `0.0` = no reference model (lower memory, faster). Higher values constrain policy closer to ref.
- **`num_iterations`** *(int, default 1)* — PPO epochs per batch (μ). Replays data within each grad accum step; e.g., `2` = two forward passes per accum step.
- **`epsilon`** *(float, default 0.2)* — Clipping for token-level log-prob ratios (typical ratio range ~[-1.2, 1.2]).
- **`delta`** *(float, optional)* — Enables upper clipping for **two-sided GRPO**. `None` = standard GRPO. Recommended `> 1 + ε` (per INTELLECT-2).
- **`epsilon_high`** *(float, optional)* — Upper-bound epsilon; defaults to `epsilon` if unset. DAPO recommends **0.28**.
- **`importance_sampling_level`** *(str, default "token")* — `"token"`: raw per-token ratios. `"sequence"`: avg per-token to single ratio (GSPO shows more stable training for seq-level rewards).
- **`reward_weights`** *(list[float], optional)* — One weight per reward. `None` = all 1.0.
- **`scale_rewards`** *(str|bool, default "group")* — `True`/`"group"`: scale by std within group. `"batch"`: scale by std across entire batch. `False`/`"none"`: no scaling (Dr. GRPO recommends to avoid difficulty bias).
- **`loss_type`** *(str, default "dapo")*:
  - `"grpo"` — normalizes over seq length (length bias; not recommended).
  - `"dr_grpo"` — normalizes by global constant ~`max_completion_length` (removes length bias).
  - `"dapo"` — normalizes by active tokens in global accumulated batch (default; removes length bias).
  - `"bnpo"` — normalizes by active tokens in local batch only (equals GRPO when `per_device_train_batch_size == 1`).
- **`mask_truncated_completions`** *(bool, default False)* — Excludes truncated completions from loss (DAPO). **Warning**: KL issues — zeroing all `completion_mask` causes `n_mask_per_reward = 0` and NaN KL. Recommended to disable.

  ```python
  # If mask_truncated_completions is enabled, zero out truncated completions in completion_mask
  if self.mask_truncated_completions:
      truncated_completions = ~is_eos.any(dim=1)
      completion_mask = completion_mask * (~truncated_completions).unsqueeze(1).int()
  ```

  [Source](https://github.com/unslothai/unsloth-zoo/blob/e705f7cb50aa3470a0b6e36052c61b7486a39133/unsloth_zoo/rl_replacements.py#L184)

- **`vllm_importance_sampling_correction`** *(bool, default True)* — Applies Truncated Importance Sampling (TIS) to correct off-policy effects. Auto-set True if using vLLM/fast_inference; otherwise False.
- **`vllm_importance_sampling_cap`** *(float, default 2.0)* — Truncation cap C for TIS; upper bound on importance sampling ratio.
- **`dtype`** — fp16 vs bf16: see [[065-get-started-reinforcement-learning-rl-guide-advanced-rl-documentation-fp16-vs-bf16-for-rl|FP16 vs BF16 for RL]].

### RL on unsupported models

Set `fast_inference=False` for models not supported by vLLM (e.g., [[020-models-qwen3.5-fine-tune|Qwen3.5]]):

```python
from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Qwen3.5-4B",
    fast_inference=False,
)
```

## Generation Parameters

- **`temperature`** *(float, default 1.0)* — Sampling temperature. Use ~1.0 for diversity in GRPO.
- **`top_p`** *(float, default 1.0)* — Cumulative prob of top tokens. (0, 1].
- **`top_k`** *(int, optional)* — Top-k filtering. `None` = disabled.
- **`min_p`** *(float, optional)* — Min token prob scaled by most likely. Range [0.0, 1.0]; typical 0.01-0.2.
- **`repetition_penalty`** *(float, default 1.0)* — >1.0 encourages new tokens; <1.0 encourages repetition.
- **`steps_per_generation`** *(int, optional)* — Steps per generation. Defaults to `gradient_accumulation_steps`. Mutually exclusive with `generation_batch_size`.

> [!info] Prefer editing `per_device_train_batch_size` and gradient accumulation for batch sizes rather than `steps_per_generation`.

## Batch & Throughput Parameters

### Key parameters

- **`train_batch_size`** — Samples per process per step. If < `num_generations`, defaults to `num_generations`.
- **`steps_per_generation`** — Microbatches for one generation's loss calc (forward only). New data batch every N steps.
- **`num_processes`** — Distributed training processes (GPUs/workers).
- **`gradient_accumulation_steps`** — Microbatches before backprop/optimizer update.

### Formulas

```
effective_batch_size = steps_per_generation * num_processes * train_batch_size
optimizer_steps_per_generation = steps_per_generation / gradient_accumulation_steps
unique_prompts = effective_batch_size / num_generations   # must be > 2
```

### GRPO Batch Examples

#### Example 1

```
num_gpus = 1
per_device_train_batch_size = 3
gradient_accumulation_steps = 2
steps_per_generation = 4

effective_batch_size = 4 * 3 * 1 = 12
num_generations = 3
```

**Generation cycle A**

| Step | Batch    | Notes                                  |
| ---: | -------- | -------------------------------------- |
|    0 | [0,0,0]  |                                        |
|    1 | [1,1,1]  | optimizer update (accum = 2 reached)   |
|    2 | [2,2,2]  |                                        |
|    3 | [3,3,3]  | optimizer update                       |

**Generation cycle B**

| Step | Batch    | Notes                                  |
| ---: | -------- | -------------------------------------- |
|    0 | [4,4,4]  |                                        |
|    1 | [5,5,5]  | optimizer update (accum = 2 reached)   |
|    2 | [6,6,6]  |                                        |
|    3 | [7,7,7]  | optimizer update                       |

#### Example 2

```
num_gpus = 1
per_device_train_batch_size = 3
steps_per_generation = gradient_accumulation_steps = 4

effective_batch_size = 4 * 3 * 1 = 12
num_generations = 3
```

**Generation cycle A**

| Step | Batch    | Notes                                |
| ---: | -------- | ------------------------------------ |
|    0 | [0,0,0]  |                                      |
|    1 | [1,1,1]  |                                      |
|    2 | [2,2,2]  |                                      |
|    3 | [3,3,3]  | optimizer update (accum = 4 reached) |

**Generation cycle B**

| Step | Batch    | Notes                                |
| ---: | -------- | ------------------------------------ |
|    0 | [4,4,4]  |                                      |
|    1 | [5,5,5]  |                                      |
|    2 | [6,6,6]  |                                      |
|    3 | [7,7,7]  | optimizer update (accum = 4 reached) |

#### Example 3

```
num_gpus = 1
per_device_train_batch_size = 3
steps_per_generation = gradient_accumulation_steps = 4

effective_batch_size = 4 * 3 * 1 = 12
num_generations = 4
unique_prompts = effective_batch_size / num_generations = 3
```

**Generation cycle A**

| Step | Batch    | Notes                                |
| ---: | -------- | ------------------------------------ |
|    0 | [0,0,0]  |                                      |
|    1 | [0,1,1]  |                                      |
|    2 | [1,1,3]  |                                      |
|    3 | [3,3,3]  | optimizer update (accum = 4 reached) |

**Generation cycle B**

| Step | Batch    | Notes                                |
| ---: | -------- | ------------------------------------ |
|    0 | [4,4,4]  |                                      |
|    1 | [4,5,5]  |                                      |
|    2 | [5,5,6]  |                                      |
|    3 | [6,6,6]  | optimizer update (accum = 4 reached) |

#### Example 4

```
num_gpus = 1
per_device_train_batch_size = 6
steps_per_generation = gradient_accumulation_steps = 2

effective_batch_size = 2 * 6 * 1 = 12
num_generations = 3
unique_prompts = 4
```

**Generation cycle A**

| Step | Batch           | Notes                                |
| ---: | --------------- | ------------------------------------ |
|    0 | [0,0,0, 1,1,1]  |                                      |
|    1 | [2,2,2, 3,3,3]  | optimizer update (accum = 2 reached) |

**Generation cycle B**

| Step | Batch           | Notes                                |
| ---: | --------------- | ------------------------------------ |
|    0 | [4,4,4, 5,5,5]  |                                      |
|    1 | [6,6,6, 7,7,7]  | optimizer update (accum = 2 reached) |

#reinforcement-learning #grpo #training-parameters #batch-size #unsloth
