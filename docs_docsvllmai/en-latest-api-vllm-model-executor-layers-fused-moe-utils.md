---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/utils/
source: sitemap
fetched_at: 2026-05-07T21:25:45.089912414-03:00
rendered_js: false
word_count: 169
summary: This document provides API documentation for utility functions used in fused Mixture-of-Experts (MoE) operations, including quantization methods, cache management, and token assignment counting.
tags:
    - fused-moe
    - quantization
    - fp8
    - int8
    - tensor-manipulation
    - expert-parallelism
category: api
---

## \_fp8\_quantize [¶](#vllm.model_executor.layers.fused_moe.utils._fp8_quantize "Permanent link")

Perform fp8 quantization on the inputs. If a block\_shape is provided, the output will be blocked.

Source code in `vllm/model_executor/layers/fused_moe/utils.py`

```
def_fp8_quantize(
    A: torch.Tensor,
    A_scale: torch.Tensor | None,
    per_act_token: bool,
    block_shape: list[int] | None = None,
) -> tuple[torch.Tensor, torch.Tensor]:
"""
    Perform fp8 quantization on the inputs.  If a block_shape
    is provided, the output will be blocked.
    """
    if block_shape is None:
        # TODO(luka): use QuantFP8 custom op
        #  https://github.com/vllm-project/vllm/issues/20711
        A, A_scale = ops.scaled_fp8_quant(
            A, A_scale, use_per_token_if_dynamic=per_act_token
        )
    else:
        assert not per_act_token
        assert len(block_shape) == 2
        _, block_k = block_shape[0], block_shape[1]
        A, A_scale = per_token_group_quant_fp8(A, block_k)
        assert cdiv(A.size(-1), block_k) == A_scale.size(-1)

    return A, A_scale
```

## \_int8\_quantize [¶](#vllm.model_executor.layers.fused_moe.utils._int8_quantize "Permanent link")

Perform int8 quantization on the inputs. If a block\_shape is provided, the output will be blocked.

Source code in `vllm/model_executor/layers/fused_moe/utils.py`

```
def_int8_quantize(
    A: torch.Tensor,
    A_scale: torch.Tensor | None,
    per_act_token: bool,
    block_shape: list[int] | None = None,
) -> tuple[torch.Tensor, torch.Tensor]:
"""
    Perform int8 quantization on the inputs.  If a block_shape
    is provided, the output will be blocked.
    """

    # If weights are per-channel (per_channel_quant=True), then
    # activations apply per-token quantization. Otherwise, assume
    # activation tensor-wise fp8/int8 quantization, dynamic or static
    if block_shape is None:
        if per_act_token:
            A, A_scale = per_token_quant_int8(A)
        elif A_scale is not None:
            # Static per-tensor: use the optimized CUDA kernel
            A, A_scale, _ = ops.scaled_int8_quant(A, scale=A_scale)
        elif A_scale is None:
            # Dynamic per-tensor: compute scale then quantize via kernel
            A_scale = torch.clamp(A.abs().max() / 127.0, min=1e-10)
            A, A_scale, _ = ops.scaled_int8_quant(A, scale=A_scale)
    else:
        assert not per_act_token
        assert len(block_shape) == 2
        _, block_k = block_shape[0], block_shape[1]
        A, A_scale = per_token_group_quant_int8(A, block_k)
        assert cdiv(A.size(-1), block_k) == A_scale.size(-1)

    return A, A_scale
```

## \_resize\_cache [¶](#vllm.model_executor.layers.fused_moe.utils._resize_cache "Permanent link")

Shrink the given tensor and apply the given view to it. This is used to resize the intermediate fused\_moe caches.

Source code in `vllm/model_executor/layers/fused_moe/utils.py`

```
def_resize_cache(x: torch.Tensor, v: tuple[int, ...]) -> torch.Tensor:
"""
    Shrink the given tensor and apply the given view to it.  This is
    used to resize the intermediate fused_moe caches.
    """
    assert prod(v) <= x.numel(), (
        f"{v} ({prod(v)}) <= {x.shape} ({x.numel()})"
    )  # CUDAGRAPH unfriendly?
    return x.flatten()[: prod(v)].view(*v)
```

## count\_expert\_num\_tokens [¶](#vllm.model_executor.layers.fused_moe.utils.count_expert_num_tokens "Permanent link")

```
count_expert_num_tokens(
    topk_ids: Tensor,
    num_local_experts: int,
    expert_map: Tensor | None,
) -> Tensor
```

Count the number to tokens assigned to each expert.

Parameters: - topk\_ids (torch.Tensor): Tensor mapping each token to its list of experts. - num\_local\_experts (int): Number of experts in this rank. - expert\_map (Optional\[torch.Tensor]): A tensor mapping expert indices from the global expert space to the local expert space of the expert parallel shard.

Returns: A tensor of size num\_local\_experts, where tensor\[i] holds the number of tokens assigned to the ith expert.

Source code in `vllm/model_executor/layers/fused_moe/utils.py`

```
defcount_expert_num_tokens(
    topk_ids: torch.Tensor, num_local_experts: int, expert_map: torch.Tensor | None
) -> torch.Tensor:
"""
    Count the number to tokens assigned to each expert.

    Parameters:
    - topk_ids (torch.Tensor): Tensor mapping each token to its
    list of experts.
    - num_local_experts (int): Number of experts in this rank.
    - expert_map (Optional[torch.Tensor]):  A tensor mapping expert indices
    from the global expert space to the local expert space of the expert
    parallel shard.

    Returns:
    A tensor of size num_local_experts, where tensor[i] holds the number
    of tokens assigned to the ith expert.
    """
    assert topk_ids.dtype.is_signed, "The kernel uses -1 to represent invalid topk_ids"
    expert_num_tokens = torch.empty(
        (num_local_experts), device=topk_ids.device, dtype=torch.int32
    )

    grid = num_local_experts
    BLOCK_SIZE = min(topk_ids.numel(), 1024)
    BLOCK_SIZE = triton.next_power_of_2(BLOCK_SIZE)

    _count_expert_num_tokens[(grid,)](
        topk_ids,
        expert_num_tokens,
        num_local_experts,
        topk_ids.numel(),
        expert_map,
        HAS_EXPERT_MAP=expert_map is not None,
        BLOCK_SIZE=BLOCK_SIZE,
    )

    return expert_num_tokens
```

## trtllm\_moe\_pack\_topk\_ids\_weights [¶](#vllm.model_executor.layers.fused_moe.utils.trtllm_moe_pack_topk_ids_weights "Permanent link")

Pack topk\_ids and topk\_weights into a single int32 tensor. Format: (expert\_id &lt;&lt; 16) | weight\_bf16.view(int16)

Source code in `vllm/model_executor/layers/fused_moe/utils.py`

```
@torch.compile(dynamic=True, backend=current_platform.simple_compile_backend)
deftrtllm_moe_pack_topk_ids_weights(
    topk_ids: torch.Tensor, topk_weights: torch.Tensor
) -> torch.Tensor:
"""
    Pack topk_ids and topk_weights into a single int32 tensor.
    Format: (expert_id << 16) | weight_bf16.view(int16)
    """
    return (topk_ids.to(torch.int32) << 16) | topk_weights.to(torch.bfloat16).view(
        torch.int16
    )
```