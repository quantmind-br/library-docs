---
title: Unsloth Benchmarks
url: https://unsloth.ai/docs/basics/unsloth-benchmarks.md
source: llms
fetched_at: 2026-04-27T18:15:17.742955671-03:00
rendered_js: false
word_count: 475
summary: This document presents various benchmarks for Unsloth performance compared to Hugging Face methods, detailing speed improvements and significantly longer context length capabilities when fine-tuning LLMs like Llama 3.1 and Llama 3.3.
tags:
    - unsloth-benchmarks
    - llm-fine-tuning
    - llama-performance
    - context-length
    - qlora-comparison
    - gpu-testing
category: reference
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Unsloth Benchmarks

Unsloth vs Hugging Face performance. More details: [Llama 3.3 Blog](https://unsloth.ai/blog/llama3-3). External benchmarks by [Hugging Face](https://huggingface.co/blog/unsloth-trl).

> [!warning] `torch.compile` warmup takes ~5 minutes. Measure throughput **after** full load — Unsloth is faster over longer runs.

**Test setup**: H100 and [Blackwell](https://unsloth.ai/docs/blog/fine-tuning-llms-with-blackwell-rtx-50-series-and-unsloth) GPUs, Alpaca dataset, batch size 2, gradient accumulation 4, rank 32, QLoRA on all linear layers (q, k, v, o, gate, up, down).

| Model | VRAM | Unsloth Speed | Unsloth VRAM Reduction | Unsloth Longer Context | HF + FA2 |
| --- | --- | --- | --- | --- | --- |
| Llama 3.3 (70B) | 80GB | 2x | >75% | 13x longer | 1x |
| Llama 3.1 (8B) | 80GB | 2x | >70% | 12x longer | 1x |

## Context Length Benchmarks

> [!info] More data = less VRAM used (Unsloth [gradient checkpointing](https://unsloth.ai/blog/long-context) + Apple CCE algorithm).

### Llama 3.1 (8B) max context length

4bit QLoRA on all linear layers (Q, K, V, O, gate, up, down), rank 32, batch size 1. Sequences padded to max length.

| GPU VRAM | Unsloth context length | HF + FA2 |
| --- | --- | --- |
| 8 GB | 2,972 | OOM |
| 12 GB | 21,848 | 932 |
| 16 GB | 40,724 | 2,551 |
| 24 GB | 78,475 | 5,789 |
| 40 GB | 153,977 | 12,264 |
| 48 GB | 191,728 | 15,502 |
| 80 GB | 342,733 | 28,454 |

### Llama 3.3 (70B) max context length

80GB A100, same QLoRA config.

| GPU VRAM | Unsloth context length | HF + FA2 |
| --- | --- | --- |
| 48 GB | 12,106 | OOM |
| 80 GB | 89,389 | 6,916 |

#unsloth-benchmarks #fine-tuning #llama #context-length #qlora
