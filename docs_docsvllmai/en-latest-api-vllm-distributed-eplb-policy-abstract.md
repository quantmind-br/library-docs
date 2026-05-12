---
title: abstract - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/eplb/policy/abstract/
source: sitemap
fetched_at: 2026-05-07T21:17:59.804427167-03:00
rendered_js: false
word_count: 109
summary: This document defines the interface for an expert-parallelism load balancer used to map logical experts to physical replicas in a distributed computing environment.
tags:
    - expert-parallelism
    - load-balancing
    - distributed-computing
    - tensor-mapping
    - machine-learning-infrastructure
category: api
---

```
rebalance_experts(
    weight: Tensor,
    num_replicas: int,
    num_groups: int,
    num_nodes: int,
    num_ranks: int,
    old_global_expert_indices: Tensor | None = None,
) -> Tensor
```

Entry point for expert-parallelism load balancer.

Parameters:

Name Type Description Default `weight` `Tensor`

\[layers, num\_logical\_experts], the load statistics for all logical experts

*required* `num_replicas` `int`

number of physical experts, must be a multiple of `num_ranks`

*required* `num_groups` `int`

number of expert groups

*required* `num_nodes` `int`

number of server nodes

*required* `num_ranks` `int`

number of ranks, must be a multiple of `num_nodes`

*required* `old_global_expert_indices` `Tensor | None`

\[layers, num\_logical\_experts], the old global expert indices. Used to avoid unnecessary weight copying for experts moving within one rank.

`None`

Returns: physical\_to\_logical\_map: \[layers, num\_replicas], the expert index of each replica

Source code in `vllm/distributed/eplb/policy/abstract.py`

```
@classmethod
@abstractmethod
defrebalance_experts(
    cls,
    weight: torch.Tensor,
    num_replicas: int,
    num_groups: int,
    num_nodes: int,
    num_ranks: int,
    old_global_expert_indices: torch.Tensor | None = None,
) -> torch.Tensor:
"""
    Entry point for expert-parallelism load balancer.

    Parameters:
        weight: [layers, num_logical_experts], the load statistics
            for all logical experts
        num_replicas: number of physical experts, must be a multiple of
            `num_ranks`
        num_groups: number of expert groups
        num_nodes: number of server nodes
        num_ranks: number of ranks, must be a multiple of `num_nodes`
        old_global_expert_indices: [layers, num_logical_experts], the old global
            expert indices. Used to avoid unnecessary weight copying
            for experts moving within one rank.
    Returns:
        physical_to_logical_map: [layers, num_replicas], the expert
            index of each replica
    """
    raise NotImplementedError
```