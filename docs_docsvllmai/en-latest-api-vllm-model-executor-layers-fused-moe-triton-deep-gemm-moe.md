---
title: triton_deep_gemm_moe - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/triton_deep_gemm_moe/
source: sitemap
fetched_at: 2026-05-07T21:25:43.423764769-03:00
rendered_js: false
word_count: 0
summary: This document defines a hybrid expert class that dynamically selects between DeepGemm and Triton implementations based on performance heuristics and input shapes for mixture-of-experts models.
tags:
    - mixture-of-experts
    - deepgemm
    - triton
    - kernel-selection
    - model-optimization
    - fallback-logic
category: concept
---

```
classTritonOrDeepGemmExperts(FallbackExperts):
"""DeepGemm with fallback to Triton for low latency shapes."""

    def__init__(self, moe_config: FusedMoEConfig, quant_config: FusedMoEQuantConfig):
        super().__init__(
            experts=DeepGemmExperts(moe_config, quant_config),
            fallback_experts=TritonExperts(moe_config, quant_config),
        )

    @staticmethod
    defget_clses() -> tuple[
        type[mk.FusedMoEExpertsModular],
        type[mk.FusedMoEExpertsModular],
    ]:
        return (DeepGemmExperts, TritonExperts)

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
        # Note: the deep gemm workspaces are strictly larger than the triton
        # workspaces so we can be pessimistic here and allocate for DeepGemm
        # even if we fall back to triton later, e.g. if expert maps are set.
        if is_deep_gemm_e8m0_used() or _valid_deep_gemm_shape(M, N, K):
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
        else:
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

    def_select_experts_impl(
        self,
        hidden_states: torch.Tensor,
        w1: torch.Tensor,
        w2: torch.Tensor,
    ) -> mk.FusedMoEExpertsModular:
        if is_deep_gemm_e8m0_used() or _valid_deep_gemm(hidden_states, w1, w2):
            return self.experts
        else:
            return self.fallback_experts
```