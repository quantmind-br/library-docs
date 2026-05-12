---
title: registry - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/attention/backends/mla/prefill/registry/
source: sitemap
fetched_at: 2026-05-07T21:39:30.251415519-03:00
rendered_js: false
word_count: 80
summary: This document defines the registry and enumeration for Multi-Head Latent Attention (MLA) prefill backends within the vLLM architecture, providing mechanisms for loading and retrieving backend classes.
tags:
    - vllm
    - mla-prefill
    - attention-backend
    - python-registry
    - lazy-loading
category: reference
---

## vllm.v1.attention.backends.mla.prefill.registry [¶](#vllm.v1.attention.backends.mla.prefill.registry "Permanent link")

Registry for MLA prefill backends.

This module provides an enumeration of all available MLA prefill backends and utilities for loading them.

## MLAPrefillBackendEnum [¶](#vllm.v1.attention.backends.mla.prefill.registry.MLAPrefillBackendEnum "Permanent link")

Bases: `Enum`

Enumeration of all supported MLA prefill backends.

Source code in `vllm/v1/attention/backends/mla/prefill/registry.py`

```
classMLAPrefillBackendEnum(Enum, metaclass=_MLAPrefillBackendEnumMeta):
"""Enumeration of all supported MLA prefill backends."""

    FLASH_ATTN = (
        "vllm.v1.attention.backends.mla.prefill.flash_attn.FlashAttnPrefillBackend"
    )
    FLASHINFER = (
        "vllm.v1.attention.backends.mla.prefill.flashinfer.FlashInferPrefillBackend"
    )
    TRTLLM_RAGGED = (
        "vllm.v1.attention.backends.mla.prefill.trtllm_ragged."
        "TrtllmRaggedPrefillBackend"
    )

    defget_path(self) -> str:
"""Get the fully qualified class path for this backend."""
        return self.value

    defget_class(self) -> "type[MLAPrefillBackend]":
"""Lazy load and return the backend class."""
        return resolve_obj_by_qualname(self.get_path())
```

### get\_class [¶](#vllm.v1.attention.backends.mla.prefill.registry.MLAPrefillBackendEnum.get_class "Permanent link")

Lazy load and return the backend class.

Source code in `vllm/v1/attention/backends/mla/prefill/registry.py`

```
defget_class(self) -> "type[MLAPrefillBackend]":
"""Lazy load and return the backend class."""
    return resolve_obj_by_qualname(self.get_path())
```

### get\_path [¶](#vllm.v1.attention.backends.mla.prefill.registry.MLAPrefillBackendEnum.get_path "Permanent link")

Get the fully qualified class path for this backend.

Source code in `vllm/v1/attention/backends/mla/prefill/registry.py`

```
defget_path(self) -> str:
"""Get the fully qualified class path for this backend."""
    return self.value
```

Bases: `EnumMeta`

Metaclass for MLAPrefillBackendEnum to provide better error messages.

Source code in `vllm/v1/attention/backends/mla/prefill/registry.py`

```
class_MLAPrefillBackendEnumMeta(EnumMeta):
"""Metaclass for MLAPrefillBackendEnum to provide better error messages."""

    def__getitem__(cls, name: str):
        try:
            return super().__getitem__(name)
        except KeyError:
            members = cls.__members__.keys()
            valid_backends = ", ".join(members)
            raise ValueError(
                f"Unknown MLA prefill backend: '{name}'. "
                f"Valid options are: {valid_backends}"
            ) fromNone
```