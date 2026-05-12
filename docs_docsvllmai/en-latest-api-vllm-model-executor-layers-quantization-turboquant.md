---
title: turboquant - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/turboquant/
source: sitemap
fetched_at: 2026-05-07T21:27:45.162225854-03:00
rendered_js: false
word_count: 529
summary: This document describes the configuration parameters and implementation details for TurboQuant, a KV-cache quantization method that utilizes Hadamard rotation, Lloyd-Max scalar quantization, and uniform value quantization to compress attention cache.
tags:
    - kv-cache
    - quantization
    - turboquant
    - llm-optimization
    - vllm
    - hadamard-rotation
category: configuration
---

Configuration for TurboQuant KV-cache quantization.

Applies Hadamard rotation followed by per-coordinate Lloyd-Max scalar quantization for keys, and uniform quantization for values.

Historical note: this is the scalar case of the HIGGS quantization method (Malinovskii et al., "Pushing the Limits of Large Language Model Quantization via the Linearity Theorem", NAACL 2025; preprint arXiv:2411.17525): rotation + optimized grid + optional re-normalization, applied to KV cache compression. A first application of this approach to KV-cache compression is in "Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models" (Shutova et al., ICML 2025; preprint arXiv:2501.19392). Both these references pre-date the TurboQuant paper.

QJL is intentionally omitted — community consensus (5+ independent groups) found it hurts attention quality by amplifying variance through softmax.

Named presets (use via --kv-cache-dtype): turboquant\_k8v4: FP8 keys + 4-bit values, 2.6x, +1.17% PPL turboquant\_4bit\_nc: 4-bit MSE keys + 4-bit values + NC, 3.8x, +2.71% turboquant\_k3v4\_nc: 3-bit MSE keys + 4-bit values + NC, ~3.5x, +10.63% turboquant\_3bit\_nc: 3-bit MSE keys + 3-bit values + NC, 4.9x, +20.59%

Parameters:

Name Type Description Default `head_dim` `int`

Attention head dimension (e.g. 64, 96, 128).

`128` `key_quant_bits` `int`

Bits for key quantization. 8 = FP8 keys (no rotation/MSE). 3-4 = Lloyd-Max MSE quantized keys.

`3` `value_quant_bits` `int`

Bits per value dimension for uniform quantization. 3 = 8 levels, 4 = 16 levels (default).

`4` `norm_correction` `bool`

Re-normalize centroid vectors to unit norm before inverse rotation during dequant. Fixes quantization-induced norm distortion, improving PPL by ~0.8% at 4-bit.

`False`

Source code in `vllm/model_executor/layers/quantization/turboquant/config.py`

