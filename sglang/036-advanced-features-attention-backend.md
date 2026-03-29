---
title: Attention Backend — SGLang
url: https://docs.sglang.io/advanced_features/attention_backend.html
source: crawler
fetched_at: 2026-02-04T08:46:46.714907042-03:00
rendered_js: false
word_count: 825
summary: This document provides a comprehensive guide on selecting and configuring various attention backends in SGLang to optimize performance based on hardware and model architecture.
tags:
    - sglang
    - attention-backend
    - mha
    - mla
    - gpu-optimization
    - llm-inference
category: guide
---

## Contents

## Attention Backend[#](#attention-backend "Link to this heading")

SGLang supports a large variety of attention backends. Each of them has different pros and cons. You can test them according to your needs.

Important

Selecting an optimal attention backend is crucial for maximizing your performance. Different backends excel in various scenarios, so choose based on your model, hardware, and use case. Not all backends are supported on all platforms and model architectures.

If you don’t specify `--attention-backend`, SGLang makes a best effort to automatically select the most performant backend based on your hardware and model architecture.

## Support Matrix[#](#support-matrix "Link to this heading")

The support matrix is split into two parts: MHA (standard attention) and MLA (multi-head latent attention). For an explanation of the key differences between MHA and MLA, please see the [SGLang documentation on DeepSeek MLA](https://docs.sglang.io/basic_usage/deepseek_v3.html#multi-head-latent-attention-mla-throughput-optimizations) and the original [DeepSeek MLA paper](https://arxiv.org/pdf/2405.04434).

### MHA Backends[#](#mha-backends "Link to this heading")

### MLA Backends[#](#mla-backends "Link to this heading")

Note

Multimodal attention is selected by `--mm-attention-backend`. The “MultiModal” column indicates whether a corresponding multimodal implementation exists for that backend family.

Note

- FlashAttention 4 is prefill-only for now.
- NSA is specifically designed for [DeepSeek V3.2 DSA](https://lmsys.org/blog/2025-09-29-deepseek-V32/).

Note

For the KV4 FA4 scenario, FA4 requires using a different –decode-attention-backend to run. Except for trtllm\_mha being incompatible with FA4, all other decode backends behave as shown in the table.

Tip

Speculative decoding topk: `topk` is the number of draft tokens sampled per step from the draft model. `topk = 1` follows classic EAGLE; `topk > 1` explores multiple branches and requires backend support in both draft and verification paths.

Tip

Page size controls how many tokens are grouped into a KV cache block. For the prefix cache to take effect, the number of tokens must fill at least one complete page. For example, if your prompt is only 32 tokens and `page_size = 64`, it won’t fill a complete page and cannot be matched in the prefix cache (pages cannot be padded). With 65 tokens and `page_size = 64`, only the first page of 64 tokens will be cached and matched; the remaining 1 token is discarded. Use `page_size = 1` for maximum prefix reuse (token-level matching).

Many backends that do not natively operate on pages can emulate `page_size > 1` at the wrapper layer by expanding page tables to per-token indices. The “Page Size &gt; 1 (native)” column indicates true in-kernel paging. Some backends require fixed native page sizes and cannot be reduced/emulated differently: TRTLLM MHA (16/32/64), TRTLLM MLA (32/64), FlashMLA (64), Cutlass MLA (128), Ascend (128).

MLA page-size constraints:

- FlashInfer MLA: page\_size = 1.
- FlashMLA: page\_size = 64.
- Cutlass MLA: page\_size = 128.
- TRTLLM MLA: page\_size ∈ {32, 64}.

### Hybrid attention (different backends for prefill vs decode) (Experimental)[#](#hybrid-attention-different-backends-for-prefill-vs-decode-experimental "Link to this heading")

Warning

Hybrid attention is an experimental feature.

You can mix-and-match attention backends for prefill and decode. This is useful when one backend excels at prefill and another excels at decode. For the implementation details, please see `python/sglang/srt/layers/attention/hybrid_attn_backend.py`.

```
# Example: Prefill with FA4, Decode with TRTLLM MLA (Blackwell)
python3-msglang.launch_server\
--model-pathnvidia/DeepSeek-R1-FP4\
--tp8\
--attention-backendtrtllm_mla\
--moe-runner-backendflashinfer_trtllm\
--quantizationmodelopt_fp4\
--prefill-attention-backendfa4
```

#### Speculative decoding with hybrid attention[#](#speculative-decoding-with-hybrid-attention "Link to this heading")

Hybrid attention also works with speculative decoding. The backend used for draft decoding and target verification depends on `--speculative-attention-mode`:

- `--speculative-attention-mode decode` (recommended): draft/verify use the decode backend.
- `--speculative-attention-mode prefill` (default): draft/verify use the prefill backend.

Constraints when combining hybrid attention with speculative decoding:

- If any attention backend is `trtllm_mha`, speculative decoding supports only `--speculative-eagle-topk 1`.
- For paged MHA backends with `--page-size > 1` and `--speculative-eagle-topk > 1`, only `flashinfer` is supported.
- CUDA Graph: the decode backend is always captured; the prefill backend is captured only when `--speculative-attention-mode prefill`.

Tip

If you set only one of `--prefill-attention-backend` or `--decode-attention-backend`, the unspecified phase inherits `--attention-backend`. If both are specified and differ, SGLang automatically enables a hybrid wrapper to dispatch to the chosen backend per phase.

## Attention Backend Selection Guide (CUDA)[#](#attention-backend-selection-guide-cuda "Link to this heading")

If the `--attention-backend` argument is not specified, SGLang automatically selects the best backend based on the hardware (CUDA) and model architecture.

### Automatic Selection Logic[#](#automatic-selection-logic "Link to this heading")

**1. MHA Models (e.g., Llama, Qwen)**

- **Hopper (e.g., H100, H200)**: Defaults to `fa3` if using CUDA 12.3+ and the model configuration is supported.
- **Blackwell (e.g., B200)**: Defaults to `trtllm_mha`, unless using speculative decoding with `topk > 1`.
- **Other Architectures (Ampere, Ada, etc.)**: Defaults to `flashinfer` if available; otherwise falls back to `triton`.

**2. MLA Models (e.g., DeepSeek V3)**

- **Hopper**: Defaults to `fa3` (requires CUDA 12.3+).
- **Blackwell**: Defaults to `trtllm_mla`.
- **Other Architectures**: Defaults to `triton`.

## User Guide[#](#user-guide "Link to this heading")

### Launch Command for Different Attention Backends[#](#launch-command-for-different-attention-backends "Link to this heading")

- FlashInfer (Default for Non-Hopper Machines, e.g., A100, A40)

```
python3-msglang.launch_server\
--modelmeta-llama/Meta-Llama-3.1-8B-Instruct\
--attention-backendflashinfer
python3-msglang.launch_server\
--tp8\
--modeldeepseek-ai/DeepSeek-V3\
--attention-backendflashinfer\
--trust-remote-code
```

- FlashAttention 3 (Default for Hopper Machines, e.g., H100, H200, H20)

```
python3-msglang.launch_server\
--modelmeta-llama/Meta-Llama-3.1-8B-Instruct\
--attention-backendfa3
python3-msglang.launch_server\
--tp8\
--modeldeepseek-ai/DeepSeek-V3\
--trust-remote-code\
--attention-backendfa3
```

- Triton

```
python3-msglang.launch_server\
--modelmeta-llama/Meta-Llama-3.1-8B-Instruct\
--attention-backendtriton
python3-msglang.launch_server\
--tp8\
--modeldeepseek-ai/DeepSeek-V3\
--attention-backendtriton\
--trust-remote-code
```

- FlashMLA

```
python3-msglang.launch_server\
--tp8\
--modeldeepseek-ai/DeepSeek-R1\
--attention-backendflashmla\
--trust-remote-code
python3-msglang.launch_server\
--tp8\
--modeldeepseek-ai/DeepSeek-R1\
--attention-backendflashmla\
--kv-cache-dtypefp8_e4m3\
--trust-remote-code
```

- TRTLLM MLA (Optimized for Blackwell Architecture, e.g., B200)

```
python3-msglang.launch_server\
--tp8\
--modeldeepseek-ai/DeepSeek-R1\
--attention-backendtrtllm_mla\
--trust-remote-code
```

- TRTLLM MLA with FP8 KV Cache (Higher concurrency, lower memory footprint)

```
python3-msglang.launch_server\
--tp8\
--modeldeepseek-ai/DeepSeek-R1\
--attention-backendtrtllm_mla\
--kv-cache-dtypefp8_e4m3\
--trust-remote-code
```

- FlashAttention 4 (MHA & MLA)

```
python3-msglang.launch_server\
--tp8\
--modeldeepseek-ai/DeepSeek-R1\
--prefill-attention-backendfa4\
--trust-remote-code
```

- Cutlass MLA

```
python3-msglang.launch_server\
--tp8\
--modeldeepseek-ai/DeepSeek-R1\
--attention-backendcutlass_mla\
--trust-remote-code
```

- Ascend

```
python3-msglang.launch_server\
--modelmeta-llama/Meta-Llama-3.1-8B-Instruct\
--attention-backendascend
```

- Intel XPU

```
python3-msglang.launch_server\
--modelmeta-llama/Meta-Llama-3.1-8B-Instruct\
--attention-backendintel_xpu
```

- Wave

```
python3-msglang.launch_server\
--modelmeta-llama/Meta-Llama-3.1-8B-Instruct\
--attention-backendwave
```

- FlexAttention

```
python3-msglang.launch_server\
--modelmeta-llama/Meta-Llama-3.1-8B-Instruct\
--attention-backendflex_attention
```

- Dual Chunk FlashAttention

```
python3-msglang.launch_server\
--modelQwen/Qwen2.5-14B-Instruct-1M\
--attention-backenddual_chunk_flash_attn
```

- Torch Native

```
python3-msglang.launch_server\
--modelmeta-llama/Meta-Llama-3.1-8B-Instruct\
--attention-backendtorch_native
```

## Steps to add a new attention backend[#](#steps-to-add-a-new-attention-backend "Link to this heading")

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