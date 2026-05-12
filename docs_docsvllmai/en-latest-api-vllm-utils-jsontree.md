---
title: jsontree - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/utils/jsontree/
source: sitemap
fetched_at: 2026-05-07T21:38:41.712953128-03:00
rendered_js: false
word_count: 121
summary: This document provides a set of utility functions for traversing, counting, mapping, and reducing leaf nodes within nested JSON-like data structures.
tags:
    - json-utilities
    - data-processing
    - python-utils
    - nested-structures
    - recursive-functions
category: reference
---

## vllm.utils.jsontree [¶](#vllm.utils.jsontree "Permanent link")

Helper functions to work with nested JSON structures.

## JSONTree `module-attribute` [¶](#vllm.utils.jsontree.JSONTree "Permanent link")

A nested JSON structure where the leaves need not be JSON-serializable.

## \_JSONTree `module-attribute` [¶](#vllm.utils.jsontree._JSONTree "Permanent link")

Same as `JSONTree` but with additional `Union` members to satisfy overloads.

## json\_count\_leaves [¶](#vllm.utils.jsontree.json_count_leaves "Permanent link")

```
json_count_leaves(value: JSONTree[_T]) -> int
```

Count the number of leaves in a nested JSON structure.

Source code in `vllm/utils/jsontree.py`

```
defjson_count_leaves(value: JSONTree[_T]) -> int:
"""Count the number of leaves in a nested JSON structure."""
    return sum(1 for _ in json_iter_leaves(value))
```

## json\_iter\_leaves [¶](#vllm.utils.jsontree.json_iter_leaves "Permanent link")

```
json_iter_leaves(value: JSONTree[_T]) -> Iterable[_T]
```

Iterate through each leaf in a nested JSON structure.

Source code in `vllm/utils/jsontree.py`

```
defjson_iter_leaves(value: JSONTree[_T]) -> Iterable[_T]:
"""Iterate through each leaf in a nested JSON structure."""
    if isinstance(value, dict):
        for v in value.values():
            yield from json_iter_leaves(v)
    elif isinstance(value, (list, tuple)):
        for v in value:
            yield from json_iter_leaves(v)
    else:
        yield value
```

## json\_map\_leaves [¶](#vllm.utils.jsontree.json_map_leaves "Permanent link")

```
json_map_leaves(
    func: Callable[[_T], _U], value: _T | list[_T]
) -> _U | list[_U]

json_map_leaves(
    func: Callable[[_T], _U], value: _T | tuple[_T, ...]
) -> _U | tuple[_U, ...]

json_map_leaves(
    func: Callable[[_T], _U], value: JSONTree[_T]
) -> JSONTree[_U]
```

Apply a function to each leaf in a nested JSON structure.

Source code in `vllm/utils/jsontree.py`

```
defjson_map_leaves(
    func: Callable[[_T], _U],
    value: Any,
) -> "BatchedTensorInputs" | _JSONTree[_U]:
"""Apply a function to each leaf in a nested JSON structure."""
    if isinstance(value, dict):
        return {k: json_map_leaves(func, v) for k, v in value.items()}  # type: ignore
    elif isinstance(value, list):
        return [json_map_leaves(func, v) for v in value]  # type: ignore
    elif isinstance(value, tuple):
        return tuple(json_map_leaves(func, v) for v in value)
    else:
        return func(value)
```

## json\_reduce\_leaves [¶](#vllm.utils.jsontree.json_reduce_leaves "Permanent link")

```
json_reduce_leaves(
    func: Callable[[_T, _T], _T], value: _T | dict[str, _T]
) -> _T

json_reduce_leaves(
    func: Callable[[_T, _T], _T], value: _T | list[_T]
) -> _T

json_reduce_leaves(
    func: Callable[[_T, _T], _T], value: _T | tuple[_T, ...]
) -> _T

json_reduce_leaves(
    func: Callable[[_T, _T], _T], value: JSONTree[_T]
) -> _T

json_reduce_leaves(
    func: Callable[[_U, _T], _U],
    value: JSONTree[_T],
    initial: _U,
) -> _U

json_reduce_leaves(
    func: Callable[[_T, _T], _T] | Callable[[_U, _T], _U],
    value: _JSONTree[_T],
    initial: _U = ...,
) -> _T | _U
```

Apply a function of two arguments cumulatively to each leaf in a nested JSON structure, from left to right, so as to reduce the sequence to a single value.

Source code in `vllm/utils/jsontree.py`

```
defjson_reduce_leaves(
    func: Callable[[_T, _T], _T] | Callable[[_U, _T], _U],
    value: _JSONTree[_T],
    initial: _U = ...,  # type: ignore[assignment]
    /,
) -> _T | _U:
"""
    Apply a function of two arguments cumulatively to each leaf in a
    nested JSON structure, from left to right, so as to reduce the
    sequence to a single value.
    """
    if initial is ...:
        return reduce(func, json_iter_leaves(value))  # type: ignore

    return reduce(func, json_iter_leaves(value), initial)  # type: ignore
```