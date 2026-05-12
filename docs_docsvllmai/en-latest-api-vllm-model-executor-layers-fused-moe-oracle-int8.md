---
title: int8 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/oracle/int8/
source: sitemap
fetched_at: 2026-05-07T21:25:07.964574981-03:00
rendered_js: false
word_count: 48
summary: This document provides the API documentation for selecting and mapping Int8 mixture-of-experts (MoE) backends based on hardware configurations and deployment settings.
tags:
    - int8
    - moe
    - backend-selection
    - vllm
    - model-executor
    - kernel-mapping
category: api
---

## \_get\_priority\_backends [¶](#vllm.model_executor.layers.fused_moe.oracle.int8._get_priority_backends "Permanent link")

```
_get_priority_backends(
    moe_config: FusedMoEConfig,
) -> list[Int8MoeBackend]
```

Get available backends in priority order based on platform and config.

Source code in `vllm/model_executor/layers/fused_moe/oracle/int8.py`

```
def_get_priority_backends(
    moe_config: FusedMoEConfig,
) -> list[Int8MoeBackend]:
"""
    Get available backends in priority order based on platform and config.
    """
    return [Int8MoeBackend.TRITON]
```

## map\_int8\_backend [¶](#vllm.model_executor.layers.fused_moe.oracle.int8.map_int8_backend "Permanent link")

```
map_int8_backend(
    runner_backend: MoEBackend,
) -> Int8MoeBackend
```

Map user's MoEBackend to Int8MoeBackend.

Source code in `vllm/model_executor/layers/fused_moe/oracle/int8.py`

```
defmap_int8_backend(runner_backend: MoEBackend) -> Int8MoeBackend:
"""Map user's MoEBackend to Int8MoeBackend."""
    mapping = {
        "triton": Int8MoeBackend.TRITON,
    }
    if backend := mapping.get(runner_backend):
        return backend
    raise ValueError(
        f"moe_backend='{runner_backend}' is not supported for Int8 MoE. "
        f"Expected one of {list(mapping.keys())}."
    )
```

## select\_int8\_moe\_backend [¶](#vllm.model_executor.layers.fused_moe.oracle.int8.select_int8_moe_backend "Permanent link")

```
select_int8_moe_backend(
    config: FusedMoEConfig,
    weight_key: QuantKey | None = kInt8StaticChannelSym,
    activation_key: QuantKey | None = kInt8DynamicTokenSym,
) -> tuple[Int8MoeBackend, type[FusedMoEExperts]]
```

Select the primary Int8 MoE backend. Note: Shape-specific fallbacks may still occur at runtime.

Source code in `vllm/model_executor/layers/fused_moe/oracle/int8.py`

```
defselect_int8_moe_backend(
    config: FusedMoEConfig,
    weight_key: QuantKey | None = kInt8StaticChannelSym,
    activation_key: QuantKey | None = kInt8DynamicTokenSym,
) -> tuple[Int8MoeBackend, type[mk.FusedMoEExperts]]:
"""
    Select the primary Int8 MoE backend.
    Note: Shape-specific fallbacks may still occur at runtime.
    """

    if config.is_lora_enabled:
        return Int8MoeBackend.TRITON, backend_to_kernel_cls(Int8MoeBackend.TRITON)[0]

    AVAILABLE_BACKENDS = _get_priority_backends(config)

    activation_format = (
        mk.FusedMoEActivationFormat.BatchedExperts
        if config.moe_parallel_config.use_batched_activation_format
        else mk.FusedMoEActivationFormat.Standard
    )

    def_make_log_backend(backend: Int8MoeBackend) -> str:
        available_backend_strs = [b.value for b in AVAILABLE_BACKENDS]
        return (
            f"Using {backend.value} Int8 MoE backend out "
            f"of potential backends: {available_backend_strs}."
        )

    def_make_log_unsupported(backend: Int8MoeBackend, reason: str | None) -> str:
        if reason:
            return (
                f"Int8 MoE backend {backend.value} does not support the "
                f"deployment configuration since {reason}."
            )
        else:
            return (
                f"Int8 MoE backend '{backend.value}' does not support the "
                "deployment configuration."
            )

    def_return_or_raise(
        backend: Int8MoeBackend,
    ) -> tuple[Int8MoeBackend, type[mk.FusedMoEExperts]]:
        for k_cls in backend_to_kernel_cls(backend):
            supported, reason = k_cls.is_supported_config(
                k_cls, config, weight_key, activation_key, activation_format
            )
            if supported:
                logger.info_once(_make_log_backend(backend))
                return backend, k_cls
        raise ValueError(_make_log_unsupported(backend, reason))

    # Handle explicit moe_backend from user.
    runner_backend = config.moe_backend
    if runner_backend != "auto":
        requested_backend = map_int8_backend(runner_backend)
        return _return_or_raise(requested_backend)

    # Select kernels in order of backend.
    for backend in AVAILABLE_BACKENDS:
        for k_cls in backend_to_kernel_cls(backend):
            supported, reason = k_cls.is_supported_config(
                k_cls,
                config,
                weight_key,
                activation_key,
                activation_format,
            )
            if supported:
                logger.info_once(_make_log_backend(backend))
                return backend, k_cls
            else:
                logger.debug_once(_make_log_unsupported(backend, reason))

    raise NotImplementedError(
        "No Int8 MoE backend supports the deployment configuration."
    )
```