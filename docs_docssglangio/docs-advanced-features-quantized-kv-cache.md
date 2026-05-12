---
title: Quantized KV Cache - SGLang Documentation
url: https://docs.sglang.io/docs/advanced_features/quantized_kv_cache
source: sitemap
fetched_at: 2026-05-11T05:49:30.13873576-03:00
rendered_js: false
word_count: 556
summary: This document explains how to optimize LLM memory usage by implementing quantized key-value cache using FP8 and FP4 formats in SGLang. It details configuration methods, scaling factor requirements, and the trade-offs between memory savings and model accuracy.
tags:
    - kv-cache
    - quantization
    - llm-optimization
    - memory-management
    - fp8
    - fp4
    - sglang
category: concept
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

Quantized KV cache reduces the memory footprint of key-value cache storage by using lower-precision data types (FP8 or FP4) instead of the default model precision in BF16. During autoregressive generation, LLMs cache previously computed key-value pairs to avoid redundant calculations. The KV cache typically consumes a significant portion of GPU memory, especially for long sequences. Quantized KV cache is a memory optimization technique that primarily benefits throughput by allowing more tokens to be cached, but may introduce minimal accuracy degradation depending on the quantization format used.

## Supported Formats

SGLang supports the following quantized KV cache formats:

### FP8 Format

[OCP (Open Compute Project)](https://www.opencompute.org) specifies two common 8-bit floating point formats:

- **E5M2** (5 exponent bits, 2 mantissa bits): Larger dynamic range (±57344.0), lower precision
- **E4M3** (4 exponent bits, 3 mantissa bits): Higher precision, smaller dynamic range (±240.0)

### FP4 Format

[OCP (Open Compute Project)](https://www.opencompute.org) specifies MXFP4 (Microscaling FP4), a 4-bit floating-point format:

- **E2M1** (1 sign bit, 2 exponent bits, 1 mantissa bit): Uses block-based microscaling where tensors are divided into blocks of consecutive elements, with each block sharing a single 8-bit exponential scaling factor. While OCP specifies blocks of 32 elements, SGLang’s current implementation uses blocks of 16 elements for KV cache quantization.

## Usage

### Enabling Quantized KV Cache

To enable quantized KV cache, use the `--kv-cache-dtype` argument when launching the server:

```
# Enable FP8 E5M2 KV cache
python3 -m sglang.launch_server \
    --model-path deepseek-ai/DeepSeek-R1-0528 \
    --kv-cache-dtype fp8_e5m2 \

# Enable FP8 E4M3 KV cache
python3 -m sglang.launch_server \
    --model-path deepseek-ai/DeepSeek-R1-0528 \
    --kv-cache-dtype fp8_e4m3 \

# Enable FP4 E2M1 KV cache
python3 -m sglang.launch_server \
    --model-path nvidia/DeepSeek-R1-0528-NVFP4 \
    --kv-cache-dtype fp4_e2m1 \
```

### Scaling Factors

FP8 quantization requires scaling factors to properly quantize and dequantize the KV cache.

Scaling factors can be:

- **Loaded from checkpoints**: Pre-quantized models (e.g., ModelOpt) may include `k_scale` and `v_scale` parameters that are automatically loaded
- **Provided via JSON**: Supply scaling factors via `--quantization-param-path`.

The JSON file should follow this format:

```
{
  "kv_cache": {
    "dtype": "float8_e4m3fn",
    "scaling_factor": {
      "0": {
        "0": 1.0,
        "1": 1.0
      }
    }
  }
}
```

Where the outer keys in `scaling_factor` are tensor parallel ranks and inner keys are layer indices.

## Performance Considerations

### Memory Savings

Quantized KV cache provides significant memory savings:

- **BF16 → FP4**: Supports approximately 3.56× more tokens than BF16 (accounting for scaling factor overhead)

This enables longer context lengths or more concurrent requests within the same memory budget.

### Accuracy Impact

#### FP8 Accuracy

FP8 E4M3 quantization typically introduces minimal accuracy degradation. The impact depends on model architecture, sequence length, and quantization format (generally, E4M3 has better accuracy than E5M2).

#### FP4 Accuracy

FP4 (MXFP4) quantization provides significant memory savings with varying accuracy impact depending on model size and dataset complexity. Preliminary accuracy test results from [PR #10078](https://github.com/sgl-project/sglang/pull/10078) (MLA) and [PR #12612](https://github.com/sgl-project/sglang/pull/12612) (MHA) show: **Large Models (e.g., Qwen3-235B-A22B, DeepSeek-R1-0528)** On large-scale models, FP4 maintains accuracy close to FP8/BF16, especially on simpler datasets:

ModelDatasetKV16KV8 (FP8 E4M3)KV4 (FP4 E2M1)Qwen3-235B-A22Bgsm8k0.91680.91810.9186Qwen3-235B-A22Baime250.77330.73330.6000Qwen3-235B-A22Bgpqa\_diamond0.70100.68990.6778DeepSeek-R1-0528gsm8k0.91570.91540.9124DeepSeek-R1-0528aime250.50670.49340.4000DeepSeek-R1-0528gpqa\_diamond0.77070.76970.7273

**Smaller Models (e.g., GPT-OSS-120B)** On smaller models, FP4 shows more pronounced accuracy drops, particularly on challenging datasets:

ModelDatasetKV16KV8 (FP8 E4M3)KV4 (FP4 E2M1)GPT-OSS-120Bgsm8k0.91610.91630.9152GPT-OSS-120Baime250.75330.76670.3533GPT-OSS-120Bgpqa\_diamond0.50810.54340.3202

**Key Observations:**

- **Simple datasets (e.g., gsm8k)**: FP4 maintains accuracy close to FP8/BF16 across model sizes
- **Model size matters**: Large models (200B+ parameters) generally tolerate FP4 quantization better than smaller models
- **Context length**: Accuracy degradation may be more pronounced in long-context scenarios, as the accumulation of the quantization error may become significant.

## Best Practices

- **Use pre-quantized models**: Prefer models quantized offline with scaling factors included in the checkpoint.
- **Choose the right format**: Use `fp8_e4m3` for better accuracy (recommended), `fp8_e5m2` for larger dynamic range, or `fp4_e2m1` for maximum memory savings (experimental)
- **Check backend compatibility**: Verify that your chosen attention backend supports quantized KV cache