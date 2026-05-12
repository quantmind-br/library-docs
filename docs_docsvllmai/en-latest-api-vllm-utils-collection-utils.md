---
title: collection_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/utils/collection_utils/
source: sitemap
fetched_at: 2026-05-07T21:38:31.493612255-03:00
rendered_js: false
word_count: 130
summary: This document provides a reference for utility functions designed to perform common operations on collections, such as lazy evaluation, grouping, list manipulation, and data transformation.
tags:
    - collection-utils
    - data-manipulation
    - python-helpers
    - utility-functions
    - lazy-evaluation
category: reference
---

Contains helpers that are applied to collections.

This is similar in concept to the `collections` module.

## LazyDict [¶](#vllm.utils.collection_utils.LazyDict "Permanent link")

Bases: `Mapping[str, _V]`, `Generic[_V]`

Evaluates dictionary items only when they are accessed.

Adapted from: https://stackoverflow.com/a/47212782/5082708

Source code in `vllm/utils/collection_utils.py`

```
classLazyDict(Mapping[str, _V], Generic[_V]):
"""
    Evaluates dictionary items only when they are accessed.

    Adapted from: https://stackoverflow.com/a/47212782/5082708
    """

    def__init__(self, factory: dict[str, Callable[[], _V]]):
        self._factory = factory
        self._dict: dict[str, _V] = {}

    def__getitem__(self, key: str) -> _V:
        if key not in self._dict:
            if key not in self._factory:
                raise KeyError(key)
            self._dict[key] = self._factory[key]()
        return self._dict[key]

    def__setitem__(self, key: str, value: Callable[[], _V]):
        self._factory[key] = value

    def__iter__(self):
        return iter(self._factory)

    def__len__(self):
        return len(self._factory)
```

## as\_list [¶](#vllm.utils.collection_utils.as_list "Permanent link")

Convert iterable to list, unless it's already a list.

Source code in `vllm/utils/collection_utils.py`

```
defas_list(maybe_list: Iterable[T]) -> list[T]:
"""Convert iterable to list, unless it's already a list."""
    return maybe_list if isinstance(maybe_list, list) else list(maybe_list)
```

## chunk\_list [¶](#vllm.utils.collection_utils.chunk_list "Permanent link")

Yield successive chunk\_size chunks from lst.

Source code in `vllm/utils/collection_utils.py`

```
defchunk_list(lst: list[T], chunk_size: int) -> Generator[list[T]]:
"""Yield successive chunk_size chunks from lst."""
    for i in range(0, len(lst), chunk_size):
        yield lst[i : i + chunk_size]
```

## common\_prefix [¶](#vllm.utils.collection_utils.common_prefix "Permanent link")

Find the longest prefix common to all items.

Source code in `vllm/utils/collection_utils.py`

```
defcommon_prefix(items: Sequence[Sequence[T] | str]) -> Sequence[T] | str:
"""Find the longest prefix common to all items."""
    if len(items) == 0:
        return []
    if len(items) == 1:
        return items[0]

    shortest = min(items, key=len)
    if not shortest:
        return shortest[:0]

    for match_len in range(1, len(shortest) + 1):
        match = shortest[:match_len]
        for item in items:
            if item[:match_len] != match:
                return shortest[: match_len - 1]

    return shortest
```

## flatten\_2d\_lists [¶](#vllm.utils.collection_utils.flatten_2d_lists "Permanent link")

Flatten a list of lists to a single list.

Source code in `vllm/utils/collection_utils.py`

```
defflatten_2d_lists(lists: Iterable[Iterable[T]]) -> list[T]:
"""Flatten a list of lists to a single list."""
    return [item for sublist in lists for item in sublist]
```

## full\_groupby [¶](#vllm.utils.collection_utils.full_groupby "Permanent link")

Unlike [`itertools.groupby`](https://docs.python.org/3/library/itertools.html#itertools.groupby), groups are not broken by non-contiguous data.

Source code in `vllm/utils/collection_utils.py`

```
deffull_groupby(values: Iterable[_V], *, key: Callable[[_V], _K]):
"""
    Unlike [`itertools.groupby`][], groups are not broken by
    non-contiguous data.
    """
    groups = defaultdict[_K, list[_V]](list)

    for value in values:
        groups[key(value)].append(value)

    return groups.items()
```

## swap\_dict\_values [¶](#vllm.utils.collection_utils.swap_dict_values "Permanent link")

```
swap_dict_values(
    obj: dict[_K, _V], key1: _K, key2: _K
) -> None
```

Swap values between two keys.

Source code in `vllm/utils/collection_utils.py`

```
defswap_dict_values(obj: dict[_K, _V], key1: _K, key2: _K) -> None:
"""Swap values between two keys."""
    v1 = obj.get(key1)
    v2 = obj.get(key2)
    if v1 is not None:
        obj[key2] = v1
    else:
        obj.pop(key2, None)
    if v2 is not None:
        obj[key1] = v2
    else:
        obj.pop(key1, None)
```