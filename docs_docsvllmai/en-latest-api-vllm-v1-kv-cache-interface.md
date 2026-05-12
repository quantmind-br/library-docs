---
title: kv_cache_interface - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/kv_cache_interface/
source: sitemap
fetched_at: 2026-05-07T21:40:52.191507641-03:00
rendered_js: false
word_count: 808
summary: This document defines various dataclasses for attention specifications in the vLLM KV cache interface, providing methods to calculate memory usage and admission constraints for different attention mechanisms.
tags:
    - vllm
    - kv-cache
    - attention-spec
    - memory-management
    - dataclass
    - distributed-inference
category: reference
---

## ChunkedLocalAttentionSpec `dataclass` [¶](#vllm.v1.kv_cache_interface.ChunkedLocalAttentionSpec "Permanent link")

Bases: `AttentionSpec`

Source code in `vllm/v1/kv_cache_interface.py`

```
@dataclass(frozen=True, kw_only=True)
classChunkedLocalAttentionSpec(AttentionSpec):
    attention_chunk_size: int

    defmax_admission_blocks_per_request(
        self, max_num_batched_tokens: int, max_model_len: int
    ) -> int:
"""Per-request admission cap, in blocks.

        Single source of truth for both startup pool sizing
        (`max_memory_usage_bytes`) and the runtime admission gate, so requests
        admitted by startup can also be admitted at runtime.
        """
        # During chunked prefill, we hold KV for at most one chunk window.
        num_tokens = min(
            self.attention_chunk_size + max_num_batched_tokens, max_model_len
        )
        return cdiv(num_tokens, self.block_size)

    defmax_memory_usage_bytes(self, vllm_config: VllmConfig) -> int:
        max_model_len = vllm_config.model_config.max_model_len
        max_num_batched_tokens = vllm_config.scheduler_config.max_num_batched_tokens
        max_blocks = self.max_admission_blocks_per_request(
            max_num_batched_tokens=max_num_batched_tokens, max_model_len=max_model_len
        )
        return max_blocks * self.page_size_bytes
```

### max\_admission\_blocks\_per\_request [¶](#vllm.v1.kv_cache_interface.ChunkedLocalAttentionSpec.max_admission_blocks_per_request "Permanent link")

```
max_admission_blocks_per_request(
    max_num_batched_tokens: int, max_model_len: int
) -> int
```

Per-request admission cap, in blocks.

Single source of truth for both startup pool sizing (`max_memory_usage_bytes`) and the runtime admission gate, so requests admitted by startup can also be admitted at runtime.

Source code in `vllm/v1/kv_cache_interface.py`

```
defmax_admission_blocks_per_request(
    self, max_num_batched_tokens: int, max_model_len: int
) -> int:
"""Per-request admission cap, in blocks.

    Single source of truth for both startup pool sizing
    (`max_memory_usage_bytes`) and the runtime admission gate, so requests
    admitted by startup can also be admitted at runtime.
    """
    # During chunked prefill, we hold KV for at most one chunk window.
    num_tokens = min(
        self.attention_chunk_size + max_num_batched_tokens, max_model_len
    )
    return cdiv(num_tokens, self.block_size)
```

## CrossAttentionSpec `dataclass` [¶](#vllm.v1.kv_cache_interface.CrossAttentionSpec "Permanent link")

Bases: `AttentionSpec`

KV cache spec for cross-attention layers in encoder-decoder models.

Source code in `vllm/v1/kv_cache_interface.py`

```
@dataclass(frozen=True)
classCrossAttentionSpec(AttentionSpec):
"""
    KV cache spec for cross-attention layers in encoder-decoder models.
    """

    defmax_memory_usage_bytes(self, vllm_config: VllmConfig) -> int:
        # For cross-attention, we need to cache encoder states
        # Get encoder length (e.g., 1500 for Whisper).
        max_encoder_len = vllm_config.scheduler_config.max_num_encoder_input_tokens
        return cdiv(max_encoder_len, self.block_size) * self.page_size_bytes
```

## FullAttentionSpec `dataclass` [¶](#vllm.v1.kv_cache_interface.FullAttentionSpec "Permanent link")

Bases: `AttentionSpec`

When hybrid allocator is disabled and the model contains both full attention layers and sliding window attention layers, sliding window attention are regarded as full attention in KV cache manager (blocks are allocated for all tokens), while computed as sliding window attention in model runner. In this case, we use FullAttentionSpec and record the sliding window size.

Source code in `vllm/v1/kv_cache_interface.py`

