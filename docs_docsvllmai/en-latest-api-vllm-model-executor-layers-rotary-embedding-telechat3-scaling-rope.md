---
title: telechat3_scaling_rope - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/rotary_embedding/telechat3_scaling_rope/
source: sitemap
fetched_at: 2026-05-07T21:28:28.84040359-03:00
rendered_js: false
word_count: 45
summary: This document defines the TeleChat3RoPEScaledRotaryEmbedding class, which implements a specific variant of the YaRN rotary embedding method for use within the vLLM model execution framework.
tags:
    - vllm
    - rotary-embedding
    - rope-scaling
    - telechat3
    - yarn-scaling
    - neural-network-layers
category: reference
---

## vllm.model\_executor.layers.rotary\_embedding.telechat3\_scaling\_rope [¶](#vllm.model_executor.layers.rotary_embedding.telechat3_scaling_rope "Permanent link")

## TeleChat3RoPEScaledRotaryEmbedding [¶](#vllm.model_executor.layers.rotary_embedding.telechat3_scaling_rope.TeleChat3RoPEScaledRotaryEmbedding "Permanent link")

Bases: `YaRNScalingRotaryEmbedding`

TeleChat3 uses a variant of YaRN method.

To achieve code reuse as much as possible, we have rewritten the `get_mscale` method in the initialization function

Source code in `vllm/model_executor/layers/rotary_embedding/telechat3_scaling_rope.py`

```
classTeleChat3RoPEScaledRotaryEmbedding(YaRNScalingRotaryEmbedding):
"""TeleChat3 uses a variant of YaRN method.

    To achieve code reuse as much as possible, we have rewritten the
    `get_mscale` method in the initialization function
    """

    def__init__(
        self,
        head_size: int,
        rotary_dim: int,
        max_position_embeddings: int,
        base: int,
        is_neox_style: bool,
        scaling_factor: float,
        dtype: torch.dtype,
        *,
        extrapolation_factor: float = 1,
        attn_factor: float = 1,
        beta_fast: int = 32,
        beta_slow: int = 1,
        truncate: bool = True,
    ) -> None:
        self.scaling_factor = scaling_factor
        self.extrapolation_factor = extrapolation_factor
        self.attn_factor = attn_factor
        self.beta_fast = beta_fast
        self.beta_slow = beta_slow
        self.truncate = truncate

        defget_mscale(scale, mscale=1):
            if scale <= 1:
                return 1.0
            return 0.07 * mscale * math.log(scale) + 1.0

        self.mscale = float(get_mscale(self.scaling_factor) * attn_factor)
        # Initialization must be performed after mscale, otherwise mscale is useless
        RotaryEmbedding.__init__(
            self,
            head_size,
            rotary_dim,
            max_position_embeddings,
            base,
            is_neox_style,
            dtype,
        )
```