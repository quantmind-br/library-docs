---
title: registry - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/attention/backends/registry/
source: sitemap
fetched_at: 2026-05-07T21:39:39.445789833-03:00
rendered_js: false
word_count: 443
summary: This document defines the enumeration of supported attention and mamba backends in vLLM, providing methods for runtime registration, path retrieval, and class resolution.
tags:
    - vllm
    - attention-mechanisms
    - backend-registry
    - enumeration
    - python-api
    - machine-learning
category: api
---

Attention backend registry

## AttentionBackendEnum [¶](#vllm.v1.attention.backends.registry.AttentionBackendEnum "Permanent link")

Bases: `Enum`

Enumeration of all supported attention backends.

The enum value is the default class path, but this can be overridden at runtime using register\_backend().

To get the actual backend class (respecting overrides), use: backend.get\_class()

Source code in `vllm/v1/attention/backends/registry.py`

```
classAttentionBackendEnum(Enum, metaclass=_AttentionBackendEnumMeta):
"""Enumeration of all supported attention backends.

    The enum value is the default class path, but this can be overridden
    at runtime using register_backend().

    To get the actual backend class (respecting overrides), use:
        backend.get_class()
    """

    FLASH_ATTN = "vllm.v1.attention.backends.flash_attn.FlashAttentionBackend"
    FLASH_ATTN_DIFFKV = (
        "vllm.v1.attention.backends.flash_attn_diffkv.FlashAttentionDiffKVBackend"
    )
    TRITON_ATTN = "vllm.v1.attention.backends.triton_attn.TritonAttentionBackend"
    ROCM_ATTN = "vllm.v1.attention.backends.rocm_attn.RocmAttentionBackend"
    ROCM_AITER_MLA = "vllm.v1.attention.backends.mla.rocm_aiter_mla.AiterMLABackend"
    ROCM_AITER_TRITON_MLA = (
        "vllm.v1.attention.backends.mla.aiter_triton_mla.AiterTritonMLABackend"
    )
    ROCM_AITER_FA = (
        "vllm.v1.attention.backends.rocm_aiter_fa.AiterFlashAttentionBackend"
    )
    ROCM_AITER_MLA_SPARSE = (
        "vllm.v1.attention.backends.mla.rocm_aiter_mla_sparse.ROCMAiterMLASparseBackend"
    )
    XPU_MLA_SPARSE = "vllm.v1.attention.backends.mla.xpu_mla_sparse.XPUMLASparseBackend"
    TORCH_SDPA = ""  # this tag is only used for ViT
    FLASHINFER = "vllm.v1.attention.backends.flashinfer.FlashInferBackend"
    FLASHINFER_MLA = (
        "vllm.v1.attention.backends.mla.flashinfer_mla.FlashInferMLABackend"
    )
    FLASHINFER_MLA_SPARSE = (
        "vllm.v1.attention.backends.mla.flashinfer_mla_sparse."
        "FlashInferMLASparseBackend"
    )
    TRITON_MLA = "vllm.v1.attention.backends.mla.triton_mla.TritonMLABackend"
    CUTLASS_MLA = "vllm.v1.attention.backends.mla.cutlass_mla.CutlassMLABackend"
    FLASHMLA = "vllm.v1.attention.backends.mla.flashmla.FlashMLABackend"
    FLASHMLA_SPARSE = (
        "vllm.v1.attention.backends.mla.flashmla_sparse.FlashMLASparseBackend"
    )
    FLASH_ATTN_MLA = "vllm.v1.attention.backends.mla.flashattn_mla.FlashAttnMLABackend"
    NO_ATTENTION = "vllm.v1.attention.backends.no_attention.NoAttentionBackend"
    FLEX_ATTENTION = "vllm.v1.attention.backends.flex_attention.FlexAttentionBackend"
    TREE_ATTN = "vllm.v1.attention.backends.tree_attn.TreeAttentionBackend"
    ROCM_AITER_UNIFIED_ATTN = (
        "vllm.v1.attention.backends.rocm_aiter_unified_attn."
        "RocmAiterUnifiedAttentionBackend"
    )
    CPU_ATTN = "vllm.v1.attention.backends.cpu_attn.CPUAttentionBackend"
    TURBOQUANT = "vllm.v1.attention.backends.turboquant_attn.TurboQuantAttentionBackend"
    # Placeholder for third-party/custom backends - must be registered before use
    # set to None to avoid alias with other backend, whose value is an empty string
    CUSTOM = None

    defget_path(self, include_classname: bool = True) -> str:
"""Get the class path for this backend (respects overrides).

        Returns:
            The fully qualified class path string

        Raises:
            ValueError: If Backend.CUSTOM is used without being registered
        """
        path = _ATTN_OVERRIDES.get(self, self.value)
        if not path:
            raise ValueError(
                f"Backend {self.name} must be registered before use. "
                f"Use register_backend(Backend.{self.name}, 'your.module.YourClass')"
            )
        if not include_classname:
            path = path.rsplit(".", 1)[0]
        return path

    defget_class(self) -> "type[AttentionBackend]":
"""Get the backend class (respects overrides).

        Returns:
            The backend class

        Raises:
            ImportError: If the backend class cannot be imported
            ValueError: If Backend.CUSTOM is used without being registered
        """
        return resolve_obj_by_qualname(self.get_path())

    defis_overridden(self) -> bool:
"""Check if this backend has been overridden.

        Returns:
            True if the backend has a registered override
        """
        return self in _ATTN_OVERRIDES

    defclear_override(self) -> None:
"""Clear any override for this backend, reverting to the default."""
        _ATTN_OVERRIDES.pop(self, None)
```

