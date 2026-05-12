---
title: allreduce_rms_fusion - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/fusion/allreduce_rms_fusion/
source: sitemap
fetched_at: 2026-05-07T21:16:22.941377859-03:00
rendered_js: false
word_count: 247
summary: This document defines compiler optimization patterns that replace discrete all-reduce, RMS norm, and quantization operations with fused FlashInfer implementations to improve performance.
tags:
    - vllm
    - flashinfer
    - fusion
    - compilation
    - all-reduce
    - rms-norm
    - quantization
    - tensor-parallelism
category: reference
---

## AllReduceFusedAddRMSNormPattern [¶](#vllm.compilation.passes.fusion.allreduce_rms_fusion.AllReduceFusedAddRMSNormPattern "Permanent link")

Bases: `BasePattern`

This pattern replaces the allreduce + rms norm (with residual) with fused flashinfer implementation. Applies to o\_proj + rmsnorm after attn and mlp + rmsnorm before attn.

Source code in `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`

```
classAllReduceFusedAddRMSNormPattern(BasePattern):
"""
    This pattern replaces the allreduce + rms norm (with residual)
    with fused flashinfer implementation.
    Applies to o_proj + rmsnorm after attn and mlp + rmsnorm before attn.
    """

    def__init__(
        self,
        epsilon: float,
        dtype: torch.dtype,
        device: str | None,
        allreduce_params: FlashInferFusedAllReduceParams,
    ) -> None:
        super().__init__(dtype, device)
        self.epsilon = epsilon
        self.allreduce_params = allreduce_params

    defget_inputs(self) -> list[torch.Tensor]:
        input = self.empty(5, 16)
        residual = self.empty(5, 16)
        weight = self.empty(16)

        # input goes through allreduce first, always 16-bit
        return [residual, input.to(self.dtype), weight]

    defregister(self, pm_pass: PatternMatcherPass) -> None:
        defpattern(
            residual: torch.Tensor, input: torch.Tensor, weight: torch.Tensor
        ) -> tuple[torch.Tensor, torch.Tensor]:
            allreduce_output = tensor_model_parallel_all_reduce(input)
            rms, residual = vllm.ir.ops.fused_add_rms_norm(
                allreduce_output, residual, weight, self.epsilon
            )
            return rms, residual

        defreplacement(
            residual: torch.Tensor, input: torch.Tensor, weight: torch.Tensor
        ) -> tuple[torch.Tensor, torch.Tensor]:
            assert flashinfer_comm is not None, "FlashInfer must be enabled"
            allreduce = auto_functionalized(
                flashinfer_trtllm_fused_allreduce_norm,
                allreduce_in=input,
                residual=residual,
                norm_out=None,
                quant_out=None,
                scale_out=None,
                rms_gamma=weight,
                rms_eps=self.epsilon,
                pattern_code=flashinfer_comm.AllReduceFusionPattern.kARResidualRMSNorm,
                **self.allreduce_params.get_trtllm_fused_allreduce_kwargs(),
            )
            # allreduce_in, residual
            return allreduce[1], allreduce[2]

        pm.register_replacement(
            pattern, replacement, self.get_inputs(), pm.fwd_only, pm_pass
        )

        # Same pattern, but only return the output and not residual
        # (helpful for end of graph where residual is not used again)
        first_return_only = lambda fn: lambda a, b, c: fn(a, b, c)[0]

        pm.register_replacement(
            first_return_only(pattern),  # type: ignore[no-untyped-call]
            first_return_only(replacement),  # type: ignore[no-untyped-call]
            self.get_inputs(),
            pm.fwd_only,
            pm_pass,
        )
```

## AllReduceFusedAddRMSNormStaticQuantFP8Pattern [¶](#vllm.compilation.passes.fusion.allreduce_rms_fusion.AllReduceFusedAddRMSNormStaticQuantFP8Pattern "Permanent link")

Bases: `BasePattern`

This pattern replaces the allreduce + rms norm (with residual) + static fp8 quant with fused flashinfer implementation. Applies to o\_proj + rmsnorm after attn + quant and mlp + rmsnorm + quant before attn.

Source code in `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`

