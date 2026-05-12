---
title: flashinfer - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/nvfp4/flashinfer/
source: sitemap
fetched_at: 2026-05-07T21:23:39.99551627-03:00
rendered_js: false
word_count: 42
summary: This document defines the FlashInfer-based NVFP4 linear kernel implementations in vLLM, providing wrappers for cuDNN, CUTLASS, and TensorRT-LLM backends to perform quantized matrix multiplications.
tags:
    - vllm
    - nvfp4
    - flashinfer
    - quantization
    - gemm
    - linear-kernel
    - gpu-acceleration
category: reference
---

## FlashInferCudnnNvFp4LinearKernel [¶](#vllm.model_executor.kernels.linear.nvfp4.flashinfer.FlashInferCudnnNvFp4LinearKernel "Permanent link")

Bases: `NvFp4LinearKernel`

NVFP4 GEMM via FlashInfer's cuDNN wrapper.

Source code in `vllm/model_executor/kernels/linear/nvfp4/flashinfer.py`

```
classFlashInferCudnnNvFp4LinearKernel(NvFp4LinearKernel):
"""NVFP4 GEMM via FlashInfer's cuDNN wrapper."""

    @classmethod
    defis_supported(
        cls, compute_capability: int | None = None
    ) -> tuple[bool, str | None]:
        if has_flashinfer():
            return True, None
        return False, "FlashInfer required"

    @classmethod
    defcan_implement(cls, config: NvFp4LinearLayerConfig) -> tuple[bool, str | None]:
        return True, None

    defprocess_weights_after_loading(self, layer: torch.nn.Module) -> None:
        # cuDNN uses the same swizzled + padded layout as CUTLASS
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
            backend="flashinfer-cudnn",
        )

        x_fp4 = pad_nvfp4_activation_for_cutlass(
            x_fp4, getattr(layer, "weights_padding_cols", 0)
        )

        out = flashinfer_scaled_fp4_mm(
            x_fp4,
            layer.weight,
            x_blockscale,
            layer.weight_scale,
            layer.alpha,
            output_dtype,
            backend="cudnn",
        )

        out = slice_nvfp4_output(out, output_size)

        if bias is not None:
            out = out + bias
        return out.view(*output_shape)
```

## FlashInferCutlassNvFp4LinearKernel [¶](#vllm.model_executor.kernels.linear.nvfp4.flashinfer.FlashInferCutlassNvFp4LinearKernel "Permanent link")

Bases: `NvFp4LinearKernel`

NVFP4 GEMM via FlashInfer's CUTLASS wrapper.

Source code in `vllm/model_executor/kernels/linear/nvfp4/flashinfer.py`

```
classFlashInferCutlassNvFp4LinearKernel(NvFp4LinearKernel):
"""NVFP4 GEMM via FlashInfer's CUTLASS wrapper."""

    @classmethod
    defis_supported(
        cls, compute_capability: int | None = None
    ) -> tuple[bool, str | None]:
        fromvllm.model_executor.layers.quantization.utils.nvfp4_utilsimport (
            cutlass_fp4_supported,
        )

        if (
            cutlass_fp4_supported()
            and current_platform.has_device_capability(100)
            and has_flashinfer()
        ):
            return True, None
        return False, "FlashInfer + >=sm_100 required"

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
            backend="flashinfer-cutlass",
        )

        x_fp4 = pad_nvfp4_activation_for_cutlass(
            x_fp4, getattr(layer, "weights_padding_cols", 0)
        )

        out = flashinfer_scaled_fp4_mm(
            x_fp4,
            layer.weight,
            x_blockscale,
            layer.weight_scale,
            layer.alpha,
            output_dtype,
            backend="cutlass",
        )

        out = slice_nvfp4_output(out, output_size)

        if bias is not None:
            out = out + bias
        return out.view(*output_shape)
```

## FlashInferTrtllmNvFp4LinearKernel [¶](#vllm.model_executor.kernels.linear.nvfp4.flashinfer.FlashInferTrtllmNvFp4LinearKernel "Permanent link")

Bases: `NvFp4LinearKernel`

NVFP4 GEMM via FlashInfer's TensorRT-LLM wrapper.

Source code in `vllm/model_executor/kernels/linear/nvfp4/flashinfer.py`

```
classFlashInferTrtllmNvFp4LinearKernel(NvFp4LinearKernel):
"""NVFP4 GEMM via FlashInfer's TensorRT-LLM wrapper."""

    @classmethod
    defis_supported(
        cls, compute_capability: int | None = None
    ) -> tuple[bool, str | None]:
        if has_flashinfer():
            return True, None
        return False, "FlashInfer required"

    @classmethod
    defcan_implement(cls, config: NvFp4LinearLayerConfig) -> tuple[bool, str | None]:
        return True, None

    defprocess_weights_after_loading(self, layer: torch.nn.Module) -> None:
        fromflashinferimport shuffle_matrix_a, shuffle_matrix_sf_a

        weight = layer.weight.data
        weight_scale = layer.weight_scale.data
        epilogue_tile_m = 128

        layer.weight = torch.nn.Parameter(
            shuffle_matrix_a(weight.view(torch.uint8), epilogue_tile_m),
            requires_grad=False,
        )
        layer.weight_scale = torch.nn.Parameter(
            shuffle_matrix_sf_a(weight_scale.view(torch.uint8), epilogue_tile_m)
            .reshape(weight_scale.shape)
            .view(torch.float8_e4m3fn),
            requires_grad=False,
        )

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
            backend="flashinfer-trtllm",
        )

        out = flashinfer_scaled_fp4_mm(
            x_fp4,
            layer.weight,
            x_blockscale,
            layer.weight_scale,
            layer.alpha,
            output_dtype,
            backend="trtllm",
        )

        out = slice_nvfp4_output(out, output_size)

        if bias is not None:
            out = out + bias
        return out.view(*output_shape)
```