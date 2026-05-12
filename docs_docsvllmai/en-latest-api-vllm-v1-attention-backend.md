---
title: backend - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/attention/backend/
source: sitemap
fetched_at: 2026-05-07T21:39:03.340853936-03:00
rendered_js: false
word_count: 0
summary: This document defines the base abstract class for attention backends, providing a standardized interface for kernel implementations, memory layout configuration, and capability validation.
tags:
    - abstract-base-class
    - attention-backend
    - kv-cache
    - pytorch
    - model-inference
    - kernel-configuration
category: concept
---

```
classAttentionBackend(ABC):
"""Abstract class for attention backends."""

    supported_dtypes: ClassVar[list[torch.dtype]] = [torch.float16, torch.bfloat16]
    supported_kv_cache_dtypes: ClassVar[list["CacheDType"]] = [
        "auto",
        "float16",
        "bfloat16",
    ]

    # Does attention's forward() include kv cache update?
    forward_includes_kv_cache_update: bool = True

    @staticmethod
    defget_supported_kernel_block_sizes() -> list[int | MultipleOf]:
        return [MultipleOf(1)]

    @staticmethod
    @abstractmethod
    defget_name() -> str:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    defget_impl_cls() -> type["AttentionImplBase"]:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    defget_builder_cls():  # -> Type["AttentionMetadataBuilder"]:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    defget_kv_cache_shape(
        num_blocks: int,
        block_size: int,
        num_kv_heads: int,
        head_size: int,
        cache_dtype_str: str = "auto",
    ) -> tuple[int, ...]:
        raise NotImplementedError

    @classmethod
    defget_kv_cache_block_dim(
        cls,
        block_size: int,
        num_kv_heads: int,
        head_size: int,
        cache_dtype_str: str = "auto",
    ) -> int:
"""Discover which tensor dim is the block index, since different
        backends lay out dims differently."""
        _S = 1234567
        shape = cls.get_kv_cache_shape(
            _S,
            block_size,
            num_kv_heads,
            head_size,
            cache_dtype_str=cache_dtype_str,
        )
        return shape.index(_S)

    @staticmethod
    defget_kv_cache_stride_order(
        include_num_layers_dimension: bool = False,
    ) -> tuple[int, ...]:
"""
        Get the physical (memory layout) ordering of the kv cache dimensions.
        e.g. if the KV cache shape is
        [2, num_blocks, block_size, num_heads, head_size],
        and get_kv_cache_stride_order returns (1, 3, 0, 2, 4) then the physical
        ordering of dimensions is
        [num_blocks, num_heads, 2, block_size, head_size].

        If this function is unimplemented / raises NotImplementedError,
        the physical layout of the KV cache will match the logical shape.

        Args:
            include_num_layers_dimension: if True, includes an additional
                num_layers dimension, which is assumed to be prepended
                to the logical KV cache shape.
                With the above example, a return value (2, 4, 0, 1, 3, 5)
                corresponds to
                [num_blocks, num_heads, num_layers, 2, block_size, head_size].

                If an additional dimension is NOT included in the returned
                tuple, the physical layout will not include a layers dimension.

        Returns:
            A tuple of ints which is a permutation of range(len(shape)).
        """
        raise NotImplementedError

    @classmethod
    deffull_cls_name(cls) -> tuple[str, str]:
        return (cls.__module__, cls.__qualname__)

    @classmethod
    defget_supported_head_sizes(cls) -> list[int]:
        return []

    @classmethod
    defsupports_head_size(cls, head_size: int) -> bool:
        supported_head_sizes = cls.get_supported_head_sizes()
        return (not supported_head_sizes) or head_size in supported_head_sizes

    @classmethod
    defsupports_dtype(cls, dtype: torch.dtype) -> bool:
        return dtype in cls.supported_dtypes

    @classmethod
    defsupports_kv_cache_dtype(cls, kv_cache_dtype: "CacheDType | None") -> bool:
        if kv_cache_dtype is None:
            return True
        return (not cls.supported_kv_cache_dtypes) or (
            kv_cache_dtype in cls.supported_kv_cache_dtypes
        )

    @classmethod
    defsupports_block_size(cls, block_size: int | None) -> bool:
        if block_size is None:
            return True

        supported_kernel_block_sizes = cls.get_supported_kernel_block_sizes()
        if not supported_kernel_block_sizes:
            return True

        for supported_size in supported_kernel_block_sizes:
            if isinstance(supported_size, MultipleOf):
                supported_size = supported_size.base
            # With hybrid_blocks feature, the framework-level block size
            # only needs to be a multiple of the kernel's requirement,
            # even if the kernel requires a fixed block_size.
            if block_size % supported_size == 0:
                return True
        return False

    @classmethod
    defget_preferred_block_size(cls, default_block_size: int) -> int:
        supported_sizes = cls.get_supported_kernel_block_sizes()
        if not supported_sizes:
            return default_block_size

        if cls.supports_block_size(default_block_size):
            return default_block_size

        return min(s.base if isinstance(s, MultipleOf) else s for s in supported_sizes)

    @classmethod
    defis_mla(cls) -> bool:
        return False

    @classmethod
    defsupports_sink(cls) -> bool:
        return False

    @classmethod
    defsupports_alibi_sqrt(cls) -> bool:
        return False

    @classmethod
    defsupports_mm_prefix(cls) -> bool:
        return False

    @classmethod
    defis_sparse(cls) -> bool:
        return False

    @classmethod
    defsupports_per_head_quant_scales(cls) -> bool:
        return False

    @classmethod
    defsupports_non_causal(cls) -> bool:
"""Check if backend supports non-causal (bidirectional) attention
        for decoder models.

        Unlike ENCODER_ONLY attention type which implies a different
        execution model, this refers to non-causal attention within the
        standard paged-KV-cache decoder path.
        """
        return False

    @classmethod
    defsupports_batch_invariance(cls) -> bool:
        return False

    @classmethod
    defsupports_attn_type(cls, attn_type: str) -> bool:
"""Check if backend supports a given attention type.

        By default, only supports decoder attention.
        Backends should override this to support other attention types.
        """
        return attn_type == AttentionType.DECODER

    @classmethod
    defsupports_compute_capability(cls, capability: "DeviceCapability") -> bool:
        return True

    @classmethod
    defsupports_combination(
        cls,
        head_size: int,
        dtype: torch.dtype,
        kv_cache_dtype: "CacheDType | None",
        block_size: int | None,
        use_mla: bool,
        has_sink: bool,
        use_sparse: bool,
        device_capability: "DeviceCapability",
    ) -> str | None:
        return None

    @classmethod
    defvalidate_configuration(
        cls,
        head_size: int,
        dtype: torch.dtype,
        kv_cache_dtype: "CacheDType | None",
        block_size: int | None,
        use_mla: bool,
        has_sink: bool,
        use_sparse: bool,
        use_mm_prefix: bool,
        use_per_head_quant_scales: bool,
        device_capability: "DeviceCapability",
        attn_type: str,
        use_non_causal: bool = False,
        use_batch_invariant: bool = False,
    ) -> list[str]:
        invalid_reasons = []
        if not cls.supports_head_size(head_size):
            invalid_reasons.append("head_size not supported")
        if not cls.supports_dtype(dtype):
            invalid_reasons.append("dtype not supported")
        if not cls.supports_kv_cache_dtype(kv_cache_dtype):
            invalid_reasons.append("kv_cache_dtype not supported")
        if not cls.supports_block_size(block_size):
            invalid_reasons.append("block_size not supported")
        if use_mm_prefix and not cls.supports_mm_prefix():
            invalid_reasons.append(
                "partial multimodal token full attention not supported"
            )
        if use_mla != cls.is_mla():
            if use_mla:
                invalid_reasons.append("MLA not supported")
            else:
                invalid_reasons.append("non-MLA not supported")
        if has_sink and not cls.supports_sink():
            invalid_reasons.append("attention sinks not supported")
        if use_sparse != cls.is_sparse():
            if use_sparse:
                invalid_reasons.append("sparse not supported")
            else:
                invalid_reasons.append("non-sparse not supported")
        if use_per_head_quant_scales and not cls.supports_per_head_quant_scales():
            invalid_reasons.append("per-head quant scales not supported")
        if not cls.supports_compute_capability(device_capability):
            invalid_reasons.append("compute capability not supported")
        if not cls.supports_attn_type(attn_type):
            invalid_reasons.append(f"attention type {attn_type} not supported")
        if use_non_causal and not cls.supports_non_causal():
            invalid_reasons.append("non-causal attention not supported")
        if use_batch_invariant and not cls.supports_batch_invariance():
            invalid_reasons.append("batch invariance not supported")
        combination_reason = cls.supports_combination(
            head_size,
            dtype,
            kv_cache_dtype,
            block_size,
            use_mla,
            has_sink,
            use_sparse,
            device_capability,
        )
        if combination_reason is not None:
            invalid_reasons.append(combination_reason)
        return invalid_reasons

    @classmethod
    defget_required_kv_cache_layout(cls) -> "KVCacheLayoutType | None":
        return None

    @classmethod
    defis_ssm(cls) -> bool:
        return False
```