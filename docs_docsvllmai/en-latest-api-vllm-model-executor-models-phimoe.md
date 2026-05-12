---
title: phimoe - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/phimoe/
source: sitemap
fetched_at: 2026-05-07T21:32:41.9401178-03:00
rendered_js: false
word_count: 0
summary: This document defines the PhiMoE class, a PyTorch module implementing a tensor-parallel Mixture-of-Experts architecture that shards expert weights across multiple ranks.
tags:
    - mixture-of-experts
    - tensor-parallelism
    - neural-network-layers
    - pytorch-implementation
    - distributed-computing
category: reference
---

```
classPhiMoE(nn.Module):
"""A tensor-parallel MoE implementation for PhiMoE that shards each expert
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
        quant_config: QuantizationConfig | None = None,
        tp_size: int | None = None,
        prefix: str = "",
    ):
        super().__init__()
        self.hidden_size = hidden_size

        # Gate always runs at half / full precision for now.
        self.gate = ReplicatedLinear(
            hidden_size,
            num_experts,
            bias=False,
            params_dtype=params_dtype,
            quant_config=None,
            prefix=f"{prefix}.gate",
        )

        self.experts = FusedMoE(
            num_experts=num_experts,
            top_k=top_k,
            hidden_size=hidden_size,
            intermediate_size=intermediate_size,
            params_dtype=params_dtype,
            renormalize=False,
            quant_config=quant_config,
            tp_size=tp_size,
            custom_routing_function=phimoe_routing_function,
            prefix=f"{prefix}.experts",
        )

    defforward(self, hidden_states: torch.Tensor) -> torch.Tensor:
        # NOTE: hidden_states can have either 1D or 2D shape.
        orig_shape = hidden_states.shape
        hidden_states = hidden_states.view(-1, self.hidden_size)
        # router_logits: (num_tokens, n_experts)
        router_logits, _ = self.gate(hidden_states)
        final_hidden_states = self.experts(hidden_states, router_logits)
        return final_hidden_states.view(orig_shape)
```