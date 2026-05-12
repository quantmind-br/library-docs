---
title: lora_context - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/lora_context/
source: sitemap
fetched_at: 2026-05-07T21:24:59.795656219-03:00
rendered_js: false
word_count: 41
summary: This document defines the MoELoRAContext dataclass, which encapsulates LoRA state and metadata required to compute adapter contributions during Mixture-of-Experts forward passes in the vLLM architecture.
tags:
    - vllm
    - lora
    - mixture-of-experts
    - triton
    - kernel-optimization
    - model-executor
category: reference
---

Carries all LoRA state for one MoE forward pass.

Built by FusedMoEWithLoRA.forward() and propagated explicitly through the modular kernel path (FusedMoEKernel -&gt; FusedMoEExpertsModular.apply) so that TritonExperts.apply() can compute the LoRA contribution inline, replacing the decorator-based monkey-patch approach.

Source code in `vllm/model_executor/layers/fused_moe/lora_context.py`

```
@dataclass
classMoELoRAContext:
"""
    Carries all LoRA state for one MoE forward pass.

    Built by FusedMoEWithLoRA.forward() and propagated explicitly through the
    modular kernel path (FusedMoEKernel -> FusedMoEExpertsModular.apply) so
    that TritonExperts.apply() can compute the LoRA contribution inline,
    replacing the decorator-based monkey-patch approach.
    """

    # LoRA weight tensors (same shapes as FusedMoEWithLoRA attributes)
    w13_lora_a_stacked: tuple[torch.Tensor, ...]
    w13_lora_b_stacked: tuple[torch.Tensor, ...]
    w2_lora_a_stacked: tuple[torch.Tensor, ...]
    w2_lora_b_stacked: tuple[torch.Tensor, ...]

    # (max_loras + 1,) int32; slot 0 is the "no-adapter" sentinel
    adapter_enabled: torch.Tensor

    # Metadata
    max_loras: int
    top_k: int
    w13_num_slices: int  # 2 = gated (gate + up), 1 = non-gated or 3D-fused
    fully_sharded: bool
    tp_rank: int
    tp_size: int
    local_num_experts: int

    punica_wrapper: PunicaWrapperBase

    # Whether VLLM_TUNED_CONFIG_FOLDER is set; selects get_lora_op_configs vs
    # try_get_optimal_moe_lora_config for Triton kernel tile configs.
    use_tuned_config: bool
```