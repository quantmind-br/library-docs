---
title: fp_quant - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/fp_quant/
source: sitemap
fetched_at: 2026-05-07T21:27:15.948397648-03:00
rendered_js: false
word_count: 0
summary: This document defines the FPQuantLinearMethod class, which manages weight initialization and quantized forward pass execution for FPQuant-compressed neural network layers.
tags:
    - quantization
    - fpquant
    - pytorch
    - model-optimization
    - linear-layer
    - mxfp4
    - nvfp4
category: reference
---

```
classFPQuantLinearMethod(LinearMethodBase):
"""Linear method for FPQuant.

    Args:
        quant_config: The FPQuant quantization config.
    """

    def__init__(self, quant_config: FPQuantConfig):
        self.quant_config = quant_config

    defcreate_weights(
        self,
        layer: torch.nn.Module,
        input_size_per_partition: int,
        output_partition_sizes: list[int],
        input_size: int,
        output_size: int,
        params_dtype: torch.dtype,
        **extra_weight_attrs,
    ):
        del output_size  # Unused.
        del input_size  # Unused.

        if params_dtype != torch.bfloat16:
            raise ValueError("Only bfloat16 is currently supported by FPQuant")
        if input_size_per_partition % self.quant_config.hadamard_group_size != 0:  # noqa: E501
            raise ValueError(
                "The input size is not aligned with the quantized "
                "weight shape. This can be caused by too large "
                "tensor parallel size. Or other skill issues."
            )

        assert self.quant_config.forward_dtype in ["mxfp4", "nvfp4"], (
            "Only mxfp4 and nvfp4 are supported for now"
        )
        if self.quant_config.forward_dtype == "mxfp4":
            group_size = 32
        elif self.quant_config.forward_dtype == "nvfp4":
            group_size = 16
        else:
            raise ValueError(
                f"Unsupported forward_dtype: {self.quant_config.forward_dtype}"
            )

        qweight = Parameter(
            torch.empty(
                sum(output_partition_sizes),
                input_size_per_partition // 2,
                dtype=torch.uint8,
            ),
            requires_grad=False,
        )
        set_weight_attrs(
            qweight,
            {
                "input_dim": 1,
                "output_dim": 0,
                "packed_dim": 1,
                "pack_factor": 2,
            }
            | extra_weight_attrs,
        )
        layer.register_parameter("qweight", qweight)

        scales = Parameter(
            torch.empty(
                sum(output_partition_sizes),
                input_size_per_partition // group_size,
                dtype=torch.uint8,
            ),
            requires_grad=False,
        )
        set_weight_attrs(
            scales,
            {
                "input_dim": 1,
                "output_dim": 0,
                "packed_dim": 1,
                "pack_factor": group_size,
            }
            | extra_weight_attrs,
        )
        layer.register_parameter("scales", scales)

        weight_global_scale = Parameter(
            torch.empty(1, dtype=torch.float32),
            requires_grad=False,
        )
        set_weight_attrs(
            weight_global_scale, {"ignore_warning": True} | extra_weight_attrs
        )
        layer.register_parameter("weight_global_scale", weight_global_scale)

        act_global_scale = Parameter(
            torch.empty(1, dtype=torch.float32),
            requires_grad=False,
        )
        set_weight_attrs(
            act_global_scale, {"ignore_warning": True} | extra_weight_attrs
        )
        layer.register_parameter("act_global_scale", act_global_scale)

        forward_hadamard_matrix = Parameter(
            torch.empty(
                self.quant_config.hadamard_group_size,
                self.quant_config.hadamard_group_size,
                dtype=params_dtype,
            ),
            requires_grad=False,
        )
        set_weight_attrs(
            forward_hadamard_matrix, {"ignore_warning": True} | extra_weight_attrs
        )
        layer.register_parameter("forward_hadamard_matrix", forward_hadamard_matrix)

        backward_hadamard_matrix = Parameter(
            torch.empty(
                self.quant_config.hadamard_group_size,
                self.quant_config.hadamard_group_size,
                dtype=params_dtype,
            ),
            requires_grad=False,
        )
        set_weight_attrs(
            backward_hadamard_matrix, {"ignore_warning": True} | extra_weight_attrs
        )
        layer.register_parameter("backward_hadamard_matrix", backward_hadamard_matrix)

    defapply(
        self,
        layer: torch.nn.Module,
        x: torch.Tensor,
        bias: torch.Tensor | None = None,
    ) -> torch.Tensor:
        return quantized_forward(
            x,
            layer.qweight,
            layer.scales,
            layer.weight_global_scale,
            layer.act_global_scale,
            bias,
            layer.forward_hadamard_matrix,
            self.quant_config.forward_method,
            self.quant_config.forward_dtype,
        )
```