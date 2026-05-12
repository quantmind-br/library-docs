---
title: flex_olmo - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/flex_olmo/
source: sitemap
fetched_at: 2026-05-07T21:30:05.221795586-03:00
rendered_js: false
word_count: 57
summary: This document provides the technical implementation details for the FlexOlmoMoE model, specifically focusing on its tensor-parallel mixture-of-experts architecture within the vLLM framework.
tags:
    - vllm
    - flex-olmo
    - moe
    - tensor-parallelism
    - model-executor
    - deep-learning
category: reference
---

## vllm.model\_executor.models.flex\_olmo [¶](#vllm.model_executor.models.flex_olmo "Permanent link")

Inference-only FlexOlmo model compatible with HuggingFace weights.

## FlexOlmoMoE [¶](#vllm.model_executor.models.flex_olmo.FlexOlmoMoE "Permanent link")

Bases: `Module`

A tensor-parallel MoE implementation for FlexOlmo that shards each expert across all ranks.

Each expert's weights are sharded across all ranks and a fused MoE kernel is used for the forward pass, and finally we reduce the outputs across ranks.

Source code in `vllm/model_executor/models/flex_olmo.py`

```
classFlexOlmoMoE(nn.Module):
"""A tensor-parallel MoE implementation for FlexOlmo that shards each expert
    across all ranks.

    Each expert's weights are sharded across all ranks and a fused MoE
    kernel is used for the forward pass, and finally we reduce the outputs
    across ranks.
    """

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()

        hf_config = vllm_config.model_config.hf_config
        assert isinstance(hf_config, FlexOlmoConfig)

        tp_size = get_tensor_model_parallel_world_size()

        # Gate always runs at half / full precision for now.
        self.gate = ReplicatedLinear(
            hf_config.hidden_size,
            hf_config.num_experts,
            bias=False,
            return_bias=False,
            quant_config=None,
            prefix=f"{prefix}.gate",
        )

        self.experts = FusedMoE(
            num_experts=hf_config.num_experts,
            top_k=hf_config.num_experts_per_tok,
            hidden_size=hf_config.hidden_size,
            intermediate_size=hf_config.intermediate_size,
            renormalize=False,
            quant_config=None,
            tp_size=tp_size,
            prefix=f"{prefix}.experts",
            router_logits_dtype=torch.float32,
        )

        self.top_k = hf_config.num_experts_per_tok

    defforward(self, hidden_states: torch.Tensor) -> torch.Tensor:
        # NOTE: hidden_states can have either 1D or 2D shape.
        orig_shape = hidden_states.shape
        hidden_dim = hidden_states.shape[-1]
        hidden_states = hidden_states.view(-1, hidden_dim)

        # router_logits: (num_tokens, n_experts)
        router_logits = self.gate(hidden_states)
        # Warning: The experts mutate the hidden state input! This messes up
        # basic things like the residual stream.
        final_hidden_states = self.experts(
            hidden_states=hidden_states.detach().clone(),
            router_logits=router_logits.float(),
        )

        return final_hidden_states.view(orig_shape)
```