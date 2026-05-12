---
title: fused_marlin_moe - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/fused_marlin_moe/
source: sitemap
fetched_at: 2026-05-07T21:24:55.189891789-03:00
rendered_js: false
word_count: 9
summary: Implements a Marlin-based fused Mixture-of-Experts (MoE) module that supports LoRA injection points for weight adaptation within high-performance inference kernels.
tags:
    - moe
    - marlin
    - lora
    - deep-learning
    - pytorch
    - kernel-optimization
    - inference
category: reference
---

```
classMarlinExperts(LoRAExpertsMixin, MarlinExpertsBase):
"""Marlin-based fused MoE expert implementation."""

    defsupports_expert_map(self) -> bool:
        return True

    deffinalize_weight_and_reduce_impl(self) -> mk.TopKWeightAndReduce:
        return TopKWeightAndReduceNoOP()

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
        # Modular Kernel provisions output buffer from workspace1. However in
        # the fused_marlin_moe() function, the final torch.sum(), is defined
        # essentially as,
        # `torch.sum(workspace1, dim=1, out=output)`
        # Having overlapping input and output tensors for torch.sum seems
        # error prone and depends on how the torch.sum is implemented.
        # For this reason we swap let the output buffer provision from
        # workspace2.

        # Workspace/IntermediateCache allocation matching fused_marlin_moe()
        # workspace1 = (M * topk * max(2 * N, K),)
        # workspace2 = (M * topk, N)

        # Workspace/IntermediateCache allocation accounting for output buffer
        # provisioning
        workspace1 = (M * topk, max(N, K))
        workspace2 = (M * topk * max(2 * N, K),)
        output = (M, K)

        return (workspace1, workspace2, output)

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
        assert self.w1_scale is not None
        assert self.w2_scale is not None

        ctx = self._lora_context
        if ctx is None:
            fused_marlin_moe(
                hidden_states=hidden_states,
                w1=w1,
                w2=w2,
                bias1=self.w1_bias,
                bias2=self.w2_bias,
                w1_scale=self.w1_scale,
                w2_scale=self.w2_scale,
                topk_weights=topk_weights,
                topk_ids=topk_ids,
                global_scale1=self.g1_alphas,
                global_scale2=self.g2_alphas,
                quant_type_id=self.quant_type_id,
                apply_router_weight_on_input=apply_router_weight_on_input,
                global_num_experts=global_num_experts,
                activation=activation,
                activation_func=self.activation,
                moe_sum=self.moe_sum,
                expert_map=expert_map,
                output=output,
                # Workspaces are swapped in workspace_shapes() to account for proper
                # output buffer allocation. Please refer to workspace_shapes().
                intermediate_cache13=workspace2,
                intermediate_cache2=workspace13,
                g_idx1=self.w13_g_idx,
                g_idx2=self.w2_g_idx,
                sort_indices1=self.w13_g_idx_sort_indices,
                sort_indices2=self.w2_g_idx_sort_indices,
                is_k_full=self.is_k_full,
                input_dtype=self.input_dtype,
            )
            return

        # LoRA path: wrap activation_func and moe_sum to inject LoRA at the
        # two natural injection points.
        #
        # Marlin uses moe_align_block_size (same as TritonExperts) so
        # intermediate_cache1 is indexed by flat (token, expert) pair index,
        # which is compatible with add_lora_fused_moe's scatter mechanism.

        M = hidden_states.size(0)
        top_k_num = topk_ids.size(1)
        lora_state: dict = {}

        defactivation_with_lora(
            act_enum: MoEActivation,
            act_output: torch.Tensor,
            act_input: torch.Tensor,
        ) -> None:
            # act_input  = intermediate_cache1 (M*topk, 2N for gated)
            # act_output = intermediate_cache2 (M*topk, N)

            (
                sorted_token_ids_lora,
                expert_ids_lora,
                num_tokens_post_padded_lora,
                token_lora_mapping,
            ) = self.apply_w13_lora(
                ctx,
                y=act_input,
                x=hidden_states,
                topk_ids=topk_ids,
                topk_weights=topk_weights,
                expert_map=expert_map,
                w1=w1,
                w2=w2,
                num_tokens=M,
                top_k_num=top_k_num,
            )
            lora_state.update(
                {
                    "sorted": sorted_token_ids_lora,
                    "eids": expert_ids_lora,
                    "npad": num_tokens_post_padded_lora,
                    "tlm": token_lora_mapping,
                }
            )
            self.activation(act_enum, act_output, act_input)
            lora_state["cache2"] = act_output

        defmoe_sum_with_lora(moe_out: torch.Tensor, out: torch.Tensor) -> None:
            # moe_out shape: (M, topk, K)
            self.apply_w2_lora(
                ctx,
                y=moe_out,
                x=lora_state["cache2"],
                topk_weights=topk_weights,
                sorted_token_ids_lora=lora_state["sorted"],
                expert_ids_lora=lora_state["eids"],
                num_tokens_post_padded_lora=lora_state["npad"],
                token_lora_mapping=lora_state["tlm"],
                num_tokens=M,
                w1=w1,
                w2=w2,
                top_k_num=top_k_num,
            )
            self.moe_sum(moe_out, out)

        return fused_marlin_moe(
            hidden_states=hidden_states,
            w1=w1,
            w2=w2,
            bias1=self.w1_bias,
            bias2=self.w2_bias,
            w1_scale=self.w1_scale,
            w2_scale=self.w2_scale,
            topk_weights=topk_weights,
            topk_ids=topk_ids,
            global_scale1=self.g1_alphas,
            global_scale2=self.g2_alphas,
            quant_type_id=self.quant_type_id,
            apply_router_weight_on_input=apply_router_weight_on_input,
            global_num_experts=global_num_experts,
            activation=activation,
            activation_func=activation_with_lora,
            moe_sum=moe_sum_with_lora,
            expert_map=expert_map,
            output=output,
            intermediate_cache13=workspace2,
            intermediate_cache2=workspace13,
            g_idx1=self.w13_g_idx,
            g_idx2=self.w2_g_idx,
            sort_indices1=self.w13_g_idx_sort_indices,
            sort_indices2=self.w2_g_idx_sort_indices,
            is_k_full=self.is_k_full,
            input_dtype=self.input_dtype,
            clamp_limit=self.gemm1_clamp_limit,
        )

    defmoe_sum(self, input: torch.Tensor, output: torch.Tensor) -> None:
        ops.moe_sum(input, output)
```