```
@dataclass(frozen=True, kw_only=True)
classFullAttentionSpec(AttentionSpec):
"""
    When hybrid allocator is disabled and the model contains both full
    attention layers and sliding window attention layers, sliding
    window attention are regarded as full attention in KV cache manager
    (blocks are allocated for all tokens), while computed as sliding window
    attention in model runner.
    In this case, we use FullAttentionSpec and record the sliding window size.
    """

    head_size_v: int = None  # type: ignore[assignment]

    sliding_window: int | None = None
"""
    Default to None for not using sliding window attention.
    """
    attention_chunk_size: int | None = None

    def__post_init__(self):
        if self.head_size_v is None:
            object.__setattr__(self, "head_size_v", self.head_size)

    defmax_memory_usage_bytes(self, vllm_config: VllmConfig) -> int:
        max_model_len = vllm_config.model_config.max_model_len
        dcp_world_size = vllm_config.parallel_config.decode_context_parallel_size
        pcp_world_size = vllm_config.parallel_config.prefill_context_parallel_size
        # Note(hc): each dcp rank only need save
        # (max_model_len//dcp_world_size) tokens locally.
        if dcp_world_size * pcp_world_size > 1:
            max_model_len = cdiv(max_model_len, dcp_world_size * pcp_world_size)
        return cdiv(max_model_len, self.block_size) * self.page_size_bytes

    @classmethod
    defmerge_window_sizes(cls, window_sizes: set[int]) -> int | None:
        if len(window_sizes) == 0:
            return None
        elif len(window_sizes) == 1:
            return window_sizes.pop()
        else:
            raise ValueError(
                "All attention layers in the same KV cache group must have the "
                "same window size."
            )

    @classmethod
    defmerge(cls, specs: list[Self]) -> Self:
"""
        Merge a list of FullAttentionSpec objects into a single
        FullAttentionSpec object.
        """
        assert all(isinstance(spec, FullAttentionSpec) for spec in specs), (
            "All attention layers in the same KV cache group must be FullAttentionSpec."
        )

        sliding_window = set(
            spec.sliding_window for spec in specs if spec.sliding_window is not None
        )
        attention_chunk_size = set(
            spec.attention_chunk_size
            for spec in specs
            if spec.attention_chunk_size is not None
        )
        assert not any(isinstance(spec, MLAAttentionSpec) for spec in specs), (
            "MLAAttentionSpec should be merged in MLAAttentionSpec.merge"
        )
        merged_spec = cls(
            block_size=specs[0].block_size,
            num_kv_heads=specs[0].num_kv_heads,
            head_size=specs[0].head_size,
            head_size_v=specs[0].head_size_v,
            dtype=specs[0].dtype,
            kv_quant_mode=specs[0].kv_quant_mode,
            page_size_padded=specs[0].page_size_padded,
            sliding_window=cls.merge_window_sizes(sliding_window),
            attention_chunk_size=cls.merge_window_sizes(attention_chunk_size),
        )
        for spec in specs:
            for f in fields(AttentionSpec):
                assert getattr(spec, f.name) == getattr(merged_spec, f.name), (
                    "All attention layers in the same KV cache group must have "
                    "the same attention spec."
                )
        assert (merged_spec.sliding_window is not None) + (
            merged_spec.attention_chunk_size is not None
        ) <= 1, (
            "Model with both sliding window layers and chunked local attention "
            "layers is not supported."
        )
        return merged_spec

    @property
    defreal_page_size_bytes(self) -> int:
        if self.kv_quant_mode.is_nvfp4:
            # Packed layout per head: fp4 data + fp8 block scales.
            # fp4 data: head_size//2 bytes (2 fp4 values per byte)
            # fp8 block scale: head_size//16 bytes (1 scale per 16 elements)
            last_dim = nvfp4_kv_cache_full_dim(
                self.head_size
            ) + nvfp4_kv_cache_full_dim(self.head_size_v)
            return (
                self.block_size
                * self.num_kv_heads
                * last_dim
                * get_dtype_size(self.dtype)
            )
        return (
            self.block_size
            * self.num_kv_heads
            * (self.head_size + self.head_size_v)
            * get_dtype_size(self.dtype)
        )
```

### sliding\_window `class-attribute` `instance-attribute` [¶](#vllm.v1.kv_cache_interface.FullAttentionSpec.sliding_window "Permanent link")

```
sliding_window: int | None = None
```

Default to None for not using sliding window attention.

### merge `classmethod` [¶](#vllm.v1.kv_cache_interface.FullAttentionSpec.merge "Permanent link")

Merge a list of FullAttentionSpec objects into a single FullAttentionSpec object.

Source code in `vllm/v1/kv_cache_interface.py`

```
@classmethod
defmerge(cls, specs: list[Self]) -> Self:
"""
    Merge a list of FullAttentionSpec objects into a single
    FullAttentionSpec object.
    """
    assert all(isinstance(spec, FullAttentionSpec) for spec in specs), (
        "All attention layers in the same KV cache group must be FullAttentionSpec."
    )

    sliding_window = set(
        spec.sliding_window for spec in specs if spec.sliding_window is not None
    )
    attention_chunk_size = set(
        spec.attention_chunk_size
        for spec in specs
        if spec.attention_chunk_size is not None
    )
    assert not any(isinstance(spec, MLAAttentionSpec) for spec in specs), (
        "MLAAttentionSpec should be merged in MLAAttentionSpec.merge"
    )
    merged_spec = cls(
        block_size=specs[0].block_size,
        num_kv_heads=specs[0].num_kv_heads,
        head_size=specs[0].head_size,
        head_size_v=specs[0].head_size_v,
        dtype=specs[0].dtype,
        kv_quant_mode=specs[0].kv_quant_mode,
        page_size_padded=specs[0].page_size_padded,
        sliding_window=cls.merge_window_sizes(sliding_window),
        attention_chunk_size=cls.merge_window_sizes(attention_chunk_size),
    )
    for spec in specs:
        for f in fields(AttentionSpec):
            assert getattr(spec, f.name) == getattr(merged_spec, f.name), (
                "All attention layers in the same KV cache group must have "
                "the same attention spec."
            )
    assert (merged_spec.sliding_window is not None) + (
        merged_spec.attention_chunk_size is not None
    ) <= 1, (
        "Model with both sliding window layers and chunked local attention "
        "layers is not supported."
    )
    return merged_spec
```

