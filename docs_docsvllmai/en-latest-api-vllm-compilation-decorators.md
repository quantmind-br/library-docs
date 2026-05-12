---
title: decorators - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/compilation/decorators/
source: sitemap
fetched_at: 2026-05-07T21:16:17.142094524-03:00
rendered_js: false
word_count: 12
summary: This document defines a decorator and implementation logic for enabling PyTorch compilation in vLLM, specifically managing dynamic shapes, model initialization patching, and graph compilation integration.
tags:
    - pytorch
    - torch-compile
    - vllm
    - decorator
    - dynamic-shapes
    - model-optimization
category: concept
---

```
def_support_torch_compile(
    cls: type[_T],
    dynamic_arg_dims: dict[str, int | list[int] | dict[int, str]],
    mark_unbacked_dims: dict[str, int | list[int]] | None = None,
    enable_if: Callable[[VllmConfig], bool] | None = None,
    is_encoder: bool = False,
) -> type[_T]:
"""Internal implementation of support_torch_compile decorator."""

    if TorchCompileWithNoGuardsWrapper in cls.__bases__:
        # support decorating multiple times
        return cls

    # take care of method resolution order
    # make sure super().__init__ is called on the base class
    #  other than TorchCompileWithNoGuardsWrapper
    cls.__bases__ = cls.__bases__ + (TorchCompileWithNoGuardsWrapper,)

    old_init = cls.__init__

    setattr(cls, IGNORE_COMPILE_KEY, False)

    def__init__(
        self: _T,
        *args,
        vllm_config: VllmConfig | None = None,
        prefix: str = "",
        **kwargs: Any,
    ) -> None:
        if vllm_config is None:
            vllm_config = get_current_vllm_config()

        # NOTE: to support multimodal models (such as encoder),
        # we may not have vllm_config so we may need to patch it
        sig = inspect.signature(old_init)
        # Check that any positional arguments match the old_init method signature
        annotations = [p.annotation for p in sig.parameters.values()]
        for arg, annotation in zip(args, annotations):
            if annotation is inspect._empty:
                continue
            if not isinstance(arg, annotation):
                init = f"'{type(self).__name__}.__init__'"
                arg_type = f"'{type(arg).__name__}'"
                raise TypeError(
                    f"{init} received a positional argument of type {arg_type}, "
                    "but no parameter of that type was found in the method signature. "
                    f"Please either annotate {init} or pass it as a keyword argument."
                )
        if "vllm_config" in sig.parameters:
            kwargs["vllm_config"] = vllm_config
        if "prefix" in sig.parameters:
            kwargs["prefix"] = prefix
        old_init(self, *args, **kwargs)

        self.vllm_config = vllm_config
        self.compilation_config = self.vllm_config.compilation_config
        enable_compile = enable_if is None or enable_if(vllm_config)
        # for CompilationMode.STOCK_TORCH_COMPILE , the upper level model runner
        # will handle the compilation, so we don't need to do anything here.
        self.do_not_compile = (
            self.compilation_config.mode
            in [CompilationMode.NONE, CompilationMode.STOCK_TORCH_COMPILE]
            or _should_ignore_torch_compile(self.__class__)
            or not enable_compile
        )
        if self.do_not_compile:
            return

        self._dynamic_arg_dims = dynamic_arg_dims

        self.was_aot_compile_fn_loaded_from_disk = False
        compilation_counter.num_models_seen += 1
        self.compiled = False

        # Handled by monkeypatching `TorchCompileWithNoGuardsWrapper` into base class
        TorchCompileWithNoGuardsWrapper.__init__(
            self,
            compile_prefix=cls.__name__ if is_encoder else "",
            is_encoder=is_encoder,
        )

    cls.__init__ = __init__

    def_mark_dynamic_inputs(
        mod: type[_T], ds_type: DynamicShapesType, *args: Any, **kwargs: Any
    ) -> None:
        defmark_dynamic(
            arg: torch.Tensor, dim_shape_pairs: list[tuple[int, str | None]]
        ) -> None:
            if ds_type == DynamicShapesType.UNBACKED:
                if is_torch_equal_or_newer("2.10.0"):
                    for dim, shape_id in dim_shape_pairs:
                        if shape_id is not None:
                            if not _SUPPORTS_SHAPE_ID:
                                raise RuntimeError(
                                    f"shape_id='{shape_id}' requires PyTorch >= 2.11.0"
                                )
                            torch._dynamo.decorators.mark_unbacked(
                                arg,
                                dim,
                                hint_override=arg.size()[dim],
                                shape_id=shape_id,
                            )
                        else:
                            torch._dynamo.decorators.mark_unbacked(
                                arg,
                                dim,
                                hint_override=arg.size()[dim],
                            )
                else:
                    # For older versions, we can't use hint_override or shape_id
                    dims = [dim for dim, _ in dim_shape_pairs]
                    torch._dynamo.decorators.mark_unbacked(arg, dims)
            else:
                dims = [dim for dim, _ in dim_shape_pairs]
                torch._dynamo.mark_dynamic(arg, dims)

        sig = inspect.signature(mod.__class__.forward)  # type: ignore[attr-defined]
        bound_args = sig.bind(mod, *args, **kwargs)
        bound_args.apply_defaults()

        # Normalize dynamic_arg_dims to dict[str, dict[int, str | None]]
        normalized_dims: dict[str, dict[int, str | None]] = {}
        for k, v in dynamic_arg_dims.items():
            if isinstance(v, dict):
                normalized_dims[k] = {dim: shape_id for dim, shape_id in v.items()}
            elif isinstance(v, int):
                normalized_dims[k] = {v: None}
            else:
                normalized_dims[k] = {d: None for d in v}

        for k, dim_to_shape_id in normalized_dims.items():
            arg = bound_args.arguments.get(k)

            if arg is not None:
                dims = list(dim_to_shape_id.keys())

                if isinstance(arg, torch.Tensor):
                    dim_shape_pairs = [
                        (arg.ndim + d if d < 0 else d, dim_to_shape_id.get(d))
                        for d in dims
                    ]
                    mark_dynamic(arg, dim_shape_pairs)
                elif isinstance(arg, IntermediateTensors):
                    for tensor in arg.tensors.values():
                        dim_shape_pairs = [
                            (tensor.ndim + d if d < 0 else d, dim_to_shape_id.get(d))
                            for d in dims
                        ]
                        mark_dynamic(tensor, dim_shape_pairs)
                else:
                    raise ValueError(
                        f"Unsupported dynamic dimensions {dims} "
                        f"for argument {k} with type {type(arg)}."
                    )

        if mark_unbacked_dims:
            for k, dims_val in mark_unbacked_dims.items():
                arg = bound_args.arguments.get(k)
                if arg is not None:
                    dims = [dims_val] if isinstance(dims_val, int) else list(dims_val)
                    if isinstance(arg, torch.Tensor):
                        dims = [arg.ndim + d if d < 0 else d for d in dims]
                        if is_torch_equal_or_newer("2.10.0"):
                            for dim in dims:
                                torch._dynamo.decorators.mark_unbacked(
                                    arg, dim, hint_override=arg.size()[dim]
                                )
                        else:
                            torch._dynamo.decorators.mark_unbacked(arg, dims)

    def__call__(self: type[_T], *args: Any, **kwargs: Any) -> Any:
        # torch.compiler.is_compiling() means we are inside the compilation
        # e.g. TPU has the compilation logic in model runner, so we don't
        # need to compile the model inside.
        if self.do_not_compile or torch.compiler.is_compiling():
            return self.forward(*args, **kwargs)

        # If skip_compiled is set, bypass compiled model call. This is used e.g. for
        # enc-dec models where tensor shapes/types vary across invocations, preventing
        # the capture of a single computational graph.
        if is_forward_context_available() and get_forward_context().skip_compiled:
            return self.forward(*args, **kwargs)

        # if aot_compiled_fn is set, call it with partition wrapper context.
        # The partition wrapper must be active at runtime for CUDA graph
        # capture to work correctly with inductor graph partitioning.
        if getattr(self, "aot_compiled_fn", None) is not None:
            with maybe_use_cudagraph_partition_wrapper(self.vllm_config):
                return self.aot_compiled_fn(self, *args, **kwargs)

        ds_type = self.compilation_config.dynamic_shapes_config.type
        cache_dir = None
        aot_compilation_path = None
        if envs.VLLM_USE_AOT_COMPILE:
"""
            When using torch.compile in AOT mode, we store the cache artifacts
            under VLLM_CACHE_ROOT/torch_compile_cache/torch_aot_compile/{hash}
            The {hash} contains all of the factors except for the source files
            being traced through, because we don't actually know which source
            files to check at this point (before dynamo runs).
            On loading we will actually look at the source files being traced
            through. If any source file have changed (compared with the
            serialized backend artifacts), then we need to generate a new AOT
            compile artifact from scratch.
            """
            from.cachingimport aot_compile_hash_factors

            factors: list[str] = aot_compile_hash_factors(self.vllm_config)

            factors.append(_model_hash_key(self.forward))
            hash_key = hashlib.sha256(str(factors).encode()).hexdigest()
            cache_dir = os.path.join(
                envs.VLLM_CACHE_ROOT,
                "torch_compile_cache",
                "torch_aot_compile",
                hash_key,
            )

            # Hash-level dir; shared across ranks on the same node.
            self.compilation_config.local_cache_dir = cache_dir
            inductor_cache = os.path.join(cache_dir, "inductor_cache")
            os.makedirs(inductor_cache, exist_ok=True)
            # Process-wide: post-load execution, CUDA-graph capture, and later
            # autotune/recompile all need to write under {hash}/inductor_cache/.
            # Unconditional because torch's cache_dir() may have pre-filled the
            # /tmp default during import, making setdefault a no-op.
            os.environ["TORCHINDUCTOR_CACHE_DIR"] = inductor_cache

            rank = self.vllm_config.parallel_config.rank
            dp_rank = self.vllm_config.parallel_config.data_parallel_index
            cache_dir = os.path.join(cache_dir, f"rank_{rank}_{dp_rank}")
            aot_compilation_path = os.path.join(cache_dir, "model")
            if not envs.VLLM_DISABLE_COMPILE_CACHE:
                loaded_fn = _try_load_aot_compiled_fn(self, aot_compilation_path)
                if loaded_fn is not None:
                    self.aot_compiled_fn = loaded_fn
                    self.was_aot_compile_fn_loaded_from_disk = True
                    with (
                        monitor_profiling_run(),
                        maybe_use_cudagraph_partition_wrapper(self.vllm_config),
                    ):
                        output = self.aot_compiled_fn(self, *args, **kwargs)
                    return output

        if self.compiled:
            assert (
                not envs.VLLM_USE_AOT_COMPILE
                or self.vllm_config.compilation_config.backend == "eager"
            )
            return TorchCompileWithNoGuardsWrapper.__call__(self, *args, **kwargs)  # type: ignore[arg-type]

        # This is the path for the first compilation.
        # the first compilation needs to have dynamic shapes marked
        _mark_dynamic_inputs(
            self,
            ds_type,
            *args,
            **kwargs,
        )

        original_code_object = self.original_code_object()
        logger.debug("Start compiling function %s", original_code_object)

        # we do not want tp delete the original code object entries since
        # we depend on them now to look up cached compiled functions.
        # torch._dynamo.eval_frame.remove_from_cache(original_code_object)

        # collect all relevant files traced by Dynamo,
        # so that the compilation cache can trigger re-compilation
        # properly when any of these files change.

        # 1. the file containing the top-level forward function
        self.compilation_config.traced_files.add(original_code_object.co_filename)

        # 2. every time Dynamo sees a function call, it will inline
        # the function by calling InliningInstructionTranslator.inline_call_
        # we hijack this function to know all the functions called
        # during Dynamo tracing, and their corresponding files
        inline_call = InliningInstructionTranslator.inline_call_

        defpatched_inline_call(self_: Any) -> Any:
            code = self_.f_code
            self.compilation_config.traced_files.add(code.co_filename)
            return inline_call(self_)

        # Disable the C++ compilation of symbolic shape guards. C++-fication
        # of symbolic shape guards can improve guard overhead. But, since
        # vllm skip guards anyways, setting this flag to False can improve
        # compile time.
        dynamo_config_patches = {}
        try:
            _ = torch._dynamo.config.enable_cpp_symbolic_shape_guards
            dynamo_config_patches["enable_cpp_symbolic_shape_guards"] = False
        except AttributeError:
            # Note: this config is not available in torch 2.6, we can skip
            # if the config doesn't exist
            logger.debug("enable_cpp_symbolic_shape_guards config not available")

        # Prepare backed_size_oblivious config patch if needed
        fx_config_patches = {}
        if ds_type == DynamicShapesType.BACKED_SIZE_OBLIVIOUS:
            fx_config_patches["backed_size_oblivious"] = True

        # Prepare inductor config patches
        # assume_32bit_indexing is only available in torch 2.10.0+
        inductor_config_patches = {}
        if is_torch_equal_or_newer("2.10.0"):
            inductor_config_patches["assume_32bit_indexing"] = (
                self.compilation_config.dynamic_shapes_config.assume_32_bit_indexing
            )

        with (
            patch.object(
                InliningInstructionTranslator, "inline_call_", patched_inline_call
            ),
            torch._dynamo.config.patch(**dynamo_config_patches),
            maybe_use_cudagraph_partition_wrapper(self.vllm_config),
            torch.fx.experimental._config.patch(**fx_config_patches),
            torch._inductor.config.patch(**inductor_config_patches),
        ):
            use_aot_compile = envs.VLLM_USE_AOT_COMPILE
            if self.vllm_config.compilation_config.backend == "eager":
                logger.warning("Detected eager backend, disabling AOT compile.")
                use_aot_compile = False
            if use_aot_compile:
                # store the path for saving after warmup
                self._aot_compilation_path = aot_compilation_path
                self._aot_cache_dir = cache_dir
                with monitor_torch_compile(
                    self.vllm_config, is_encoder=self._is_encoder
                ):
                    self.aot_compiled_fn = self.aot_compile(*args, **kwargs)
                    compilation_counter.num_aot_compiles += 1
                    # All compilation is done at this point, save the
                    # AOT artifact.
                    self.save_aot_compiled_function()

                with monitor_profiling_run():
                    output = self.aot_compiled_fn(self, *args, **kwargs)
            else:
                with monitor_torch_compile(
                    self.vllm_config,
                    "torch.compile and initial profiling/warmup "
                    "run together took %.2f s in total",
                    is_encoder=self._is_encoder,
                ):
                    output = TorchCompileWithNoGuardsWrapper.__call__(
                        self,  # type: ignore[arg-type]
                        *args,
                        **kwargs,
                    )

        self.compiled = True
        return output

    # triggers VllmSerializableFunction.serialize()
    defsave_aot_compiled_function(self: type[_T]) -> None:
        if envs.VLLM_DISABLE_COMPILE_CACHE:
            return

        if self.was_aot_compile_fn_loaded_from_disk:
            logger.debug("AOT compiled function was loaded from cache, skipping save")
            return

        assert (
            self.aot_compiled_fn and self._aot_compilation_path and self._aot_cache_dir
        )

        try:
            os.makedirs(self._aot_cache_dir, exist_ok=True)
            # File saving should be atomic, so we will save to a temporary location
            # first. Should be upstreamed to PyTorch 2.12 as well.
            tmp_file = f"{self._aot_compilation_path}.{os.getpid()}.tmp"
            self.aot_compiled_fn.save_compiled_function(tmp_file)
            os.replace(tmp_file, self._aot_compilation_path)
            compilation_counter.num_aot_artifacts_saved += 1
            logger.info_once(
                "saved AOT compiled function to %s",
                self._aot_compilation_path,
            )
        except Exception as e:
            logger.warning(
                "unable to save AOT compiled function to %s: %s",
                self._aot_compilation_path,
                e,
            )

    cls.__call__ = __call__
    cls.save_aot_compiled_function = save_aot_compiled_function
    return cls
```