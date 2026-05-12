---
title: act_quant_fusion - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/fusion/act_quant_fusion/
source: sitemap
fetched_at: 2026-05-07T21:16:21.935316621-03:00
rendered_js: false
word_count: 0
summary: This document defines a quantization pattern class for fusing SiluMul operations with dynamic per-group FP8 quantization. It provides the necessary structure to match patterns and define replacements for optimized tensor computation.
tags:
    - quantization
    - fp8
    - torch
    - tensor-fusion
    - neural-network-optimization
    - performance-tuning
category: api
---

```
classSiluMulBlockQuantPattern(ActivationQuantPattern):
"""
    Fusion for SiluMul+BlockQuant (FP8 dynamic per-group) Pattern.
    Supports group_size 128 and 64 via QuantKey.
    Parameterized on is_scale_transposed for different scale layouts.
    """

    def__init__(
        self,
        quant_key: QuantKey,
        is_scale_transposed: bool = False,
        is_e8m0: bool = False,
        is_tma_aligned: bool = False,
        match_aiter: bool = False,
    ) -> None:
        super().__init__(quant_key)
        self.quant_matcher = MatcherQuantFP8(
            quant_key,
            has_col_major_scales=is_scale_transposed,
            is_e8m0=is_e8m0,
            is_tma_aligned=is_tma_aligned,
        )
        self.group_size = quant_key.scale.group_shape[1]
        self.is_scale_transposed = is_scale_transposed
        self.is_e8m0 = is_e8m0
        self.is_tma_aligned = is_tma_aligned

    defget_inputs(self) -> list[torch.Tensor]:
        scale = self.quant_matcher.empty_f32(1, 1)
        return self.silu_and_mul_matcher.inputs() + [scale]

    @property
    defpattern(self):
        def_pattern(
            input: torch.Tensor,
            scale: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor]:
            silu_out = self.silu_and_mul_matcher(input)
            result = torch.empty(
                silu_out.shape,
                device=silu_out.device,
                dtype=self.quant_dtype,
            )
            assert scale is not None
            finfo = torch.finfo(self.quant_dtype)
            _, result, scale = auto_functionalized(
                self.quant_matcher.QUANT_OP,
                input=silu_out,
                output_q=result,
                output_s=scale,
                group_size=self.group_size,
                eps=1e-10,
                fp8_min=finfo.min,
                fp8_max=finfo.max,
                scale_ue8m0=self.is_e8m0,
                dummy_is_scale_transposed=self.is_scale_transposed,
                dummy_is_tma_aligned=self.is_tma_aligned,
            )
            return result, scale

        return _pattern

    @property
    defreplacement(self):
        def_replacement(
            input: torch.Tensor,
            scale: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor]:
            d = input.shape[-1] // 2
            output_shape = input.shape[:-1] + (d,)
            result = torch.empty(
                output_shape, device=input.device, dtype=self.quant_dtype
            )
            if self.is_scale_transposed:
                scale = torch.empty(
                    (d // self.group_size, input.shape[0]),
                    device=input.device,
                    dtype=torch.float32,
                ).permute(-1, -2)
            else:
                scale = torch.empty(
                    (input.shape[0], d // self.group_size),
                    device=input.device,
                    dtype=torch.float32,
                )
            at = auto_functionalized(
                self.FUSED_OP,
                out=result,
                input=input,
                scales=scale,
                group_size=self.group_size,
                scale_ub=None,
                is_scale_transposed=self.is_scale_transposed,
            )
            return at[1], at[2]

        return _replacement
```