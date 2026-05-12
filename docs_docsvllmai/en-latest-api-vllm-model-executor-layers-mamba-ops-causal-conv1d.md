---
title: causal_conv1d - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/mamba/ops/causal_conv1d/
source: sitemap
fetched_at: 2026-05-07T21:26:00.003369654-03:00
rendered_js: false
word_count: 595
summary: This document provides the API definition and parameter specifications for the causal_conv1d_fn function, which implements causal convolution operations with support for variable length sequences and continuous batching in vLLM.
tags:
    - causal-convolution
    - vllm
    - continuous-batching
    - tensor-operations
    - mamba
    - sequence-modeling
category: api
---

## causal\_conv1d\_fn [¶](#vllm.model_executor.layers.mamba.ops.causal_conv1d.causal_conv1d_fn "Permanent link")

```
causal_conv1d_fn(
    x: Tensor,
    weight: Tensor,
    bias: Tensor | None,
    conv_states: Tensor,
    query_start_loc: Tensor,
    cache_indices: Tensor | None = None,
    has_initial_state: Tensor | None = None,
    activation: str | None = "silu",
    pad_slot_id: int = PAD_SLOT_ID,
    null_block_id: int = NULL_BLOCK_ID,
    block_idx_first_scheduled_token: Tensor | None = None,
    block_idx_last_scheduled_token: Tensor | None = None,
    initial_state_idx: Tensor | None = None,
    num_computed_tokens: Tensor | None = None,
    block_size_to_align=0,
    metadata=None,
    validate_data=False,
)
```

support varlen + continuous batching when x is 2D tensor

(dim,cu\_seq\_len)

cu\_seq\_len = total tokens of all seqs in that batch sequences are concatenated from left to right for varlen

