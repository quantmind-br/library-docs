---
title: Fine-tune MoE Models 12x Faster with Unsloth
url: https://unsloth.ai/docs/basics/faster-moe.md
source: llms
fetched_at: 2026-04-27T18:15:02.232487256-03:00
rendered_js: false
word_count: 2519
summary: This document explains how Unsloth achieves up to 12x faster fine-tuning of Mixture of Experts (MoE) models by utilizing custom Triton kernels and mathematical optimizations. It details backend selection, performance benefits over standard PyTorch methods, and compatibility across various GPU hardware.
tags:
    - moe-llm
    - unsloth
    - fast-finetuning
    - triton-kernels
    - pytorch-optimization
    - grouped-mm
    - vram-reduction
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:33:00Z
---

# Fine-tune MoE Models 12x Faster with Unsloth

~12x faster MoE LLM training with **>35% less VRAM** and **~6x longer context** via custom Triton kernels and mathematical optimizations. No accuracy loss.

**Key facts:**
- Supports [gpt-oss](https://unsloth.ai/docs/models/gpt-oss-how-to-run-and-fine-tune), [Qwen3](https://unsloth.ai/docs/models/tutorials/qwen3-how-to-run-and-fine-tune) (30B, 235B, VL, Coder), DeepSeek [R1](https://unsloth.ai/docs/models/tutorials/deepseek-r1-0528-how-to-run-locally)/[V3](https://unsloth.ai/docs/models/tutorials/deepseek-v3.1-how-to-run-locally), GLM ([4.6](https://unsloth.ai/docs/models/tutorials/glm-4.6-how-to-run-locally), [4.7](https://unsloth.ai/docs/models/tutorials/glm-4.7), [Flash](https://unsloth.ai/docs/models/glm-4.7-flash))
- gpt-oss-20b fine-tunes in **12.8 GB VRAM**. Qwen3-30B-A3B (16-bit LoRA) uses 63GB
- Works on data-center (B200, H100), **consumer** and older GPUs (e.g., RTX 3090), FFT, LoRA and QLoRA

In collaboration with Hugging Face, MoE training is standardized with PyTorch's `torch._grouped_mm`. Transformers v5 has ~6x faster MoE than v4; Unsloth adds custom Triton grouped-GEMM + LoRA kernels for an **additional** ~2x speedup, >35% VRAM reduction and >6x longer context (12-30x overall vs v4).

**Notebooks:**

| Notebook | GPU |
| --- | --- |
| [gpt-oss (20b)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(20B\)-Fine-tuning.ipynb) (free) | Colab |
| [Qwen3-30B-A3B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_MoE.ipynb) | A100 |
| [GLM-4.7-Flash](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/GLM_Flash_A100\(80GB\).ipynb) | A100 |
| [gpt-oss-120b](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(120B\)_A100-Fine-tuning.ipynb) | A100 |
| [gpt-oss (500K context)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt_oss_\(20B\)_500K_Context_Fine_tuning.ipynb) | Colab |
| [TinyQwen3 MoE](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/TinyQwen3_MoE.ipynb) | test only |

## Unsloth MoE Triton Kernels

Custom Triton MoE kernels work alongside `torch._grouped_mm`. **Backwards compatible** with older hardware (A100) and older PyTorch versions.

On A100, Triton kernels are **~2.5x faster** than `torch._grouped_mm`. One-time autotune step (~2 minutes at training start) speeds up full runs by 35% on A100 vs `_grouped_mm` -- worthwhile for longer runs.

> [!tip]
> Larger models and longer context = more pronounced memory savings from Unsloth kernels (scales exponentially).

## Automatic backend selection

**Split LoRA approach**: ~35% less memory and 2x faster training vs Transformers v5 + `torch._grouped_mm`. Custom `torch._grouped_mm` + Triton kernels = ~12-30x faster than Transformers v4.

| Backend | Description |
| --- | --- |
| `grouped_mm` | `torch._grouped_mm` -- available T4 through B200, optimized for H100s+ |
| `unsloth_triton` | Unsloth Triton kernels -- auto-enables on A100s and older PyTorch |
| `native_torch` | Native PyTorch -- 12x slower, but VRAM reductions still apply |

```python
os.environ["UNSLOTH_MOE_BACKEND"] = "grouped_mm"
os.environ["UNSLOTH_MOE_BACKEND"] = "unsloth_triton"
os.environ["UNSLOTH_MOE_BACKEND"] = "native_torch"
```

> [!warning]
> **4-bit QLoRA for MoE is not supported** -- BitsandBytes doesn't support it. Use bf16 for LoRA or full fine-tuning.

> [!tip]
> Update Unsloth: `pip install --upgrade unsloth unsloth_zoo`

## What is torch._grouped_mm?

Previously MoE weights were stored as `ModuleList` of per-expert linear layers, requiring an expensive for-loop:

```python
for expert_idx in expert_hit:
    expert_idx = expert_idx[0]
    if expert_idx == num_experts: continue
    _, token_idx = torch.where(expert_mask[expert_idx])
    current_state = hidden_states[token_idx]
    gate, up = nn.functional.linear(current_state, self.gate_up_proj[expert_idx]).chunk(2, dim=-1)
```

PyTorch introduced [`grouped_mm`](https://docs.pytorch.org/docs/main/generated/torch.nn.functional.grouped_mm.html) to address this. Unsloth provides its own MoE-optimized Triton kernels. Transformers v5 changed from [ModuleList (4.57.6)](https://github.com/huggingface/transformers/blob/v4.57.6/src/transformers/models/qwen3_moe/modeling_qwen3_moe.py#L222):

```python
self.experts = nn.ModuleList(
    [Qwen3MoeMLP(config, intermediate_size) for _ in range(self.num_experts)]
)
```

to [single nn.Parameter (5.0.0)](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/qwen3_moe/modeling_qwen3_moe.py#L226):

```python
self.gate_up_proj = nn.Parameter(torch.empty(num_experts, 2 * intermediate_dim, hidden_dim))
```

`torch._grouped_mm` works on NVIDIA T4 and above; verified on H100, A100, B200, RTX 6000 Pro.

## Kernel Results + Benchmarks

Comparison vs Transformers v5 (which already uses `torch._grouped_mm`). LoRA rank = 64, all LoRA modules on MoE layers (gate, up, down).

### gpt-oss Benchmarks

Benchmark: [unsloth/gpt-oss-20b-BF16](https://huggingface.co/unsloth/gpt-oss-20b-BF16). **7x faster, 36% less VRAM** at 16K context. TF v5 + TRL OOMs at 16K; Unsloth does not. Speedup increases with sequence length.

| Context Length | Unsloth (ms) | TF v5 (ms) | Unsloth Mem (GB) | TF v5 Mem (GB) | Speed Up | VRAM Saving |
| --- | --- | --- | --- | --- | --- | --- |
| 1024 | 275.35 | 376.99 | 40.91 | 43.88 | 1.4x | 6.76% |
| 2048 | 292.88 | 696.57 | 41.83 | 44.93 | 2.4x | 6.89% |
| 4096 | 370.30 | 1785.89 | 43.68 | 49.86 | 4.8x | 12.39% |
| 8192 | 712.33 | 5226.86 | 47.43 | 73.80 | 7.3x | 35.73% |
| 16384 | 1775.80 | **OOM** | 55.13 | **OOM** | N/A | N/A |

### Qwen3 Benchmarks

NVIDIA B200. **~1.7x speedup, ~35% better memory efficiency** with Qwen3-30B-A3B LoRA. Memory savings improve at longer sequences. Qwen3-Next and Coder fit on single B200 in bf16 LoRA.

| Context Length | Unsloth (ms) | TF v5 (ms) | Unsloth Mem (GB) | TF v5 Mem (GB) | Speed Up | VRAM Saving |
| --- | --- | --- | --- | --- | --- | --- |
| 1024 | 366.3 | 628.3 | 80.88 | 104.80 | 1.7x | 2.06% |
| 2048 | 467.0 | 745.3 | 80.88 | 104.81 | 1.6x | 2.57% |
| 4096 | 711.6 | 975.5 | 80.89 | 104.80 | 1.4x | 5.08% |
| 8192 | 1376.6 | 1633.5 | 80.90 | 104.81 | 1.2x | 9.17% |
| 16384 | 3182.2 | 3407.9 | 85.53 | 116.61 | 1.1x | 15.26% |

H100: up to **1.77x speedup**, ~5.3GB saved at 4K context. TF v5 OOMs at 8K; Unsloth uses less memory at 8K than baseline at 4K.

### GLM 4.7 Benchmarks

**2.6x faster throughput, >15% less VRAM** across all batch sizes. GLM 4.7 Flash: 30B MoE (3B active params), 64 routed experts + 1 shared expert (DeepSeek MoE style).

[GLM 4.7 Flash Notebook (A100 80GB)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/GLM_Flash_A100(80GB).ipynb)

| Context Length | Unsloth (ms) | TF v5 (ms) | Unsloth Mem (GB) | TF v5 Mem (GB) | Speed Up | VRAM Saving |
| --- | --- | --- | --- | --- | --- | --- |
| 512 | 1145.0 | 2992.1 | 57.81 | 60.89 | 2.6x | 6.51% |
| 1024 | 1298.9 | 3323.3 | 58.76 | 62.55 | 2.6x | 6.22% |
| 2048 | 1831.9 | 4119.3 | 60.09 | 67.32 | 2.3x | 9.46% |
| 4096 | 2883.9 | 5646.1 | 63.34 | 76.78 | 2x | 14.83% |

## Faster LoRA MoE Training

Standard PEFT approach merges LoRA adapter into base weight before MoE computation, materializing `lora_B @ lora_A.t()` for all experts -- very memory-hungry. Unsloth avoids this by reordering operations via matrix-multiplication associativity. Same loss, gradients, outputs; different (faster) order of operations.

> [!warning]
> **4-bit QLoRA for MoE not supported** -- use bf16 for LoRA or full fine-tuning.

Optimizations are **enabled by default** for MoE models. Toggle via `UNSLOTH_MOE_BACKEND` env var.

```python
import os
# if you want to choose a different backend (grouped_mm by default), set the below variable:
# os.environ['UNSLOTH_MOE_BACKEND'] = 'unsloth_triton' # or grouped_mm or native_torch
lora_rank = 16
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "Qwen/Qwen3-30B-A3B-Instruct-2507", #MoE model
    max_seq_length = max_seq_length,
    load_in_4bit = False, # MoE nn.Parameter doesn't support bnb 4bit yet
)
model = FastLanguageModel.get_peft_model(
    model,
    r = lora_rank,
    target_modules = [
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_up_proj", "down_proj", # LoRA on MoE layers!
    ],
    lora_alpha = lora_rank*2, # *2 speeds up training
    use_gradient_checkpointing = "unsloth", # Reduces memory usage
    random_state = 3407,
)
```

## Implementation Details

### LoRA basics

LoRA trains low-rank adapters instead of full weight matrices. Weight shape **(m, n)** -> two matrices **(m, r)** and **(r, n)**. Tracks `m*r + r*n` params vs `m*n` (full fine-tuning). Typical MLP: `m~4096, n~12k, r~64` -> ~1M LoRA params vs ~48M full (~2%, minimal accuracy loss).

> [!info]
> Router layer fine-tuning is disabled by default -- not recommended for MoE.

### MoE LoRA specifics

MoE has **E expert MLPs in parallel**, so per-expert LoRA scales across all experts.

**Qwen3-30B-A3B**: hidden `m=2048`, intermediate `n=768`, **E=128** experts, **k=8** activated per token. Per expert: `gate_up_proj` = `(m, n) = (2048, 768)`, `down_proj` = `(n, m) = (768, 2048)`.

With LoRA rank `r=64`: `r*(m+n)=180,224` params per expert (~11% of a `2048x768` matrix). Core issue: `r/n = 64/768` is large vs typical MLP (e.g., `r/n = 64/25600` in [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B/blob/main/config.json#L13)). Fused `gate_up_proj` roughly doubles overhead.

**Memory comparison** (per expert):

```
# Common to both approaches
Input activations: (s, m)
Final output: (s, n)
```

PEFT approach -- materializes full delta:
```
delta = loraA@loraB = (m,n) per expert = Emn parameters
```

Unsloth Split LoRA -- sparse computation:
```
Y = X @ loraA : (s,m) @ (m, r)  # sparse for k experts = ksr parameters
Y @ loraB    : (s, r) @ (r, n)  # sparse for k experts = ksn parameters
```

**For Qwen3-30B-A3B** (`E=128, k=8, m=2048, n=768`):

$$
\text{PEFT params: } Emn \quad | \quad \text{Split LoRA params: } ks(r+n)
$$
$$
\text{Split LoRA better when: } Emn > ksn \Rightarrow s < \frac{Emn}{kn} = 32K
$$

**Compute comparison:**

$$
\text{MoE PEFT LoRA flops} = E(2mnr + mn) + 2k \cdot smn
$$
$$
\text{MoE Split LoRA flops} = 2k(smn + smr + srn)
$$
$$
\text{Crossover: } s > \frac{Emn}{k(m+n)} \times (1+\frac{1}{2r}) \approx 16K \text{ tokens}
$$

Additional speedups from **reduced memory traffic** -- modern GPUs are bandwidth-bound. Rough speedup estimate: `Emn / [k*s*(m+n)]`.

## Model Support

- **Qwen3** (Thinking and Instruct): VL, 2507, Coder
- **gpt-oss**: 20B, 120B, safeguard
- **GLM**: 4.5, 4.6, 4.6-Air, 4.7, 4.7-Flash
- **DeepSeek**: V3, R1, V3.1, V3.2

## More Benchmarks

### gpt-oss BF16 (vs Transformers v4)

**Training Speed:**

| Context length | Unsloth (ms) | TF v5 (ms) | TF v4 (ms) | Speed Up |
| --- | --- | --- | --- | --- |
| 1024 | 275.35 | 376.99 | 2111.18 | 1.37x |
| 2048 | 292.88 | 696.57 | 2626.80 | 2.38x |
| 4096 | 370.30 | 1785.89 | 4027.93 | 4.82x |
| 8192 | 712.33 | 5226.86 | 8513.52 | 7.34x |
| 16384 | 1775.80 | OOM | OOM | N/A |

**VRAM Usage:**

| Context length | Unsloth Mem (GB) | TF v5 Mem (GB) | TF v4 Mem (GB) | VRAM Saving |
| --- | --- | --- | --- | --- |
| 1024 | 40.91 | 43.88 | 89.75 | 6.76% |
| 2048 | 41.83 | 44.93 | 90.47 | 6.89% |
| 4096 | 43.68 | 49.86 | 92.72 | 12.39% |
| 8192 | 47.43 | 73.80 | 100.3 | 35.73% |
| 16384 | 55.13 | OOM | OOM | N/A |

## Important Unsloth Updates

1. **Gemma-3 now uses Flex-Attention by default** (works in float16). **O(N) memory (not O(N^2)), >3x faster training**. Scales better with context. Previous versions OOMed.

| Context | Old Peak VRAM | New Peak VRAM | VRAM Saving |
| --- | --- | --- | --- |
| 1K | 20.1 GB | 20.1 GB | 0 GB (0%) |
| 2K | 21.5 GB | 21.1 GB | 0.3 GB (2%) |
| 4K | 27.7 GB | 23.3 GB | 4.5 GB (16%) |
| 8K | 52.3 GB | 27.5 GB | 24.8 GB (47%) |
| 16K | OOM | 36.0 GB | -- |
| 24K | OOM | 44.6 GB | -- |
| 32K | OOM | 53.1 GB | -- |
| 48K | OOM | 38.4 GB | -- |
| 64K | OOM | 44.7 GB | -- |

2. Vision fine-tuning now accepts mixed image + text data
3. [Windows now officially supported (no WSL needed)](https://unsloth.ai/docs/get-started/install/windows-installation)
4. `trl==0.27.1` and `transformers==5.1.0` supported -- >80% notebook coverage (up from 30%), targeting 100%
5. Bug fixes -- see https://github.com/unslothai/unsloth/releases/tag/February-2026

> [!tip]
> Update Unsloth: `pip install --upgrade unsloth unsloth_zoo`

### Acknowledgements

Hugging Face team for MoE training collaboration. torchao team, especially Vasily Kuznetsov (vkuzo), for grouped_mm float16 support on T4 and A100 backward compatibility.

#moe #unsloth #triton #lora #pytorch #fine-tuning