```
@dataclass
classTurboQuantConfig:
"""Configuration for TurboQuant KV-cache quantization.

    Applies Hadamard rotation followed by per-coordinate Lloyd-Max scalar
    quantization for keys, and uniform quantization for values.

    Historical note: this is the scalar case of the HIGGS quantization
    method (Malinovskii et al., "Pushing the Limits of Large Language Model
    Quantization via the Linearity Theorem", NAACL 2025; preprint
    arXiv:2411.17525): rotation + optimized grid + optional re-normalization,
    applied to KV cache compression. A first application of this approach to
    KV-cache compression is in "Cache Me If You Must: Adaptive Key-Value
    Quantization for Large Language Models" (Shutova et al., ICML 2025;
    preprint arXiv:2501.19392). Both these references pre-date the
    TurboQuant paper.

    QJL is intentionally omitted — community consensus (5+ independent
    groups) found it hurts attention quality by amplifying variance through
    softmax.

    Named presets (use via --kv-cache-dtype):
        turboquant_k8v4:   FP8 keys + 4-bit values, 2.6x, +1.17% PPL
        turboquant_4bit_nc: 4-bit MSE keys + 4-bit values + NC, 3.8x, +2.71%
        turboquant_k3v4_nc: 3-bit MSE keys + 4-bit values + NC, ~3.5x, +10.63%
        turboquant_3bit_nc: 3-bit MSE keys + 3-bit values + NC, 4.9x, +20.59%

    Args:
        head_dim: Attention head dimension (e.g. 64, 96, 128).
        key_quant_bits: Bits for key quantization. 8 = FP8 keys (no
            rotation/MSE). 3-4 = Lloyd-Max MSE quantized keys.
        value_quant_bits: Bits per value dimension for uniform quantization.
            3 = 8 levels, 4 = 16 levels (default).
        norm_correction: Re-normalize centroid vectors to unit norm before
            inverse rotation during dequant. Fixes quantization-induced norm
            distortion, improving PPL by ~0.8% at 4-bit.
    """

    head_dim: int = 128
    key_quant_bits: int = 3  # 3-4 = MSE keys, 8 = FP8 keys
    value_quant_bits: int = 4  # 3-4 = uniform quantized values
    seed: int = 42  # kept for backward compatibility; no longer used internally
    norm_correction: bool = False

    @property
    defkey_fp8(self) -> bool:
"""Whether keys are stored as FP8 — no rotation/quantization needed."""
        return self.key_quant_bits == 8

    @property
    defmse_bits(self) -> int:
"""MSE quantizer bit-width (determines centroid count: 2^mse_bits).

        For MSE key modes, equals key_quant_bits.
        For FP8 key mode, falls back to value_quant_bits (centroids are still
        needed for continuation-prefill dequant and decode kernel params).
        """
        if self.key_fp8:
            return self.value_quant_bits
        return self.key_quant_bits

    @property
    defkey_mse_bits(self) -> int:
"""MSE bits actually used for key quantization (0 if FP8 keys)."""
        if self.key_fp8:
            return 0
        return self.key_quant_bits

    @property
    defcentroid_bits(self) -> int:
"""Bits for centroid generation — always non-zero."""
        return self.mse_bits

    @property
    defn_centroids(self) -> int:
        return 2**self.mse_bits

    @property
    defkey_packed_size(self) -> int:
"""Packed bytes for a single KEY vector.

        FP8 mode (key_quant_bits=8):
          head_dim bytes (1 byte per element, no overhead).

        TQ mode:
          - MSE indices: ceil(head_dim * key_mse_bits / 8) bytes
          - vec_norm:     2 bytes (float16)
        """
        if self.key_fp8:
            return self.head_dim  # 1 byte per element
        mse_bytes = math.ceil(self.head_dim * self.key_mse_bits / 8)
        norm_bytes = 2  # vec_norm fp16
        return mse_bytes + norm_bytes

    @property
    defeffective_value_quant_bits(self) -> int:
"""Actual bits used for value storage."""
        return self.value_quant_bits

    @property
    defvalue_packed_size(self) -> int:
"""Packed bytes for a single VALUE vector.

        Uniform quantization: ceil(head_dim * bits / 8) + 4 bytes (scale + zero fp16).
        """
        data_bytes = math.ceil(self.head_dim * self.value_quant_bits / 8)
        return data_bytes + 4  # +2 scale(fp16) +2 zero(fp16)

    @property
    defslot_size(self) -> int:
"""Total packed bytes per head per position (key + value combined).

        Layout: [key_packed | value_packed]
        """
        return self.key_packed_size + self.value_packed_size

    @property
    defslot_size_aligned(self) -> int:
"""Slot size rounded up to next even number.

        Even-number is required so effective_head_size = slot_size_aligned // 2
        is integral.
        """
        s = self.slot_size
        return s + (s % 2)  # round up to even

    @staticmethod
    defget_boundary_skip_layers(
        model_config: ModelConfig,
        n: int = 2,
    ) -> list[str]:
"""Layer indices to skip TQ compression (boundary protection).

        For hybrid models (attention + Mamba/linear-attention), boundary
        protection is disabled — hybrids typically have only 8-12
        full-attention layers and a hard n=2 on each side would cover
        ~40 % of them.  The dense GSM8K baselines that motivate n=2
        don't apply to hybrids.

        For dense models, skips first N and last N attention layers.
        Empirically required for aggressive presets (k3v4_nc, 3bit_nc)
        — without it GSM8K drops ~30 points on Qwen3-4B.
        """
        if model_config.is_hybrid:
            attn_indices = _get_full_attention_layer_indices(model_config)
            if not attn_indices:
                raise NotImplementedError(
                    "TurboQuant KV cache requires identifiable "
                    "full-attention layers, but none were found in "
                    "the hybrid model config."
                )
            logger.info("TQ hybrid: full-attention layers %s", attn_indices)
            return []

        num_layers = model_config.hf_text_config.num_hidden_layers
        if n <= 0 or num_layers <= 0:
            return []
        n = min(n, num_layers // 2)  # don't skip more than half
        first = list(range(n))
        last = list(range(num_layers - n, num_layers))
        # Deduplicate (if num_layers <= 2*n)
        indices = sorted(set(first + last))
        return [str(i) for i in indices]

    @staticmethod
    deffrom_cache_dtype(cache_dtype: str, head_dim: int) -> TurboQuantConfig:
"""Create config from a named preset.

        Valid presets: turboquant_k8v4, turboquant_4bit_nc, etc.
        """
        if cache_dtype not in TQ_PRESETS:
            valid = ", ".join(TQ_PRESETS.keys())
            raise ValueError(
                f"Unknown TurboQuant cache dtype: {cache_dtype!r}. "
                f"Valid presets: {valid}"
            )
        preset = TQ_PRESETS[cache_dtype]
        return TurboQuantConfig(
            head_dim=head_dim,
            key_quant_bits=preset["key_quant_bits"],
            value_quant_bits=preset["value_quant_bits"],
            norm_correction=preset["norm_correction"],
        )
```

