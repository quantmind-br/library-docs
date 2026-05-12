---
title: compiler_interface - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/compilation/compiler_interface/
source: sitemap
fetched_at: 2026-05-07T21:16:13.850266947-03:00
rendered_js: false
word_count: 0
summary: This document defines an InductorAdaptor class for integrating the PyTorch Inductor compiler into the vLLM ecosystem, managing cache initialization, graph compilation, and monkey-patching internal compiler functions to ensure compatibility.
tags:
    - pytorch
    - inductor
    - vllm
    - compilation
    - caching
    - fx-graph
    - monkey-patching
category: api
---

```
classInductorAdaptor(CompilerInterface):
"""
    The adaptor for the Inductor compiler, version 2.5, 2.6, 2.7.
    """

    name = "inductor"

    defcompute_hash(self, vllm_config: VllmConfig) -> str:
        factors = get_inductor_factors()
        hash_str: str = safe_hash(
            str(factors).encode(), usedforsecurity=False
        ).hexdigest()[:10]
        return hash_str

    definitialize_cache(
        self, cache_dir: str, disable_cache: bool = False, prefix: str = ""
    ) -> None:
        self.cache_dir = cache_dir
        self.prefix = prefix
        self.base_cache_dir = cache_dir[: -len(prefix)] if prefix else cache_dir
        if disable_cache:
            return
        # redirect the cache directory to a subdirectory
        # set flags so that Inductor and Triton store their cache
        # in the cache_dir, then users only need to copy the cache_dir
        # to another machine to reuse the cache.
        inductor_cache = os.path.join(self.base_cache_dir, "inductor_cache")
        os.makedirs(inductor_cache, exist_ok=True)
        os.environ["TORCHINDUCTOR_CACHE_DIR"] = inductor_cache
        triton_cache = os.path.join(self.base_cache_dir, "triton_cache")
        os.makedirs(triton_cache, exist_ok=True)
        os.environ["TRITON_CACHE_DIR"] = triton_cache

    defcompile(
        self,
        graph: fx.GraphModule,
        example_inputs: list[Any],
        compiler_config: dict[str, Any],
        compile_range: Range,
        key: str | None = None,
    ) -> tuple[Callable[..., Any] | None, Any | None]:
        _apply_constrain_to_fx_strides_patch()
        compilation_counter.num_inductor_compiles += 1
        fromtorch._inductor.compile_fximport compile_fx

        current_config = {}
        if compiler_config is not None:
            current_config.update(compiler_config)

        # disable remote cache
        current_config["fx_graph_cache"] = True
        current_config["fx_graph_remote_cache"] = False

        set_inductor_config(current_config, compile_range)
        set_functorch_config()

        # inductor can inplace modify the graph, so we need to copy it
        # see https://github.com/pytorch/pytorch/issues/138980
        graph = copy.deepcopy(graph)

        # it's the first time we compile this graph
        # the assumption is that we don't have nested Inductor compilation.
        # compiled_fx_graph_hash will only be called once, and we can hook
        # it to get the hash of the compiled graph directly.

        hash_str, file_path = None, None
        fromtorch._inductor.codecacheimport compiled_fx_graph_hash

        defhijacked_compile_fx_inner(*args: Any, **kwargs: Any) -> Any:
            output = torch._inductor.compile_fx.compile_fx_inner(*args, **kwargs)
            nonlocal hash_str
            inductor_compiled_graph = output
            if inductor_compiled_graph is not None:
                nonlocal file_path
                compiled_fn = inductor_compiled_graph.current_callable
                file_path = compiled_fn.__code__.co_filename  # noqa
                if (
                    not file_path.startswith(self.base_cache_dir)
                    and compiled_fn.__closure__ is not None
                ):
                    # hooked in the align_inputs_from_check_idxs function
                    # in torch/_inductor/utils.py
                    for cell in compiled_fn.__closure__:
                        if not callable(cell.cell_contents):
                            continue
                        code = cell.cell_contents.__code__
                        if code.co_filename.startswith(self.base_cache_dir):
                            # this is the real file path
                            # compiled from Inductor
                            file_path = code.co_filename
                            break
                hash_str = inductor_compiled_graph._fx_graph_cache_key
            return output

        defhijack_compiled_fx_graph_hash(*args: Any, **kwargs: Any) -> Any:
            out = compiled_fx_graph_hash(*args, **kwargs)
            nonlocal hash_str
            hash_str = out[0]
            return out

        def_check_can_cache(*args: Any, **kwargs: Any) -> None:
            # no error means it can be cached.
            # Inductor refuses to cache the graph outside of Dynamo
            # tracing context, and also disables caching for graphs
            # with high-order ops.
            # For vLLM, in either case, we want to cache the graph.
            # see https://github.com/pytorch/pytorch/blob/9f5ebf3fc609105a74eab4ccc24932d6353ff566/torch/_inductor/codecache.py#L1221 # noqa
            return

        def_get_shape_env() -> AlwaysHitShapeEnv:
            return AlwaysHitShapeEnv()

        with ExitStack() as stack:
            # for hijacking the hash of the compiled graph
            stack.enter_context(
                patch(
                    "torch._inductor.codecache.compiled_fx_graph_hash",
                    hijack_compiled_fx_graph_hash,
                )
            )

            # for providing a dummy shape environment
            stack.enter_context(
                patch(
                    "torch._inductor.codecache.FxGraphCache._get_shape_env",
                    _get_shape_env,
                )
            )

            fromtorch._functorch._aot_autograd.autograd_cacheimport AOTAutogradCache

            # torch 2.8+ on main uses _get_shape_env in AOTAutogradCache
            if hasattr(AOTAutogradCache, "_get_shape_env"):
                stack.enter_context(
                    patch(
                        "torch._functorch._aot_autograd.autograd_cache.AOTAutogradCache._get_shape_env",
                        _get_shape_env,
                    )
                )

            # for forcing the graph to be cached
            stack.enter_context(
                patch(
                    "torch._inductor.codecache.FxGraphCache._check_can_cache",
                    _check_can_cache,
                )
            )

            # Dynamo metrics context, see method for more details.
            stack.enter_context(self.metrics_context())

            # Disable remote caching. When these are on, on remote cache-hit,
            # the monkey-patched functions never actually get called.
            # vLLM today assumes and requires the monkey-patched functions to
            # get hit.
            # TODO(zou3519): we're going to replace this all with
            # standalone_compile sometime.
            stack.enter_context(
                torch._inductor.config.patch(fx_graph_remote_cache=False)
            )
            # InductorAdaptor (unfortunately) requires AOTAutogradCache
            # to be turned off to run. It will fail to acquire the hash_str
            # and error if not.
            # StandaloneInductorAdaptor (PyTorch 2.8+) fixes this problem.
            stack.enter_context(
                torch._functorch.config.patch(enable_autograd_cache=False)
            )
            stack.enter_context(
                torch._functorch.config.patch(enable_remote_autograd_cache=False)
            )

            # Clear the tracing context before calling compile_fx.
            # vLLM calls compile_fx from within a PiecewiseCompileInterpreter
            # that runs under Dynamo's tracing context. The tracing context
            # has a FakeTensorMode from Dynamo, but the example inputs for
            # this subgraph have fake tensors from a different FakeTensorMode.
            # compile_fx's _compile_fx_main calls detect_fake_mode() which
            # asserts all FakeTensorModes match, causing a crash.
            # Clearing the tracing context lets compile_fx create its own.
            saved_tracing_context = torch._guards.TracingContext.try_get()
            if saved_tracing_context is not None:
                torch._guards._TLS.tracing_context = None

                def_restore_tracing_context():
                    torch._guards._TLS.tracing_context = saved_tracing_context

                stack.callback(_restore_tracing_context)

            compiled_graph = compile_fx(
                graph,
                example_inputs,
                inner_compile=hijacked_compile_fx_inner,
                config_patches=current_config,
            )

        # Turn off the checks if we disable the compilation cache.
        if is_compile_cache_enabled(compiler_config):
            if hash_str is None:
                raise RuntimeError(
                    "vLLM failed to compile the model. The most "
                    "likely reason for this is that a previous compilation "
                    "failed, leading to a corrupted compilation artifact. "
                    "We recommend trying to "
                    "remove ~/.cache/vllm/torch_compile_cache and try again "
                    "to see the real issue. "
                )
            assert file_path is not None, (
                "failed to get the file path of the compiled graph"
            )
        return compiled_graph, (hash_str, file_path)

    defload(
        self,
        handle: Any,
        graph: fx.GraphModule,
        example_inputs: list[Any],
        graph_index: int,
        compile_range: Range,
    ) -> Callable[..., Any]:
        assert isinstance(handle, tuple)
        assert isinstance(handle[0], str)
        assert isinstance(handle[1], str)
        hash_str = handle[0]

        fromtorch._functorch._aot_autograd.autograd_cacheimport AOTAutogradCache
        fromtorch._inductor.codecacheimport FxGraphCache

        with ExitStack() as exit_stack:
            exit_stack.enter_context(
                patch(
                    "torch._inductor.codecache.FxGraphCache._get_shape_env",
                    lambda *args, **kwargs: AlwaysHitShapeEnv(),
                )
            )
            # torch 2.8+ on main uses _get_shape_env in AOTAutogradCache
            if hasattr(AOTAutogradCache, "_get_shape_env"):
                exit_stack.enter_context(
                    patch(
                        "torch._functorch._aot_autograd.autograd_cache.AOTAutogradCache._get_shape_env",
                        lambda *args, **kwargs: AlwaysHitShapeEnv(),
                    )
                )

            # Dynamo metrics context, see method for more details.
            exit_stack.enter_context(self.metrics_context())

            fromtorch._inductor.output_codeimport CompiledFxGraphConstantsWithGm

            constants = CompiledFxGraphConstantsWithGm(graph)
            inductor_compiled_graph, _ = FxGraphCache._lookup_graph(
                hash_str, example_inputs, True, None, constants
            )
            assert inductor_compiled_graph is not None, (
                "Inductor cache lookup failed. Please remove "
                f"the cache directory and try again."  # noqa
            )

        # Inductor calling convention (function signature):
        # f(list) -> tuple
        # Dynamo calling convention (function signature):
        # f(*args) -> Any

        # need to know if the graph returns a tuple
        fromtorch._inductor.compile_fximport graph_returns_tuple

        returns_tuple = graph_returns_tuple(graph)

        # this is the callable we return to Dynamo to run
        defcompiled_graph(*args: Any) -> tuple[Any, ...] | Any:
            # convert args to list
            list_args = list(args)
            graph_output = inductor_compiled_graph(list_args)
            # unpack the tuple if needed
            if returns_tuple:
                return graph_output
            else:
                return graph_output[0]

        return compiled_graph

    defmetrics_context(self) -> contextlib.AbstractContextManager[Any]:
"""
        This method returns the Dynamo metrics context (if it exists,
        otherwise a null context). It is used by various compile components.
        Present in torch>=2.6, it's used inside FxGraphCache in
        torch==2.6 (but not after). It might also be used in various other
        torch.compile internal functions.

        Because it is re-entrant, we always set it (even if entering via Dynamo
        and the context was already entered). We might want to revisit if it
        should be set at a different mode of compilation.

        This is likely a bug in PyTorch: public APIs should not rely on
        manually setting up internal contexts. But we also rely on non-public
        APIs which might not provide these guarantees.
        """
        if is_torch_equal_or_newer("2.6"):
            importtorch._dynamo.utils

            return torch._dynamo.utils.get_metrics_context()  # type: ignore[no-any-return]
        else:
            return contextlib.nullcontext()
```