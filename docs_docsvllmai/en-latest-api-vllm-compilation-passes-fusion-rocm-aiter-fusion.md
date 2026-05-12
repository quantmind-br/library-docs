---
title: rocm_aiter_fusion - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/fusion/rocm_aiter_fusion/
source: sitemap
fetched_at: 2026-05-07T21:16:31.217331261-03:00
rendered_js: false
word_count: 329
summary: This document defines compilation patterns for the vLLM framework that fuse RMSNorm and residual addition operations with padding or quantization kernels specifically optimized for ROCm AITER.
tags:
    - vllm
    - rocm
    - aiter
    - operator-fusion
    - quantization
    - graph-compilation
category: api
---

## AddAiterRMSNormPadPattern [¶](#vllm.compilation.passes.fusion.rocm_aiter_fusion.AddAiterRMSNormPadPattern "Permanent link")

This pattern replaces an aiter\_rmsnorm\_with\_add & a pad op with a custom triton\_add\_rmsnorm\_pad op from AITER.

Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`

```
classAddAiterRMSNormPadPattern:
"""
    This pattern replaces an aiter_rmsnorm_with_add & a pad op
    with a custom triton_add_rmsnorm_pad op from AITER.
    """

    AITER_TRITON_ADD_RMSNORM_PAD_OP = rocm_aiter_ops.get_triton_add_rmsnorm_pad_op()

    def__init__(
        self,
        epsilon: float,
        hidden_size: int,
        x_pad_to_multiple: int,
    ):
        self.epsilon = epsilon
        self.hidden_size = hidden_size
        self.x_pad_to_multiple = x_pad_to_multiple

    defget_inputs(self) -> list[torch.Tensor]:
        device = torch.device("cuda")
        dtype = torch.bfloat16
        input = torch.empty(5, 16, dtype=dtype, device=device)
        weight = torch.empty(16, dtype=dtype, device=device)
        residual = torch.empty(5, 16, dtype=dtype, device=device)
        router_weight = torch.empty([8, 16], dtype=dtype, device=device)
        router_bias = torch.empty([8], dtype=dtype, device=device)
        return [input, weight, residual, router_weight, router_bias]

    defregister(self, pm_pass: PatternMatcherPass) -> None:
        defpattern(
            input: torch.Tensor,
            weight: torch.Tensor,
            residual: torch.Tensor,
            router_weight: torch.Tensor,
            router_bias: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
            pad_size = self.x_pad_to_multiple - (
                self.hidden_size % self.x_pad_to_multiple
            )
            result_rms, residual_out = torch.ops.vllm_ir.fused_add_rms_norm(
                input, residual, weight, self.epsilon
            )
            router_logits = torch.ops.vllm.rocm_unquantized_gemm(
                result_rms, router_weight, router_bias
            )
            result = torch.nn.functional.pad(
                result_rms, (0, pad_size), mode="constant", value=0.0
            )
            return result, residual_out, router_logits

        defreplacement(
            input: torch.Tensor,
            weight: torch.Tensor,
            residual: torch.Tensor,
            router_weight: torch.Tensor,
            router_bias: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
            at = self.AITER_TRITON_ADD_RMSNORM_PAD_OP(
                x=input,
                weight=weight,
                variance_epsilon=self.epsilon,
                residual=residual,
                x_pad_to_multiple=self.x_pad_to_multiple,
            )
            result_padded = at[0]
            router_logits = torch.ops.vllm.rocm_unquantized_gemm(
                result_padded[:, : self.hidden_size], router_weight, router_bias
            )
            residual_out = at[1]
            return result_padded, residual_out, router_logits

        pm.register_replacement(
            pattern, replacement, self.get_inputs(), pm.fwd_only, pm_pass
        )
```

## AiterFusedAddRMSFp8GroupQuantPattern [¶](#vllm.compilation.passes.fusion.rocm_aiter_fusion.AiterFusedAddRMSFp8GroupQuantPattern "Permanent link")

Bases: `AiterRMSNormQuantPattern`

This pattern fuses aiter rms\_norm\_with\_add & group fp8 quant custom ops into a aiter rms\_norm\_with\_add\_group\_fp8\_quant op.

Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`

```
classAiterFusedAddRMSFp8GroupQuantPattern(AiterRMSNormQuantPattern):
"""
    This pattern fuses aiter rms_norm_with_add & group fp8 quant custom ops
    into a aiter rms_norm_with_add_group_fp8_quant op.
    """

    FUSED_OP = rocm_aiter_ops.get_rmsnorm_group_add_fused_quant_op()

    def__init__(
        self,
        epsilon: float,
        quant_dtype: torch.dtype,
        group_shape: GroupShape,
        match_aiter_quant: bool = True,
        symmetric: bool = True,
    ) -> None:
        scale = ScaleDesc(torch.float32, False, group_shape)
        key = FusedRMSQuantKey(
            fused_add=True,
            quant=QuantKey(dtype=quant_dtype, scale=scale, symmetric=symmetric),
        )

        super().__init__(epsilon, key, match_aiter_quant)

    defregister(self, pm_pass: PatternMatcherPass) -> None:
        defpattern(
            input: torch.Tensor,
            weight: torch.Tensor,
            residual: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
            result_rms, residual_out = torch.ops.vllm_ir.fused_add_rms_norm(
                input, residual, weight, self.epsilon
            )
            result, scale = self.quant_matcher(result_rms)

            return result, residual_out, scale

        defreplacement(
            input: torch.Tensor,
            weight: torch.Tensor,
            residual: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
            at = self.FUSED_OP(
                x=input,
                residual=residual,
                weight=weight,
                variance_epsilon=self.epsilon,
                group_size=128,
            )

            # result, scale, residual
            return at[0], at[1], at[2]

        inputs = [
            self.empty(5, 16),  # input
            self.empty(16),  # weight
            self.empty(5, 16),  # residual
        ]

        pm.register_replacement(pattern, replacement, inputs, pm.fwd_only, pm_pass)
```

## AiterFusedAddRMSNormDynamicQuantPattern [¶](#vllm.compilation.passes.fusion.rocm_aiter_fusion.AiterFusedAddRMSNormDynamicQuantPattern "Permanent link")

Bases: `AiterRMSNormQuantPattern`

AITER RMSNorm Fused Add + Dynamic Quantization pattern.

Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`

```
classAiterFusedAddRMSNormDynamicQuantPattern(AiterRMSNormQuantPattern):
"""AITER RMSNorm Fused Add + Dynamic Quantization pattern."""

    FUSED_OP = rocm_aiter_ops.get_rmsnorm_fused_add_dynamic_quant_op()

    def__init__(
        self,
        epsilon: float,
        quant_dtype: torch.dtype,
        match_aiter_quant: bool = True,
        group_shape: GroupShape = GroupShape.PER_TOKEN,
        symmetric: bool = True,
    ) -> None:
        scale = ScaleDesc(torch.float32, False, group_shape)
        key = FusedRMSQuantKey(
            fused_add=True,
            quant=QuantKey(dtype=quant_dtype, scale=scale, symmetric=symmetric),
        )

        super().__init__(epsilon, key, match_aiter_quant)

    defregister(self, pm_pass: PatternMatcherPass) -> None:
        defpattern(
            input: torch.Tensor,
            weight: torch.Tensor,
            residual: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
            result_rms, residual_out = torch.ops.vllm_ir.fused_add_rms_norm(
                input, residual, weight, self.epsilon
            )
            result, scale = self.quant_matcher(result_rms)

            return result, residual_out, scale

        defreplacement(
            input: torch.Tensor, weight: torch.Tensor, residual: torch.Tensor
        ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
            result = self.FUSED_OP(
                x=input,
                residual=residual,
                weight=weight,
                epsilon=self.epsilon,
                quant_dtype=self.quant_dtype,
            )

            return result[0], result[1], result[2]

        inputs = [
            self.empty(5, 16),  # input
            self.empty(16),  # weight
            self.empty(5, 16),  # residual
        ]

        pm.register_replacement(
            pattern,
            replacement,
            inputs,
            pm.fwd_only,
            pm_pass,
        )
```

## AiterRMSFp8GroupQuantPattern [¶](#vllm.compilation.passes.fusion.rocm_aiter_fusion.AiterRMSFp8GroupQuantPattern "Permanent link")

Bases: `AiterRMSNormQuantPattern`

This pattern fuses aiter rms\_norm & group fp8 quant custom ops into an aiter rms\_norm\_group\_fp8\_quant op.

Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`

```
classAiterRMSFp8GroupQuantPattern(AiterRMSNormQuantPattern):
"""
    This pattern fuses aiter rms_norm & group fp8 quant custom
    ops into an aiter rms_norm_group_fp8_quant op.
    """

    FUSED_OP = rocm_aiter_ops.get_rmsnorm_group_fused_quant_op()

    def__init__(
        self,
        epsilon: float,
        quant_dtype: torch.dtype,
        group_shape: GroupShape,
        match_aiter_quant: bool = True,
        symmetric: bool = True,
    ) -> None:
        scale = ScaleDesc(torch.float32, False, group_shape)
        key = FusedRMSQuantKey(
            fused_add=False,
            quant=QuantKey(dtype=quant_dtype, scale=scale, symmetric=symmetric),
        )

        super().__init__(epsilon, key, match_aiter_quant)

    defregister(self, pm_pass: PatternMatcherPass) -> None:
        defpattern(
            input: torch.Tensor,
            weight: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor]:
            result_rms = torch.ops.vllm_ir.rms_norm(input, weight, self.epsilon)
            result, scale = self.quant_matcher(result_rms)
            return result, scale

        defreplacement(
            input: torch.Tensor,
            weight: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor]:
            at = self.FUSED_OP(
                x=input,
                weight=weight,
                variance_epsilon=self.epsilon,
                group_size=128,
            )

            return at[0], at[1]

        pm.register_replacement(
            pattern,
            replacement,
            # input, weight
            [self.empty(5, 16), self.empty(16)],
            pm.fwd_only,
            pm_pass,
        )
```

## AiterRMSNormDynamicQuantPattern [¶](#vllm.compilation.passes.fusion.rocm_aiter_fusion.AiterRMSNormDynamicQuantPattern "Permanent link")

Bases: `AiterRMSNormQuantPattern`

AITER RMSNorm + Dynamic Quantization pattern.

Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`

```
classAiterRMSNormDynamicQuantPattern(AiterRMSNormQuantPattern):
"""AITER RMSNorm + Dynamic Quantization pattern."""

    FUSED_OP = rocm_aiter_ops.get_rmsnorm_fused_dynamic_quant_op()

    def__init__(
        self,
        epsilon: float,
        quant_dtype: torch.dtype,
        match_aiter_quant: bool = True,
        group_shape: GroupShape = GroupShape.PER_TOKEN,
        symmetric: bool = True,
    ) -> None:
        scale = ScaleDesc(torch.float32, False, group_shape)
        key = FusedRMSQuantKey(
            fused_add=False,
            quant=QuantKey(dtype=quant_dtype, scale=scale, symmetric=symmetric),
        )

        super().__init__(epsilon, key, match_aiter_quant)

    defregister(self, pm_pass: PatternMatcherPass) -> None:
        defpattern(
            input: torch.Tensor,
            weight: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor]:
            result_rms = torch.ops.vllm_ir.rms_norm(input, weight, self.epsilon)
            result, scale = self.quant_matcher(result_rms)
            return result, scale

        defreplacement(
            input: torch.Tensor,
            weight: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor]:
            result = self.FUSED_OP(
                x=input,
                weight=weight,
                epsilon=self.epsilon,
                quant_dtype=self.quant_dtype,
            )

            return result[0], result[1]

        pm.register_replacement(
            pattern,
            replacement,
            # input, weight
            [self.empty(5, 16), self.empty(16)],
            pm.fwd_only,
            pm_pass,
        )
```

## AiterSiluMulFp8GroupQuantPattern [¶](#vllm.compilation.passes.fusion.rocm_aiter_fusion.AiterSiluMulFp8GroupQuantPattern "Permanent link")

Bases: `VllmPatternReplacement`

This pattern fuses aiter silu\_and\_mul & group fp8 quant custom ops into an aiter silu\_and\_mul\_group\_fp8\_quant op.

Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`

```
classAiterSiluMulFp8GroupQuantPattern(VllmPatternReplacement):
"""
    This pattern fuses aiter silu_and_mul & group fp8 quant custom
    ops into an aiter silu_and_mul_group_fp8_quant op.
    """

    FUSED_SILU_MUL_QUANT_OP = rocm_aiter_ops.get_act_mul_fused_fp8_group_quant_op()

    def__init__(self) -> None:
        self.silu_and_mul_matcher = MatcherSiluAndMul()
        self.quant_matcher = MatcherQuantFP8(
            quant_key=kFp8Dynamic128Sym, match_rocm_aiter=True
        )

    defget_inputs(self) -> list[torch.Tensor]:
        return [
            self.silu_and_mul_matcher.inputs()[0],
        ]

    @property
    defpattern(self):
        def_pattern(
            input: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor]:
            at1 = self.silu_and_mul_matcher(input)
            at2 = self.quant_matcher(at1)
            return at2[0], at2[1]

        return _pattern

    @property
    defreplacement(self):
        def_replacement(
            input: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor]:
            at = self.FUSED_SILU_MUL_QUANT_OP(x=input, group_size=128)
            return at[0], at[1]

        return _replacement
```

## MLADualRMSNormFusionPass [¶](#vllm.compilation.passes.fusion.rocm_aiter_fusion.MLADualRMSNormFusionPass "Permanent link")

Bases: `VllmFusionPatternMatcherPass`

Post-grad PatternMatcher pass that fuses paired q / kv RMS norms in MLA attention into `fused_mla_dual_rms_norm` backed by aiter's `fused_qk_rmsnorm` HIP kernel.

Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`

```
classMLADualRMSNormFusionPass(VllmFusionPatternMatcherPass):
"""
    Post-grad PatternMatcher pass that fuses paired q / kv RMS norms in
    MLA attention into ``fused_mla_dual_rms_norm`` backed by aiter's
    ``fused_qk_rmsnorm`` HIP kernel.
    """

    def__init__(self, config: VllmConfig) -> None:
        super().__init__(config, "mla_dual_rms_norm_fusion_pass")

        for epsilon in [1e-5, 1e-6]:
            self.register(MLADualRMSNormPattern(epsilon))
```

## MLADualRMSNormPattern [¶](#vllm.compilation.passes.fusion.rocm_aiter_fusion.MLADualRMSNormPattern "Permanent link")

Bases: `VllmPatternReplacement[..., tuple[Tensor, Tensor, Tensor]]`

Fuse paired q\_a\_layernorm + kv\_a\_layernorm in MLA attention into AITER's `fused_qk_rmsnorm` HIP kernel.

Target FX-graph pattern (unfused, `vllm_ir` stage)::

```
gemm -> split_with_sizes([q_dim, kv_dim])
    +-- q_c     -> vllm_ir.rms_norm(q_c, q_w, eps)
    +-- kv_lora -> split_with_sizes([kv_c_dim, k_pe_dim])
                    +-- kv_c -> vllm_ir.rms_norm(kv_c, kv_w, eps)
                    +-- k_pe
```

The pattern covers the connected subgraph rooted at the first `split_with_sizes` (which produces `q_c` and `kv_lora`), through the two `rms_norm` calls, and the `k_pe` passthrough.

Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`

```
classMLADualRMSNormPattern(
    VllmPatternReplacement[..., tuple[torch.Tensor, torch.Tensor, torch.Tensor]]
):
"""
    Fuse paired q_a_layernorm + kv_a_layernorm in MLA attention into
    AITER's ``fused_qk_rmsnorm`` HIP kernel.

    Target FX-graph pattern (unfused, ``vllm_ir`` stage)::

        gemm -> split_with_sizes([q_dim, kv_dim])
            +-- q_c     -> vllm_ir.rms_norm(q_c, q_w, eps)
            +-- kv_lora -> split_with_sizes([kv_c_dim, k_pe_dim])
                            +-- kv_c -> vllm_ir.rms_norm(kv_c, kv_w, eps)
                            +-- k_pe

    The pattern covers the connected subgraph rooted at the first
    ``split_with_sizes`` (which produces ``q_c`` and ``kv_lora``),
    through the two ``rms_norm`` calls, and the ``k_pe`` passthrough.
    """

    def__init__(self, epsilon: float) -> None:
        self._epsilon = epsilon

    defget_inputs(self) -> list[torch.Tensor]:
        q_dim, kv_c_dim, k_pe_dim = 8, 4, 2
        return [
            self.empty_bf16(5, q_dim + kv_c_dim + k_pe_dim),
            self.empty_bf16(q_dim),
            self.empty_bf16(kv_c_dim),
        ]

    @property
    defpattern(
        self,
    ) -> Callable[..., tuple[torch.Tensor, torch.Tensor, torch.Tensor]]:
        eps = self._epsilon

        def_pattern(
            projected: torch.Tensor,
            q_weight: torch.Tensor,
            kv_weight: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
            q_dim = q_weight.shape[0]
            kv_dim = projected.shape[-1] - q_dim
            kv_c_dim = kv_weight.shape[0]
            k_pe_dim = kv_dim - kv_c_dim
            q_c, kv_lora = projected.split([q_dim, kv_dim], dim=-1)
            kv_c, k_pe = kv_lora.split([kv_c_dim, k_pe_dim], dim=-1)
            q_normed = vllm.ir.ops.rms_norm(q_c, q_weight, eps)
            kv_normed = vllm.ir.ops.rms_norm(kv_c, kv_weight, eps)
            return q_normed, kv_normed, k_pe

        return _pattern

    @property
    defreplacement(
        self,
    ) -> Callable[..., tuple[torch.Tensor, torch.Tensor, torch.Tensor]]:
        eps = self._epsilon

        def_replacement(
            projected: torch.Tensor,
            q_weight: torch.Tensor,
            kv_weight: torch.Tensor,
        ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
            q_dim = q_weight.shape[0]
            kv_dim = projected.shape[-1] - q_dim
            kv_c_dim = kv_weight.shape[0]
            k_pe_dim = kv_dim - kv_c_dim
            q_c, kv_lora = projected.split([q_dim, kv_dim], dim=-1)
            kv_c, k_pe = kv_lora.split([kv_c_dim, k_pe_dim], dim=-1)
            q_normed, kv_normed = torch.ops.vllm.fused_mla_dual_rms_norm(
                q_c,
                q_weight,
                kv_c,
                kv_weight,
                eps,
                eps,
            )
            return q_normed, kv_normed, k_pe

        return _replacement
```

## RocmAiterRMSNormQuantFusionPass [¶](#vllm.compilation.passes.fusion.rocm_aiter_fusion.RocmAiterRMSNormQuantFusionPass "Permanent link")

Bases: `VllmPatternMatcherPass`

This pass fuses aiter rms\_norm & vllm/aiter quant custom ops into a fused rms\_norm\_quant op. It also supports fused\_add\_rms\_norm.

Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`

```
classRocmAiterRMSNormQuantFusionPass(VllmPatternMatcherPass):
"""
    This pass fuses aiter rms_norm & vllm/aiter quant custom ops
    into a fused rms_norm_quant op.
    It also supports fused_add_rms_norm.
    """

    @enable_fake_mode
    def__init__(self, config: VllmConfig) -> None:
        super().__init__(config)

        self.patterns: PatternMatcherPass = PatternMatcherPass(
            pass_name="rocm_aiter_rms_norm_quant_fusion_pass"
        )

        # Make sure fused add patterns are before simple rms norm,
        # as the latter is a subset of the former in torch ops
        for epsilon in [1e-5, 1e-6]:
            #  Fuse aiter rms_norm + aiter dynamic group fp8 quant
            AiterRMSFp8GroupQuantPattern(
                epsilon, FP8_DTYPE, GroupShape(1, 128)
            ).register(self.patterns)

            # Fuse aiter fused_add_rms_norm + aiter dynamic group fp8 quant
            AiterFusedAddRMSFp8GroupQuantPattern(
                epsilon, FP8_DTYPE, GroupShape(1, 128)
            ).register(self.patterns)

            # When quant_fp8 custom ops are disabled, both AITER and native
            # quant matchers trace through QuantFP8's native implementation.
            # Registering both variants would create duplicate Inductor
            # patterns.
            is_quant_fp8_enabled = config.compilation_config.is_custom_op_enabled(
                "quant_fp8"
            )
            match_aiter_quant_options = (
                [True, False] if is_quant_fp8_enabled else [False]
            )

            for match_aiter_quant in match_aiter_quant_options:
                # Fuse aiter rms_norm + (aiter / vllm built-in)
                # dynamic per-token fp8 quant
                AiterRMSNormDynamicQuantPattern(
                    epsilon, FP8_DTYPE, match_aiter_quant=match_aiter_quant
                ).register(self.patterns)

                # Fuse aiter fused_add_rms_norm + (aiter / vllm built-in)
                # dynamic per-token fp8 quant
                AiterFusedAddRMSNormDynamicQuantPattern(
                    epsilon, FP8_DTYPE, match_aiter_quant=match_aiter_quant
                ).register(self.patterns)

        self.dump_patterns(config, self.patterns)

    @VllmInductorPass.time_and_log
    def__call__(self, graph: fx.Graph) -> None:
        self.matched_count = self.patterns.apply(graph)
        logger.debug(
            "%s Replaced %s patterns", self.__class__.__name__, self.matched_count
        )

    defuuid(self) -> str:
        fusion_patterns = [
            AiterRMSNormDynamicQuantPattern,
            AiterFusedAddRMSNormDynamicQuantPattern,
            AiterRMSFp8GroupQuantPattern,
            AiterFusedAddRMSFp8GroupQuantPattern,
        ]
        return self.hash_source(self, *fusion_patterns)
```

## RocmAiterSiluMulFp8GroupQuantFusionPass [¶](#vllm.compilation.passes.fusion.rocm_aiter_fusion.RocmAiterSiluMulFp8GroupQuantFusionPass "Permanent link")

Bases: `VllmFusionPatternMatcherPass`

This pass fuses a pre-defined set of custom ops into fused ops. It uses the torch pattern matcher to find the patterns and replace them.

Because patterns can only be registered once, the pass is a singleton. This will be addressed in a future version of PyTorch: https://github.com/pytorch/pytorch/pull/139321#issuecomment-2452354980

Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`

```
classRocmAiterSiluMulFp8GroupQuantFusionPass(VllmFusionPatternMatcherPass):
"""
    This pass fuses a pre-defined set of custom ops into fused ops.
    It uses the torch pattern matcher to find the patterns and replace them.

    Because patterns can only be registered once, the pass is a singleton.
    This will be addressed in a future version of PyTorch:
    https://github.com/pytorch/pytorch/pull/139321#issuecomment-2452354980
    """

    def__init__(self, config: VllmConfig) -> None:
        super().__init__(config, "rocm_aiter_silu_mul_fp8_group_quant_fusion_pass")

        self.register(AiterSiluMulFp8GroupQuantPattern())

        self.dump_patterns(config, self.pm_pass)
```

## RocmAiterTritonAddRMSNormPadFusionPass [¶](#vllm.compilation.passes.fusion.rocm_aiter_fusion.RocmAiterTritonAddRMSNormPadFusionPass "Permanent link")

Bases: `VllmPatternMatcherPass`

This pass replaces an AITER CK RMSNorm + residual add and a pad op with an triton\_add\_rmsnorm\_pad op from AITER.

Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`

```
classRocmAiterTritonAddRMSNormPadFusionPass(VllmPatternMatcherPass):
"""
    This pass replaces an AITER CK RMSNorm + residual add and a pad op
    with an triton_add_rmsnorm_pad op from AITER.
    """

    def__init__(self, config: VllmConfig):
        super().__init__(config)
        self.patterns: PatternMatcherPass = PatternMatcherPass(
            pass_name="rocm_aiter_triton_add_rmsnorm_pad_fusion_pass"
        )

        # gpt-oss has hidden size 2880
        # padded to a multiple of 128 on gfx942 and 256 on gfx950 respectively
        hidden_size = 2880
        for epsilon in [1e-5, 1e-6]:
            for x_pad_to_multiple in [128, 256]:
                AddAiterRMSNormPadPattern(
                    epsilon, hidden_size, x_pad_to_multiple
                ).register(self.patterns)

        self.dump_patterns(config, self.patterns)

    @VllmInductorPass.time_and_log
    def__call__(self, graph: torch.fx.Graph) -> None:
        self.matched_count = self.patterns.apply(graph)
        logger.debug("Replaced %s patterns", self.matched_count)

    defuuid(self) -> str:
        return VllmInductorPass.hash_source(self, AddAiterRMSNormPadPattern)
```