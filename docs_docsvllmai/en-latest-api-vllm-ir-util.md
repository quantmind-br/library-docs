---
title: util - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/ir/util/
source: sitemap
fetched_at: 2026-05-07T21:22:07.861511412-03:00
rendered_js: false
word_count: 81
summary: Provides utility functions for hashing object source code and implementing memory-efficient caching using weak references.
tags:
    - python-utilities
    - caching-mechanisms
    - source-hashing
    - memory-management
    - weak-references
category: api
---

## hash\_source [¶](#vllm.ir.util.hash_source "Permanent link")

Utility method to hash the sources of functions or objects. :param srcs: strings or objects to add to the hash. Objects and functions have their source inspected. :return:

Source code in `vllm/ir/util.py`

```
defhash_source(*srcs: str | Any) -> str:
"""
    Utility method to hash the sources of functions or objects.
    :param srcs: strings or objects to add to the hash.
    Objects and functions have their source inspected.
    :return:
    """
    hasher = hashlib.sha256()
    for src in srcs:
        if src is None:
            src_str = "None"
        elif isinstance(src, str):
            src_str = src
        elif isinstance(src, Path):
            src_str = src.read_text()
        elif isinstance(src, (types.FunctionType, type)):
            src_str = inspect.getsource(src)
        else:
            # object instance
            src_str = inspect.getsource(src.__class__)
        hasher.update(src_str.encode("utf-8"))
    return hasher.hexdigest()
```

## weak\_cache [¶](#vllm.ir.util.weak_cache "Permanent link")

```
weak_cache(user_function)
```

Simple weak equivalent to functools.cache

Source code in `vllm/ir/util.py`

```
defweak_cache(user_function, /):
"""Simple weak equivalent to functools.cache"""
    return weak_lru_cache(maxsize=None)(user_function)
```

## weak\_lru\_cache [¶](#vllm.ir.util.weak_lru_cache "Permanent link")

```
weak_lru_cache(
    maxsize: int | None = 128, typed: bool = False
)
```

LRU Cache decorator that keeps a weak reference to 'self'. This avoids memory leakage, which happens when functools.lru\_cache stores a reference to self in the global cache.

Taken from: https://stackoverflow.com/a/68052994/5082708

Source code in `vllm/ir/util.py`

```
defweak_lru_cache(maxsize: int | None = 128, typed: bool = False):
"""
    LRU Cache decorator that keeps a weak reference to 'self'.
    This avoids memory leakage, which happens when functools.lru_cache
    stores a reference to self in the global cache.

    Taken from: https://stackoverflow.com/a/68052994/5082708
    """

    defwrapper(func):
        @functools.lru_cache(maxsize, typed)
        def_func(_self, *args, **kwargs):
            return func(_self(), *args, **kwargs)

        @functools.wraps(func)
        definner(self, *args, **kwargs):
            return _func(weakref.ref(self), *args, **kwargs)

        return inner

    return wrapper
```