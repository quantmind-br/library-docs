---
title: deep_gemm - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/utils/deep_gemm/
source: sitemap
fetched_at: 2026-05-07T21:38:35.35931015-03:00
rendered_js: false
word_count: 873
summary: This module provides a compatibility layer for integrating DeepGEMM within vLLM, handling dynamic imports of external or vendored libraries and managing quantization scale formats through an oracle cache system.
tags:
    - deep-gemm
    - vllm
    - quantization
    - compatibility
    - python-wrappers
    - jit-compilation
category: api
---

Compatibility wrapper for DeepGEMM API changes.

Users of vLLM should always import **only** these wrappers.

## DeepGemmQuantScaleFMT [¶](#vllm.utils.deep_gemm.DeepGemmQuantScaleFMT "Permanent link")

Bases: `Enum`

Source code in `vllm/utils/deep_gemm.py`

```
classDeepGemmQuantScaleFMT(Enum):
    # Float32 scales in Float32 tensor
    FLOAT32 = 0
    # Compute float32 scales and ceil the scales to UE8M0.
    # Keep the scales in Float32 tensor.
    FLOAT32_CEIL_UE8M0 = 1
    # Compute float32 scales and ceil the scales to UE8M0.
    # Pack the scales into a int32 tensor where each int32
    # element contains 4 scale values.
    UE8M0 = 2

    @classmethod
    definit_oracle_cache(cls) -> None:
"""Initialize the oracle decision and store it in the class cache"""
        cached = getattr(cls, "_oracle_cache", None)
        if cached is not None:
            return

        use_e8m0 = (
            envs.VLLM_USE_DEEP_GEMM_E8M0
            and is_deep_gemm_supported()
            and (_fp8_gemm_nt_impl is not None)
        )
        if not use_e8m0:
            cls._oracle_cache = cls.FLOAT32  # type: ignore
            return

        cls._oracle_cache = (  # type: ignore
            cls.UE8M0
            if current_platform.is_device_capability_family(100)
            else cls.FLOAT32_CEIL_UE8M0
        )

    @classmethod
    deffrom_oracle(cls) -> "DeepGemmQuantScaleFMT":
"""Return the pre-initialized oracle decision"""
        cached = getattr(cls, "_oracle_cache", None)
        assert cached is not None, "DeepGemmQuantScaleFMT oracle cache not initialized"
        return cached
```

### from\_oracle `classmethod` [¶](#vllm.utils.deep_gemm.DeepGemmQuantScaleFMT.from_oracle "Permanent link")

```
from_oracle() -> DeepGemmQuantScaleFMT
```

Return the pre-initialized oracle decision

Source code in `vllm/utils/deep_gemm.py`

```
@classmethod
deffrom_oracle(cls) -> "DeepGemmQuantScaleFMT":
"""Return the pre-initialized oracle decision"""
    cached = getattr(cls, "_oracle_cache", None)
    assert cached is not None, "DeepGemmQuantScaleFMT oracle cache not initialized"
    return cached
```

### init\_oracle\_cache `classmethod` [¶](#vllm.utils.deep_gemm.DeepGemmQuantScaleFMT.init_oracle_cache "Permanent link")

```
init_oracle_cache() -> None
```

Initialize the oracle decision and store it in the class cache

Source code in `vllm/utils/deep_gemm.py`

```
@classmethod
definit_oracle_cache(cls) -> None:
"""Initialize the oracle decision and store it in the class cache"""
    cached = getattr(cls, "_oracle_cache", None)
    if cached is not None:
        return

    use_e8m0 = (
        envs.VLLM_USE_DEEP_GEMM_E8M0
        and is_deep_gemm_supported()
        and (_fp8_gemm_nt_impl is not None)
    )
    if not use_e8m0:
        cls._oracle_cache = cls.FLOAT32  # type: ignore
        return

    cls._oracle_cache = (  # type: ignore
        cls.UE8M0
        if current_platform.is_device_capability_family(100)
        else cls.FLOAT32_CEIL_UE8M0
    )
```

## \_import\_deep\_gemm [¶](#vllm.utils.deep_gemm._import_deep_gemm "Permanent link")

Import the deep\_gemm module.

