---
title: emulation - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/nvfp4/emulation/
source: sitemap
fetched_at: 2026-05-07T21:23:38.127852687-03:00
rendered_js: false
word_count: 31
summary: This document describes the software emulation fallback kernel used for NVFP4 operations, providing a method to execute matrix multiplication when native hardware support is unavailable.
tags:
    - nvfp4
    - linear-kernel
    - software-emulation
    - vllm-internals
    - cuda-fallback
category: reference
---

## vllm.model\_executor.kernels.linear.nvfp4.emulation [¶](#vllm.model_executor.kernels.linear.nvfp4.emulation "Permanent link")

## EmulationNvFp4LinearKernel [¶](#vllm.model_executor.kernels.linear.nvfp4.emulation.EmulationNvFp4LinearKernel "Permanent link")

Bases: `NvFp4LinearKernel`

Software emulation fallback for NVFP4 (dequant → BF16 matmul).

Source code in `vllm/model_executor/kernels/linear/nvfp4/emulation.py`

```
classEmulationNvFp4LinearKernel(NvFp4LinearKernel):
"""Software emulation fallback for NVFP4 (dequant → BF16 matmul)."""

    @classmethod
    defis_supported(
        cls, compute_capability: int | None = None
    ) -> tuple[bool, str | None]:
        # Always available as a last-resort fallback.
        return True, None

    @classmethod
    defcan_implement(cls, config: NvFp4LinearLayerConfig) -> tuple[bool, str | None]:
        return True, None

    defprocess_weights_after_loading(self, layer: torch.nn.Module) -> None:
        # Move the E2M1 lookup table to the device now, because
        # `.to(device)` is not allowed during CUDA graph capture.
        kE2M1ToFloat_handle.val = kE2M1ToFloat_handle.val.to(layer.weight.device)

    defapply_weights(
        self,
        layer: torch.nn.Module,
        x: torch.Tensor,
        bias: torch.Tensor | None = None,
    ) -> torch.Tensor:
        out = run_nvfp4_emulations(
            x=x,
            input_global_scale=layer.input_global_scale_inv,
            weight=layer.weight,
            weight_scale_swizzled=layer.weight_scale,
            weight_global_scale=layer.weight_global_scale,
            swizzle=False,
        )
        if bias is not None:
            out = out + bias
        return out
```