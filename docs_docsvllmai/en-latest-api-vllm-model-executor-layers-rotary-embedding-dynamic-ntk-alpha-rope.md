---
title: dynamic_ntk_alpha_rope - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/rotary_embedding/dynamic_ntk_alpha_rope/
source: sitemap
fetched_at: 2026-05-07T21:28:16.973709529-03:00
rendered_js: false
word_count: 22
summary: This document defines the DynamicNTKAlphaRotaryEmbedding class, which extends standard rotary positional embeddings with dynamic NTK alpha scaling for improved long-context handling.
tags:
    - vllm
    - rotary-embedding
    - ntk-scaling
    - neural-network-layers
    - pytorch
    - positional-encoding
category: reference
---

## vllm.model\_executor.layers.rotary\_embedding.dynamic\_ntk\_alpha\_rope [¶](#vllm.model_executor.layers.rotary_embedding.dynamic_ntk_alpha_rope "Permanent link")

## DynamicNTKAlphaRotaryEmbedding [¶](#vllm.model_executor.layers.rotary_embedding.dynamic_ntk_alpha_rope.DynamicNTKAlphaRotaryEmbedding "Permanent link")

Bases: `RotaryEmbedding`

RotaryEmbedding extended with Dynamic NTK alpha.

Based on the original RotaryEmbedding implementation.

Source code in `vllm/model_executor/layers/rotary_embedding/dynamic_ntk_alpha_rope.py`

```
classDynamicNTKAlphaRotaryEmbedding(RotaryEmbedding):
"""RotaryEmbedding extended with Dynamic NTK alpha.

    Based on the original RotaryEmbedding implementation.
    """

    def__init__(
        self,
        head_size: int,
        rotary_dim: int,
        max_position_embeddings: int,
        base: float,
        is_neox_style: bool,
        scaling_alpha: float,
        dtype: torch.dtype,
    ) -> None:
        self.scaling_alpha = scaling_alpha
        super().__init__(
            head_size, rotary_dim, max_position_embeddings, base, is_neox_style, dtype
        )

    def_compute_cos_sin_cache(self) -> torch.Tensor:
        # For Hunyuan DynamicNTKAlphaRotaryEmbedding
        max_len = self.max_position_embeddings
        base = self.base * self.scaling_alpha ** (
            self.rotary_dim / (self.rotary_dim - 2)
        )
        inv_freq = self._compute_inv_freq(base)
        t = torch.arange(max_len, dtype=torch.float)

        freqs = torch.einsum("i,j -> ij", t, inv_freq)
        cos = freqs.cos()
        sin = freqs.sin()
        cache = torch.cat((cos, sin), dim=-1)
        return cache
```