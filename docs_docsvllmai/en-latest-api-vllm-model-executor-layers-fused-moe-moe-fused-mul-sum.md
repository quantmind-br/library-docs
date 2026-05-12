---
title: moe_fused_mul_sum - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/moe_fused_mul_sum/
source: sitemap
fetched_at: 2026-05-07T21:25:04.219918418-03:00
rendered_js: false
word_count: 7
summary: This document defines a fused kernel function for Mixture of Experts (MoE) architectures that performs a weighted summation of expert outputs across tokens.
tags:
    - mixture-of-experts
    - fused-kernel
    - torch-compute
    - neural-networks
    - tensor-operations
    - deep-learning-optimization
category: api
---

```
defmoe_fused_mul_sum(
    inputs: torch.Tensor,
    topk_weights: torch.Tensor,
    outputs: torch.Tensor | None = None,
    topk_ids: torch.Tensor | None = None,
    expert_map: torch.Tensor | None = None,
) -> torch.Tensor:
"""
    Fused kernel for MoE (Mixture of Experts) to perform weighted summation
    of expert outputs.

    Args:
        inputs: The output from experts.
            Shape: (num_tokens, top_k, hidden_size).
        topk_weights: The weights assigned to each expert for each token.
            Shape: (num_tokens, top_k).
        outputs: Optional pre-allocated output tensor.
            Shape: (num_tokens, hidden_size).
        topk_ids: Optional indices of the top-k experts. Used when
            `expert_map` is provided. Shape: (num_tokens, top_k).
        expert_map: Optional mapping for Expert Parallelism. A value < 0
            indicates an invalid token/expert pair that will be skipped.

    Returns:
        The fused weighted sum of expert outputs.
        Shape: (num_tokens, hidden_size).
    """
    assert inputs.ndim == 3
    assert topk_weights.ndim == 2
    assert inputs.is_contiguous()
    assert topk_weights.is_contiguous()
    assert inputs.dtype in (torch.float32, torch.float16, torch.bfloat16)
    assert topk_weights.dtype in (torch.float32, torch.float16, torch.bfloat16)

    num_tokens, top_k, size = inputs.shape
    output_shape = (num_tokens, size)
    if outputs is None:
        outputs = torch.empty(output_shape, dtype=inputs.dtype, device=inputs.device)

    assert outputs.shape == output_shape
    assert topk_weights.shape == (num_tokens, top_k)

    if not isinstance(inputs, FakeTensor):
        BLOCK_M, BLOCK_K, num_warps, num_stages = _heuristic_config(
            num_tokens,
            top_k,
            size,
            inputs.element_size(),
        )
        grid = (triton.cdiv(size, BLOCK_K), triton.cdiv(num_tokens, BLOCK_M))
        moe_fused_mul_sum_kernel[grid](
            inputs,
            topk_weights,
            outputs,
            topk_ids,
            expert_map,
            num_tokens,
            top_k * size,
            expert_map is not None,
            top_k,
            size,
            BLOCK_M,
            BLOCK_K,
            num_warps=num_warps,
            num_stages=num_stages,
        )

    return outputs
```