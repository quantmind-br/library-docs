---
title: torch.compile with Multimodal Encoders - vLLM
url: https://docs.vllm.ai/en/latest/design/torch_compile_multimodal/
source: sitemap
fetched_at: 2026-05-07T21:12:32.87291858-03:00
rendered_js: false
word_count: 573
summary: This document outlines the integration of torch.compile for multimodal encoders in vLLM, providing instructions for enabling compilation and troubleshooting performance or integration issues.
tags:
    - vllm
    - torch-compile
    - multimodal-models
    - performance-optimization
    - encoder-optimization
    - deep-learning
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/design/torch_compile_multimodal.md "Edit this page")

`torch.compile` can now be applied to multimodal encoders and miscellaneous nn modules in vLLM, including vision-language models like LLaMA 4, Qwen-VL, and similar encoder-based architectures.

This document covers the basics of how the `torch.compile` integration works for multimodal encoders in vLLM, as well as how to apply the decorator to new models to improve performance.

## Overview[¶](#overview "Permanent link")

We have recently enabled the `@support_torch_compile` decorator to work for multiple nn module components within a model type; this enables turning compile on for multimodal encoders, bringing performance improvements to additional components of the stack.

When applied to the vision block of [`Qwen2_5_vl`](https://github.com/vllm-project/vllm/pull/23207) we observe ~4.5% e2e perf improvements with some increase in compilation time

This feature is off by default, but can be enabled by setting `compile_mm_encoder: true` in the compilation config when models have the `@support_torch_compile` decorator.

## How Compilation Works for Multimodal Components[¶](#how-compilation-works-for-multimodal-components "Permanent link")

### APIs for Enablement[¶](#apis-for-enablement "Permanent link")

To compile a multimodal component such as an encoder, we follow the same mechanism as the LLM text backbone, with a few additional scaffoldings:

1. The `@support_torch_compile` decorator should include `enable_if=should_torch_compile_mm_encoder`. This will gate the compilation behind our `compile_mm_encoder` configuration
2. The `@support_torch_compile` decorator should include `is_encoder=True` for encoder components. This is needed for compile range integration (see Compile Range Integration). The decorator automatically uses the class name as the cache directory prefix, avoiding collisions between independently compiled sub-modules (e.g. vision encoder components vs the text backbone).

### CompilationConfig[¶](#compilationconfig "Permanent link")

With the exception of `compile_mm_encoder: true`, the multimodal encoder will inherit from the same compilation config as the text LLM. We may extend this for more configuration in the future.

## Applying torch.compile to a New Multimodal Model/Component[¶](#applying-torchcompile-to-a-new-multimodal-modelcomponent "Permanent link")

To apply `support_torch_compile` to a new general nn.Module, we advise following the same steps in [`debug_vllm_compile`](https://docs.vllm.ai/en/latest/design/debug_vllm_compile/); this includes:

1. Applying `support_torch_compile` on initially small modules (such as basic MLP layers), then raising to more general modules until one reaches a good performance tradeoff
2. Leveraging [`tlparse`](https://github.com/meta-pytorch/tlparse) to identify and eliminate the source of recompiles and graph breaks
3. Using `dynamic_arg_dims` and proper `dynamic_shapes_config` to handle dynamism.

### Common pitfalls[¶](#common-pitfalls "Permanent link")

## VllmBackend Feature Support[¶](#vllmbackend-feature-support "Permanent link")

### Compile ranges[¶](#compile-ranges "Permanent link")

The torch.compile integration will try to rely on max\_batch\_size to infer compilation ranges for dynamic shapes; however, for modules used in the encoder, this shape can be difficult to infer due to the unspecified range of shapes the encoder may see as input. Therefore, we rely on `is_encoder=True` in the `@support_torch_compile` decorator to alert torch.compile to the fact that this range cannot be inferred, and we default to the range (1, MAX\_INT).

Note

We may seek to tighten this range for better performance in the future

### Cudagraphs[¶](#cudagraphs "Permanent link")

We have not yet explored compilation for multimodal encoders with CUDAGraph integration; behavior is currently unspecified.

## Troubleshooting[¶](#troubleshooting "Permanent link")

### Graph Breaks in Vision Encoders[¶](#graph-breaks-in-vision-encoders "Permanent link")

Some vision encoder operations may cause graph breaks. To identify them:

```
TORCH_LOGS="+dynamo"vllmserve<MODEL>
```

Common causes of graph breaks in multimodal models:

- **Dynamic image sizes**: Use `dynamic_shapes_config` to handle variable resolutions
- **Untraceable operations**: Some operations (such as to\_list) may not be supported by Dynamo
- **Conditional processing**: Data-dependent branching based on image properties

### Compilation Errors[¶](#compilation-errors "Permanent link")

If compilation fails for a multimodal model:

1. **Disable and test**: First verify the model works without compilation:
   
   ```
   VLLM_TORCH_COMPILE_LEVEL=0vllmserve<model>--compilation-config='{"compile_mm_encoder":"false"}'
   ```
2. **Check logs**: Enable debug logging to see compilation details:
   
   ```
   VLLM_LOGGING_LEVEL=DEBUGvllmserve<model>--compilation-config='{"compile_mm_encoder":"true"}'
   ```
3. **Report issues**: If you find a bug, [open an issue on GitHub](https://github.com/vllm-project/vllm/issues/new/choose)

## See Also[¶](#see-also "Permanent link")

- [torch.compile Integration](https://docs.vllm.ai/en/latest/design/torch_compile/) - Core design document
- [Debugging torch.compile](https://docs.vllm.ai/en/latest/design/debug_vllm_compile/) - Detailed debugging guide
- [Multimodal Inputs](https://docs.vllm.ai/en/latest/features/multimodal_inputs/) - How to pass multimodal data
- [Disaggregated Encoder](https://docs.vllm.ai/en/latest/features/disagg_encoder/) - Scaling vision encoders
- [Supported Multimodal Models](https://docs.vllm.ai/en/latest/models/supported_models/#list-of-multimodal-language-models) - Model compatibility