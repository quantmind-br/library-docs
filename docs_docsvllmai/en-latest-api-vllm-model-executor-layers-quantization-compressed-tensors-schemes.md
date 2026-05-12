---
title: schemes - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/compressed_tensors/schemes/
source: sitemap
fetched_at: 2026-05-07T21:26:50.854235494-03:00
rendered_js: false
word_count: 215
summary: This document defines the abstract base class and specific implementation schemes for supporting various quantization formats, such as MXFP4 and MXFP8, within the CompressedTensors framework.
tags:
    - quantization
    - compressed-tensors
    - mxfp4
    - mxfp8
    - model-inference
    - pytorch
category: reference
---

Modules:

Name Description `compressed_tensors_scheme` `compressed_tensors_w4a16_mxfp4` `compressed_tensors_w8a8_mxfp8`

Bases: `ABC`

Abstract class used to describe the weight creation and forward pass of different quantization schemes supported by CompressedTensors.

Source code in `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_scheme.py`

```
classCompressedTensorsScheme(ABC):
"""
    Abstract class used to describe the weight creation and forward pass
    of different quantization schemes supported by CompressedTensors.
    """

    @classmethod
    @abstractmethod
    defget_min_capability(cls) -> int:
"""
        Get minimum device capability.
        """
        raise NotImplementedError()

    @abstractmethod
    defcreate_weights(self, *args, **kwargs):
"""
        Weight creation for the particular scheme. Inputs to this function

        """
        raise NotImplementedError()

    @abstractmethod
    defapply_weights(
        self, layer: torch.nn.Module, x: torch.Tensor, bias: torch.Tensor | None
    ):
"""
        Run the forward pass for the particular scheme. This is where
        scheme-specific dequant/quant steps/kernels should be applied.

        :param layer: torch.nn.Module with the registered weights and
            other parameters relevant to the particular scheme.
        :param x: input to the layer
        :param bias: bias parameter

        """
        raise NotImplementedError()

    @abstractmethod
    defprocess_weights_after_loading(self, layer: torch.nn.Module):
"""
        Called after weight loading is complete for any cleanup that
        needs to occur.
        """
        raise NotImplementedError()
```

Run the forward pass for the particular scheme. This is where scheme-specific dequant/quant steps/kernels should be applied.

:param layer: torch.nn.Module with the registered weights and other parameters relevant to the particular scheme. :param x: input to the layer :param bias: bias parameter

Source code in `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_scheme.py`

```
@abstractmethod
defapply_weights(
    self, layer: torch.nn.Module, x: torch.Tensor, bias: torch.Tensor | None
):
"""
    Run the forward pass for the particular scheme. This is where
    scheme-specific dequant/quant steps/kernels should be applied.

    :param layer: torch.nn.Module with the registered weights and
        other parameters relevant to the particular scheme.
    :param x: input to the layer
    :param bias: bias parameter

    """
    raise NotImplementedError()

create_weights(*args, **kwargs)
```

Weight creation for the particular scheme. Inputs to this function

Source code in `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_scheme.py`

```
@abstractmethod
defcreate_weights(self, *args, **kwargs):
"""
    Weight creation for the particular scheme. Inputs to this function

    """
    raise NotImplementedError()

get_min_capability() -> int
```

Get minimum device capability.

Source code in `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_scheme.py`

```
@classmethod
@abstractmethod
defget_min_capability(cls) -> int:
"""
    Get minimum device capability.
    """
    raise NotImplementedError()

process_weights_after_loading(layer: Module)
```

Called after weight loading is complete for any cleanup that needs to occur.

Source code in `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_scheme.py`

```
@abstractmethod
defprocess_weights_after_loading(self, layer: torch.nn.Module):
"""
    Called after weight loading is complete for any cleanup that
    needs to occur.
    """
    raise NotImplementedError()
```

## CompressedTensorsW4A16Mxfp4 [¶](#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsW4A16Mxfp4 "Permanent link")

Bases: `CompressedTensorsScheme`

Compressed tensors scheme for MXFP4 weight-only quantization.

Supports models quantized with the compressed-tensors mxfp4-pack-quantized format.

MXFP4 format: - 4-bit float weights (E2M1) packed into uint8 - Per-group E8M0 scales with group\_size=32 - No global scale (unlike NVFP4)

Source code in `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a16_mxfp4.py`

