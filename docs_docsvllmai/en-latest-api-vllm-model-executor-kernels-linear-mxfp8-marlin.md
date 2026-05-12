---
title: marlin - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/mxfp8/marlin/
source: sitemap
fetched_at: 2026-05-07T21:23:33.011304499-03:00
rendered_js: false
word_count: 16
summary: This document defines the MarlinMxfp8LinearKernel class, which provides an implementation for MXFP8 W8A16 matrix multiplication kernels within the vLLM framework for supported hardware.
tags:
    - vllm
    - marlin
    - mxfp8
    - quantization
    - kernel-execution
    - linear-layer
    - gpu-acceleration
category: reference
---

## vllm.model\_executor.kernels.linear.mxfp8.marlin [¶](#vllm.model_executor.kernels.linear.mxfp8.marlin "Permanent link")

## MarlinMxfp8LinearKernel [¶](#vllm.model_executor.kernels.linear.mxfp8.marlin.MarlinMxfp8LinearKernel "Permanent link")

Bases: `Mxfp8LinearKernel`

MXFP8 W8A16 GEMM via Marlin (SM80+).

Source code in `vllm/model_executor/kernels/linear/mxfp8/marlin.py`

```
classMarlinMxfp8LinearKernel(Mxfp8LinearKernel):
"""MXFP8 W8A16 GEMM via Marlin (SM80+)."""

    @classmethod
    defis_supported(
        cls, compute_capability: int | None = None
    ) -> tuple[bool, str | None]:
        fromvllm.model_executor.layers.quantization.utils.marlin_utils_fp8import (
            is_fp8_marlin_supported,
        )

        if is_fp8_marlin_supported():
            return True, None
        return False, "Marlin FP8 not available"

    @classmethod
    defcan_implement(cls, c: Mxfp8LinearLayerConfig) -> tuple[bool, str | None]:
        return True, None

    defprocess_weights_after_loading(self, layer: torch.nn.Module) -> None:
        fromvllm.model_executor.layers.quantization.utils.marlin_utils_fp8import (
            prepare_mxfp8_layer_for_marlin,
        )

        prepare_mxfp8_layer_for_marlin(layer)

    defapply_weights(
        self,
        layer: torch.nn.Module,
        x: torch.Tensor,
        bias: torch.Tensor | None = None,
    ) -> torch.Tensor:
        fromvllm.model_executor.layers.quantization.utils.marlin_utils_fp8import (
            apply_mxfp8_marlin_linear,
        )

        return apply_mxfp8_marlin_linear(
            input=x,
            weight=layer.weight,
            weight_scale=layer.weight_scale,
            workspace=layer.workspace,
            size_n=layer.output_size_per_partition,
            size_k=layer.input_size_per_partition,
            bias=bias,
        )
```