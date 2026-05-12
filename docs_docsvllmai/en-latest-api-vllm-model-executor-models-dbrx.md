---
title: dbrx - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/dbrx/
source: sitemap
fetched_at: 2026-05-07T21:29:31.780441146-03:00
rendered_js: false
word_count: 39
summary: This document describes the DbrxMoE class, which implements a tensor-parallel Mixture-of-Experts architecture using sharded weights and fused kernels for distributed forward passes.
tags:
    - dbrx
    - mixture-of-experts
    - tensor-parallelism
    - neural-networks
    - distributed-computing
    - deep-learning
category: reference
---

Bases: `Module`

A tensor-parallel MoE implementation for DBRX.

Each expert's weights are sharded across all ranks and a fused MoE kernel is used for the forward pass, and finally we reduce the outputs across ranks.

Source code in `vllm/model_executor/models/dbrx.py`

```
classDbrxMoE(nn.Module):
"""A tensor-parallel MoE implementation for DBRX.

    Each expert's weights are sharded across all ranks and a fused MoE
    kernel is used for the forward pass, and finally we reduce the outputs
    across ranks.
    """

    def__init__(
        self,
        config: DbrxConfig,
        quant_config: QuantizationConfig | None = None,
        params_dtype: torch.dtype | None = None,
        prefix: str = "",
    ):
        super().__init__()
        self.d_model = config.d_model
        if params_dtype is None:
            params_dtype = torch.get_default_dtype()
        self.params_dtype = params_dtype

        self.router = DbrxRouter(config, self.params_dtype)

        self.experts = DbrxExperts(
            config=config,
            quant_config=quant_config,
            params_dtype=self.params_dtype,
            prefix=f"{prefix}.experts",
        )

    defforward(self, hidden_states: torch.Tensor) -> torch.Tensor:
        orig_shape = hidden_states.shape
        hidden_states = hidden_states.view(-1, self.d_model)
        # router_logits: (num_tokens, n_experts)
        router_logits = self.router(hidden_states)
        final_hidden_states = self.experts(hidden_states, router_logits)
        return final_hidden_states.view(orig_shape)
```