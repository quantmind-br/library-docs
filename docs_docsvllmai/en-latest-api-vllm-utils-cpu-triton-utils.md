---
title: cpu_triton_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/utils/cpu_triton_utils/
source: sitemap
fetched_at: 2026-05-07T21:38:34.401004024-03:00
rendered_js: false
word_count: 0
summary: This function serves as an adapter that bridges Triton kernel interfaces with C++ backend implementations, handling necessary data type conversions and output synchronization.
tags:
    - triton-kernel
    - cpp-adapter
    - data-type-conversion
    - tensor-processing
    - kernel-interface
category: api
---

```
def_copy_and_expand_eagle_inputs_kernel_impl(
    target_token_ids_ptr,
    target_positions_ptr,
    next_token_ids_ptr,
    out_input_ids_ptr,
    out_positions_ptr,
    out_is_rejected_token_mask_ptr,
    out_is_masked_token_mask_ptr,
    out_new_token_indices_ptr,
    out_hidden_state_mapping_ptr,
    query_start_loc_ptr,
    query_end_loc_ptr,
    padding_token_id,
    parallel_drafting_token_id,
    total_input_tokens,
    num_padding_slots_per_request,
    shift_input_ids,
    BLOCK_SIZE_TOKENS=None,
    BLOCK_SIZE_REQS=None,
):
"""Adapter between Triton kernel call convention and C++ implementation.

    The Triton kernel uses '_ptr' suffixed parameter names and compile-time
    constants (BLOCK_SIZE_TOKENS, BLOCK_SIZE_REQS) which are not needed by
    the C++ implementation. C++ reads token id tensors as int64_t*.
    Output tensors that are int32 need copy-back after C++ writes int64.
    """
    orig_ids_dtype = out_input_ids_ptr.dtype
    orig_pos_dtype = out_positions_ptr.dtype
    out_ids_i64 = _ensure_int64(out_input_ids_ptr)
    out_pos_i64 = _ensure_int64(out_positions_ptr)
    torch.ops._C.copy_and_expand_eagle_inputs_kernel_impl(
        _ensure_int64(target_token_ids_ptr),
        _ensure_int64(target_positions_ptr),
        _ensure_int64(next_token_ids_ptr),
        out_ids_i64,
        out_pos_i64,
        out_is_rejected_token_mask_ptr,
        out_is_masked_token_mask_ptr,
        out_new_token_indices_ptr,
        out_hidden_state_mapping_ptr,
        query_start_loc_ptr,
        query_end_loc_ptr,
        padding_token_id,
        parallel_drafting_token_id,
        total_input_tokens,
        num_padding_slots_per_request,
        shift_input_ids,
    )
    if orig_ids_dtype != torch.int64:
        out_input_ids_ptr.copy_(out_ids_i64.to(orig_ids_dtype))
    if orig_pos_dtype != torch.int64:
        out_positions_ptr.copy_(out_pos_i64.to(orig_pos_dtype))
```