```
classAllReduceFusedAddRMSNormStaticQuantFP8Pattern(BasePattern):
"""
    This pattern replaces the allreduce + rms norm (with residual)
    + static fp8 quant with fused flashinfer implementation.
    Applies to o_proj + rmsnorm after attn + quant and
    mlp + rmsnorm + quant before attn.
    """

    def__init__(
        self,
        epsilon: float,
        dtype: torch.dtype,
        device: str | None,
        allreduce_params: FlashInferFusedAllReduceParams,
    ) -> None:
        super().__init__(dtype, device)
        self.epsilon = epsilon
        self.allreduce_params = allreduce_params
        self.quant_dtype = torch.float8_e4m3fn

        self.quant_matcher = MatcherQuantFP8(kFp8StaticTensorSym)

    defget_inputs(self) -> list[torch.Tensor]:
        input = self.empty(5, 16)
        residual = self.empty(5, 16)
        weight = self.empty(16)
        _, scale = self.quant_matcher.inputs()

        # input goes through allreduce first, always 16-bit
        return [residual, input.to(self.dtype), weight, scale]

    defregister(self, pm_pass: PatternMatcherPass) -> None:
        defpattern(
            residual: torch.Tensor,
            input: torch.Tensor,
            weight: torch.Tensor,
            scale: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor]:
            allreduce_output = tensor_model_parallel_all_reduce(input)
            rms, res = vllm.ir.ops.fused_add_rms_norm(
                allreduce_output, residual, weight, self.epsilon
            )
            quant, _ = self.quant_matcher(rms, scale)

            return quant, res

        defreplacement(
            residual: torch.Tensor,
            input: torch.Tensor,
            weight: torch.Tensor,
            scale: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor]:
            result_quant = torch.empty_like(input, dtype=self.quant_dtype)
            assert flashinfer_comm is not None, "FlashInfer must be enabled"
            allreduce = auto_functionalized(
                flashinfer_trtllm_fused_allreduce_norm,
                allreduce_in=input,
                residual=residual,
                norm_out=None,
                quant_out=result_quant,
                scale_out=None,
                rms_gamma=weight,
                rms_eps=self.epsilon,
                # We don't use norm_out afterwards
                pattern_code=(
                    flashinfer_comm.AllReduceFusionPattern.kARResidualRMSNormFP8Quant
                ),
                scale_factor=scale,
                **self.allreduce_params.get_trtllm_fused_allreduce_kwargs(),
            )
            # quant_out, rms_norm_residual
            return allreduce[4], allreduce[2]

        pm.register_replacement(
            pattern, replacement, self.get_inputs(), pm.fwd_only, pm_pass
        )
```

## AllReduceFusedAddRMSNormStaticQuantNVFP4Pattern [¶](#vllm.compilation.passes.fusion.allreduce_rms_fusion.AllReduceFusedAddRMSNormStaticQuantNVFP4Pattern "Permanent link")

Bases: `BasePattern`

This pattern replaces the allreduce + rms norm (with residual) + static nvfp4 quant with fused flashinfer implementation. Applies to o\_proj + rmsnorm after attn + quant and mlp + rmsnorm + quant before attn.

Source code in `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`

