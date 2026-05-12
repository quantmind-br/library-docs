---
title: 3x Faster LLM Training with Unsloth Kernels + Packing
url: https://unsloth.ai/docs/blog/3x-faster-training-packing.md
source: llms
fetched_at: 2026-04-27T18:15:18.72882065-03:00
rendered_js: false
word_count: 1672
summary: This document details the performance enhancements in Unsloth, showcasing up to 5x faster LLM training achieved through custom RoPE and MLP Triton kernels, along with intelligent auto-packing capabilities that drastically reduce VRAM usage without affecting accuracy.
tags:
    - llm-training
    - unsloth
    - triton-kernels
    - vram-reduction
    - padding-free
    - performance-boost
category: reference
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# 3x Faster LLM Training with Unsloth Kernels + Packing

Unsloth supports up to **5x faster** (typically 3x) training via custom **RoPE and MLP Triton kernels** + smart auto packing. Kernels also **reduce VRAM 30-90%** with no accuracy loss. Example: [Qwen3](047-models-tutorials-qwen3-how-to-run-and-fine-tune.md)-4B trains on just **3GB VRAM**, 3x faster.

Key improvements:
- **2.3x faster QK Rotary Embedding** — fused Triton kernel with packing support
- Updated SwiGLU/GeGLU kernels with **int64 indexing for long context**
- **2.5x to 5x faster uncontaminated packing** — xformers, SDPA, FA3 backends
- **2.1x faster padding-free, 50% less VRAM**, 0% accuracy change
- Improved SFT loss stability and more predictable GPU utilization
- Works **for all training methods** (full fine-tuning, pretraining, etc.)

Padding-free packing is auto-enabled for all training runs. All fast attention backends supported (FlashAttention 3, xFormers, SDPA). Loss curves match non-packing runs exactly.

## Fused QK RoPE Triton Kernel with Packing

Original RoPE kernel (Dec 2023 launch) had 2 separate Triton kernels for Q and K. Merged into 1 kernel with variable-length RoPE support (required for padding-free packing). Result: **2.3x faster on longer context**, 1.9x faster on shorter context.

Also eliminated all clones and contiguous transpose operations — **RoPE is now fully inplace**, reducing GPU memory further.

Backward pass uses `sin1 = -sin1`:

```
Q * cos + rotate_half(Q) * sin
is equivalent to
Q * cos + Q @ R * sin
where R is a rotation matrix [ 0,  I]
                             [-I,  0]
dC/dY = dY * cos + dY @ R.T * sin
where R.T is again the same  [ 0, -I]
but the minus is transposed. [ I,  0]
```

## Int64 Indexing for Triton Kernels

During [[103-blog-500k-context-length-fine-tuning.md|500K context training]], CUDA out-of-bounds errors occurred because MLP kernels (SwiGLU, GeGLU) used int32 indexing (Triton/CUDA default).

Rather than always using `tl.program_id(0).to(tl.int64)` (which slows short-context training), `LONG_INDEXING` is a `tl.constexpr` variable so the Triton compiler specializes per context length:

```python
block_idx = tl.program_id(0)
if LONG_INDEXING:
    offsets = block_idx.to(tl.int64) * BLOCK_SIZE + tl.arange(0, BLOCK_SIZE).to(tl.int64)
    n_elements = tl.cast(n_elements, tl.int64)
else:
    offsets = block_idx * BLOCK_SIZE + tl.arange(0, BLOCK_SIZE)
```

## Why Padding is Needed and Mathematical Speedup

GPUs cannot process variable-length datasets, so padding with 0s is required. For a dataset with 50% short sequences (S) and 50% long sequences (L), worst-case token usage = `batchsize x L`.

Packing multiple examples into a single 1D tensor eliminates padding:

$$\text{Token Usage} = \frac{\text{batchsize}}{2}L+\frac{\text{batchsize}}{2}S$$

$$\text{Speedup} = \frac{\text{batchsize} \times L}{\frac{\text{batchsize}}{2}L+\frac{\text{batchsize}}{2}S} = 2 \frac{L}{L + S}$$

