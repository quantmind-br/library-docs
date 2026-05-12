---
title: kernel - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/config/kernel/
source: sitemap
fetched_at: 2026-05-07T21:16:57.252914456-03:00
rendered_js: false
word_count: 470
summary: The IrOpPriorityConfig class manages the dispatching and lowering priority of vLLM IR operations during the forward pass, providing mechanisms for kernel configuration and execution cache management.
tags:
    - vllm
    - ir-operations
    - kernel-configuration
    - dispatch-priority
    - compilation-cache
    - python-config
category: reference
---

## IrOpPriorityConfig [¶](#vllm.config.kernel.IrOpPriorityConfig "Permanent link")

Configuration for vLLM IR op priority for dispatching/lowering during the forward pass. Each member is a list of strings, which will be passed to vllm.ir.ops..set\_priority() for the duration of the forward pass. A single comma-separated string is accepted as well,

If specified manually, platform defaults will be appended to the lists. See KernelConfig.set\_platform\_defaults().

Source code in `vllm/config/kernel.py`

```
@config
classIrOpPriorityConfig:
"""
    Configuration for vLLM IR op priority for dispatching/lowering during the
    forward pass. Each member is a list of strings, which will be passed to
    vllm.ir.ops.<op_name>.set_priority() for the duration of the forward pass.
    A single comma-separated string is accepted as well,

    If specified manually, platform defaults will be appended to the lists.
    See KernelConfig.set_platform_defaults().
    """

    rms_norm: list[str] = Field(default_factory=list)
"""Priority list for vllm.ir.ops.rms_norm"""

    fused_add_rms_norm: list[str] = Field(default_factory=list)
"""Priority list for vllm.ir.ops.fused_add_rms_norm"""

    defcompute_hash(self) -> str:
"""
        Produces a hash unique to the pass configuration.
        Any new fields that affect compilation should be added to the hash.
        Any future fields that don't affect compilation should be excluded.

        Also, manually add IR op impl UUIDs to make sure they affect the compile cache.
        """
        factors = get_hash_factors(self, set())

        # Implementations are hidden from Dynamo,
        # so they don't show up in the traced files list.
        fromvllm.ir.opimport IrOp

        assert "_impls" not in factors
        factors["_impls"] = {
            name: {
                provider: IrOp.registry[name].impls[provider].uuid() for provider in p
            }
            for name, p in asdict(self).items()  # type: ignore[call-overload]
        }

        return hash_factors(factors)

    @field_validator("*", mode="before")
    @classmethod
    def_to_list_str(cls, value: str | list[str]):
        if isinstance(value, str):
            value = value.replace(" ", "").split(",")

        assert all(isinstance(v, str) for v in value)
        return value

    @contextlib.contextmanager
    defset_priority(self):
"""
        Context manager to set the IR op priority for all op members.
        It also imports IR kernel implementations for the current platform
        to ensure all implementations are made available.
        """
        fromvllm.ir.opimport IrOp
        fromvllm.platformsimport current_platform

        current_platform.import_ir_kernels()

        with contextlib.ExitStack() as stack:
            for field in fields(self):  # type: ignore[arg-type]
                op_priority = getattr(self, field.name)
                assert op_priority is not None, (
                    f"IR op priority for {field.name} must be set"
                )
                logger.debug(
                    "Setting IR op priority for %s to %s", field.name, op_priority
                )
                ir_op = IrOp.registry[field.name]
                stack.enter_context(ir_op.set_priority(op_priority))

            yield

    @classmethod
    defwith_default(
        cls, default: list[str], /, **kwargs: list[str]
    ) -> "IrOpPriorityConfig":
"""
        A helper to create an IrOpPriorityConfig where fields not specified in kwargs
        use the given default list.
        """
        for field in fields(cls):  # type: ignore[arg-type]
            if field.name not in kwargs:
                kwargs[field.name] = list(default)

        return cls(**kwargs)
```