Prefers an externally installed `deep_gemm` package (so users can pin a specific version), then falls back to the vendored copy bundled in the vLLM wheel.

Returns `None` when neither source is usable.

Source code in `vllm/utils/deep_gemm.py`

```
def_import_deep_gemm():
"""Import the deep_gemm module.

    Prefers an externally installed ``deep_gemm`` package (so users can
    pin a specific version), then falls back to the vendored copy bundled
    in the vLLM wheel.

    Returns ``None`` when neither source is usable.
    """
    # 1. Try the external (pip-installed) package first.
    try:
        module = importlib.import_module("deep_gemm")
        logger.debug_once("Imported deep_gemm module from site-packages")
        return module
    except ImportError:
        logger.debug_once(
            "deep_gemm not found in site-packages, "
            "trying vendored vllm.third_party.deep_gemm"
        )

    # 2. Fall back to the vendored copy bundled in the vLLM wheel.
    try:
        module = importlib.import_module("vllm.third_party.deep_gemm")
        logger.debug_once("Imported deep_gemm module from vllm.third_party.deep_gemm")
        return module
    except ImportError:
        logger.debug_once("Vendored deep_gemm not found either")
    except Exception as e:
        # The vendored module may raise RuntimeError during _C.init()
        # if JIT include files are missing (e.g. incomplete wheel).
        logger.warning_once("Failed to import vendored deep_gemm: %s", e)

    return None
```

## \_lazy\_init [¶](#vllm.utils.deep_gemm._lazy_init "Permanent link")

Import deep\_gemm and resolve symbols on first use.

Source code in `vllm/utils/deep_gemm.py`

```
def_lazy_init() -> None:
"""Import deep_gemm and resolve symbols on first use."""
    global _cublaslt_gemm_nt_impl
    global _fp8_gemm_nt_impl, _fp8_einsum_impl
    global _grouped_impl, _grouped_masked_impl, _grouped_fp4_impl
    global _fp8_fp4_mqa_logits_impl, _fp8_fp4_paged_mqa_logits_impl
    global _get_paged_mqa_logits_metadata_impl
    global _tf32_hc_prenorm_gemm_impl
    global _get_mn_major_tma_aligned_tensor_impl
    global _get_mk_alignment_for_contiguous_layout_impl
    global _transform_sf_into_required_layout_impl
    # fast path
    if (
        _cublaslt_gemm_nt_impl is not None
        or _fp8_gemm_nt_impl is not None
        or _fp8_einsum_impl is not None
        or _grouped_impl is not None
        or _grouped_masked_impl is not None
        or _grouped_fp4_impl is not None
        or _fp8_fp4_mqa_logits_impl is not None
        or _fp8_fp4_paged_mqa_logits_impl is not None
        or _get_paged_mqa_logits_metadata_impl is not None
        or _tf32_hc_prenorm_gemm_impl is not None
        or _get_mk_alignment_for_contiguous_layout_impl is not None
        or _transform_sf_into_required_layout_impl is not None
    ):
        return

    if not has_deep_gemm():
        return

    # Set up deep_gemm cache path
    DEEP_GEMM_JIT_CACHE_ENV_NAME = "DG_JIT_CACHE_DIR"
    if not os.environ.get(DEEP_GEMM_JIT_CACHE_ENV_NAME, None):
        os.environ[DEEP_GEMM_JIT_CACHE_ENV_NAME] = os.path.join(
            envs.VLLM_CACHE_ROOT, "deep_gemm"
        )

    _dg = _import_deep_gemm()
    if _dg is None:
        return

    _cublaslt_gemm_nt_impl = getattr(_dg, "cublaslt_gemm_nt", None)
    _fp8_gemm_nt_impl = getattr(_dg, "fp8_gemm_nt", None)
    _fp8_einsum_impl = getattr(_dg, "fp8_einsum", None)
    _grouped_impl = getattr(_dg, "m_grouped_fp8_gemm_nt_contiguous", None)
    _grouped_masked_impl = getattr(_dg, "fp8_m_grouped_gemm_nt_masked", None)
    _grouped_fp4_impl = getattr(_dg, "m_grouped_fp8_fp4_gemm_nt_contiguous", None)
    # DeepGEMM exposes fp8_fp4_*_mqa_logits as the canonical symbols that
    # handle both the FP8 and FP4 Q/K paths via a tuple-typed `q`.
    _fp8_fp4_mqa_logits_impl = getattr(_dg, "fp8_fp4_mqa_logits", None)
    _fp8_fp4_paged_mqa_logits_impl = getattr(_dg, "fp8_fp4_paged_mqa_logits", None)
    _get_paged_mqa_logits_metadata_impl = getattr(
        _dg, "get_paged_mqa_logits_metadata", None
    )
    _tf32_hc_prenorm_gemm_impl = getattr(_dg, "tf32_hc_prenorm_gemm", None)
    _get_mn_major_tma_aligned_tensor_impl = getattr(
        _dg, "get_mn_major_tma_aligned_tensor", None
    )
    _get_mk_alignment_for_contiguous_layout_impl = getattr(
        _dg, "get_mk_alignment_for_contiguous_layout", None
    )
    _transform_sf_into_required_layout_impl = getattr(
        _dg, "transform_sf_into_required_layout", None
    )
    DeepGemmQuantScaleFMT.init_oracle_cache()
```

