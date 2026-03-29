---
title: configure_cache - DSPy
url: https://dspy.ai/api/utils/configure_cache/
source: sitemap
fetched_at: 2026-01-23T08:02:58.594548712-03:00
rendered_js: false
word_count: 130
summary: This document describes the dspy.configure_cache function, which is used to manage settings for on-disk and in-memory caching within the DSPy framework.
tags:
    - dspy
    - cache-management
    - disk-cache
    - memory-cache
    - api-configuration
    - optimization
category: api
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/utils/configure_cache.md "Edit this page")

## `dspy.configure_cache(enable_disk_cache: bool | None = True, enable_memory_cache: bool | None = True, disk_cache_dir: str | None = DISK_CACHE_DIR, disk_size_limit_bytes: int | None = DISK_CACHE_LIMIT, memory_max_entries: int = 1000000)` [¶](#dspy.configure_cache "Permanent link")

Configure the cache for DSPy.

Parameters:

Name Type Description Default `enable_disk_cache` `bool | None`

Whether to enable on-disk cache.

`True` `enable_memory_cache` `bool | None`

Whether to enable in-memory cache.

`True` `disk_cache_dir` `str | None`

The directory to store the on-disk cache.

`DISK_CACHE_DIR` `disk_size_limit_bytes` `int | None`

The size limit of the on-disk cache.

`DISK_CACHE_LIMIT` `memory_max_entries` `int`

The maximum number of entries in the in-memory cache. To allow the cache to grow without bounds, set this parameter to `math.inf` or a similar value.

`1000000`

Source code in `dspy/clients/__init__.py`

```
defconfigure_cache(
    enable_disk_cache: bool | None = True,
    enable_memory_cache: bool | None = True,
    disk_cache_dir: str | None = DISK_CACHE_DIR,
    disk_size_limit_bytes: int | None = DISK_CACHE_LIMIT,
    memory_max_entries: int = 1000000,
):
"""Configure the cache for DSPy.

    Args:
        enable_disk_cache: Whether to enable on-disk cache.
        enable_memory_cache: Whether to enable in-memory cache.
        disk_cache_dir: The directory to store the on-disk cache.
        disk_size_limit_bytes: The size limit of the on-disk cache.
        memory_max_entries: The maximum number of entries in the in-memory cache. To allow the cache to grow without
                            bounds, set this parameter to `math.inf` or a similar value.
    """

    DSPY_CACHE = Cache(
        enable_disk_cache,
        enable_memory_cache,
        disk_cache_dir,
        disk_size_limit_bytes,
        memory_max_entries,
    )

    importdspy

    # Update the reference to point to the new cache
    dspy.cache = DSPY_CACHE
```

:::