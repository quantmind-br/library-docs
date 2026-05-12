---
title: LLM Compressor - vLLM
url: https://docs.vllm.ai/en/latest/features/quantization/llm_compressor/
source: sitemap
fetched_at: 2026-05-07T21:14:30.952296813-03:00
rendered_js: false
word_count: 235
summary: This document introduces LLM Compressor, a library designed to optimize large language models for vLLM deployment through various quantization techniques to reduce memory usage and improve inference speed.
tags:
    - llm-quantization
    - model-optimization
    - vllm-integration
    - inference-acceleration
    - memory-optimization
    - fp8-quantization
category: concept
---

[](https://github.com/vllm-project/vllm/edit/main/docs/features/quantization/llm_compressor.md "Edit this page")

[LLM Compressor](https://docs.vllm.ai/projects/llm-compressor/en/latest/) is a library for optimizing models for deployment with vLLM. It provides a comprehensive set of quantization algorithms, including support for techniques such as FP4, FP8, INT8, and INT4 quantization.

## Why use LLM Compressor?[¶](#why-use-llm-compressor "Permanent link")

Modern LLMs often contain billions of parameters stored in 16-bit or 32-bit floating point, requiring substantial GPU memory and limiting deployment options. Quantization lowers memory requirements while maintaining inference output quality by reducing the precision of model weights and activations to smaller data types.

LLM Compressor provides the following benefits:

- **Reduced memory footprint**: Run larger models on smaller GPUs.
- **Lower inference costs**: Serve more concurrent users per GPU, directly reducing the cost per query in production deployments.
- **Faster inference**: Smaller data types mean less memory bandwidth consumed, which often translates to higher throughput, especially for memory-bound workloads.

LLM Compressor handles the complexity of quantization, calibration, and format conversion, producing models ready for immediate use with vLLM.

## Key features[¶](#key-features "Permanent link")

- **Multiple Quantization Algorithms**: Support for AWQ, GPTQ, AutoRound, and Round-to-Nearest. Also includes support for QuIP and SpinQuant-style transforms as well as KV cache and attention quantization.
- **Multiple Quantization Methods**: Support for FP8, INT8, INT4, NVFP4, MXFP4, and mixed-precision quantization
- **One-Shot Quantization**: Quantize models quickly with minimal calibration data
- **vLLM Integration**: Seamlessly deploy quantized models with vLLM using the compressed-tensors format
- **Hugging Face Compatibility**: Works with models from the Hugging Face Hub

## Resources[¶](#resources "Permanent link")

- [LLM Compressor examples](https://github.com/vllm-project/llm-compressor/tree/main/examples)
- [GitHub Repository](https://github.com/vllm-project/llm-compressor)