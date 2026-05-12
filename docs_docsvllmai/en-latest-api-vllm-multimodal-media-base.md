---
title: base - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/multimodal/media/base/
source: sitemap
fetched_at: 2026-05-07T21:34:12.194877233-03:00
rendered_js: false
word_count: 165
summary: This document defines the base classes and structures for handling multimodal media input, including configuration merging and a wrapper for managing media objects with their raw byte data.
tags:
    - multimodal
    - media-io
    - data-processing
    - configuration-management
    - python-base-classes
category: reference
---

Bases: `ABC`, `Generic[_T]`

Configuration values can be user-provided either by --media-io-kwargs or by the runtime API field "media\_io\_kwargs". Ensure proper validation and error handling.

Source code in `vllm/multimodal/media/base.py`

```
classMediaIO(ABC, Generic[_T]):
"""Configuration values can be user-provided either by --media-io-kwargs or
    by the runtime API field "media_io_kwargs". Ensure proper validation and
    error handling.
    """

    @classmethod
    defmerge_kwargs(
        cls,
        default_kwargs: dict[str, Any] | None,
        runtime_kwargs: dict[str, Any] | None,
    ) -> dict[str, Any]:
"""Merge config-level kwargs and request-level kwargs.

        By default this performs a shallow merge where runtime kwargs override
        keys in default kwargs. Subclasses may override to apply modality-
        specific behavior.
        """
        merged = dict(default_kwargs or {})
        if runtime_kwargs:
            merged.update(runtime_kwargs)
        return merged

    @abstractmethod
    defload_bytes(self, data: bytes) -> _T:
        raise NotImplementedError

    @abstractmethod
    defload_base64(self, media_type: str, data: str) -> _T:
"""
        List of media types:
        https://www.iana.org/assignments/media-types/media-types.xhtml
        """
        raise NotImplementedError

    @abstractmethod
    defload_file(self, filepath: Path) -> _T:
        raise NotImplementedError
```

### load\_base64 `abstractmethod` [¶](#vllm.multimodal.media.base.MediaIO.load_base64 "Permanent link")

```
load_base64(media_type: str, data: str) -> _T
```

List of media types: https://www.iana.org/assignments/media-types/media-types.xhtml

Source code in `vllm/multimodal/media/base.py`

```
@abstractmethod
defload_base64(self, media_type: str, data: str) -> _T:
"""
    List of media types:
    https://www.iana.org/assignments/media-types/media-types.xhtml
    """
    raise NotImplementedError
```

### merge\_kwargs `classmethod` [¶](#vllm.multimodal.media.base.MediaIO.merge_kwargs "Permanent link")

Merge config-level kwargs and request-level kwargs.

By default this performs a shallow merge where runtime kwargs override keys in default kwargs. Subclasses may override to apply modality- specific behavior.

Source code in `vllm/multimodal/media/base.py`

```
@classmethod
defmerge_kwargs(
    cls,
    default_kwargs: dict[str, Any] | None,
    runtime_kwargs: dict[str, Any] | None,
) -> dict[str, Any]:
"""Merge config-level kwargs and request-level kwargs.

    By default this performs a shallow merge where runtime kwargs override
    keys in default kwargs. Subclasses may override to apply modality-
    specific behavior.
    """
    merged = dict(default_kwargs or {})
    if runtime_kwargs:
        merged.update(runtime_kwargs)
    return merged
```

Bases: `Generic[_T]`

Wrapper that couples a media object with its original encoded bytes.

This ensures the raw bytes and media object remain synchronized, preventing cache corruption from in-place modifications.

The wrapper delegates attribute access to the underlying media object, making it behave transparently like the wrapped type (e.g., PIL.Image).

NOTE: Currently, this wrapper is used only for the image modality.

Source code in `vllm/multimodal/media/base.py`

```
@dataclass
classMediaWithBytes(Generic[_T]):
"""
    Wrapper that couples a media object with its original encoded bytes.

    This ensures the raw bytes and media object remain synchronized,
    preventing cache corruption from in-place modifications.

    The wrapper delegates attribute access to the underlying media object,
    making it behave transparently like the wrapped type (e.g., PIL.Image).

    NOTE: Currently, this wrapper is used only for the image modality.
    """

    media: _T
    original_bytes: bytes = field(repr=False)

    def__array__(self, *args, **kwargs) -> np.ndarray:
"""Allow np.array(obj) to return np.array(obj.media)."""
        return np.array(self.media, *args, **kwargs)

    def__getstate__(self):
        return self.__dict__.copy()

    def__setstate__(self, state: dict[str, Any]):
        self.__dict__.update(state)

    def__getattr__(self, name: str):
"""Delegate attribute access to the underlying media object."""
        return getattr(self.media, name)
```

### \_\_array\__ [¶](#vllm.multimodal.media.base.MediaWithBytes.__array__ "Permanent link")

```
__array__(*args, **kwargs) -> ndarray
```

Allow np.array(obj) to return np.array(obj.media).

Source code in `vllm/multimodal/media/base.py`

```
def__array__(self, *args, **kwargs) -> np.ndarray:
"""Allow np.array(obj) to return np.array(obj.media)."""
    return np.array(self.media, *args, **kwargs)
```

### \_\_getattr\__ [¶](#vllm.multimodal.media.base.MediaWithBytes.__getattr__ "Permanent link")

Delegate attribute access to the underlying media object.

Source code in `vllm/multimodal/media/base.py`

```
def__getattr__(self, name: str):
"""Delegate attribute access to the underlying media object."""
    return getattr(self.media, name)
```