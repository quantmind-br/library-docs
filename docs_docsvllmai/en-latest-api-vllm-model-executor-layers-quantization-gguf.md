---
title: gguf - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/gguf/
source: sitemap
fetched_at: 2026-05-07T21:27:16.857838287-03:00
rendered_js: false
word_count: 140
summary: This document defines the GGUF configuration and processing methods for vLLM, providing the classes and logic required to handle GGUF-quantized model layers and weight loading.
tags:
    - vllm
    - quantization
    - gguf
    - model-executor
    - linear-method
    - embedding-method
category: reference
---

## GGUFConfig [¶](#vllm.model_executor.layers.quantization.gguf.GGUFConfig "Permanent link")

Bases: `QuantizationConfig`

Config class for GGUF.

Source code in `vllm/model_executor/layers/quantization/gguf.py`

```
classGGUFConfig(QuantizationConfig):
"""Config class for GGUF."""

    def__init__(self, unquantized_modules: list[str] | None = None) -> None:
        super().__init__()
        self.unquantized_modules = unquantized_modules or []

    def__repr__(self) -> str:
        return "GGUFConfig()"

    defget_name(self) -> QuantizationMethods:
        return "gguf"

    defget_supported_act_dtypes(self) -> list[torch.dtype]:
        # GGUF dequantization kernels use half precision (fp16) internally.
        # bfloat16 has precision issues on Blackwell devices.
        if current_platform.has_device_capability(100):
            logger.warning_once("GGUF has precision issues with bfloat16 on Blackwell.")
            return [torch.half, torch.float32]
        return [torch.half, torch.bfloat16, torch.float32]

    @classmethod
    defget_min_capability(cls) -> int:
        return 60

    @classmethod
    defget_config_filenames(cls) -> list[str]:
        return []  # no extra configs.

    @classmethod
    deffrom_config(cls, config: dict[str, Any]) -> "GGUFConfig":
        return cls()

    @classmethod
    defoverride_quantization_method(
        cls, hf_quant_cfg: dict[str, Any], user_quant: str | None, hf_config=None
    ) -> "QuantizationMethods | None":
        # When user explicitly specifies --quantization gguf, override
        # whatever quantization method is in the HF model config (e.g. fp8).
        if user_quant == "gguf":
            return "gguf"
        return None

    defget_quant_method(
        self, layer: torch.nn.Module, prefix: str
    ) -> "QuantizeMethodBase | None":
        if isinstance(layer, LinearBase):
            if is_layer_skipped_gguf(
                prefix, self.unquantized_modules, self.packed_modules_mapping
            ):
                return UnquantizedLinearMethod()
            return GGUFLinearMethod(self)
        elif isinstance(layer, VocabParallelEmbedding):
            if is_layer_skipped_gguf(
                prefix, self.unquantized_modules, self.packed_modules_mapping
            ):
                return UnquantizedEmbeddingMethod()
            return GGUFEmbeddingMethod(self)
        elif isinstance(layer, FusedMoE):
            # TODO: Select UnquantizedFusedMoEMethod on unquantized layers.
            return GGUFMoEMethod(self, layer.moe_config)
        return None

    defapply_vllm_mapper(self, hf_to_vllm_mapper: "WeightsMapper"):
"""
        Interface for models to update module names referenced in
        quantization configs in order to reflect the vllm model structure

        :param hf_to_vllm_mapper: maps from hf model structure (the assumed
            structure of the qconfig) to vllm model structure
        """
        if self.unquantized_modules is not None:
            self.unquantized_modules = hf_to_vllm_mapper.apply_list(
                self.unquantized_modules
            )
```

### apply\_vllm\_mapper [¶](#vllm.model_executor.layers.quantization.gguf.GGUFConfig.apply_vllm_mapper "Permanent link")

Interface for models to update module names referenced in quantization configs in order to reflect the vllm model structure

:param hf\_to\_vllm\_mapper: maps from hf model structure (the assumed structure of the qconfig) to vllm model structure

Source code in `vllm/model_executor/layers/quantization/gguf.py`