### centroid\_bits `property` [¶](#vllm.model_executor.layers.quantization.turboquant.TurboQuantConfig.centroid_bits "Permanent link")

Bits for centroid generation — always non-zero.

### effective\_value\_quant\_bits `property` [¶](#vllm.model_executor.layers.quantization.turboquant.TurboQuantConfig.effective_value_quant_bits "Permanent link")

```
effective_value_quant_bits: int
```

Actual bits used for value storage.

### key\_fp8 `property` [¶](#vllm.model_executor.layers.quantization.turboquant.TurboQuantConfig.key_fp8 "Permanent link")

Whether keys are stored as FP8 — no rotation/quantization needed.

### key\_mse\_bits `property` [¶](#vllm.model_executor.layers.quantization.turboquant.TurboQuantConfig.key_mse_bits "Permanent link")

MSE bits actually used for key quantization (0 if FP8 keys).

### key\_packed\_size `property` [¶](#vllm.model_executor.layers.quantization.turboquant.TurboQuantConfig.key_packed_size "Permanent link")

Packed bytes for a single KEY vector.

FP8 mode (key\_quant\_bits=8): head\_dim bytes (1 byte per element, no overhead).

TQ mode

- MSE indices: ceil(head\_dim * key\_mse\_bits / 8) bytes
- vec\_norm: 2 bytes (float16)

### mse\_bits `property` [¶](#vllm.model_executor.layers.quantization.turboquant.TurboQuantConfig.mse_bits "Permanent link")

MSE quantizer bit-width (determines centroid count: 2^mse\_bits).

For MSE key modes, equals key\_quant\_bits. For FP8 key mode, falls back to value\_quant\_bits (centroids are still needed for continuation-prefill dequant and decode kernel params).

### slot\_size `property` [¶](#vllm.model_executor.layers.quantization.turboquant.TurboQuantConfig.slot_size "Permanent link")

Total packed bytes per head per position (key + value combined).

Layout: \[key\_packed | value\_packed]

