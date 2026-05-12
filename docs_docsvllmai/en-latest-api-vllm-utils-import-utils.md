---
title: import_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/utils/import_utils/
source: sitemap
fetched_at: 2026-05-07T21:38:40.246646095-03:00
rendered_js: false
word_count: 774
summary: This document describes internal utility classes for handling module imports, specifically providing mechanisms for lazy loading to optimize dependency management and placeholder objects to improve error reporting for missing modules.
tags:
    - python
    - lazy-loading
    - module-import
    - dependency-management
    - error-handling
    - utilities
category: reference
---

Contains helpers related to importing modules.

This is similar in concept to the `importlib` module.

## LazyLoader [¶](#vllm.utils.import_utils.LazyLoader "Permanent link")

Bases: `ModuleType`

`LazyLoader` module borrowed from \[Tensorflow] (https://github.com/tensorflow/tensorflow/blob/main/tensorflow/python/util/lazy\_loader.py) with an addition of "module caching".

Lazily import a module, mainly to avoid pulling in large dependencies. Modules such as `xgrammar` might do additional side effects, so we only want to use this when it is needed, delaying all eager effects.

Source code in `vllm/utils/import_utils.py`

```
classLazyLoader(ModuleType):
"""
    `LazyLoader` module borrowed from [Tensorflow]
    (https://github.com/tensorflow/tensorflow/blob/main/tensorflow/python/util/lazy_loader.py)
    with an addition of "module caching".

    Lazily import a module, mainly to avoid pulling in large dependencies.
    Modules such as `xgrammar` might do additional side effects, so we
    only want to use this when it is needed, delaying all eager effects.
    """

    def__init__(
        self,
        local_name: str,
        parent_module_globals: dict[str, Any],
        name: str,
    ):
        self._local_name = local_name
        self._parent_module_globals = parent_module_globals
        self._module: ModuleType | None = None

        super().__init__(str(name))

    def_load(self) -> ModuleType:
        # Import the target module and insert it into the parent's namespace
        try:
            module = importlib.import_module(self.__name__)
            self._parent_module_globals[self._local_name] = module
            # The additional add to sys.modules
            # ensures library is actually loaded.
            sys.modules[self._local_name] = module
        except ModuleNotFoundError as err:
            raise err fromNone

        # Update this object's dict so that if someone keeps a
        # reference to the LazyLoader, lookups are efficient
        # (__getattr__ is only called on lookups that fail).
        self.__dict__.update(module.__dict__)
        return module

    def__getattr__(self, item: Any) -> Any:
        if self._module is None:
            self._module = self._load()
        return getattr(self._module, item)

    def__dir__(self) -> list[str]:
        if self._module is None:
            self._module = self._load()
        return dir(self._module)
```

## PlaceholderModule [¶](#vllm.utils.import_utils.PlaceholderModule "Permanent link")

Bases: `_PlaceholderBase`

A placeholder object to use when a module does not exist.

This enables more informative errors when trying to access attributes of a module that does not exist.

Source code in `vllm/utils/import_utils.py`

```
classPlaceholderModule(_PlaceholderBase):
"""
    A placeholder object to use when a module does not exist.

    This enables more informative errors when trying to access attributes
    of a module that does not exist.
    """

    def__init__(self, name: str) -> None:
        super().__init__()

        # Apply name mangling to avoid conflicting with module attributes
        self.__name = name

    defplaceholder_attr(self, attr_path: str):
        return _PlaceholderModuleAttr(self, attr_path)

    def__getattr__(self, key: str) -> Never:
        name = self.__name

        try:
            importlib.import_module(name)
        except ImportError as exc:
            for extra, names in get_vllm_optional_dependencies().items():
                if name in names:
                    msg = f"Please install vllm[{extra}] for {extra} support"
                    raise ImportError(msg) fromexc

            raise exc

        raise AssertionError(
            "PlaceholderModule should not be used "
            "when the original module can be imported"
        )
```

## \_PlaceholderBase [¶](#vllm.utils.import_utils._PlaceholderBase "Permanent link")

Disallows downstream usage of placeholder modules.

We need to explicitly override each dunder method because [`__getattr__`](#vllm.utils.import_utils._PlaceholderBase.__getattr__ "            __getattr__") is not called when they are accessed.

Info

[Special method lookup](https://docs.python.org/3/reference/datamodel.html#special-lookup)

Source code in `vllm/utils/import_utils.py`

```
class_PlaceholderBase:
"""
    Disallows downstream usage of placeholder modules.

    We need to explicitly override each dunder method because
    [`__getattr__`][vllm.utils.import_utils._PlaceholderBase.__getattr__]
    is not called when they are accessed.

    Info:
        [Special method lookup](https://docs.python.org/3/reference/datamodel.html#special-lookup)
    """

    def__getattr__(self, key: str) -> Never:
"""
        The main class should implement this to throw an error
        for attribute accesses representing downstream usage.
        """
        raise NotImplementedError

    # [Basic customization]

    def__lt__(self, other: object):
        return self.__getattr__("__lt__")

    def__le__(self, other: object):
        return self.__getattr__("__le__")

    def__eq__(self, other: object):
        return self.__getattr__("__eq__")

    def__ne__(self, other: object):
        return self.__getattr__("__ne__")

    def__gt__(self, other: object):
        return self.__getattr__("__gt__")

    def__ge__(self, other: object):
        return self.__getattr__("__ge__")

    def__hash__(self):
        return self.__getattr__("__hash__")

    def__bool__(self):
        return self.__getattr__("__bool__")

    # [Callable objects]

    def__call__(self, *args: object, **kwargs: object):
        return self.__getattr__("__call__")

    # [Container types]

    def__len__(self):
        return self.__getattr__("__len__")

    def__getitem__(self, key: object):
        return self.__getattr__("__getitem__")

    def__setitem__(self, key: object, value: object):
        return self.__getattr__("__setitem__")

    def__delitem__(self, key: object):
        return self.__getattr__("__delitem__")

    # __missing__ is optional according to __getitem__ specification,
    # so it is skipped

    # __iter__ and __reversed__ have a default implementation
    # based on __len__ and __getitem__, so they are skipped.

    # [Numeric Types]

    def__add__(self, other: object):
        return self.__getattr__("__add__")

    def__sub__(self, other: object):
        return self.__getattr__("__sub__")

    def__mul__(self, other: object):
        return self.__getattr__("__mul__")

    def__matmul__(self, other: object):
        return self.__getattr__("__matmul__")

    def__truediv__(self, other: object):
        return self.__getattr__("__truediv__")

    def__floordiv__(self, other: object):
        return self.__getattr__("__floordiv__")

    def__mod__(self, other: object):
        return self.__getattr__("__mod__")

    def__divmod__(self, other: object):
        return self.__getattr__("__divmod__")

    def__pow__(self, other: object, modulo: object = ...):
        return self.__getattr__("__pow__")

    def__lshift__(self, other: object):
        return self.__getattr__("__lshift__")

    def__rshift__(self, other: object):
        return self.__getattr__("__rshift__")

    def__and__(self, other: object):
        return self.__getattr__("__and__")

    def__xor__(self, other: object):
        return self.__getattr__("__xor__")

    def__or__(self, other: object):
        return self.__getattr__("__or__")

    # r* and i* methods have lower priority than
    # the methods for left operand so they are skipped

    def__neg__(self):
        return self.__getattr__("__neg__")

    def__pos__(self):
        return self.__getattr__("__pos__")

    def__abs__(self):
        return self.__getattr__("__abs__")

    def__invert__(self):
        return self.__getattr__("__invert__")

    # __complex__, __int__ and __float__ have a default implementation
    # based on __index__, so they are skipped.

    def__index__(self):
        return self.__getattr__("__index__")

    def__round__(self, ndigits: object = ...):
        return self.__getattr__("__round__")

    def__trunc__(self):
        return self.__getattr__("__trunc__")

    def__floor__(self):
        return self.__getattr__("__floor__")

    def__ceil__(self):
        return self.__getattr__("__ceil__")

    # [Context managers]

    def__enter__(self):
        return self.__getattr__("__enter__")

    def__exit__(self, *args: object, **kwargs: object):
        return self.__getattr__("__exit__")
```

### \_\_getattr\__ [¶](#vllm.utils.import_utils._PlaceholderBase.__getattr__ "Permanent link")

The main class should implement this to throw an error for attribute accesses representing downstream usage.

Source code in `vllm/utils/import_utils.py`

```
def__getattr__(self, key: str) -> Never:
"""
    The main class should implement this to throw an error
    for attribute accesses representing downstream usage.
    """
    raise NotImplementedError
```

## \_has\_module `cached` [¶](#vllm.utils.import_utils._has_module "Permanent link")

```
_has_module(module_name: str) -> bool
```

Return True if *module\_name* can be found in the current environment.

The result is cached so that subsequent queries for the same module incur no additional overhead.

Source code in `vllm/utils/import_utils.py`

```
@cache
def_has_module(module_name: str) -> bool:
"""Return True if *module_name* can be found in the current environment.

    The result is cached so that subsequent queries for the same module incur
    no additional overhead.
    """
    return importlib.util.find_spec(module_name) is not None
```

## has\_aiter [¶](#vllm.utils.import_utils.has_aiter "Permanent link")

Whether the optional `aiter` package is available.

Source code in `vllm/utils/import_utils.py`

```
defhas_aiter() -> bool:
"""Whether the optional `aiter` package is available."""
    return _has_module("aiter")
```

## has\_arctic\_inference [¶](#vllm.utils.import_utils.has_arctic_inference "Permanent link")

```
has_arctic_inference() -> bool
```

Whether the optional `arctic_inference` package is available.

Source code in `vllm/utils/import_utils.py`

```
defhas_arctic_inference() -> bool:
"""Whether the optional `arctic_inference` package is available."""

    return _has_module("arctic_inference")
```

## has\_deep\_ep [¶](#vllm.utils.import_utils.has_deep_ep "Permanent link")

Whether the optional `deep_ep` package is available.

Source code in `vllm/utils/import_utils.py`

```
defhas_deep_ep() -> bool:
"""Whether the optional `deep_ep` package is available."""
    return _has_module("deep_ep")
```

## has\_deep\_gemm [¶](#vllm.utils.import_utils.has_deep_gemm "Permanent link")

Whether the optional `deep_gemm` package is available.

Prefers an externally installed `deep_gemm` package (so users can override with a newer version), then falls back to the vendored copy bundled in the vLLM wheel.

Source code in `vllm/utils/import_utils.py`

```
defhas_deep_gemm() -> bool:
"""Whether the optional `deep_gemm` package is available.

    Prefers an externally installed ``deep_gemm`` package (so users can
    override with a newer version), then falls back to the vendored copy
    bundled in the vLLM wheel.
    """
    return _has_module("deep_gemm") or _has_module("vllm.third_party.deep_gemm")
```

## has\_fbgemm\_gpu [¶](#vllm.utils.import_utils.has_fbgemm_gpu "Permanent link")

Whether the optional `fbgemm_gpu` package is available.

Source code in `vllm/utils/import_utils.py`

```
defhas_fbgemm_gpu() -> bool:
"""Whether the optional `fbgemm_gpu` package is available."""
    return _has_module("fbgemm_gpu")
```

## has\_helion [¶](#vllm.utils.import_utils.has_helion "Permanent link")

Whether the optional `helion` package is available.

Helion is a Python-embedded DSL for writing ML kernels. See: https://github.com/pytorch/helion

Usage

if has\_helion(): import helion import helion.language as hl # use helion...

Source code in `vllm/utils/import_utils.py`

```
defhas_helion() -> bool:
"""Whether the optional `helion` package is available.

    Helion is a Python-embedded DSL for writing ML kernels.
    See: https://github.com/pytorch/helion

    Usage:
        if has_helion():
            import helion
            import helion.language as hl
            # use helion...
    """
    return _has_module("helion")
```

## has\_mori [¶](#vllm.utils.import_utils.has_mori "Permanent link")

Whether the optional `mori` package is available.

Source code in `vllm/utils/import_utils.py`

```
defhas_mori() -> bool:
"""Whether the optional `mori` package is available."""
    return _has_module("mori")
```

## has\_nixl\_ep [¶](#vllm.utils.import_utils.has_nixl_ep "Permanent link")

Whether the optional `nixl_ep` package is available.

Source code in `vllm/utils/import_utils.py`

```
defhas_nixl_ep() -> bool:
"""Whether the optional `nixl_ep` package is available."""
    return _has_module("nixl_ep")
```

## has\_tilelang [¶](#vllm.utils.import_utils.has_tilelang "Permanent link")

Whether the optional `tilelang` package is available.

Source code in `vllm/utils/import_utils.py`

```
defhas_tilelang() -> bool:
"""Whether the optional `tilelang` package is available."""
    return _has_module("tilelang")
```

## has\_triton\_kernels [¶](#vllm.utils.import_utils.has_triton_kernels "Permanent link")

```
has_triton_kernels() -> bool
```

Whether the optional `triton_kernels` package is available.

Source code in `vllm/utils/import_utils.py`

```
defhas_triton_kernels() -> bool:
"""Whether the optional `triton_kernels` package is available."""
    is_available = _has_module("triton_kernels") or _has_module(
        "vllm.third_party.triton_kernels"
    )
    if is_available:
        import_triton_kernels()
    return is_available
```

## import\_from\_path [¶](#vllm.utils.import_utils.import_from_path "Permanent link")

Import a Python file according to its file path.

Based on the official recipe: https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly

Source code in `vllm/utils/import_utils.py`

```
defimport_from_path(module_name: str, file_path: str | os.PathLike):
"""
    Import a Python file according to its file path.

    Based on the official recipe:
    https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly
    """
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None:
        raise ModuleNotFoundError(f"No module named {module_name!r}")

    assert spec.loader is not None

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module
```

## import\_pynvml [¶](#vllm.utils.import_utils.import_pynvml "Permanent link")

Historical comments:

libnvml.so is the library behind nvidia-smi, and pynvml is a Python wrapper around it. We use it to get GPU status without initializing CUDA context in the current process. Historically, there are two packages that provide pynvml: - `nvidia-ml-py` (https://pypi.org/project/nvidia-ml-py/): The official wrapper. It is a dependency of vLLM, and is installed when users install vLLM. It provides a Python module named `pynvml`. - `pynvml` (https://pypi.org/project/pynvml/): An unofficial wrapper. Prior to version 12.0, it also provides a Python module `pynvml`, and therefore conflicts with the official one. What's worse, the module is a Python package, and has higher priority than the official one which is a standalone Python file. This causes errors when both of them are installed. Starting from version 12.0, it migrates to a new module named `pynvml_utils` to avoid the conflict. It is so confusing that many packages in the community use the unofficial one by mistake, and we have to handle this case. For example, `nvcr.io/nvidia/pytorch:24.12-py3` uses the unofficial one, and it will cause errors, see the issue https://github.com/vllm-project/vllm/issues/12847 for example. After all the troubles, we decide to copy the official `pynvml` module to our codebase, and use it directly.

Source code in `vllm/utils/import_utils.py`

```
defimport_pynvml():
"""
    Historical comments:

    libnvml.so is the library behind nvidia-smi, and
    pynvml is a Python wrapper around it. We use it to get GPU
    status without initializing CUDA context in the current process.
    Historically, there are two packages that provide pynvml:
    - `nvidia-ml-py` (https://pypi.org/project/nvidia-ml-py/): The official
        wrapper. It is a dependency of vLLM, and is installed when users
        install vLLM. It provides a Python module named `pynvml`.
    - `pynvml` (https://pypi.org/project/pynvml/): An unofficial wrapper.
        Prior to version 12.0, it also provides a Python module `pynvml`,
        and therefore conflicts with the official one. What's worse,
        the module is a Python package, and has higher priority than
        the official one which is a standalone Python file.
        This causes errors when both of them are installed.
        Starting from version 12.0, it migrates to a new module
        named `pynvml_utils` to avoid the conflict.
    It is so confusing that many packages in the community use the
    unofficial one by mistake, and we have to handle this case.
    For example, `nvcr.io/nvidia/pytorch:24.12-py3` uses the unofficial
    one, and it will cause errors, see the issue
    https://github.com/vllm-project/vllm/issues/12847 for example.
    After all the troubles, we decide to copy the official `pynvml`
    module to our codebase, and use it directly.
    """
    importvllm.third_party.pynvmlaspynvml

    return pynvml
```

## import\_triton\_kernels `cached` [¶](#vllm.utils.import_utils.import_triton_kernels "Permanent link")

For convenience, prioritize triton\_kernels that is available in `site-packages`. Use `vllm.third_party.triton_kernels` as a fall-back.

Source code in `vllm/utils/import_utils.py`

```
@cache
defimport_triton_kernels():
"""
    For convenience, prioritize triton_kernels that is available in
    `site-packages`. Use `vllm.third_party.triton_kernels` as a fall-back.
    """
    if _has_module("triton_kernels"):
        importtriton_kernels

        logger.debug_once(
            f"Loading module triton_kernels from {triton_kernels.__file__}.",
        )
    elif _has_module("vllm.third_party.triton_kernels"):
        importvllm.third_party.triton_kernelsastriton_kernels

        logger.debug_once(
            f"Loading module triton_kernels from {triton_kernels.__file__}.",
        )
        sys.modules["triton_kernels"] = triton_kernels
    else:
        logger.info_once(
            "triton_kernels unavailable in this build. "
            "Please consider installing triton_kernels from "
            "https://github.com/triton-lang/triton/tree/main/python/triton_kernels"
        )
```

## resolve\_obj\_by\_qualname [¶](#vllm.utils.import_utils.resolve_obj_by_qualname "Permanent link")

```
resolve_obj_by_qualname(qualname: str) -> Any
```

Resolve an object by its fully-qualified class name.

Source code in `vllm/utils/import_utils.py`

```
defresolve_obj_by_qualname(qualname: str) -> Any:
"""
    Resolve an object by its fully-qualified class name.
    """
    module_name, obj_name = qualname.rsplit(".", 1)
    module = importlib.import_module(module_name)
    return getattr(module, obj_name)
```