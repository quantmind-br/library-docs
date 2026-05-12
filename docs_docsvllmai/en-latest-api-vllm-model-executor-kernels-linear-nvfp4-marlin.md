---
title: marlin - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/nvfp4/marlin/
source: sitemap
fetched_at: 2026-05-07T21:23:40.879534375-03:00
rendered_js: false
word_count: 16
summary: This document defines the MarlinNvFp4LinearKernel class, which facilitates weight-only FP4 quantization and GEMM operations for neural network layers within the vLLM framework.
tags:
    - vllm
    - fp4-quantization
    - marlin-kernel
    - gemm-operations
    - neural-network-kernels
    - gpu-acceleration
category: reference
---

## vllm.model\_executor.kernels.linear.nvfp4.marlin [¶](#vllm.model_executor.kernels.linear.nvfp4.marlin "Permanent link")

## MarlinNvFp4LinearKernel [¶](#vllm.model_executor.kernels.linear.nvfp4.marlin.MarlinNvFp4LinearKernel "Permanent link")

Bases: `NvFp4LinearKernel`

NVFP4 weight-only GEMM via Marlin (W4A16).

Source code in `vllm/model_executor/kernels/linear/nvfp4/marlin.py`

```
classMarlinNvFp4LinearKernel(NvFp4LinearKernel):
"""NVFP4 weight-only GEMM via Marlin (W4A16)."""

    @classmethod
    defis_supported(
        cls, compute_capability: int | None = None
    ) -> tuple[bool, str | None]:
        if is_fp4_marlin_supported():
            return True, None
        return False, "Marlin FP4 not available"

    @classmethod
    defcan_implement(cls, config: NvFp4LinearLayerConfig) -> tuple[bool, str | None]:
        return True, None

    defprocess_weights_after_loading(self, layer: torch.nn.Module) -> None:
        logger.warning_once(
            "Your GPU does not have native support for FP4 computation but "
            "FP4 quantization is being used. Weight-only FP4 compression "
            "will be used leveraging the Marlin kernel. This may degrade "
            "performance for compute-heavy workloads."
        )
        prepare_fp4_layer_for_marlin(layer)

    defapply_weights(
        self,
        layer: torch.nn.Module,
        x: torch.Tensor,
        bias: torch.Tensor | None = None,
    ) -> torch.Tensor:
        return apply_fp4_marlin_linear(
            input=x,
            weight=layer.weight,
            weight_scale=layer.weight_scale,
            weight_global_scale=layer.weight_global_scale,
            workspace=layer.workspace,
            size_n=layer.output_size_per_partition,
            size_k=layer.input_size_per_partition,
            bias=bias,
        )
```