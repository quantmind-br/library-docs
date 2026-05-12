---
title: LoRA fine-tuning Hyperparameters Guide
url: https://unsloth.ai/docs/get-started/fine-tuning-llms-guide/lora-hyperparameters-guide.md
source: llms
fetched_at: 2026-04-27T18:13:05.102674627-03:00
rendered_js: false
word_count: 2933
summary: This document serves as a comprehensive guide to the hyperparameters used when fine-tuning Large Language Models (LLMs) using LoRA. It details how various settings, such as learning rate and epochs, affect model accuracy and stability, offering best practices for selecting optimal values.
tags:
    - lora-fine-tuning
    - hyperparameters
    - llm-training
    - learning-rate
    - overfitting
    - qlora
category: guide
optimized: true
optimized_at: 2026-04-27T21:22:00Z
---

# LoRA fine-tuning Hyperparameters Guide

LoRA hyperparameters control how Low-Rank Adaptation [[064-get-started-fine-tuning-llms-guide|fine-tunes]] LLMs. LoRA can match full fine-tuning performance while using 4x less VRAM. The goal: increase accuracy while counteracting [overfitting/underfitting](#avoiding-overfitting--underfitting).

**What is LoRA:** Instead of updating all model weights (e.g., 70B parameters), thin matrices A and B are added to each weight and only those (~1%) are optimized.

## Key Fine-tuning Hyperparameters

### Learning Rate

How much weights adjust per training step.

- **Higher** -- faster convergence but can cause instability or miss optimal minimum
- **Lower** -- more stable/precise but may need more epochs; can also cause overfitting
- **Typical range:** `2e-4` to `5e-6`
  - Normal LoRA/QLoRA: **`2e-4`** starting point
  - Reinforcement Learning (DPO, GRPO): **`5e-6`**
  - Full Fine-tuning: lower rates

### Epochs

Times the model sees the full dataset.

- **More** -- better learning but risk of memorization/overfitting
- **Fewer** -- less training time, prevents overfitting, but may undertrain
- **Recommended:** 1-3. Beyond 3 offers diminishing returns on instruction datasets.

### LoRA vs QLoRA

| Type | Precision | Speed | Accuracy | VRAM |
|------|-----------|-------|----------|------|
| LoRA | 16-bit | Slightly faster | Slightly more accurate | 4x more |
| QLoRA | 4-bit | Slightly slower | Marginally less accurate | 4x less |

> [!tip] 70B LLaMA fits in <48GB VRAM with QLoRA in Unsloth -- [more details](https://unsloth.ai/blog/llama3-3)

### Hyperparameters & Recommendations

| Hyperparameter | Function | Recommended Settings |
|---|---|---|
| **LoRA Rank** (`r`) | Controls trainable parameter count in LoRA adapter matrices. Higher rank = more capacity + memory. | 8, 16, 32, 64, 128 -- choose **16 or 32** |
| **LoRA Alpha** (`lora_alpha`) | Scales fine-tune adjustment strength relative to `r`. | `r` (standard) or `r * 2` -- [more details](#lora-alpha-and-rank-relationship) |
| **LoRA Dropout** | Regularization: randomly zeros LoRA activations during training. Not that useful, defaults to 0. | 0 (default) to 0.1 |
| **Weight Decay** | Regularization: penalizes large weights. Don't use too large. | 0.01 (recommended) to 0.1 |
| **Warmup Steps** | Gradually increases learning rate at start. | 5-10% of total steps |
| **Scheduler Type** | Adjusts learning rate dynamically. | `linear` or `cosine` |
| **Seed** (`random_state`) | Fixed number for reproducibility. | Any integer (e.g., `42`, `3407`) |
| **Target Modules** | Which model parts get LoRA adapters -- attention, MLP, or both. Attention: `q_proj, k_proj, v_proj, o_proj`. MLP: `gate_proj, up_proj, down_proj`. | Target all major linear layers: `q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj` |

## Gradient Accumulation and Batch Size

### Effective Batch Size

**Effective Batch Size** = `batch_size * gradient_accumulation_steps`

- Larger = smoother, more stable training
- Smaller = more variance

| Parameter | Description | Recommended |
|---|---|---|
| **Batch Size** (`batch_size`) | Samples per forward/backward pass on one GPU. Primary VRAM driver. | 2 |
| **Gradient Accumulation** (`gradient_accumulation_steps`) | Micro-batches before weight update. Primary training time driver. Simulates larger `batch_size` without extra VRAM. | 8 |
| **Effective Batch Size** | True batch per gradient update. Directly influences stability and quality. | 4 to 16. **Recommended: 16** (2 x 8) |

### VRAM & Performance Trade-off

All configurations yielding the same effective batch size are equivalent for weight updates, but differ in VRAM:

| batch_size | gradient_accumulation_steps | VRAM Usage | Training Speed |
|---|---|---|---|
| 32 | 1 | Highest | Fastest |
| 2 | 16 | Lowest | Slightly slower |

**Prefer smaller `batch_size` + higher `gradient_accumulation_steps`** to avoid OOM errors.

### Unsloth Gradient Accumulation Fix

<mark style="color:green;">**Batch size and gradient accumulation are now fully equivalent in Unsloth**</mark> due to bug fixes. Previously, configurations like `b1/g16`, `b2/g8`, `b4/g4` with the same effective batch size produced different loss curves. Now they align correctly.

[Read the blog post](https://unsloth.ai/blog/gradient) for more details.

## LoRA Hyperparameters in Unsloth

Standard configuration -- Unsloth provides optimized defaults, but understanding these enables manual tuning.

1. ```python
   r = 16, # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128
   ```
   Rank (`r`). Larger = more memory, slower, potentially more accuracy on complex tasks. Too large causes overfitting. Suggested: 8-16 (fast), up to 128.

2. ```python
   target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                     "gate_proj", "up_proj", "down_proj",],
   ```
   <mark style="background-color:blue;">**LoRA should be applied to all major linear layers**</mark>. Removing modules saves minimal memory and harms quality. [Research details below](#lora-target-modules-and-qlora-vs-lora).

3. ```python
   lora_alpha = 16,
   ```
   Scaling factor for fine-tune adjustments. Set equal to `r` (baseline) or `r * 2` (more aggressive learning). [More details](#lora-alpha-and-rank-relationship).

4. ```python
   lora_dropout = 0, # Supports any, but = 0 is optimized
   ```
   Regularization via random zeroing. [Recent research](https://arxiv.org/abs/2410.09692) suggests it's unreliable for short fine-tuning runs. Unsloth optimizes when `lora_dropout = 0` (slightly faster). Use non-zero if you suspect overfitting.

5. ```python
   bias = "none",    # Supports any, but = "none" is optimized
   ```
   Leave as `"none"` -- avoids training bias terms with little practical gain.

6. ```python
   use_gradient_checkpointing = "unsloth", # True or "unsloth" for very long context
   ```
   Options: `True`, `False`, `"unsloth"`. Recommend `"unsloth"` -- reduces memory by extra 30% and supports very long context. See [long context blog](https://unsloth.ai/blog/long-context).

7. ```python
   random_state = 3407,
   ```
   Seed for deterministic, reproducible runs.

8. ```python
   use_rslora = False,  # We support rank stabilized LoRA
   ```
   [Rank-Stabilized LoRA](https://arxiv.org/abs/2312.03732). When `True`, effective scaling becomes `lora_alpha / sqrt(r)` instead of `lora_alpha / r`. Can improve stability at higher ranks. [More details](#lora-alpha-and-rank-relationship).

9. ```python
   loftq_config = None, # And LoftQ
   ```
   [LoftQ](https://arxiv.org/abs/2310.08659) initializes LoRA matrices with top `r` singular vectors from pretrained weights. Can improve accuracy but may cause memory spike at training start.

### Verifying LoRA Weight Updates

Avoid `np.allclose()` -- it misses subtle but meaningful changes (especially in LoRA A, initialized with small Gaussian values). Recommended methods:

- Checksum/hash comparisons (e.g., MD5)
- Sum of absolute differences between tensors
- Tensor statistics inspection (mean, variance)
- `np.array_equal()` if exact equality expected

Thanks to [contributors](https://github.com/unslothai/unsloth/issues/3035).

## LoRA Alpha and Rank Relationship

> [!tip] Best practice: `lora_alpha = 2 * lora_rank` or `lora_alpha = lora_rank`

**Standard LoRA formula:**

```
W_hat = W + (alpha / rank) * A * B
```

This means **alpha/rank should be at least 1**.

**rsLoRA formula:**

```
W_hat_rslora = W + (alpha / sqrt(rank)) * A * B
```

Per the [rsLoRA paper](https://arxiv.org/abs/2312.03732), scaling by sqrt(rank) is theoretically optimal (lower perplexity). Enable with `use_rslora = True`.

**Recommendation:** Set alpha equal to rank, or at least 2x rank (alpha/rank = 1 or 2).

## LoRA Target Modules and QLoRA vs LoRA

> [!tip]
> - Target both MLP and attention: `target_modules = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]`
> - **QLoRA** = 4-bit, >75% VRAM reduction
> - **LoRA** (16-bit) = slightly more accurate and faster

Per the [QLoRA paper](https://arxiv.org/pdf/2305.14314), apply LoRA to both attention and MLP layers.

RougeL scores by configuration (higher is better):

1. **QLoRA-All** -- LoRA on all FFN/MLP + Attention layers. Best overall.
2. **QLoRA-FFN** -- LoRA only on FFN (`gate_proj`, `up_proj`, `down_proj`)
3. **QLoRA-Attention** -- LoRA only on Attention (`q_proj`, `k_proj`, `v_proj`, `o_proj`)

## Training on Completions Only (Masking Inputs)

The [QLoRA paper](https://arxiv.org/pdf/2305.14314) shows masking inputs and training only on completions (assistant messages) increases accuracy by ~1%, especially for multi-turn conversational finetunes.

| Approach | Training Content |
|---|---|
| Standard | USER + ASSISTANT tokens |
| Completions only | ASSISTANT tokens only (USER masked) |

**For Llama 3/3.1/3.2/3.3/4:**

```python
from unsloth.chat_templates import train_on_responses_only
trainer = train_on_responses_only(
    trainer,
    instruction_part = "<|start_header_id|>user<|end_header_id|>\n\n",
    response_part = "<|start_header_id|>assistant<|end_header_id|>\n\n",
)
```

**For Gemma 2/3/3n:**

```python
from unsloth.chat_templates import train_on_responses_only
trainer = train_on_responses_only(
    trainer,
    instruction_part = "<start_of_turn>user\n",
    response_part = "<start_of_turn>model\n",
)
```

See [conversational notebooks](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.2_\(1B_and_3B\)-Conversational.ipynb) for full examples.

### Training on Completions for Vision Models (VLMs)

Use extra arguments in `UnslothVisionDataCollator`:

```python
class UnslothVisionDataCollator:
def __init__(
    self,
    ...
    train_on_responses_only = False, # EQUIVALENT to train_on_responses_only for LLMs
    instruction_part = None, # EQUIVALENT to train_on_responses_only(instruction_part = ...)
    response_part    = None, # EQUIVALENT to train_on_responses_only(response_part = ...)
    force_match      = True, # Match newlines as well!
)
```

Example for Llama 3.2 Vision:

```python
UnslothVisionDataCollator(
    model, tokenizer,
    ...
    train_on_responses_only = True,
    instruction_part = "<|start_header_id|>user<|end_header_id|>\n\n",
    response_part = "<|start_header_id|>assistant<|end_header_id|>\n\n",
    ...
)
```

## Avoiding Overfitting & Underfitting

### Overfitting (Poor Generalization)

Model memorizes training data including noise, fails on unseen data.

> [!tip] If training loss drops below 0.2, likely overfitting. Fix: multiply each LoRA alpha by 0.5. Equivalent to averaging base model + finetuned weights / 2.

**Solutions:**

- Adjust learning rate (high LR often causes overfitting in short runs)
- Reduce epochs (1-3 max)
- Increase `weight_decay` (0.01 or 0.1)
- Increase `lora_dropout` (e.g., 0.1)
- Increase batch size or gradient accumulation steps
- Expand dataset with higher-quality open-source data
- Enable evaluation early stopping (stop when eval loss increases)
- LoRA alpha scaling (reduce alpha post-training)
- Weight averaging (base + finetuned) / 2

### Underfitting (Too Generic)

Model fails to capture training data patterns.

**Solutions:**

- Increase learning rate (for short runs); decrease for long runs
- Increase training epochs (monitor validation loss)
- Increase LoRA Rank (`r`) and alpha (rank >= alpha; rank between 4-64)
- Use more domain-relevant, higher-quality dataset
- Decrease batch size to 1 (more vigorous updates)

> [!tip] No single "best" approach -- experimentation is key. Unsloth notebooks set optimal parameters based on research papers and experiments.

Acknowledgements: Thanks to [Eyera](https://huggingface.co/Orenguteng) for contributing to this guide.

---
# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://unsloth.ai/docs/get-started/fine-tuning-llms-guide/lora-hyperparameters-guide.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

#lora #fine-tuning #hyperparameters #qlora #llm-training
