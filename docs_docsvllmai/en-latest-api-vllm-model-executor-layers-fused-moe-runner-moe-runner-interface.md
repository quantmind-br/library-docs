---
title: moe_runner_interface - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/runner/moe_runner_interface/
source: sitemap
fetched_at: 2026-05-07T21:25:38.979345616-03:00
rendered_js: false
word_count: 48
summary: This document defines the abstract base class for Mixture of Experts (MoE) runners, establishing the required interface for execution, expert routing, and tensor parallel operations.
tags:
    - moe-runner
    - abstract-base-class
    - mixture-of-experts
    - model-execution
    - tensor-parallelism
category: reference
---

Bases: `PluggableLayer`, `ABC`

Abstract base class for Mixture of Experts (MoE) runners.

This class defines the interface that all MoE runner implementations must follow. MoE runners are responsible for executing the forward pass of MoE layers, handling expert routing, and managing tensor parallel operations.

Source code in `vllm/model_executor/layers/fused_moe/runner/moe_runner_interface.py`

```
classMoERunnerInterface(PluggableLayer, ABC):
"""
    Abstract base class for Mixture of Experts (MoE) runners.

    This class defines the interface that all MoE runner implementations must follow.
    MoE runners are responsible for executing the forward pass of MoE layers, handling
    expert routing, and managing tensor parallel operations.
    """

    @abstractmethod
    defforward(
        self,
        hidden_states: torch.Tensor,
        router_logits: torch.Tensor,
        input_ids: torch.Tensor | None = None,
    ) -> torch.Tensor:
        raise NotImplementedError

    @abstractmethod
    defis_internal_router(self) -> bool:
        raise NotImplementedError

    @property
    @abstractmethod
    defshared_experts(self) -> SharedExperts | None:
        raise NotImplementedError

    # TODO(bnell): temporary hack, do not call this method.
    @abstractmethod
    def_replace_quant_method(self, quant_method: FusedMoEMethodBase):
        raise NotImplementedError
```