### fused\_add\_rms\_norm `class-attribute` `instance-attribute` [¶](#vllm.config.kernel.IrOpPriorityConfig.fused_add_rms_norm "Permanent link")

```
fused_add_rms_norm: list[str] = Field(default_factory=list)
```

Priority list for vllm.ir.ops.fused\_add\_rms\_norm

### rms\_norm `class-attribute` `instance-attribute` [¶](#vllm.config.kernel.IrOpPriorityConfig.rms_norm "Permanent link")

Priority list for vllm.ir.ops.rms\_norm

### compute\_hash [¶](#vllm.config.kernel.IrOpPriorityConfig.compute_hash "Permanent link")

Produces a hash unique to the pass configuration. Any new fields that affect compilation should be added to the hash. Any future fields that don't affect compilation should be excluded.

Also, manually add IR op impl UUIDs to make sure they affect the compile cache.

Source code in `vllm/config/kernel.py`

```
defcompute_hash(self) -> str:
"""
    Produces a hash unique to the pass configuration.
    Any new fields that affect compilation should be added to the hash.
    Any future fields that don't affect compilation should be excluded.

    Also, manually add IR op impl UUIDs to make sure they affect the compile cache.
    """
    factors = get_hash_factors(self, set())

    # Implementations are hidden from Dynamo,
    # so they don't show up in the traced files list.
    fromvllm.ir.opimport IrOp

    assert "_impls" not in factors
    factors["_impls"] = {
        name: {
            provider: IrOp.registry[name].impls[provider].uuid() for provider in p
        }
        for name, p in asdict(self).items()  # type: ignore[call-overload]
    }

    return hash_factors(factors)
```

### set\_priority [¶](#vllm.config.kernel.IrOpPriorityConfig.set_priority "Permanent link")

Context manager to set the IR op priority for all op members. It also imports IR kernel implementations for the current platform to ensure all implementations are made available.

Source code in `vllm/config/kernel.py`

```
@contextlib.contextmanager
defset_priority(self):
"""
    Context manager to set the IR op priority for all op members.
    It also imports IR kernel implementations for the current platform
    to ensure all implementations are made available.
    """
    fromvllm.ir.opimport IrOp
    fromvllm.platformsimport current_platform

    current_platform.import_ir_kernels()

    with contextlib.ExitStack() as stack:
        for field in fields(self):  # type: ignore[arg-type]
            op_priority = getattr(self, field.name)
            assert op_priority is not None, (
                f"IR op priority for {field.name} must be set"
            )
            logger.debug(
                "Setting IR op priority for %s to %s", field.name, op_priority
            )
            ir_op = IrOp.registry[field.name]
            stack.enter_context(ir_op.set_priority(op_priority))

        yield
```

### with\_default `classmethod` [¶](#vllm.config.kernel.IrOpPriorityConfig.with_default "Permanent link")

A helper to create an IrOpPriorityConfig where fields not specified in kwargs use the given default list.

Source code in `vllm/config/kernel.py`

```
@classmethod
defwith_default(
    cls, default: list[str], /, **kwargs: list[str]
) -> "IrOpPriorityConfig":
"""
    A helper to create an IrOpPriorityConfig where fields not specified in kwargs
    use the given default list.
    """
    for field in fields(cls):  # type: ignore[arg-type]
        if field.name not in kwargs:
            kwargs[field.name] = list(default)

    return cls(**kwargs)
```

## KernelConfig [¶](#vllm.config.kernel.KernelConfig "Permanent link")

Configuration for kernel selection and warmup behavior.

Source code in `vllm/config/kernel.py`

