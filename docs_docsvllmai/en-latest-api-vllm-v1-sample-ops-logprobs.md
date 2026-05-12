---
title: logprobs - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/sample/ops/logprobs/
source: sitemap
fetched_at: 2026-05-07T21:41:30.353500419-03:00
rendered_js: false
word_count: 93
summary: This document provides technical documentation for the batched_count_greater_than operation used for calculating log probability statistics in vLLM.
tags:
    - vllm
    - tensor-operations
    - logprobs
    - pytorch-optimization
    - torch-compile
    - machine-learning-ops
category: reference
---

## vllm.v1.sample.ops.logprobs [¶](#vllm.v1.sample.ops.logprobs "Permanent link")

Some utilities for logprobs, including logits.

## batched\_count\_greater\_than [¶](#vllm.v1.sample.ops.logprobs.batched_count_greater_than "Permanent link")

Counts elements in each row of x that are greater than the corresponding value in values. Use torch.compile to generate an optimized kernel for this function. otherwise, it will create additional copies of the input tensors and cause memory issues.

Parameters:

Name Type Description Default `x` `Tensor`

A 2D tensor of shape (batch\_size, n\_elements).

*required* `values` `Tensor`

A 2D tensor of shape (batch\_size, 1).

*required*

Returns:

Type Description `Tensor`

torch.Tensor: A 1D tensor of shape (batch\_size,) with the counts.

Source code in `vllm/v1/sample/ops/logprobs.py`

```
@torch.compile(backend=current_platform.simple_compile_backend)
defbatched_count_greater_than(x: torch.Tensor, values: torch.Tensor) -> torch.Tensor:
"""
    Counts elements in each row of x that are greater than the corresponding
    value in values.  Use torch.compile to generate an optimized kernel for
    this function. otherwise, it will create additional copies of the input
    tensors and cause memory issues.

    Args:
        x (torch.Tensor): A 2D tensor of shape (batch_size, n_elements).
        values (torch.Tensor): A 2D tensor of shape (batch_size, 1).

    Returns:
        torch.Tensor: A 1D tensor of shape (batch_size,) with the counts.
    """
    torch._check(x.shape[0] >= 1)
    torch._check(x.shape[0] == values.shape[0])
    return (x >= values).sum(-1)
```