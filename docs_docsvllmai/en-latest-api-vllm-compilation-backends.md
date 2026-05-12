---
title: backends - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/compilation/backends/
source: sitemap
fetched_at: 2026-05-07T21:16:09.959017689-03:00
rendered_js: false
word_count: 24
summary: The VllmBackend class provides a custom compilation backend for torch.compile in vLLM, responsible for partitioning computational graphs and managing Inductor post-gradient passes.
tags:
    - vllm
    - torch-compile
    - graph-compilation
    - backend-integration
    - model-optimization
    - inductor
category: concept
---

```
classVllmBackend:
"""The compilation backend for `torch.compile` with vLLM.
    It is used for compilation mode of `CompilationMode.VLLM_COMPILE`,
    where we customize the compilation.

    The major work of this backend is to split the graph into
    piecewise graphs, and pass them to the piecewise backend.

    This backend also adds the PostGradPassManager to Inductor config,
    which handles the post-grad passes.
    """

    vllm_config: VllmConfig
    compilation_config: CompilationConfig
    _called: bool = False
    # the graph we compiled
    graph: fx.GraphModule
    # the stiching graph module for all the piecewise graphs
    split_gm: fx.GraphModule
    piecewise_graphs: list[SplitItem]
    returned_callable: Callable[..., Any]
    # Inductor passes to run on the graph pre-defunctionalization
    post_grad_passes: Sequence[Callable[..., Any]]
    compiler_manager: CompilerManager
    # Copy of CompilationConfig.inductor_compile_config +
    # an entry for PostGradPassManager
    inductor_config: dict[str, Any]

    def__init__(
        self,
        vllm_config: VllmConfig,
        prefix: str = "",
        is_encoder: bool = False,
    ) -> None:
        # if the model is initialized with a non-empty prefix,
        # then usually it's enough to use that prefix,
        # e.g. language_model, vision_model, etc.
        # when multiple parts are initialized as independent
        # models, we need to use the model_tag to distinguish
        # them, e.g. backbone (default), eagle_head, etc.
        self.prefix = prefix or model_tag

        # Mark compilation for encoder.
        self.is_encoder = is_encoder or model_is_encoder

        # Passes to run on the graph post-grad.
        self.pass_manager = resolve_obj_by_qualname(
            current_platform.get_pass_manager_cls()
        )()
        self.pass_key = current_platform.pass_key

        self.vllm_config = vllm_config
        self.compilation_config = vllm_config.compilation_config

        self.compiler_manager: CompilerManager = CompilerManager(
            self.compilation_config
        )

        # Deepcopy the inductor config to detach the post-grad custom pass
        # from CompilationConfig.
        # We want to avoid PostGradPassManager in CompilationConfig because
        # in future we need PostGradPassManager.uuid() to be executed
        # only at compile time.
        self.inductor_config = deepcopy(self.compilation_config.inductor_compile_config)
        # `torch.compile` is JIT compiled, so we don't need to
        # do anything here

    defcollect_standalone_compile_artifacts(
        self,
    ) -> tuple[Any, dict[str, list[int]] | None, dict[str, bool] | None]:
"""Collect inductor cache artifacts from all piecewise backends.

        Returns:
            tuple: (standalone_compile_artifacts, sym_shape_indices_map,
                    returns_tuple_map)
                - standalone_compile_artifacts: StandaloneCompiledArtifacts
                  with compiled artifacts
                - sym_shape_indices_map: dict mapping submod_name to
                  sym_shape_indices
                - returns_tuple_map: dict mapping submod_name to
                  returns_tuple
        """

        if not envs.VLLM_USE_MEGA_AOT_ARTIFACT:
            return None, None, None

        from.cachingimport StandaloneCompiledArtifacts
        from.piecewise_backendimport PiecewiseBackend

        standalone_compile_artifacts = StandaloneCompiledArtifacts()
        sym_shape_indices_map = {}
        returns_tuple_map = {}

        for name, _ in self.split_gm.named_children():
            # get the actual attribute (shadowed by PiecewiseBackend in __dict__)
            child = getattr(self.split_gm, name)
            # unwrap the static graph wrapper class if applicable
            piecewise_backend = child.runnable if hasattr(child, "runnable") else child

            if not isinstance(piecewise_backend, PiecewiseBackend):
                continue

            submod_name = name
            sym_shape_indices_map[submod_name] = piecewise_backend.sym_shape_indices
            returns_tuple_map[submod_name] = piecewise_backend.returns_tuple

            for shape_str, bytes_data in piecewise_backend.to_bytes().items():
                standalone_compile_artifacts.insert(submod_name, shape_str, bytes_data)
                logger.debug(
                    "collected artifact for %s shape %s (%d bytes)",
                    submod_name,
                    shape_str,
                    len(bytes_data),
                )

        logger.info(
            "collected artifacts: %d entries, %d artifacts, %d bytes total",
            standalone_compile_artifacts.num_entries(),
            standalone_compile_artifacts.num_artifacts(),
            standalone_compile_artifacts.size_bytes(),
        )

        logger.debug(
            "standalone compile artifact keys: %s",
            list(standalone_compile_artifacts.submodule_bytes.keys()),
        )

        return standalone_compile_artifacts, sym_shape_indices_map, returns_tuple_map

    defconfigure_post_pass(self) -> None:
        # TODO proper PassManager?
        pre_grad_pass_key = "pre_grad_custom_pass"
        assert self.pass_key != pre_grad_pass_key
        assert pre_grad_pass_key not in self.inductor_config
        self.inductor_config[pre_grad_pass_key] = VllmIRInplaceFunctionalizationPass(
            self.vllm_config
        )

        # Make sure pre_grad_custom_pass is not pickled
        # as part of AOTAutograd built-in cache key
        # TODO(luka) is there a cleaner way to do this
        importtorch._inductor.configasinductor_config

        ignore = inductor_config._cache_config_ignore_prefix + [pre_grad_pass_key]
        assert "_cache_config_ignore_prefix" not in self.inductor_config
        self.inductor_config["_cache_config_ignore_prefix"] = ignore

        # Configure the (nominally post-grad) pass manager
        self.pass_manager.configure(self.vllm_config)

        # Post-grad custom passes are run using the post_grad_custom_post_pass
        # hook. If a pass for that hook exists, add it to the pass manager.
        if self.pass_key in self.inductor_config:
            if isinstance(self.inductor_config[self.pass_key], PostGradPassManager):
                raise ValueError(
                    "PostGradPassManager can not be kept in CompilationConfig."
                )
            else:
                # Config should automatically wrap all inductor passes
                assert isinstance(
                    self.compilation_config.inductor_compile_config[self.pass_key],
                    InductorPass,
                )
                self.pass_manager.add(
                    self.compilation_config.inductor_compile_config[self.pass_key]
                )
        self.inductor_config[self.pass_key] = self.pass_manager

    def_log_compilation_config(self):
"""Log vLLM compilation config for TORCH_TRACE/tlparse."""
        cc = self.compilation_config
        pass_cfg = cc.pass_config

        # Helper to convert lists to comma-separated strings for tlparse display
        deflist_to_str(lst: list | None) -> str:
            if lst is None:
                return ""
            return ", ".join(str(x) for x in lst)

        # Get enabled passes by introspecting dataclass fields
        enabled_passes = [
            f.name
            for f in dataclasses.fields(pass_cfg)
            if isinstance(getattr(pass_cfg, f.name), bool) and getattr(pass_cfg, f.name)
        ]

        trace_structured(
            "artifact",
            metadata_fn=lambda: {
                "name": "vllm_compilation_config",
                "encoding": "json",
            },
            payload_fn=lambda: json.dumps(
                {
                    "model": self.vllm_config.model_config.model,
                    "prefix": self.prefix,
                    "mode": str(cc.mode),
                    "backend": cc.backend,
                    "custom_ops": list_to_str(cc.custom_ops),
                    "splitting_ops": list_to_str(cc.splitting_ops),
                    "cudagraph_mode": str(cc.cudagraph_mode),
                    "compile_sizes": list_to_str(cc.compile_sizes),
                    "compile_ranges_endpoints": list_to_str(
                        cc.compile_ranges_endpoints
                    ),
                    "use_inductor_graph_partition": cc.use_inductor_graph_partition,
                    "inductor_passes": list_to_str(list(cc.inductor_passes.keys())),
                    "enabled_passes": list_to_str(enabled_passes),
                    "dynamic_shapes_type": str(cc.dynamic_shapes_config.type),
                    "dynamic_shapes_evaluate_guards": cc.dynamic_shapes_config.evaluate_guards,  # noqa: E501
                }
            ),
        )

    @dynamo_timed("vllm_backend")
    def__call__(self, graph: fx.GraphModule, example_inputs: Sequence[Any]) -> Any:
        from.cachingimport (
            VllmSerializableFunction,
        )

        vllm_config = self.vllm_config

        self._log_compilation_config()

        # Minimal hashing here with existing utilities, reused below.

        env_factors = envs.compile_factors()
        env_hash = hash_factors(env_factors)
        # Compute config/compiler/code hashes once and reuse
        config_hash = vllm_config.compute_hash()
        compiler_hash = self.compiler_manager.compute_hash(vllm_config)
        forward_code_files = list(sorted(self.compilation_config.traced_files))

        logger.debug(
            "Traced files (to be considered for compilation cache):\n%s",
            lazy(lambda: "\n".join(forward_code_files)),
        )
        hash_content = []
        for filepath in forward_code_files:
            if filepath == "<string>":
                # This means the function was dynamically generated, with
                # e.g. exec(). We can't actually check these.
                continue
            hash_content.append(filepath)
            try:
                with open(filepath) as f:
                    hash_content.append(f.read())
            except (OSError, UnicodeDecodeError):
                logger.warning("Failed to read file %s", filepath)
                continue
        code_hash = hashlib.sha256("\n".join(hash_content).encode()).hexdigest()
        # Clear after consumption
        self.compilation_config.traced_files.clear()
        if not self.compilation_config.cache_dir:
            # no provided cache dir, generate one based on the known factors
            # that affects the compilation. if none of the factors change,
            # the cache dir will be the same so that we can reuse the compiled
            # graph.
            factors = [env_hash, config_hash, code_hash, compiler_hash]
            # Use SHA-256 for cache key hashing to be consistent across
            # compute_hash functions. Truncate for a short cache dir name.
            hash_key = hashlib.sha256(str(factors).encode()).hexdigest()[:10]
            cache_dir = os.path.join(
                envs.VLLM_CACHE_ROOT, "torch_compile_cache", hash_key
            )
            self.compilation_config.cache_dir = cache_dir

        cache_dir = self.compilation_config.cache_dir
        os.makedirs(cache_dir, exist_ok=True)
        self.compilation_config.cache_dir = cache_dir
        rank = vllm_config.parallel_config.rank
        dp_rank = vllm_config.parallel_config.data_parallel_index
        local_cache_dir = os.path.join(cache_dir, f"rank_{rank}_{dp_rank}", self.prefix)
        os.makedirs(local_cache_dir, exist_ok=True)
        self.compilation_config.local_cache_dir = local_cache_dir

        # Honors opt-outs such as CompilationMode.NONE or VLLM_DISABLE_COMPILE_CACHE.
        disable_cache = not is_compile_cache_enabled(self.inductor_config)

        # TODO(patchy): ngram gpu kernel will cause vllm torch compile cache errors.
        is_ngram_gpu_enabled = (
            vllm_config.speculative_config is not None
            and vllm_config.speculative_config.use_ngram_gpu()
        )
        disable_cache = disable_cache or is_ngram_gpu_enabled

        if disable_cache:
            logger.info_once("vLLM's torch.compile cache is disabled.")
        else:
            logger.info_once(
                "Using cache directory: %s for vLLM's torch.compile",
                local_cache_dir,
            )

        self.compiler_manager.initialize_cache(
            local_cache_dir, disable_cache, self.prefix
        )

        # Reuses existing cache key

        logger.debug(
            "torch.compile cache factors: env=%s cfg=%s comp=%s code=%s dir=%s",
            env_hash,
            config_hash,
            compiler_hash,
            code_hash,
            local_cache_dir,
        )

        # Persist and log only hash-relevant factors together.
        try:
            logger.debug(
                "Compile env factors (raw):\n%s\nVllm config hash: %s",
                lazy(partial(pprint.pformat, env_factors, width=120)),
                config_hash,
            )
            meta_path = os.path.join(local_cache_dir, "cache_key_factors.json")
            if not os.path.exists(meta_path):
                with open(meta_path, "w") as f:
                    json.dump(
                        {
                            "env": env_factors,  # raw factors used for env_hash
                            "config_hash": config_hash,
                            "code_hash": code_hash,
                            "compiler_hash": compiler_hash,
                        },
                        f,
                        indent=2,
                        sort_keys=True,
                    )
        except Exception:
            # Best-effort only; metadata write failures are non-fatal.
            logger.warning(
                (
                    "Could not write compile cache metadata at %s; continuing without "
                    "metadata. Compiled cache remains valid; diagnostics may be "
                    "limited."
                ),
                local_cache_dir,
                exc_info=True,
            )

        # when dynamo calls the backend, it means the bytecode
        # transform and analysis are done
        compilation_counter.num_graphs_seen += 1
        from.monitorimport torch_compile_start_time

        dynamo_time = time.perf_counter() - torch_compile_start_time
        logger.info_once(
            "Dynamo bytecode transform time: %.2f s",
            dynamo_time,
        )

        # Record Dynamo time in tracing if available
        start_time = int(torch_compile_start_time * 1e9)
        attributes = {"dynamo.time_seconds": dynamo_time}
        instrument_manual("Dynamo bytecode transform", start_time, None, attributes)

        # we control the compilation process, each instance can only be
        # called once
        assert not self._called, "VllmBackend can only be called once"

        self.graph = graph
        self.configure_post_pass()

        if self.compilation_config.use_inductor_graph_partition:
            # Let Inductor decide partitioning; avoid FX-level pre-splitting.
            fx_split_ops: list[str] = []
        else:
            fx_split_ops = self.compilation_config.splitting_ops or []

        self.split_gm, self.piecewise_graphs = split_graph(graph, fx_split_ops)

        # keep a split_gm copy from BEFORE the interpreter replaces
        # submodules with PiecewiseBackend -- used for serialization
        original_split_gm = None
        if envs.VLLM_USE_MEGA_AOT_ARTIFACT:
            original_split_gm = deepcopy(self.split_gm)

        fromtorch._dynamo.utilsimport lazy_format_graph_code

        # depyf will hook lazy_format_graph_code and dump the graph
        # for debugging, no need to print the graph here
        lazy_format_graph_code("before split", self.graph)
        lazy_format_graph_code("after split", self.split_gm)

        # Log the piecewise split graph for TORCH_TRACE/tlparse
        trace_structured(
            "graph_dump",
            metadata_fn=lambda: {"name": "vllm_piecewise_split_graph"},
            payload_fn=lambda: self.split_gm.print_readable(print_output=False),
        )

        compilation_counter.num_piecewise_graphs_seen += len(self.piecewise_graphs)
        submod_names_to_compile = [
            item.submod_name
            for item in self.piecewise_graphs
            if not item.is_splitting_graph
        ]

        # Extract fake values from the graph to use them when needed.
        all_fake_values = []
        for i in graph.graph.find_nodes(op="placeholder"):
            all_fake_values.append(i.meta["example_value"])

        fake_args = [
            all_fake_values[i] if isinstance(t, torch.Tensor) else t
            for i, t in enumerate(example_inputs)
        ]

        # propagate the split graph to the piecewise backend,
        # compile submodules with symbolic shapes, and compile all ranges
        # up front so that compilation is complete before the callable
        # is returned.
        PiecewiseCompileInterpreter(
            self.split_gm, submod_names_to_compile, self.vllm_config, self
        ).run(*fake_args)

        # All compilation is done. Save the cache.
        time_before_saving = time.perf_counter()
        self.compiler_manager.save_to_file()
        elapsed = time.perf_counter() - time_before_saving
        if elapsed > 1:
            logger.info_once(
                "Saved compiler manager cache in %.2f seconds.",
                elapsed,
            )

        fromtorch._guardsimport detect_fake_mode

        fake_mode = detect_fake_mode()

        if (
            self.compilation_config.dynamic_shapes_config.evaluate_guards
            and self.compilation_config.dynamic_shapes_config.type
            == DynamicShapesType.BACKED
        ):
            fromtorch.utils._sympy.value_rangesimport ValueRanges

            # Drop counter-0/1 specializations guards; for backed dynamic shapes,
            # torch.compile will specialize for 0/1 inputs or otherwise guards that
            # shape is >= 2. This is because it's really hard not to hit a check
            # against 0/1. When we evaluate shape guards, we exclude checking those
            # guards (We would fail always otherwise).

            # We avoid that by updating the ranges of backed sizes when the min is
            # 2 for any, we assume it's 0.
            for s, r in fake_mode.shape_env.var_to_range.items():
                if r.lower == 2:
                    fake_mode.shape_env.var_to_range[s] = ValueRanges(0, r.upper)

        graph_path = os.path.join(local_cache_dir, "computation_graph.py")
        if not os.path.exists(graph_path):
            # code adapted from
            # https://github.com/thuml/depyf/blob/dab831108a752d1facc00acdd6d4243891845c37/depyf/explain/patched_lazy_format_graph_code.py#L30
            # use `print_readable` because it can include submodules
            src = (
                "from __future__ import annotations\nimport torch\n"
                + self.split_gm.print_readable(print_output=False)
            )
            src = src.replace("<lambda>", "GraphModule")
            with open(graph_path, "w") as f:
                f.write(src)

            logger.debug_once("Computation graph saved to %s", graph_path)

        self._called = True
        graph_to_serialize = (
            original_split_gm if envs.VLLM_USE_MEGA_AOT_ARTIFACT else self.graph
        )

        execution_code, submod_names, consts = generate_execution_code(self.split_gm)
        # Use getattr to get correct callables: __dict__ has PiecewiseBackend
        # instances (from PiecewiseCompileInterpreter), _modules has originals.
        # getattr checks __dict__ first, then falls back to _modules.
        submod_callables = {
            name: getattr(self.split_gm, name)
            for name, _ in self.split_gm.named_children()
        }
        runtime_callable = compile_execution_fn(
            execution_code, submod_callables, submod_names, consts
        )

        if (
            self.compilation_config.cudagraph_mode == CUDAGraphMode.NONE
            or not self.compilation_config.cudagraph_copy_inputs
        ):
            return VllmSerializableFunction(
                graph_to_serialize,
                example_inputs,
                self.prefix,
                runtime_callable,
                is_encoder=self.is_encoder,
                vllm_backend=self,
                execution_code=execution_code,
                submod_names=submod_names,
                consts=consts,
            )

        # index of tensors that have symbolic shapes (batch size)
        # for weights and static buffers, they will have concrete shapes.
        # symbolic shape only happens for input tensors.
        fromtorch.fx.experimental.symbolic_shapesimport is_symbolic

        sym_tensor_indices = [
            i
            for i, x in enumerate(fake_args)
            if isinstance(x, torch._subclasses.fake_tensor.FakeTensor)
            and any(is_symbolic(d) for d in x.size())
        ]

        # compiler managed cudagraph input buffers
        # we assume the first run with symbolic shapes
        # has the maximum size among all the tensors
        copy_and_call = make_copy_and_call(
            sym_tensor_indices,
            [example_inputs[x].clone() for x in sym_tensor_indices],
            runtime_callable,
        )

        return VllmSerializableFunction(
            graph_to_serialize,
            example_inputs,
            self.prefix,
            copy_and_call,
            is_encoder=self.is_encoder,
            vllm_backend=self,
            sym_tensor_indices=sym_tensor_indices,
            execution_code=execution_code,
            submod_names=submod_names,
            consts=consts,
        )
```