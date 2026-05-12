---
title: ops - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/attention/ops/
source: sitemap
fetched_at: 2026-05-07T21:39:48.224211455-03:00
rendered_js: false
word_count: 65
summary: This document provides an overview of available modules and Triton-based kernel operations for attention mechanisms and memory-efficient decoding processes.
tags:
    - triton-kernels
    - attention-mechanisms
    - memory-efficient-decoding
    - gpu-acceleration
    - module-reference
category: reference
---

Modules:

Name Description `common` `dcp_alltoall`

DCP All-to-All communication backend for attention.

`deepseek_v4_ops` `flashmla` `merge_attn_states` `rocm_aiter_mla_sparse` `triton_attention_helpers`

Shared `@triton.jit` helpers used by the unified attention kernel

`triton_decode_attention`

Memory-efficient attention for decoding.

`triton_prefill_attention`

Memory-efficient attention for prefill.

`triton_reshape_and_cache_flash` `triton_turboquant_decode`

Triton fused TurboQuant decode attention.

`triton_turboquant_store`

Fused Triton kernels for TurboQuant KV store.

`triton_unified_attention` `vit_attn_wrappers`

This file contains ops for ViT attention to be compatible with torch.compile

`xpu_mla_sparse`