## KVCacheConfig `dataclass` [¶](#vllm.v1.kv_cache_interface.KVCacheConfig "Permanent link")

The KV cache configuration of a model.

Source code in `vllm/v1/kv_cache_interface.py`

```
@dataclass
classKVCacheConfig:
"""
    The KV cache configuration of a model.
    """

    num_blocks: int
"""The number of KV cache blocks"""
    kv_cache_tensors: list[KVCacheTensor]
"""How should model runner initialize the KV cache tensors for each layer"""
    kv_cache_groups: list[KVCacheGroupSpec]
"""
    The kv cache groups of the model.
    For models with only one type of attention, there is only one group that
    contains all layers.
    For models with multiple types of attention, there will be multiple groups,
    see `_get_kv_cache_config_uniform_page_size` for more details.
    """

    @property
    defhas_mamba_layers(self) -> bool:
        return any(isinstance(g.kv_cache_spec, MambaSpec) for g in self.kv_cache_groups)

    @property
    defneeds_kv_cache_zeroing(self) -> bool:
        return self.has_mamba_layers
```

### kv\_cache\_groups `instance-attribute` [¶](#vllm.v1.kv_cache_interface.KVCacheConfig.kv_cache_groups "Permanent link")

The kv cache groups of the model. For models with only one type of attention, there is only one group that contains all layers. For models with multiple types of attention, there will be multiple groups, see `_get_kv_cache_config_uniform_page_size` for more details.

### kv\_cache\_tensors `instance-attribute` [¶](#vllm.v1.kv_cache_interface.KVCacheConfig.kv_cache_tensors "Permanent link")

How should model runner initialize the KV cache tensors for each layer

### num\_blocks `instance-attribute` [¶](#vllm.v1.kv_cache_interface.KVCacheConfig.num_blocks "Permanent link")

The number of KV cache blocks

## KVCacheGroupSpec `dataclass` [¶](#vllm.v1.kv_cache_interface.KVCacheGroupSpec "Permanent link")

Represents a group of model layers that share the same KV cache block table. These layers are regarded as one layer in the KV cache manager.

Source code in `vllm/v1/kv_cache_interface.py`

```
@dataclass
classKVCacheGroupSpec:
"""
    Represents a group of model layers that share the same KV cache block table.
    These layers are regarded as one layer in the KV cache manager.
    """

    # The names of model layers in this group
    layer_names: list[str]
    # The KV cache spec of this manager layer
    kv_cache_spec: KVCacheSpec
    # Whether this group contains EAGLE/MTP draft attention layers.
    is_eagle_group: bool = False
```

## KVCacheSpec `dataclass` [¶](#vllm.v1.kv_cache_interface.KVCacheSpec "Permanent link")

A base class for specifying the KV cache format of one layer.

Source code in `vllm/v1/kv_cache_interface.py`

```
@dataclass(frozen=True)
classKVCacheSpec:
"""
    A base class for specifying the KV cache format of one layer.
    """

    # number of tokens in a block
    block_size: int

    @property
    defpage_size_bytes(self) -> int:
"""
        The size of a page with `block_size` tokens in bytes.

        Returns:
            The page size
        """
        raise NotImplementedError

    @property
    defstorage_block_size(self) -> int:
        return self.block_size

    defmax_memory_usage_bytes(self, vllm_config: VllmConfig) -> int:
"""
        The maximum possible memory usage of this KV cache in bytes.

        Returns:
            The KV cache size in bytes
        """
        raise NotImplementedError

    defcopy_with_new_block_size(self, block_size: int) -> Self:
"""
        Create a new KVCacheSpec from self but replacing the block size.
        """
        return replace(self, block_size=block_size)

    @classmethod
    defmerge(cls, specs: list[Self]) -> Self:
"""
        Merge a list of KVCacheSpec objects into a single KVCacheSpec object.
        """
        assert all(spec == specs[0] for spec in specs[1:]), (
            "All layers in the same KV cache group must be the same."
        )
        return copy.deepcopy(specs[0])
```

### page\_size\_bytes `property` [¶](#vllm.v1.kv_cache_interface.KVCacheSpec.page_size_bytes "Permanent link")

The size of a page with `block_size` tokens in bytes.

Returns:

Type Description `int`

The page size

### copy\_with\_new\_block\_size [¶](#vllm.v1.kv_cache_interface.KVCacheSpec.copy_with_new_block_size "Permanent link")