```
defapply_vllm_mapper(self, hf_to_vllm_mapper: "WeightsMapper"):
"""
    Interface for models to update module names referenced in
    quantization configs in order to reflect the vllm model structure

    :param hf_to_vllm_mapper: maps from hf model structure (the assumed
        structure of the qconfig) to vllm model structure
    """
    if self.unquantized_modules is not None:
        self.unquantized_modules = hf_to_vllm_mapper.apply_list(
            self.unquantized_modules
        )
```

## GGUFEmbeddingMethod [¶](#vllm.model_executor.layers.quantization.gguf.GGUFEmbeddingMethod "Permanent link")

Bases: `GGUFLinearMethod`

Embedding method for GGUF.

Parameters:

Name Type Description Default `quant_config` `GGUFConfig`

The GGUF quantization config.

*required*

Source code in `vllm/model_executor/layers/quantization/gguf.py`

```
classGGUFEmbeddingMethod(GGUFLinearMethod):
"""Embedding method for GGUF.

    Args:
        quant_config: The GGUF quantization config.
    """

    defembedding(self, layer: torch.nn.Module, x: torch.Tensor) -> torch.Tensor:
        qweight = layer.qweight
        qweight_type = layer.qweight_type.weight_type
        hidden_size = qweight.tensor_shape[1]

        return apply_gguf_embedding(
            x, qweight, qweight_type, hidden_size, dtype=self.params_dtype
        )
```

## GGUFLinearMethod [¶](#vllm.model_executor.layers.quantization.gguf.GGUFLinearMethod "Permanent link")

Bases: `LinearMethodBase`

Linear method for GGUF.

Parameters:

Name Type Description Default `quant_config` `GGUFConfig`

The GGUF quantization config.

*required*

Source code in `vllm/model_executor/layers/quantization/gguf.py`

