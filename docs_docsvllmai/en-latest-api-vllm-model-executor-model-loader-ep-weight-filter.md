---
title: ep_weight_filter - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/ep_weight_filter/
source: sitemap
fetched_at: 2026-05-07T21:28:39.869572171-03:00
rendered_js: false
word_count: 253
summary: This module provides utility functions for filtering expert-specific model weights during loading to reduce disk I/O in distributed expert parallelism deployments.
tags:
    - vllm
    - model-loading
    - expert-parallelism
    - moe-models
    - distributed-computing
    - weight-filtering
category: reference
---

## vllm.model\_executor.model\_loader.ep\_weight\_filter [¶](#vllm.model_executor.model_loader.ep_weight_filter "Permanent link")

Filter out non-local expert weights during loading to avoid redundant I/O.

In DP+EP deployments each rank only needs its own expert shard. Skipping non-local expert tensors *before* they are read from disk eliminates the majority of storage I/O for MoE models (experts typically account for ~85-90 % of total weight bytes).

## compute\_local\_expert\_ids [¶](#vllm.model_executor.model_loader.ep_weight_filter.compute_local_expert_ids "Permanent link")

```
compute_local_expert_ids(
    num_experts: int,
    ep_size: int,
    ep_rank: int,
    placement: str = "linear",
) -> set[int] | None
```

Compute the set of global expert ids owned by *ep\_rank*.

Returns `None` when EP is not active (`ep_size <= 1`), meaning all experts are local and no filtering should be performed.

The distribution logic mirrors :func:`vllm.model_executor.layers.fused_moe.layer.determine_expert_map`.

Parameters:

Name Type Description Default `placement` `str`

`"linear"` for contiguous assignment, `"round_robin"` for interleaved assignment.

`'linear'`

Source code in `vllm/model_executor/model_loader/ep_weight_filter.py`

```
defcompute_local_expert_ids(
    num_experts: int,
    ep_size: int,
    ep_rank: int,
    placement: str = "linear",
) -> set[int] | None:
"""Compute the set of global expert ids owned by *ep_rank*.

    Returns ``None`` when EP is not active (``ep_size <= 1``), meaning all
    experts are local and no filtering should be performed.

    The distribution logic mirrors
    :func:`vllm.model_executor.layers.fused_moe.layer.determine_expert_map`.

    Args:
        placement: ``"linear"`` for contiguous assignment,
            ``"round_robin"`` for interleaved assignment.
    """
    if ep_size <= 1:
        return None

    if placement == "linear":
        base = num_experts // ep_size
        remainder = num_experts % ep_size
        start = ep_rank * base + min(ep_rank, remainder)
        local_count = base + (1 if ep_rank < remainder else 0)
        return set(range(start, start + local_count))
    elif placement == "round_robin":
        return set(range(ep_rank, num_experts, ep_size))
    else:
        raise ValueError(f"Unknown expert placement strategy: {placement}")
```

## parse\_expert\_id [¶](#vllm.model_executor.model_loader.ep_weight_filter.parse_expert_id "Permanent link")

```
parse_expert_id(weight_name: str) -> int | None
```

Return the expert id embedded in *weight\_name*, or `None` if it is not an per-expert weight.

Returns `None` for dense weights (attention, layernorm, embedding), shared experts, and 3D fused-expert tensors where all experts are stored in a single tensor without a numeric expert id in the name.

Source code in `vllm/model_executor/model_loader/ep_weight_filter.py`

```
defparse_expert_id(weight_name: str) -> int | None:
"""Return the expert id embedded in *weight_name*, or ``None`` if it is
    not an per-expert weight.

    Returns ``None`` for dense weights (attention, layernorm, embedding),
    shared experts, and 3D fused-expert tensors where all experts are stored
    in a single tensor without a numeric expert id in the name."""
    m = _EXPERT_ID_RE.search(weight_name)
    return int(m.group(1)) if m else None
```

## should\_skip\_weight [¶](#vllm.model_executor.model_loader.ep_weight_filter.should_skip_weight "Permanent link")

```
should_skip_weight(
    weight_name: str, local_expert_ids: set[int] | None
) -> bool
```

Return `True` if *weight\_name* is an expert weight that does not belong to the local rank and should be skipped during loading.

Source code in `vllm/model_executor/model_loader/ep_weight_filter.py`

```
defshould_skip_weight(
    weight_name: str,
    local_expert_ids: set[int] | None,
) -> bool:
"""Return ``True`` if *weight_name* is an expert weight that does not
    belong to the local rank and should be skipped during loading."""
    if local_expert_ids is None:
        return False
    eid = parse_expert_id(weight_name)
    if eid is None:
        # Not an expert weight (dense / shared-expert / embedding) → keep.
        return False
    # Only skip heavy weight tensors, never scale/metadata tensors.
    # Scale tensors are tiny and some backends need them from ALL experts
    # (e.g. FlashInfer NVFP4 computes a global max of activation scales).
    if not weight_name.endswith(".weight"):
        return False
    return eid not in local_expert_ids
```