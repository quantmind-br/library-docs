---
title: dcp_alltoall - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/attention/ops/dcp_alltoall/
source: sitemap
fetched_at: 2026-05-07T21:39:51.247906502-03:00
rendered_js: false
word_count: 324
summary: This document explains the All-to-All (A2A) communication backend for Decode Context Parallel (DCP), which optimizes attention output reduction by packing partial outputs and LSE values into a single collective communication operation.
tags:
    - dcp
    - all-to-all
    - attention-mechanism
    - parallel-computing
    - vllm
    - distributed-training
    - nccl
category: concept
---

DCP All-to-All communication backend for attention.

Provides All-to-All (A2A) communication as an alternative to AllGather + ReduceScatter (AG+RS) for Decode Context Parallel (DCP). Instead of gathering the full Q tensor and scattering partial outputs, A2A exchanges partial attention outputs and their LSE values across ranks, then combines them with exact LSE-weighted reduction.

This reduces the number of NCCL calls per attention layer by exchanging the partial output and LSE in a single packed All-to-All payload.

Usage

vllm serve model --tp 16 --dcp 16 --dcp-comm-backend a2a

Reference: https://arxiv.org/abs/2507.07120

## \_lse\_weighted\_combine [¶](#vllm.v1.attention.ops.dcp_alltoall._lse_weighted_combine "Permanent link")

CPU reference implementation for LSE-weighted combination.

This is a pure PyTorch implementation used for testing and validation.

Parameters:

Name Type Description Default `outputs` `Tensor`

Partial attention outputs \[N, B, H, D] N = number of KV shards (ranks) B = batch size (num\_tokens) H = number of heads per rank D = head dimension

*required* `lses` `Tensor`

Log-sum-exp values \[N, B, H]

*required* `return_lse` `bool`

If True, also return the global LSE

`False` `is_lse_base_on_e` `bool`

If True, LSE is base e; if False, base 2

`True`

Returns:

Type Description `Tensor | tuple[Tensor, Tensor]`

Combined output \[B, H, D], and optionally global LSE \[B, H]

Source code in `vllm/v1/attention/ops/dcp_alltoall.py`

```
def_lse_weighted_combine(
    outputs: torch.Tensor,
    lses: torch.Tensor,
    return_lse: bool = False,
    is_lse_base_on_e: bool = True,
) -> torch.Tensor | tuple[torch.Tensor, torch.Tensor]:
"""
    CPU reference implementation for LSE-weighted combination.

    This is a pure PyTorch implementation used for testing and validation.

    Args:
        outputs: Partial attention outputs [N, B, H, D]
                 N = number of KV shards (ranks)
                 B = batch size (num_tokens)
                 H = number of heads per rank
                 D = head dimension
        lses: Log-sum-exp values [N, B, H]
        return_lse: If True, also return the global LSE
        is_lse_base_on_e: If True, LSE is base e; if False, base 2

    Returns:
        Combined output [B, H, D], and optionally global LSE [B, H]
    """
    N, B, H, D = outputs.shape

    # Handle NaN and inf in LSEs
    lses = torch.where(
        torch.isnan(lses) | torch.isinf(lses),
        torch.tensor(float("-inf"), device=lses.device, dtype=lses.dtype),
        lses,
    )

    # Compute max LSE for numerical stability
    lse_max, _ = lses.max(dim=0)  # [B, H]
    lse_max = torch.where(
        lse_max == float("-inf"),
        torch.zeros_like(lse_max),
        lse_max,
    )

    # Compute weights: softmax over the N dimension
    if is_lse_base_on_e:
        weights = torch.exp(lses - lse_max.unsqueeze(0))  # [N, B, H]
    else:
        weights = torch.pow(2.0, lses - lse_max.unsqueeze(0))  # [N, B, H]

    # Handle NaN weights
    weights = torch.where(torch.isnan(weights), torch.zeros_like(weights), weights)

    # Normalize weights
    weight_sum = weights.sum(dim=0, keepdim=True)  # [1, B, H]
    weights = weights / weight_sum.clamp(min=1e-10)  # [N, B, H]

    # Weighted combination: sum over N dimension
    result = (outputs * weights.unsqueeze(-1)).sum(dim=0)  # [B, H, D]

    if return_lse:
        if is_lse_base_on_e:
            global_lse = torch.log(weight_sum.squeeze(0)) + lse_max  # [B, H]
        else:
            global_lse = torch.log2(weight_sum.squeeze(0)) + lse_max  # [B, H]
        return result, global_lse

    return result
```

