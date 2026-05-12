---
title: Attention Backend - SGLang Documentation
url: https://docs.sglang.io/docs/advanced_features/attention_backend
source: sitemap
fetched_at: 2026-05-11T05:49:40.926720154-03:00
rendered_js: false
word_count: 831
summary: This document provides a comprehensive overview of attention backends supported by SGLang, including support matrices for MHA, MLA, GDN, and NSA, as well as guidance on automatic backend selection and hybrid attention configurations.
tags:
    - sglang
    - attention-backend
    - llm-optimization
    - cuda
    - flash-attention
    - mha
    - mla
category: reference
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

SGLang supports a large variety of attention backends. Each of them has different pros and cons. You can test them according to your needs.

## Support Matrix

The support matrix is split into two parts: MHA (standard attention) and MLA (multi-head latent attention). For an explanation of the key differences between MHA and MLA, please see the [SGLang documentation on DeepSeek MLA](https://docs.sglang.io/docs/basic_usage/deepseek_v3#multi-head-latent-attention-mla-throughput-optimizations) and the original [DeepSeek MLA paper](https://arxiv.org/pdf/2405.04434).

### MHA Backends

**Backend****Page Size &gt; 1 (native)****FP8 KV Cache****FP4 KV Cache****Spec topk=1****Spec topk&gt;1****Sliding Window****MultiModal****FlashInfer**✅✅❌✅✅✅❌**FA3 (FlashAttention 3)**✅✅❌✅✅✅✅**FA4 (FlashAttention 4)**128❌✅✅✅✅✅**Triton**❌✅✅✅✅✅✅**Torch Native (SDPA)**❌✅✅❌❌❌✅**FlexAttention (PyTorch)**❌❌✅❌❌❌❌**TRTLLM MHA**16, 32 or 64✅✅✅❌✅❌**Dual Chunk FlashAttention**✅❌❌❌❌❌❌**AITER (ROCm)**✅✅❌✅✅✅✅**Wave (ROCm)**✅❌❌❌❌❌❌**Ascend (NPU)**✅❌❌✅❌✅✅**Intel XPU**✅❌❌❌❌✅❌**Intel AMX (CPU)**❌❌❌❌❌❌❌

### MLA Backends

**Backend****Native Page Sizes****FP8 KV Cache****FP4 KV Cache****Chunked Prefix Cache****Spec topk=1****Spec topk&gt;1****FlashInfer MLA**1❌✅✅✅❌**FlashMLA**64✅✅✅✅❌**Cutlass MLA**128✅✅✅✅❌**TRTLLM MLA (Blackwell)**32 or 64✅✅✅✅❌**FA3 (FlashAttention 3)**n/a❌❌✅✅⚠️ (page\_size=1 only)**Triton**n/a❌❌❌✅⚠️ (page\_size=1 only)**FA4**1❌✅✅❌❌**Ascend MLA (NPU)**128❌❌❌❌❌

Many backends that do not natively operate on pages can emulate `page_size > 1` at the wrapper layer by expanding page tables to per-token indices. The “Page Size &gt; 1 (native)” column indicates true in-kernel paging. Some backends require fixed native page sizes and cannot be reduced/emulated differently: TRTLLM MHA (16/32/64), TRTLLM MLA (32/64), FlashMLA (64), Cutlass MLA (128), Ascend (128). MLA page-size constraints:

- FlashInfer MLA: page\_size = 1.
- FlashMLA: page\_size = 64.
- Cutlass MLA: page\_size = 128.
- TRTLLM MLA: page\_size ∈ {32, 64}.

### GDN Attention Backends

GDN (Gated Delta Network) is a linear attention mechanism with O(n) complexity, used in hybrid models that alternate GDN linear attention layers with standard full attention layers. GDN is **not** selected via `--attention-backend`; it is automatically activated when the model architecture requires it (e.g., Qwen 3.5, Qwen 3 Next, Jet Nemotron, Jet VLM). The GDN linear attention layers have their own kernel backends, selected via `--linear-attn-backend` (default: `triton`). You can override the kernel per phase with `--linear-attn-decode-backend` and `--linear-attn-prefill-backend`.

BackendDecodePrefill / ExtendSpec Decoding (Target Verify)**Triton (CUDA)**✅✅✅**Triton (AMD/ROCm)**✅✅✅**Triton (NPU)**✅✅❌**Triton (CPU)**✅✅❌**CuTe DSL (CUDA only)**✅❌❌

### DSA Attention Backend (NSA)

DSA (Deepseek Sparse Attention) is a native sparse attention mechanism used by [DeepSeek V3.2](https://lmsys.org/blog/2025-09-29-deepseek-V32/). It is activated automatically when the model architecture requires it and is selected via `--attention-backend nsa`. Internally, the NSA backend dispatches to different sub-backends for prefill and decode phases. You can override these with `--nsa-prefill-backend` and `--nsa-decode-backend`:

Sub-backendPrefillDecodeNotes**flashmla\_sparse**✅✅Default prefill on Hopper and Blackwell (bf16)**flashmla\_kv**✅✅Default decode for FP8 on Blackwell with DP**flashmla\_auto**✅❌Auto-selects flashmla\_sparse or flashmla\_kv based on kv\_cache\_dtype**fa3**✅✅Default decode on Hopper (bf16)**trtllm**✅✅Default decode on Blackwell (bf16); default for both on Blackwell without DP**tilelang**✅✅Default on AMD (ROCm)**aiter**✅✅AMD-specific kernel library (requires aiter package)

For deployment examples, see the [DeepSeek V3.2 deployment guide](https://docs.sglang.io/docs/basic_usage/deepseek_v32).

### Hybrid attention (different backends for prefill vs decode) (Experimental)

You can mix-and-match attention backends for prefill and decode. This is useful when one backend excels at prefill and another excels at decode. For the implementation details, please see `python/sglang/srt/layers/attention/hybrid_attn_backend.py`.

```
# Example: Prefill with FA4, Decode with TRTLLM MLA (Blackwell)
python3 -m sglang.launch_server \
  --model-path nvidia/DeepSeek-R1-FP4 \
  --tp 8 \
  --attention-backend trtllm_mla \
  --moe-runner-backend flashinfer_trtllm \
  --quantization modelopt_fp4 \
  --prefill-attention-backend fa4
```

#### Speculative decoding with hybrid attention

Hybrid attention also works with speculative decoding. The backend used for draft decoding and target verification depends on `--speculative-attention-mode`:

- `--speculative-attention-mode decode` (recommended): draft/verify use the decode backend.
- `--speculative-attention-mode prefill` (default): draft/verify use the prefill backend.

Constraints when combining hybrid attention with speculative decoding:

- If any attention backend is `trtllm_mha`, speculative decoding supports only `--speculative-eagle-topk 1`.
- For paged MHA backends with `--page-size > 1` and `--speculative-eagle-topk > 1`, only `flashinfer` is supported.
- CUDA Graph: the decode backend is always captured; the prefill backend is captured only when `--speculative-attention-mode prefill`.

## Attention Backend Selection Guide (CUDA)

If the `--attention-backend` argument is not specified, SGLang automatically selects the best backend based on the hardware (CUDA) and model architecture.

### Automatic Selection Logic

**1. MHA Models (e.g., Llama, Qwen)**

- **Hopper (e.g., H100, H200)**: Defaults to `fa3` if using CUDA 12.3+ and the model configuration is supported.
- **Blackwell (e.g., B200)**: Defaults to `trtllm_mha`, unless using speculative decoding with `topk > 1`.
- **Other Architectures (Ampere, Ada, etc.)**: Defaults to `flashinfer` if available; otherwise falls back to `triton`.

**2. MLA Models (e.g., DeepSeek V3)**

- **Hopper**: Defaults to `fa3` (requires CUDA 12.3+).
- **Blackwell**: Defaults to `flashinfer`; `trtllm_mla` is auto-selected for DeepSeek V3 models specifically.
- **Other Architectures**: Defaults to `triton`.

## User Guide

### Launch Command for Different Attention Backends

- FlashInfer (Default for Non-Hopper Machines, e.g., A100, A40)

```
python3 -m sglang.launch_server \
  --model meta-llama/Meta-Llama-3.1-8B-Instruct \
  --attention-backend flashinfer
python3 -m sglang.launch_server \
  --tp 8 \
  --model deepseek-ai/DeepSeek-V3 \
  --attention-backend flashinfer \
  --trust-remote-code
```

- FlashAttention 3 (Default for Hopper Machines, e.g., H100, H200, H20)

```
python3 -m sglang.launch_server \
  --model meta-llama/Meta-Llama-3.1-8B-Instruct \
  --attention-backend fa3
python3 -m sglang.launch_server \
  --tp 8 \
  --model deepseek-ai/DeepSeek-V3 \
  --trust-remote-code \
  --attention-backend fa3
```

- Triton

```
python3 -m sglang.launch_server \
  --model meta-llama/Meta-Llama-3.1-8B-Instruct \
  --attention-backend triton
python3 -m sglang.launch_server \
  --tp 8 \
  --model deepseek-ai/DeepSeek-V3 \
  --attention-backend triton \
  --trust-remote-code
```

- FlashMLA

```
python3 -m sglang.launch_server \
  --tp 8 \
  --model deepseek-ai/DeepSeek-R1 \
  --attention-backend flashmla \
  --trust-remote-code
python3 -m sglang.launch_server \
  --tp 8 \
  --model deepseek-ai/DeepSeek-R1 \
  --attention-backend flashmla \
  --kv-cache-dtype fp8_e4m3 \
  --trust-remote-code
```

- TRTLLM MLA (Optimized for Blackwell Architecture, e.g., B200)

```
python3 -m sglang.launch_server \
  --tp 8 \
  --model deepseek-ai/DeepSeek-R1 \
  --attention-backend trtllm_mla \
  --trust-remote-code
```

- TRTLLM MLA with FP8 KV Cache (Higher concurrency, lower memory footprint)

```
python3 -m sglang.launch_server \
  --tp 8 \
  --model deepseek-ai/DeepSeek-R1 \
  --attention-backend trtllm_mla \
  --kv-cache-dtype fp8_e4m3 \
  --trust-remote-code
```

- TRTLLM MHA (Optimized for Blackwell Architecture, e.g., B200)

```
python3 -m sglang.launch_server \
  --tp 4 \
  --model Qwen/Qwen3.5-35B-A3B-FP8 \
  --attention-backend trtllm_mha \
  --trust-remote-code
```

- TRTLLM MHA (XQA backend) (Optimized for SM90 and SM120, e.g., H20, H200, 5090) Note that TRTLLM XQA backend only works well for pagesize 64.

```
python3 -m sglang.launch_server \
  --tp 4 \
  --model Qwen/Qwen3.5-35B-A3B-FP8 \
  --decode-attention-backend trtllm_mha \
  --trust-remote-code
```

- FlashAttention 4 (MHA & MLA)

```
# FA4 for both prefill and decode on SM90/SM100
python3 -m sglang.launch_server \
  --model-path Qwen/Qwen3-30B-A3B-Instruct-2507-FP8 \
  --attention-backend fa4 \
  --page-size 128 \
  --trust-remote-code

python3 -m sglang.launch_server \
  --tp 8 \
  --model deepseek-ai/DeepSeek-R1 \
  --prefill-attention-backend fa4 \
  --trust-remote-code
```

- Cutlass MLA

```
python3 -m sglang.launch_server \
  --tp 8 \
  --model deepseek-ai/DeepSeek-R1 \
  --attention-backend cutlass_mla \
  --trust-remote-code
```

- Ascend

```
python3 -m sglang.launch_server \
  --model meta-llama/Meta-Llama-3.1-8B-Instruct \
  --attention-backend ascend
```

- Intel XPU

```
python3 -m sglang.launch_server \
  --model meta-llama/Meta-Llama-3.1-8B-Instruct \
  --attention-backend intel_xpu
```

- Wave

```
python3 -m sglang.launch_server \
  --model meta-llama/Meta-Llama-3.1-8B-Instruct \
  --attention-backend wave
```

- FlexAttention

```
python3 -m sglang.launch_server \
  --model meta-llama/Meta-Llama-3.1-8B-Instruct \
  --attention-backend flex_attention
```

- Dual Chunk FlashAttention

```
python3 -m sglang.launch_server \
  --model Qwen/Qwen2.5-14B-Instruct-1M \
  --attention-backend dual_chunk_flash_attn
```

- Torch Native

```
python3 -m sglang.launch_server \
  --model meta-llama/Meta-Llama-3.1-8B-Instruct \
  --attention-backend torch_native
```

## Steps to add a new attention backend

To add a new attention backend, you can learn from the existing backends (`python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`) and follow the steps below.

1. Run without cuda graph. Support the two forward functions
   
   - forward\_extend
     
     - Will be used for prefill, prefill with KV cache, and target verification
     - It will be called once per layer
   - forward\_decode
     
     - Will be used for normal decode, and draft decode
     - It will be called once per layer
   - init\_forward\_metadata
     
     - Initialize the class and common metadata shared by all layers
     - Call the plan function for optimizations like split\_kv
     - It will be called once per forward
2. Run with cuda graph. It has two phases (capture and replay) and you need to implement three functions
   
   - init\_cuda\_graph\_state
     
     - It will be called once during life time
     - Create all common shared buffers
   - init\_forward\_metadata\_capture\_cuda\_graph
     
     - It will be called before capturing a cuda graph
     - It is similar to init\_forward\_metadata but write the medatada to some pre-defined buffers
   - init\_forward\_metadata\_replay\_cuda\_graph
     
     - It will be called before replaying a cuda graph
     - This function is in the critical path and needs to be fast