---
title: Online Quantization - vLLM
url: https://docs.vllm.ai/en/latest/features/quantization/online/
source: sitemap
fetched_at: 2026-05-07T21:14:32.967786922-03:00
rendered_js: false
word_count: 214
summary: This document explains how to perform online quantization in vLLM, enabling the conversion of model weights to lower precision formats like FP8 during loading without needing pre-quantized data.
tags:
    - vllm
    - quantization
    - fp8
    - mxfp8
    - model-optimization
    - llm-inference
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/features/quantization/online.md "Edit this page")

Online quantization lets you take a BF16/FP16 model and quantize its Linear and MoE weights to lower precision (such as FP8) at load time, without needing a pre-quantized checkpoint or calibration data. Weights are converted during model loading and activations are dynamically scaled during each forward pass.

## Quick Start[¶](#quick-start "Permanent link")

Pass a scheme name to the `quantization` parameter:

```
fromvllmimport LLM

# Per-tensor FP8 quantization (one scale per weight tensor)
llm = LLM("meta-llama/Llama-3.1-8B", quantization="fp8_per_tensor")

# Per-block FP8 quantization (128x128 block scaling for weights and 1x128 block scaling for activations)
llm = LLM("meta-llama/Llama-3.1-8B", quantization="fp8_per_block")

# MXFP8 quantization for weights and activations
llm = LLM("meta-llama/Llama-3.1-8B", quantization="mxfp8")
```

Or with the CLI:

```
vllmservemeta-llama/Llama-3.1-8B--quantizationfp8_per_tensor
vllmservemeta-llama/Llama-3.1-8B--quantizationfp8_per_block
vllmservemeta-llama/Llama-3.1-8B--quantizationmxfp8
```

## Supported Schemes[¶](#supported-schemes "Permanent link")

Scheme Weight recipe Activation recipe Notes `fp8_per_tensor` fp8\_e4m3 data, fp32 per-tensor scale fp8\_e4m3 data, fp32 per-tensor scale On some GPUs (Ada, Hopper) linear activations use per-token scaling for better performance `fp8_per_block` fp8\_e4m3 data, fp32 per-128x128-block scale fp8\_e4m3 data, fp32 per-1x128-block scale `mxfp8` fp8\_e4m3 data, e8m0 per-1x32-block scale fp8\_e4m3 data, e8m0 per-1x32-block scale Requires SM 100+ (Blackwell or newer) for w8a8, other GPUs use a w8a16 fallback

## Advanced Configuration[¶](#advanced-configuration "Permanent link")

For fine-grained control, use a `quantization_config` dictionary.

### Separate Schemes for Dense and MoE Layers[¶](#separate-schemes-for-dense-and-moe-layers "Permanent link")

You can apply different quantization schemes to dense linear layers and MoE expert layers:

```
fromvllmimport LLM

llm = LLM(
    "ibm-granite/granite-3.0-1b-a400m-base",
    quantization="fp8_per_tensor",
    quantization_config={
        "linear_scheme_override": "fp8_per_block",
    },
)
```

Or,

```
fromvllmimport LLM

llm = LLM(
    "ibm-granite/granite-3.0-1b-a400m-base",
    quantization="fp8_per_tensor",
    quantization_config={
        "moe_scheme_override": "fp8_per_block",
    },
)
```

### Excluding Layers from Quantization[¶](#excluding-layers-from-quantization "Permanent link")

Use the `ignore` parameter to skip specific layers. It accepts exact layer names and regex patterns (prefixed with `re:`):

```
fromvllmimport LLM

llm = LLM(
    "ibm-granite/granite-3.0-1b-a400m-base",
    quantization="fp8_per_tensor",
    quantization_config={
        "ignore": [
            # exact layer name
            "model.layers.1.self_attn.o_proj",
            # regex: skip all QKV projections
            "re:.*[qkv]_proj",
        ],
    },
)
```

Note

For fused layers (e.g., `qkv_proj` which fuses `q_proj`, `k_proj`, `v_proj`), the ignore pattern must match the **unfused** shard names (`q_proj`, `k_proj`, `v_proj`), not the fused name.