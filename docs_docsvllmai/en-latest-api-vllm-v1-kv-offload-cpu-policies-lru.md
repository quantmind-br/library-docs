---
title: lru - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/kv_offload/cpu/policies/lru/
source: sitemap
fetched_at: 2026-05-07T21:41:02.042122899-03:00
rendered_js: false
word_count: 18
summary: This document defines the LRUCachePolicy class, which implements a Least Recently Used cache strategy for managing KV cache offloading in vLLM.
tags:
    - vllm
    - kv-cache
    - lru-cache
    - memory-management
    - caching-policy
category: reference
---

## vllm.v1.kv\_offload.cpu.policies.lru [¶](#vllm.v1.kv_offload.cpu.policies.lru "Permanent link")

## LRUCachePolicy [¶](#vllm.v1.kv_offload.cpu.policies.lru.LRUCachePolicy "Permanent link")

Bases: `CachePolicy`

LRU cache policy backed by a single OrderedDict.

Source code in `vllm/v1/kv_offload/cpu/policies/lru.py`

```
classLRUCachePolicy(CachePolicy):
"""LRU cache policy backed by a single OrderedDict."""

    def__init__(self, cache_capacity: int):
        # cache_capacity unused by LRU but accepted for a uniform constructor
        self.blocks: OrderedDict[OffloadKey, BlockStatus] = OrderedDict()

    defget(self, key: OffloadKey) -> BlockStatus | None:
        return self.blocks.get(key)

    definsert(self, key: OffloadKey, block: BlockStatus) -> None:
        self.blocks[key] = block

    defremove(self, key: OffloadKey) -> None:
        del self.blocks[key]

    deftouch(self, keys: Iterable[OffloadKey]) -> None:
        for key in reversed(list(keys)):
            if key in self.blocks:
                self.blocks.move_to_end(key)

    defevict(
        self, n: int, protected: set[OffloadKey]
    ) -> list[tuple[OffloadKey, BlockStatus]] | None:
        if n == 0:
            return []
        candidates: list[tuple[OffloadKey, BlockStatus]] = []
        for key, block in self.blocks.items():
            if block.ref_cnt == 0 and key not in protected:
                candidates.append((key, block))
                if len(candidates) == n:
                    break
        if len(candidates) < n:
            return None
        for key, _ in candidates:
            del self.blocks[key]
        return candidates
```