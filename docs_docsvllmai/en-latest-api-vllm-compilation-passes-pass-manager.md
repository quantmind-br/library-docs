---
title: pass_manager - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/pass_manager/
source: sitemap
fetched_at: 2026-05-07T21:16:41.041165859-03:00
rendered_js: false
word_count: 142
summary: The PostGradPassManager coordinates the execution and configuration of compilation passes for vLLM, ensuring proper graph optimization and functionalization within the Inductor framework.
tags:
    - vllm
    - compiler-optimization
    - graph-compilation
    - torch-inductor
    - post-grad-passes
    - model-optimization
category: reference
---

## vllm.compilation.passes.pass\_manager [¶](#vllm.compilation.passes.pass_manager "Permanent link")

## PostGradPassManager [¶](#vllm.compilation.passes.pass_manager.PostGradPassManager "Permanent link")

Bases: `CustomGraphPass`

The pass manager for post-grad passes. It handles configuration, adding custom passes, and running passes. It supports uuid for the Inductor code cache. That includes torch&lt;2.6 support using pickling (in .inductor\_pass.CustomGraphPass).

The order of the post-grad post-passes is: 1. passes (constructor parameter) 2. default passes (NoopEliminationPass, FusionPass) 3. config\["post\_grad\_custom\_post\_pass"] (if it exists) 4. fix\_functionalization This way, all passes operate on a functionalized graph.

Source code in `vllm/compilation/passes/pass_manager.py`

```
classPostGradPassManager(CustomGraphPass):  # type: ignore[misc]
"""
    The pass manager for post-grad passes.
    It handles configuration, adding custom passes, and running passes.
    It supports uuid for the Inductor code cache. That includes torch<2.6
    support using pickling (in .inductor_pass.CustomGraphPass).

    The order of the post-grad post-passes is:
    1. passes (constructor parameter)
    2. default passes (NoopEliminationPass, FusionPass)
    3. config["post_grad_custom_post_pass"] (if it exists)
    4. fix_functionalization
    This way, all passes operate on a functionalized graph.
    """

    def__init__(self) -> None:
        self.passes: list[InductorPass] = []

    @with_pattern_match_debug
    def__call__(self, graph: fx.Graph) -> None:
        VllmInductorPass.dump_prefix = 0  # reset dump index

        compile_range = get_pass_context().compile_range
        for pass_ in self.passes:
            if pass_.is_applicable_for_range(compile_range):
                pass_(graph)
                VllmInductorPass.dump_prefix += 1
            else:
                logger.debug("Skipping %s with compile range %s", pass_, compile_range)

        # perform the first post-cleanup before IR lowering to clean up fusion artifacts
        # and make sure no dead IR ops are lowered.
        self.post_cleanup(graph)
        VllmInductorPass.dump_prefix += 1

        # lowering before cleanup so DCE can clean up lowered ops.
        # DCE handles mutating ops correctly as well.
        self.ir_lowering(graph)
        VllmInductorPass.dump_prefix += 1
        self.clone_elimination(graph)
        VllmInductorPass.dump_prefix += 1

        # clean up after lowering again
        self.post_cleanup(graph)
        VllmInductorPass.dump_prefix += 1

        # always run fix_functionalization last
        self.fix_functionalization(graph)
        VllmInductorPass.dump_prefix = None  # Cleanup index

        VllmPatternMatcherPass.log_match_summary()

    defconfigure(self, config: VllmConfig) -> None:
        self.pass_config = config.compilation_config.pass_config

        # Set the current vllm config to allow tracing CustomOp instances
        with set_current_vllm_config(config, check_compile=False):
            if self.pass_config.eliminate_noops:
                self.passes += [NoOpEliminationPass(config)]

            if self.pass_config.enable_sp:
                self.passes += [SequenceParallelismPass(config)]
                if self.pass_config.fuse_gemm_comms:
                    self.passes += [AsyncTPPass(config)]

            if self.pass_config.fuse_allreduce_rms:
                if rocm_aiter_ops.is_enabled():
                    self.passes += [RocmAiterAllReduceFusionPass(config)]
                else:
                    self.passes += [AllReduceFusionPass(config)]

            if self.pass_config.fuse_minimax_qk_norm:
                self.passes += [MiniMaxQKNormPass(config)]

            if self.pass_config.fuse_norm_quant:
                if rocm_aiter_ops.is_enabled():
                    self.passes += [
                        RocmAiterRMSNormQuantFusionPass(config),
                    ]
                self.passes += [RMSNormQuantFusionPass(config)]

            if self.pass_config.fuse_act_quant:
                self.passes += [ActivationQuantFusionPass(config)]
                if rocm_aiter_ops.is_enabled():
                    self.passes += [RocmAiterSiluMulFp8GroupQuantFusionPass(config)]

            if self.pass_config.fuse_act_padding and rocm_aiter_ops.is_enabled():
                self.passes += [RocmAiterTritonAddRMSNormPadFusionPass(config)]

            if self.pass_config.fuse_mla_dual_rms_norm and rocm_aiter_ops.is_enabled():
                self.passes += [MLADualRMSNormFusionPass(config)]

            if self.pass_config.fuse_rope_kvcache:
                self.passes += [SplitCoalescingPass(config)]
                self.passes += [ScatterSplitReplacementPass(config)]
                self.passes += [RopeKVCacheFusionPass(config)]

            if self.pass_config.fuse_attn_quant:
                self.passes += [AttnQuantFusionPass(config)]
                self.passes += [MLAAttnQuantFusionPass(config)]

            if self.pass_config.enable_qk_norm_rope_fusion:
                self.passes += [SplitCoalescingPass(config)]
                self.passes += [QKNormRoPEFusionPass(config)]

            self.ir_lowering = VllmIRLoweringPass(config)
            self.clone_elimination = UnsafeCloneEliminationPass(config)
            self.post_cleanup = PostCleanupPass(config)
            self.fix_functionalization = FixFunctionalizationPass(config)

    defadd(self, pass_: InductorPass) -> None:
        assert isinstance(pass_, InductorPass)
        self.passes.append(pass_)

    defuuid(self) -> str:
"""
        The PostGradPassManager is set as a custom pass in the Inductor and
        affects compilation caching. Its uuid depends on the UUIDs of all
        dependent passes and the pass config. See InductorPass for more info.
        """
        passes = []

        state: dict[str, Any] = {"pass_config": self.pass_config.compute_hash()}
        for pass_ in self.passes:
            passes.append(pass_.uuid())

        passes.append(self.post_cleanup.uuid())
        passes.append(self.ir_lowering.uuid())
        passes.append(self.clone_elimination.uuid())
        passes.append(self.post_cleanup.uuid())
        passes.append(self.fix_functionalization.uuid())

        # Include the compile range in the uuid to ensure that inductor
        # recompiles the graph for the new dynamic compile range.
        state["compile_range"] = str(get_pass_context().compile_range)
        state["passes"] = passes
        return InductorPass.hash_dict(state)
```

