---
title: encoder_only_attention - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/attention/encoder_only_attention/
source: sitemap
fetched_at: 2026-05-07T21:24:01.091477101-03:00
rendered_js: false
word_count: 22
summary: This document defines the EncoderOnlyAttention class in vLLM, which implements attention mechanisms for encoder-only models that do not require a key-value cache.
tags:
    - vllm
    - encoder-only
    - attention-mechanism
    - machine-learning
    - model-execution
category: reference
---

## vllm.model\_executor.layers.attention.encoder\_only\_attention [¶](#vllm.model_executor.layers.attention.encoder_only_attention "Permanent link")

## EncoderOnlyAttention [¶](#vllm.model_executor.layers.attention.encoder_only_attention.EncoderOnlyAttention "Permanent link")

Bases: `Attention`

Encoder attention is a special case that doesn't need a KV Cache.

Source code in `vllm/model_executor/layers/attention/encoder_only_attention.py`

```
classEncoderOnlyAttention(Attention):
"""
    Encoder attention is a special case that doesn't need a KV Cache.
    """

    def__init__(
        self,
        num_heads: int,
        head_size: int,
        scale: float,
        cache_config: CacheConfig | None = None,
        attn_type: str | None = None,
        **kwargs,
    ):
        dtype = torch.get_default_dtype()

        if cache_config is not None:
            kv_cache_dtype = cache_config.cache_dtype
        else:
            kv_cache_dtype = "auto"

        underlying_attn_backend = get_attn_backend(
            head_size,
            dtype,
            kv_cache_dtype,
            attn_type=AttentionType.ENCODER_ONLY,
        )

        attn_backend = create_encoder_only_attention_backend(underlying_attn_backend)

        if attn_type is not None:
            assert attn_type == AttentionType.ENCODER_ONLY, (
                "EncoderOnlyAttention only supports AttentionType.ENCODER_ONLY"
            )

        super().__init__(
            num_heads=num_heads,
            head_size=head_size,
            scale=scale,
            cache_config=cache_config,
            attn_backend=attn_backend,
            attn_type=AttentionType.ENCODER_ONLY,
            **kwargs,
        )

    defget_kv_cache_spec(self, vllm_config: VllmConfig) -> KVCacheSpec | None:
        # Does not need KV cache
        return None
```