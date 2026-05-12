---
title: topk_weight_and_reduce - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/topk_weight_and_reduce/
source: sitemap
fetched_at: 2026-05-07T21:25:41.109931434-03:00
rendered_js: false
word_count: 153
summary: This document defines various implementations for weight application and reduction strategies in fused Mixture-of-Experts (MoE) layers within the vLLM framework.
tags:
    - moe
    - fused-layers
    - tensor-operations
    - deep-learning
    - vllm-architecture
category: reference
---

## TopKWeightAndReduceContiguous [¶](#vllm.model_executor.layers.fused_moe.topk_weight_and_reduce.TopKWeightAndReduceContiguous "Permanent link")

Bases: `TopKWeightAndReduce`

TopKWeightAndReduce implementation for a fused\_experts output of shape (m, topk, K)

Source code in `vllm/model_executor/layers/fused_moe/topk_weight_and_reduce.py`

```
classTopKWeightAndReduceContiguous(mk.TopKWeightAndReduce):
"""
    TopKWeightAndReduce implementation for a fused_experts output
    of shape (m, topk, K)
    """

    def__eq__(self, other):
        return isinstance(other, TopKWeightAndReduceContiguous)

    defapply(
        self,
        output: torch.Tensor | None,
        fused_expert_output: torch.Tensor,
        topk_weights: torch.Tensor,
        topk_ids: torch.Tensor,
        apply_router_weight_on_input: bool,
    ) -> torch.Tensor:
        m, num_topk = topk_ids.size()
        k = fused_expert_output.size(-1)
        if fused_expert_output.ndim == 2:
            fused_expert_output = fused_expert_output.view(m, num_topk, k)

        assert fused_expert_output.size() == (m, num_topk, k), (
            f"Expected fused_expert_output size {(m,num_topk,k)}. But got "
            f"{fused_expert_output.size()}"
        )

        if not apply_router_weight_on_input:
            fused_expert_output.mul_(topk_weights.view(m, -1, 1))

        if output is None:
            output = torch.empty(
                (m, k),
                device=fused_expert_output.device,
                dtype=fused_expert_output.dtype,
            )
        assert output.size() == (m, k), (
            f"Expected output size {(m,k)}. But got {output.size()}"
        )

        ops.moe_sum(fused_expert_output, output)
        return output
```

## TopKWeightAndReduceDelegate [¶](#vllm.model_executor.layers.fused_moe.topk_weight_and_reduce.TopKWeightAndReduceDelegate "Permanent link")

Bases: `TopKWeightAndReduce`

Useful in the case when some FusedMoEExpertsModular implementation does not perform weight application and reduction but cannot address the needs of all the compatible PrepareAndFinalize implementations. For example, BatchedTritonExperts is compatible with both batched PrepareAndFinalize implementations like DeepEPLLPrepareAndFinalize and BatchedPrepareAndFinalize. Some PrepareAndFinalize implementations do the weight-application + reduction as part of the combine kernel, while BatchedPrepareAndFinalize needs an explicit implementation. To facilitate this case, the BatchedTritonExperts could use TopKWeightAndReduceDelegate so the PrepareAndFinalize implementations could choose how to weight + reduce.

Source code in `vllm/model_executor/layers/fused_moe/topk_weight_and_reduce.py`

```
classTopKWeightAndReduceDelegate(mk.TopKWeightAndReduce):
"""
    Useful in the case when some FusedMoEExpertsModular
    implementation does not perform weight application and reduction
    but cannot address the needs of all the compatible PrepareAndFinalize
    implementations.
    For example, BatchedTritonExperts is compatible with both batched
    PrepareAndFinalize implementations like DeepEPLLPrepareAndFinalize and
    BatchedPrepareAndFinalize. Some PrepareAndFinalize implementations do
    the weight-application + reduction as part of the combine kernel, while
    BatchedPrepareAndFinalize needs an explicit implementation. To facilitate
    this case, the BatchedTritonExperts could use TopKWeightAndReduceDelegate
    so the PrepareAndFinalize implementations could choose how to
    weight + reduce.
    """

    def__eq__(self, other):
        return isinstance(other, TopKWeightAndReduceDelegate)

    defapply(
        self,
        output: torch.Tensor | None,
        fused_expert_output: torch.Tensor,
        topk_weights: torch.Tensor,
        topk_ids: torch.Tensor,
        apply_router_weight_on_input: bool,
    ) -> torch.Tensor:
        raise RuntimeError(
            "The caller is expected to choose an appropriate "
            "TopKWeightAndReduce implementation."
        )
```

