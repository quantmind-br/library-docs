---
title: fused_topk_router - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/router/fused_topk_router/
source: sitemap
fetched_at: 2026-05-07T21:25:31.107831035-03:00
rendered_js: false
word_count: 0
summary: This document defines the FusedTopKRouter class, which implements a standard fused top-k routing mechanism for expert selection in neural network architectures.
tags:
    - neural-networks
    - routing-logic
    - expert-models
    - fused-topk
    - python-class
    - machine-learning
category: reference
---

```
classFusedTopKRouter(BaseRouter):
"""Default router using standard fused top-k routing."""

    def__init__(
        self,
        top_k: int,
        global_num_experts: int,
        eplb_state: EplbLayerState,
        scoring_func: str = "softmax",
        renormalize: bool = True,
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
        self.renormalize = renormalize
        self.scoring_func = scoring_func

    @property
    defrouting_method_type(self) -> RoutingMethodType:
        return get_routing_method_type(
            scoring_func=self.scoring_func,
            top_k=self.top_k,
            renormalize=self.renormalize,
            num_expert_group=None,
            has_e_score_bias=False,
        )

    def_compute_routing(
        self,
        hidden_states: torch.Tensor,
        router_logits: torch.Tensor,
        indices_type: torch.dtype | None,
        *,
        input_ids: torch.Tensor | None = None,
    ) -> tuple[torch.Tensor, torch.Tensor]:
"""Compute routing using standard fused top-k."""
        topk_weights, topk_ids, token_expert_indices = fused_topk(
            hidden_states=hidden_states,
            gating_output=router_logits,
            topk=self.top_k,
            renormalize=self.renormalize,
            indices_type=indices_type,
            scoring_func=self.scoring_func,
        )

        return topk_weights, topk_ids
```