```
@config
classKernelConfig:
"""Configuration for kernel selection and warmup behavior."""

    ir_op_priority: IrOpPriorityConfig = Field(default_factory=IrOpPriorityConfig)
"""
    vLLM IR op priority for dispatching/lowering during the forward pass.
    Platform defaults appended automatically during VllmConfig.__post_init__.
    """

    enable_flashinfer_autotune: bool = None  # type: ignore[assignment]
"""If True, run FlashInfer autotuning during kernel warmup."""

    moe_backend: MoEBackend = "auto"
"""Backend for MoE expert computation kernels. Available options:

    - "auto": Automatically select the best backend based on model and hardware
    - "triton": Use Triton-based fused MoE kernels
    - "deep_gemm": Use DeepGEMM kernels (FP8 block-quantized only)
    - "deep_gemm_mega_moe": Use DeepGEMM mega MoE kernels
    - "cutlass": Use vLLM CUTLASS kernels
    - "flashinfer_trtllm": Use FlashInfer with TRTLLM-GEN kernels
    - "flashinfer_cutlass": Use FlashInfer with CUTLASS kernels
    - "flashinfer_cutedsl": Use FlashInfer with CuteDSL kernels (FP4 only)
    - "marlin": Use Marlin kernels (weight-only quantization)
    - "humming": Use Humming Mixed Precision kernels
    - "triton_unfused": Use Triton unfused MoE kernels
    - "aiter": Use AMD AITer kernels (ROCm only)
    - "emulation": use BF16/FP16 GEMM, dequantizing weights and
                   running QDQ on activations.
    """

    @field_validator("moe_backend", mode="before")
    @classmethod
    def_normalize_moe_backend(cls, value: Any) -> Any:
        if isinstance(value, str):
            return value.lower().replace("-", "_")
        return value

    defcompute_hash(self) -> str:
"""
        Produces a hash unique to the pass configuration.
        Any new fields that affect compilation should be added to the hash.
        Any future fields that don't affect compilation should be excluded.
        """
        ignored_factors = {
            "enable_flashinfer_autotune",
            "ir_op_priority",  # handled separately below
        }
        factors = get_hash_factors(self, ignored_factors)
        factors["ir_op_priority"] = self.ir_op_priority.compute_hash()
        return hash_factors(factors)

    @field_validator("enable_flashinfer_autotune", mode="wrap")
    @classmethod
    def_skip_none_validation(cls, value: Any, handler: Callable) -> Any:
"""Skip validation if the value is `None` when initialization is delayed."""
        if value is None:
            return value
        return handler(value)

    defset_platform_defaults(self, vllm_config: "VllmConfig") -> None:
"""Set platform-specific defaults for the kernel config."""
        fromvllm.platformsimport current_platform

        platform_op_priority = current_platform.get_default_ir_op_priority(vllm_config)
        logger.debug(
            "Setting platform-specific IR op priority defaults: %s, user-defined: %s",
            platform_op_priority,
            self.ir_op_priority,
        )
        for op_name, op_priority in asdict(platform_op_priority).items():
            current_op_priority: list[str] = getattr(self.ir_op_priority, op_name)
            if current_op_priority is None:
                setattr(self.ir_op_priority, op_name, op_priority)
            else:
                # Append platform-specific priorities
                # Must be idempotent because vllm_config.set_platform_defaults() may be
                # called multiple times (due to VllmConfig.__post_init__ manual call).
                unique_op_priority = [
                    op for op in op_priority if op not in current_op_priority
                ]
                current_op_priority.extend(unique_op_priority)

        logger.info(
            "Final IR op priority after setting platform defaults: %s",
            self.ir_op_priority,
        )
```

### enable\_flashinfer\_autotune `class-attribute` `instance-attribute` [¶](#vllm.config.kernel.KernelConfig.enable_flashinfer_autotune "Permanent link")

```
enable_flashinfer_autotune: bool = None
```

If True, run FlashInfer autotuning during kernel warmup.

### ir\_op\_priority `class-attribute` `instance-attribute` [¶](#vllm.config.kernel.KernelConfig.ir_op_priority "Permanent link")

```
ir_op_priority: IrOpPriorityConfig = Field(
    default_factory=IrOpPriorityConfig
)
```

vLLM IR op priority for dispatching/lowering during the forward pass. Platform defaults appended automatically during VllmConfig.**post\_init**.