```
copy_with_new_block_size(block_size: int) -> Self
```

Create a new KVCacheSpec from self but replacing the block size.

Source code in `vllm/v1/kv_cache_interface.py`

```
defcopy_with_new_block_size(self, block_size: int) -> Self:
"""
    Create a new KVCacheSpec from self but replacing the block size.
    """
    return replace(self, block_size=block_size)
```

### max\_memory\_usage\_bytes [¶](#vllm.v1.kv_cache_interface.KVCacheSpec.max_memory_usage_bytes "Permanent link")

The maximum possible memory usage of this KV cache in bytes.

Returns:

Type Description `int`

The KV cache size in bytes

Source code in `vllm/v1/kv_cache_interface.py`

```
defmax_memory_usage_bytes(self, vllm_config: VllmConfig) -> int:
"""
    The maximum possible memory usage of this KV cache in bytes.

    Returns:
        The KV cache size in bytes
    """
    raise NotImplementedError
```

### merge `classmethod` [¶](#vllm.v1.kv_cache_interface.KVCacheSpec.merge "Permanent link")

Merge a list of KVCacheSpec objects into a single KVCacheSpec object.

Source code in `vllm/v1/kv_cache_interface.py`

```
@classmethod
defmerge(cls, specs: list[Self]) -> Self:
"""
    Merge a list of KVCacheSpec objects into a single KVCacheSpec object.
    """
    assert all(spec == specs[0] for spec in specs[1:]), (
        "All layers in the same KV cache group must be the same."
    )
    return copy.deepcopy(specs[0])
```

## KVCacheTensor `dataclass` [¶](#vllm.v1.kv_cache_interface.KVCacheTensor "Permanent link")

A class for specifying how the workers should initialize the KV cache.

Source code in `vllm/v1/kv_cache_interface.py`

```
@dataclass
classKVCacheTensor:
"""
    A class for specifying how the workers should initialize the KV cache.
    """

    size: int  # size of the KV cache tensor in bytes
    shared_by: list[str]  # layer names that share the same KV cache tensor
```

## KVQuantMode [¶](#vllm.v1.kv_cache_interface.KVQuantMode "Permanent link")

Bases: `IntEnum`

KV cache quantization mode.

Used by attention backends and kernels to dispatch quantization logic without string matching on `kv_cache_dtype`.

Source code in `vllm/v1/kv_cache_interface.py`

```
classKVQuantMode(IntEnum):
"""KV cache quantization mode.

    Used by attention backends and kernels to dispatch quantization logic
    without string matching on ``kv_cache_dtype``.
    """

    NONE = 0
    FP8_PER_TENSOR = 1  # per-tensor scales (current fp8 path)
    INT8_PER_TOKEN_HEAD = 2  # per-token-head dynamic scales for int8
    FP8_PER_TOKEN_HEAD = 3  # per-token-head dynamic scales for fp8
    NVFP4 = 4  # packed fp4 data + fp8 block scales

    @property
    defis_per_token_head(self) -> bool:
"""True for any per-token-head quantization mode."""
        return self in (
            KVQuantMode.INT8_PER_TOKEN_HEAD,
            KVQuantMode.FP8_PER_TOKEN_HEAD,
        )

    @property
    defis_nvfp4(self) -> bool:
"""True for NVFP4 packed quantization mode."""
        return self == KVQuantMode.NVFP4
```

### is\_nvfp4 `property` [¶](#vllm.v1.kv_cache_interface.KVQuantMode.is_nvfp4 "Permanent link")

True for NVFP4 packed quantization mode.

### is\_per\_token\_head `property` [¶](#vllm.v1.kv_cache_interface.KVQuantMode.is_per_token_head "Permanent link")

True for any per-token-head quantization mode.

## SinkFullAttentionSpec `dataclass` [¶](#vllm.v1.kv_cache_interface.SinkFullAttentionSpec "Permanent link")

Bases: `FullAttentionSpec`

Source code in `vllm/v1/kv_cache_interface.py`

```
@dataclass(frozen=True)
classSinkFullAttentionSpec(FullAttentionSpec):
    sink_len: int | None = None

    @classmethod
    defmerge(cls, specs: list[Self]) -> Self:
"""
        Merge a list of FullAttentionSpec objects into a single
        FullAttentionSpec object.
        """
        assert all(isinstance(spec, FullAttentionSpec) for spec in specs), (
            "All attention layers in the same KV cache group must be FullAttentionSpec."
        )

        sliding_window = set(
            spec.sliding_window for spec in specs if spec.sliding_window is not None
        )
        attention_chunk_size = set(
            spec.attention_chunk_size
            for spec in specs
            if spec.attention_chunk_size is not None
        )
        assert not any(isinstance(spec, MLAAttentionSpec) for spec in specs), (
            "MLAAttentionSpec should be merged in MLAAttentionSpec.merge"
        )
        merged_spec = cls(
            block_size=specs[0].block_size,
            num_kv_heads=specs[0].num_kv_heads,
            head_size=specs[0].head_size,
            head_size_v=specs[0].head_size_v,
            sink_len=specs[0].sink_len,
            dtype=specs[0].dtype,
            kv_quant_mode=specs[0].kv_quant_mode,
            page_size_padded=specs[0].page_size_padded,
            sliding_window=cls.merge_window_sizes(sliding_window),
            attention_chunk_size=cls.merge_window_sizes(attention_chunk_size),
        )
        for spec in specs:
            for f in fields(AttentionSpec):
                assert getattr(spec, f.name) == getattr(merged_spec, f.name), (
                    "All attention layers in the same KV cache group must have "
                    "the same attention spec."
                )
        assert (merged_spec.sliding_window is not None) + (
            merged_spec.attention_chunk_size is not None
        ) <= 1, (
            "Model with both sliding window layers and chunked local attention "
            "layers is not supported."
        )
        return merged_spec
```

