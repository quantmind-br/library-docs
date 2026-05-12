---
title: cpu_wna16 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/cpu_wna16/
source: sitemap
fetched_at: 2026-05-07T21:27:11.78192133-03:00
rendered_js: false
word_count: 0
summary: This class implements the CPU AWQ quantization method for linear layers, handling weight initialization, packing, and optimized GEMM execution paths for different inference backends.
tags:
    - awq
    - cpu-quantization
    - model-optimization
    - linear-layer
    - tensor-packing
    - vllm
category: api
---

```
classCPUAWQLinearMethod(LinearMethodBase):
"""Linear method for CPU AWQ.

    Args:
        quant_config: The CPU AWQ quantization config.
    """

    def__init__(self, quant_config: CPUAWQConfig) -> None:
        self.quant_config = quant_config
        assert self.quant_config.zero_point

    defcreate_weights(
        self,
        layer: torch.nn.Module,
        input_size_per_partition: int,
        output_partition_sizes: list[int],
        input_size: int,
        output_size: int,
        params_dtype: torch.dtype,
        **extra_weight_attrs,
    ) -> None:
        del output_size
        output_size_per_partition = sum(output_partition_sizes)
        weight_loader = extra_weight_attrs.get("weight_loader")

        # Normalize group_size
        if self.quant_config.group_size != -1:
            group_size = self.quant_config.group_size
        else:
            group_size = input_size

        qweight = PackedvLLMParameter(
            data=torch.empty(
                input_size_per_partition,
                output_size_per_partition // self.quant_config.pack_factor,
                dtype=torch.int32,
            ),
            input_dim=0,
            output_dim=1,
            packed_dim=1,
            packed_factor=self.quant_config.pack_factor,
            weight_loader=weight_loader,
        )

        num_groups = input_size_per_partition // group_size

        qzeros = PackedvLLMParameter(
            data=torch.empty(
                num_groups,
                output_size_per_partition // self.quant_config.pack_factor,
                dtype=torch.int32,
            ),
            input_dim=0,
            output_dim=1,
            packed_dim=1,
            packed_factor=self.quant_config.pack_factor,
            weight_loader=weight_loader,
        )

        scales = GroupQuantScaleParameter(
            data=torch.empty(
                num_groups,
                output_size_per_partition,
                dtype=params_dtype,
            ),
            input_dim=0,
            output_dim=1,
            weight_loader=weight_loader,
        )

        layer.register_parameter("qweight", qweight)
        layer.register_parameter("qzeros", qzeros)
        layer.register_parameter("scales", scales)

    defprocess_weights_after_loading(self, layer: torch.nn.Module) -> None:
        layer.use_w4a8 = envs.VLLM_CPU_INT4_W4A8 and torch.cpu._is_amx_tile_supported()
        if layer.use_w4a8:
            self._process_weights_sglang_int4(layer)
        else:
            self._process_weights_woq(layer)

    def_process_weights_woq(self, layer: torch.nn.Module) -> None:
"""Original WOQ int4 repack path."""
        packed_weight = layer.qweight.data
        packed_zeros = layer.qzeros.data
        group_num = packed_zeros.size(0)
        bits = self.quant_config.weight_bits
        pack_factor = int(self.quant_config.pack_factor)
        input_size, packed_output_size = packed_weight.size()
        output_size = packed_output_size * pack_factor
        isa_hint = _get_isa_hint(layer.scales.dtype)
        layer.isa_hint = isa_hint

        interleave_map = (0, 4, 1, 5, 2, 6, 3, 7)
        weight = unpack_cols(
            packed_weight,
            bits,
            input_size,
            output_size,
        )
        zeros = unpack_cols(
            packed_zeros,
            bits,
            group_num,
            output_size,
        )
        weight = (
            weight.view(input_size, -1, pack_factor)[:, :, interleave_map]
            .reshape(input_size, output_size)
            .contiguous()
        )
        zeros = (
            zeros.view(group_num, -1, pack_factor)[:, :, interleave_map]
            .reshape(group_num, output_size)
            .contiguous()
        )

        zeros = pack_cols(zeros, bits, group_num, output_size).contiguous()
        weight = pack_cols(weight, bits, input_size, output_size)
        weight = (
            weight.view(input_size, -1, 16 // pack_factor)
            .permute(1, 0, 2)
            .reshape(-1, input_size * 16 // pack_factor)
            .contiguous()
        )
        layer.qweight.data = weight
        layer.qzeros.data = zeros

    def_process_weights_sglang_int4(self, layer: torch.nn.Module) -> None:
"""SGLang INT4 W4A8 path: pack int4 weights with VNNI reordering."""
        packed_weight = layer.qweight.data
        packed_zeros = layer.qzeros.data
        scales = layer.scales.data
        blocked_w, blocked_zp, blocked_s = ops.convert_weight_packed_scale_zp(
            packed_weight,
            packed_zeros,
            scales,
            ops.CPUQuantAlgo.AWQ,
        )

        layer.packed_weight = blocked_w
        layer.packed_qzeros = blocked_zp
        layer.packed_scales = blocked_s
        layer.qweight = None
        layer.qzeros = None
        layer.scales = None

    defapply(
        self,
        layer: torch.nn.Module,
        x: torch.Tensor,
        bias: torch.Tensor | None = None,
    ) -> torch.Tensor:
        if layer.use_w4a8:
            return self._apply_sglang_int4(layer, x, bias)
        return self._apply_woq(layer, x, bias)

    def_apply_woq(
        self,
        layer: torch.nn.Module,
        x: torch.Tensor,
        bias: torch.Tensor | None = None,
    ) -> torch.Tensor:
"""Original WOQ int4 GEMM path."""
        x = ops.cpu_gemm_wna16(
            input=x,
            q_weight=layer.qweight,
            scales=layer.scales,
            zeros=layer.qzeros,
            g_idx=None,
            bias=bias,
            pack_factor=8,
            isa_hint=layer.isa_hint,
        )
        return x

    def_apply_sglang_int4(
        self,
        layer: torch.nn.Module,
        x: torch.Tensor,
        bias: torch.Tensor | None = None,
    ) -> torch.Tensor:
"""SGLang INT4 W4A8 GEMM path."""
        return ops.int4_scaled_mm_cpu(
            x,
            layer.packed_weight,
            layer.packed_qzeros,
            layer.packed_scales,
            bias,
        )
```