---
title: vLLM Engine Arguments
url: https://unsloth.ai/docs/basics/inference-and-deployment/vllm-guide/vllm-engine-arguments.md
source: llms
fetched_at: 2026-04-27T18:14:45.108102585-03:00
rendered_js: false
word_count: 474
summary: This document provides a comprehensive reference of available arguments and flags for configuring the vLLM engine when serving models. It details options related to memory utilization, sequence length, quantization methods (like fp8), tensor/pipeline parallelism, LoRA support, data types, and more.
tags:
    - vllm-arguments
    - engine-configuration
    - model-serving
    - gpu-optimization
    - lora-support
    - quantization-options
category: reference
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# vLLM Engine Arguments

vLLM engine arguments and flags for serving models.

## Argument Reference

| Argument | Description |
| --- | --- |
| `--gpu-memory-utilization` | Default 0.9. Fraction of VRAM vLLM can use. Reduce if OOM; try 0.95 or 0.97. |
| `--max-model-len` | Max sequence length. Reduce if OOM. E.g., `--max-model-len 32768` for 32K. |
| `--quantization` | Use `fp8` for dynamic float8 quantization. Pair with `--kv-cache-dtype fp8`. |
| `--kv-cache-dtype` | Use `fp8` for float8 KV cache (50% memory reduction). |
| `--port` | Default 8000. Localhost access port. |
| `--api-key` | Optional password for model access. |
| `--tensor-parallel-size` | Default 1. Split model across tensors. Set to GPU count. Requires NCCL. |
| `--pipeline-parallel-size` | Default 1. Split model across layers. Use with TP: TP within node, PP across nodes (PP = node count). |
| `--enable-lora` | Enable LoRA serving (for Unsloth finetuned LoRAs). |
| `--max-loras` | Max concurrent LoRAs (e.g., 1 or 16). Queue-based hot-swap. |
| `--max-lora-rank` | Max rank: `8`, `16`, `32`, `64`, `128`, `256`, `320`, `512`. |
| `--dtype` | `auto`, `bfloat16`, `float16`. Float8/other quant uses `--quantization`. |
| `--tokenizer` | Tokenizer path if different from served model (e.g., `unsloth/gpt-oss-20b`). |
| `--hf-token` | HuggingFace token for gated models. |
| `--swap-space` | Default 4GB. CPU offloading. Reduce if VRAM available, increase for low-memory GPUs. |
| `--seed` | Default 0. |
| `--disable-log-stats` | Disable throughput/request logging. |
| `--enforce-eager` | Disable compilation. Faster load, slower inference. |
| `--disable-cascade-attn` | For RL with vLLM < 0.11.0. Cascade Attention buggy on A100 (Unsloth fixes this). |

## Float8 Quantization

Llama 3.3 70B Instruct (128K context) with Float8 KV cache + quantization:

```bash
vllm serve unsloth/Llama-3.3-70B-Instruct \
    --quantization fp8 \
    --kv-cache-dtype fp8
    --gpu-memory-utilization 0.97 \
    --max-model-len 65536
```

## LoRA Hot Swapping / Dynamic LoRAs

Enable LoRA serving for up to 4 hot-swapped LoRAs. Set environment flag to allow hot swapping. See [[089-basics-inference-and-deployment-vllm-guide-lora-hot-swapping-guide|LoRA Hot Swapping Guide]].

#vllm #model-serving #gpu-optimization #lora #quantization
