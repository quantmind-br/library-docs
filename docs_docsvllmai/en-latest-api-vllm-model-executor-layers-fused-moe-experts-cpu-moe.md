---
title: cpu_moe - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/cpu_moe/
source: sitemap
fetched_at: 2026-05-07T21:24:38.138338933-03:00
rendered_js: false
word_count: 0
summary: This document defines a Python class for executing CPU-based FP8 block-quantized Mixture-of-Experts (MoE) operations using monolithic fused experts. It provides logic for verifying hardware support, activation functions, and quantization schemes for efficient model inference.
tags:
    - mixture-of-experts
    - cpu-inference
    - fp8-quantization
    - model-optimization
    - fused-kernels
    - deep-learning
category: reference
---

```
classCPUExpertsFp8(mk.FusedMoEExpertsMonolithic):
"""CPU FP8 W8A16 block-quantized monolithic MoE experts."""

    def__init__(
        self,
        moe_config: FusedMoEConfig,
        quant_config: FusedMoEQuantConfig,
    ):
        super().__init__(
            moe_config,
            quant_config,
        )

    @property
    defexpects_unquantized_inputs(self) -> bool:
        return True

    @staticmethod
    defactivation_format() -> mk.FusedMoEActivationFormat:
        return mk.FusedMoEActivationFormat.Standard

    @staticmethod
    def_supports_current_device() -> bool:
        return current_platform.is_cpu()

    @staticmethod
    def_supports_no_act_and_mul() -> bool:
        return False

    @staticmethod
    def_supports_activation(activation: MoEActivation) -> bool:
        return activation == MoEActivation.SILU

    @staticmethod
    def_supports_parallel_config(
        moe_parallel_config: FusedMoEParallelConfig,
    ) -> bool:
        return True

    @staticmethod
    def_supports_quant_scheme(
        weight_key: QuantKey | None,
        activation_key: QuantKey | None,
    ) -> bool:
        SUPPORTED_W_A = [
            (kFp8Static128BlockSym, kFp8Dynamic128Sym),
        ]
        return (weight_key, activation_key) in SUPPORTED_W_A

    @staticmethod
    def_supports_routing_method(
        routing_method: RoutingMethodType,
        weight_key: QuantKey | None,
        activation_key: QuantKey | None,
    ) -> bool:
        return routing_method in [
            RoutingMethodType.Default,
            RoutingMethodType.Renormalize,
            RoutingMethodType.RenormalizeNaive,
        ]

    @staticmethod
    def_supports_router_logits_dtype(
        router_logits_dtype: torch.dtype | None,
        routing_method: RoutingMethodType,
    ) -> bool:
        return True

    defsupports_expert_map(self) -> bool:
        return False

    defapply(
        self,
        hidden_states: torch.Tensor,
        w1: torch.Tensor,
        w2: torch.Tensor,
        router_logits: torch.Tensor,
        activation: MoEActivation,
        global_num_experts: int,
        expert_map: torch.Tensor | None,
        a1q_scale: torch.Tensor | None,
        apply_router_weight_on_input: bool,
        # grouped topk + fused topk bias parameters
        num_expert_group: int | None = None,
        e_score_correction_bias: torch.Tensor | None = None,
        routed_scaling_factor: float | None = None,
        topk_group: int | None = None,
    ) -> torch.Tensor:
        fromvllm.model_executor.layers.fused_moe.cpu_fused_moeimport (
            select_experts,
        )

        topk_weights, topk_ids = select_experts(
            hidden_states=hidden_states,
            router_logits=router_logits,
            use_grouped_topk=num_expert_group is not None,
            top_k=self.moe_config.experts_per_token,
            renormalize=self.moe_config.routing_method
            in (
                RoutingMethodType.Renormalize,
                RoutingMethodType.RenormalizeNaive,
            ),
            topk_group=topk_group,
            num_expert_group=num_expert_group,
            scoring_func="softmax",
            routed_scaling_factor=(
                routed_scaling_factor if routed_scaling_factor is not None else 1.0
            ),
            e_score_correction_bias=e_score_correction_bias,
        )

        block_shape = (
            list(self.quant_config.block_shape)
            if self.quant_config.block_shape
            else (
                [self.quant_config._w1.shape.row, self.quant_config._w1.shape.col]
                if self.quant_config._w1.shape is not None
                else None
            )
        )

        return fused_experts_cpu(
            hidden_states,
            w1,
            w2,
            topk_weights,
            topk_ids,
            False,  # inplace
            CPUQuantMethod.FP8_W8A16,  # moe_comp_method
            self.w1_scale,  # w1_scale
            self.w2_scale,  # w2_scale
            None,  # w1_zero
            None,  # w2_zero
            block_shape,  # block_size
            True,  # is_vnni
        )
```