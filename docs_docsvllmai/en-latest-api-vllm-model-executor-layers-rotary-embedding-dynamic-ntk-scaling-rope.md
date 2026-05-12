---
title: dynamic_ntk_scaling_rope - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/rotary_embedding/dynamic_ntk_scaling_rope/
source: sitemap
fetched_at: 2026-05-07T21:28:17.909127039-03:00
rendered_js: false
word_count: 24
summary: This document defines the DynamicNTKScalingRotaryEmbedding class, which extends standard Rotary Embeddings with dynamic NTK scaling to support longer sequence lengths in transformer models.
tags:
    - vllm
    - rotary-embedding
    - ntk-scaling
    - neural-network-layers
    - model-execution
category: reference
---

## vllm.model\_executor.layers.rotary\_embedding.dynamic\_ntk\_scaling\_rope [¶](#vllm.model_executor.layers.rotary_embedding.dynamic_ntk_scaling_rope "Permanent link")

## DynamicNTKScalingRotaryEmbedding [¶](#vllm.model_executor.layers.rotary_embedding.dynamic_ntk_scaling_rope.DynamicNTKScalingRotaryEmbedding "Permanent link")

Bases: `RotaryEmbedding`

RotaryEmbedding extended with Dynamic NTK scaling.

Credits to the Reddit users /u/bloc97 and /u/emozilla

Source code in `vllm/model_executor/layers/rotary_embedding/dynamic_ntk_scaling_rope.py`

```
classDynamicNTKScalingRotaryEmbedding(RotaryEmbedding):
"""RotaryEmbedding extended with Dynamic NTK scaling.

    Credits to the Reddit users /u/bloc97 and /u/emozilla
    """

    def__init__(
        self,
        head_size: int,
        rotary_dim: int,
        max_position_embeddings: int,
        base: float,
        is_neox_style: bool,
        scaling_factor: float,
        dtype: torch.dtype,
    ) -> None:
        self.scaling_factor = scaling_factor
        super().__init__(
            head_size, rotary_dim, max_position_embeddings, base, is_neox_style, dtype
        )

    def_compute_cos_sin_cache(self) -> torch.Tensor:
        # NOTE(woosuk): self.max_position_embeddings is the original
        # maximum length before applying the rope scaling.
        # Thus, the maximum length after applying the rope scaling is
        # self.max_position_embeddings * self.scaling_factor.
        max_len = self.max_position_embeddings * self.scaling_factor
        base = self.base * (
            (self.scaling_factor * max_len / self.max_position_embeddings)
            - (self.scaling_factor - 1)
        ) ** (self.rotary_dim / (self.rotary_dim - 2))
        inv_freq = self._compute_inv_freq(base)
        t = torch.arange(max_len, dtype=torch.float)

        freqs = torch.einsum("i,j -> ij", t, inv_freq)
        cos = freqs.cos()
        sin = freqs.sin()
        cache = torch.cat((cos, sin), dim=-1)
        return cache
```