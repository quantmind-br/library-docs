---
title: mxfp8 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/oracle/mxfp8/
source: sitemap
fetched_at: 2026-05-07T21:25:10.901979178-03:00
rendered_js: false
word_count: 44
summary: This document provides API documentation for selecting appropriate backends and expert classes for MXFP8 Mixture-of-Experts (MoE) configurations within vLLM.
tags:
    - vllm
    - mxfp8
    - moe
    - backend-selection
    - machine-learning-infrastructure
category: api
---

## vllm.model\_executor.layers.fused\_moe.oracle.mxfp8 [¶](#vllm.model_executor.layers.fused_moe.oracle.mxfp8 "Permanent link")

## \_select\_kernel\_cls [¶](#vllm.model_executor.layers.fused_moe.oracle.mxfp8._select_kernel_cls "Permanent link")

Select the first supported expert class for the MXFP8 config.

Source code in `vllm/model_executor/layers/fused_moe/oracle/mxfp8.py`

```
def_select_kernel_cls(
    backend: Fp8MoeBackend,
    config: FusedMoEConfig,
) -> type[mk.FusedMoEExperts]:
"""Select the first supported expert class for the MXFP8 config."""
    activation_format = (
        mk.FusedMoEActivationFormat.BatchedExperts
        if config.moe_parallel_config.use_batched_activation_format
        else mk.FusedMoEActivationFormat.Standard
    )
    last_reason: str | None = None
    for cls in backend_to_kernel_cls(backend):
        supported, reason = cls.is_supported_config(
            cls,
            config,
            kMxfp8Static,
            kMxfp8Dynamic,
            activation_format,
        )
        if supported:
            return cls
        last_reason = reason
    raise ValueError(
        f"No supported MXFP8 expert class for {backend.value}: {last_reason}"
    )
```

## select\_mxfp8\_moe\_backend [¶](#vllm.model_executor.layers.fused_moe.oracle.mxfp8.select_mxfp8_moe_backend "Permanent link")

Select the MXFP8 MoE backend and the best expert class.

Returns:

Type Description `tuple[Fp8MoeBackend, type[FusedMoEExperts]]`

A tuple of (fp8\_backend, experts\_cls).

Source code in `vllm/model_executor/layers/fused_moe/oracle/mxfp8.py`

```
defselect_mxfp8_moe_backend(
    config: FusedMoEConfig,
) -> tuple[Fp8MoeBackend, type[mk.FusedMoEExperts]]:
"""Select the MXFP8 MoE backend and the best expert class.

    Returns:
        A tuple of (fp8_backend, experts_cls).
    """
    if config.is_lora_enabled:
        raise NotImplementedError("LoRA is not supported for MXFP8 MoE.")

    runner_backend = config.moe_backend
    if runner_backend != "auto":
        backend = _BACKEND_NAME_MAP.get(runner_backend)
        if backend is None:
            raise ValueError(
                f"moe_backend='{runner_backend}' is not supported for "
                f"MXFP8 MoE. Expected one of "
                f"{list(_BACKEND_NAME_MAP.keys())}."
            )
        logger.info_once(
            "Using '%s' MxFp8 MoE backend (user-requested).",
            backend.value,
        )
        return backend, _select_kernel_cls(backend, config)

    # Auto-select: pick the first supported backend.
    for backend in _SUPPORTED_BACKENDS:
        try:
            experts_cls = _select_kernel_cls(backend, config)
        except ValueError:
            continue
        logger.info_once("Using '%s' MxFp8 MoE backend.", backend.value)
        return backend, experts_cls

    raise ValueError("No MXFP8 MoE backends available.")
```