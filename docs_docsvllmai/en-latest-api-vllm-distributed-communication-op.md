---
title: communication_op - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/communication_op/
source: sitemap
fetched_at: 2026-05-07T21:17:23.969409056-03:00
rendered_js: false
word_count: 56
summary: This document provides the API specifications for tensor model parallel communication operations used to synchronize and aggregate data across distributed model parallel groups.
tags:
    - distributed-computing
    - model-parallelism
    - tensor-operations
    - vllm
    - communication-primitives
category: api
---

## tensor\_model\_parallel\_all\_gather [¶](#vllm.distributed.communication_op.tensor_model_parallel_all_gather "Permanent link")

```
tensor_model_parallel_all_gather(
    input_: Tensor, dim: int = -1
) -> Tensor
```

All-gather the input tensor across model parallel group.

Source code in `vllm/distributed/communication_op.py`

```
deftensor_model_parallel_all_gather(
    input_: torch.Tensor, dim: int = -1
) -> torch.Tensor:
"""All-gather the input tensor across model parallel group."""
    return get_tp_group().all_gather(input_, dim)
```

## tensor\_model\_parallel\_all\_reduce [¶](#vllm.distributed.communication_op.tensor_model_parallel_all_reduce "Permanent link")

All-reduce the input tensor across model parallel group.

Source code in `vllm/distributed/communication_op.py`

```
deftensor_model_parallel_all_reduce(input_: torch.Tensor) -> torch.Tensor:
"""All-reduce the input tensor across model parallel group."""
    return get_tp_group().all_reduce(input_)
```

## tensor\_model\_parallel\_gather [¶](#vllm.distributed.communication_op.tensor_model_parallel_gather "Permanent link")

```
tensor_model_parallel_gather(
    input_: Tensor, dst: int = 0, dim: int = -1
) -> Tensor | None
```

Gather the input tensor across model parallel group.

Source code in `vllm/distributed/communication_op.py`

```
deftensor_model_parallel_gather(
    input_: torch.Tensor, dst: int = 0, dim: int = -1
) -> torch.Tensor | None:
"""Gather the input tensor across model parallel group."""
    return get_tp_group().gather(input_, dst, dim)
```

## tensor\_model\_parallel\_reduce\_scatter [¶](#vllm.distributed.communication_op.tensor_model_parallel_reduce_scatter "Permanent link")

```
tensor_model_parallel_reduce_scatter(
    input_: Tensor, dim: int = -1
) -> Tensor
```

Reduce-Scatter the input tensor across model parallel group.

Source code in `vllm/distributed/communication_op.py`

```
deftensor_model_parallel_reduce_scatter(
    input_: torch.Tensor, dim: int = -1
) -> torch.Tensor:
"""Reduce-Scatter the input tensor across model parallel group."""
    return get_tp_group().reduce_scatter(input_, dim)
```