---
title: inductor_pass - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/inductor_pass/
source: sitemap
fetched_at: 2026-05-07T21:16:35.123144454-03:00
rendered_js: false
word_count: 235
summary: This document defines base classes and utility functions for implementing custom compiler passes within the vLLM Inductor framework, including mechanisms for unique identifier generation and execution context management.
tags:
    - vllm
    - compiler-passes
    - inductor
    - graph-compilation
    - hash-utility
    - fake-tensor-mode
category: reference
---

## CallableInductorPass [¶](#vllm.compilation.passes.inductor_pass.CallableInductorPass "Permanent link")

Bases: `InductorPass`

This class is a wrapper for a callable that automatically provides an implementation of the UUID.

Source code in `vllm/compilation/passes/inductor_pass.py`

```
classCallableInductorPass(InductorPass):
"""
    This class is a wrapper for a callable that automatically provides an
    implementation of the UUID.
    """

    def__init__(
        self, callable: Callable[[fx.Graph], None], uuid: Any | None = None
    ) -> None:
        self.callable = callable
        self._uuid = self.hash_source(callable) if uuid is None else uuid

    def__call__(self, graph: torch.fx.Graph) -> None:
        self.callable(graph)

    defuuid(self) -> Any:
        return self._uuid
```

## InductorPass [¶](#vllm.compilation.passes.inductor_pass.InductorPass "Permanent link")

Bases: `CustomGraphPass`

A custom graph pass that uses a hash of its source as the UUID. This is defined as a convenience and should work in most cases.

Source code in `vllm/compilation/passes/inductor_pass.py`

```
classInductorPass(CustomGraphPass):  # type: ignore[misc]
"""
    A custom graph pass that uses a hash of its source as the UUID.
    This is defined as a convenience and should work in most cases.
    """

    defuuid(self) -> str:
"""
        Provide a unique identifier for the pass, used in Inductor code cache.
        This should depend on the pass implementation, so that changes to the
        pass result in recompilation.
        By default, the object source is hashed.
        """
        return InductorPass.hash_source(self)

    @staticmethod
    defhash_source(*srcs: str | Any) -> str:
"""
        Utility method to hash the sources of functions or objects.
        :param srcs: strings or objects to add to the hash.
        Objects and functions have their source inspected.
        Results are cached by resolved types to avoid repeated
        inspect.getsource() calls.
        :return:
        """
        # Resolve instances to their class for a hashable cache key.
        cache_key = tuple(
            src if isinstance(src, (str, type, types.FunctionType)) else src.__class__
            for src in srcs
        )
        return _hash_source_cached(*cache_key)

    @staticmethod
    defhash_dict(dict_: dict[Any, Any]) -> str:
"""
        Utility method to hash a dictionary, can alternatively be used for uuid.
        :return: A sha256 hash of the json rep of the dictionary.
        """
        encoded = json.dumps(dict_, sort_keys=True).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()

    defis_applicable_for_range(self, compile_range: Range) -> bool:
        return True
```

### hash\_dict `staticmethod` [¶](#vllm.compilation.passes.inductor_pass.InductorPass.hash_dict "Permanent link")

Utility method to hash a dictionary, can alternatively be used for uuid. :return: A sha256 hash of the json rep of the dictionary.

Source code in `vllm/compilation/passes/inductor_pass.py`

```
@staticmethod
defhash_dict(dict_: dict[Any, Any]) -> str:
"""
    Utility method to hash a dictionary, can alternatively be used for uuid.
    :return: A sha256 hash of the json rep of the dictionary.
    """
    encoded = json.dumps(dict_, sort_keys=True).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()
```

### hash\_source `staticmethod` [¶](#vllm.compilation.passes.inductor_pass.InductorPass.hash_source "Permanent link")

Utility method to hash the sources of functions or objects. :param srcs: strings or objects to add to the hash. Objects and functions have their source inspected. Results are cached by resolved types to avoid repeated inspect.getsource() calls. :return:

Source code in `vllm/compilation/passes/inductor_pass.py`

```
@staticmethod
defhash_source(*srcs: str | Any) -> str:
"""
    Utility method to hash the sources of functions or objects.
    :param srcs: strings or objects to add to the hash.
    Objects and functions have their source inspected.
    Results are cached by resolved types to avoid repeated
    inspect.getsource() calls.
    :return:
    """
    # Resolve instances to their class for a hashable cache key.
    cache_key = tuple(
        src if isinstance(src, (str, type, types.FunctionType)) else src.__class__
        for src in srcs
    )
    return _hash_source_cached(*cache_key)
```

### uuid [¶](#vllm.compilation.passes.inductor_pass.InductorPass.uuid "Permanent link")

Provide a unique identifier for the pass, used in Inductor code cache. This should depend on the pass implementation, so that changes to the pass result in recompilation. By default, the object source is hashed.

Source code in `vllm/compilation/passes/inductor_pass.py`

```
defuuid(self) -> str:
"""
    Provide a unique identifier for the pass, used in Inductor code cache.
    This should depend on the pass implementation, so that changes to the
    pass result in recompilation.
    By default, the object source is hashed.
    """
    return InductorPass.hash_source(self)
```

## enable\_fake\_mode [¶](#vllm.compilation.passes.inductor_pass.enable_fake_mode "Permanent link")

Applies a FakeTensorMode context. This is useful when you don't want to create or run things with real tensors.

Source code in `vllm/compilation/passes/inductor_pass.py`

```
defenable_fake_mode(fn: Callable[P, R]) -> Callable[P, R]:
"""
    Applies a FakeTensorMode context. This is useful when you don't want to
    create or run things with real tensors.
    """

    @functools.wraps(fn)
    deffn_new(*args: P.args, **kwargs: P.kwargs) -> R:
        with torch._guards.tracing(None), unset_fake_temporarily(), FakeTensorMode():
            result = fn(*args, **kwargs)

        return result

    return fn_new
```

## get\_pass\_context [¶](#vllm.compilation.passes.inductor_pass.get_pass_context "Permanent link")

```
get_pass_context() -> PassContext
```

Get the current pass context.

Source code in `vllm/compilation/passes/inductor_pass.py`

```
defget_pass_context() -> PassContext:
"""Get the current pass context."""
    assert _pass_context is not None
    return _pass_context
```

## pass\_context [¶](#vllm.compilation.passes.inductor_pass.pass_context "Permanent link")

A context manager that stores the current pass context, usually it is a list of sizes to specialize.

Source code in `vllm/compilation/passes/inductor_pass.py`

```
@contextmanager
defpass_context(compile_range: Range) -> Generator[None, None, None]:
"""A context manager that stores the current pass context,
    usually it is a list of sizes to specialize.
    """
    global _pass_context
    prev_context = _pass_context
    _pass_context = PassContext(compile_range)
    try:
        yield
    finally:
        _pass_context = prev_context
```