### uuid [¶](#vllm.compilation.passes.pass_manager.PostGradPassManager.uuid "Permanent link")

The PostGradPassManager is set as a custom pass in the Inductor and affects compilation caching. Its uuid depends on the UUIDs of all dependent passes and the pass config. See InductorPass for more info.

Source code in `vllm/compilation/passes/pass_manager.py`

```
defuuid(self) -> str:
"""
    The PostGradPassManager is set as a custom pass in the Inductor and
    affects compilation caching. Its uuid depends on the UUIDs of all
    dependent passes and the pass config. See InductorPass for more info.
    """
    passes = []

    state: dict[str, Any] = {"pass_config": self.pass_config.compute_hash()}
    for pass_ in self.passes:
        passes.append(pass_.uuid())

    passes.append(self.post_cleanup.uuid())
    passes.append(self.ir_lowering.uuid())
    passes.append(self.clone_elimination.uuid())
    passes.append(self.post_cleanup.uuid())
    passes.append(self.fix_functionalization.uuid())

    # Include the compile range in the uuid to ensure that inductor
    # recompiles the graph for the new dynamic compile range.
    state["compile_range"] = str(get_pass_context().compile_range)
    state["passes"] = passes
    return InductorPass.hash_dict(state)
```

## with\_pattern\_match\_debug [¶](#vllm.compilation.passes.pass_manager.with_pattern_match_debug "Permanent link")

Function decorator that turns on inductor pattern match debug for the duration of the call. Used to avoid logging builtin Inductor pattern matching.

Source code in `vllm/compilation/passes/pass_manager.py`

```
defwith_pattern_match_debug(fn: Callable[P, R]) -> Callable[P, R]:
"""
    Function decorator that turns on inductor pattern match debug
    for the duration of the call.
    Used to avoid logging builtin Inductor pattern matching.
    """

    @functools.wraps(fn)
    defwrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        if (debug_val := envs.VLLM_PATTERN_MATCH_DEBUG) is not None:
            # optionally check rank here
            with set_env_var("TORCHINDUCTOR_PATTERN_MATCH_DEBUG", debug_val):
                return fn(*args, **kwargs)
        return fn(*args, **kwargs)

    return wrapper
```