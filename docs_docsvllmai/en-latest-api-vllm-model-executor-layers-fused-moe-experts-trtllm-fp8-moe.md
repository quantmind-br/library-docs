---
title: trtllm_fp8_moe - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe/
source: sitemap
fetched_at: 2026-05-07T21:24:47.513310541-03:00
rendered_js: false
word_count: 0
summary: This class implements FP8 monolithic kernels for Mixture-of-Experts (MoE) layers within the TRTLLM framework, providing mechanisms for both per-tensor and block-level quantization.
tags:
    - fp8-quantization
    - mixture-of-experts
    - trtllm
    - flashinfer
    - deep-learning-kernels
    - tensor-scaling
category: api
---

```
classTrtLlmFp8ExpertsMonolithic(TrtLlmFp8ExpertsBase, mk.FusedMoEExpertsMonolithic):
"""
    Fp8 TRTLLM-Gen MoE kernels. Supports monolithic interface.
    """

    def__init__(
        self,
        moe_config: FusedMoEConfig,
        quant_config: FusedMoEQuantConfig,
    ):
        super().__init__(moe_config, quant_config)

        # Make additional scales for per-tensor interface.
        if self.quant_config.is_per_tensor:
            w1_scale = self.quant_config.w1_scale
            assert w1_scale is not None
            a1_scale = self.quant_config.a1_scale
            assert a1_scale is not None
            w2_scale = self.quant_config.w2_scale
            assert w2_scale is not None
            a2_scale = self.quant_config.a2_scale
            assert a2_scale is not None

            self._g1_alphas = (w1_scale * a1_scale).squeeze()
            self._g2_alphas = (w2_scale * a2_scale).squeeze()
            self._g1_scale_c = (
                self._g1_alphas / self.quant_config.a2_scale
                if moe_config.is_act_and_mul
                else torch.ones_like(self._g1_alphas) / self.quant_config.a2_scale
            )

    @staticmethod
    def_supports_quant_scheme(
        weight_key: QuantKey | None,
        activation_key: QuantKey | None,
    ) -> bool:
"""Supports Fp8 per-tensor, Fp8 block, and MXFP8."""
        SUPPORTED_W_A = [
            (kFp8Static128BlockSym, kFp8Dynamic128Sym),
            (kFp8StaticTensorSym, kFp8StaticTensorSym),
            (kMxfp8Static, kMxfp8Dynamic),
        ]
        return (weight_key, activation_key) in SUPPORTED_W_A

    @staticmethod
    def_supports_router_logits_dtype(
        router_logits_dtype: torch.dtype | None,
        routing_method: RoutingMethodType,
    ) -> bool:
        return True

    @staticmethod
    def_supports_routing_method(
        routing_method: RoutingMethodType,
        weight_key: QuantKey | None,
        activation_key: QuantKey | None,
    ) -> bool:
"""Monolithic kernels need to express router support."""
        # NOTE(dbari): TopK routing could also be enabled, but need to validate models
        # NOTE(dbari): Default is not implemented and should not be enabled until it is

        if (weight_key, activation_key) in [
            (kFp8Static128BlockSym, kFp8Dynamic128Sym),
            (kMxfp8Static, kMxfp8Dynamic),
        ]:
            # NOTE(rob): potentially allow others here. This is a conservative list.
            return routing_method in [
                RoutingMethodType.DeepSeekV3,
                RoutingMethodType.Renormalize,
                RoutingMethodType.RenormalizeNaive,
                RoutingMethodType.SigmoidRenorm,
                RoutingMethodType.MiniMax2,
                RoutingMethodType.Simulated,
            ]
        elif (weight_key, activation_key) == (kFp8StaticTensorSym, kFp8StaticTensorSym):
            # NOTE(dbari): as above, potentially allow others here.
            return routing_method in [
                RoutingMethodType.DeepSeekV3,
                RoutingMethodType.Llama4,
                RoutingMethodType.Renormalize,
                RoutingMethodType.RenormalizeNaive,
                RoutingMethodType.SigmoidRenorm,
                RoutingMethodType.MiniMax2,
                RoutingMethodType.Simulated,
            ]
        else:
            raise ValueError("Unsupported quantization scheme.")

    def_apply_block_scale(
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
        importflashinfer
        fromflashinfer.fused_moeimport Fp8QuantizationType, WeightLayout

        assert not apply_router_weight_on_input
        assert activation == MoEActivation.SILU
        assert self.topk <= global_num_experts
        assert self.topk <= 10
        assert global_num_experts % 4 == 0
        assert self.quant_config.block_shape in [[128, 128], [1, 32]]
        # Kernel expects #experts <= #threads 512
        assert global_num_experts <= 512
        # TODO: fuse into the quant kernel.
        assert a1q_scale is not None

        is_mxfp8 = self.quant_config.block_shape == [1, 32]
        if is_mxfp8:
            fp8_quant_type = Fp8QuantizationType.MxFp8
            use_shuffled_weight = True
            weight_layout = WeightLayout.MajorK
            hidden_states_scale = a1q_scale
        else:
            fp8_quant_type = Fp8QuantizationType.DeepSeekFp8
            use_shuffled_weight = True
            weight_layout = WeightLayout.BlockMajorK
            hidden_states_scale = a1q_scale.t().contiguous()

        return flashinfer.fused_moe.trtllm_fp8_block_scale_moe(
            routing_logits=router_logits,
            routing_bias=e_score_correction_bias,
            hidden_states=hidden_states,
            hidden_states_scale=hidden_states_scale,
            gemm1_weights=w1,
            gemm1_weights_scale=self.quant_config.w1_scale,
            gemm2_weights=w2,
            gemm2_weights_scale=self.quant_config.w2_scale,
            num_experts=global_num_experts,
            top_k=self.topk,
            n_group=(num_expert_group or 0),
            topk_group=(topk_group or 0),
            intermediate_size=self.intermediate_size_per_partition,
            local_expert_offset=self.ep_rank * self.local_num_experts,
            local_num_experts=self.local_num_experts,
            routed_scaling_factor=routed_scaling_factor,
            routing_method_type=self.routing_method_type,
            use_shuffled_weight=use_shuffled_weight,
            weight_layout=weight_layout,
            fp8_quantization_type=fp8_quant_type,
        )

    def_apply_per_tensor(
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
        # Delay import for non-CUDA.
        importflashinfer

        # Confirm supported activation function.
        assert activation in [MoEActivation.SILU, MoEActivation.RELU2_NO_MUL]

        activation_type = activation_to_flashinfer_int(activation)

        # Confirm Llama-4 routing is proper.
        if self.routing_method_type == RoutingMethodType.Llama4:
            assert apply_router_weight_on_input
        else:
            assert not apply_router_weight_on_input

        # Currently FI requires bfloat16 routing bias.
        # https://github.com/flashinfer-ai/flashinfer/issues/2909
        if e_score_correction_bias is not None:
            e_score_correction_bias = e_score_correction_bias.to(torch.bfloat16)

        out = flashinfer.fused_moe.trtllm_fp8_per_tensor_scale_moe(
            routing_logits=router_logits,
            routing_bias=e_score_correction_bias,
            hidden_states=hidden_states,
            gemm1_weights=w1,
            output1_scales_scalar=self._g1_scale_c,
            output1_scales_gate_scalar=self._g1_alphas,
            gemm2_weights=w2,
            output2_scales_scalar=self._g2_alphas,
            num_experts=global_num_experts,
            top_k=self.topk,
            n_group=num_expert_group or 0,
            topk_group=topk_group or 0,
            intermediate_size=self.intermediate_size_per_partition,
            local_expert_offset=self.ep_rank * self.local_num_experts,
            local_num_experts=self.local_num_experts,
            routed_scaling_factor=routed_scaling_factor,
            use_routing_scales_on_input=apply_router_weight_on_input,
            routing_method_type=self.routing_method_type,
            activation_type=activation_type,
        )
        return out

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
        if self.quant_config.block_shape is not None:
            return self._apply_block_scale(
                hidden_states,
                w1,
                w2,
                router_logits,
                activation,
                global_num_experts,
                expert_map,
                a1q_scale,
                apply_router_weight_on_input,
                num_expert_group=num_expert_group,
                e_score_correction_bias=e_score_correction_bias,
                routed_scaling_factor=routed_scaling_factor,
                topk_group=topk_group,
            )
        elif self.quant_config.is_per_tensor:
            return self._apply_per_tensor(
                hidden_states,
                w1,
                w2,
                router_logits,
                activation,
                global_num_experts,
                expert_map,
                a1q_scale,
                apply_router_weight_on_input,
                num_expert_group=num_expert_group,
                e_score_correction_bias=e_score_correction_bias,
                routed_scaling_factor=routed_scaling_factor,
            )
        else:
            raise NotImplementedError(
                "Only per-block, per-tensor, and MXFP8 quantization are "
                f"supported in {self.__class__.__name__}."
            )
```