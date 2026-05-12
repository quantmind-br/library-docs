---
title: grouped_topk_router - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/router/grouped_topk_router/
source: sitemap
fetched_at: 2026-05-07T21:25:33.054668188-03:00
rendered_js: false
word_count: 0
summary: This document defines the ClassGroupedTopKRouter, which implements a grouped top-k routing strategy for mixture-of-experts models, supporting fused kernel operations for efficiency.
tags:
    - mixture-of-experts
    - deep-learning
    - neural-network-router
    - grouped-top-k
    - torch-implementation
    - model-architecture
category: reference
---

```
classGroupedTopKRouter(BaseRouter):
"""Router using grouped top-k routing (e.g., DeepSeekV2/V3)."""

    def__init__(
        self,
        top_k: int,
        global_num_experts: int,
        eplb_state: EplbLayerState,
        num_expert_group: int,
        topk_group: int,
        renormalize: bool = True,
        scoring_func: str = "softmax",
        routed_scaling_factor: float = 1.0,
        e_score_correction_bias: torch.Tensor | None = None,
        num_fused_shared_experts: int = 0,
        enable_eplb: bool = False,
        indices_type_getter: Callable[[], torch.dtype | None] | None = None,
    ):
        super().__init__(
            top_k=top_k,
            global_num_experts=global_num_experts,
            eplb_state=eplb_state,
            enable_eplb=enable_eplb,
            indices_type_getter=indices_type_getter,
        )
        self.num_expert_group = num_expert_group
        self.topk_group = topk_group
        self.renormalize = renormalize
        self.scoring_func = scoring_func
        self.routed_scaling_factor = routed_scaling_factor
        self.e_score_correction_bias = e_score_correction_bias
        self.num_fused_shared_experts = num_fused_shared_experts

    @property
    defrouting_method_type(self) -> RoutingMethodType:
        return get_routing_method_type(
            scoring_func=self.scoring_func,
            top_k=self.top_k,
            renormalize=self.renormalize,
            num_expert_group=self.num_expert_group,
            has_e_score_bias=self.e_score_correction_bias is not None,
        )

    def_compute_routing(
        self,
        hidden_states: torch.Tensor,
        router_logits: torch.Tensor,
        indices_type: torch.dtype | None,
        *,
        input_ids: torch.Tensor | None = None,
    ) -> tuple[torch.Tensor, torch.Tensor]:
"""Compute routing using grouped top-k."""

        defvalid_grouping() -> bool:
            # Check if num_experts is greater than num_expert_group
            # and is divisible by num_expert_group
            num_experts = router_logits.shape[-1]
            if num_experts <= self.num_expert_group:
                return False
            return num_experts % self.num_expert_group == 0

        if not valid_grouping():
            if self.e_score_correction_bias is not None:
                topk_weights, topk_ids = fused_topk_bias(
                    hidden_states=hidden_states,
                    gating_output=router_logits,
                    scoring_func=self.scoring_func,
                    e_score_correction_bias=self.e_score_correction_bias.data,
                    topk=self.top_k,
                    renormalize=self.renormalize,
                )
                if self.routed_scaling_factor != 1.0:
                    topk_weights *= self.routed_scaling_factor
            else:
                topk_weights, topk_ids, token_expert_indices = fused_topk(
                    hidden_states=hidden_states,
                    gating_output=router_logits,
                    topk=self.top_k,
                    renormalize=self.renormalize,
                    indices_type=indices_type,
                )
            return topk_weights, topk_ids

        # Select grouped_topk implementation
        if rocm_aiter_ops.is_fused_moe_enabled():
            if not rocm_aiter_ops.is_fusion_moe_shared_experts_enabled():
                assert self.num_fused_shared_experts == 0
            grouped_topk_impl = partial(
                rocm_aiter_grouped_topk,
                num_fused_shared_experts=self.num_fused_shared_experts,
            )
        else:
            grouped_topk_impl = grouped_topk

        topk_weights, topk_ids = grouped_topk_impl(
            hidden_states=hidden_states,
            gating_output=router_logits,
            topk=self.top_k,
            renormalize=self.renormalize,
            num_expert_group=self.num_expert_group,
            topk_group=self.topk_group,
            scoring_func=self.scoring_func,
            routed_scaling_factor=self.routed_scaling_factor,
            e_score_correction_bias=self.e_score_correction_bias,
        )

        return topk_weights, topk_ids
```