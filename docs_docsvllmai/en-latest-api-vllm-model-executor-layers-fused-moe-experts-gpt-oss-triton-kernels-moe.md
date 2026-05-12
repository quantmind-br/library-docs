---
title: gpt_oss_triton_kernels_moe - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe/
source: sitemap
fetched_at: 2026-05-07T21:24:43.508183353-03:00
rendered_js: false
word_count: 0
summary: This class implements a Triton-based Mixture of Experts (MoE) component that separates activation and summation steps to facilitate the injection of LoRA adapters.
tags:
    - triton
    - moe
    - lora
    - deep-learning
    - pytorch
    - kernel-optimization
category: concept
---

```
classUnfusedOAITritonExperts(LoRAExpertsMixin, BaseOAITritonExperts):
"""
    A Triton based MoE expert class that operates on expert standard
    format and explicitly keeps the activation and reduction (moe_sum) steps
    unfused from the matmul_ogs kernel. This exposes injection points
    for activation and moe_sum.

    One use case for it is to inject LoRA modules on the activation and moe_sum.
    """

    @staticmethod
    def_supports_activation(activation: MoEActivation) -> bool:
        return activation in [
            MoEActivation.SILU,
            MoEActivation.GELU,
            MoEActivation.SWIGLUOAI,
            MoEActivation.SWIGLUSTEP,
        ]

    @staticmethod
    defactivation_format() -> mk.FusedMoEActivationFormat:
        return mk.FusedMoEActivationFormat.Standard

    defworkspace_shapes(
        self,
        M: int,
        N: int,
        K: int,
        topk: int,
        global_num_experts: int,
        local_num_experts: int,
        expert_tokens_meta: mk.ExpertTokensMetadata | None,
        activation: MoEActivation,
    ) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
        # workspace are allocated inside the kernel
        activation_out_dim = self.adjust_N_for_activation(N, activation)
        workspace1 = (M * topk, activation_out_dim)
        workspace2 = (M * topk, max(N, K))
        output = (M, K)
        return (workspace1, workspace2, output)

    defmoe_sum(self, input: torch.Tensor, output: torch.Tensor):
        ops.moe_sum(input, output)

    defactivation(
        self,
        activation: MoEActivation,
        output: torch.Tensor,
        input: torch.Tensor,
    ) -> None:
        quant_config = self.quant_config or FUSED_MOE_UNQUANTIZED_CONFIG
        if activation == MoEActivation.SWIGLUOAI:
            alpha = (
                quant_config.gemm1_alpha
                if quant_config.gemm1_alpha is not None
                else 1.702
            )
            limit = (
                quant_config.gemm1_clamp_limit
                if quant_config.gemm1_clamp_limit is not None
                else 7.0
            )
            torch.ops._C.swigluoai_and_mul(output, input, alpha, limit)
        elif (
            activation == MoEActivation.SILU
            and quant_config.gemm1_clamp_limit is not None
        ):
            swiglu_limit_func(
                output,
                input,
                quant_config.gemm1_clamp_limit,
            )
        else:
            super().activation(activation, output, input)

    defapply(
        self,
        output: torch.Tensor,
        hidden_states: torch.Tensor,
        w1: torch.Tensor,
        w2: torch.Tensor,
        topk_weights: torch.Tensor,
        topk_ids: torch.Tensor,
        activation: MoEActivation,
        global_num_experts: int,
        expert_map: torch.Tensor | None,
        a1q_scale: torch.Tensor | None,
        a2_scale: torch.Tensor | None,
        workspace13: torch.Tensor,
        workspace2: torch.Tensor,
        expert_tokens_meta: mk.ExpertTokensMetadata | None,
        apply_router_weight_on_input: bool,
    ):
        # Use local variable to help mypy narrow the type after None check
        quant_config = self.quant_config
        if quant_config is None:
            quant_config = FUSED_MOE_UNQUANTIZED_CONFIG

        global_topk_ids = topk_ids
        if expert_map is not None:
            topk_ids = expert_map[topk_ids]

        local_num_experts = w1.shape[0]
        if global_num_experts == -1:
            global_num_experts = local_num_experts

        routing_data, gather_indx, scatter_indx = self._make_routing_data(
            topk_ids, topk_weights, local_num_experts
        )

        topk = topk_ids.size(1)

        # type check, uint8 means mxfp4
        assert hidden_states.dtype == torch.bfloat16
        assert (
            quant_config.w1_bias is None or quant_config.w1_bias.dtype == torch.float32
        )
        assert (
            quant_config.w2_bias is None or quant_config.w2_bias.dtype == torch.float32
        )

        # Shape check, only check non-mxfp4
        assert hidden_states.ndim == 2
        assert hidden_states.shape[-1] == w1.shape[-2]
        assert w2.shape[-1] == w1.shape[1]

        batch_dim = 1
        M, K = hidden_states.shape
        E, _, N = w1.shape

        if global_num_experts == -1:
            global_num_experts = E

        # Note that the output tensor might be in workspace13
        intermediate_cache1 = _resize_cache(workspace2, (batch_dim, M * topk, N))
        intermediate_cache3 = _resize_cache(workspace2, (batch_dim, M * topk, K))
        activation_out_dim = self.adjust_N_for_activation(N, activation)
        intermediate_cache2 = _resize_cache(workspace13, (M * topk, activation_out_dim))

        gammas = routing_data.gate_scal if routing_data else None

        matmul_ogs(
            hidden_states,
            w1,
            quant_config.w1_bias,
            routing_data,
            gather_indx=gather_indx,
            precision_config=quant_config.w1_precision,
            gammas=gammas if apply_router_weight_on_input else None,
            fused_activation=None,
            y=intermediate_cache1,
        )

        # w13 LoRA: gather the activation input from expert-sorted
        # intermediate_cache1, then add the LoRA delta in-place on that copy
        # before passing it to activation — exactly mirroring the old
        # decorator approach which modified the gathered tensor in-place.
        act_input = intermediate_cache1.view(-1, N)[gather_indx.dst_indx]

        sorted_token_ids_lora = None
        expert_ids_lora = None
        num_tokens_post_padded_lora = None
        token_lora_mapping = None
        lora_context = self._lora_context
        if lora_context is not None:
            (
                sorted_token_ids_lora,
                expert_ids_lora,
                num_tokens_post_padded_lora,
                token_lora_mapping,
            ) = self.apply_w13_lora(
                lora_context,
                y=act_input,
                x=hidden_states,
                topk_ids=global_topk_ids,
                topk_weights=topk_weights,
                expert_map=expert_map,
                w1=w1,
                w2=w2,
                num_tokens=M,
                top_k_num=topk,
            )

        self.activation(
            activation,
            intermediate_cache2,
            act_input,
        )

        # matmul_ogs grouped reduction fuses sum across multiple experts:
        # y[dst_indx // n_expts_act, :] += x
        # Set n_expts_act to 1 to unfuse the sum so we can do it manually via moe_sum.
        routing_data.n_expts_act = 1

        matmul_ogs(
            intermediate_cache2[gather_indx.src_indx],
            w2,
            quant_config.w2_bias,
            routing_data,
            scatter_indx=scatter_indx,
            precision_config=quant_config.w2_precision,
            gammas=None if apply_router_weight_on_input else gammas,
            y=intermediate_cache3,
        )

        # w2 LoRA: after matmul_ogs with scatter_indx, intermediate_cache3 is
        # in token-topk order, matching the (M, topk, K) layout add_lora_w2 expects.
        if lora_context is not None:
            self.apply_w2_lora(
                lora_context,
                y=intermediate_cache3.view(-1, topk, K),
                x=intermediate_cache2,
                topk_weights=topk_weights,
                sorted_token_ids_lora=sorted_token_ids_lora,
                expert_ids_lora=expert_ids_lora,
                num_tokens_post_padded_lora=num_tokens_post_padded_lora,
                token_lora_mapping=token_lora_mapping,
                num_tokens=M,
                w1=w1,
                w2=w2,
                top_k_num=topk,
            )

        self.moe_sum(intermediate_cache3.view(-1, topk, K), output)
```