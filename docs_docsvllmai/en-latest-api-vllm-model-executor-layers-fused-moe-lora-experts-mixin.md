---
title: lora_experts_mixin - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/lora_experts_mixin/
source: sitemap
fetched_at: 2026-05-07T21:25:00.897951952-03:00
rendered_js: false
word_count: 0
summary: This document defines a mixin class that enables Mixture-of-Experts (MoE) modular components to natively support and apply LoRA adapters using Punica kernel wrappers.
tags:
    - lora
    - moe
    - deep-learning
    - pytorch
    - mixin
    - adapter-optimization
category: api
---

```
classLoRAExpertsMixin:
"""
    Mixin for FusedMoEExpertsModular subclasses that natively handle
    MoELoRAContext inside their apply() implementation.

    Mixing this class in:
    - Flips supports_lora() to True so _can_fused_experts_support lets
      LoRA through the gate check.
    - Stashes a MoELoRAContext on the experts instance via
      set_lora_context(), which apply() consumes from self._lora_context.
    - Provides apply_w13_lora / apply_w2_lora helpers that dispatch to
      the PunicaWrapper kernels.

    The helper methods are pure functions of their inputs; all required
    state is on lora_context or passed as arguments.
    """

    _lora_context: MoELoRAContext | None = None

    defset_lora_context(self, ctx: MoELoRAContext) -> None:
        self._lora_context = ctx

    @staticmethod
    defsupports_lora() -> bool:
        return True

    defapply_w13_lora(
        self,
        lora_context: MoELoRAContext,
        *,
        y: torch.Tensor,
        x: torch.Tensor,
        topk_ids: torch.Tensor,
        topk_weights: torch.Tensor,
        expert_map: torch.Tensor | None,
        w1: torch.Tensor,
        w2: torch.Tensor,
        num_tokens: int,
        top_k_num: int,
    ) -> tuple[
        torch.Tensor | None,
        torch.Tensor | None,
        torch.Tensor | None,
        torch.Tensor | None,
    ]:
        return lora_context.punica_wrapper.add_lora_w13(
            y,
            x,
            lora_context.w13_lora_a_stacked,
            lora_context.w13_lora_b_stacked,
            topk_ids,
            topk_weights,
            expert_map,
            w1,
            w2,
            num_tokens,
            top_k_num,
            lora_context.max_loras,
            lora_context.adapter_enabled,
            lora_context.local_num_experts,
            lora_context.top_k,
            lora_context.w13_num_slices,
            lora_context.fully_sharded,
            lora_context.use_tuned_config,
        )

    defapply_w2_lora(
        self,
        lora_context: MoELoRAContext,
        *,
        y: torch.Tensor,
        x: torch.Tensor,
        topk_weights: torch.Tensor,
        sorted_token_ids_lora: torch.Tensor | None,
        expert_ids_lora: torch.Tensor | None,
        num_tokens_post_padded_lora: torch.Tensor | None,
        token_lora_mapping: torch.Tensor | None,
        num_tokens: int,
        w1: torch.Tensor,
        w2: torch.Tensor,
        top_k_num: int,
    ) -> None:
        lora_context.punica_wrapper.add_lora_w2(
            y,
            x,
            lora_context.w2_lora_a_stacked,
            lora_context.w2_lora_b_stacked,
            topk_weights,
            sorted_token_ids_lora,
            expert_ids_lora,
            num_tokens_post_padded_lora,
            token_lora_mapping,
            num_tokens,
            w1,
            w2,
            top_k_num,
            lora_context.max_loras,
            lora_context.adapter_enabled,
            lora_context.top_k,
            lora_context.fully_sharded,
            lora_context.tp_rank,
            lora_context.use_tuned_config,
        )
```