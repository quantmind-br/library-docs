---
title: func_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/utils/func_utils/
source: sitemap
fetched_at: 2026-05-07T21:38:37.263313293-03:00
rendered_js: false
word_count: 227
summary: This document describes utility functions for inspecting callable signatures and filtering keyword arguments to ensure they are compatible with specific function requirements.
tags:
    - python-utilities
    - function-inspection
    - keyword-arguments
    - introspection
    - callable-signature
category: reference
---

Contains helpers that are applied to functions.

This is similar in concept to the `functools` module.

## \_supports\_kw `cached` [¶](#vllm.utils.func_utils._supports_kw "Permanent link")

Internal cached implementation of supports\_kw.

Source code in `vllm/utils/func_utils.py`

```
@lru_cache
def_supports_kw(
    callable: Callable[..., object],
    kw_name: str,
    *,
    requires_kw_only: bool = False,
    allow_var_kwargs: bool = True,
) -> bool:
"""Internal cached implementation of supports_kw."""
    params = inspect.signature(callable).parameters
    if not params:
        return False

    param_val = params.get(kw_name)

    # Types where the it may be valid, i.e., explicitly defined & nonvariadic
    passable_kw_types = set(
        (
            inspect.Parameter.POSITIONAL_ONLY,
            inspect.Parameter.POSITIONAL_OR_KEYWORD,
            inspect.Parameter.KEYWORD_ONLY,
        )
    )

    if param_val:
        is_sig_param = param_val.kind in passable_kw_types
        # We want kwargs only, but this is passable as a positional arg
        if (
            requires_kw_only
            and is_sig_param
            and param_val.kind != inspect.Parameter.KEYWORD_ONLY
        ):
            return False
        if (requires_kw_only and param_val.kind == inspect.Parameter.KEYWORD_ONLY) or (
            not requires_kw_only and is_sig_param
        ):
            return True

    # If we're okay with var-kwargs, it's supported as long as
    # the kw_name isn't something like *args, **kwargs
    if allow_var_kwargs:
        # Get the last param; type is ignored here because params is a proxy
        # mapping, but it wraps an ordered dict, and they appear in order.
        # Ref: https://docs.python.org/3/library/inspect.html#inspect.Signature.parameters
        last_param = params[next(reversed(params))]  # type: ignore
        return (
            last_param.kind == inspect.Parameter.VAR_KEYWORD
            and last_param.name != kw_name
        )

    return False
```

## get\_allowed\_kwarg\_only\_overrides [¶](#vllm.utils.func_utils.get_allowed_kwarg_only_overrides "Permanent link")

Given a callable which has one or more keyword only params and a dict mapping param names to values, drop values that can be not be kwarg expanded to overwrite one or more keyword-only args. This is used in a few places to handle custom processor overrides for multimodal models, e.g., for profiling when processor options provided by the user may affect the number of mm tokens per instance.

Parameters:

Name Type Description Default `callable` `Callable[..., object]`

Callable which takes 0 or more keyword only arguments. If None is provided, all overrides names are allowed.

*required* `overrides` `Mapping[str, object] | None`

Potential overrides to be used when invoking the callable.

*required* `allow_var_kwargs` `bool`

Allows overrides that are expandable for var kwargs.

`False`

Returns:

Type Description `dict[str, Any]`

Dictionary containing the kwargs to be leveraged which may be used

`dict[str, Any]`

to overwrite one or more keyword only arguments when invoking the

`dict[str, Any]`

callable.

Source code in `vllm/utils/func_utils.py`

```
defget_allowed_kwarg_only_overrides(
    callable: Callable[..., object],
    overrides: Mapping[str, object] | None,
    *,
    requires_kw_only: bool = True,
    allow_var_kwargs: bool = False,
) -> dict[str, Any]:
"""
    Given a callable which has one or more keyword only params and a dict
    mapping param names to values, drop values that can be not be kwarg
    expanded to overwrite one or more keyword-only args. This is used in a
    few places to handle custom processor overrides for multimodal models,
    e.g., for profiling when processor options provided by the user
    may affect the number of mm tokens per instance.

    Args:
        callable: Callable which takes 0 or more keyword only arguments.
                  If None is provided, all overrides names are allowed.
        overrides: Potential overrides to be used when invoking the callable.
        allow_var_kwargs: Allows overrides that are expandable for var kwargs.

    Returns:
        Dictionary containing the kwargs to be leveraged which may be used
        to overwrite one or more keyword only arguments when invoking the
        callable.
    """
    if not overrides:
        return {}

    # Drop any mm_processor_kwargs provided by the user that
    # are not kwargs, unless it can fit it var_kwargs param
    filtered_overrides = {
        kwarg_name: val
        for kwarg_name, val in overrides.items()
        if supports_kw(
            callable,
            kwarg_name,
            requires_kw_only=requires_kw_only,
            allow_var_kwargs=allow_var_kwargs,
        )
    }

    # If anything is dropped, log a warning
    dropped_keys = overrides.keys() - filtered_overrides.keys()
    if dropped_keys:
        if requires_kw_only:
            logger.warning(
                "The following intended overrides are not keyword-only args "
                "and will be dropped: %s",
                dropped_keys,
            )
        else:
            logger.warning(
                "The following intended overrides are not keyword args "
                "and will be dropped: %s",
                dropped_keys,
            )

    return filtered_overrides
```

## identity [¶](#vllm.utils.func_utils.identity "Permanent link")

```
identity(value: T, **kwargs) -> T
```

Returns the first provided value.

Source code in `vllm/utils/func_utils.py`

```
defidentity(value: T, **kwargs) -> T:
"""Returns the first provided value."""
    return value
```

## supports\_kw [¶](#vllm.utils.func_utils.supports_kw "Permanent link")

Check if a keyword is a valid kwarg for a callable; if requires\_kw\_only disallows kwargs names that can also be positional arguments.

Source code in `vllm/utils/func_utils.py`

```
defsupports_kw(
    callable: Callable[..., object],
    kw_name: str,
    *,
    requires_kw_only: bool = False,
    allow_var_kwargs: bool = True,
) -> bool:
"""Check if a keyword is a valid kwarg for a callable; if requires_kw_only
    disallows kwargs names that can also be positional arguments.
    """
    # Unwrap bound methods so that the lru_cache key is the underlying
    # function, not the instance. Caching bound methods pins the object
    # (and all its GPU tensors) for the lifetime of the cache.
    if hasattr(callable, "__func__"):
        callable = callable.__func__
    return _supports_kw(
        callable,
        kw_name,
        requires_kw_only=requires_kw_only,
        allow_var_kwargs=allow_var_kwargs,
    )
```