## \_missing [¶](#vllm.utils.deep_gemm._missing "Permanent link")

Placeholder for unavailable DeepGEMM backend.

Source code in `vllm/utils/deep_gemm.py`

```
def_missing(*_: Any, **__: Any) -> NoReturn:
"""Placeholder for unavailable DeepGEMM backend."""
    raise RuntimeError(
        "DeepGEMM backend is not available or outdated. Please install or "
        "update the `deep_gemm` to a newer version to enable FP8 kernels."
    )
```

## calc\_diff [¶](#vllm.utils.deep_gemm.calc_diff "Permanent link")

Return a global difference metric for unit tests.

DeepGEMM kernels on Blackwell/B200 currently exhibit noticeable per-element error, causing `torch.testing.assert_close` to fail. Instead of checking every element, we compute a cosine-style similarity over the whole tensor and report `1 - sim`. Once kernel accuracy improves this helper can be removed.

Source code in `vllm/utils/deep_gemm.py`

```
defcalc_diff(x: torch.Tensor, y: torch.Tensor):
"""Return a global difference metric for unit tests.

    DeepGEMM kernels on Blackwell/B200 currently exhibit noticeable per-element
    error, causing `torch.testing.assert_close` to fail.  Instead of checking
    every element, we compute a cosine-style similarity over the whole tensor
    and report `1 - sim`.  Once kernel accuracy improves this helper can be
    removed.
    """

    x, y = x.double(), y.double()
    denominator = (x * x + y * y).sum()
    sim = 2 * (x * y).sum() / denominator
    return 1 - sim
```

## fp8\_fp4\_mqa\_logits [¶](#vllm.utils.deep_gemm.fp8_fp4_mqa_logits "Permanent link")

Compute MQA logits for a single sequence without KV paging.

Unified FP8/FP4 dispatch — the underlying DeepGEMM kernel takes `q = (values, scales_or_None)` where `scales` is None for FP8 Q (per-token scale is folded into `weights`) and a packed block-scale tensor for MXFP4 Q.

Parameters:

Name Type Description Default `q` `tuple[Tensor, Tensor | None]`

Tuple `(q_values, q_scale)`. FP8 path: q\_values is \[M, H, D] float8\_e4m3fn and q\_scale is None (per-token scale is folded into `weights`). FP4 path: q\_values is packed uint8 and q\_scale is the companion block-scale tensor.

*required* `kv` `tuple[Tensor, Tensor]`

Tuple `(k_packed, k_scales)` — FP8 layout is \[N, D] float8\_e4m3fn plus fp32 scales \[N]; FP4 layout is packed uint8.

*required* `weights` `Tensor`

weights of shape \[M, H], dtype `torch.float32`.

*required* `cu_seqlen_ks` `Tensor`

Start indices (inclusive) for valid K per query position, shape \[M], dtype int32.

*required* `cu_seqlen_ke` `Tensor`

End indices (exclusive) for valid K per query position, shape \[M], dtype int32.

