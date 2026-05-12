---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/attention/backends/utils/
source: sitemap
fetched_at: 2026-05-07T21:39:47.886956437-03:00
rendered_js: false
word_count: 725
summary: This document provides API documentation and utility functions for managing attention backend hyperparameters, sequence length calculations for distributed decoding, and block table handling for mamba kernels.
tags:
    - attention-backend
    - hyperparameter-inference
    - distributed-decoding
    - kv-cache
    - mamba-kernel
    - vllm
category: api
---

## PerLayerParameters `dataclass` [¶](#vllm.v1.attention.backends.utils.PerLayerParameters "Permanent link")

Currently, FlashInfer backend only support models in which all layers share the same values for the following hyperparameters. Should not be used for trtllm-gen backend since it supports different values for the following hyperparameters.

Source code in `vllm/v1/attention/backends/utils.py`

```
@dataclass
classPerLayerParameters:
"""
    Currently, FlashInfer backend only support models in which all layers share
    the same values for the following hyperparameters. Should not be used for
    trtllm-gen backend since it supports different values for the following
    hyperparameters.
    """

    window_left: int
    logits_soft_cap: float | None
    sm_scale: float
    has_sinks: bool = False
    # has same params for all layers
    has_same_window_lefts: bool | None = field(default=None, compare=False)
    has_same_all_params: bool | None = field(default=None, compare=False)
```

## get\_dcp\_local\_seq\_lens [¶](#vllm.v1.attention.backends.utils.get_dcp_local_seq_lens "Permanent link")

```
get_dcp_local_seq_lens(
    seq_lens: Tensor,
    dcp_size: int = 1,
    dcp_rank: int | None = None,
    cp_kv_cache_interleave_size: int = 1,
) -> Tensor
```

While using dcp, kv\_cache size stored on each rank may be different, use this function to calculate split decode seq\_lens of each dcp rank. Only consider dcp now, we can extend the case of cp based on this.

Source code in `vllm/v1/attention/backends/utils.py`

```
defget_dcp_local_seq_lens(
    seq_lens: torch.Tensor,
    dcp_size: int = 1,
    dcp_rank: int | None = None,
    cp_kv_cache_interleave_size: int = 1,
) -> torch.Tensor:
"""While using dcp, kv_cache size stored on each rank may be different,
    use this function to calculate split decode seq_lens of each dcp rank.
    Only consider dcp now, we can extend the case of cp based on this.
    """
    num_requests = seq_lens.size(0)
    if dcp_rank is None:
        rank_offsets = (
            torch.arange(dcp_size, dtype=torch.int32, device=seq_lens.device)
            .unsqueeze(0)
            .repeat(num_requests, 1)
        )
    else:
        rank_offsets = torch.tensor(
            [[dcp_rank]], dtype=torch.int32, device=seq_lens.device
        )
    seq_lens_tiled = (
        seq_lens.to(torch.int32).unsqueeze(-1).repeat(1, rank_offsets.shape[1])
    )
    base = (
        seq_lens_tiled
        // cp_kv_cache_interleave_size
        // dcp_size
        * cp_kv_cache_interleave_size
    )
    remainder = seq_lens_tiled - base * dcp_size
    remainder = torch.clip(
        remainder - rank_offsets * cp_kv_cache_interleave_size,
        0,
        cp_kv_cache_interleave_size,
    )
    dcp_local_seq_lens = base + remainder
    return dcp_local_seq_lens.squeeze(1)
```

## get\_per\_layer\_parameters [¶](#vllm.v1.attention.backends.utils.get_per_layer_parameters "Permanent link")

Scan layers in `layer_names` and determine some hyperparameters to use during `plan`.

Source code in `vllm/v1/attention/backends/utils.py`

