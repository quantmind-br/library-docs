---
title: Features - vLLM
url: https://docs.vllm.ai/en/latest/features/
source: sitemap
fetched_at: 2026-05-07T21:14:02.325546544-03:00
rendered_js: false
word_count: 399
summary: This document provides a compatibility matrix outlining the support status of various vLLM features when combined with other features or different hardware architectures.
tags:
    - vllm
    - compatibility-matrix
    - hardware-support
    - feature-compatibility
    - infrastructure-requirements
category: reference
---

[](https://github.com/vllm-project/vllm/edit/main/docs/features/README.md "Edit this page")

## Compatibility Matrix[¶](#compatibility-matrix "Permanent link")

The tables below show mutually exclusive features and the support on some hardware.

The symbols used have the following meanings:

- ✅ = Full compatibility
- 🟠 = Partial compatibility
- ❌ = No compatibility
- ❔ = Unknown or TBD

Note

Check the ❌ or 🟠 with links to see tracking issue for unsupported feature/hardware combination.

### Feature x Feature[¶](#feature-x-feature "Permanent link")

Feature [CP](https://docs.vllm.ai/en/latest/configuration/optimization/#chunked-prefill) [APC](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/) [LoRA](https://docs.vllm.ai/en/latest/features/lora/) [SD](https://docs.vllm.ai/en/latest/features/speculative_decoding/) CUDA graph [pooling](https://docs.vllm.ai/en/latest/models/pooling_models/) enc-dec logP prmpt logP async output multi-step mm best-of beam-search [prompt-embeds](https://docs.vllm.ai/en/latest/features/prompt_embeds/) [CP](https://docs.vllm.ai/en/latest/configuration/optimization/#chunked-prefill) ✅ [APC](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/) ✅ ✅ [LoRA](https://docs.vllm.ai/en/latest/features/lora/) ✅ ✅ ✅ [SD](https://docs.vllm.ai/en/latest/features/speculative_decoding/) ✅ ✅ ❌ ✅ CUDA graph ✅ ✅ ✅ ✅ ✅ [pooling](https://docs.vllm.ai/en/latest/models/pooling_models/) 🟠* 🟠* ✅ ❌ ✅ ✅ enc-dec ❌ [❌](https://github.com/vllm-project/vllm/issues/7366) ❌ [❌](https://github.com/vllm-project/vllm/issues/7366) ✅ ✅ ✅ logP ✅ ✅ ✅ ✅ ✅ ❌ ✅ ✅ prmpt logP ✅ ✅ ✅ ✅ ✅ ❌ ✅ ✅ ✅ async output ✅ ✅ ✅ ❌ ✅ ❌ ❌ ✅ ✅ ✅ multi-step ❌ ✅ ❌ ❌ ✅ ❌ ❌ ✅ ✅ ✅ ✅ [mm](https://docs.vllm.ai/en/latest/features/multimodal_inputs/) ✅ ✅ [🟠](https://github.com/vllm-project/vllm/pull/4194)^ ❔ ✅ ✅ ✅ ✅ ✅ ✅ ❔ ✅ best-of ✅ ✅ ✅ [❌](https://github.com/vllm-project/vllm/issues/6137) ✅ ❌ ✅ ✅ ✅ ❔ [❌](https://github.com/vllm-project/vllm/issues/7968) ✅ ✅ beam-search ✅ ✅ ✅ [❌](https://github.com/vllm-project/vllm/issues/6137) ✅ ❌ ✅ ✅ ✅ ❔ [❌](https://github.com/vllm-project/vllm/issues/7968) ❔ ✅ ✅ [prompt-embeds](https://docs.vllm.ai/en/latest/features/prompt_embeds/) ✅ ✅ ✅ ❌ ✅ ❌ ❌ ✅ ❌ ❔ ❔ ✅ ❔ ❔ ✅

\* Chunked prefill and prefix caching are only applicable to last-token or all pooling with causal attention.  
^ LoRA is only applicable to the language backbone of multimodal models.

### Feature x Hardware[¶](#feature-x-hardware "Permanent link")

Feature Volta Turing Ampere Ada Hopper CPU AMD Intel GPU [CP](https://docs.vllm.ai/en/latest/configuration/optimization/#chunked-prefill) [❌](https://github.com/vllm-project/vllm/issues/2729) ✅ ✅ ✅ ✅ ✅ ✅ ✅ [APC](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/) [❌](https://github.com/vllm-project/vllm/issues/3687) ✅ ✅ ✅ ✅ ✅ ✅ ✅ [LoRA](https://docs.vllm.ai/en/latest/features/lora/) ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ [SD](https://docs.vllm.ai/en/latest/features/speculative_decoding/) ✅ ✅ ✅ ✅ ✅ ❌ ✅ ✅ CUDA graph ✅ ✅ ✅ ✅ ✅ ❌ ✅ [❌](https://github.com/vllm-project/vllm/issues/26970) [pooling](https://docs.vllm.ai/en/latest/models/pooling_models/) ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ enc-dec ✅ ✅ ✅ ✅ ✅ ✅ ❌ ✅ [mm](https://docs.vllm.ai/en/latest/features/multimodal_inputs/) ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ [prompt-embeds](https://docs.vllm.ai/en/latest/features/prompt_embeds/) ✅ ✅ ✅ ✅ ✅ ✅ ❔ ✅ logP ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ prmpt logP ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ async output ✅ ✅ ✅ ✅ ✅ ❌ ❌ ✅ multi-step ✅ ✅ ✅ ✅ ✅ [❌](https://github.com/vllm-project/vllm/issues/8477) ✅ ✅ best-of ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅ beam-search ✅ ✅ ✅ ✅ ✅ ✅ ✅ ✅