*required* `clean_logits` `bool`

Whether to clean the unfilled logits into `-inf`.

*required*

Returns:

Type Description `Tensor`

Logits tensor of shape \[M, N], dtype `torch.float32`.

Source code in `vllm/utils/deep_gemm.py`

```
deffp8_fp4_mqa_logits(
    q: tuple[torch.Tensor, torch.Tensor | None],
    kv: tuple[torch.Tensor, torch.Tensor],
    weights: torch.Tensor,
    cu_seqlen_ks: torch.Tensor,
    cu_seqlen_ke: torch.Tensor,
    clean_logits: bool,
) -> torch.Tensor:
"""Compute MQA logits for a single sequence without KV paging.

    Unified FP8/FP4 dispatch — the underlying DeepGEMM kernel takes
    ``q = (values, scales_or_None)`` where ``scales`` is None for FP8 Q
    (per-token scale is folded into ``weights``) and a packed block-scale
    tensor for MXFP4 Q.

    Args:
        q: Tuple ``(q_values, q_scale)``. FP8 path: q_values is [M, H, D]
            float8_e4m3fn and q_scale is None (per-token scale is folded
            into ``weights``). FP4 path: q_values is packed uint8 and
            q_scale is the companion block-scale tensor.
        kv: Tuple `(k_packed, k_scales)` — FP8 layout is [N, D]
            float8_e4m3fn plus fp32 scales [N]; FP4 layout is packed uint8.
        weights: weights of shape [M, H], dtype `torch.float32`.
        cu_seqlen_ks: Start indices (inclusive) for valid K per query
            position, shape [M], dtype int32.
        cu_seqlen_ke: End indices (exclusive) for valid K per query
            position, shape [M], dtype int32.
        clean_logits: Whether to clean the unfilled logits into `-inf`.

    Returns:
        Logits tensor of shape [M, N], dtype `torch.float32`.
    """
    _lazy_init()
    if _fp8_fp4_mqa_logits_impl is None:
        return _missing()
    return _fp8_fp4_mqa_logits_impl(
        q,
        kv,
        weights,
        cu_seqlen_ks,
        cu_seqlen_ke,
        clean_logits=clean_logits,
    )
```

## fp8\_fp4\_paged\_mqa\_logits [¶](#vllm.utils.deep_gemm.fp8_fp4_paged_mqa_logits "Permanent link")

Compute MQA logits using a paged KV-cache.

Unified FP8/FP4 dispatch — the underlying DeepGEMM kernel takes `q = (values, scales_or_None)`; pass `(q_tensor, None)` for the FP8 path and `(q_values, q_scale)` for MXFP4.

Parameters:

Name Type Description Default `q` `tuple[Tensor, Tensor | None]`

Tuple `(q_values, q_scale)`. FP8 path: q\_values is \[B, next\_n, H, D] float8\_e4m3fn and q\_scale is None. FP4 path: q\_values is packed uint8 and q\_scale is the companion block-scale tensor.

*required* `kv_cache` `Tensor`

Paged KV-cache. FP8 layout is \[num\_blocks, block\_size, 1, D+4], dtype `torch.uint8`, with the last 4 bytes per (block, pos) storing the float dequant scale.

*required* `weights` `Tensor`

Tensor of shape \[B * next\_n, H], dtype `torch.float32`.

*required* `context_lens` `Tensor`

Tensor of shape \[B], dtype int32; effective context length for each batch element.

*required* `block_tables` `Tensor`

Tensor of shape \[B, max\_blocks], dtype int32; maps logical block indices to physical blocks in the paged cache.

*required* `schedule_metadata` `Tensor`

Returned by `get_paged_mqa_logits_metadata`; used to distribute work across SMs.

*required* `max_model_len` `int`

Maximum sequence length used to size the logits output.

*required* `clean_logits` `bool`

Whether to clean the unfilled logits into `-inf`.

*required*

Returns:

Type Description `Tensor`

Logits tensor of shape \[B * next\_n, max\_model\_len], dtype

`Tensor`

`torch.float32`.

Source code in `vllm/utils/deep_gemm.py`