```
classGGUFLinearMethod(LinearMethodBase):
"""Linear method for GGUF.

    Args:
        quant_config: The GGUF quantization config.
    """

    def__init__(self, quant_config: GGUFConfig):
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
        self.params_dtype = params_dtype
        output_size_per_partition = sum(output_partition_sizes)

        tensor_shape = (output_size_per_partition, input_size_per_partition)
        qweight = GGUFUninitializedParameter(requires_grad=False)
        set_weight_attrs(
            qweight,
            {
                "input_dim": 1,
                "output_dim": 0,
                "tensor_shape": tensor_shape,
                "is_gguf_weight": True,
                "data_container": [],
                "shard_id": [],
                "shard_id_map": {},
            },
        )
        set_weight_attrs(qweight, extra_weight_attrs)
        layer.register_parameter("qweight", qweight)

        qweight_type = Parameter(
            torch.empty(len(output_partition_sizes), dtype=torch.uint8),
            requires_grad=False,
        )
        set_weight_attrs(
            qweight_type,
            {
                "is_gguf_weight_type": True,
                "weight_type": 0,
                "shard_weight_type": {},
                "ignore_warning": True,
            },
        )
        set_weight_attrs(qweight_type, extra_weight_attrs)
        layer.register_parameter("qweight_type", qweight_type)

    defprocess_weights_after_loading(self, layer: torch.nn.Module):
        qweight_type = layer.qweight_type.weight_type
        if not (qweight_type in UNQUANTIZED_TYPES or qweight_type in DEQUANT_TYPES):
            qweight_type = WeightType(qweight_type)
            raise ValueError(
                f"Unsupported GGUF quantization type {qweight_type} in layer {layer}."
            )
        # For MergedColumnParallelLinear and QKVParallelLinear, we need to
        # materialize the padded weight parameter for CUDA Graph compatibility.
        self._create_padded_weight_param(layer)

    def_create_padded_weight_param(self, layer: torch.nn.Module):
"""Create padded weight parameter for GGUF MergedLinear layer."""
        qweight = layer.qweight
        shard_id_map = qweight.shard_id_map
        shard_id = qweight.shard_id
        if len(data_container := qweight.data_container) > 1:
            dtype = {data.dtype for data in data_container}
            assert len(dtype) == 1, ValueError(
                f"Data container has mixed dtypes: {dtype}"
            )
            dtype = next(iter(dtype))
            # concat dim0 and pad dim1
            padded_side = max(x.size(1) for x in data_container)
            concat_side = sum(x.size(0) for x in data_container)
            # Pad the quantized weights to dense tensor, and create a map
            # with the location of each shard in the padded tensor.
            padded_data = torch.zeros(
                (concat_side, padded_side), dtype=dtype, device=qweight.device
            )
            # (dim0_start, dim0_end, dim1_size)
            shard_offset_map = dict[str, tuple[int, int, int]]()
            for idx in shard_id:
                id_in_container = shard_id_map[idx]
                start = sum(x.size(0) for x in data_container[:id_in_container])
                end = start + data_container[id_in_container].size(0)
                size = data_container[id_in_container].size(1)
                padded_data[start:end, :size] = data_container[id_in_container]
                shard_offset_map[idx] = (start, end, size)
            qweight.data_container.clear()
            padded_param = Parameter(padded_data, requires_grad=False)
            set_weight_attrs(padded_param, vars(qweight))
            set_weight_attrs(padded_param, {"shard_offset_map": shard_offset_map})
            layer.register_parameter("qweight", padded_param)

    defapply(
        self,
        layer: torch.nn.Module,
        x: torch.Tensor,
        bias: torch.Tensor | None = None,
    ) -> torch.Tensor:
        shard_id = layer.qweight.shard_id

        if shard_id:
            # dequantize shard weights respectively
            shard_id = ["q", "k", "v"] if "q" in shard_id else shard_id
            qweight = layer.qweight
            result = []
            for idx in shard_id:
                start, end, offset = layer.qweight.shard_offset_map[idx]
                qweight_type = layer.qweight_type.shard_weight_type[idx]
                result.append(
                    fused_mul_mat_gguf(
                        x, qweight[start:end, :offset].contiguous(), qweight_type
                    )
                )
            out = torch.cat(result, axis=1)
        else:
            qweight = layer.qweight
            qweight_type = layer.qweight_type.weight_type
            out = fused_mul_mat_gguf(x, qweight, qweight_type)
        if bias is not None:
            out.add_(bias)
        return out
```

### \_create\_padded\_weight\_param [¶](#vllm.model_executor.layers.quantization.gguf.GGUFLinearMethod._create_padded_weight_param "Permanent link")

```
_create_padded_weight_param(layer: Module)
```

Create padded weight parameter for GGUF MergedLinear layer.

Source code in `vllm/model_executor/layers/quantization/gguf.py`

```
def_create_padded_weight_param(self, layer: torch.nn.Module):
"""Create padded weight parameter for GGUF MergedLinear layer."""
    qweight = layer.qweight
    shard_id_map = qweight.shard_id_map
    shard_id = qweight.shard_id
    if len(data_container := qweight.data_container) > 1:
        dtype = {data.dtype for data in data_container}
        assert len(dtype) == 1, ValueError(
            f"Data container has mixed dtypes: {dtype}"
        )
        dtype = next(iter(dtype))
        # concat dim0 and pad dim1
        padded_side = max(x.size(1) for x in data_container)
        concat_side = sum(x.size(0) for x in data_container)
        # Pad the quantized weights to dense tensor, and create a map
        # with the location of each shard in the padded tensor.
        padded_data = torch.zeros(
            (concat_side, padded_side), dtype=dtype, device=qweight.device
        )
        # (dim0_start, dim0_end, dim1_size)
        shard_offset_map = dict[str, tuple[int, int, int]]()
        for idx in shard_id:
            id_in_container = shard_id_map[idx]
            start = sum(x.size(0) for x in data_container[:id_in_container])
            end = start + data_container[id_in_container].size(0)
            size = data_container[id_in_container].size(1)
            padded_data[start:end, :size] = data_container[id_in_container]
            shard_offset_map[idx] = (start, end, size)
        qweight.data_container.clear()
        padded_param = Parameter(padded_data, requires_grad=False)
        set_weight_attrs(padded_param, vars(qweight))
        set_weight_attrs(padded_param, {"shard_offset_map": shard_offset_map})
        layer.register_parameter("qweight", padded_param)
```

