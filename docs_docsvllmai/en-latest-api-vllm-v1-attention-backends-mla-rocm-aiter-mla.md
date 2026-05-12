---
title: rocm_aiter_mla - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/attention/backends/mla/rocm_aiter_mla/
source: sitemap
fetched_at: 2026-05-07T21:39:33.82118646-03:00
rendered_js: false
word_count: 83
summary: This document describes a Triton kernel implementation designed to map block-level KV cache indices into individual token positions for the aiter MLA architecture.
tags:
    - triton-kernel
    - vllm
    - kv-cache
    - mla
    - gpu-programming
    - memory-mapping
category: reference
---

```
_expand_page_indices_kernel(
    page_indices,
    block_table,
    block_table_stride,
    cu_num_tokens,
    seq_lens,
    KERNEL_BLOCK_SIZE: constexpr,
    BLOCK_SIZE: constexpr,
)
```

Expand block table entries into per-token flat page indices.

The aiter MLA kernel always operates with page\_size=1 internally (kv\_buffer is flattened via .view(-1, 1, 1, H)). This kernel converts block-level indices from the block table into individual token positions in the flattened KV buffer.

When KERNEL\_BLOCK\_SIZE=1: block\_idx=t, offset=0, flat=block\_id (equivalent to a direct copy -- no regression from the original kernel).

When KERNEL\_BLOCK\_SIZE=K: block table entry b (covering K tokens) is expanded to flat indices b*K, b*K+1, ..., b\*K+(K-1).

Source code in `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`

```
@triton.jit
def_expand_page_indices_kernel(
    page_indices,
    block_table,
    block_table_stride,
    cu_num_tokens,
    seq_lens,
    KERNEL_BLOCK_SIZE: tl.constexpr,
    BLOCK_SIZE: tl.constexpr,
):
"""Expand block table entries into per-token flat page indices.

    The aiter MLA kernel always operates with page_size=1 internally
    (kv_buffer is flattened via .view(-1, 1, 1, H)). This kernel converts
    block-level indices from the block table into individual token positions
    in the flattened KV buffer.

    When KERNEL_BLOCK_SIZE=1: block_idx=t, offset=0, flat=block_id
    (equivalent to a direct copy -- no regression from the original kernel).

    When KERNEL_BLOCK_SIZE=K: block table entry b (covering K tokens)
    is expanded to flat indices b*K, b*K+1, ..., b*K+(K-1).
    """
    req_idx = tl.program_id(0)
    row_ptr = block_table + req_idx * block_table_stride
    start_idx = tl.load(cu_num_tokens + req_idx)
    num_tokens = tl.load(seq_lens + req_idx)

    offset = tl.arange(0, BLOCK_SIZE)
    for i in tl.range(0, num_tokens, BLOCK_SIZE):
        token_offsets = i + offset
        mask = token_offsets < num_tokens

        # Which block in the block table does this token belong to?
        block_idx = token_offsets // KERNEL_BLOCK_SIZE
        # Offset within that block
        offset_in_block = token_offsets % KERNEL_BLOCK_SIZE

        # Load the block ID from the block table
        block_ids = tl.load(row_ptr + block_idx, mask=mask)

        # Compute flat index in the flattened kv_buffer
        flat_indices = block_ids * KERNEL_BLOCK_SIZE + offset_in_block

        tl.store(
            page_indices + start_idx + token_offsets,
            flat_indices,
            mask=mask,
        )
```