```
deffp8_fp4_paged_mqa_logits(
    q: tuple[torch.Tensor, torch.Tensor | None],
    kv_cache: torch.Tensor,
    weights: torch.Tensor,
    context_lens: torch.Tensor,
    block_tables: torch.Tensor,
    schedule_metadata: torch.Tensor,
    max_model_len: int,
    clean_logits: bool,
) -> torch.Tensor:
"""Compute MQA logits using a paged KV-cache.

    Unified FP8/FP4 dispatch — the underlying DeepGEMM kernel takes
    ``q = (values, scales_or_None)``; pass ``(q_tensor, None)`` for the FP8
    path and ``(q_values, q_scale)`` for MXFP4.

    Args:
        q: Tuple ``(q_values, q_scale)``. FP8 path: q_values is
            [B, next_n, H, D] float8_e4m3fn and q_scale is None. FP4 path:
            q_values is packed uint8 and q_scale is the companion
            block-scale tensor.
        kv_cache: Paged KV-cache. FP8 layout is [num_blocks, block_size, 1,
            D+4], dtype `torch.uint8`, with the last 4 bytes per (block, pos)
            storing the float dequant scale.
        weights: Tensor of shape [B * next_n, H], dtype `torch.float32`.
        context_lens: Tensor of shape [B], dtype int32; effective context length
            for each batch element.
        block_tables: Tensor of shape [B, max_blocks], dtype int32; maps logical
            block indices to physical blocks in the paged cache.
        schedule_metadata: Returned by `get_paged_mqa_logits_metadata`;
            used to distribute work across SMs.
        max_model_len: Maximum sequence length used to size the logits output.
        clean_logits: Whether to clean the unfilled logits into `-inf`.

    Returns:
        Logits tensor of shape [B * next_n, max_model_len], dtype
        `torch.float32`.
    """
    _lazy_init()
    if _fp8_fp4_paged_mqa_logits_impl is None:
        return _missing()
    return _fp8_fp4_paged_mqa_logits_impl(
        q,
        kv_cache,
        weights,
        context_lens,
        block_tables,
        schedule_metadata,
        max_model_len,
        clean_logits=clean_logits,
    )
```

## get\_col\_major\_tma\_aligned\_tensor [¶](#vllm.utils.deep_gemm.get_col_major_tma_aligned_tensor "Permanent link")

Wrapper for DeepGEMM's get\_mn\_major\_tma\_aligned\_tensor

Source code in `vllm/utils/deep_gemm.py`

```
defget_col_major_tma_aligned_tensor(x: torch.Tensor) -> torch.Tensor:
"""Wrapper for DeepGEMM's get_mn_major_tma_aligned_tensor"""
    _lazy_init()
    if _get_mn_major_tma_aligned_tensor_impl is None:
        return _missing()
    return _get_mn_major_tma_aligned_tensor_impl(x)
```

## get\_paged\_mqa\_logits\_metadata [¶](#vllm.utils.deep_gemm.get_paged_mqa_logits_metadata "Permanent link")

```
get_paged_mqa_logits_metadata(
    context_lens: Tensor, block_size: int, num_sms: int
) -> Tensor
```

Build scheduling metadata for paged MQA logits.

Parameters:

Name Type Description Default `context_lens` `Tensor`

Tensor of shape \[B], dtype int32; effective context length per batch element.

*required* `block_size` `int`

KV-cache block size in tokens (e.g., 64).

*required* `num_sms` `int`

Number of SMs available. 132 for Hopper

*required*

Returns:

Type Description `Tensor`

Backend-specific tensor consumed by `fp8_fp4_paged_mqa_logits` to

`Tensor`

schedule work across SMs.

Source code in `vllm/utils/deep_gemm.py`

```
defget_paged_mqa_logits_metadata(
    context_lens: torch.Tensor, block_size: int, num_sms: int
) -> torch.Tensor:
"""Build scheduling metadata for paged MQA logits.

    Args:
        context_lens: Tensor of shape [B], dtype int32; effective context length
            per batch element.
        block_size: KV-cache block size in tokens (e.g., 64).
        num_sms: Number of SMs available. 132 for Hopper

    Returns:
        Backend-specific tensor consumed by `fp8_fp4_paged_mqa_logits` to
        schedule work across SMs.
    """
    _lazy_init()
    if _get_paged_mqa_logits_metadata_impl is None:
        return _missing()
    return _get_paged_mqa_logits_metadata_impl(context_lens, block_size, num_sms)
```

