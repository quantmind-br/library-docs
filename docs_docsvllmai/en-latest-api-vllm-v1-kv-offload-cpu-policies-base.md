---
title: base - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/kv_offload/cpu/policies/base/
source: sitemap
fetched_at: 2026-05-07T21:41:01.269307246-03:00
rendered_js: false
word_count: 246
summary: This document defines the base data structures and abstract interface for managing KV cache block offloading and eviction policies within the vLLM system.
tags:
    - vllm
    - kv-cache
    - memory-management
    - cache-eviction
    - python-ctypes
    - data-structures
category: reference
---

## BlockStatus [¶](#vllm.v1.kv_offload.cpu.policies.base.BlockStatus "Permanent link")

Bases: `Structure`

Offloading status for a single block of KV data. Holds the following information:

ref\_cnt - the current number of transfers using this block as a source. A value of -1 indicates the block is not yet ready to be read. block\_id - index of the physical CPU buffer slot.

Source code in `vllm/v1/kv_offload/cpu/policies/base.py`

```
classBlockStatus(ctypes.Structure):
"""
    Offloading status for a single block of KV data.
    Holds the following information:

    ref_cnt - the current number of transfers using this block as a source.
        A value of -1 indicates the block is not yet ready to be read.
    block_id - index of the physical CPU buffer slot.
    """

    _fields_ = [("ref_cnt", ctypes.c_int32), ("block_id", ctypes.c_int64)]

    def__init__(self, block_id: int):
        super().__init__()
        # initialize block as "not ready" (ref_cnt = -1)
        self.ref_cnt = -1
        self.block_id = block_id

    @property
    defis_ready(self) -> bool:
"""
        Returns whether the block is ready to be read.
        """
        return self.ref_cnt >= 0
```

### is\_ready `property` [¶](#vllm.v1.kv_offload.cpu.policies.base.BlockStatus.is_ready "Permanent link")

Returns whether the block is ready to be read.

## CachePolicy [¶](#vllm.v1.kv_offload.cpu.policies.base.CachePolicy "Permanent link")

Bases: `ABC`

Encapsulates both block organization (data structures) and replacement decisions (which block to evict). LRU and ARC differ in both dimensions — ARC's ghost lists and target\_t1\_size live at the intersection of storage and eviction, so they cannot be separated cleanly.

Source code in `vllm/v1/kv_offload/cpu/policies/base.py`

```
classCachePolicy(ABC):
"""
    Encapsulates both block organization (data structures) and replacement
    decisions (which block to evict). LRU and ARC differ in both dimensions —
    ARC's ghost lists and target_t1_size live at the intersection of storage
    and eviction, so they cannot be separated cleanly.
    """

    @abstractmethod
    def__init__(self, cache_capacity: int) -> None: ...

    @abstractmethod
    defget(self, key: OffloadKey) -> BlockStatus | None:
"""Find block in data structures. Returns None if not present."""

    @abstractmethod
    definsert(self, key: OffloadKey, block: BlockStatus) -> None:
"""Add a newly allocated block. For ARC: also removes from ghost lists."""

    @abstractmethod
    defremove(self, key: OffloadKey) -> None:
"""Remove a block (used to clean up after a failed store)."""

    @abstractmethod
    deftouch(self, keys: Iterable[OffloadKey]) -> None:
"""Mark blocks as recently used."""

    @abstractmethod
    defevict(
        self, n: int, protected: set[OffloadKey]
    ) -> list[tuple[OffloadKey, BlockStatus]] | None:
"""
        Evict exactly n blocks, skipping any in protected.

        Returns a list of (key, block) for the evicted blocks,
        or None if n evictions cannot be satisfied. The operation is atomic:
        if None is returned, no state changes are made.

        For ARC: ghost list cleanup (trimming to cache_capacity) is performed
        at the end of a successful eviction.
        """
```

### evict `abstractmethod` [¶](#vllm.v1.kv_offload.cpu.policies.base.CachePolicy.evict "Permanent link")

Evict exactly n blocks, skipping any in protected.

Returns a list of (key, block) for the evicted blocks, or None if n evictions cannot be satisfied. The operation is atomic: if None is returned, no state changes are made.

For ARC: ghost list cleanup (trimming to cache\_capacity) is performed at the end of a successful eviction.

Source code in `vllm/v1/kv_offload/cpu/policies/base.py`

```
@abstractmethod
defevict(
    self, n: int, protected: set[OffloadKey]
) -> list[tuple[OffloadKey, BlockStatus]] | None:
"""
    Evict exactly n blocks, skipping any in protected.

    Returns a list of (key, block) for the evicted blocks,
    or None if n evictions cannot be satisfied. The operation is atomic:
    if None is returned, no state changes are made.

    For ARC: ghost list cleanup (trimming to cache_capacity) is performed
    at the end of a successful eviction.
    """
```

### get `abstractmethod` [¶](#vllm.v1.kv_offload.cpu.policies.base.CachePolicy.get "Permanent link")

```
get(key: OffloadKey) -> BlockStatus | None
```

Find block in data structures. Returns None if not present.

Source code in `vllm/v1/kv_offload/cpu/policies/base.py`

```
@abstractmethod
defget(self, key: OffloadKey) -> BlockStatus | None:
"""Find block in data structures. Returns None if not present."""
```

### insert `abstractmethod` [¶](#vllm.v1.kv_offload.cpu.policies.base.CachePolicy.insert "Permanent link")

```
insert(key: OffloadKey, block: BlockStatus) -> None
```

Add a newly allocated block. For ARC: also removes from ghost lists.

Source code in `vllm/v1/kv_offload/cpu/policies/base.py`

```
@abstractmethod
definsert(self, key: OffloadKey, block: BlockStatus) -> None:
"""Add a newly allocated block. For ARC: also removes from ghost lists."""
```

### remove `abstractmethod` [¶](#vllm.v1.kv_offload.cpu.policies.base.CachePolicy.remove "Permanent link")

```
remove(key: OffloadKey) -> None
```

Remove a block (used to clean up after a failed store).

Source code in `vllm/v1/kv_offload/cpu/policies/base.py`

```
@abstractmethod
defremove(self, key: OffloadKey) -> None:
"""Remove a block (used to clean up after a failed store)."""
```

### touch `abstractmethod` [¶](#vllm.v1.kv_offload.cpu.policies.base.CachePolicy.touch "Permanent link")

```
touch(keys: Iterable[OffloadKey]) -> None
```

Mark blocks as recently used.

Source code in `vllm/v1/kv_offload/cpu/policies/base.py`

```
@abstractmethod
deftouch(self, keys: Iterable[OffloadKey]) -> None:
"""Mark blocks as recently used."""
```