### moe\_backend `class-attribute` `instance-attribute` [¶](#vllm.config.kernel.KernelConfig.moe_backend "Permanent link")

```
moe_backend: MoEBackend = 'auto'
```

Backend for MoE expert computation kernels. Available options:

- "auto": Automatically select the best backend based on model and hardware
- "triton": Use Triton-based fused MoE kernels
- "deep\_gemm": Use DeepGEMM kernels (FP8 block-quantized only)
- "deep\_gemm\_mega\_moe": Use DeepGEMM mega MoE kernels
- "cutlass": Use vLLM CUTLASS kernels
- "flashinfer\_trtllm": Use FlashInfer with TRTLLM-GEN kernels
- "flashinfer\_cutlass": Use FlashInfer with CUTLASS kernels
- "flashinfer\_cutedsl": Use FlashInfer with CuteDSL kernels (FP4 only)
- "marlin": Use Marlin kernels (weight-only quantization)
- "humming": Use Humming Mixed Precision kernels
- "triton\_unfused": Use Triton unfused MoE kernels
- "aiter": Use AMD AITer kernels (ROCm only)
- "emulation": use BF16/FP16 GEMM, dequantizing weights and running QDQ on activations.

### \_skip\_none\_validation `classmethod` [¶](#vllm.config.kernel.KernelConfig._skip_none_validation "Permanent link")

Skip validation if the value is `None` when initialization is delayed.

Source code in `vllm/config/kernel.py`

```
@field_validator("enable_flashinfer_autotune", mode="wrap")
@classmethod
def_skip_none_validation(cls, value: Any, handler: Callable) -> Any:
"""Skip validation if the value is `None` when initialization is delayed."""
    if value is None:
        return value
    return handler(value)
```

### compute\_hash [¶](#vllm.config.kernel.KernelConfig.compute_hash "Permanent link")

Produces a hash unique to the pass configuration. Any new fields that affect compilation should be added to the hash. Any future fields that don't affect compilation should be excluded.

Source code in `vllm/config/kernel.py`

```
defcompute_hash(self) -> str:
"""
    Produces a hash unique to the pass configuration.
    Any new fields that affect compilation should be added to the hash.
    Any future fields that don't affect compilation should be excluded.
    """
    ignored_factors = {
        "enable_flashinfer_autotune",
        "ir_op_priority",  # handled separately below
    }
    factors = get_hash_factors(self, ignored_factors)
    factors["ir_op_priority"] = self.ir_op_priority.compute_hash()
    return hash_factors(factors)
```

### set\_platform\_defaults [¶](#vllm.config.kernel.KernelConfig.set_platform_defaults "Permanent link")

```
set_platform_defaults(vllm_config: VllmConfig) -> None
```

Set platform-specific defaults for the kernel config.

Source code in `vllm/config/kernel.py`

```
defset_platform_defaults(self, vllm_config: "VllmConfig") -> None:
"""Set platform-specific defaults for the kernel config."""
    fromvllm.platformsimport current_platform

    platform_op_priority = current_platform.get_default_ir_op_priority(vllm_config)
    logger.debug(
        "Setting platform-specific IR op priority defaults: %s, user-defined: %s",
        platform_op_priority,
        self.ir_op_priority,
    )
    for op_name, op_priority in asdict(platform_op_priority).items():
        current_op_priority: list[str] = getattr(self.ir_op_priority, op_name)
        if current_op_priority is None:
            setattr(self.ir_op_priority, op_name, op_priority)
        else:
            # Append platform-specific priorities
            # Must be idempotent because vllm_config.set_platform_defaults() may be
            # called multiple times (due to VllmConfig.__post_init__ manual call).
            unique_op_priority = [
                op for op in op_priority if op not in current_op_priority
            ]
            current_op_priority.extend(unique_op_priority)

    logger.info(
        "Final IR op priority after setting platform defaults: %s",
        self.ir_op_priority,
    )
```