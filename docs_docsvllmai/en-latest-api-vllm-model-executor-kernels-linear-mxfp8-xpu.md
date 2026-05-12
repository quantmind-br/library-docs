---
title: xpu - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/mxfp8/xpu/
source: sitemap
fetched_at: 2026-05-07T21:23:34.246161803-03:00
rendered_js: false
word_count: 0
summary: This document defines the implementation of MXFP8 linear kernels for XPU devices, providing methods for compatibility verification, weight processing, and performing quantized GEMM operations.
tags:
    - xpu
    - mxfp8
    - gemm
    - linear-kernel
    - quantization
    - pytorch-extension
category: api
---

```
classXPUMxFp8LinearKernel(Mxfp8LinearKernel):
"""MXFP8 W8A8 GEMM on XPU."""

    @classmethod
    defis_supported(
        cls, compute_capability: int | None = None
    ) -> tuple[bool, str | None]:
        if not current_platform.is_xpu():
            return False, "XPUMxFp8 only support on XPU"
        return True, None

    @classmethod
    defcan_implement(cls, c: Mxfp8LinearLayerConfig) -> tuple[bool, str | None]:
        return True, None

    defprocess_weights_after_loading(self, layer: torch.nn.Module) -> None:
        weight_scale = layer.weight_scale.view(torch.float8_e8m0fnu)
        weight_scale = weight_scale.t().contiguous()
        replace_parameter(layer, "weight", layer.weight.t())
        replace_parameter(layer, "weight_scale", weight_scale.data)

    defapply_weights(
        self,
        layer: torch.nn.Module,
        x: torch.Tensor,
        bias: torch.Tensor | None = None,
    ) -> torch.Tensor:
        out_dtype = x.dtype
        x_fp8, x_scale = quant_mxfp8(x)
        return torch.ops._xpu_C.fp8_gemm(
            x_fp8,
            layer.weight,
            out_dtype,
            x_scale,
            layer.weight_scale,
            bias,
        )
```