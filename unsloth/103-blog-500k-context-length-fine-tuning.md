---
title: 500K Context Length Fine-tuning
url: https://unsloth.ai/docs/blog/500k-context-length-fine-tuning.md
source: llms
fetched_at: 2026-04-27T18:15:19.095461511-03:00
rendered_js: false
word_count: 1172
summary: This document details new algorithms within Unsloth designed to significantly extend the context length capabilities of LLMs and VLMs. Key improvements include fused/chunked loss, enhanced Gradient Checkpointing, and the introduction of Tiled MLP, which together allow training on contexts exceeding 500K tokens with minimal accuracy degradation.
tags:
    - long-context
    - llm-training
    - unsloth
    - tiled-mlp
    - gradient-checkpointing
    - vram-optimization
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# 500K Context Length Fine-tuning

New algorithms in Unsloth enabling **500K+ context** training for any LLM/VLM. gpt-oss-20b reaches 500K+ on a single 80GB H100 (up from 80K), and >750K on a B200 192GB.

> [!tip] Try it
> [500K-context gpt-oss-20b fine-tuning on 80GB A100 Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt_oss_\(20B\)_500K_Context_Fine_tuning.ipynb)

## Key Improvements

- **60% lower VRAM** with **3.2x longer context** via fused/chunked cross-entropy loss -- no speed or accuracy degradation
- Enhanced activation offloading in Unsloth Gradient Checkpointing
- **Tiled MLP** (with [Stas Bekman](https://x.com/StasBekman), Snowflake) enables 2x more contexts

gpt-oss-20b QLoRA (4bit): 290K context on H100 with no accuracy loss; 500K+ with Tiled MLP -- **>6.4x longer context lengths** overall.

With latest update, **1M context length** is possible with a smaller model on a single GPU.

## Unsloth Loss Refactoring: Chunk & Fuse

Dynamic sequence chunking: instead of computing logits and cross-entropies over the entire sequence at once, processes manageable slices along the flattened sequence dimension. Each chunk runs a fully fused forward + backward pass via `torch.func.grad_and_value`, retaining mixed precision accuracy by upcasting to float32 if necessary. No degradation in training speed or accuracy.

**Chunk size is chosen automatically at runtime** based on available VRAM:
- More free VRAM -> larger chunks (faster)
- Less VRAM -> more chunks (avoids memory blowouts)

This removes manual tuning and keeps the algorithm robust across GPUs, workloads, and sequence lengths.

> [!success] Auto-tuning behavior
> Smaller contexts use more VRAM (fewer chunks) to avoid unnecessary overhead. With 80GB VRAM, yields >3.2x longer contexts.

## Unsloth Gradient Checkpointing Enhancements

[Unsloth Gradient Checkpointing](https://unsloth.ai/blog/long-context) (introduced April 2024) offloads activations to CPU RAM for 10x longer context lengths. New enhancements use CUDA Streams to add at most **0.1%** training overhead with no accuracy impact (previously 1-3%).

```python
# Original Unsloth version released April 2024 - LGPLv3 Licensed
class Unsloth_Offloaded_Gradient_Checkpointer(torch.autograd.Function):
    @staticmethod
    @torch_amp_custom_fwd
    def forward(ctx, forward_function, hidden_states, *args):
        ctx.device = hidden_states.device
        saved_hidden_states = hidden_states.to("cpu", non_blocking = True)
        with torch.no_grad():
            output = forward_function(hidden_states, *args)
        ctx.save_for_backward(saved_hidden_states)
        ctx.forward_function, ctx.args = forward_function, args
        return output

    @staticmethod
    @torch_amp_custom_bwd
    def backward(ctx, dY):
        (hidden_states,) = ctx.saved_tensors
        hidden_states = hidden_states.to(ctx.device, non_blocking = True).detach()
        hidden_states.requires_grad_(True)
        with torch.enable_grad():
            (output,) = ctx.forward_function(hidden_states, *ctx.args)
        torch.autograd.backward(output, dY)
        return (None, hidden_states.grad,) + (None,)*len(ctx.args)
```

By offloading activations as soon as produced, peak activation footprint is minimized and GPU memory is freed when needed. A single decoder layer's activations can exceed 2 GB in long-context/large-batch training.

> **Unsloth's new algorithms + Gradient Checkpointing contributes most improvements (3.2x), enabling 290K-context-length QLoRA GPT-OSS fine-tuning on a single H100.**

## Tiled MLP: Unlocking 500K+

Integrated from Snowflake's Arctic Long Sequence Training [paper](https://arxiv.org/abs/2506.13996). TiledMLP reduces activation memory by tiling hidden states along the sequence dimension before heavy MLP projections.

### Quality-of-Life Improvements

RNG state is preserved across tiled forward recomputations, so dropout and stochastic ops are consistent between forward and backward replays. Nested checkpointed computations remain stable and numerically identical.

> [!success] Auto-patching
> Auto-patches any module named or typed as `mlp` -- nearly all models with MLP modules are supported out of the box.

### Tradeoffs

TiledMLP saves VRAM at the cost of extra forward passes. Inside a checkpointed transformer block, it becomes a nested checkpoint: one MLP performs **~3 forward passes and 1 backward pass per step**. In return, nearly all intermediate MLP activations are dropped from VRAM.

Memory timeline comparison (single decoder layer):
- **Without Tiled MLP**: peak VRAM during MLP backward
- **With Tiled MLP**: peak shifts to fused loss calculation; **~40% lower VRAM**

Overall: without Tiled MLP, long-context training requires roughly **2x memory**; with Tiled MLP, a single GPU pays only about **1.3x increase in step time** for the same context length.

### Enabling Tiled MLP

```py
model, tokenizer = FastLanguageModel.from_pretrained(
    ...,
    unsloth_tiled_mlp = True,
)
```

Set `unsloth_tiled_mlp = True` in `from_pretrained`. Follows Arctic paper logic: `num_shards = ceil(seq_len/hidden_size)`. Each tile operates on sequence lengths equal to the model's hidden dimension to balance throughput and memory savings.

> [!tip] When to use
> Next time fine-tuning runs out of memory, try `unsloth_tiled_mlp = True`. Saves VRAM as long as context length > model's hidden dimension.

DeepSpeed provided a [doc update](https://github.com/deepspeedai/DeepSpeed/pull/7664) for Tiled MLP within DeepSpeed.

#long-context #llm-training #unsloth #tiled-mlp