If S → 0: 2x theoretical speedup. With 20% long + 80% short: `L / 0.2L = 5x`. Packing speedup scales with the ratio of short sequences in your dataset.

## Padding-Free by Default

Beyond setting `packing = True` in `SFTConfig`, Unsloth **automatically uses padding-free batching** to reduce waste and increase tokens/s throughput with the ***exact same loss***.

Results for Qwen3-8B and Qwen3-32B: 60% memory reduction, 2x faster, identical loss and grad norm curves.

## Uncontaminated Packing — 2-5x Faster Training

Real datasets have varying sequence lengths; increasing batch size (e.g., to 32) causes padding, slowing training and increasing VRAM.

> [!tip] In the past, increasing `batch_size` to large numbers (>32) made training SLOWER due to padding. Now `packing = True` eliminates this — training gets FASTER.

Packing keeps sequence-length metadata to properly mask samples without leaking attention between samples. The RoPE kernel resets position ids per sample.

With 20% long + 80% short sequences: `L / 0.2L = 5x` faster training. More short rows = faster packing.

## Analysis and Benchmarks

Fine-tuning runs with [Qwen3-32B](047-models-tutorials-qwen3-how-to-run-and-fine-tune.md), Qwen3-8B, Llama 3 8B on `yahma/alpaca-cleaned`. Compared new Unsloth (packing + kernels) vs standard optimized (FA3 enabled). Fixed `max_length = 1024`, varied batch size in {1, 2, 4, 8, 16, 32} (token counts: 1K-32K per batch).

**Tokens/s throughput**: training an epoch **1.7-3x faster** (sometimes 5x+). Gains more pronounced with many short sequences and longer runs.

**Packing efficiency**: percentage of valid (non-padding) tokens per batch. Unpacked case approaches ~50% padding at batch size 8. Packed case maintains high efficiency regardless of max sequence length.

**Epoch progress** (`max_length = 2048`, `max_steps = 500`): packed case covers ~40% of an epoch in the same wall-clock time unpacked covers <5%. Loss curves match in scale and trend; packed loss is less variable (more tokens per step).

## How to Enable Packing

**Update Unsloth — padding-free is on by default.** All training immediately 1.1-2x faster, 30% less memory, 0% accuracy change.

```bash
pip install --upgrade --force-reinstall --no-cache-dir --no-deps unsloth
pip install --upgrade --force-reinstall --no-cache-dir --no-deps unsloth_zoo
```

Supported: Flash Attention 3 via xFormers, SDPA, FA2. Works on old GPUs (Tesla T4, RTX 2080) and new (H100, B200). Packing works regardless of attention backend or model family.

> [!warning] `packing=True` changes training loss and truncates dataset row count (multiple short sequences packed into 1). For identical loss numbers, set `packing=False` — auto padding-free still makes training faster.

Explicit packing example:

```python
from unsloth import FastLanguageModel
from trl import SFTTrainer, SFTConfig

model, tokenizer = FastLanguageModel.from_pretrained(
    "unsloth/Qwen3-14B",
)

trainer = SFTTrainer(
    model = model,
    processing_class = tokenizer,
    train_dataset = dataset,
    args = SFTConfig(
        per_device_train_batch_size = 1,
        max_length = 4096,
        …,
        packing = True, # required to enable sample packing!
    ),
)
trainer.train()
```

All notebooks auto-benefit. See [[073-get-started-unsloth-notebooks.md|unsloth-notebooks]].

See also:
- [[103-blog-500k-context-length-fine-tuning.md|500k-context-length-fine-tuning]]
- [[068-get-started-reinforcement-learning-rl-guide-memory-efficient-rl.md|memory-efficient-rl]]
- [[011-models-gpt-oss-how-to-run-and-fine-tune-long-context-gpt-oss-training.md|long-context-gpt-oss-training]]

#llm-training #unsloth #triton-kernels #vram-reduction #performance-boost
