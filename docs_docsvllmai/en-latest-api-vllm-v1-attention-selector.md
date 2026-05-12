---
title: selector - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/attention/selector/
source: sitemap
fetched_at: 2026-05-07T21:40:13.30178853-03:00
rendered_js: false
word_count: 33
summary: These functions provide a mechanism to dynamically select and lazily import the appropriate attention backend based on specific model and configuration requirements.
tags:
    - vllm
    - attention-mechanism
    - backend-selection
    - lazy-loading
    - machine-learning-infrastructure
category: api
---

## get\_attn\_backend [¶](#vllm.v1.attention.selector.get_attn_backend "Permanent link")

```
get_attn_backend(
    head_size: int,
    dtype: dtype,
    kv_cache_dtype: str | None,
    use_mla: bool = False,
    has_sink: bool = False,
    use_sparse: bool = False,
    use_mm_prefix: bool = False,
    use_per_head_quant_scales: bool = False,
    attn_type: str | None = None,
    num_heads: int | None = None,
) -> type[AttentionBackend]
```

Selects which attention backend to use and lazily imports it.

Source code in `vllm/v1/attention/selector.py`

```
defget_attn_backend(
    head_size: int,
    dtype: torch.dtype,
    kv_cache_dtype: str | None,
    use_mla: bool = False,
    has_sink: bool = False,
    use_sparse: bool = False,
    use_mm_prefix: bool = False,
    use_per_head_quant_scales: bool = False,
    attn_type: str | None = None,
    num_heads: int | None = None,
) -> type[AttentionBackend]:
"""Selects which attention backend to use and lazily imports it."""

    if kv_cache_dtype is not None:
        valid_cache_dtypes = get_args(CacheDType)
        assert kv_cache_dtype in valid_cache_dtypes, (
            f"Invalid kv_cache_dtype: {kv_cache_dtype}. "
            f"Valid values are: {valid_cache_dtypes}"
        )

    fromvllm.configimport get_current_vllm_config

    vllm_config = get_current_vllm_config()

    cache_config = vllm_config.cache_config
    if cache_config is not None and cache_config.user_specified_block_size:
        block_size = cache_config.block_size
    else:
        block_size = None

    attn_selector_config = AttentionSelectorConfig(
        head_size=head_size,
        dtype=dtype,
        kv_cache_dtype=cast(CacheDType | None, kv_cache_dtype),
        block_size=block_size,
        use_mla=use_mla,
        has_sink=has_sink,
        use_sparse=use_sparse,
        use_mm_prefix=use_mm_prefix,
        use_per_head_quant_scales=use_per_head_quant_scales,
        attn_type=attn_type or AttentionType.DECODER,
        use_non_causal=vllm_config.attention_config.use_non_causal,
        use_batch_invariant=envs.VLLM_BATCH_INVARIANT,
    )

    return _cached_get_attn_backend(
        backend=vllm_config.attention_config.backend,
        attn_selector_config=attn_selector_config,
        num_heads=num_heads,
    )
```

## get\_mamba\_attn\_backend [¶](#vllm.v1.attention.selector.get_mamba_attn_backend "Permanent link")

Select which mamba attention backend to use and lazily import it.

Source code in `vllm/v1/attention/selector.py`

```
defget_mamba_attn_backend(
    mamba_type: str,
) -> type[AttentionBackend]:
"""Select which mamba attention backend to use and lazily import it."""
    return _cached_get_mamba_attn_backend(mamba_type)
```