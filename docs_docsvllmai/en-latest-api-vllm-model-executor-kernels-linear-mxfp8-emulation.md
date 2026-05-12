---
title: emulation - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/mxfp8/emulation/
source: sitemap
fetched_at: 2026-05-07T21:23:31.012240215-03:00
rendered_js: false
word_count: 18
summary: This document defines the EmulationMxfp8LinearKernel class, which provides a software fallback for processing MXFP8 weights by dequantizing them to BF16 format.
tags:
    - vllm
    - mxfp8
    - linear-kernel
    - quantization
    - software-emulation
    - neural-network-acceleration
category: reference
---

## vllm.model\_executor.kernels.linear.mxfp8.emulation [¶](#vllm.model_executor.kernels.linear.mxfp8.emulation "Permanent link")

## EmulationMxfp8LinearKernel [¶](#vllm.model_executor.kernels.linear.mxfp8.emulation.EmulationMxfp8LinearKernel "Permanent link")

Bases: `Mxfp8LinearKernel`

Software emulation fallback for MXFP8 (dequant to BF16).

Source code in `vllm/model_executor/kernels/linear/mxfp8/emulation.py`

```
classEmulationMxfp8LinearKernel(Mxfp8LinearKernel):
"""Software emulation fallback for MXFP8 (dequant to BF16)."""

    @classmethod
    defis_supported(
        cls, compute_capability: int | None = None
    ) -> tuple[bool, str | None]:
        return True, None

    @classmethod
    defcan_implement(cls, c: Mxfp8LinearLayerConfig) -> tuple[bool, str | None]:
        return True, None

    defprocess_weights_after_loading(self, layer: torch.nn.Module) -> None:
        weight = layer.weight.data  # [N, K]
        N, K = weight.shape
        scale_k = K // MXFP8_BLOCK_SIZE

        weight_scale = layer.weight_scale.data[:N, :scale_k].contiguous()

        layer.weight = Parameter(weight.contiguous(), requires_grad=False)
        layer.weight_scale = Parameter(weight_scale, requires_grad=False)

    defapply_weights(
        self,
        layer: torch.nn.Module,
        x: torch.Tensor,
        bias: torch.Tensor | None = None,
    ) -> torch.Tensor:
        weight_scale = layer.weight_scale
        if weight_scale.dtype != MXFP8_SCALE_DTYPE:
            raise ValueError(
                f"Emulation backend requires {MXFP8_SCALE_DTYPE} "
                f"weight_scale dtype, got {weight_scale.dtype}."
            )
        if weight_scale.ndim != 2:
            raise ValueError(
                f"Emulation backend requires 2D weight_scale, "
                f"got {weight_scale.ndim}D. "
                f"Ensure process_weights_after_loading was called."
            )

        weight_bf16 = dequant_mxfp8_to_bf16(layer.weight, weight_scale)
        output = torch.nn.functional.linear(x, weight_bf16, bias)
        return output.to(x.dtype)
```