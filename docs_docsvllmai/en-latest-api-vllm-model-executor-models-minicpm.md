---
title: minicpm - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/minicpm/
source: sitemap
fetched_at: 2026-05-07T21:31:45.039807759-03:00
rendered_js: false
word_count: 0
summary: This document defines a tensor-parallel Mixture-of-Experts (MoE) neural network layer that shards expert weights across multiple ranks and utilizes fused kernels for efficient computation.
tags:
    - mixture-of-experts
    - tensor-parallelism
    - deep-learning
    - pytorch
    - distributed-training
    - neural-network-layer
category: reference
---

```
classMiniCPMMoE(nn.Module):
"""A tensor-parallel MoE implementation that shards each expert
    across all ranks.

    Each expert's weights are sharded across all ranks and a fused MoE
    kernel is used for the forward pass, and finally we reduce the outputs
    across ranks.
    """

    def__init__(
        self,
        num_experts: int,
        top_k: int,
        hidden_size: int,
        intermediate_size: int,
        params_dtype: torch.dtype | None = None,
        tp_size: int | None = None,
        prefix: str = "",
    ):
        super().__init__()
        self.tp_size = tp_size or get_tensor_model_parallel_world_size()
        self.num_total_experts = num_experts
        self.top_k = top_k
        self.hidden_size = hidden_size
        self.intermediate_size = intermediate_size // self.tp_size

        if params_dtype is None:
            params_dtype = torch.get_default_dtype()
        self.params_dtype = params_dtype

        self.gate = ReplicatedLinear(
            self.hidden_size,
            self.num_total_experts,
            bias=False,
            params_dtype=self.params_dtype,
            quant_config=None,
            prefix=f"{prefix}.gate",
        )

        self.ws = nn.Parameter(
            torch.empty(
                self.num_total_experts,
                2 * self.intermediate_size,
                self.hidden_size,
                device=current_platform.device_type,
                dtype=self.params_dtype,
            )
        )
        self.w2s = nn.Parameter(
            torch.empty(
                self.num_total_experts,
                self.hidden_size,
                self.intermediate_size,
                device=current_platform.device_type,
                dtype=self.params_dtype,
            )
        )

        set_weight_attrs(
            self.ws,
            {
                "weight_loader": self.weight_loader,
            },
        )
        set_weight_attrs(
            self.w2s,
            {
                "weight_loader": self.weight_loader,
            },
        )

    defweight_loader(
        self,
        param: nn.Parameter,
        loaded_weight: torch.Tensor,
        weight_name: str,
        expert_id: int,
    ):
        tp_rank = get_tensor_model_parallel_rank()
        param_data = param.data
        shard_size = self.intermediate_size
        shard = slice(tp_rank * shard_size, (tp_rank + 1) * shard_size)
        if weight_name.endswith("w1.weight"):
            param_data[expert_id, 0:shard_size, :] = loaded_weight[shard, :]
        if weight_name.endswith("w3.weight"):
            param_data[expert_id, shard_size : 2 * shard_size, :] = loaded_weight[
                shard, :
            ]
        if weight_name.endswith("w2.weight"):
            param_data[expert_id, :, :] = loaded_weight[:, shard]

    defforward(self, hidden_states: torch.Tensor) -> torch.Tensor:
        num_tokens, hidden_size = hidden_states.shape
        hidden_states = hidden_states.view(-1, self.hidden_size)
        # router_logits: (num_tokens, n_experts)
        router_logits, _ = self.gate(hidden_states)

        topk_weights, topk_ids, _ = fused_topk(
            hidden_states, router_logits, self.top_k, renormalize=True
        )

        final_hidden_states = fused_experts(
            hidden_states, self.ws, self.w2s, topk_weights, topk_ids, inplace=False
        )

        if self.tp_size > 1:
            final_hidden_states = tensor_model_parallel_all_reduce(final_hidden_states)

        return final_hidden_states.view(num_tokens, hidden_size)
```