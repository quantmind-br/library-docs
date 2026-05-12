---
title: trtllm_mxfp4_moe - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/trtllm_mxfp4_moe/
source: sitemap
fetched_at: 2026-05-07T21:24:48.18154019-03:00
rendered_js: false
word_count: 0
summary: This document defines a modular implementation of the MXFP4 TRTLLM kernel for expert computation in mixture-of-experts (MoE) models, wrapping the flashinfer library's routing functionality.
tags:
    - mxfp4
    - trtllm
    - mixture-of-experts
    - flashinfer
    - kernel-implementation
    - quantization
    - moe
category: reference
---

```
classTrtLlmMxfp4ExpertsModular(TrtLlmMxfp4ExpertsBase, mk.FusedMoEExpertsModular):
"""
    Modular version of the MXFP4 TRTLLM kernel (just the experts).
    Wraps flashinfer.trtllm_fp4_block_scale_routed_moe().
    Moved from trtllm_moe.py.
    """

    @staticmethod
    def_supports_parallel_config(
        moe_parallel_config: FusedMoEParallelConfig,
    ) -> bool:
        return True

    @staticmethod
    def_supports_routing_method(
        routing_method: RoutingMethodType,
        weight_key: QuantKey | None,
        activation_key: QuantKey | None,
    ) -> bool:
        # Modular kernel handles only the expert computation;
        # routing is done externally, so accept any routing method.
        return True

    defsupports_expert_map(self) -> bool:
        return True

    deffinalize_weight_and_reduce_impl(self) -> mk.TopKWeightAndReduce:
        return TopKWeightAndReduceNoOP()

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
        # The workspaces for this implementation are managed by flashinfer.
        workspace1 = (0,)
        workspace2 = (0,)
        output = (M, self.hidden_dim_unpadded)
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
        topk = topk_ids.size(-1)
        local_num_experts = w1.size(0)
        intermediate_size = self.intermediate_size_per_partition
        local_expert_offset = self.moe_config.ep_rank * local_num_experts

        if a1q_scale is not None:
            x_quant = hidden_states
            x_scale = a1q_scale.view(torch.float8_e4m3fn)
        else:
            assert hidden_states.dtype == torch.bfloat16
            x_quant = hidden_states
            x_scale = None

        # Pack topk ids and weights into format expected by the kernel.
        packed_tensor = trtllm_moe_pack_topk_ids_weights(topk_ids, topk_weights)

        assert self.w1_scale is not None
        assert self.w2_scale is not None
        kwargs = {
            "topk_ids": packed_tensor,
            "routing_bias": None,
            "hidden_states": x_quant,
            "hidden_states_scale": x_scale,
            "gemm1_weights": w1,
            "gemm1_weights_scale": self.w1_scale,
            "gemm1_bias": self.w1_bias,
            "gemm1_alpha": self.gemm1_alpha,
            "gemm1_beta": self.gemm1_beta,
            "gemm1_clamp_limit": self.gemm1_clamp_limit,
            "gemm2_weights": w2,
            "gemm2_weights_scale": self.w2_scale,
            "gemm2_bias": self.w2_bias,
            "output1_scale_scalar": None,
            "output1_scale_gate_scalar": None,
            "output2_scale_scalar": None,
            "num_experts": global_num_experts,
            "top_k": topk,
            "n_group": None,
            "topk_group": None,
            "intermediate_size": intermediate_size,
            "local_expert_offset": local_expert_offset,
            "local_num_experts": local_num_experts,
            "routed_scaling_factor": None,
            # Modular kernel receives pre-routed tokens, so routing
            # is already done. Use Renormalize as a safe default that
            # the TRTLLM C++ kernel supports.
            "routing_method_type": RoutingMethodType.Renormalize,
            "do_finalize": True,
            "output": output,
            "tune_max_num_tokens": max(self.max_capture_size, 1),
        }

        fromflashinferimport trtllm_fp4_block_scale_routed_moe

        fromvllm.utils.flashinferimport _is_fi_autotuning, autotune

        with autotune(_is_fi_autotuning):
            trtllm_fp4_block_scale_routed_moe(**kwargs)

        return output
```