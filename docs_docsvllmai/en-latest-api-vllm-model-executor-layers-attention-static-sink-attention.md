---
title: static_sink_attention - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/attention/static_sink_attention/
source: sitemap
fetched_at: 2026-05-07T21:24:05.03378141-03:00
rendered_js: false
word_count: 0
summary: Defines a custom attention mechanism class with static sink token support, enabling specialized KV cache handling within the vLLM framework.
tags:
    - attention-mechanism
    - kv-cache
    - vllm
    - custom-op
    - deep-learning
    - transformer-optimization
category: concept
---

```
@CustomOp.register("static_sink_attention")
classStaticSinkAttention(Attention, CustomOp):
"""
    Attention with static sink tokens
    """

    def__init__(
        self,
        num_heads: int,
        head_size: int,
        scale: float,
        sink_len: int,
        attn_backend: type[AttentionBackend] | None = None,
        cache_config: CacheConfig | None = None,
        **kwargs,
    ):
        dtype = torch.get_default_dtype()

        if cache_config is not None:
            kv_cache_dtype = cache_config.cache_dtype
        else:
            kv_cache_dtype = "auto"

        if attn_backend is not None:
            underlying_attn_backend = attn_backend
        else:
            underlying_attn_backend = get_attn_backend(head_size, dtype, kv_cache_dtype)
        attn_backend = create_static_sink_attention_backend(
            underlying_attn_backend,  # type: ignore[arg-type]
            sink_len=sink_len,
        )
        Attention.__init__(
            self=self,
            num_heads=num_heads,
            head_size=head_size,
            scale=scale,
            cache_config=cache_config,
            attn_backend=attn_backend,
            **kwargs,
        )
        CustomOp.__init__(self)

        self.sink_len = sink_len
        self.sink_populated = False
        self.sink_key = None
        self.sink_value = None

    defupdate_sink_kv(self, sink_key, sink_value) -> None:
        self.sink_key = sink_key
        self.sink_value = sink_value

    defforward_native(
        self,
        query: torch.Tensor,
        key: torch.Tensor,
        value: torch.Tensor,
        output_shape: torch.Size | None = None,
    ) -> torch.Tensor:
        assert self.sink_key is not None and self.sink_value is not None, (
            "sink_key and sink_value have not been prepared"
        )
        if not self.sink_populated:
            self_kv_cache = self.kv_cache
            torch.ops.vllm.maybe_populate_sink(
                self_kv_cache, _encode_layer_name(self.layer_name)
            )

        return super().forward(query, key, value, output_shape)

    defforward_cuda(
        self,
        query: torch.Tensor,
        key: torch.Tensor,
        value: torch.Tensor,
        output_shape: torch.Size | None = None,
    ) -> torch.Tensor:
        return self.forward_native(query, key, value, output_shape)

    defforward(self, *args, **kwargs):
        return self._forward_method(*args, **kwargs)

    defpopulate_sink_kv(self, self_kv_cache):
        sink_kv_slot_mapping = torch.arange(
            self.block_size,
            self.sink_len + self.block_size,
            device=torch.accelerator.current_device_index(),
            dtype=torch.long,
        )
        triton_reshape_and_cache_flash_diffkv(
            self.sink_key,
            self.sink_value,
            self_kv_cache,
            sink_kv_slot_mapping,
            self.kv_cache_dtype,
            self._k_scale,
            self._v_scale,
        )
        # We only populate the sink_key and sink_value once
        self.sink_populated = True

    defget_kv_cache_spec(self, vllm_config: VllmConfig) -> KVCacheSpec:
        # Block size may get updated after model loading, refresh it
        self.block_size = vllm_config.cache_config.block_size
        # Should not be called for enc-dec or encoder-only attention.
        assert self.attn_type == AttentionType.DECODER

        return SinkFullAttentionSpec(
            block_size=self.block_size,
            num_kv_heads=self.num_kv_heads,
            head_size=self.head_size,
            head_size_v=self.head_size_v,
            sink_len=self.sink_len,
            dtype=self.kv_cache_torch_dtype,
            kv_quant_mode=get_kv_quant_mode(self.kv_cache_dtype),
        )
```