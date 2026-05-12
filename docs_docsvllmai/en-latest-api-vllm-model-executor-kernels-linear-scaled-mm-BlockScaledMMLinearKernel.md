---
title: BlockScaledMMLinearKernel - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/scaled_mm/BlockScaledMMLinearKernel/
source: sitemap
fetched_at: 2026-05-07T21:23:42.119500093-03:00
rendered_js: false
word_count: 47
summary: This document defines the Fp8BlockScaledDynamicMMLinearKernel class, which enables runtime dispatching between base and fallback FP8 block-scaled kernels in vLLM.
tags:
    - vllm
    - fp8
    - kernel-execution
    - linear-layers
    - dynamic-dispatch
    - machine-learning-kernels
category: reference
---

## vllm.model\_executor.kernels.linear.scaled\_mm.BlockScaledMMLinearKernel [¶](#vllm.model_executor.kernels.linear.scaled_mm.BlockScaledMMLinearKernel "Permanent link")

## Fp8BlockScaledDynamicMMLinearKernel [¶](#vllm.model_executor.kernels.linear.scaled_mm.BlockScaledMMLinearKernel.Fp8BlockScaledDynamicMMLinearKernel "Permanent link")

Bases: `Fp8BlockScaledMMLinearKernel`, `ABC`

Dynamic FP8 block-scaled kernel that dispatches at runtime.

Extends Fp8BlockScaledMMLinearKernel to inherit apply\_weights and overrides apply\_block\_scaled\_mm to dispatch between two sub-kernels using torch.cond.

Subclasses must define

base\_type: The primary kernel class. fallback\_type: The fallback kernel class.

Source code in `vllm/model_executor/kernels/linear/scaled_mm/BlockScaledMMLinearKernel.py`

```
classFp8BlockScaledDynamicMMLinearKernel(Fp8BlockScaledMMLinearKernel, ABC):
"""Dynamic FP8 block-scaled kernel that dispatches at runtime.

    Extends Fp8BlockScaledMMLinearKernel to inherit apply_weights and overrides
    apply_block_scaled_mm to dispatch between two sub-kernels using torch.cond.

    Subclasses must define:
        base_type:     The primary kernel class.
        fallback_type: The fallback kernel class.
    """

    base_type: ClassVar[type[Fp8BlockScaledMMLinearKernel]]
    fallback_type: ClassVar[type[Fp8BlockScaledMMLinearKernel]]

    def__init__(self, config: "FP8ScaledMMLinearLayerConfig") -> None:
        super().__init__(config)
        self.base = self.base_type(config)
        self.fallback = self.fallback_type(config)

    @classmethod
    defis_supported(
        cls, compute_capability: int | None = None
    ) -> tuple[bool, str | None]:
        is_base_supported, reason_1 = cls.base_type.is_supported(compute_capability)
        is_fallback_supported, reason_2 = cls.fallback_type.is_supported(
            compute_capability
        )
        if is_base_supported and is_fallback_supported:
            return True, None
        if not is_base_supported and not is_fallback_supported:
            return (
                False,
                f"base is not supported due to {reason_1}; "
                f"fallback is not supported due to {reason_2}",
            )
        if not is_base_supported:
            return False, f"base is not supported due to {reason_1}"
        return False, f"fallback is not supported due to {reason_2}"

    @classmethod
    defcan_implement(
        cls, config: "FP8ScaledMMLinearLayerConfig"
    ) -> tuple[bool, str | None]:
        can_implement_base, reason_1 = cls.base_type.can_implement(config)
        can_implement_fallback, reason_2 = cls.fallback_type.can_implement(config)
        if can_implement_base and can_implement_fallback:
            return True, None
        if not can_implement_base and not can_implement_fallback:
            return (
                False,
                f"base cannot implement due to {reason_1}; "
                f"fallback cannot implement due to {reason_2}",
            )
        if not can_implement_base:
            return False, f"base cannot implement due to {reason_1}"
        return False, f"fallback cannot implement due to {reason_2}"
```