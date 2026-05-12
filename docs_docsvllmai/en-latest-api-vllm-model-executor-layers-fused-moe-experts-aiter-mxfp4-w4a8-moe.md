---
title: aiter_mxfp4_w4a8_moe - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/aiter_mxfp4_w4a8_moe/
source: sitemap
fetched_at: 2026-05-07T21:24:37.240932663-03:00
rendered_js: false
word_count: 0
summary: This document defines the AiterW4A8ExpertsMonolithic class, which implements a monolithic Mixture-of-Experts (MoE) backend using Triton kernels for W4A8 quantization on GFX950 hardware.
tags:
    - moe
    - triton
    - quantization
    - w4a8
    - mxfp4
    - rocm
    - kernel-implementation
category: reference
---

```
classAiterW4A8ExpertsMonolithic(mk.FusedMoEExpertsMonolithic):
"""
    Monolithic MXFP4 W4A8 expert using AITER triton kernels.

    This backend uses:
    - aiter.ops.triton.moe_routing.routing for routing
    - aiter.ops.triton.moe_op_gemm_a8w4.moe_gemm_a8w4 for computation

    Weight format: MXFP4 weights with GFX950 swizzle
    Activation: Static FP8 quantization
    """

    def__init__(
        self,
        moe_config: FusedMoEConfig,
        quant_config: FusedMoEQuantConfig,
    ):
        super().__init__(moe_config, quant_config)
        self.topk = moe_config.experts_per_token
        self.renormalize = moe_config.routing_method in (
            RoutingMethodType.Renormalize,
            RoutingMethodType.RenormalizeNaive,
        )

    @staticmethod
    defactivation_format() -> mk.FusedMoEActivationFormat:
        return mk.FusedMoEActivationFormat.Standard

    @staticmethod
    def_supports_current_device() -> bool:
        # Requires AITER and GFX950
        if not rocm_aiter_ops.is_enabled():
            return False
        fromvllm.platforms.rocmimport on_gfx950

        return on_gfx950()

    @staticmethod
    def_supports_no_act_and_mul() -> bool:
        return False

    @staticmethod
    def_supports_quant_scheme(
        weight_key: QuantKey | None,
        activation_key: QuantKey | None,
    ) -> bool:
        # W4A8: MXFP4 weights with static FP8 activations
        SUPPORTED_W_A = [
            (kMxfp4Static, kFp8StaticTensorSym),
        ]
        return (weight_key, activation_key) in SUPPORTED_W_A

    @staticmethod
    def_supports_activation(activation: MoEActivation) -> bool:
        # Only SILU activation (swiglu) is supported
        return activation == MoEActivation.SWIGLUOAI

    @staticmethod
    def_supports_parallel_config(
        moe_parallel_config: FusedMoEParallelConfig,
    ) -> bool:
        return (
            not moe_parallel_config.use_all2all_kernels
            and not moe_parallel_config.enable_eplb
            and moe_parallel_config.dp_size <= 1
        )

    @staticmethod
    def_supports_routing_method(
        routing_method: RoutingMethodType,
        weight_key: QuantKey | None,
        activation_key: QuantKey | None,
    ) -> bool:
        return routing_method in [
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
        return False  # Expert parallelism not yet supported

    @property
    defexpects_unquantized_inputs(self) -> bool:
        return True

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
        assert self.moe_config.intermediate_size_per_partition_unpadded is not None
        assert self.moe_config.hidden_dim_unpadded is not None
        return aiter_triton_kernel_w4a8_moe_forward(
            hidden_states=hidden_states,
            w1=w1,
            w2=w2,
            gating_output=router_logits,
            topk=self.topk,
            renormalize=self.renormalize,
            global_num_experts=global_num_experts,
            expert_map=expert_map,
            quant_config=self.quant_config,
            apply_router_weight_on_input=apply_router_weight_on_input,
            unpadded_N_w1=self.moe_config.intermediate_size_per_partition_unpadded * 2,
            unpadded_K_w1=self.moe_config.hidden_dim_unpadded,
            unpadded_N_w2=self.moe_config.hidden_dim_unpadded,
            unpadded_K_w2=self.moe_config.intermediate_size_per_partition_unpadded,
        )
```