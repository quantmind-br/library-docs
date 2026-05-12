---
title: bitsandbytes - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/bitsandbytes/
source: sitemap
fetched_at: 2026-05-07T21:26:34.949615004-03:00
rendered_js: false
word_count: 0
summary: This document defines the BitsAndBytesMoEMethod class, which implements quantization support for Mixture-of-Experts (MoE) layers using bitsandbytes 4-bit and 8-bit techniques within the vLLM framework.
tags:
    - moe
    - bitsandbytes
    - quantization
    - vllm
    - model-optimization
    - deep-learning-infrastructure
category: api
---

```
classBitsAndBytesMoEMethod(FusedMoEMethodBase):
"""MoE method for BitsAndBytes.

    Args:
       quant_config: The BitsAndBytes quantization config.
    """

    def__init__(
        self,
        quant_config: BitsAndBytesConfig,
        moe: FusedMoEConfig,
    ):
        super().__init__(moe)
        _check_bitsandbytes_version()
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
        if self.quant_config.load_in_8bit:
            call_fun = self._create_weights_8bit
        else:
            call_fun = self._create_weights_4bit
        call_fun(
            layer,
            num_experts,
            hidden_size,
            intermediate_size_per_partition,
            params_dtype,
            **extra_weight_attrs,
        )

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
        fromvllm.model_executor.layers.fused_moeimport fused_experts

        # TODO(bnell): Do these need to be called on the hot path?
        if self.quant_config.load_in_8bit:
            w13, w2 = self._apply_8bit_dequant(layer)
        else:
            w13, w2 = self._apply_4bit_dequnt(layer)
        return fused_experts(
            hidden_states=x,
            w1=w13,
            w2=w2,
            topk_weights=topk_weights,
            topk_ids=topk_ids,
            inplace=not self.moe.disable_inplace,
            activation=layer.activation,
            apply_router_weight_on_input=layer.apply_router_weight_on_input,
            global_num_experts=layer.global_num_experts,
            expert_map=layer.expert_map,
            quant_config=self.moe_quant_config,
        )

    def_create_weights_4bit(
        self,
        layer: torch.nn.Module,
        num_experts: int,
        hidden_size: int,
        intermediate_size_per_partition: int,
        params_dtype: torch.dtype,
        **extra_weight_attrs,
    ):
        quant_ratio = calculate_quant_ratio(params_dtype)
        # Fused gate_up_proj (column parallel)
        w13_total_size = (
            hidden_size * 2 * intermediate_size_per_partition
        ) // quant_ratio
        w13_qweight = torch.nn.Parameter(
            torch.empty(
                num_experts,
                w13_total_size,
                1,
                dtype=torch.uint8,
            ),
            requires_grad=False,
        )
        layer.register_parameter("w13_weight", w13_qweight)
        set_weight_attrs(w13_qweight, extra_weight_attrs)
        set_weight_attrs(
            w13_qweight,
            {
                "num_experts": num_experts,
                "input_dim": hidden_size,
                "output_dim": 2 * intermediate_size_per_partition,
                "experts_shape": (
                    num_experts,
                    intermediate_size_per_partition * 2,
                    hidden_size,
                ),
                "pack_factor": quant_ratio,
                "use_bitsandbytes_4bit": True,
            },
        )
        # down_proj (row parallel)
        w2_total_size = (hidden_size * intermediate_size_per_partition) // quant_ratio
        w2_qweight = torch.nn.Parameter(
            torch.empty(
                num_experts,
                w2_total_size,
                1,
                dtype=torch.uint8,
            ),
            requires_grad=False,
        )
        set_weight_attrs(
            w2_qweight,
            {
                "num_experts": num_experts,
                "input_dim": intermediate_size_per_partition,
                "output_dim": hidden_size,
                "experts_shape": (
                    num_experts,
                    hidden_size,
                    intermediate_size_per_partition,
                ),
                "pack_factor": quant_ratio,
                "use_bitsandbytes_4bit": True,
            },
        )
        layer.register_parameter("w2_weight", w2_qweight)
        set_weight_attrs(w2_qweight, extra_weight_attrs)

    def_create_weights_8bit(
        self,
        layer: torch.nn.Module,
        num_experts: int,
        hidden_size: int,
        intermediate_size_per_partition: int,
        params_dtype: torch.dtype,
        **extra_weight_attrs,
    ):
        raise NotImplementedError

    def_apply_4bit_dequnt(
        self, layer: torch.nn.Module
    ) -> tuple[torch.Tensor, torch.Tensor]:
        frombitsandbytes.functionalimport dequantize_4bit

        w13 = dequantize_4bit(
            layer.w13_weight.reshape(-1, 1),
            layer.w13_weight.bnb_quant_state,
        )
        w2 = dequantize_4bit(
            layer.w2_weight.reshape(-1, 1),
            layer.w2_weight.bnb_quant_state,
        )
        w13 = w13.reshape(layer.w13_weight.experts_shape)
        w2 = w2.reshape(layer.w2_weight.experts_shape)
        return w13, w2

    def_apply_8bit_dequant(
        self, layer: torch.nn.Module
    ) -> tuple[torch.Tensor, torch.Tensor]:
        raise NotImplementedError
```