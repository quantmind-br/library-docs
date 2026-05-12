---
title: whisper_causal - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/whisper_causal/
source: sitemap
fetched_at: 2026-05-07T21:33:48.033157341-03:00
rendered_js: false
word_count: 0
summary: Defines a Whisper causal attention layer implementation that incorporates block pooling for optimized KV cache management.
tags:
    - deep-learning
    - attention-mechanism
    - whisper-model
    - kv-cache
    - neural-network-layers
category: concept
---

```
classWhisperCausalAttentionWithBlockPooling(Attention):
"""Attention layer with block pooling."""

    def__init__(
        self,
        num_heads: int,
        head_size: int,
        scale: float,
        num_kv_heads: int | None = None,
        alibi_slopes: list[float] | None = None,
        cache_config: CacheConfig | None = None,
        quant_config: QuantizationConfig | None = None,
        logits_soft_cap: float | None = None,
        per_layer_sliding_window: int | None = None,
        prefix: str = "",
        attn_type: str = AttentionType.DECODER,
        kv_sharing_target_layer_name: str | None = None,
        block_pool_size: int = 1,
        attn_backend: type[AttentionBackend] | None = None,
        **extra_impl_args,
    ) -> None:
        self.block_pool_size = block_pool_size
        dtype = torch.get_default_dtype()

        if cache_config is not None:
            kv_cache_dtype = cache_config.cache_dtype
        else:
            kv_cache_dtype = "auto"

        underlying_attn_backend = get_attn_backend(
            head_size,
            dtype,
            kv_cache_dtype,
            attn_type=attn_type,
        )
        attn_backend = create_whisper_attention_backend_with_block_pooling(
            underlying_attn_backend, block_pool_size
        )

        super().__init__(
            num_heads=num_heads,
            head_size=head_size,
            scale=scale,
            num_kv_heads=num_kv_heads,
            alibi_slopes=alibi_slopes,
            cache_config=cache_config,
            quant_config=quant_config,
            logits_soft_cap=logits_soft_cap,
            per_layer_sliding_window=per_layer_sliding_window,
            prefix=prefix,
            attn_type=attn_type,
            kv_sharing_target_layer_name=kv_sharing_target_layer_name,
            attn_backend=attn_backend,
            **extra_impl_args,
        )

    defget_kv_cache_spec(self, vllm_config: VllmConfig):
        kv_cache_spec = super().get_kv_cache_spec(vllm_config)
        assert isinstance(kv_cache_spec, AttentionSpec)
        kv_cache_spec = replace(
            kv_cache_spec,
            num_kv_heads=self.block_pool_size * kv_cache_spec.num_kv_heads,
        )
        return kv_cache_spec
```