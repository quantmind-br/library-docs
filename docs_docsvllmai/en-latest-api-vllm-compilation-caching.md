---
title: caching - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/compilation/caching/
source: sitemap
fetched_at: 2026-05-07T21:16:12.175956801-03:00
rendered_js: false
word_count: 0
summary: This class provides a serialization mechanism for vLLM compiled functions, enabling the saving and loading of Dynamo FX graphs and associated compilation artifacts.
tags:
    - vllm
    - serialization
    - pytorch
    - torch-fx
    - compilation
    - model-loading
category: api
---

```
classVllmSerializableFunction(SerializableCallable):  # type: ignore[misc]
"""
    A wrapper around a compiled function by vllm. It will forward the tensor
    inputs to the compiled function and return the result.
    It also implements a serialization interface to support PyTorch's precompile
    with custom backend, so that we can save and load the compiled function on
    disk. There's no need to wrap around the compiled function if we don't want
    to serialize them in particular cases.
    Right now serialization for the custom backend is done via
    serializing the Dynamo fx graph plus example inputs.
    """

    def__init__(
        self,
        graph_module: torch.fx.GraphModule | bytes,
        example_inputs: Sequence[Any],
        prefix: str,
        optimized_call: Callable[..., Any],
        is_encoder: bool = False,
        vllm_backend: Any | None = None,
        sym_tensor_indices: list[int] | None = None,
        aot_autograd_config: dict[str, Any] | None = None,
        execution_code: str | None = None,
        submod_names: list[str] | None = None,
        consts: list[Any] | None = None,
    ) -> None:
        self.graph_module = graph_module
        self.example_inputs = example_inputs
        self.prefix = prefix
        self.optimized_call = optimized_call
        self.is_encoder = is_encoder
        self.shape_env = None
        self.vllm_backend = vllm_backend
        self.sym_tensor_indices = sym_tensor_indices
        self.execution_code = execution_code
        self.submod_names = submod_names
        self.consts = consts
        self._fake_mode: Any | None = None

        importtorch._functorch.configasfunctorch_config

        self.aot_autograd_config = (
            aot_autograd_config or functorch_config.save_config_portable()
        )
        sym_input = next(
            (i for i in self.example_inputs if isinstance(i, torch.SymInt)), None
        )
        if sym_input is not None:
            self.shape_env = sym_input.node.shape_env

    def__call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.optimized_call(*args, **kwargs)

    @classmethod
    defserialize_graph_module(cls, graph_module: torch.fx.GraphModule) -> bytes:
        importsympy

        graph_reducer_override = GraphPickler.reducer_override

        def_graph_reducer_override(
            self: GraphPickler, obj: Any
        ) -> tuple[Callable[..., Any], tuple[Any, ...]] | Any:
            if (
                inspect.isclass(obj)
                and issubclass(obj, sympy.Function)
                and hasattr(obj, "_torch_unpickler")
            ):
                return obj._torch_unpickler, (obj._torch_handler_name,)
            if isinstance(obj, FakeTensorMode):
                return type(None), ()
            return graph_reducer_override(self, obj)

        with (
            patch.object(GraphPickler, "reducer_override", _graph_reducer_override),
            patch_pytree_map_over_slice(),
        ):
            return GraphPickler.dumps(graph_module, Options(ops_filter=None))

    @classmethod
    defdeserialize_graph_module(
        cls, data: bytes, fake_mode: FakeTensorMode
    ) -> torch.fx.GraphModule:
        with patch_pytree_map_over_slice():
            return GraphPickler.loads(data, fake_mode)

    @classmethod
    defserialize_compile_artifacts(
        cls, compiled_fn: "VllmSerializableFunction"
    ) -> bytes:
        state = compiled_fn.__dict__.copy()
        state.pop("optimized_call")
        state.pop("shape_env")
        state.pop("vllm_backend", None)
        state.pop("_fake_mode", None)
        for node in state["graph_module"].graph.nodes:
            node.meta.pop("source_fn_stack", None)
            node.meta.pop("nn_module_stack", None)
        for name, submod in state["graph_module"].named_children():
            if hasattr(submod, "graph"):
                for node in submod.graph.nodes:
                    node.meta.pop("source_fn_stack", None)
                    node.meta.pop("nn_module_stack", None)

        if state.get("sym_tensor_indices"):
            # put tensor inputs on meta device since their data
            # isn't needed, yet we need the meta for make_copy_and_call
            state["example_inputs"] = pytree.tree_map_only(
                torch.Tensor,
                lambda inp: torch.empty_like(inp, device="meta"),
                state["example_inputs"],
            )
        else:
            # mask off all tensor inputs since they are large and not needed.
            state["example_inputs"] = pytree.tree_map_only(
                torch.Tensor,
                lambda inp: torch.empty_like(inp, device="meta"),
                state["example_inputs"],
            )

        state["graph_module"] = cls.serialize_graph_module(state["graph_module"])
        state["example_inputs"] = GraphPickler.dumps(state["example_inputs"])

        if compiled_fn.vllm_backend:
            (
                standalone_compile_artifacts,
                sym_shape_indices_map,
                returns_tuple_map,
            ) = compiled_fn.vllm_backend.collect_standalone_compile_artifacts()
            state["standalone_compile_artifacts"] = standalone_compile_artifacts
            state["sym_shape_indices_map"] = sym_shape_indices_map
            state["returns_tuple_map"] = returns_tuple_map
        return pickle.dumps(state)

    @classmethod
    defdeserialize_compile_artifacts(cls, data: bytes) -> "VllmSerializableFunction":
        fromtorch._guardsimport TracingContext, tracing
        fromtorch.fx.experimental.symbolic_shapesimport ShapeEnv

        state = pickle.loads(data)
        fake_mode = FakeTensorMode(shape_env=ShapeEnv())

        state["example_inputs"] = GraphPickler.loads(state["example_inputs"], fake_mode)

        standalone_compile_artifacts = state.pop("standalone_compile_artifacts", None)
        sym_shape_indices_map = state.pop("sym_shape_indices_map", {})
        returns_tuple_map = state.pop("returns_tuple_map", {})

        saved_aot_autograd_config = state["aot_autograd_config"]
        if saved_aot_autograd_config is not None:
            functorch_ctx = torch._functorch.config.patch(saved_aot_autograd_config)
        else:
            functorch_ctx = contextlib.nullcontext()

        if envs.VLLM_USE_MEGA_AOT_ARTIFACT:
            assert standalone_compile_artifacts is not None
            submod_names = standalone_compile_artifacts.submodule_names()
            num_submods = len(submod_names)
            num_artifacts = standalone_compile_artifacts.num_artifacts()

            with functorch_ctx:
                fn = reconstruct_serializable_fn_from_mega_artifact(
                    state=state,
                    standalone_compile_artifacts=standalone_compile_artifacts,
                    vllm_config=get_current_vllm_config(),
                    sym_shape_indices_map=sym_shape_indices_map,
                    returns_tuple_map=returns_tuple_map,
                    fake_mode=fake_mode,
                )

            logger.info(
                "reconstructed serializable fn from standalone compile "
                "artifacts. num_artifacts=%d num_submods=%d",
                num_artifacts,
                num_submods,
            )

            return fn

        state["graph_module"] = cls.deserialize_graph_module(
            state["graph_module"], fake_mode
        )
        state["graph_module"].recompile()

        # Fall back to standard VllmBackend.
        # Use a lazy closure: the backend needs traced_files for cache
        # dir computation, but those are only populated after
        # _verify_source_unchanged runs in decorators.py (which happens
        # after deserialization completes).
        fromvllm.compilation.backendsimport VllmBackend

        is_encoder = state.get("is_encoder", False)
        vllm_config = get_current_vllm_config()
        compile_inputs = list(state["example_inputs"])

        defoptimized_call(*example_inputs: Any) -> Any:
            vllm_backend: VllmBackend = VllmBackend(
                vllm_config, state["prefix"], is_encoder
            )
            with tracing(TracingContext(fake_mode)), functorch_ctx:
                fn.optimized_call = vllm_backend(
                    state["graph_module"], compile_inputs
                ).optimized_call
                fn.vllm_backend = vllm_backend
            return fn.optimized_call(*example_inputs)

        fn = cls(**state, optimized_call=optimized_call)
        fn._fake_mode = fake_mode
        return fn

    deffinalize_loading(self, vllm_config: VllmConfig) -> None:
"""Eagerly initialize the compiled backend and perform all loading.

        Must be called after _verify_source_unchanged has populated
        compilation_config.traced_files, which is needed for cache dir
        computation.
        """
        if self._fake_mode is None:
            return  # Already finalized, or mega path (no _fake_mode set)

        fromtorch._guardsimport TracingContext, tracing

        fromvllm.compilation.backendsimport VllmBackend

        saved_aot_autograd_config = self.aot_autograd_config
        if saved_aot_autograd_config is not None:
            functorch_ctx = torch._functorch.config.patch(saved_aot_autograd_config)
        else:
            functorch_ctx = contextlib.nullcontext()

        vllm_backend = VllmBackend(vllm_config, self.prefix, self.is_encoder)
        with tracing(TracingContext(self._fake_mode)), functorch_ctx:
            result = vllm_backend(self.graph_module, list(self.example_inputs))
            self.optimized_call = result.optimized_call
            self.vllm_backend = vllm_backend

        self._fake_mode = None

    @property
    defco_name(self) -> Literal["VllmSerializableFunction"]:
"""
        Used for depyf debugging.
        """
        return "VllmSerializableFunction"
```