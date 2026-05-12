---
title: cutlass - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/nvfp4/cutlass/
source: sitemap
fetched_at: 2026-05-07T21:23:36.988186495-03:00
rendered_js: false
word_count: 0
summary: This document defines the NvFp4LinearKernel class, which integrates CUTLASS FP4 GEMM kernels into vLLM for high-performance linear layer computations.
tags:
    - vllm
    - cutlass
    - fp4-quantization
    - gemm-kernel
    - linear-layer
    - gpu-acceleration
category: api
---

```
classCutlassNvFp4LinearKernel(NvFp4LinearKernel):
"""NVFP4 GEMM via the vLLM CUTLASS kernel."""

    @classmethod
    defis_supported(
        cls, compute_capability: int | None = None
    ) -> tuple[bool, str | None]:
        if cutlass_fp4_supported():
            return True, None
        return False, "CUTLASS FP4 kernels not available"

    @classmethod
    defcan_implement(cls, config: NvFp4LinearLayerConfig) -> tuple[bool, str | None]:
        return True, None

    defprocess_weights_after_loading(self, layer: torch.nn.Module) -> None:
        layer.weight_scale = torch.nn.Parameter(
            swizzle_blockscale(layer.weight_scale.data), requires_grad=False
        )
        padded_weight, weights_padding_cols = pad_nvfp4_weight_for_cutlass(
            layer.weight.data
        )
        layer.weight = torch.nn.Parameter(padded_weight, requires_grad=False)
        layer.weights_padding_cols = weights_padding_cols

    defapply_weights(
        self,
        layer: torch.nn.Module,
        x: torch.Tensor,
        bias: torch.Tensor | None = None,
    ) -> torch.Tensor:
        output_size = layer.output_size_per_partition
        output_dtype = x.dtype
        output_shape = [*x.shape[:-1], output_size]

        x_fp4, x_blockscale = scaled_fp4_quant(
            x,
            layer.input_global_scale_inv,
            is_sf_swizzled_layout=True,
            backend="cutlass",
        )

        x_fp4 = pad_nvfp4_activation_for_cutlass(
            x_fp4, getattr(layer, "weights_padding_cols", 0)
        )

        out = cutlass_scaled_fp4_mm(
            x_fp4,
            layer.weight,
            x_blockscale,
            layer.weight_scale,
            layer.alpha,
            output_dtype,
        )

        out = slice_nvfp4_output(out, output_size)

        if bias is not None:
            out = out + bias
        return out.view(*output_shape)
```