### slot\_size\_aligned `property` [¶](#vllm.model_executor.layers.quantization.turboquant.TurboQuantConfig.slot_size_aligned "Permanent link")

Slot size rounded up to next even number.

Even-number is required so effective\_head\_size = slot\_size\_aligned // 2 is integral.

### value\_packed\_size `property` [¶](#vllm.model_executor.layers.quantization.turboquant.TurboQuantConfig.value_packed_size "Permanent link")

Packed bytes for a single VALUE vector.

Uniform quantization: ceil(head\_dim * bits / 8) + 4 bytes (scale + zero fp16).

### from\_cache\_dtype `staticmethod` [¶](#vllm.model_executor.layers.quantization.turboquant.TurboQuantConfig.from_cache_dtype "Permanent link")

Create config from a named preset.

Valid presets: turboquant\_k8v4, turboquant\_4bit\_nc, etc.

Source code in `vllm/model_executor/layers/quantization/turboquant/config.py`

```
@staticmethod
deffrom_cache_dtype(cache_dtype: str, head_dim: int) -> TurboQuantConfig:
"""Create config from a named preset.

    Valid presets: turboquant_k8v4, turboquant_4bit_nc, etc.
    """
    if cache_dtype not in TQ_PRESETS:
        valid = ", ".join(TQ_PRESETS.keys())
        raise ValueError(
            f"Unknown TurboQuant cache dtype: {cache_dtype!r}. "
            f"Valid presets: {valid}"
        )
    preset = TQ_PRESETS[cache_dtype]
    return TurboQuantConfig(
        head_dim=head_dim,
        key_quant_bits=preset["key_quant_bits"],
        value_quant_bits=preset["value_quant_bits"],
        norm_correction=preset["norm_correction"],
    )
```

### get\_boundary\_skip\_layers `staticmethod` [¶](#vllm.model_executor.layers.quantization.turboquant.TurboQuantConfig.get_boundary_skip_layers "Permanent link")

Layer indices to skip TQ compression (boundary protection).

For hybrid models (attention + Mamba/linear-attention), boundary protection is disabled — hybrids typically have only 8-12 full-attention layers and a hard n=2 on each side would cover ~40 % of them. The dense GSM8K baselines that motivate n=2 don't apply to hybrids.

For dense models, skips first N and last N attention layers. Empirically required for aggressive presets (k3v4\_nc, 3bit\_nc) — without it GSM8K drops ~30 points on Qwen3-4B.

Source code in `vllm/model_executor/layers/quantization/turboquant/config.py`

```
@staticmethod
defget_boundary_skip_layers(
    model_config: ModelConfig,
    n: int = 2,
) -> list[str]:
"""Layer indices to skip TQ compression (boundary protection).

    For hybrid models (attention + Mamba/linear-attention), boundary
    protection is disabled — hybrids typically have only 8-12
    full-attention layers and a hard n=2 on each side would cover
    ~40 % of them.  The dense GSM8K baselines that motivate n=2
    don't apply to hybrids.

    For dense models, skips first N and last N attention layers.
    Empirically required for aggressive presets (k3v4_nc, 3bit_nc)
    — without it GSM8K drops ~30 points on Qwen3-4B.
    """
    if model_config.is_hybrid:
        attn_indices = _get_full_attention_layer_indices(model_config)
        if not attn_indices:
            raise NotImplementedError(
                "TurboQuant KV cache requires identifiable "
                "full-attention layers, but none were found in "
                "the hybrid model config."
            )
        logger.info("TQ hybrid: full-attention layers %s", attn_indices)
        return []

    num_layers = model_config.hf_text_config.num_hidden_layers
    if n <= 0 or num_layers <= 0:
        return []
    n = min(n, num_layers // 2)  # don't skip more than half
    first = list(range(n))
    last = list(range(num_layers - n, num_layers))
    # Deduplicate (if num_layers <= 2*n)
    indices = sorted(set(first + last))
    return [str(i) for i in indices]
```