## GGUFMoEMethod [¶](#vllm.model_executor.layers.quantization.gguf.GGUFMoEMethod "Permanent link")

Bases: `FusedMoEMethodBase`

MoE method for GGUF.

Parameters:

Name Type Description Default `quant_config` `GGUFConfig`

The GGUF quantization config.

*required*

Source code in `vllm/model_executor/layers/quantization/gguf.py`

```
classGGUFMoEMethod(FusedMoEMethodBase):
"""MoE method for GGUF.

    Args:
        quant_config: The GGUF quantization config.
    """

    def__init__(
        self,
        quant_config: GGUFConfig,
        moe: FusedMoEConfig,
    ):
        super().__init__(moe)
        self.quant_config = quant_config

    defcreate_weights(
        self,
        layer: torch.nn.Module,
        num_experts: int,
        hidden_size: int,
        intermediate_size_per_partition: int,
        params_dtype: torch.dtype,
        **extra_weight_attrs,
    ):
        tensor_shape = (num_experts, 2 * intermediate_size_per_partition, hidden_size)
        # gate up proj
        w13_qweight = GGUFUninitializedParameter(requires_grad=False)
        set_weight_attrs(
            w13_qweight,
            {
                "input_dim": 1,
                "output_dim": 0,
                "tensor_shape": tensor_shape,
                "is_gguf_weight": True,
                "data_container": [],
            },
        )
        set_weight_attrs(w13_qweight, extra_weight_attrs)
        layer.register_parameter("w13_qweight", w13_qweight)

        w13_qweight_type = Parameter(
            torch.empty(1, dtype=torch.uint8), requires_grad=False
        )
        set_weight_attrs(
            w13_qweight_type,
            {"is_gguf_weight_type": True, "weight_type": 0, "ignore_warning": True},
        )
        set_weight_attrs(w13_qweight_type, extra_weight_attrs)
        layer.register_parameter("w13_qweight_type", w13_qweight_type)

        tensor_shape = (num_experts, intermediate_size_per_partition, hidden_size)
        # gate down proj
        w2_qweight = GGUFUninitializedParameter(requires_grad=False)
        set_weight_attrs(
            w2_qweight,
            {
                "input_dim": 1,
                "output_dim": 0,
                "tensor_shape": tensor_shape,
                "is_gguf_weight": True,
                "data_container": [],
            },
        )
        set_weight_attrs(w2_qweight, extra_weight_attrs)
        layer.register_parameter("w2_qweight", w2_qweight)

        w2_qweight_type = Parameter(
            torch.empty(1, dtype=torch.uint8), requires_grad=False
        )
        set_weight_attrs(
            w2_qweight_type,
            {"is_gguf_weight_type": True, "weight_type": 0, "ignore_warning": True},
        )

        set_weight_attrs(w2_qweight_type, extra_weight_attrs)
        layer.register_parameter("w2_qweight_type", w2_qweight_type)

    defget_fused_moe_quant_config(
        self, layer: torch.nn.Module
    ) -> FusedMoEQuantConfig | None:
        return None

    defapply(
        self,
        layer: FusedMoE,
        x: torch.Tensor,
        topk_weights: torch.Tensor,
        topk_ids: torch.Tensor,
        shared_experts_input: torch.Tensor | None,
    ) -> torch.Tensor:
        if layer.apply_router_weight_on_input:
            raise NotImplementedError(
                "Apply router weight on input is not supported for"
                "fused GGUF MoE method."
            )

        return fused_moe_gguf(
            x,
            layer.w13_qweight,
            layer.w2_qweight,
            topk_weights,
            topk_ids,
            layer.w13_qweight_type.weight_type,
            layer.w2_qweight_type.weight_type,
            layer.activation.value,
        )
```