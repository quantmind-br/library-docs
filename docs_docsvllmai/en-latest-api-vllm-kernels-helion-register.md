---
title: register - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/kernels/helion/register/
source: sitemap
fetched_at: 2026-05-07T21:22:15.353683987-03:00
rendered_js: false
word_count: 0
summary: This document defines a Python class that wraps Helion kernels to manage configuration selection, autotuning, and registration within the PyTorch operator framework.
tags:
    - python-wrapper
    - kernel-autotuning
    - pytorch-operators
    - vllm-helion
    - code-optimization
category: api
---

```
classHelionKernelWrapper:
"""Wrapper for Helion kernels with pre-tuned config selection and HOP support."""

    def__init__(
        self,
        raw_kernel_func: Callable,
        op_name: str,
        fake_impl: Callable,
        config_picker: Callable[[tuple[Any, ...], list[str]], str | None],
        helion_settings: "helion.Settings | None" = None,
        input_generator: Callable[[], dict[str, tuple[Any, ...]]] | None = None,
    ):
        # Validate helion_settings doesn't conflict with our custom autotuner
        validate_helion_settings(helion_settings, op_name)

        self.raw_kernel_func = raw_kernel_func
        self.op_name = op_name
        self._fake_impl = fake_impl
        self.helion_settings = helion_settings
        self._config_picker = config_picker
        self._input_generator = input_generator
        self._configured_kernel: ConfiguredHelionKernel | None = None
        # TODO(@gmagogsfm): Remove this disable flag once integrated with vLLM IR,
        # which handles op enablement/disablement.
        self._disabled = False
        self._disabled_reason: str | None = None

        try:
            if not _HOP_AVAILABLE:
                self._get_or_register_custom_op()
            else:
                self.get_configured_op()
        except ValueError as e:
            self._disabled = True
            self._disabled_reason = str(e)
            logger.warning(
                "Helion kernel '%s' is disabled: %s",
                op_name,
                self._disabled_reason,
            )

    def__call__(self, *args, **kwargs):
        if self._disabled:
            raise RuntimeError(
                f"Helion kernel '{self.op_name}' is disabled: {self._disabled_reason}"
            )
        if not _HOP_AVAILABLE:
            op = getattr(torch.ops.vllm_helion, self.op_name)
            return op(*args, **kwargs)
        assert self._configured_kernel is not None, (
            f"Kernel '{self.op_name}' was not initialized. "
            "Please open an issue on GitHub."
        )

        # During Dynamo tracing, this call will be intercepted by our custom
        # HelionKernelWrapperVariable and handled via proper HOP emission.
        # During eager execution, call the kernel directly.
        return self._configured_kernel(*args, **kwargs)

    defget_inputs(self) -> dict[str, tuple[Any, ...]]:
        if self._input_generator is None:
            raise NotImplementedError(
                f"No input generator registered for kernel '{self.op_name}'. "
                f"Use register_kernel(..., input_generator=...) to register one."
            )
        return self._input_generator()

    defrun_autotune(
        self,
        inputs: tuple[Any, ...],
        autotune_effort: str = "quick",
    ) -> Config:
"""Run autotuning for a single input configuration."""
        extra_kwargs = {
            "autotune_effort": autotune_effort,
            "autotune_ignore_errors": True,
        }
        autotune_kernel = create_helion_decorated_kernel(
            self.raw_kernel_func, self.helion_settings, extra_kwargs
        )
        return autotune_kernel.autotune(inputs)

    defget_configured_op(self) -> ConfiguredHelionKernel:
        if self._disabled:
            raise RuntimeError(
                f"Helion kernel '{self.op_name}' is disabled: {self._disabled_reason}"
            )
        if self._configured_kernel is None:
            self._configured_kernel = ConfiguredHelionKernel(
                op_name=self.op_name,
                config_picker=self._config_picker,
                raw_kernel_func=self.raw_kernel_func,
                helion_settings=self.helion_settings,
            )
        return self._configured_kernel

    def_get_or_register_custom_op(self) -> Any:
        if hasattr(torch.ops.vllm_helion, self.op_name):
            return getattr(torch.ops.vllm_helion, self.op_name)

        configured_kernel = self.get_configured_op()

        logger.info("Registering op: vllm_helion::%s", self.op_name)
        direct_register_custom_op(
            op_name=self.op_name,
            op_func=configured_kernel._decorated_kernel,
            mutates_args=None,
            fake_impl=self._fake_impl,
            target_lib=vllm_helion_lib,
        )
        return getattr(torch.ops.vllm_helion, self.op_name)
```