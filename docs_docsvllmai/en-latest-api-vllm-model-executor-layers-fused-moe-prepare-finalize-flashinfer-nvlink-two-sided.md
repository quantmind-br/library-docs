---
title: flashinfer_nvlink_two_sided - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/prepare_finalize/flashinfer_nvlink_two_sided/
source: sitemap
fetched_at: 2026-05-07T21:25:19.001633288-03:00
rendered_js: false
word_count: 0
summary: This document defines a base class for handling FlashInfer MoE prepare and finalize operations, specifically managing all-to-all communication and data preparation for NVLink-based dispatchers.
tags:
    - moe
    - flashinfer
    - nvlink
    - all-to-all
    - distributed-training
    - tensor-parallelism
category: reference
---

```
classFlashInferNVLinkTwoSidedPrepareAndFinalize(mk.FusedMoEPrepareAndFinalizeModular):
"""Base class for FlashInfer MoE prepare and finalize operations."""

    all2all_manager: All2AllManagerBase

    def__init__(
        self,
        num_dispatchers: int = 1,
    ):
        super().__init__()
        self.num_dispatchers_ = num_dispatchers
        device_communicator = get_ep_group().device_communicator
        assert device_communicator is not None
        assert device_communicator.all2all_manager is not None
        self.all2all_manager = device_communicator.all2all_manager

    @property
    defactivation_format(self) -> mk.FusedMoEActivationFormat:
        return mk.FusedMoEActivationFormat.Standard

    defmax_num_tokens_per_rank(self) -> int | None:
        return None

    deftopk_indices_dtype(self) -> torch.dtype | None:
        return None

    defnum_dispatchers(self) -> int:
        return self.num_dispatchers_

    defoutput_is_reduced(self) -> bool:
        return False

    def_apply_router_weight_on_input(
        self,
        a1: torch.Tensor,
        topk_weights: torch.Tensor,
        topk_ids: torch.Tensor,
        apply_router_weight_on_input: bool,
    ) -> None:
"""Apply router weight on input if needed."""
        if apply_router_weight_on_input:
            topk = topk_ids.size(1)
            assert topk == 1, (
                "apply_router_weight_on_input is only implemented for topk=1"
            )
            a1.mul_(topk_weights.to(a1.dtype))

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
        self._apply_router_weight_on_input(
            a1, topk_weights, topk_ids, apply_router_weight_on_input
        )
        global_num_tokens_cpu = get_local_sizes()
        top_k = topk_ids.size(1)

        (self.alltoall_info, topk_ids, topk_weights, a1q, a1q_scale) = (
            flashinfer_alltoall_dispatch(
                self.all2all_manager,
                global_num_tokens_cpu,
                a1,
                quant_config.a1_gscale,
                topk_ids,
                topk_weights,
                top_k,
                num_experts,
                quant_config,
                defer_input_quant=defer_input_quant,
            )
        )

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
        top_k = topk_ids.size(1)
        token_count = output.shape[0]
        fused_expert_output = flashinfer_alltoall_combine(
            self.all2all_manager,
            fused_expert_output,
            top_k=top_k,
            token_count=token_count,
            alltoall_info=self.alltoall_info,
        )
        output.copy_(fused_expert_output)
```