### merge `classmethod` [¶](#vllm.v1.kv_cache_interface.SinkFullAttentionSpec.merge "Permanent link")

Merge a list of FullAttentionSpec objects into a single FullAttentionSpec object.

Source code in `vllm/v1/kv_cache_interface.py`

```
@classmethod
defmerge(cls, specs: list[Self]) -> Self:
"""
    Merge a list of FullAttentionSpec objects into a single
    FullAttentionSpec object.
    """
    assert all(isinstance(spec, FullAttentionSpec) for spec in specs), (
        "All attention layers in the same KV cache group must be FullAttentionSpec."
    )

    sliding_window = set(
        spec.sliding_window for spec in specs if spec.sliding_window is not None
    )
    attention_chunk_size = set(
        spec.attention_chunk_size
        for spec in specs
        if spec.attention_chunk_size is not None
    )
    assert not any(isinstance(spec, MLAAttentionSpec) for spec in specs), (
        "MLAAttentionSpec should be merged in MLAAttentionSpec.merge"
    )
    merged_spec = cls(
        block_size=specs[0].block_size,
        num_kv_heads=specs[0].num_kv_heads,
        head_size=specs[0].head_size,
        head_size_v=specs[0].head_size_v,
        sink_len=specs[0].sink_len,
        dtype=specs[0].dtype,
        kv_quant_mode=specs[0].kv_quant_mode,
        page_size_padded=specs[0].page_size_padded,
        sliding_window=cls.merge_window_sizes(sliding_window),
        attention_chunk_size=cls.merge_window_sizes(attention_chunk_size),
    )
    for spec in specs:
        for f in fields(AttentionSpec):
            assert getattr(spec, f.name) == getattr(merged_spec, f.name), (
                "All attention layers in the same KV cache group must have "
                "the same attention spec."
            )
    assert (merged_spec.sliding_window is not None) + (
        merged_spec.attention_chunk_size is not None
    ) <= 1, (
        "Model with both sliding window layers and chunked local attention "
        "layers is not supported."
    )
    return merged_spec
```

## SlidingWindowMLASpec `dataclass` [¶](#vllm.v1.kv_cache_interface.SlidingWindowMLASpec "Permanent link")

Bases: `SlidingWindowSpec`

Sliding window attention with MLA cache format.

Source code in `vllm/v1/kv_cache_interface.py`

```
@dataclass(frozen=True, kw_only=True)
classSlidingWindowMLASpec(SlidingWindowSpec):
"""Sliding window attention with MLA cache format."""

    cache_dtype_str: str | None = None
    # DeepseekV4-only: see MLAAttentionSpec.model_version.
    alignment: int | None = None  # Default to None for no padding.
    compress_ratio: int = 1
    model_version: str | None = None

    def__post_init__(self):
        _apply_alignment_padding(self)

    @property
    defstorage_block_size(self) -> int:
        return self.block_size // self.compress_ratio

    @property
    defreal_page_size_bytes(self) -> int:
        if self.model_version == "deepseek_v4":
            # DeepseekV4: 448B NoPE + 128B RoPE + 8B fp8 scale = 584B per token.
            return self.storage_block_size * 584
        assert self.model_version is None, (
            f"Unsupported model version: {self.model_version}"
        )
        return (
            self.storage_block_size
            * self.num_kv_heads
            * self.head_size
            * get_dtype_size(self.dtype)
        )

    @classmethod
    defmerge(cls, specs: list[Self]) -> Self:
        assert all(isinstance(spec, SlidingWindowMLASpec) for spec in specs), (
            "All attention layers in the same KV cache group must be "
            "SlidingWindowMLASpec."
        )
        cache_dtype_str_set = set(spec.cache_dtype_str for spec in specs)
        compress_ratio_set = set(spec.compress_ratio for spec in specs)
        model_version_set = set(spec.model_version for spec in specs)
        sliding_window_set = set(spec.sliding_window for spec in specs)
        assert (
            len(cache_dtype_str_set) == 1
            and len(compress_ratio_set) == 1
            and len(model_version_set) == 1
            and len(sliding_window_set) == 1
        ), (
            "All attention layers in the same KV cache group must use the same "
            "quantization method, compress ratio, model version and sliding "
            "window size."
        )
        return cls(
            block_size=specs[0].block_size,
            num_kv_heads=specs[0].num_kv_heads,
            head_size=specs[0].head_size,
            dtype=specs[0].dtype,
            page_size_padded=specs[0].page_size_padded,
            sliding_window=sliding_window_set.pop(),
            cache_dtype_str=cache_dtype_str_set.pop(),
            compress_ratio=compress_ratio_set.pop(),
            model_version=model_version_set.pop(),
        )
```

