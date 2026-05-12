---
title: NixlConnector Compatibility Matrix - vLLM
url: https://docs.vllm.ai/en/latest/features/nixl_connector_compatibility/
source: sitemap
fetched_at: 2026-05-07T21:14:15.338730376-03:00
rendered_js: false
word_count: 538
summary: This document outlines the feature compatibility matrix and configuration requirements for using the NixlConnector with disaggregated prefilling in vLLM.
tags:
    - nixl-connector
    - disaggregated-prefilling
    - kv-cache
    - compatibility-matrix
    - tensor-parallelism
    - model-architecture
category: reference
---

[](https://github.com/vllm-project/vllm/edit/main/docs/features/nixl_connector_compatibility.md "Edit this page")

This page documents the feature compatibility of **disaggregated prefilling with the NixlConnector**. For general usage instructions, see the [NixlConnector Usage Guide](https://docs.vllm.ai/en/latest/features/nixl_connector_usage/). For an overview of disaggregated prefilling, see [Disaggregated Prefilling](https://docs.vllm.ai/en/latest/features/disagg_prefill/).

Note

This page reflects the current state of the codebase and is subject to change as features evolve. Entries marked 🟠 or ❌ may link to tracking issues. See the [NIXL connector roadmap](https://github.com/vllm-project/vllm/issues/33702) for upcoming feature development.

**Legend:**

- ✅ = Fully supported
- 🟠 = Partial support (see footnotes)
- ❌ = Not supported
- ❔ = Unknown / not yet validated
- 🚧 = Work in progress

## Model Architecture x Capability[¶](#model-architecture-x-capability "Permanent link")

Model type Basic PD Spec Decode Hetero TP Cross-layer blocks SWA Host buffer Hetero block size Dense Transformers ✅ ✅1 ✅ ✅2 ✅ ✅ 🟠3 MLA (e.g. DeepSeek-V2/V3) ✅ ✅1 🟠4 ✅2 ✅ ✅ 🟠3 Sparse MLA (e.g. DeepSeek-V3.2) ✅ ✅1 🟠4 ✅2 ✅ ✅ 🟠3 Hybrid SSM / Mamba ✅ ❔ 🚧5 ❌ ✅ ✅ ❌6 MoE ✅ ✅1 ✅ ✅2 ✅ ✅ 🟠3 Multimodal ❔ ❔ ❔ ❔ ❔ ❔ ❔ Encoder-Decoder ❌ ❌ ❌ ❌ ❌ ❌ ❌

1 P and D instances must use the same speculation configuration.

2 Requires `FLASH_ATTN` or `FLASHINFER` backend **and** `HND` KV cache layout. Enable via `--kv-transfer-config '{"kv_connector_extra_config": {"enable_cross_layers_blocks": "True"}}'`.

3 Supported only when HMA is **not** required (i.e., non-hybrid models). Block IDs are remapped automatically. Only P block size &lt; D block size is supported.

4 MLA KV cache is replicated across TP workers, so heterogeneous TP works but there is no head-splitting. When P TP &gt; D TP, only a single read is executed (redundant ranks are skipped). D TP &gt; P TP also works.

5 Hybrid SSM (Mamba) models require **homogeneous TP** (`P TP == D TP`). Heterogeneous TP is not yet supported for Mamba layers.

6 HMA (required by hybrid models) does not support different remote block sizes.

## Configuration Notes[¶](#configuration-notes "Permanent link")

### What must match between P and D[¶](#what-must-match-between-p-and-d "Permanent link")

By default, a **compatibility hash** is checked during handshake. P and D instances must agree on:

- vLLM version and NIXL connector version
- Model (architecture, dtype, number of KV heads, head size, number of hidden layers)
- Attention backend
- KV cache dtype (`cache_dtype`)

Warning

Disable the hash check with `--kv-transfer-config '{"kv_connector_extra_config": {"enforce_handshake_compat": false}}'` at your own risk.

### What can safely differ between P and D[¶](#what-can-safely-differ-between-p-and-d "Permanent link")

- `tensor-parallel-size` (heterogeneous TP, subject to model restrictions above)
- `block-size` (heterogeneous block size, subject to restrictions above)
- Number of KV cache blocks (determined by available memory on each instance)

### KV cache layout[¶](#kv-cache-layout "Permanent link")

- NixlConnector defaults to **`HND`** layout for optimal transfer performance (non-MLA models).
- `NHD` layout is supported but does **not** allow heterogeneous TP head splitting.
- Experimental `HND` ↔ `NHD` permute: enable via `--kv-transfer-config '{"enable_permute_local_kv": true}'`. Not supported with HMA.

### Quantized KV cache[¶](#quantized-kv-cache "Permanent link")

[Quantized KV cache](https://docs.vllm.ai/en/latest/features/quantization/quantized_kvcache/) (e.g., FP8) requires both P and D instances to use the **same** `cache_dtype`. Mismatched cache dtypes will fail the compatibility hash check during handshake.

- **Static quantization** (scales loaded from checkpoint): ✅ Supported. Scales are loaded independently by each instance from the model checkpoint.
- **Dynamic quantization** (scales computed at runtime): ❌ Not supported. Per-block scales are not transferred alongside KV cache data.
- **Packed-layout scales** (scales stored inline with weights): ✅ Supported. Scales are transferred together with the KV cache blocks.