```
classCompressedTensorsW4A16Mxfp4(CompressedTensorsScheme):
"""
    Compressed tensors scheme for MXFP4 weight-only quantization.

    Supports models quantized with the compressed-tensors mxfp4-pack-quantized
    format.

    MXFP4 format:
    - 4-bit float weights (E2M1) packed into uint8
    - Per-group E8M0 scales with group_size=32
    - No global scale (unlike NVFP4)
    """

    def__init__(self):
        self.group_size = 32

    @classmethod
    defget_min_capability(cls) -> int:
        return 80

    defcreate_weights(
        self,
        layer: torch.nn.Module,
        output_partition_sizes: list[int],
        input_size_per_partition: int,
        params_dtype: torch.dtype,
        weight_loader: Callable,
        **kwargs,
    ):
        output_size_per_partition = sum(output_partition_sizes)
        layer.logical_widths = output_partition_sizes
        layer.input_size_per_partition = input_size_per_partition
        layer.output_size_per_partition = output_size_per_partition
        layer.params_dtype = params_dtype

        # Packed FP4 weights (2 values per byte)
        weight = ModelWeightParameter(
            data=torch.empty(
                output_size_per_partition,
                input_size_per_partition // 2,
                dtype=torch.uint8,
            ),
            input_dim=1,
            output_dim=0,
            weight_loader=weight_loader,
        )
        layer.register_parameter("weight_packed", weight)

        # Per-group E8M0 scales
        weight_scale = GroupQuantScaleParameter(
            data=torch.empty(
                output_size_per_partition,
                input_size_per_partition // self.group_size,
                dtype=torch.uint8,
            ),
            input_dim=1,
            output_dim=0,
            weight_loader=weight_loader,
        )
        layer.register_parameter("weight_scale", weight_scale)

    defprocess_weights_after_loading(self, layer: torch.nn.Module) -> None:
        # Rename weight_packed to weight that marlin expects
        layer.weight = Parameter(layer.weight_packed.data, requires_grad=False)
        del layer.weight_packed

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
            weight_global_scale=None,
            workspace=layer.workspace,
            size_n=layer.output_size_per_partition,
            size_k=layer.input_size_per_partition,
            bias=bias,
        )
```

## CompressedTensorsW8A8Mxfp8 [¶](#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsW8A8Mxfp8 "Permanent link")

Bases: `CompressedTensorsScheme`

Compressed tensors scheme for MXFP8 quantization (W8A8).

Loads pre-quantized MXFP8 weights from compressed-tensors checkpoints. Activations are dynamically quantized to MXFP8 at runtime.

MXFP8 format: - 8-bit float weights (E4M3) stored as float8\_e4m3fn - Per-group E8M0 scales (uint8) with group\_size=32 - Activations dynamically quantized to MXFP8 during inference

Source code in `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_mxfp8.py`

```
classCompressedTensorsW8A8Mxfp8(CompressedTensorsScheme):
"""
    Compressed tensors scheme for MXFP8 quantization (W8A8).

    Loads pre-quantized MXFP8 weights from compressed-tensors checkpoints.
    Activations are dynamically quantized to MXFP8 at runtime.

    MXFP8 format:
    - 8-bit float weights (E4M3) stored as float8_e4m3fn
    - Per-group E8M0 scales (uint8) with group_size=32
    - Activations dynamically quantized to MXFP8 during inference
    """

    def__init__(self):
        self.kernel = init_mxfp8_linear_kernel()

    @classmethod
    defget_min_capability(cls) -> int:
        return 75

    defcreate_weights(
        self,
        layer: torch.nn.Module,
        output_partition_sizes: list[int],
        input_size_per_partition: int,
        params_dtype: torch.dtype,
        weight_loader: Callable,
        **kwargs,
    ):
        output_size_per_partition = sum(output_partition_sizes)
        layer.logical_widths = output_partition_sizes
        layer.input_size_per_partition = input_size_per_partition
        layer.output_size_per_partition = output_size_per_partition
        layer.params_dtype = params_dtype

        weight = ModelWeightParameter(
            data=torch.empty(
                output_size_per_partition,
                input_size_per_partition,
                dtype=MXFP8_VALUE_DTYPE,
            ),
            input_dim=1,
            output_dim=0,
            weight_loader=weight_loader,
        )
        layer.register_parameter("weight", weight)

        weight_scale = GroupQuantScaleParameter(
            data=torch.empty(
                output_size_per_partition,
                input_size_per_partition // MXFP8_BLOCK_SIZE,
                dtype=MXFP8_SCALE_DTYPE,
            ),
            input_dim=1,
            output_dim=0,
            weight_loader=weight_loader,
        )
        layer.register_parameter("weight_scale", weight_scale)

    defprocess_weights_after_loading(self, layer: torch.nn.Module) -> None:
        self.kernel.process_weights_after_loading(layer)

    defapply_weights(
        self,
        layer: torch.nn.Module,
        x: torch.Tensor,
        bias: torch.Tensor | None = None,
    ) -> torch.Tensor:
        return self.kernel.apply_weights(layer, x, bias)
```