```
classAllReduceFusedAddRMSNormStaticQuantNVFP4Pattern(BasePattern):
"""
    This pattern replaces the allreduce + rms norm (with residual)
    + static nvfp4 quant with fused flashinfer implementation.
    Applies to o_proj + rmsnorm after attn + quant and
    mlp + rmsnorm + quant before attn.
    """

    def__init__(
        self,
        epsilon: float,
        dtype: torch.dtype,
        device: str | None,
        allreduce_params: FlashInferFusedAllReduceParams,
    ) -> None:
        super().__init__(dtype, device)
        self.epsilon = epsilon
        self.allreduce_params = allreduce_params

    defget_inputs(self) -> list[torch.Tensor]:
        input = torch.empty([16, 16], device=self.device, dtype=self.dtype)

        residual = torch.empty([16, 16], device=self.device, dtype=self.dtype)
        weight = torch.empty([16, 16], device=self.device, dtype=self.dtype)
        quant_result = torch.empty((16, 8), device=self.device, dtype=torch.uint8)
        input_global_scale = torch.empty(
            [1, 1], device=self.device, dtype=torch.float32
        )
        output_scale = torch.empty([128, 4], device=self.device, dtype=torch.int32)

        return [
            quant_result,
            residual,
            input,
            output_scale,
            weight,
            input_global_scale,
        ]

    defregister(self, pm_pass: PatternMatcherPass) -> None:
        defpattern(
            quant_result: torch.Tensor,
            residual: torch.Tensor,
            input: torch.Tensor,
            output_scale: torch.Tensor,
            weight: torch.Tensor,
            input_global_scale: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
            allreduce_output = tensor_model_parallel_all_reduce(input)
            rms, residual = vllm.ir.ops.fused_add_rms_norm(
                allreduce_output, residual, weight, self.epsilon
            )
            quant_out_tuple = auto_functionalized(
                STATIC_FP4_QUANT_OP,
                input=rms,
                input_scale=input_global_scale,
                is_sf_swizzled_layout=True,
                output=quant_result,
                output_scale=output_scale,
            )

            # quant_out, allreduce_output, output_scale
            return quant_out_tuple[1], residual, quant_out_tuple[2]

        defreplacement(
            quant_result: torch.Tensor,
            residual: torch.Tensor,
            input: torch.Tensor,
            output_scale: torch.Tensor,
            weight: torch.Tensor,
            input_global_scale: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
            assert flashinfer_comm is not None, "FlashInfer must be enabled"
            allreduce = auto_functionalized(
                flashinfer_trtllm_fused_allreduce_norm,
                allreduce_in=input,
                residual=residual,
                norm_out=None,
                quant_out=quant_result,
                scale_out=output_scale,
                rms_gamma=weight,
                rms_eps=self.epsilon,
                # We don't use norm_out afterwards
                pattern_code=(
                    flashinfer_comm.AllReduceFusionPattern.kARResidualRMSNormFP4Quant
                ),
                scale_factor=input_global_scale,
                **self.allreduce_params.get_trtllm_fused_allreduce_kwargs(),
            )
            # quant_out, rms_norm_residual, output_scale
            return allreduce[4], allreduce[2], allreduce[5]

        pm.register_replacement(
            pattern, replacement, self.get_inputs(), pm.fwd_only, pm_pass
        )
```

## AllReduceFusedRMSNormStaticQuantFP8Pattern [¶](#vllm.compilation.passes.fusion.allreduce_rms_fusion.AllReduceFusedRMSNormStaticQuantFP8Pattern "Permanent link")

Bases: `BasePattern`

This pattern replaces the allreduce + rms norm (without residual) + static fp8 quant with fused flashinfer implementation. Applies to allreduce + rmsnorm + quant before attn in the first Transformer block.

Source code in `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`

```
classAllReduceFusedRMSNormStaticQuantFP8Pattern(BasePattern):
"""
    This pattern replaces the allreduce + rms norm (without residual)
    + static fp8 quant with fused flashinfer implementation.
    Applies to allreduce + rmsnorm + quant before attn
    in the first Transformer block.
    """

    def__init__(
        self,
        epsilon: float,
        dtype: torch.dtype,
        device: str | None,
        allreduce_params: FlashInferFusedAllReduceParams,
    ) -> None:
        super().__init__(dtype, device)
        self.epsilon = epsilon
        self.allreduce_params = allreduce_params
        self.quant_dtype = torch.float8_e4m3fn
        self.quant_matcher = MatcherQuantFP8(kFp8StaticTensorSym)

    defget_inputs(self) -> list[torch.Tensor]:
        _, scale = self.quant_matcher.inputs()

        # input, weight
        return [self.empty(5, 16), self.empty(16), scale]

    defregister(self, pm_pass: PatternMatcherPass) -> None:
        defpattern(
            input: torch.Tensor,
            weight: torch.Tensor,
            scale: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor]:
            all_reduce = tensor_model_parallel_all_reduce(input)
            rms = vllm.ir.ops.rms_norm(all_reduce, weight, self.epsilon)
            quant, _ = self.quant_matcher(rms, scale)
            return quant, all_reduce

        defreplacement(
            input: torch.Tensor, weight: torch.Tensor, scale: torch.Tensor
        ) -> tuple[torch.Tensor, torch.Tensor]:
            residual = torch.zeros_like(input)
            result_rms = torch.empty_like(input)
            result_quant = torch.empty_like(input, dtype=self.quant_dtype)
            assert flashinfer_comm is not None, "FlashInfer must be enabled"
            allreduce = auto_functionalized(
                flashinfer_trtllm_fused_allreduce_norm,
                allreduce_in=input,
                residual=residual,
                norm_out=result_rms,
                quant_out=result_quant,
                scale_out=None,
                rms_gamma=weight,
                rms_eps=self.epsilon,
                # We don't use norm_out afterwards
                pattern_code=(
                    flashinfer_comm.AllReduceFusionPattern.kARResidualRMSNormFP8Quant
                ),
                scale_factor=scale,
                **self.allreduce_params.get_trtllm_fused_allreduce_kwargs(),
            )

            # quant_out, allreduce_output
            return allreduce[4], allreduce[1]

        pm.register_replacement(
            pattern,
            replacement,
            self.get_inputs(),
            pm.fwd_only,
            pm_pass,
            extra_check=_rms_input_weight_dtype_match,
        )
```

