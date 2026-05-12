---
title: extract_hidden_states - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/extract_hidden_states/
source: sitemap
fetched_at: 2026-05-07T21:29:58.837308179-03:00
rendered_js: false
word_count: 0
summary: This document defines a specialized attention layer class for storing key-value states in a cache without performing standard attention computations. It provides mechanisms for initializing cache-only storage and integrating with the model's KV cache management system.
tags:
    - attention-mechanism
    - kv-cache
    - neural-network-layer
    - pytorch-module
    - tensor-caching
category: reference
---

```
classCacheOnlyAttentionLayer(nn.Module, AttentionLayerBase):
"""Attention layer that only caches key/value states without computing attention."""

    def__init__(
        self,
        num_heads: int,
        head_size: int,
        cache_config: CacheConfig | None = None,
        prefix: str = "",
        attn_type: str = AttentionType.DECODER,
    ):
        super().__init__()

        self.num_heads = num_heads
        self.head_size = head_size
        self.layer_name = prefix

        vllm_config = get_current_vllm_config()

        # KV cache configuration
        cache_config = cache_config or vllm_config.cache_config
        if cache_config is not None:
            kv_cache_dtype = cache_config.cache_dtype
            self.block_size = cache_config.block_size
        else:
            kv_cache_dtype = "auto"
            self.block_size = 16

        assert kv_cache_dtype in ["auto", "bfloat16", "float16"], (
            "CacheOnlyAttentionLayer doesn't currently support quantized kv cache but"
            f"kv cache dtype was set to {kv_cache_dtype}"
        )
        self.kv_cache_torch_dtype = kv_cache_dtype_str_to_dtype(
            kv_cache_dtype, vllm_config.model_config
        )

        # Initialize KV cache quantization attributes
        set_default_quant_scales(self, register_buffer=True)

        # Attention backend
        self.attn_backend = CacheOnlyAttentionBackend
        impl_cls = self.attn_backend.get_impl_cls()
        self.impl = impl_cls(
            num_heads,
            head_size,
            kv_cache_dtype,
            self.kv_cache_torch_dtype,
            attn_type,
        )

        assert not self.attn_backend.forward_includes_kv_cache_update, (
            "KV cache update should be independent of forward"
        )

        # Placeholder KV cache (replaced by bind_kv_cache)
        self.kv_cache = torch.tensor([])

        # Register in compilation context
        compilation_config = vllm_config.compilation_config
        if prefix in compilation_config.static_forward_context:
            raise ValueError(f"Duplicate layer name: {prefix}")
        compilation_config.static_forward_context[prefix] = self

    defforward(self, to_cache: torch.Tensor) -> torch.Tensor:
"""Cache hidden states as KV pairs without computing attention.

        Args:
            to_cache: The tensor to insert into the kv cache.
                shape [num_tokens, num_heads, head_size]

        Returns:
            Dummy output tensor (not used)
        """
        # Note: we set num_heads to num_hidden_layers and
        # head_size to hidden_size for hidden states storage
        output = torch.empty(0, device=to_cache.device, dtype=to_cache.dtype)

        # Note: dummy_out is used to force torch.compile to preserve ordering between
        # cache update and attention op (which triggers kv_connector transfer)
        dummy_out = unified_kv_cache_update(to_cache, self.layer_name)

        # Triggers kv_connector transfer via decorator
        _ = dummy_attention(self.layer_name, dummy_out)

        return output

    defget_attn_backend(self) -> type[AttentionBackend]:
        return self.attn_backend

    defget_kv_cache_spec(self, vllm_config: VllmConfig) -> KVCacheSpec:
        # Note: we use MLAAttentionSpec here to because it will
        # produce page sizes of (block_size * num_kv_heads * head_size * dtype_size)
        # whereas FullAttentionSpec will add an additional factor of 2
        return MLAAttentionSpec(
            block_size=self.block_size,
            num_kv_heads=self.num_heads,
            head_size=self.head_size,
            dtype=self.kv_cache_torch_dtype,
        )
```