### clear\_override [¶](#vllm.v1.attention.backends.registry.AttentionBackendEnum.clear_override "Permanent link")

Clear any override for this backend, reverting to the default.

Source code in `vllm/v1/attention/backends/registry.py`

```
defclear_override(self) -> None:
"""Clear any override for this backend, reverting to the default."""
    _ATTN_OVERRIDES.pop(self, None)
```

### get\_class [¶](#vllm.v1.attention.backends.registry.AttentionBackendEnum.get_class "Permanent link")

Get the backend class (respects overrides).

Returns:

Type Description `type[AttentionBackend]`

The backend class

Raises:

Type Description `ImportError`

If the backend class cannot be imported

`ValueError`

If Backend.CUSTOM is used without being registered

Source code in `vllm/v1/attention/backends/registry.py`

```
defget_class(self) -> "type[AttentionBackend]":
"""Get the backend class (respects overrides).

    Returns:
        The backend class

    Raises:
        ImportError: If the backend class cannot be imported
        ValueError: If Backend.CUSTOM is used without being registered
    """
    return resolve_obj_by_qualname(self.get_path())
```

### get\_path [¶](#vllm.v1.attention.backends.registry.AttentionBackendEnum.get_path "Permanent link")

```
get_path(include_classname: bool = True) -> str
```

Get the class path for this backend (respects overrides).

Returns:

Type Description `str`

The fully qualified class path string

Raises:

Type Description `ValueError`

If Backend.CUSTOM is used without being registered

Source code in `vllm/v1/attention/backends/registry.py`

```
defget_path(self, include_classname: bool = True) -> str:
"""Get the class path for this backend (respects overrides).

    Returns:
        The fully qualified class path string

    Raises:
        ValueError: If Backend.CUSTOM is used without being registered
    """
    path = _ATTN_OVERRIDES.get(self, self.value)
    if not path:
        raise ValueError(
            f"Backend {self.name} must be registered before use. "
            f"Use register_backend(Backend.{self.name}, 'your.module.YourClass')"
        )
    if not include_classname:
        path = path.rsplit(".", 1)[0]
    return path
```

### is\_overridden [¶](#vllm.v1.attention.backends.registry.AttentionBackendEnum.is_overridden "Permanent link")

Check if this backend has been overridden.

Returns:

Type Description `bool`

True if the backend has a registered override

Source code in `vllm/v1/attention/backends/registry.py`

```
defis_overridden(self) -> bool:
"""Check if this backend has been overridden.

    Returns:
        True if the backend has a registered override
    """
    return self in _ATTN_OVERRIDES
```

## MambaAttentionBackendEnum [¶](#vllm.v1.attention.backends.registry.MambaAttentionBackendEnum "Permanent link")

Bases: `Enum`

Enumeration of all supported mamba attention backends.

The enum value is the default class path, but this can be overridden at runtime using register\_backend().

To get the actual backend class (respecting overrides), use: backend.get\_class()

Source code in `vllm/v1/attention/backends/registry.py`