## SlidingWindowSpec `dataclass` [¶](#vllm.v1.kv_cache_interface.SlidingWindowSpec "Permanent link")

Bases: `AttentionSpec`

Source code in `vllm/v1/kv_cache_interface.py`

```
@dataclass(frozen=True, kw_only=True)
classSlidingWindowSpec(AttentionSpec):
    sliding_window: int
    head_size_v: int = None  # type: ignore[assignment]

    def__post_init__(self):
        if self.head_size_v is None:
            object.__setattr__(self, "head_size_v", self.head_size)

    @property
    defreal_page_size_bytes(self) -> int:
        return (
            self.block_size
            * self.num_kv_heads
            * (self.head_size + self.head_size_v)
            * get_dtype_size(self.dtype)
        )

    defmax_admission_blocks_per_request(
        self, max_num_batched_tokens: int, max_model_len: int
    ) -> int:
"""Per-request admission cap, in blocks.

        Single source of truth for both startup pool sizing
        (`max_memory_usage_bytes`) and the runtime admission gate. Per-request
        real-held blocks plateau at this bound because
        `SlidingWindowManager.remove_skipped_blocks` runs from `allocate_slots`
        before each chunk's `get_num_blocks_to_allocate`.
        """
        # During chunked prefill, we hold KV for the last `sliding_window-1`
        # computed tokens plus the newly scheduled tokens, and never more
        # than `max_model_len`.
        num_tokens = min(
            self.sliding_window - 1 + max_num_batched_tokens, max_model_len
        )
        # +1 because the sliding window may not start from the beginning of
        # the block. E.g. block size 4 and num_token 4 needs two blocks
        # [XXCD][EF] to store the 6-token window [CDEF].
        return cdiv(num_tokens, self.block_size) + 1

    defmax_memory_usage_bytes(self, vllm_config: VllmConfig) -> int:
        assert vllm_config.parallel_config.decode_context_parallel_size == 1, (
            "DCP not support sliding window."
        )
        max_model_len = vllm_config.model_config.max_model_len
        max_num_batched_tokens = vllm_config.scheduler_config.max_num_batched_tokens
        max_blocks = self.max_admission_blocks_per_request(
            max_num_batched_tokens=max_num_batched_tokens, max_model_len=max_model_len
        )
        return max_blocks * self.page_size_bytes
```

### max\_admission\_blocks\_per\_request [¶](#vllm.v1.kv_cache_interface.SlidingWindowSpec.max_admission_blocks_per_request "Permanent link")

```
max_admission_blocks_per_request(
    max_num_batched_tokens: int, max_model_len: int
) -> int
```

Per-request admission cap, in blocks.

Single source of truth for both startup pool sizing (`max_memory_usage_bytes`) and the runtime admission gate. Per-request real-held blocks plateau at this bound because `SlidingWindowManager.remove_skipped_blocks` runs from `allocate_slots` before each chunk's `get_num_blocks_to_allocate`.

Source code in `vllm/v1/kv_cache_interface.py`

```
defmax_admission_blocks_per_request(
    self, max_num_batched_tokens: int, max_model_len: int
) -> int:
"""Per-request admission cap, in blocks.

    Single source of truth for both startup pool sizing
    (`max_memory_usage_bytes`) and the runtime admission gate. Per-request
    real-held blocks plateau at this bound because
    `SlidingWindowManager.remove_skipped_blocks` runs from `allocate_slots`
    before each chunk's `get_num_blocks_to_allocate`.
    """
    # During chunked prefill, we hold KV for the last `sliding_window-1`
    # computed tokens plus the newly scheduled tokens, and never more
    # than `max_model_len`.
    num_tokens = min(
        self.sliding_window - 1 + max_num_batched_tokens, max_model_len
    )
    # +1 because the sliding window may not start from the beginning of
    # the block. E.g. block size 4 and num_token 4 needs two blocks
    # [XXCD][EF] to store the 6-token window [CDEF].
    return cdiv(num_tokens, self.block_size) + 1
```

## TQFullAttentionSpec `dataclass` [¶](#vllm.v1.kv_cache_interface.TQFullAttentionSpec "Permanent link")

Bases: `FullAttentionSpec`

FullAttentionSpec with TQ-aware page size.

Python equivalent of the C++ TQ4FullAttentionSpec. Overrides real\_page\_size\_bytes to use TQ slot bytes instead of the raw head\_size * dtype formula.

Source code in `vllm/v1/kv_cache_interface.py`

