---
title: backends - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/attention/backends/
source: sitemap
fetched_at: 2026-05-07T21:39:04.156708639-03:00
rendered_js: false
word_count: 77
summary: This document lists the available attention module backends supported by the vLLM system, providing a brief description of their specific functionality or implementation.
tags:
    - vllm
    - attention-mechanisms
    - model-architecture
    - gpu-acceleration
    - backend-modules
    - deep-learning
category: reference
---

Modules:

Name Description `cpu_attn` `fa_utils` `flash_attn`

Attention layer with FlashAttention.

`flash_attn_diffkv`

Attention layer with FlashAttention.

`flashinfer`

Attention layer with FlashInfer.

`flex_attention`

Attention layer with FlexAttention.

`gdn_attn`

Backend for GatedDeltaNet attention.

`mamba2_attn` `mamba_attn` `mla` `registry`

Attention backend registry

`rocm_aiter_fa`

Attention layer with AiterFlashAttention.

`rocm_aiter_unified_attn`

Attention layer with PagedAttention and Triton prefix prefill.

`rocm_attn`

Attention layer with PagedAttention and Triton prefix prefill.

`tree_attn`

Attention layer with TreeAttention.

`triton_attn`

High-Performance Triton-only Attention layer.

`turboquant_attn`

TurboQuant attention backend for vLLM.

`utils`