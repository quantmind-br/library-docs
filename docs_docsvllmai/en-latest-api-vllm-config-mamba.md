---
title: mamba - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/config/mamba/
source: sitemap
fetched_at: 2026-05-07T21:17:01.846759169-03:00
rendered_js: false
word_count: 189
summary: This document defines the configuration schema and backend enumeration for Mamba state space model integration within the vLLM framework.
tags:
    - mamba
    - ssm
    - vllm-config
    - stochastic-rounding
    - backend-selection
category: reference
---

## MambaBackendEnum [¶](#vllm.config.mamba.MambaBackendEnum "Permanent link")

Bases: `Enum`

Enumeration of supported Mamba SSU (selective state update) backends.

Source code in `vllm/config/mamba.py`

```
classMambaBackendEnum(Enum, metaclass=_MambaBackendEnumMeta):
"""Enumeration of supported Mamba SSU (selective state update) backends."""

    TRITON = "triton"
    FLASHINFER = "flashinfer"
```

## MambaConfig [¶](#vllm.config.mamba.MambaConfig "Permanent link")

Configuration for Mamba SSM backends.

Source code in `vllm/config/mamba.py`

```
@config
classMambaConfig:
"""Configuration for Mamba SSM backends."""

    backend: MambaBackendEnum = MambaBackendEnum.TRITON
"""Mamba SSU backend to use."""

    enable_stochastic_rounding: bool = False
"""Enable stochastic rounding when writing SSM state to fp16 cache.
    Uses random bits to unbias the rounding error, which can improve
    numerical stability for long sequences."""
    stochastic_rounding_philox_rounds: int = 0
"""Number of Philox PRNG rounds for stochastic rounding random number
    generation. 0 uses the Triton default. Higher values improve randomness
    quality at the cost of compute."""

    @field_validator("backend", mode="before")
    @classmethod
    defvalidate_backend_before(cls, value: Any) -> Any:
"""Enable parsing of the `backend` enum type from string."""
        if isinstance(value, str):
            return MambaBackendEnum[value.upper()]
        return value

    def__post_init__(self):
        if self.enable_stochastic_rounding:
            fromvllm.platformsimport current_platform

            if not current_platform.is_cuda():
                raise ValueError(
                    "Stochastic rounding for Mamba cache is only supported "
                    "on NVIDIA CUDA platforms. Please do not specify  "
                    "`--enable-mamba-cache-stochastic-rounding`."
                )
            if (
                self.backend == MambaBackendEnum.TRITON
                and not current_platform.is_device_capability_family(100)
            ):
                raise ValueError(
                    "Stochastic rounding for Mamba cache with triton backend requires "
                    "compute capability 10.0 (data center Blackwell). The `cvt.rs` "
                    "PTX instruction is not supported on your GPU. Please do not "
                    "specify `--enable-mamba-cache-stochastic-rounding`, "
                    "or set `--mamba-backend flashinfer`."
                )
```

### backend `class-attribute` `instance-attribute` [¶](#vllm.config.mamba.MambaConfig.backend "Permanent link")

```
backend: MambaBackendEnum = TRITON
```

Mamba SSU backend to use.

### enable\_stochastic\_rounding `class-attribute` `instance-attribute` [¶](#vllm.config.mamba.MambaConfig.enable_stochastic_rounding "Permanent link")

```
enable_stochastic_rounding: bool = False
```

Enable stochastic rounding when writing SSM state to fp16 cache. Uses random bits to unbias the rounding error, which can improve numerical stability for long sequences.

### stochastic\_rounding\_philox\_rounds `class-attribute` `instance-attribute` [¶](#vllm.config.mamba.MambaConfig.stochastic_rounding_philox_rounds "Permanent link")

```
stochastic_rounding_philox_rounds: int = 0
```

Number of Philox PRNG rounds for stochastic rounding random number generation. 0 uses the Triton default. Higher values improve randomness quality at the cost of compute.

### validate\_backend\_before `classmethod` [¶](#vllm.config.mamba.MambaConfig.validate_backend_before "Permanent link")

```
validate_backend_before(value: Any) -> Any
```

Enable parsing of the `backend` enum type from string.

Source code in `vllm/config/mamba.py`

```
@field_validator("backend", mode="before")
@classmethod
defvalidate_backend_before(cls, value: Any) -> Any:
"""Enable parsing of the `backend` enum type from string."""
    if isinstance(value, str):
        return MambaBackendEnum[value.upper()]
    return value
```

Bases: `EnumMeta`

Metaclass for MambaBackendEnum to provide better error messages.

Source code in `vllm/config/mamba.py`

```
class_MambaBackendEnumMeta(EnumMeta):
"""Metaclass for MambaBackendEnum to provide better error messages."""

    def__getitem__(cls, name: str):
        try:
            return super().__getitem__(name)
        except KeyError:
            valid = ", ".join(cls.__members__.keys())
            raise ValueError(
                f"Unknown Mamba SSU backend: '{name}'. Valid options are: {valid}"
            ) fromNone
```