---
title: gemma4_rope - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/rotary_embedding/gemma4_rope/
source: sitemap
fetched_at: 2026-05-07T21:28:20.777754456-03:00
rendered_js: false
word_count: 139
summary: This document describes the implementation of Gemma4-specific proportional Rotary Positional Embeddings (RoPE) within the vLLM framework, detailing how frequency computation and zero-padding are handled to maintain compatibility with Hugging Face transformers.
tags:
    - gemma4
    - rotary-embedding
    - rope
    - vllm
    - positional-encoding
    - deep-learning
category: reference
---

## vllm.model\_executor.layers.rotary\_embedding.gemma4\_rope [¶](#vllm.model_executor.layers.rotary_embedding.gemma4_rope "Permanent link")

Gemma4-specific Rotary Positional Embeddings (proportional scaling).

Gemma4 uses "proportional" RoPE which computes inv\_freq frequencies scaled by head\_dim (not rotary\_dim), and zero-pads for non-rotated dimensions when partial\_rotary\_factor &lt; 1. The actual rotation uses standard neox-style rotate\_half, matching HF transformers' apply\_rotary\_pos\_emb.

## Gemma4RotaryEmbedding [¶](#vllm.model_executor.layers.rotary_embedding.gemma4_rope.Gemma4RotaryEmbedding "Permanent link")

Bases: `RotaryEmbedding`

Gemma4 proportional RoPE.

Extends RotaryEmbedding (which provides standard neox-style rotation via ops.rotary\_embedding CUDA kernel) but overrides the inv\_freq computation to match HF's \_compute\_proportional\_rope\_parameters: - Frequency exponents use head\_dim (not rotary\_dim) as denominator - Non-rotated dims are zero-padded (cos=1, sin=0 = identity rotation)

When partial\_rotary\_factor=1.0 (the default for some variants), ALL dims are rotated and this is equivalent to standard RotaryEmbedding with head\_dim-scaled frequencies.

Source code in `vllm/model_executor/layers/rotary_embedding/gemma4_rope.py`

```
classGemma4RotaryEmbedding(RotaryEmbedding):
"""Gemma4 proportional RoPE.

    Extends RotaryEmbedding (which provides standard neox-style rotation
    via ops.rotary_embedding CUDA kernel) but overrides the inv_freq
    computation to match HF's _compute_proportional_rope_parameters:
    - Frequency exponents use head_dim (not rotary_dim) as denominator
    - Non-rotated dims are zero-padded (cos=1, sin=0 = identity rotation)

    When partial_rotary_factor=1.0 (the default for some variants), ALL dims are
    rotated and this is equivalent to standard RotaryEmbedding with
    head_dim-scaled frequencies.
    """

    def__init__(
        self,
        head_size: int,
        rotary_dim: int,
        max_position_embeddings: int,
        base: float,
        is_neox_style: bool,
        dtype: torch.dtype,
    ) -> None:
        # Number of rotation angle pairs (from partial_rotary_factor)
        self.rope_angles = rotary_dim // 2
        # Non-rotated angle pairs per half
        self.nope_angles = (head_size // 2) - self.rope_angles

        # Important: set rotary_dim = head_size so the base class's
        # forward_static applies rotation to ALL dims of the cos/sin cache.
        # The non-rotated dims will have cos=1, sin=0 (identity) thanks
        # to our _compute_inv_freq zero-padding.
        super().__init__(
            head_size,
            head_size,  # rotary_dim = head_size (full application)
            max_position_embeddings,
            base,
            is_neox_style,
            dtype,
        )

    def_compute_inv_freq(self, base: float) -> torch.Tensor:
"""Compute frequencies matching HF proportional RoPE.

        Key difference from base: exponent denominator is head_size (not
        rotary_dim), and non-rotated dims are zero-padded.
        """
        # HF formula: base ** (arange(0, 2*rope_angles, 2) / head_dim)
        freq_exponents = (
            torch.arange(0, 2 * self.rope_angles, 2, dtype=torch.float) / self.head_size
        )
        inv_freq = 1.0 / (base**freq_exponents)

        # Zero-pad for non-rotated dims (identity rotation: cos=1, sin=0)
        if self.nope_angles > 0:
            inv_freq = torch.cat(
                [
                    inv_freq,
                    torch.zeros(self.nope_angles, dtype=torch.float),
                ]
            )
        return inv_freq

    defextra_repr(self) -> str:
        s = f"head_size={self.head_size}, rotary_dim={self.rotary_dim}"
        s += f", rope_angles={self.rope_angles}, nope_angles={self.nope_angles}"
        s += f", max_position_embeddings={self.max_position_embeddings}"
        s += f", base={self.base}, is_neox_style={self.is_neox_style}"
        return s
```

### \_compute\_inv\_freq [¶](#vllm.model_executor.layers.rotary_embedding.gemma4_rope.Gemma4RotaryEmbedding._compute_inv_freq "Permanent link")

Compute frequencies matching HF proportional RoPE.

Key difference from base: exponent denominator is head\_size (not rotary\_dim), and non-rotated dims are zero-padded.

Source code in `vllm/model_executor/layers/rotary_embedding/gemma4_rope.py`

```
def_compute_inv_freq(self, base: float) -> torch.Tensor:
"""Compute frequencies matching HF proportional RoPE.

    Key difference from base: exponent denominator is head_size (not
    rotary_dim), and non-rotated dims are zero-padded.
    """
    # HF formula: base ** (arange(0, 2*rope_angles, 2) / head_dim)
    freq_exponents = (
        torch.arange(0, 2 * self.rope_angles, 2, dtype=torch.float) / self.head_size
    )
    inv_freq = 1.0 / (base**freq_exponents)

    # Zero-pad for non-rotated dims (identity rotation: cos=1, sin=0)
    if self.nope_angles > 0:
        inv_freq = torch.cat(
            [
                inv_freq,
                torch.zeros(self.nope_angles, dtype=torch.float),
            ]
        )
    return inv_freq
```