weight: (dim, width) conv\_states: (...,dim,width - 1) itype updated inplace if cache\_indices are not provided [it use `cache_indices` to get the index to the cache of conv\_state for that sequence

```
conv_state[cache_indices[i]] for seq-i - to be used as initial_state when has_initial_state[i] = True
     and after that conv_state[cache_indices[i]] need to be shift-left and updated with values from 'x'
]
```

query\_start\_loc: (batch + 1) int32 The cumulative sequence lengths of the sequences in the batch, used to index into sequence. prepended by 0. if x = \[5, 1, 1, 1] &lt;- continuous batching (batch=4) then query\_start\_loc = \[0, 5, 6, 7, 8] &lt;- the starting index of the next sequence; while the last value is the ending index of the last sequence \[length(query\_start\_loc)-1 == batch] for example: query\_start\_loc = torch.Tensor(\[0,10,16,17]), x.shape=(dim,17) cache\_indices: (batch) int32 indicates the corresponding state index, like so: conv\_state = conv\_states\[cache\_indices\[batch\_id]] has\_initial\_state: (batch) bool indicates whether should the kernel take the current state as initial state for the calculations \[single boolean for each sequence in the batch: True or False] bias: (dim,) activation: either None or "silu" or "swish" or True pad\_slot\_id: int if cache\_indices is passed, lets the kernel identify padded entries that will not be processed, for example: cache\_indices = \[pad\_slot\_id, 1, 20, pad\_slot\_id] in this case, the kernel will not process entries at indices 0 and 3 block\_idx\_first\_scheduled\_token: (batch,), dtype int32 The pointer into cache\_indices, where the first cache block to be filled is located. block\_idx\_last\_scheduled\_token: (batch,), dtype int32 The pointer into cache\_indices, where the last cache block to be filled is located. initial\_state\_idx: (batch,), dtype int32 The pointer into cache\_indices, where the cache block containing the initial state is located. num\_computed\_tokens: (batch,), dtype int32 The number of tokens already completed for each sequence block\_size\_to\_align: int The block size to align the cached states to out: same shape as `x`

Source code in `vllm/model_executor/layers/mamba/ops/causal_conv1d.py`

```
defcausal_conv1d_fn(
    x: torch.Tensor,
    weight: torch.Tensor,
    bias: torch.Tensor | None,
    conv_states: torch.Tensor,
    query_start_loc: torch.Tensor,
    cache_indices: torch.Tensor | None = None,
    has_initial_state: torch.Tensor | None = None,
    activation: str | None = "silu",
    pad_slot_id: int = PAD_SLOT_ID,
    null_block_id: int = NULL_BLOCK_ID,
    block_idx_first_scheduled_token: torch.Tensor | None = None,
    block_idx_last_scheduled_token: torch.Tensor | None = None,
    initial_state_idx: torch.Tensor | None = None,
    num_computed_tokens: torch.Tensor | None = None,
    block_size_to_align=0,
    metadata=None,
    validate_data=False,
):
"""support varlen + continuous batching when x is 2D tensor

    x: (dim,cu_seq_len)
        cu_seq_len = total tokens of all seqs in that batch
        sequences are concatenated from left to right for varlen
    weight: (dim, width)
    conv_states: (...,dim,width - 1) itype
        updated inplace if cache_indices are not provided
        [it use `cache_indices` to get the index to the cache of conv_state for that sequence

        conv_state[cache_indices[i]] for seq-i - to be used as initial_state when has_initial_state[i] = True
             and after that conv_state[cache_indices[i]] need to be shift-left and updated with values from 'x'
        ]
    query_start_loc: (batch + 1) int32
        The cumulative sequence lengths of the sequences in
        the batch, used to index into sequence. prepended by 0.
        if
        x = [5, 1, 1, 1] <- continuous batching (batch=4)
        then
        query_start_loc = [0, 5, 6, 7, 8] <- the starting index of the next sequence; while the last value is
           the ending index of the last sequence
        [length(query_start_loc)-1 == batch]
        for example: query_start_loc = torch.Tensor([0,10,16,17]),
        x.shape=(dim,17)
    cache_indices: (batch)  int32
        indicates the corresponding state index,
        like so: conv_state = conv_states[cache_indices[batch_id]]
    has_initial_state: (batch) bool
        indicates whether should the kernel take the current state as initial
        state for the calculations
        [single boolean for each sequence in the batch: True or False]
    bias: (dim,)
    activation: either None or "silu" or "swish" or True
    pad_slot_id: int
        if cache_indices is passed, lets the kernel identify padded
        entries that will not be processed,
        for example: cache_indices = [pad_slot_id, 1, 20, pad_slot_id]
        in this case, the kernel will not process entries at
        indices 0 and 3
    block_idx_first_scheduled_token: (batch,), dtype int32
        The pointer into cache_indices, where the first cache block to be filled is located.
    block_idx_last_scheduled_token: (batch,), dtype int32
        The pointer into cache_indices, where the last cache block to be filled is located.
    initial_state_idx: (batch,), dtype int32
        The pointer into cache_indices, where the cache block containing the initial state is located.
    num_computed_tokens: (batch,), dtype int32
        The number of tokens already completed for each sequence
    block_size_to_align: int
        The block size to align the cached states to
    out: same shape as `x`
    """
    if isinstance(activation, bool) and activation:
        activation = "silu"

    args = None
    # Store original dtype to cast back at the end
    original_x_dtype = x.dtype
    x = x.to(conv_states.dtype)
    out = torch.empty_like(x)
    if metadata is not None:
        nums_dict = metadata.nums_dict
        args = nums_dict
        batch_ptr = metadata.batch_ptr
        token_chunk_offset_ptr = metadata.token_chunk_offset_ptr
    else:
        seqlens = query_start_loc.diff().to("cpu")
        args = seqlens
        MAX_NUM_PROGRAMS = 1024

        batch_ptr = torch.full(
            (MAX_NUM_PROGRAMS,), PAD_SLOT_ID, dtype=torch.int32, device=x.device
        )  # tracking which seq-idx the Triton program is handling
        token_chunk_offset_ptr = torch.full(
            (MAX_NUM_PROGRAMS,), PAD_SLOT_ID, dtype=torch.int32, device=x.device
        )  # tracking BLOCK_M-based index in the sequence the Triton program is handling

    is_channel_last = (x.stride(0) == 1) & (x.stride(1) > 1)
    dim, cu_seqlen = x.shape
    _, width = weight.shape
    state_len = width - 1
    np2_statelen = triton.next_power_of_2(state_len)

    padded_batch = query_start_loc.size(0) - 1
    stride_x_dim = x.stride(0)
    stride_x_token = x.stride(1)
    stride_w_dim = weight.stride(0)
    stride_w_width = weight.stride(1)
    stride_istate_seq = 0
    stride_istate_dim = 0
    stride_istate_token = 0
    num_cache_lines = 0
    BLOCK_M = 8
    if conv_states is not None:
        # extensions to support vLLM:
        # 1. conv_states is used to replaced initial_states
        # 2. conv_states serve as a cache with num cache lines can be larger than batch size
        # 3. mapping from sequence x[idx] to a cache line at index as specified via cache_indices[idx]
        # 4. computation can be skipped if cache_indices[idx] == pad_slot_id
        num_cache_lines = conv_states.size(0)
        assert (
            num_cache_lines == conv_states.shape[0]
            and dim == conv_states.shape[1]
            and width - 1 <= conv_states.shape[2]
        )
        stride_istate_seq = conv_states.stride(0)
        stride_istate_dim = conv_states.stride(1)
        stride_istate_token = conv_states.stride(2)
    if out.dim() == 2:
        stride_o_dim = out.stride(0)
        stride_o_token = out.stride(1)
    else:
        stride_o_dim = out.stride(1)
        stride_o_token = out.stride(2)
    stride_cache_indices = cache_indices.stride(0) if cache_indices is not None else 0

    if validate_data:
        assert x.dim() == 2
        assert query_start_loc is not None
        assert query_start_loc.dim() == 1
        assert x.stride(0) == 1 or x.stride(1) == 1
        if bias is not None:
            assert bias.dim() == 1
            assert dim == bias.size(0)
        if cache_indices is not None:
            assert cache_indices.dim() == 1
            assert padded_batch == cache_indices.size(0)
        if has_initial_state is not None:
            assert has_initial_state.size() == (padded_batch,)
            assert conv_states is not None, (
                "ERROR: `has_initial_state` is used, which needs also `conv_states`"
            )
        assert weight.stride(1) == 1
        assert (dim, width) == weight.shape
        assert is_channel_last, "Need to run in channel-last layout"
        if block_size_to_align is not None and block_size_to_align > 0:
            assert (block_size_to_align % BLOCK_M) == 0, (
                "The mamba block size needs to be divisible by the BLOCK_M"
            )
        else:
            block_size_to_align = BLOCK_M

    if metadata is None:

        defnum_program(META, seqlens):
            tot = 0

            mlist = []
            offsetlist = []  # type: ignore

            nums = -(-seqlens // META["BLOCK_M"])

            tot = nums.sum().item()
            mlist = np.repeat(np.arange(len(nums)), nums)
            for idx, num in enumerate(nums):
                offsetlist.extend(
                    range(num)
                )  # chunk-idx if a sequence is split into multiple chunks

            if META["batch_ptr"].nelement() < len(mlist):
                newlen = len(mlist) + 1
                META["batch_ptr"].resize_(newlen).fill_(PAD_SLOT_ID)
                META["token_chunk_offset_ptr"].resize_(newlen).fill_(PAD_SLOT_ID)

            if META["batch_ptr"].nelement() >= len(mlist):
                META["batch_ptr"][0 : len(mlist)].copy_(
                    torch.from_numpy(np.array(mlist))
                )
                META["token_chunk_offset_ptr"][0 : len(mlist)].copy_(
                    torch.from_numpy(np.array(offsetlist))
                )

            META["batch_ptr"] = META["batch_ptr"].to(META["x_ptr"].device)
            META["token_chunk_offset_ptr"] = META["token_chunk_offset_ptr"].to(
                META["x_ptr"].device
            )
            return tot
    else:

        defnum_program(META, nums_dict):
            tot = nums_dict[META["BLOCK_M"]]["tot"]

            mlist = nums_dict[META["BLOCK_M"]]["mlist"]
            mlist_len = nums_dict[META["BLOCK_M"]]["mlist_len"]

            offsetlist = nums_dict[META["BLOCK_M"]]["offsetlist"]

            if nums_dict[META["BLOCK_M"]]["batch_ptr"] is not None:
                META["batch_ptr"] = nums_dict[META["BLOCK_M"]]["batch_ptr"]
                META["token_chunk_offset_ptr"] = nums_dict[META["BLOCK_M"]][
                    "token_chunk_offset_ptr"
                ]
            else:
                if META["batch_ptr"].nelement() < mlist_len:
                    newlen = mlist_len + 1
                    META["batch_ptr"].resize_(newlen).fill_(PAD_SLOT_ID)
                    META["token_chunk_offset_ptr"].resize_(newlen).fill_(PAD_SLOT_ID)

                if META["batch_ptr"].nelement() >= mlist_len:
                    META["batch_ptr"][0:mlist_len].copy_(mlist)
                    META["token_chunk_offset_ptr"][0:mlist_len].copy_(offsetlist)
            return tot

    defgrid(META):
        return (
            num_program(META, args),
            triton.cdiv(dim, META["BLOCK_N"]),
        )

    if batch_ptr.device != x.device:
        batch_ptr = batch_ptr.to(x.device)
        token_chunk_offset_ptr = token_chunk_offset_ptr.to(x.device)

    _causal_conv1d_fwd_kernel[grid](
        # Pointers to matrices
        x,
        weight,
        bias,
        conv_states,
        cache_indices,
        has_initial_state,
        query_start_loc,
        batch_ptr,
        token_chunk_offset_ptr,
        block_idx_first_scheduled_token,
        block_idx_last_scheduled_token,
        initial_state_idx,
        num_computed_tokens,
        out,
        # Matrix dimensions
        dim,
        cu_seqlen,
        num_cache_lines,
        # stride
        stride_x_dim,
        stride_x_token,
        stride_w_dim,
        stride_w_width,
        stride_istate_seq,
        stride_istate_dim,
        stride_istate_token,
        stride_cache_indices,
        stride_o_dim,
        stride_o_token,
        block_size_to_align // BLOCK_M,
        # others
        pad_slot_id,
        null_block_id,
        # META
        HAS_BIAS=bias is not None,
        KERNEL_WIDTH=width,
        SILU_ACTIVATION=activation in ["silu", "swish"],
        IS_APC_ENABLED=block_idx_last_scheduled_token is not None,
        HAS_NULL_BLOCK=null_block_id is not None,
        NP2_STATELEN=np2_statelen,
        # launch_cooperative_grid=True
        BLOCK_M=BLOCK_M,
        BLOCK_N=256,
        num_stages=2,
    )
    return out.to(original_x_dtype)
```

## causal\_conv1d\_update [¶](#vllm.model_executor.layers.mamba.ops.causal_conv1d.causal_conv1d_update "Permanent link")

```
causal_conv1d_update(
    x: Tensor,
    conv_state: Tensor,
    weight: Tensor,
    bias: Tensor | None = None,
    activation: bool | str | None = None,
    conv_state_indices: Tensor | None = None,
    num_accepted_tokens: Tensor | None = None,
    query_start_loc: Tensor | None = None,
    max_query_len: int = -1,
    null_block_id: int = NULL_BLOCK_ID,
    block_idx_last_scheduled_token: Tensor | None = None,
    initial_state_idx: Tensor | None = None,
    validate_data=False,
)
```

x: Input tensor which can take the following shapes:

- `[batch, dim]` - single token prediction
- `[batch, dim, seqlen]` - single or multiple tokens prediction
- `[num_tokens, dim]` - continuous batching, where num\_tokens is the total tokens of all sequences in that batch

conv\_state: (..., dim, state\_len), where state\_len &gt;= width - 1 weight: (dim, width) bias: (dim,) conv\_state\_indices: (batch,), dtype int32 If not None, the conv\_state is a larger tensor along the batch dim, and we are selecting the batch coords specified by conv\_state\_indices. Useful for a continuous batching scenario. block\_idx\_last\_scheduled\_token: (batch,), dtype int32 The pointer into conv\_state\_indices, where the last cache block to be filled is located. initial\_state\_idx: (batch,), dtype int32 The pointer into conv\_state\_indices, where the cache block containing the initial state is located. num\_accepted\_tokens: (batch,), dtype int32 If not None, it indicates the number of accepted tokens for each sequence in the batch. This is used in speculative decoding, where the conv\_state is updated in a sliding window manner. query\_start\_loc: (batch + 1,) int32 If not None, the inputs is given in a varlen fashion and this indicates the starting index of each sequence in the batch. max\_query\_len: int If query\_start\_loc is not None, this indicates the maximum query length in the batch. null\_block\_id: int Block ID used to identify padded entries in conv\_state\_indices. Block 0 is the null block. for example: conv\_state\_indices = \[null\_block\_id, 1, 20, null\_block\_id] in this case, the kernel will not process entries at indices 0 and 3 out: (batch, dim) or (batch, dim, seqlen) or (num\_tokens, dim), same shape as `x`

Source code in `vllm/model_executor/layers/mamba/ops/causal_conv1d.py`

```
defcausal_conv1d_update(
    x: torch.Tensor,
    conv_state: torch.Tensor,
    weight: torch.Tensor,
    bias: torch.Tensor | None = None,
    activation: bool | str | None = None,
    conv_state_indices: torch.Tensor | None = None,
    num_accepted_tokens: torch.Tensor | None = None,
    query_start_loc: torch.Tensor | None = None,
    max_query_len: int = -1,
    null_block_id: int = NULL_BLOCK_ID,
    block_idx_last_scheduled_token: torch.Tensor | None = None,
    initial_state_idx: torch.Tensor | None = None,
    validate_data=False,
):
"""
    x: Input tensor which can take the following shapes:

    - `[batch, dim]` - single token prediction
    - `[batch, dim, seqlen]` - single or multiple tokens prediction
    - `[num_tokens, dim]` - continuous batching, where num_tokens is
        the total tokens of all sequences in that batch

    conv_state: (..., dim, state_len), where state_len >= width - 1
    weight: (dim, width)
    bias: (dim,)
    conv_state_indices: (batch,), dtype int32
        If not None, the conv_state is a larger tensor along the batch dim,
        and we are selecting the batch coords specified by conv_state_indices.
        Useful for a continuous batching scenario.
    block_idx_last_scheduled_token: (batch,), dtype int32
        The pointer into conv_state_indices, where the last cache block to be filled is located.
    initial_state_idx: (batch,), dtype int32
        The pointer into conv_state_indices, where the cache block containing the initial state is located.
    num_accepted_tokens: (batch,), dtype int32
        If not None, it indicates the number of accepted tokens for each
        sequence in the batch.
        This is used in speculative decoding, where the conv_state is updated
        in a sliding window manner.
    query_start_loc: (batch + 1,) int32
        If not None, the inputs is given in a varlen fashion and this indicates
        the starting index of each sequence in the batch.
    max_query_len: int
        If query_start_loc is not None, this indicates the maximum query
        length in the batch.
    null_block_id: int
            Block ID used to identify padded entries in
            conv_state_indices. Block 0 is the null block.
            for example: conv_state_indices = [null_block_id, 1, 20, null_block_id]
            in this case, the kernel will not process entries at
            indices 0 and 3
    out: (batch, dim) or (batch, dim, seqlen) or (num_tokens, dim), same shape as `x`
    """
    if validate_data:
        assert null_block_id is not None
        assert x.stride(1) == 1
    if isinstance(activation, bool):
        activation = "silu" if activation is True else None
    elif activation is not None:
        assert activation in ["silu", "swish"]

    original_x_dtype = x.dtype
    x = x.to(conv_state.dtype)
    unsqueeze = query_start_loc is None and x.dim() == 2
    if unsqueeze:
        # make it (batch, dim, seqlen) with seqlen == 1
        x = x.unsqueeze(-1)
    if query_start_loc is None:
        batch, dim, seqlen = x.shape
    else:
        assert conv_state_indices is not None
        batch = conv_state_indices.size(0)
        dim = x.size(1)
        seqlen = max_query_len
    _, width = weight.shape
    # conv_state: (..., dim, state_len), where state_len >= width - 1
    num_cache_lines, _, state_len = conv_state.size()

    if validate_data:
        assert dim == weight.size(0)
        assert state_len >= width - 1
        # when above happens, we don't shift-left to keep any records in conv_state
        assert dim == conv_state.size(1)
        if conv_state_indices is None:
            assert conv_state.size(0) >= batch
        else:
            assert batch == conv_state_indices.shape[0], (
                f"ERROR: conv_state_indices should have shape ({batch},*) but got {conv_state_indices.shape}"
            )

        assert num_cache_lines >= batch
        assert weight.stride(1) == 1  # Need this

    # adopt the strategy in vLLM that overwrite on 'x' directly, rather than creating a new tensor 'o'
    out = x
    stride_w_dim, stride_w_width = weight.stride()

    if query_start_loc is None:
        # X (batch, dim, seqlen)
        stride_x_seq, stride_x_dim, stride_x_token = x.stride()
        stride_o_seq, stride_o_dim, stride_o_token = out.stride()
    else:
        # X (dim, cu_seqlen)
        stride_x_token, stride_x_dim = x.stride()
        stride_x_seq = 0
        stride_o_token, stride_o_dim = out.stride()
        stride_o_seq = 0

    stride_istate_seq, stride_istate_dim, stride_istate_token = conv_state.stride()
    stride_state_indices = (
        conv_state_indices.stride(0) if conv_state_indices is not None else 0
    )
    if num_accepted_tokens is not None:
        state_len = width - 1 + (seqlen - 1)  # effective state_len needed
    else:
        state_len = width - 1
    np2_statelen = triton.next_power_of_2(state_len)

    defgrid(META):
        return (
            batch,
            triton.cdiv(dim, META["BLOCK_N"]),
        )

    _causal_conv1d_update_kernel[grid](
        # Pointers to matrices
        x,
        weight,
        bias,
        conv_state,
        conv_state_indices,
        num_accepted_tokens,
        query_start_loc,
        block_idx_last_scheduled_token,
        initial_state_idx,
        out,
        # Matrix dimensions
        batch,
        dim,
        seqlen,
        state_len,
        num_cache_lines,
        # stride
        stride_x_seq,
        stride_x_dim,
        stride_x_token,
        stride_w_dim,
        stride_w_width,
        stride_istate_seq,
        stride_istate_dim,
        stride_istate_token,
        stride_state_indices,
        stride_o_seq,
        stride_o_dim,
        stride_o_token,
        # others
        null_block_id,
        # META
        HAS_BIAS=bias is not None,
        KERNEL_WIDTH=width,
        SILU_ACTIVATION=activation in ["silu", "swish"],
        IS_VARLEN=query_start_loc is not None,
        IS_APC_ENABLED=block_idx_last_scheduled_token is not None,
        IS_SPEC_DECODING=num_accepted_tokens is not None,
        NP2_STATELEN=np2_statelen,
        HAS_NULL_BLOCK=null_block_id is not None,
        BLOCK_N=256,
    )
    if unsqueeze:
        out = out.squeeze(-1)
    return out.to(original_x_dtype)
```