```
classMambaAttentionBackendEnum(Enum, metaclass=_AttentionBackendEnumMeta):
"""Enumeration of all supported mamba attention backends.

    The enum value is the default class path, but this can be overridden
    at runtime using register_backend().

    To get the actual backend class (respecting overrides), use:
        backend.get_class()
    """

    MAMBA1 = "vllm.v1.attention.backends.mamba1_attn.Mamba1AttentionBackend"
    MAMBA2 = "vllm.v1.attention.backends.mamba2_attn.Mamba2AttentionBackend"
    SHORT_CONV = "vllm.v1.attention.backends.short_conv_attn.ShortConvAttentionBackend"
    LINEAR = "vllm.v1.attention.backends.linear_attn.LinearAttentionBackend"
    GDN_ATTN = "vllm.v1.attention.backends.gdn_attn.GDNAttentionBackend"
    # Placeholder for third-party/custom backends - must be registered before use
    # set to None to avoid alias with other backend, whose value is an empty string
    CUSTOM = None

    defget_path(self, include_classname: bool = True) -> str:
"""Get the class path for this backend (respects overrides).

        Returns:
            The fully qualified class path string

        Raises:
            ValueError: If Backend.CUSTOM is used without being registered
        """
        path = _MAMBA_ATTN_OVERRIDES.get(self, self.value)
        if not path:
            raise ValueError(
                f"Backend {self.name} must be registered before use. "
                f"Use register_backend(Backend.{self.name}, 'your.module.YourClass')"
            )
        if not include_classname:
            path = path.rsplit(".", 1)[0]
        return path

    defget_class(self) -> "type[AttentionBackend]":
"""Get the backend class (respects overrides).

        Returns:
            The backend class

        Raises:
            ImportError: If the backend class cannot be imported
            ValueError: If Backend.CUSTOM is used without being registered
        """
        return resolve_obj_by_qualname(self.get_path())

    defis_overridden(self) -> bool:
"""Check if this backend has been overridden.

        Returns:
            True if the backend has a registered override
        """
        return self in _MAMBA_ATTN_OVERRIDES

    defclear_override(self) -> None:
"""Clear any override for this backend, reverting to the default."""
        _MAMBA_ATTN_OVERRIDES.pop(self, None)
```

### clear\_override [¶](#vllm.v1.attention.backends.registry.MambaAttentionBackendEnum.clear_override "Permanent link")

Clear any override for this backend, reverting to the default.

Source code in `vllm/v1/attention/backends/registry.py`

```
defclear_override(self) -> None:
"""Clear any override for this backend, reverting to the default."""
    _MAMBA_ATTN_OVERRIDES.pop(self, None)
```

### get\_class [¶](#vllm.v1.attention.backends.registry.MambaAttentionBackendEnum.get_class "Permanent link")

Get the backend class (respects overrides).

Returns:

Type Description `type[AttentionBackend]`

The backend class

Raises:

Type Description `ImportError`

If the backend class cannot be imported

`ValueError`

If Backend.CUSTOM is used without being registered

Source code in `vllm/v1/attention/backends/registry.py`

```
defget_class(self) -> "type[AttentionBackend]":
"""Get the backend class (respects overrides).

    Returns:
        The backend class

    Raises:
        ImportError: If the backend class cannot be imported
        ValueError: If Backend.CUSTOM is used without being registered
    """
    return resolve_obj_by_qualname(self.get_path())
```

### get\_path [¶](#vllm.v1.attention.backends.registry.MambaAttentionBackendEnum.get_path "Permanent link")

```
get_path(include_classname: bool = True) -> str
```

Get the class path for this backend (respects overrides).

Returns:

Type Description `str`

The fully qualified class path string

Raises:

Type Description `ValueError`

If Backend.CUSTOM is used without being registered

Source code in `vllm/v1/attention/backends/registry.py`

```
defget_path(self, include_classname: bool = True) -> str:
"""Get the class path for this backend (respects overrides).

    Returns:
        The fully qualified class path string

    Raises:
        ValueError: If Backend.CUSTOM is used without being registered
    """
    path = _MAMBA_ATTN_OVERRIDES.get(self, self.value)
    if not path:
        raise ValueError(
            f"Backend {self.name} must be registered before use. "
            f"Use register_backend(Backend.{self.name}, 'your.module.YourClass')"
        )
    if not include_classname:
        path = path.rsplit(".", 1)[0]
    return path
```

### is\_overridden [¶](#vllm.v1.attention.backends.registry.MambaAttentionBackendEnum.is_overridden "Permanent link")

Check if this backend has been overridden.

Returns:

Type Description `bool`

True if the backend has a registered override

Source code in `vllm/v1/attention/backends/registry.py`

```
defis_overridden(self) -> bool:
"""Check if this backend has been overridden.

    Returns:
        True if the backend has a registered override
    """
    return self in _MAMBA_ATTN_OVERRIDES
```

Bases: `EnumMeta`

Metaclass for AttentionBackendEnum to provide better error messages.

