---
title: custom_routing_router - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/router/custom_routing_router/
source: sitemap
fetched_at: 2026-05-07T21:25:28.021673221-03:00
rendered_js: false
word_count: 28
summary: This document defines the CustomRoutingRouter class, which enables the implementation of user-provided routing functions for mixture-of-experts model architectures within vLLM.
tags:
    - vllm
    - mixture-of-experts
    - routing
    - machine-learning
    - model-executor
    - custom-function
category: reference
---

## CustomRoutingRouter [¶](#vllm.model_executor.layers.fused_moe.router.custom_routing_router.CustomRoutingRouter "Permanent link")

Bases: `BaseRouter`

Router using a custom user-provided routing function.

Source code in `vllm/model_executor/layers/fused_moe/router/custom_routing_router.py`

```
classCustomRoutingRouter(BaseRouter):
"""Router using a custom user-provided routing function."""

    def__init__(
        self,
        top_k: int,
        global_num_experts: int,
        eplb_state: EplbLayerState,
        custom_routing_function: Callable,
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
        self.custom_routing_function = custom_routing_function
        self.renormalize = renormalize

    @property
    defrouting_method_type(self) -> RoutingMethodType:
        fromvllm.model_executor.models.cohere_moeimport token_choice_with_bias
        fromvllm.model_executor.models.llama4import Llama4MoE

        # NOTE: FLASHINFER_TRTLLM support the Llama4 router.
        if self.custom_routing_function == Llama4MoE.custom_routing_function:
            return RoutingMethodType.Llama4
        # Cohere MoE uses a sigmoid -> top-k -> renormalize routing function.
        if self.custom_routing_function == token_choice_with_bias:
            return RoutingMethodType.SigmoidRenorm
        return RoutingMethodType.Custom

    def_compute_routing(
        self,
        hidden_states: torch.Tensor,
        router_logits: torch.Tensor,
        indices_type: torch.dtype | None,
        *,
        input_ids: torch.Tensor | None = None,
    ) -> tuple[torch.Tensor, torch.Tensor]:
"""Compute routing using the custom routing function."""
        topk_weights, topk_ids = self.custom_routing_function(
            hidden_states=hidden_states,
            gating_output=router_logits,
            topk=self.top_k,
            renormalize=self.renormalize,
        )

        return topk_weights.to(torch.float32), topk_ids.to(
            torch.int32 if indices_type is None else indices_type
        )
```

### \_compute\_routing [¶](#vllm.model_executor.layers.fused_moe.router.custom_routing_router.CustomRoutingRouter._compute_routing "Permanent link")

Compute routing using the custom routing function.

Source code in `vllm/model_executor/layers/fused_moe/router/custom_routing_router.py`

```
def_compute_routing(
    self,
    hidden_states: torch.Tensor,
    router_logits: torch.Tensor,
    indices_type: torch.dtype | None,
    *,
    input_ids: torch.Tensor | None = None,
) -> tuple[torch.Tensor, torch.Tensor]:
"""Compute routing using the custom routing function."""
    topk_weights, topk_ids = self.custom_routing_function(
        hidden_states=hidden_states,
        gating_output=router_logits,
        topk=self.top_k,
        renormalize=self.renormalize,
    )

    return topk_weights.to(torch.float32), topk_ids.to(
        torch.int32 if indices_type is None else indices_type
    )
```