## AllReduceFusedRMSNormStaticQuantNVFP4Pattern [¶](#vllm.compilation.passes.fusion.allreduce_rms_fusion.AllReduceFusedRMSNormStaticQuantNVFP4Pattern "Permanent link")

Bases: `BasePattern`

This pattern replaces the allreduce + rms norm (without residual) + static nvfp4 quant with fused flashinfer implementation. Applies to allreduce + rmsnorm + quant before attn in the first Transformer block.

Source code in `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`

```
classAllReduceFusedRMSNormStaticQuantNVFP4Pattern(BasePattern):
"""
    This pattern replaces the allreduce + rms norm (without residual)
    + static nvfp4 quant with fused flashinfer implementation.
    Applies to allreduce + rmsnorm + quant before attn
    in the first Transformer block.
    """

    def__init__(
        self,
        epsilon: float,
        dtype: torch.dtype,
        device: str | None,
        allreduce_params: FlashInferFusedAllReduceParams,
    ) -> None:
        super().__init__(dtype, device)
        self.epsilon = epsilon
        self.allreduce_params = allreduce_params

    defget_inputs(self) -> list[torch.Tensor]:
        input = torch.empty([1, 16, 16], device=self.device, dtype=self.dtype)
        quant_result = torch.empty((16, 8), device=self.device, dtype=torch.uint8)
        input_global_scale = torch.empty(
            [1, 1], device=self.device, dtype=torch.float32
        )
        weight = torch.empty([16], device=self.device, dtype=self.dtype)
        output_scale = torch.empty([128, 4], device=self.device, dtype=torch.int32)

        return [input, quant_result, weight, input_global_scale, output_scale]

    defregister(self, pm_pass: PatternMatcherPass) -> None:
        defpattern(
            input: torch.Tensor,
            quant_result: torch.Tensor,
            weight: torch.Tensor,
            input_global_scale: torch.Tensor,
            output_scale: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
            all_reduce = tensor_model_parallel_all_reduce(input)
            rms = vllm.ir.ops.rms_norm(all_reduce, weight, self.epsilon)
            quant_out_tuple = auto_functionalized(
                STATIC_FP4_QUANT_OP,
                input=rms,
                input_scale=input_global_scale,
                is_sf_swizzled_layout=True,
                output=quant_result,
                output_scale=output_scale,
            )

            # quant_out, allreduce_output, output_scale
            return quant_out_tuple[1], all_reduce, quant_out_tuple[2]

        defreplacement(
            input: torch.Tensor,
            quant_result: torch.Tensor,
            weight: torch.Tensor,
            input_global_scale: torch.Tensor,
            output_scale: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
            residual = torch.zeros_like(input)
            result_rms = torch.empty_like(input)
            assert flashinfer_comm is not None, "FlashInfer must be enabled"
            allreduce = auto_functionalized(
                flashinfer_trtllm_fused_allreduce_norm,
                allreduce_in=input,
                residual=residual,
                norm_out=result_rms,
                quant_out=quant_result,
                scale_out=output_scale,
                rms_gamma=weight,
                rms_eps=self.epsilon,
                # We don't use norm_out afterwards
                pattern_code=(
                    flashinfer_comm.AllReduceFusionPattern.kARResidualRMSNormFP4Quant
                ),
                scale_factor=input_global_scale,
                **self.allreduce_params.get_trtllm_fused_allreduce_kwargs(),
            )

            # quant_out, allreduce_output, output_scale
            return allreduce[4], allreduce[1], allreduce[5]

        pm.register_replacement(
            pattern,
            replacement,
            self.get_inputs(),
            pm.fwd_only,
            pm_pass,
            extra_check=_rms_input_weight_dtype_match,
        )
```

