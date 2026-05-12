---
title: fused_moe_router - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/router/fused_moe_router/
source: sitemap
fetched_at: 2026-05-07T21:25:29.318360504-03:00
rendered_js: false
word_count: 97
summary: This document defines the FusedMoERouter abstract base class, which provides a formal interface for routing hidden states to top-k experts in Mixture-of-Experts models.
tags:
    - fused-moe
    - router-logic
    - machine-learning
    - vllm
    - abstract-base-class
    - tensor-routing
category: reference
---

Bases: `ABC`

FusedMoERouter is an abstract class that provides a 'select\_experts' method that is used for routing hidden states based on router logits.

Source code in `vllm/model_executor/layers/fused_moe/router/fused_moe_router.py`

```
classFusedMoERouter(ABC):
"""
    FusedMoERouter is an abstract class that provides a 'select_experts'
    method that is used for routing hidden states based on router logits.
    """

    @abstractmethod
    defset_capture_fn(
        self,
        capture_fn: Callable[[torch.Tensor], None] | None,
    ) -> None:
        raise NotImplementedError

    @property
    @abstractmethod
    defrouting_method_type(self) -> RoutingMethodType:
        raise NotImplementedError

    @abstractmethod
    defselect_experts(
        self,
        hidden_states: torch.Tensor,
        router_logits: torch.Tensor,
        *,
        input_ids: torch.Tensor | None = None,
    ) -> tuple[torch.Tensor, torch.Tensor]:
"""
        Route the input hidden states to the top-k experts based on the
        router logits.

        Returns:
            (topk_weights, topk_ids)
            (tuple[torch.Tensor, torch.Tensor]):
            The weights and expert ids computation result.

            **Compatibility**: When EPLB is not enabled, the returned ids are
            equivalent to global logical ids, so should be compatible with
            plain MoE implementations without redundant experts.
        """
        raise NotImplementedError
```

### select\_experts `abstractmethod` [¶](#vllm.model_executor.layers.fused_moe.router.fused_moe_router.FusedMoERouter.select_experts "Permanent link")

Route the input hidden states to the top-k experts based on the router logits.

Returns:

Type Description `Tensor`

(topk\_weights, topk\_ids)

`tuple[Tensor, Tensor]` `tuple[Tensor, Tensor]`

The weights and expert ids computation result.

`tuple[Tensor, Tensor]`

**Compatibility**: When EPLB is not enabled, the returned ids are

`tuple[Tensor, Tensor]`

equivalent to global logical ids, so should be compatible with

`tuple[Tensor, Tensor]`

plain MoE implementations without redundant experts.

Source code in `vllm/model_executor/layers/fused_moe/router/fused_moe_router.py`

```
@abstractmethod
defselect_experts(
    self,
    hidden_states: torch.Tensor,
    router_logits: torch.Tensor,
    *,
    input_ids: torch.Tensor | None = None,
) -> tuple[torch.Tensor, torch.Tensor]:
"""
    Route the input hidden states to the top-k experts based on the
    router logits.

    Returns:
        (topk_weights, topk_ids)
        (tuple[torch.Tensor, torch.Tensor]):
        The weights and expert ids computation result.

        **Compatibility**: When EPLB is not enabled, the returned ids are
        equivalent to global logical ids, so should be compatible with
        plain MoE implementations without redundant experts.
    """
    raise NotImplementedError
```