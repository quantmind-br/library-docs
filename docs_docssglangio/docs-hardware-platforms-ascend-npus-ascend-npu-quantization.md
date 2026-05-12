---
title: Quantization on Ascend - SGLang Documentation
url: https://docs.sglang.io/docs/hardware-platforms/ascend-npus/ascend_npu_quantization
source: sitemap
fetched_at: 2026-05-11T05:48:35.790686054-03:00
rendered_js: false
word_count: 258
summary: This document outlines the support for various quantization methods in SGLang when deploying models on Ascend NPU hardware, including specific compatibility matrices for different layer types.
tags:
    - quantization
    - ascend-npu
    - model-deployment
    - gguf
    - gptq
    - awq
    - model-optimization
category: reference
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

To load already quantized models, simply load the model weights and config. Again, if the model has been quantized offline, there’s no need to add `--quantization` argument when starting the engine. The quantization method will be automatically parsed from the downloaded `quant_model_description.json` or `config.json` config. SGLang support **mix-bits** quantization (independently defines and loads each layer depending on the type of quantification specified in the `quant_model_description'.json`). [Advanced mix-bits for MoE](https://github.com/sgl-project/sglang/pull/17361) in progress, will add independent quantization determination for the w13 (up-gate) and w2 (down) layers. [ModelSlim on Ascend support](https://github.com/sgl-project/sglang/pull/14504)

Quantization schemeLayer typeA2 SupportedA3 SupportedA5 SupportedDiffusion modelsW4A4 dynamicLinear**√****√****TBD****√**W8A8 staticLinear**√****√****TBD****√**W8A8 dynamicLinear**√****√****TBD****√**[MXFP8](https://github.com/sgl-project/sglang/pull/20922)Linear**x****x****√****√**W4A4 dynamicMoE**√****√****TBD****x**W4A8 dynamicMoE**√****√****TBD****x**W8A8 dynamicMoE**√****√****TBD****x**[MXFP8](https://github.com/sgl-project/sglang/pull/20922)MoE**x****x****WIP****x**

[AWQ on Ascend support](https://github.com/sgl-project/sglang/pull/10158):

Quantization schemeLayer typeA2 SupportedA3 SupportedA5 SupportedW4A16Linear**√****√****TBD**W8A16Linear**√****√****TBD**W4A16MoE**√****√****TBD**

GPTQ on Ascend support

Quantization schemeLayer typeA2 SupportedA3 SupportedA5 Supported[W4A16](https://github.com/sgl-project/sglang/pull/15203)Linear**√****√****TBD**[W8A16](https://github.com/sgl-project/sglang/pull/15203)Linear**√****√****TBD**[W4A16 MOE](https://github.com/sgl-project/sglang/pull/16364)MoE**√****√****TBD**[W8A16 MOE](https://github.com/sgl-project/sglang/pull/16364)MoE**√****√****TBD**

[Auto-round on Ascend support](https://github.com/sgl-project/sglang/pull/16699)

Quantization schemeLayer typeA2 SupportedA3 SupportedA5 SupportedW4A16Linear**√****√****TBD**W8A16Linear**√****√****TBD**W4A16MoE**√****√****TBD**W8A16MoE**√****√****TBD**

Compressed-tensors (LLM Compressor) on Ascend support:

Quantization schemeLayer typeA2 SupportedA3 SupportedA5 Supported[W8A8 dynamic](https://github.com/sgl-project/sglang/pull/14504)Linear**√****√****TBD**[W4A8 dynamic with/without activation clip](https://github.com/sgl-project/sglang/pull/14736)MoE**√****√****TBD**[W4A16 MOE](https://github.com/sgl-project/sglang/pull/12759)MoE**√****√****TBD**[W8A8 dynamic](https://github.com/sgl-project/sglang/pull/14504)MoE**√****√****TBD**

[GGUF on Ascend support](https://github.com/sgl-project/sglang/pull/17883)

Quantization typeLayer typeA2 SupportedA3 SupportedA5 SupportedAll GGUF types (standard, K-quant)Linear**√****√****TBD**All GGUF types (standard, K-quant)MoE**√****√****TBD**

**Usage Examples:**

- Dense model (e.g. Qwen3-14B-Q4\_K\_M.gguf):

```
python3 -m sglang.launch_server \
    --model-path Qwen3-14B-Q4_K_M.gguf \
    --device npu --attention-backend ascend \
    --host 0.0.0.0 --port 30000 \
    --mem-fraction-static 0.7 --tp-size 2
```

- MoE model (e.g. Qwen3-30B-A3B-Q4\_K\_M.gguf):

```
python3 -m sglang.launch_server \
    --model-path Qwen3-30B-A3B-Q4_K_M.gguf \
    --device npu --attention-backend ascend \
    --host 0.0.0.0 --port 30000 \
    --mem-fraction-static 0.8 --tp-size 2
```

> **Implementation Notes:**
> 
> - GGUF weights are pre-dequantized to FP16/BF16 during model loading on CPU, then transferred to NPU for inference. This trades higher memory usage for faster runtime performance (no per-forward-pass dequantization overhead).
> - MoE layers use `npu_grouped_matmul` and `npu_moe_init_routing` / `npu_moe_finalize_routing` for high-performance expert computation.
> - TP (tensor parallelism) sharding is supported for both dense and MoE GGUF models.