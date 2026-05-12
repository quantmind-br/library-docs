---
title: registry - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/utils/registry/
source: sitemap
fetched_at: 2026-05-07T21:38:55.227604001-03:00
rendered_js: false
word_count: 91
summary: The ExtensionManager class provides a registry mechanism to register, manage, and instantiate pluggable classes by name at runtime.
tags:
    - extension-manager
    - registry-pattern
    - plugin-system
    - class-loading
    - python-utilities
category: reference
---

## ExtensionManager [¶](#vllm.utils.registry.ExtensionManager "Permanent link")

A registry for managing pluggable extension classes.

This class provides a simple mechanism to register and instantiate extension classes by name. It is commonly used to implement plugin systems where different implementations can be swapped at runtime.

Examples:

Basic usage with a registry instance:

```
>>> FOO_REGISTRY = ExtensionManager()
>>> @FOO_REGISTRY.register("my_foo_impl")
... classMyFooImpl(Foo):
...     def__init__(self, value):
...         self.value = value
>>> foo_impl = FOO_REGISTRY.load("my_foo_impl", value=123)
```

Source code in `vllm/utils/registry.py`

```
classExtensionManager:
"""
    A registry for managing pluggable extension classes.

    This class provides a simple mechanism to register and instantiate
    extension classes by name. It is commonly used to implement plugin
    systems where different implementations can be swapped at runtime.

    Examples:
        Basic usage with a registry instance:

        >>> FOO_REGISTRY = ExtensionManager()
        >>> @FOO_REGISTRY.register("my_foo_impl")
        ... class MyFooImpl(Foo):
        ...     def __init__(self, value):
        ...         self.value = value
        >>> foo_impl = FOO_REGISTRY.load("my_foo_impl", value=123)

    """

    def__init__(self) -> None:
"""
        Initialize an empty extension registry.
        """
        self.name2class: dict[str, type] = {}

    defregister(self, name: str):
"""
        Decorator to register a class with the given name.
        """

        defwrap(cls_to_register: _T) -> _T:
            self.name2class[name] = cls_to_register
            return cls_to_register

        return wrap

    defload(self, cls_name: str, *args, **kwargs) -> Any:
"""
        Instantiate and return a registered extension class by name.
        """
        cls = self.name2class.get(cls_name)
        assert cls is not None, f"Extension class {cls_name} not found"
        return cls(*args, **kwargs)
```

### \_\_init\__ [¶](#vllm.utils.registry.ExtensionManager.__init__ "Permanent link")

Initialize an empty extension registry.

Source code in `vllm/utils/registry.py`

```
def__init__(self) -> None:
"""
    Initialize an empty extension registry.
    """
    self.name2class: dict[str, type] = {}
```

### load [¶](#vllm.utils.registry.ExtensionManager.load "Permanent link")

```
load(cls_name: str, *args, **kwargs) -> Any
```

Instantiate and return a registered extension class by name.

Source code in `vllm/utils/registry.py`

```
defload(self, cls_name: str, *args, **kwargs) -> Any:
"""
    Instantiate and return a registered extension class by name.
    """
    cls = self.name2class.get(cls_name)
    assert cls is not None, f"Extension class {cls_name} not found"
    return cls(*args, **kwargs)
```

### register [¶](#vllm.utils.registry.ExtensionManager.register "Permanent link")

Decorator to register a class with the given name.

Source code in `vllm/utils/registry.py`

```
defregister(self, name: str):
"""
    Decorator to register a class with the given name.
    """

    defwrap(cls_to_register: _T) -> _T:
        self.name2class[name] = cls_to_register
        return cls_to_register

    return wrap
```