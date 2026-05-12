---
title: naive_dp_ep - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/prepare_finalize/naive_dp_ep/
source: sitemap
fetched_at: 2026-05-07T21:25:21.045363883-03:00
rendered_js: false
word_count: 0
summary: This code implements a naive prepare and finalize strategy for Mixture-of-Experts (MoE) models, utilizing data-parallel and expert-parallel communication patterns within a modular kernel architecture.
tags:
    - mixture-of-experts
    - distributed-training
    - quantization
    - tensor-parallelism
    - modular-kernels
category: reference
---

```
classMoEPrepareAndFinalizeNaiveDPEPModular(mk.FusedMoEPrepareAndFinalizeModular):
"""
    Naive Prepare/Finalize for Dp/Ep case for Modular Kernels.

    Uses Torch AR/RS or AR for dispatch/combine operations, applied
    to the topk weights and ids.
    """

    def__init__(
        self,
        is_sequence_parallel: bool = False,
        num_dispatchers: int = 1,
    ) -> None:
        super().__init__()
        self.is_sequence_parallel = is_sequence_parallel
        self._num_dispatchers = num_dispatchers

    @property
    defactivation_format(self) -> mk.FusedMoEActivationFormat:
        return mk.FusedMoEActivationFormat.Standard

    defmax_num_tokens_per_rank(self) -> int | None:
        return None

    deftopk_indices_dtype(self) -> torch.dtype | None:
        return None

    defnum_dispatchers(self) -> int:
        return self._num_dispatchers

    defoutput_is_reduced(self) -> bool:
        return False

    defprepare(
        self,
        a1: torch.Tensor,
        topk_weights: torch.Tensor,
        topk_ids: torch.Tensor,
        num_experts: int,
        expert_map: torch.Tensor | None,
        apply_router_weight_on_input: bool,
        quant_config: FusedMoEQuantConfig,
        defer_input_quant: bool = False,
    ) -> mk.PrepareResultType:
"""Quantize and Dispatch Topk Weights and Topk Ids."""

        if apply_router_weight_on_input:
            topk = topk_ids.size(1)
            assert topk == 1, (
                "apply_router_weight_on_input is only implemented for topk=1"
            )
            # Note: do not use inplace for shared experts overlap
            a1 = a1 * topk_weights.to(a1.dtype)

        a1q, scales = _quantize_and_setup_dispatch(a1, quant_config, defer_input_quant)

        res = get_ep_group().dispatch(
            a1q,
            topk_weights,
            topk_ids,
            is_sequence_parallel=self.is_sequence_parallel,
            extra_tensors=scales,
        )

        if scales is None:
            assert len(res) == 3
            a1q, topk_weights, topk_ids = res
            a1q_scale = None
        else:
            assert len(res) == 4
            a1q, topk_weights, topk_ids, scales = res
            a1q_scale = _unwrap_scale_and_prepare_for_moe(scales, quant_config)

        return a1q, a1q_scale, None, topk_ids, topk_weights

    deffinalize(
        self,
        output: torch.Tensor,
        fused_expert_output: torch.Tensor,
        topk_weights: torch.Tensor,
        topk_ids: torch.Tensor,
        apply_router_weight_on_input: bool,
        weight_and_reduce_impl: mk.TopKWeightAndReduce,
    ) -> None:
        if isinstance(weight_and_reduce_impl, TopKWeightAndReduceDelegate):
            weight_and_reduce_impl = TopKWeightAndReduceContiguous()

        out = weight_and_reduce_impl.apply(
            output=None,
            fused_expert_output=fused_expert_output,
            topk_weights=topk_weights,
            topk_ids=topk_ids,
            apply_router_weight_on_input=apply_router_weight_on_input,
        )

        output.copy_(
            get_ep_group().combine(out, is_sequence_parallel=self.is_sequence_parallel)
        )
```