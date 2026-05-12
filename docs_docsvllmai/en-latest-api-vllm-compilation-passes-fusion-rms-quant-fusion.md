---
title: rms_quant_fusion - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/fusion/rms_quant_fusion/
source: sitemap
fetched_at: 2026-05-07T21:16:30.257992837-03:00
rendered_js: false
word_count: 0
summary: This document defines a compiler optimization pass that fuses RMS normalization and quantization operations into single, efficient kernels to improve performance in VLLM. It registers various fusion patterns for different quantization types and hardware-specific configurations.
tags:
    - compiler-optimization
    - model-fusion
    - quantization
    - rms-norm
    - vllm
    - graph-transformation
category: concept
---

```
classRMSNormQuantFusionPass(VllmPatternMatcherPass):
"""
    This pass fuses rms_norm & quant custom ops into a fused rms_norm_quant op.
    It also supports fused_add_rms_norm.
    """

    @enable_fake_mode
    def__init__(self, config: VllmConfig) -> None:
        super().__init__(config)

        self.patterns: PatternMatcherPass = PatternMatcherPass(
            pass_name="rmsnorm_quant_fusion_pass"
        )

        # Make sure fused add patterns are before simple rms norm,
        # as the latter is a subset of the former in torch ops
        for epsilon in [1e-5, 1e-6]:
            # Fuse fused_add_rms_norm + static fp8 quant
            FusedAddRMSNormStaticQuantPattern(epsilon, FP8_DTYPE).register(
                self.patterns
            )

            # Fuse rms_norm + static fp8 quant
            RMSNormStaticQuantPattern(epsilon, FP8_DTYPE).register(self.patterns)

            # Fuse fused_add_rms_norm + dynamic per-token fp8 quant
            FusedAddRMSNormDynamicQuantPattern(epsilon, FP8_DTYPE).register(
                self.patterns
            )

            # Fuse rms_norm + dynamic per-token fp8 quant
            RMSNormDynamicQuantPattern(epsilon, FP8_DTYPE).register(self.patterns)

            # Only register group quant patterns on CUDA where the C++ op exists
            if current_platform.is_cuda():
                for group_shape in [GroupShape(1, 128), GroupShape(1, 64)]:
                    for has_col_major_scales in [True, False]:
                        for is_e8m0 in [True, False]:
                            for is_tma_aligned in [False, True]:
                                # Fuse fused_add_rms_norm + fp8 group quant
                                FusedAddRMSNormGroupQuantPattern(
                                    epsilon,
                                    FP8_DTYPE,
                                    group_shape=group_shape,
                                    is_e8m0=is_e8m0,
                                    has_col_major_scales=has_col_major_scales,
                                    is_tma_aligned=is_tma_aligned,
                                ).register(self.patterns)

                                # Fuse rms_norm + fp8 group quant
                                RMSNormGroupQuantPattern(
                                    epsilon,
                                    FP8_DTYPE,
                                    group_shape=group_shape,
                                    is_e8m0=is_e8m0,
                                    has_col_major_scales=has_col_major_scales,
                                    is_tma_aligned=is_tma_aligned,
                                ).register(self.patterns)

        self.dump_patterns(config, self.patterns)

    @VllmInductorPass.time_and_log
    def__call__(self, graph: fx.Graph) -> None:
        self.matched_count = self.patterns.apply(graph)
        logger.debug("Replaced %s patterns", self.matched_count)

    defuuid(self) -> str:
        return self.hash_source(
            self,
            RMSNormGroupQuantPattern,
            RMSNormQuantPattern,
            RMSNormStaticQuantPattern,
            RMSNormDynamicQuantPattern,
            FusedAddRMSNormStaticQuantPattern,
            FusedAddRMSNormDynamicQuantPattern,
            FusedAddRMSNormGroupQuantPattern,
        )
```