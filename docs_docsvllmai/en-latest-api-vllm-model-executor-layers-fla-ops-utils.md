---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fla/ops/utils/
source: sitemap
fetched_at: 2026-05-07T21:24:27.84000743-03:00
rendered_js: false
word_count: 124
summary: This document describes utility decorators designed to manage tensor operations, specifically for ensuring input contiguity, setting execution devices, and implementing result caching for tensor-based functions.
tags:
    - python
    - decorators
    - tensor-processing
    - caching-mechanism
    - vllm-utilities
    - memory-management
category: reference
---

## input\_guard [¶](#vllm.model_executor.layers.fla.ops.utils.input_guard "Permanent link")

A decorator to make sure all input tensors are contiguous and set the device based on input tensors.

Source code in `vllm/model_executor/layers/fla/ops/utils.py`

```
definput_guard(fn: Callable[..., torch.Tensor]) -> Callable[..., torch.Tensor]:
"""
    A decorator to make sure all input tensors are contiguous and set the device based on input tensors.
    """

    @functools.wraps(fn)
    defwrapper(*args, **kwargs):
        contiguous_args = (
            i if not isinstance(i, torch.Tensor) else i.contiguous() for i in args
        )
        contiguous_kwargs = {
            k: (v if not isinstance(v, torch.Tensor) else v.contiguous())
            for k, v in kwargs.items()
        }

        tensor = None
        for arg in args:
            if isinstance(arg, torch.Tensor):
                tensor = arg
                break
        if tensor is None:
            for value in kwargs.values():
                if isinstance(value, torch.Tensor):
                    tensor = value
                    break

        if tensor is not None:
            ctx = torch.accelerator.device_index(tensor.device.index)
        else:
            ctx = contextlib.nullcontext()

        with ctx:
            return fn(*contiguous_args, **contiguous_kwargs)

    return wrapper
```

## tensor\_cache [¶](#vllm.model_executor.layers.fla.ops.utils.tensor_cache "Permanent link")

A decorator that caches the most recent results of a function with tensor inputs.

This decorator will store the output of the decorated function for the most recent set of input tensors. The cache is limited to a fixed size (default is 4). When the cache is full, the oldest entry will be removed.

Parameters:

Name Type Description Default `fn` `Callable[..., Tensor]`

The function to be decorated. It should take tensor inputs and return tensor outputs.

*required*

Returns:

Type Description `Callable[..., Tensor]`

Callable\[..., torch.Tensor]: A wrapped version of the input function with single-entry caching.

Source code in `vllm/model_executor/layers/fla/ops/utils.py`

```
deftensor_cache(fn: Callable[..., torch.Tensor]) -> Callable[..., torch.Tensor]:
"""
    A decorator that caches the most recent results of a function with tensor inputs.

    This decorator will store the output of the decorated function for the most recent set of input tensors.
    The cache is limited to a fixed size (default is 4). When the cache is full, the oldest entry will be removed.

    Args:
        fn (Callable[..., torch.Tensor]):
            The function to be decorated. It should take tensor inputs and return tensor outputs.

    Returns:
        Callable[..., torch.Tensor]:
            A wrapped version of the input function with single-entry caching.
    """

    cache_entries: tuple[tuple | None, dict | None, Any] = []
    cache_size = 8

    @functools.wraps(fn)
    defwrapper(*args: Any, **kwargs: Any) -> Any:
        nonlocal cache_entries, cache_size
        for i, entry in enumerate(cache_entries):
            last_args, last_kwargs, last_result = entry
            if (
                len(args) == len(last_args)
                and len(kwargs) == len(last_kwargs)
                and all(a is b for a, b in zip(args, last_args))
                and all(
                    k in last_kwargs and v is last_kwargs[k] for k, v in kwargs.items()
                )
            ):
                cache_entries = (
                    cache_entries[:i]
                    + cache_entries[i + 1 :]
                    + [(args, kwargs, last_result)]
                )
                return last_result

        result = fn(*args, **kwargs)

        if len(cache_entries) >= cache_size:
            cache_entries = cache_entries[1:]
        cache_entries.append((args, kwargs, result))
        return result

    return wrapper
```