```
@dataclass(frozen=True, kw_only=True)
classTQFullAttentionSpec(FullAttentionSpec):
"""FullAttentionSpec with TQ-aware page size.

    Python equivalent of the C++ TQ4FullAttentionSpec. Overrides
    real_page_size_bytes to use TQ slot bytes instead of the raw
    head_size * dtype formula.
    """

    tq_slot_size: int = 0

    @property
    defreal_page_size_bytes(self) -> int:
        if self.tq_slot_size > 0:
            return self.block_size * self.num_kv_heads * self.tq_slot_size
        return super().real_page_size_bytes

    @classmethod
    defmerge(cls, specs: list[Self]) -> Self:
        merged = super().merge(specs)
        assert all(s.tq_slot_size == specs[0].tq_slot_size for s in specs), (
            "All TQ layers in the same KV cache group must use the same tq_slot_size."
        )
        return replace(merged, tq_slot_size=specs[0].tq_slot_size)
```

## UniformTypeKVCacheSpecs `dataclass` [¶](#vllm.v1.kv_cache_interface.UniformTypeKVCacheSpecs "Permanent link")

Bases: `KVCacheSpec`

A KV cache spec for multiple layers with the same type of attention. Here, same types means always need the same number of token slots. For example, sliding window attentions with different window sizes are not the same type and should not be merged into one UniformTypeKVCacheSpecs.

Source code in `vllm/v1/kv_cache_interface.py`

```
@dataclass(frozen=True)
classUniformTypeKVCacheSpecs(KVCacheSpec):
"""
    A KV cache spec for multiple layers with the same type of attention. Here,
    same types means always need the same number of token slots. For example,
    sliding window attentions with different window sizes are not the same type
    and should not be merged into one UniformTypeKVCacheSpecs.
    """

    kv_cache_specs: dict[str, KVCacheSpec]

    @property
    defpage_size_bytes(self) -> int:
        return sum(spec.page_size_bytes for spec in self.kv_cache_specs.values())

    defmax_memory_usage_bytes(self, vllm_config: VllmConfig) -> int:
        max_num_pages = max(
            cdiv(spec.max_memory_usage_bytes(vllm_config), spec.page_size_bytes)
            for spec in self.kv_cache_specs.values()
        )
        return max_num_pages * self.page_size_bytes

    @classmethod
    defis_uniform_type(cls, kv_cache_specs: dict[str, KVCacheSpec]) -> bool:
"""
        Whether all layers have the same type of KV cache spec.
        """
        block_sizes = set(spec.block_size for spec in kv_cache_specs.values())
        if len(block_sizes) > 1:
            # Different block sizes, not uniform.
            return False
        one_spec = next(iter(kv_cache_specs.values()))
        # NOTE: Check subclasses before parent classes since isinstance()
        # returns True for subclasses.
        if isinstance(one_spec, SlidingWindowMLASpec):
            # SlidingWindowMLASpec is uniform if all specs are SlidingWindowMLASpec
            # with the same sliding_window size.
            return all(
                isinstance(spec, SlidingWindowMLASpec)
                and spec.sliding_window == one_spec.sliding_window
                for spec in kv_cache_specs.values()
            )
        elif isinstance(one_spec, FullAttentionSpec):
            return all(
                isinstance(spec, FullAttentionSpec) for spec in kv_cache_specs.values()
            )
        elif isinstance(one_spec, CrossAttentionSpec):
            return all(
                isinstance(spec, CrossAttentionSpec) for spec in kv_cache_specs.values()
            )
        elif isinstance(one_spec, SlidingWindowSpec):
            return all(
                isinstance(spec, SlidingWindowSpec)
                and spec.sliding_window == one_spec.sliding_window
                for spec in kv_cache_specs.values()
            )
        elif isinstance(one_spec, ChunkedLocalAttentionSpec):
            return all(
                isinstance(spec, ChunkedLocalAttentionSpec)
                and spec.attention_chunk_size == one_spec.attention_chunk_size
                for spec in kv_cache_specs.values()
            )
        elif isinstance(one_spec, MambaSpec):
            return all(
                isinstance(spec, MambaSpec)
                and spec.num_speculative_blocks == one_spec.num_speculative_blocks
                for spec in kv_cache_specs.values()
            )
        else:
            # NOTE(Chen): Please add new branches for new KV cache spec types.
            raise NotImplementedError(
                f"Unsupported KV cache spec type: {type(one_spec)}"
            )

    @classmethod
    deffrom_specs(cls, kv_cache_specs: dict[str, KVCacheSpec]) -> Self | None:
"""
        Return a SameTypeKVCacheSpecs object if all layers have the same type
        of KV cache spec. Return None if not.
        """
        if cls.is_uniform_type(kv_cache_specs):
            block_size = next(iter(kv_cache_specs.values())).block_size
            return cls(block_size=block_size, kv_cache_specs=kv_cache_specs)
        else:
            return None

    # NOTE: below util functions are only used by DeepseekV4 for now.
    defget_page_sizes(self) -> list[int]:
        return list(set(spec.page_size_bytes for spec in self.kv_cache_specs.values()))

    defget_num_layer_tuples(self) -> int:
        return Counter(
            spec.page_size_bytes for spec in self.kv_cache_specs.values()
        ).most_common(1)[0][1]

    defmax_memory_usage_pages(self, vllm_config: VllmConfig) -> int:
        return max(
            cdiv(spec.max_memory_usage_bytes(vllm_config), spec.page_size_bytes)
            for spec in self.kv_cache_specs.values()
        )
```