Source code in `vllm/v1/attention/backends/registry.py`

```
class_AttentionBackendEnumMeta(EnumMeta):
"""Metaclass for AttentionBackendEnum to provide better error messages."""

    def__getitem__(cls, name: str):
"""Get backend by name with helpful error messages."""
        try:
            return super().__getitem__(name)
        except KeyError:
            members = cast("dict[str, Enum]", cls.__members__).keys()
            valid_backends = ", ".join(members)
            raise ValueError(
                f"Unknown attention backend: '{name}'. "
                f"Valid options are: {valid_backends}"
            ) fromNone
```

### \_\_getitem\__ [¶](#vllm.v1.attention.backends.registry._AttentionBackendEnumMeta.__getitem__ "Permanent link")

Get backend by name with helpful error messages.

Source code in `vllm/v1/attention/backends/registry.py`

```
def__getitem__(cls, name: str):
"""Get backend by name with helpful error messages."""
    try:
        return super().__getitem__(name)
    except KeyError:
        members = cast("dict[str, Enum]", cls.__members__).keys()
        valid_backends = ", ".join(members)
        raise ValueError(
            f"Unknown attention backend: '{name}'. "
            f"Valid options are: {valid_backends}"
        ) fromNone
```

## register\_backend [¶](#vllm.v1.attention.backends.registry.register_backend "Permanent link")

Register or override a backend implementation.

Parameters:

Name Type Description Default `backend` `AttentionBackendEnum | MambaAttentionBackendEnum`

The AttentionBackendEnum member to register

*required* `class_path` `str | None`

Optional class path. If not provided and used as decorator, will be auto-generated from the class.

`None`

Returns:

Type Description `Callable[[type], type]`

Decorator function if class\_path is None, otherwise a no-op

Examples:

### Override an existing attention backend[¶](#vllm.v1.attention.backends.registry.register_backend--override-an-existing-attention-backend "Permanent link")

@register\_backend(AttentionBackendEnum.FLASH\_ATTN) class MyCustomFlashAttn: ...

### Override an existing mamba attention backend[¶](#vllm.v1.attention.backends.registry.register_backend--override-an-existing-mamba-attention-backend "Permanent link")

@register\_backend(MambaAttentionBackendEnum.LINEAR, is\_mamba=True) class MyCustomMambaAttn: ...

### Register a custom third-party attention backend[¶](#vllm.v1.attention.backends.registry.register_backend--register-a-custom-third-party-attention-backend "Permanent link")

@register\_backend(AttentionBackendEnum.CUSTOM) class MyCustomBackend: ...

### Direct registration[¶](#vllm.v1.attention.backends.registry.register_backend--direct-registration "Permanent link")

register\_backend( AttentionBackendEnum.CUSTOM, "my.module.MyCustomBackend" )

Source code in `vllm/v1/attention/backends/registry.py`

```
defregister_backend(
    backend: AttentionBackendEnum | MambaAttentionBackendEnum,
    class_path: str | None = None,
    is_mamba: bool = False,
) -> Callable[[type], type]:
"""Register or override a backend implementation.

    Args:
        backend: The AttentionBackendEnum member to register
        class_path: Optional class path. If not provided and used as
            decorator, will be auto-generated from the class.

    Returns:
        Decorator function if class_path is None, otherwise a no-op

    Examples:
        # Override an existing attention backend
        @register_backend(AttentionBackendEnum.FLASH_ATTN)
        class MyCustomFlashAttn:
            ...

        # Override an existing mamba attention backend
        @register_backend(MambaAttentionBackendEnum.LINEAR, is_mamba=True)
        class MyCustomMambaAttn:
            ...

        # Register a custom third-party attention backend
        @register_backend(AttentionBackendEnum.CUSTOM)
        class MyCustomBackend:
            ...

        # Direct registration
        register_backend(
            AttentionBackendEnum.CUSTOM,
            "my.module.MyCustomBackend"
        )
    """

    defdecorator(cls: type) -> type:
        if is_mamba:
            _MAMBA_ATTN_OVERRIDES[backend] = f"{cls.__module__}.{cls.__qualname__}"  # type: ignore[index]
        else:
            _ATTN_OVERRIDES[backend] = f"{cls.__module__}.{cls.__qualname__}"  # type: ignore[index]
        return cls

    if class_path is not None:
        if is_mamba:
            _MAMBA_ATTN_OVERRIDES[backend] = class_path  # type: ignore[index]
        else:
            _ATTN_OVERRIDES[backend] = class_path  # type: ignore[index]
        return lambda x: x

    return decorator
```