## AllReduceRMSNormPattern [¶](#vllm.compilation.passes.fusion.allreduce_rms_fusion.AllReduceRMSNormPattern "Permanent link")

Bases: `BasePattern`

This pattern replaces the allreduce + rms norm (without residual) with fused flashinfer implementation. Applies to allreduce + rmsnorm before attn in the first Transformer block.

Source code in `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`

```
classAllReduceRMSNormPattern(BasePattern):
"""
    This pattern replaces the allreduce + rms norm (without residual)
    with fused flashinfer implementation.
    Applies to allreduce + rmsnorm before attn in the first Transformer block.
    """

    def__init__(
        self,
        epsilon: float,
        dtype: torch.dtype,
        device: str | None,
        allreduce_params: FlashInferFusedAllReduceParams,
    ) -> None:
        super().__init__(dtype, device)
        self.epsilon = epsilon
        self.allreduce_params = allreduce_params

    defget_inputs(self) -> list[torch.Tensor]:
        # input, weight
        return [self.empty(5, 16), self.empty(16)]

    defregister(self, pm_pass: PatternMatcherPass) -> None:
        defpattern(
            input: torch.Tensor, weight: torch.Tensor
        ) -> tuple[torch.Tensor, torch.Tensor]:
            allreduce_output = tensor_model_parallel_all_reduce(input)
            rms = vllm.ir.ops.rms_norm(allreduce_output, weight, self.epsilon)

            return rms, allreduce_output

        defreplacement(
            input: torch.Tensor, weight: torch.Tensor
        ) -> tuple[torch.Tensor, torch.Tensor]:
            residual = torch.zeros_like(input)
            rms_result = torch.empty_like(input)
            assert flashinfer_comm is not None, "FlashInfer must be enabled"
            allreduce = auto_functionalized(
                flashinfer_trtllm_fused_allreduce_norm,
                allreduce_in=input,
                residual=residual,
                norm_out=rms_result,
                quant_out=None,
                scale_out=None,
                rms_gamma=weight,
                rms_eps=self.epsilon,
                pattern_code=flashinfer_comm.AllReduceFusionPattern.kARResidualRMSNorm,
                **self.allreduce_params.get_trtllm_fused_allreduce_kwargs(),
            )
            # rms_result, allreduce_in
            return allreduce[3], allreduce[1]

        pm.register_replacement(
            pattern,
            replacement,
            self.get_inputs(),
            pm.fwd_only,
            pm_pass,
            extra_check=_rms_input_weight_dtype_match,
        )
```

## FlashInferFusedAllReduceParams [¶](#vllm.compilation.passes.fusion.allreduce_rms_fusion.FlashInferFusedAllReduceParams "Permanent link")

Parameters for FlashInfer fused allreduce operations.

Source code in `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`

```
classFlashInferFusedAllReduceParams:
"""Parameters for FlashInfer fused allreduce operations."""

    def__init__(
        self,
        world_size: int,
        max_token_num: int = 1024,
    ) -> None:
        self.world_size = world_size
        self.launch_with_pdl = True
        self.fp32_acc = True
        self.max_token_num = max_token_num

    defget_trtllm_fused_allreduce_kwargs(self) -> dict[str, bool | int]:
        return {
            "world_size": self.world_size,
            "launch_with_pdl": self.launch_with_pdl,
            "fp32_acc": self.fp32_acc,
            "max_token_num": self.max_token_num,
        }
```