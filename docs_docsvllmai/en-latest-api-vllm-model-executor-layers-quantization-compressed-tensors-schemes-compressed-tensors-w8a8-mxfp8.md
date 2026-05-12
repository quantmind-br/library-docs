---
title: compressed_tensors_w8a8_mxfp8 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_mxfp8/
source: sitemap
fetched_at: 2026-05-07T21:27:01.894980496-03:00
rendered_js: false
word_count: 0
summary: This document defines a quantization scheme for MXFP8 weight and activation compression within the CompressedTensors framework. It provides the implementation for loading quantized weights and applying dynamic MXFP8 quantization during inference.
tags:
    - mxfp8
    - quantization
    - compressed-tensors
    - model-optimization
    - deep-learning
    - pytorch
category: api
---

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