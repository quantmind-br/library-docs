---
title: op - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/ir/op/
source: sitemap
fetched_at: 2026-05-07T21:22:01.843605906-03:00
rendered_js: false
word_count: 1
summary: This document defines a class structure for registering, dispatching, and managing custom operators within a PyTorch-based intermediate representation system.
tags:
    - custom-ops
    - pytorch-dispatcher
    - operator-registration
    - lowering
    - ir-design
    - dispatch-logic
category: concept
---

````
classIrOp:
    registry: ClassVar[dict[str, "IrOp"]] = {}

    name: str
    impls: dict[str, "IrOpImpl"]
    allow_inplace: bool = False

    def__init__(
        self,
        name: str,
        native_impl: Callable,
        activations: list[str] | None = None,
    ):
        self._py_signature = inspect.signature(native_impl)
        if any(
            p.kind == inspect.Parameter.KEYWORD_ONLY
            for p in self._py_signature.parameters.values()
        ):
            raise ValueError(
                f"Op {name} has keyword-only arguments which are not currently "
                f"supported. That's because kwargs are not allowed during lowering."
            )

        # By convention, we consider parameters starting with 'x' as activations.
        if activations is None:
            activations = [
                p.name
                for p in self._py_signature.parameters.values()
                if p.name.startswith("x")
            ]

        self.name = name
        self.impls: dict[str, IrOpImpl] = {}
        self.activations = activations
        self.activation_indices = [
            i
            for i, p in enumerate(self._py_signature.parameters.values())
            if p.name in activations
        ]
        self._priority_impls: list[IrOpImpl] = []
        self._schema_str = infer_schema(native_impl, mutates_args=[])
        self._input_generator: InputGenerator | None = None
        self._tolerance_overrides: ToleranceSpec = {}

        # native implementation
        self.impls["native"] = IrOpImpl(
            self,
            "native",
            native_impl,
            # always supported
            supported=True,
            supports_args=None,
        )

        # By default, fake routes directly to native,
        # can be overridden by register_fake
        self._fake_fn = native_impl

        # torch registration
        vllm_ir_lib.define(self.name + self._schema_str)
        # CompositeExplicitAutograd is not decomposed
        # by ATen IR normalization in AOTAutograd
        vllm_ir_lib.impl(
            self.name, self._inner_call, dispatch_key="CompositeExplicitAutograd"
        )
        vllm_ir_lib._register_fake(self.name, self._fake_call)
        assert hasattr(torch.ops.vllm_ir, name)
        self.torch_op: torch._ops.OpOverload = getattr(torch.ops.vllm_ir, name).default

    defregister_fake(self, fn: Callable) -> Callable:
"""
        Register a fake impl for the torch custom op. If this method is not called,
        the native implementation is used directly for the fake implementation.
        """
        self._fake_fn = fn
        return fn

    def_fake_call(self, *args, **kwargs) -> Any:
"""
        Call to the fake implementation of the op. We use indirection because we want
        users to be able to register fake later but also want it to fall back to native
        directly by default, instead of going through the dispatching mechanism.
        """
        return self._fake_fn(*args, **kwargs)

    defregister_impl(
        self,
        provider: str,
        *,
        supported: bool = True,
        supports_args: Callable[..., bool] | None = None,
        inplace: bool = False,
    ):
"""
        Register an implementation for this custom op.
        :param provider: The name of the provider, must be unique.
        :param supported: Static support check, use this to check platform support.
        :param supports_args: Dynamic arg support check, used for types and shapes.
        :param inplace: Does this op reuse activation input memory for outputs
        :return: A decorator that registers the implementation.

        The decorated function must have the same semantics and signature as
        the native implementation.

        The provider name must be unique and not one of the RESERVED_PROVIDERS.
        The supported and supports_args parameters should not be used to implement
        custom enablement logic based on global state (e.g. environment variables).
        Instead, supported param should only be used to check for platform support
        (e.g. whether a specific hardware or library is available).
        supports_args should be used to check whether the provided arguments are
        compatible with the implementation.
        For custom enablement logic, set op impl priority.

        Example:
        ```python
        @my_op.register_impl("my_provider", supported=torch.cuda.is_available())
        def my_provider_impl(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor: ...
        ```

        """
        assert provider not in RESERVED_PROVIDERS, (
            f"Provider name {provider} is reserved."
        )

        def_register_impl(f: Callable):
            impl = IrOpImpl(self, provider, f, supported, supports_args, inplace)
            self.impls[provider] = impl

            if self.get_priority():
                logger.warning(
                    "Warning: registering new impl %s for op %s while priority is set.",
                    provider,
                    self.name,
                )

            return impl

        return _register_impl

    def_inner_call(self, *args, **kwargs) -> Any:
"""
        Eager call to torch op lands here. When torch wrapping is disabled,
        __call__ routes straight here instead of going through torch op dispatching.
        """
        impl = self.dispatch(*args, **kwargs)

        # Default overload must be functional,
        # use func_impl_fn to correctly handle inplace impls.
        return impl.func_impl_fn(*args, **kwargs)

    defapply_arg_defaults(self, args) -> tuple:
"""
        Return args with default values applied.
        Defaults are taken from the native implementation signature.

        SHOULD NOT BE USED IN THE DISPATCH PATH (SLOW).
        Only for Inductor lowering.
        """
        bound_args = self._py_signature.bind(*args)
        bound_args.apply_defaults()
        return bound_args.args

    defdispatch(self, *args, **kwargs) -> "IrOpImpl":
"""
        Dispatch to the appropriate implementation based on current priority
        and argument support checks. Returns the selected IrOpImpl.

        THIS FUNCTION IS ON THE HOT PATH (OP DISPATCH), MUST BE FAST.
        """
        if not self._priority_impls:
            if not torch.compiler.is_compiling():
                # Logging not compatible with Dynamo tracing
                # (this code is exposed when torch wrapping is disabled)
                logger.warning_once(
                    "Priority not set for op %s, using native implementation.",
                    self.name,
                )
            return self.impls["native"]

        for impl in self._priority_impls:
            if not impl.supported:
                raise ValueError(
                    f"Implementation {impl.provider} for op {self.name} not supported. "
                    f"All implementations in priority list must be supported."
                )
            if impl.supports_args(*args, **kwargs):
                return impl

            if not torch.compiler.is_compiling():
                logger.debug(
                    "Skipping provider %s because it does not support "
                    "%s with args=%s kwargs=%s",
                    impl.provider,
                    self.name,
                    lazy(lambda: tensors_str_no_data(args)),
                    lazy(lambda: tensors_str_no_data(kwargs)),
                )

        raise RuntimeError(
            "Priority set incorrectly: the last implementation must "
            "support all args (can be native). This is likely an internal bug"
        )

    def__call__(self, *args, **kwargs) -> Any:
        if not _ENABLE_TORCH_WRAP:
            return self._inner_call(*args, **kwargs)

        return self.torch_op(*args, **kwargs)

    defget_priority(self) -> list[str]:
"""Get the current dispatch priority for implementations for this op."""
        return [p.provider for p in self._priority_impls]

    @contextlib.contextmanager
    defset_priority(self, priority: list[str]):
"""
        Context manager to set the dispatch priority for implementations for this op.
        """
        assert all(p in self.impls for p in priority), (
            "All providers in priority must be registered implementations."
        )

        deffilter_priority_impls(p_list: list[str]) -> list[IrOpImpl]:
            filtered_impls = []
            for p in p_list:
                impl = self.impls[p]
                if not impl.supported:
                    # Skip unsupported implementations
                    continue

                filtered_impls.append(impl)

                # If all args are supported, skip other implementations
                if impl.supports_all_args:
                    return filtered_impls

            logger.warning_once(
                "Op %s: No implementation in priority list supports all args, "
                "execution fallback to native is possible. To silence this warning, "
                "explicitly add 'native' to the end of the priority list",
                self.name,
            )
            filtered_impls.append(self.impls["native"])
            return filtered_impls

        # Temporarily set priority
        old_priority_impls = self._priority_impls
        try:
            self._priority_impls = filter_priority_impls(priority)
            logger.debug(
                "Priority for vllm.ir.%s set to %s",
                self.name,
                lazy(lambda: [p.provider for p in self._priority_impls]),
            )
            yield
        finally:
            self._priority_impls = old_priority_impls

    defsupported_providers(self) -> list[str]:
        return [p.provider for p in self.impls.values() if p.supported]

    @property
    defhas_input_generator(self) -> bool:
        return self._input_generator is not None

    defregister_input_generator(self, fn: InputGenerator) -> InputGenerator:
        self._input_generator = fn
        return fn

    defgenerate_inputs(self, **kwargs: Any) -> tuple[Any, ...]:
        if self._input_generator is None:
            raise RuntimeError(
                f"No input generator registered for op '{self.name}'. "
                f"Use @ir.ops.{self.name}.register_input_generator"
            )
        return self._input_generator(**kwargs)

    defoverride_tolerance(
        self, dtype: torch.dtype, *, atol: float, rtol: float
    ) -> None:
        self._tolerance_overrides[dtype] = {"atol": atol, "rtol": rtol}

    defget_tolerance(self, dtype: torch.dtype) -> dict[str, float]:
        if dtype in self._tolerance_overrides:
            return self._tolerance_overrides[dtype]
        if dtype in DEFAULT_TOLERANCES:
            return DEFAULT_TOLERANCES[dtype]
        raise ValueError(
            f"No tolerance defined for dtype {dtype} in op '{self.name}'. "
            f"Use op.override_tolerance({dtype}, atol=..., rtol=...) "
            f"or add {dtype} to DEFAULT_TOLERANCES."
        )
````