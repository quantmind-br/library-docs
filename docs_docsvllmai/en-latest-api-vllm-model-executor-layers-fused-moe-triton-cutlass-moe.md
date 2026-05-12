---
title: triton_cutlass_moe - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/triton_cutlass_moe/
source: sitemap
fetched_at: 2026-05-07T21:25:42.265881559-03:00
rendered_js: false
word_count: 0
summary: This document defines a class for selecting between Cutlass and Triton expert implementations for Mixture of Experts models, optimizing performance based on hardware capabilities and input batch size.
tags:
    - mixture-of-experts
    - model-optimization
    - triton
    - cutlass
    - gpu-acceleration
    - sm100
category: concept
---

```
classTritonOrCutlassExperts(FallbackExperts):
"""Cutlass with fallback to Triton for low latency shapes on SM100."""

    def__init__(
        self,
        moe_config: FusedMoEConfig,
        quant_config: FusedMoEQuantConfig,
    ):
        self.is_sm100 = current_platform.has_device_capability(100)
        super().__init__(
            experts=CutlassExpertsFp8(moe_config, quant_config),
            fallback_experts=TritonExperts(moe_config, quant_config),
        )

    @staticmethod
    defget_clses() -> tuple[
        type[mk.FusedMoEExpertsModular],
        type[mk.FusedMoEExpertsModular],
    ]:
        return (CutlassExpertsFp8, TritonExperts)

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
        # Small batch fallback for sm100.
        if self.is_sm100 and M <= 8:
            return self.fallback_experts.workspace_shapes(
                M,
                N,
                K,
                topk,
                global_num_experts,
                local_num_experts,
                expert_tokens_meta,
                activation,
            )
        else:
            return self.experts.workspace_shapes(
                M,
                N,
                K,
                topk,
                global_num_experts,
                local_num_experts,
                expert_tokens_meta,
                activation,
            )

    def_select_experts_impl(
        self,
        hidden_states: torch.Tensor,
        w1: torch.Tensor,
        w2: torch.Tensor,
    ) -> mk.FusedMoEExpertsModular:
        # Small batch fallback for sm100.
        if self.is_sm100 and hidden_states.shape[0] <= 8:
            return self.fallback_experts
        else:
            return self.experts
```