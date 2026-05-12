---
title: arctic - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/arctic/
source: sitemap
fetched_at: 2026-05-07T21:29:02.676110109-03:00
rendered_js: false
word_count: 0
summary: Defines a model-parallel Mixture-of-Experts (MoE) neural network layer designed for efficient expert routing and fused computation in PyTorch models.
tags:
    - mixture-of-experts
    - model-parallelism
    - neural-network-layer
    - pytorch-implementation
    - tensor-parallelism
category: api
---

```
classArcticMoE(nn.Module):
"""
    Model-parallel implementation of Arctic MoE Layer.
    """

    def__init__(
        self,
        config: ArcticConfig,
        tp_size: int | None = None,
        params_dtype: torch.dtype | None = None,
        quant_config: QuantizationConfig | None = None,
        reduce_results: bool = True,
        prefix: str = "",
    ):
        super().__init__()

        layer_id = extract_layer_index(prefix)
        self.tp_size = tp_size or get_tensor_model_parallel_world_size()
        self.hidden_size = config.hidden_size
        self.num_experts = config.num_local_experts
        self.layer_id = layer_id
        self.top_k = config.num_experts_per_tok
        self.intermediate_size = config.intermediate_size // self.tp_size

        self.is_moe_layer = (layer_id + 1) % config.moe_layer_frequency == 0
        self.reduce_results = reduce_results
        # Some other parameters
        if params_dtype is None:
            params_dtype = torch.get_default_dtype()
        self.params_dtype = params_dtype

        if not self.is_moe_layer:
            self.mlp = ArcticMLP(
                config,
                quant_config=quant_config,
                reduce_results=reduce_results,
                prefix=f"{prefix}.mlp",
            )
        else:
            self.gate = ReplicatedLinear(
                self.hidden_size,
                self.num_experts,
                bias=False,
                params_dtype=self.params_dtype,
                quant_config=quant_config,
                prefix=f"{prefix}.gate",
            )
            self.ws = nn.Parameter(
                torch.empty(
                    self.num_experts,
                    2 * self.intermediate_size,
                    self.hidden_size,
                    device=current_platform.device_type,
                    dtype=self.params_dtype,
                )
            )
            self.w2s = nn.Parameter(
                torch.empty(
                    self.num_experts,
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

    deflocal_moe_fused(self, hidden_states: torch.Tensor) -> torch.Tensor:
        num_tokens, hidden_size = hidden_states.shape
        hidden_states = hidden_states.view(-1, self.hidden_size)
        # router_logits: (num_tokens, n_experts)
        router_logits, _ = self.gate(hidden_states)
        do_normalize = self.top_k > 1
        topk_weights, topk_ids, token_expert_indices = fused_topk(
            hidden_states, router_logits, self.top_k, renormalize=do_normalize
        )
        final_hidden_states = fused_experts(
            hidden_states,
            self.ws,
            self.w2s,
            topk_weights,
            topk_ids,
            inplace=True,
        )
        if self.reduce_results and self.tp_size > 1:
            final_hidden_states = tensor_model_parallel_all_reduce(final_hidden_states)
        return final_hidden_states.view(num_tokens, hidden_size)

    defforward(self, hidden_states: torch.Tensor):
        if self.is_moe_layer:
            final_hidden_states = self.local_moe_fused(hidden_states)
        else:
            final_hidden_states = self.mlp(hidden_states)
        return final_hidden_states
```