```
defget_per_layer_parameters(
    vllm_config: VllmConfig, layer_names: list[str], cls_: type["AttentionImpl"]
) -> dict[str, PerLayerParameters]:
"""
    Scan layers in `layer_names` and determine some hyperparameters
    to use during `plan`.
    """

    layers = get_layers_from_vllm_config(
        vllm_config,
        AttentionLayerBase,  # type: ignore[type-abstract]
        layer_names,
    )
    per_layer_params: dict[str, PerLayerParameters] = {}

    for key, layer in layers.items():
        impl = layer.impl
        assert isinstance(impl, cls_)

        # Infer hyperparameters from the attention layer
        window_size = getattr(impl, "sliding_window", None)
        window_left = window_size[0] if window_size is not None else -1
        logits_soft_cap = getattr(impl, "logits_soft_cap", None)
        sm_scale = impl.scale
        has_sinks = getattr(impl, "sinks", None) is not None

        per_layer_params[key] = PerLayerParameters(
            window_left, logits_soft_cap, sm_scale, has_sinks
        )

    return per_layer_params
```

## infer\_global\_hyperparameters [¶](#vllm.v1.attention.backends.utils.infer_global_hyperparameters "Permanent link")

```
infer_global_hyperparameters(
    per_layer_params: dict[str, PerLayerParameters],
) -> PerLayerParameters
```

Currently, FlashInfer backend other than trtllm-gen only support models in which all layers share the same values for the following hyperparameters: - `window_left` - `logits_soft_cap` - `sm_scale`

So this function asserts that all layers share the same values for these hyperparameters and returns the global values.

Source code in `vllm/v1/attention/backends/utils.py`

```
definfer_global_hyperparameters(
    per_layer_params: dict[str, PerLayerParameters],
) -> PerLayerParameters:
"""
    Currently, FlashInfer backend other than trtllm-gen
    only support models in which all layers share
    the same values for the following hyperparameters:
    - `window_left`
    - `logits_soft_cap`
    - `sm_scale`

    So this function asserts that all layers share the same values for these
    hyperparameters and returns the global values.
    """

    assert len(per_layer_params) > 0, "No attention layers found in the model."

    param_sets = list(per_layer_params.values())
    global_params = param_sets[0]

    global_params.has_same_window_lefts = all(
        params.window_left == global_params.window_left for params in param_sets
    )
    global_params.has_same_all_params = all(
        params == global_params for params in param_sets
    )

    return global_params
```

## mamba\_get\_block\_table\_tensor [¶](#vllm.v1.attention.backends.utils.mamba_get_block_table_tensor "Permanent link")

Get the block table tensor for mamba kernels from the input common\_attn\_metadata.block\_table\_tensor given different mamba cache modes.