### from\_specs `classmethod` [¶](#vllm.v1.kv_cache_interface.UniformTypeKVCacheSpecs.from_specs "Permanent link")

Return a SameTypeKVCacheSpecs object if all layers have the same type of KV cache spec. Return None if not.

Source code in `vllm/v1/kv_cache_interface.py`

```
@classmethod
deffrom_specs(cls, kv_cache_specs: dict[str, KVCacheSpec]) -> Self | None:
"""
    Return a SameTypeKVCacheSpecs object if all layers have the same type
    of KV cache spec. Return None if not.
    """
    if cls.is_uniform_type(kv_cache_specs):
        block_size = next(iter(kv_cache_specs.values())).block_size
        return cls(block_size=block_size, kv_cache_specs=kv_cache_specs)
    else:
        return None
```

### is\_uniform\_type `classmethod` [¶](#vllm.v1.kv_cache_interface.UniformTypeKVCacheSpecs.is_uniform_type "Permanent link")

Whether all layers have the same type of KV cache spec.

Source code in `vllm/v1/kv_cache_interface.py`

```
@classmethod
defis_uniform_type(cls, kv_cache_specs: dict[str, KVCacheSpec]) -> bool:
"""
    Whether all layers have the same type of KV cache spec.
    """
    block_sizes = set(spec.block_size for spec in kv_cache_specs.values())
    if len(block_sizes) > 1:
        # Different block sizes, not uniform.
        return False
    one_spec = next(iter(kv_cache_specs.values()))
    # NOTE: Check subclasses before parent classes since isinstance()
    # returns True for subclasses.
    if isinstance(one_spec, SlidingWindowMLASpec):
        # SlidingWindowMLASpec is uniform if all specs are SlidingWindowMLASpec
        # with the same sliding_window size.
        return all(
            isinstance(spec, SlidingWindowMLASpec)
            and spec.sliding_window == one_spec.sliding_window
            for spec in kv_cache_specs.values()
        )
    elif isinstance(one_spec, FullAttentionSpec):
        return all(
            isinstance(spec, FullAttentionSpec) for spec in kv_cache_specs.values()
        )
    elif isinstance(one_spec, CrossAttentionSpec):
        return all(
            isinstance(spec, CrossAttentionSpec) for spec in kv_cache_specs.values()
        )
    elif isinstance(one_spec, SlidingWindowSpec):
        return all(
            isinstance(spec, SlidingWindowSpec)
            and spec.sliding_window == one_spec.sliding_window
            for spec in kv_cache_specs.values()
        )
    elif isinstance(one_spec, ChunkedLocalAttentionSpec):
        return all(
            isinstance(spec, ChunkedLocalAttentionSpec)
            and spec.attention_chunk_size == one_spec.attention_chunk_size
            for spec in kv_cache_specs.values()
        )
    elif isinstance(one_spec, MambaSpec):
        return all(
            isinstance(spec, MambaSpec)
            and spec.num_speculative_blocks == one_spec.num_speculative_blocks
            for spec in kv_cache_specs.values()
        )
    else:
        # NOTE(Chen): Please add new branches for new KV cache spec types.
        raise NotImplementedError(
            f"Unsupported KV cache spec type: {type(one_spec)}"
        )
```

## get\_kv\_quant\_mode [¶](#vllm.v1.kv_cache_interface.get_kv_quant_mode "Permanent link")

```
get_kv_quant_mode(kv_cache_dtype: str) -> KVQuantMode
```

Map a `kv_cache_dtype` string to a :class:`KVQuantMode`.

Source code in `vllm/v1/kv_cache_interface.py`

```
defget_kv_quant_mode(kv_cache_dtype: str) -> KVQuantMode:
"""Map a ``kv_cache_dtype`` string to a :class:`KVQuantMode`."""
    if kv_cache_dtype == "int8_per_token_head":
        return KVQuantMode.INT8_PER_TOKEN_HEAD
    if kv_cache_dtype == "fp8_per_token_head":
        return KVQuantMode.FP8_PER_TOKEN_HEAD
    if kv_cache_dtype == "nvfp4":
        return KVQuantMode.NVFP4
    if isinstance(kv_cache_dtype, str) and kv_cache_dtype.startswith("fp8"):
        return KVQuantMode.FP8_PER_TENSOR
    return KVQuantMode.NONE
```

## kv\_cache\_uses\_per\_token\_head\_scales [¶](#vllm.v1.kv_cache_interface.kv_cache_uses_per_token_head_scales "Permanent link")

```
kv_cache_uses_per_token_head_scales(
    kv_cache_dtype: str,
) -> bool
```

Return True if *kv\_cache\_dtype* needs per-token-head scales.

Source code in `vllm/v1/kv_cache_interface.py`

```
defkv_cache_uses_per_token_head_scales(kv_cache_dtype: str) -> bool:
"""Return True if *kv_cache_dtype* needs per-token-head scales."""
    return get_kv_quant_mode(kv_cache_dtype).is_per_token_head
```