## is\_deep\_gemm\_e8m0\_used `cached` [¶](#vllm.utils.deep_gemm.is_deep_gemm_e8m0_used "Permanent link")

```
is_deep_gemm_e8m0_used() -> bool
```

Return `True` if vLLM is configured to use DeepGEMM " "E8M0 scale on a Hopper or Blackwell-class GPU.

Source code in `vllm/utils/deep_gemm.py`

```
@functools.cache
defis_deep_gemm_e8m0_used() -> bool:
"""Return `True` if vLLM is configured to use DeepGEMM "
    "E8M0 scale on a Hopper or Blackwell-class GPU.
    """
    if not is_deep_gemm_supported():
        logger.debug_once(
            "DeepGEMM E8M0 disabled: DeepGEMM not supported on this system."
        )
        return False

    _lazy_init()

    if _fp8_gemm_nt_impl is None:
        logger.info_once("DeepGEMM E8M0 disabled: _fp8_gemm_nt_impl not found")
        return False

    if envs.VLLM_USE_DEEP_GEMM_E8M0:
        logger.info_once("DeepGEMM E8M0 enabled on current platform.")
        return True

    logger.info_once("DeepGEMM E8M0 disabled on current configuration.")
    return False
```

## is\_deep\_gemm\_supported `cached` [¶](#vllm.utils.deep_gemm.is_deep_gemm_supported "Permanent link")

```
is_deep_gemm_supported() -> bool
```

Return `True` if DeepGEMM is supported on the current platform. Currently, only Hopper and Blackwell GPUs are supported.

Source code in `vllm/utils/deep_gemm.py`

```
@functools.cache
defis_deep_gemm_supported() -> bool:
"""Return `True` if DeepGEMM is supported on the current platform.
    Currently, only Hopper and Blackwell GPUs are supported.
    """
    is_supported_arch = current_platform.support_deep_gemm()
    return envs.VLLM_USE_DEEP_GEMM and has_deep_gemm() and is_supported_arch
```

## should\_auto\_disable\_deep\_gemm [¶](#vllm.utils.deep_gemm.should_auto_disable_deep_gemm "Permanent link")

```
should_auto_disable_deep_gemm(
    model_type: str | None,
) -> bool
```

Check if DeepGemm should be auto-disabled for this model on Blackwell.

Returns True if the model is known to have accuracy degradation with DeepGemm's E8M0 scale format on Blackwell GPUs (SM100+).

Source code in `vllm/utils/deep_gemm.py`

```
defshould_auto_disable_deep_gemm(model_type: str | None) -> bool:
"""Check if DeepGemm should be auto-disabled for this model on Blackwell.

    Returns True if the model is known to have accuracy degradation with
    DeepGemm's E8M0 scale format on Blackwell GPUs (SM100+).
    """
    if model_type is None:
        return False
    if not current_platform.is_device_capability_family(100):
        return False
    return model_type in _DEEPGEMM_BLACKWELL_EXCLUDED_MODEL_TYPES
```

## tf32\_hc\_prenorm\_gemm [¶](#vllm.utils.deep_gemm.tf32_hc_prenorm_gemm "Permanent link")

Perform the following computation

out = x.float() @ fn.T sqrsum = x.float().square().sum(-1)

See the caller function for shape requirement

Source code in `vllm/utils/deep_gemm.py`

```
deftf32_hc_prenorm_gemm(
    x: torch.Tensor,
    fn: torch.Tensor,
    out: torch.Tensor,
    sqrsum: torch.Tensor,
    num_split: int,
) -> torch.Tensor:
"""
    Perform the following computation:
        out = x.float() @ fn.T
        sqrsum = x.float().square().sum(-1)

    See the caller function for shape requirement
    """
    _lazy_init()
    if _tf32_hc_prenorm_gemm_impl is None:
        return _missing()
    return _tf32_hc_prenorm_gemm_impl(
        x,
        fn,
        out,
        sqrsum,
        num_split,
    )
```