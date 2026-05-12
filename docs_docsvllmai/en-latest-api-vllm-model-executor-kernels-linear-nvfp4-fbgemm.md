---
title: fbgemm - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/nvfp4/fbgemm/
source: sitemap
fetched_at: 2026-05-07T21:23:38.990830083-03:00
rendered_js: false
word_count: 0
summary: This document defines the implementation of a linear kernel class that utilizes FBGEMM for NVFP4 quantization and matrix multiplication operations.
tags:
    - fbgemm
    - fp4-quantization
    - linear-kernel
    - gpu-acceleration
    - matrix-multiplication
category: api
---

```
classFbgemmNvFp4LinearKernel(NvFp4LinearKernel):
"""NVFP4 GEMM via FBGEMM."""

    @classmethod
    defis_supported(
        cls, compute_capability: int | None = None
    ) -> tuple[bool, str | None]:
        if has_fbgemm_gpu():
            return True, None
        return False, "fbgemm_gpu required"

    @classmethod
    defcan_implement(cls, config: NvFp4LinearLayerConfig) -> tuple[bool, str | None]:
        return True, None

    defprocess_weights_after_loading(self, layer: torch.nn.Module) -> None:
        swizzled = swizzle_blockscale(layer.weight_scale.data)
        layer.weight_scale = torch.nn.Parameter(
            swizzled.view(-1).view(torch.uint8), requires_grad=False
        )

    defapply_weights(
        self,
        layer: torch.nn.Module,
        x: torch.Tensor,
        bias: torch.Tensor | None = None,
    ) -> torch.Tensor:
        importfbgemm_gpu  # noqa: F401 - registers torch.ops.fbgemm.*

        output_size = layer.output_size_per_partition
        output_dtype = x.dtype
        output_shape = [*x.shape[:-1], output_size]

        x_fp4, x_blockscale = scaled_fp4_quant(
            x,
            layer.input_global_scale_inv,
            is_sf_swizzled_layout=True,
            backend="fbgemm",
        )

        out = torch.ops.fbgemm.f4f4bf16(
            x_fp4,
            layer.weight,
            x_blockscale.view(-1).view(torch.uint8),
            layer.weight_scale,
            layer.alpha,
            use_mx=False,
        ).to(output_dtype)

        out = slice_nvfp4_output(out, output_size)

        if bias is not None:
            out = out + bias
        return out.view(*output_shape)
```