## TopKWeightAndReduceNaiveBatched [¶](#vllm.model_executor.layers.fused_moe.topk_weight_and_reduce.TopKWeightAndReduceNaiveBatched "Permanent link")

Bases: `TopKWeightAndReduce`

TopKWeightAndReduce implementation for a fused\_experts output of shape (num\_experts, batch\_size, K)

Source code in `vllm/model_executor/layers/fused_moe/topk_weight_and_reduce.py`

```
classTopKWeightAndReduceNaiveBatched(mk.TopKWeightAndReduce):
"""
    TopKWeightAndReduce implementation for a fused_experts output
    of shape (num_experts, batch_size, K)
    """

    def__init__(self, rank: int):
        self.rank = rank

    def__eq__(self, other):
        return isinstance(other, TopKWeightAndReduceNaiveBatched) and (
            other.rank == self.rank
        )

    defapply(
        self,
        output: torch.Tensor | None,
        fused_expert_output: torch.Tensor,
        topk_weights: torch.Tensor,
        topk_ids: torch.Tensor,
        apply_router_weight_on_input: bool,
    ) -> torch.Tensor:
        assert fused_expert_output.ndim == 3
        num_tokens = topk_ids.size(0)
        num_local_experts = fused_expert_output.size(0)
        K = fused_expert_output.size(-1)

        if output is None:
            output = torch.zeros(
                (num_tokens, K),
                device=fused_expert_output.device,
                dtype=fused_expert_output.dtype,
            )
        else:
            output.fill_(0)

        assert output.size() == (num_tokens, K), (
            f"Expected output size {(num_tokens,K)}, but got {output.size()}"
        )

        first_expert = num_local_experts * self.rank
        last_expert = first_expert + num_local_experts

        for expert_id in range(first_expert, last_expert):
            matching_tokens = topk_ids == expert_id
            topks = torch.any(matching_tokens, dim=1).flatten()
            rows = torch.count_nonzero(topks)
            rhs = fused_expert_output[expert_id - first_expert, :rows, :]
            if not apply_router_weight_on_input:
                rhs.mul_(topk_weights[matching_tokens].view(rhs.size(0), 1))
            output[topks] = output[topks] + rhs

        return output
```

## TopKWeightAndReduceNoOP [¶](#vllm.model_executor.layers.fused_moe.topk_weight_and_reduce.TopKWeightAndReduceNoOP "Permanent link")

Bases: `TopKWeightAndReduce`

The fused\_experts outputs have already been weight applied and reduced. This implementation is a no-op.

Source code in `vllm/model_executor/layers/fused_moe/topk_weight_and_reduce.py`

```
classTopKWeightAndReduceNoOP(mk.TopKWeightAndReduce):
"""
    The fused_experts outputs have already been weight applied and reduced.
    This implementation is a no-op.
    """

    def__eq__(self, other):
        return isinstance(other, TopKWeightAndReduceNoOP)

    defapply(
        self,
        output: torch.Tensor | None,
        fused_expert_output: torch.Tensor,
        topk_weights: torch.Tensor,
        topk_ids: torch.Tensor,
        apply_router_weight_on_input: bool,
    ) -> torch.Tensor:
        # Weight application and reduction operations are already done.
        if output is None:
            return fused_expert_output

        # Skip self-copy when caller aliased fused_out to output upstream.
        if output is fused_expert_output:
            return output

        # MoEPrepareAndFinalizeNoDPEPModular needs the output to be in the `output`
        # tensor.
        assert output.size() == fused_expert_output.size(), (
            "output shape is expected to match the fused_expert_output shape. "
            f"But got output={output.size()}, "
            f"used_expert_output={fused_expert_output.size()}"
        )
        output.copy_(fused_expert_output, non_blocking=True)
        return output
```