## dcp\_a2a\_lse\_reduce [¶](#vllm.v1.attention.ops.dcp_alltoall.dcp_a2a_lse_reduce "Permanent link")

Combine partial attention outputs across DCP ranks using All-to-All.

The output and fp32 LSE are packed into a single output-dtype buffer, sent with one All-to-All, then unpacked and combined with exact LSE weighting.

Parameters:

Name Type Description Default `cp_attn_out` `Tensor`

\[B, H, D] where B=num\_tokens, H=total\_heads, D=head\_dim

*required* `cp_attn_lse` `Tensor`

\[B, H] log-sum-exp values (fp32)

*required* `cp_group` `GroupCoordinator`

GroupCoordinator for DCP communication

*required* `ctx` `CPTritonContext | None`

CPTritonContext (unused, for signature compatibility)

`None` `return_lse` `bool`

If True, also return the combined global LSE

`False` `is_lse_base_on_e` `bool`

If True, LSE is base e; if False, base 2

`True`

Returns:

Type Description `Tensor | tuple[Tensor, Tensor]`

Combined output \[B, H/N, D] (head-scattered)

`Tensor | tuple[Tensor, Tensor]`

If return\_lse=True, also returns global\_lse \[B, H/N]

Source code in `vllm/v1/attention/ops/dcp_alltoall.py`

```
defdcp_a2a_lse_reduce(
    cp_attn_out: torch.Tensor,
    cp_attn_lse: torch.Tensor,
    cp_group: GroupCoordinator,
    ctx: CPTritonContext | None = None,
    return_lse: bool = False,
    is_lse_base_on_e: bool = True,
) -> torch.Tensor | tuple[torch.Tensor, torch.Tensor]:
"""
    Combine partial attention outputs across DCP ranks using All-to-All.

    The output and fp32 LSE are packed into a single output-dtype buffer, sent
    with one All-to-All, then unpacked and combined with exact LSE weighting.

    Args:
        cp_attn_out: [B, H, D] where B=num_tokens, H=total_heads, D=head_dim
        cp_attn_lse: [B, H] log-sum-exp values (fp32)
        cp_group: GroupCoordinator for DCP communication
        ctx: CPTritonContext (unused, for signature compatibility)
        return_lse: If True, also return the combined global LSE
        is_lse_base_on_e: If True, LSE is base e; if False, base 2

    Returns:
        Combined output [B, H/N, D] (head-scattered)
        If return_lse=True, also returns global_lse [B, H/N]
    """
    world_size = cp_group.world_size

    if world_size == 1:
        if return_lse:
            return cp_attn_out, cp_attn_lse
        return cp_attn_out

    B, H, D = cp_attn_out.shape
    if H % world_size != 0:
        raise ValueError(f"H={H} must be divisible by DCP world size {world_size}.")
    H_per_rank = H // world_size
    lse_pack_dim = _dcp_a2a_lse_pack_dim(cp_attn_out.dtype)

    send_buffer, recv_buffer = _dcp_a2a_send_recv_buffers(
        (world_size, B, H_per_rank, D + lse_pack_dim),
        device=cp_attn_out.device,
        dtype=cp_attn_out.dtype,
    )

    _dcp_a2a_pack_send(
        cp_attn_out,
        cp_attn_lse,
        send_buffer,
        world_size,
        H_per_rank,
        D,
        lse_pack_dim,
    )

    work = dist.all_to_all_single(
        recv_buffer.view(-1),
        send_buffer.view(-1),
        group=cp_group.device_group,
        async_op=True,
    )
    work.wait()

    return _dcp_a2a_unpack_combine(
        recv_buffer, D, lse_pack_dim, return_lse, is_lse_base_on_e
    )
```