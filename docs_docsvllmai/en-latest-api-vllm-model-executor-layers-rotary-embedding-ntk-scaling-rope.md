---
title: ntk_scaling_rope - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/rotary_embedding/ntk_scaling_rope/
source: sitemap
fetched_at: 2026-05-07T21:28:26.967941181-03:00
rendered_js: false
word_count: 19
summary: This document defines the NTKScalingRotaryEmbedding class, which extends rotary position embeddings with support for fixed and mixed Neural Tangent Kernel (NTK) scaling to improve context window handling.
tags:
    - vllm
    - rotary-embedding
    - ntk-scaling
    - neural-networks
    - positional-encoding
    - deep-learning
category: reference
---

## vllm.model\_executor.layers.rotary\_embedding.ntk\_scaling\_rope [¶](#vllm.model_executor.layers.rotary_embedding.ntk_scaling_rope "Permanent link")

## NTKScalingRotaryEmbedding [¶](#vllm.model_executor.layers.rotary_embedding.ntk_scaling_rope.NTKScalingRotaryEmbedding "Permanent link")

Bases: `RotaryEmbedding`

RotaryEmbedding extended with fixed and mixed NTK scaling. https://kexue.fm/archives/9706

Source code in `vllm/model_executor/layers/rotary_embedding/ntk_scaling_rope.py`

```
classNTKScalingRotaryEmbedding(RotaryEmbedding):
"""RotaryEmbedding extended with fixed and mixed NTK scaling.
    https://kexue.fm/archives/9706"""

    def__init__(
        self,
        head_size: int,
        rotary_dim: int,
        max_position_embeddings: int,
        base: float,
        is_neox_style: bool,
        scaling_factor: float,
        dtype: torch.dtype,
        mixed_b: float | None = None,
    ) -> None:
        self.scaling_factor = scaling_factor
        self.mixed_b = mixed_b
        super().__init__(
            head_size, rotary_dim, max_position_embeddings, base, is_neox_style, dtype
        )

    def_compute_inv_freq(self, base: float) -> torch.Tensor:
        base = self.base * (self.scaling_factor if self.mixed_b is None else 1)
        inv_freq = super()._compute_inv_freq(base)

        if self.mixed_b is None:
            inv_freq = inv_freq / self.scaling_factor ** (2 / self.rotary_dim)
        else:
            a = (
                torch.tensor(self.scaling_factor).log()
                / (self.rotary_dim / 2) ** self.mixed_b
            )
            lambda_1_m = (
                a * torch.arange(1, self.rotary_dim // 2 + 1).float() ** self.mixed_b
            ).exp()
            inv_freq = inv_freq / lambda_1_m

        return inv_freq
```