---
title: base - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/kv_offload/base/
source: sitemap
fetched_at: 2026-05-07T21:40:54.372034408-03:00
rendered_js: false
word_count: 158
summary: This document defines the specification for loading and storing KV cache blocks to GPU memory within the vLLM architecture, including support for grouped KV caches and unaligned block offloading.
tags:
    - vllm
    - kv-cache
    - gpu-memory
    - memory-management
    - block-storage
    - tensor-parallelism
category: reference
---

Bases: `BlockIDsLoadStoreSpec`

Spec for loading/storing a KV block to GPU memory.

If there are multiple KV groups, the blocks are expected to be ordered by the group index. In that case, group\_sizes\[i] determines the number of blocks per the i-th KV group, and thus sum(group\_sizes) == len(block\_ids). group\_sizes=None indicates a single KV group.

If block\_indices is given, each group (determined by group\_sizes) of block IDs will correspond to logically contiguous blocks, e.g. blocks 5-10 of a some request. block\_indices\[i] will represent the block index of the first block in group #i. Thus, len(block\_indices) == len(group\_sizes) = number of KV cache groups. This information is required in order to support off/loading from offloaded blocks which are larger than GPU blocks. In such cases, the first GPU block per each group may be unaligned to the offloaded block size, and so knowing block\_indices\[i] allows the worker to correctly skip part of the first matching offloaded block.

Source code in `vllm/v1/kv_offload/base.py`

```
classGPULoadStoreSpec(BlockIDsLoadStoreSpec):
"""
    Spec for loading/storing a KV block to GPU memory.

    If there are multiple KV groups, the blocks are expected to be
    ordered by the group index.
    In that case, group_sizes[i] determines the number of blocks
    per the i-th KV group, and thus sum(group_sizes) == len(block_ids).
    group_sizes=None indicates a single KV group.

    If block_indices is given, each group (determined by group_sizes) of block IDs
    will correspond to logically contiguous blocks, e.g. blocks 5-10 of a some request.
    block_indices[i] will represent the block index of the first block in group #i.
    Thus, len(block_indices) == len(group_sizes) = number of KV cache groups.
    This information is required in order to support off/loading from offloaded blocks
    which are larger than GPU blocks.
    In such cases, the first GPU block per each group may be unaligned to the offloaded
    block size, and so knowing block_indices[i] allows the worker to correctly
    skip part of the first matching offloaded block.
    """

    def__init__(
        self,
        block_ids: list[int],
        group_sizes: Sequence[int],
        block_indices: Sequence[int],
    ):
        super().__init__(block_ids)
        assert sum(group_sizes) == len(block_ids)
        assert len(block_indices) == len(group_sizes)
        self.group_sizes: Sequence[int] = group_sizes
        self.block_indices: Sequence[int] = block_indices

    @staticmethod
    defmedium() -> str:
        return "GPU"
```