- "all": input (#requests, cdiv(max\_model\_len, block\_size)); output (#requests, cdiv(max\_model\_len, block\_size)).
- "none": input (#requests, 1 + num\_speculative\_blocks); output (#requests, 1 + num\_speculative\_blocks).
- "align": input (#requests, cdiv(max\_model\_len, block\_size)); output (#requests, 1 + num\_speculative\_blocks), which are the last 1 + num\_speculative\_blocks of each request.

Source code in `vllm/v1/attention/backends/utils.py`

```
defmamba_get_block_table_tensor(
    block_table: torch.Tensor,
    seq_lens: torch.Tensor,
    kv_cache_spec: KVCacheSpec,
    mamba_cache_mode: str,
) -> torch.Tensor:
"""
    Get the block table tensor for mamba kernels from the input
    common_attn_metadata.block_table_tensor given different mamba cache modes.

    - "all":   input  (#requests, cdiv(max_model_len, block_size));
               output (#requests, cdiv(max_model_len, block_size)).

    - "none":  input  (#requests, 1 + num_speculative_blocks);
               output (#requests, 1 + num_speculative_blocks).

    - "align": input  (#requests, cdiv(max_model_len, block_size));
               output (#requests, 1 + num_speculative_blocks), which are the last
               1 + num_speculative_blocks of each request.
    """
    if mamba_cache_mode in ("all", "none"):
        return block_table
    else:
        assert isinstance(kv_cache_spec, MambaSpec)
        # NOTE: For 0-length requests in CUDA graph, use a start_index of 0
        # to handle the invalid block table.
        start_indices = torch.clamp(
            (seq_lens - 1) // kv_cache_spec.block_size,
            min=0,
        )
        # Use int32 for arithmetic to avoid dtype promotion overhead,
        # then convert to int64 for gather (which requires Long indices)
        offsets = torch.arange(
            1 + kv_cache_spec.num_speculative_blocks,
            device=block_table.device,
            dtype=torch.int32,
        )
        indices_to_gather = (start_indices.unsqueeze(1) + offsets).to(torch.int64)
        return torch.gather(block_table, 1, indices_to_gather)
```

## reorder\_batch\_to\_split\_decodes\_and\_prefills [¶](#vllm.v1.attention.backends.utils.reorder_batch_to_split_decodes_and_prefills "Permanent link")

```
reorder_batch_to_split_decodes_and_prefills(
    input_batch: InputBatch,
    scheduler_output: SchedulerOutput,
    decode_threshold: int = 1,
) -> bool
```

Reorders the batch to split into prefill and decode requests; places all requests with &lt;= decode\_threshold tokens at the front of the batch.

The batch is reordered into 4 regions

decode: (num\_scheduled &lt;= threshold AND is not prefilling) short\_extend: (num\_scheduled &lt;= threshold AND is chunked prefilling) long\_extend: (num\_scheduled &gt; threshold AND is chunked prefilling) prefill: (num\_computed == 0) # First chunks

Returns:

Type Description `bool`

True if the batch was modified, False otherwise.

Source code in `vllm/v1/attention/backends/utils.py`

```
defreorder_batch_to_split_decodes_and_prefills(
    input_batch: "InputBatch",
    scheduler_output: "SchedulerOutput",
    decode_threshold: int = 1,
) -> bool:
"""
    Reorders the batch to split into prefill and decode requests; places all
    requests with <= decode_threshold tokens at the front of the batch.

    The batch is reordered into 4 regions:
        decode:        (num_scheduled <= threshold AND is not prefilling)
        short_extend:  (num_scheduled <= threshold AND is chunked prefilling)
        long_extend:   (num_scheduled > threshold AND is chunked prefilling)
        prefill:       (num_computed == 0)   # First chunks

    Returns:
        True if the batch was modified, False otherwise.
    """
    num_reqs = len(input_batch.req_ids)
    num_scheduled_tokens = [
        scheduler_output.num_scheduled_tokens[id] for id in input_batch.req_ids
    ]
    num_scheduled_tokens_np = np.array(num_scheduled_tokens)
    num_computed_tokens_np = input_batch.num_computed_tokens_cpu[:num_reqs]
    num_prompt_tokens_np = input_batch.num_prompt_tokens[:num_reqs]

    has_context = num_computed_tokens_np > 0
    is_below_threshold = num_scheduled_tokens_np <= decode_threshold
    done_prefilling = num_computed_tokens_np >= num_prompt_tokens_np

    # Mutually exclusive categories (exactly one True per request):
    # 1. No context yet -> prefill
    # 2. Has context, above threshold -> long_extend
    # 3. Has context, below threshold, still prefilling -> short_extend
    # 4. Has context, below threshold, done prefilling -> decode
    is_pure_prefill = ~has_context
    is_long_extend = has_context & ~is_below_threshold
    is_short_extend = has_context & is_below_threshold & ~done_prefilling
    is_decode = has_context & is_below_threshold & done_prefilling

    # Desired order: decode → short_extend → long_extend → prefill
    req_regions = np.zeros(num_reqs, dtype=np.int32)  # 0 = decode by default
    req_regions[is_short_extend] = 1
    req_regions[is_long_extend] = 2
    req_regions[is_pure_prefill] = 3

    num_decodes = int(is_decode.sum())
    num_short_extends = int(is_short_extend.sum())
    num_long_extends = int(is_long_extend.sum())
    num_prefills = int(is_pure_prefill.sum())

    target_regions = np.repeat(
        [0, 1, 2, 3],
        [num_decodes, num_short_extends, num_long_extends, num_prefills],
    ).astype(np.int32)

    needs_swap = req_regions != target_regions

    if not needs_swap.any():
        return False

    # Extract indices that need swapping and sort by target region
    orig_indices = np.where(needs_swap)[0]
    sorted_order = np.argsort(req_regions[needs_swap], kind="stable")
    src_indices = orig_indices[sorted_order]

    src_dest_map = {int(src): int(dst) for src, dst in zip(src_indices, orig_indices)}

    for src in src_dest_map:
        dst = src_dest_map[src]
        while src != dst:
            input_batch.swap_states(src, dst)
            # Mark dst as done by updating its destination to itself
            next_dst = src_dest_map.get(dst, dst)
            src_dest_map[dst] = dst
            dst = next_dst

    return True
```

## reshape\_attn\_output\_for\_spec\_decode [¶](#vllm.v1.attention.backends.utils.reshape_attn_output_for_spec_decode "Permanent link")

```
reshape_attn_output_for_spec_decode(
    attn_output: Tensor,
) -> Tensor
```

Reshapes the attention output tensor, so that the batch\_size and seq\_len dimensions are combined.

Source code in `vllm/v1/attention/backends/utils.py`

```
defreshape_attn_output_for_spec_decode(attn_output: torch.Tensor) -> torch.Tensor:
"""
    Reshapes the attention output tensor, so that
    the batch_size and seq_len dimensions are combined.
    """
    if attn_output.dim() == 3:
        # Already in the correct shape
        return attn_output
    assert attn_output.dim() == 4, f"attn_output must be 4D, got {attn_output.dim()}D"
    total_tokens = attn_output.shape[0] * attn_output.shape[1]
    return attn_output.view(total_tokens, attn_output.shape[2], attn_output.shape[3])
```

## reshape\_query\_for\_spec\_decode [¶](#vllm.v1.attention.backends.utils.reshape_query_for_spec_decode "Permanent link")

Reshapes the query tensor for the specified batch size, so that it has shape (batch\_size, seq\_len, num\_heads, head\_dim).

Source code in `vllm/v1/attention/backends/utils.py`

```
defreshape_query_for_spec_decode(query: torch.Tensor, batch_size: int) -> torch.Tensor:
"""
    Reshapes the query tensor for the specified batch size, so that
    it has shape (batch_size, seq_len, num_heads, head_dim).
    """
    assert query.dim() == 3, f"query must be 3D, got {query.dim()}D"
    total_tokens = query.shape[0]
    num_heads = query.shape[1]
    head_dim = query.shape[2]
    assert total_tokens % batch_size == 0, (
        f"{total_tokens=} is not divisible by {batch_size=}"
    )
    seq_len = total_tokens // batch_size
    return query.view(batch_size, seq_len, num_heads, head_dim)
```

## split\_decodes\_and\_prefills [¶](#vllm.v1.attention.backends.utils.split_decodes_and_prefills "Permanent link")

Assuming a reordered batch, finds the boundary between prefill and decode requests.

The batch is expected to be ordered as

decode → short\_extend → long\_extend → prefill

Parameters:

Name Type Description Default `common_attn_metadata` `CommonAttentionMetadata`

CommonAttentionMetadata object containing the batch metadata.

*required* `decode_threshold` `int`

The maximum query length to be considered a decode.

`1` `require_uniform` `bool`

If True, requires that all decode requests have the same query length. When set, some queries may be considered prefills even if they are &lt;= decode\_threshold, in order to ensure uniformity.

`False` `treat_short_extends_as_decodes` `bool`

If True (default), short extends (query\_len &lt;= threshold but still prefilling) are counted as decodes. If False, they are counted as prefills.

`True`

Returns:

Name Type Description `num_decodes` `int`

The number of decode requests.

`num_prefills` `int`

The number of prefill requests.

`num_decode_tokens` `int`

The number of tokens in the decode requests.

`num_prefill_tokens` `int`

The number of tokens in the prefill requests.

Source code in `vllm/v1/attention/backends/utils.py`

```
defsplit_decodes_and_prefills(
    common_attn_metadata: CommonAttentionMetadata,
    decode_threshold: int = 1,
    require_uniform: bool = False,
    treat_short_extends_as_decodes: bool = True,
) -> tuple[int, int, int, int]:
"""
    Assuming a reordered batch, finds the boundary between prefill and decode
    requests.

    The batch is expected to be ordered as:
        decode → short_extend → long_extend → prefill

    Args:
        common_attn_metadata: CommonAttentionMetadata object containing the
            batch metadata.
        decode_threshold: The maximum query length to be considered a decode.
        require_uniform: If True, requires that all decode requests have the
            same query length. When set, some queries may be considered prefills
            even if they are <= decode_threshold, in order to ensure uniformity.
        treat_short_extends_as_decodes: If True (default), short extends
            (query_len <= threshold but still prefilling) are counted as
            decodes. If False, they are counted as prefills.

    Returns:
        num_decodes: The number of decode requests.
        num_prefills: The number of prefill requests.
        num_decode_tokens: The number of tokens in the decode requests.
        num_prefill_tokens: The number of tokens in the prefill requests.
    """
    max_query_len = common_attn_metadata.max_query_len
    num_reqs = common_attn_metadata.num_reqs
    num_tokens = common_attn_metadata.num_actual_tokens
    query_start_loc = common_attn_metadata.query_start_loc_cpu

    if (
        max_query_len <= decode_threshold
        and (not require_uniform or decode_threshold <= 1)
        and treat_short_extends_as_decodes
    ):
        return num_reqs, 0, num_tokens, 0

    query_lens = query_start_loc[1:] - query_start_loc[:-1]
    if query_lens[0].item() > decode_threshold:
        # first request is not decode, so no decode requests
        return 0, num_reqs, 0, num_tokens

    if require_uniform:
        # check if we are in a padded uniform batch; this is used for full-CGs, some
        # requests may have a query length of 0 but since they are padding its fine
        # to treat them as decodes (ensures num_decodes matches the captured size)
        if torch.all((query_lens == query_lens[0]) | (query_lens == 0)):
            return num_reqs, 0, num_tokens, 0  # all decodes
        is_prefill = query_lens != query_lens[0]
    else:
        is_prefill = query_lens > decode_threshold

    if not treat_short_extends_as_decodes:
        assert common_attn_metadata.is_prefilling is not None
        is_prefill |= common_attn_metadata.is_prefilling

    if not torch.any(is_prefill):
        return num_reqs, 0, num_tokens, 0

    first_prefill = is_prefill.int().argmax(dim=-1).item()
    num_decodes = first_prefill
    num_prefills = num_reqs - num_decodes
    num_decode_tokens = query_start_loc[first_prefill].item()
    num_prefill_tokens = num_tokens - num_decode_tokens
    return (num_decodes, num_prefills, num_decode_tokens, num_prefill_tokens)
```

## split\_decodes\_prefills\_and\_extends [¶](#vllm.v1.attention.backends.utils.split_decodes_prefills_and_extends "Permanent link")

Assuming a reordered batch, finds the boundary between prefill and decode requests.

Parameters:

Name Type Description Default `common_attn_metadata` `CommonAttentionMetadata`

CommonAttentionMetadata object containing the batch metadata.

*required* `decode_threshold` `int`

The maximum query length to be considered a decode.

`1`

Returns:

Name Type Description `num_decodes` `int`

The number of decode requests.

`num_extends` `int`

The number of extend requests.

`num_prefills` `int`

The number of prefill requests.

`num_decode_tokens` `int`

The number of tokens in the decode requests.

`num_extend_tokens` `int`

The number of tokens in the extend requests.

`num_prefill_tokens` `int`

The number of tokens in the prefill requests.

Source code in `vllm/v1/attention/backends/utils.py`

```
defsplit_decodes_prefills_and_extends(
    common_attn_metadata: CommonAttentionMetadata,
    decode_threshold: int = 1,
) -> tuple[int, int, int, int, int, int]:
"""
    Assuming a reordered batch, finds the boundary between prefill and decode
    requests.

    Args:
        common_attn_metadata: CommonAttentionMetadata object containing the
            batch metadata.
        decode_threshold: The maximum query length to be considered a decode.

    Returns:
        num_decodes: The number of decode requests.
        num_extends: The number of extend requests.
        num_prefills: The number of prefill requests.
        num_decode_tokens: The number of tokens in the decode requests.
        num_extend_tokens: The number of tokens in the extend requests.
        num_prefill_tokens: The number of tokens in the prefill requests.
    """
    max_query_len = common_attn_metadata.max_query_len
    num_reqs = common_attn_metadata.num_reqs
    num_tokens = common_attn_metadata.num_actual_tokens
    query_start_loc = common_attn_metadata.query_start_loc_cpu
    # Upper bound is exact for prefill rows; decode rows still satisfy
    # seq_len > query_len under the optimistic bound, so `seq_lens ==
    # query_lens` identifies prefills correctly either way.
    assert common_attn_metadata.seq_lens_cpu_upper_bound is not None
    seq_lens = common_attn_metadata.seq_lens_cpu_upper_bound

    if max_query_len <= decode_threshold:
        return num_reqs, 0, 0, num_tokens, 0, 0

    query_lens = query_start_loc[1:] - query_start_loc[:-1]
    is_prefill_or_extend = query_lens > decode_threshold
    is_prefill = (seq_lens == query_lens) & is_prefill_or_extend
    first_extend = is_prefill_or_extend.int().argmax(dim=-1).item()
    first_prefill = is_prefill.int().argmax(dim=-1).item()
    num_decodes = first_extend
    num_decode_tokens = query_start_loc[first_extend].item()
    if not torch.any(is_prefill_or_extend):
        return (num_decodes, 0, 0, num_decode_tokens, 0, 0)

    num_prefills_or_extends = num_reqs - num_decodes
    num_prefill_or_extend_tokens = num_tokens - num_decode_tokens
    if not torch.any(is_prefill):
        return (
            num_decodes,
            num_prefills_or_extends,
            0,
            num_decode_tokens,
            num_prefill_or_extend_tokens,
            0,
        )

    num_extends = first_prefill - num_decodes
    num_prefills = num_reqs - first_prefill

    num_prefill_tokens = num_tokens - query_start_loc[first_prefill]
    num_extend_tokens = num_prefill_or_extend_tokens - num_prefill_tokens
    return (
        num_decodes,
        num_extends,
        num_prefills,
        num_decode_tokens,
        num_extend_tokens,
        num_prefill_tokens,
    )
```

## split\_prefill\_chunks [¶](#vllm.v1.attention.backends.utils.split_prefill_chunks "Permanent link")

Split the prefill requests into chunks such that the total sequence length of each chunk is less than or equal to the workspace size.

Parameters:

Name Type Description Default `seq_lens_cpu` `Tensor`

The sequence lengths of the prefill requests on CPU.

*required* `workspace_size` `int`

The maximum workspace size (in tokens) per chunk.

*required* `request_offset` `int`

The offset to add to the request indices.

`0`

Returns: A list of tuples of (reqs\_start, reqs\_end) representing chunk boundaries.

Source code in `vllm/v1/attention/backends/utils.py`

```
defsplit_prefill_chunks(
    seq_lens_cpu: torch.Tensor, workspace_size: int, request_offset: int = 0
) -> list[tuple[int, int]]:
"""
    Split the prefill requests into chunks such that the total sequence length
    of each chunk is less than or equal to the workspace size.

    Args:
        seq_lens_cpu: The sequence lengths of the prefill requests on CPU.
        workspace_size: The maximum workspace size (in tokens) per chunk.
        request_offset: The offset to add to the request indices.
    Returns:
        A list of tuples of (reqs_start, reqs_end) representing chunk boundaries.
    """
    chunk_bounds = []
    i, n = 0, len(seq_lens_cpu)
    assert torch.all(seq_lens_cpu <= workspace_size).item()

    while i < n:
        start, chunk_total = i, 0
        while i < n and (chunk_total + (s := seq_lens_cpu[i].item())) <= workspace_size:
            chunk_total += s
            i += 1
        chunk_bounds.append((start + request_offset, i + request_offset))
    return chunk_bounds
```

Return a new subclass of `metadata_cls` with additional fields

Source code in `vllm/v1/attention/backends/utils.py`

```
defsubclass_attention_metadata(
    name_prefix: str,
    metadata_cls: Any,
    fields: list[tuple[str, Any, Any]],
) -> Any:
"""
    Return a new subclass of `metadata_cls` with additional fields
    """
    name: str = name_prefix + metadata_cls.__name__  # type: ignore
    Wrapped = make_dataclass(name, fields, bases=(metadata_cls,))
    return Wrapped
```