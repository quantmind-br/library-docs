---
title: flashinfer - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/utils/flashinfer/
source: sitemap
fetched_at: 2026-05-07T21:38:36.426859341-03:00
rendered_js: false
word_count: 808
summary: This document provides a utility wrapper layer for the FlashInfer API within vLLM, offering safe lazy-loading, dependency checks, and specialized kernel helpers for attention operations and quantization.
tags:
    - vllm
    - flashinfer
    - api-wrapper
    - kernel-optimization
    - lazy-loading
    - mxfp8
    - tensor-operations
category: api
---

Compatibility wrapper for FlashInfer API changes.

Users of vLLM should always import **only** these wrappers.

## \_flashinfer\_concat\_mla\_k [¶](#vllm.utils.flashinfer._flashinfer_concat_mla_k "Permanent link")

Custom op wrapper for flashinfer's concat\_mla\_k.

This is an in-place operation that concatenates k\_nope and k\_pe into k.

The kernel is optimized for DeepSeek V3 dimensions: - num\_heads=128 - nope\_dim=128 - rope\_dim=64

Key optimizations: - Warp-based processing with software pipelining - Vectorized memory access (int2 for nope, int for rope) - L2 prefetching for next row while processing current - Register reuse for rope values across all heads

Parameters:

Name Type Description Default `k` `Tensor`

Output tensor, shape \[num\_tokens, num\_heads, nope\_dim + rope\_dim]. Modified in-place.

*required* `k_nope` `Tensor`

The nope part of k, shape \[num\_tokens, num\_heads, nope\_dim].

*required* `k_pe` `Tensor`

The rope part of k (shared), shape \[num\_tokens, 1, rope\_dim]. This is broadcast to all heads.

*required*

Source code in `vllm/utils/flashinfer.py`

```
def_flashinfer_concat_mla_k(
    k: torch.Tensor,
    k_nope: torch.Tensor,
    k_pe: torch.Tensor,
) -> None:
"""Custom op wrapper for flashinfer's concat_mla_k.

    This is an in-place operation that concatenates k_nope and k_pe into k.

    The kernel is optimized for DeepSeek V3 dimensions:
    - num_heads=128
    - nope_dim=128
    - rope_dim=64

    Key optimizations:
    - Warp-based processing with software pipelining
    - Vectorized memory access (int2 for nope, int for rope)
    - L2 prefetching for next row while processing current
    - Register reuse for rope values across all heads

    Args:
        k: Output tensor, shape [num_tokens, num_heads, nope_dim + rope_dim].
            Modified in-place.
        k_nope: The nope part of k, shape [num_tokens, num_heads, nope_dim].
        k_pe: The rope part of k (shared), shape [num_tokens, 1, rope_dim].
              This is broadcast to all heads.
    """
    fromflashinfer.concat_opsimport concat_mla_k

    concat_mla_k(k, k_nope, k_pe)
```

## \_get\_submodule [¶](#vllm.utils.flashinfer._get_submodule "Permanent link")

```
_get_submodule(module_name: str) -> Any | None
```

Safely import a submodule and return it, or None if not available.

Source code in `vllm/utils/flashinfer.py`

```
def_get_submodule(module_name: str) -> Any | None:
"""Safely import a submodule and return it, or None if not available."""
    try:
        return importlib.import_module(module_name)
    except (ImportError, ModuleNotFoundError):
        return None
```

## \_lazy\_import\_wrapper [¶](#vllm.utils.flashinfer._lazy_import_wrapper "Permanent link")

```
_lazy_import_wrapper(
    module_name: str,
    attr_name: str,
    fallback_fn: Callable[..., Any] = _missing,
)
```

Create a lazy import wrapper for a specific function.

Source code in `vllm/utils/flashinfer.py`

```
def_lazy_import_wrapper(
    module_name: str, attr_name: str, fallback_fn: Callable[..., Any] = _missing
):
"""Create a lazy import wrapper for a specific function."""

    @functools.cache
    def_get_impl():
        if not has_flashinfer():
            return None
        mod = _get_submodule(module_name)
        return getattr(mod, attr_name, None) if mod else None

    defwrapper(*args, **kwargs):
        impl = _get_impl()
        if impl is None:
            return fallback_fn(*args, **kwargs)
        return impl(*args, **kwargs)

    return wrapper
```

## \_missing [¶](#vllm.utils.flashinfer._missing "Permanent link")

Placeholder for unavailable FlashInfer backend.

Source code in `vllm/utils/flashinfer.py`

```
def_missing(*_: Any, **__: Any) -> NoReturn:
"""Placeholder for unavailable FlashInfer backend."""
    raise RuntimeError(
        "FlashInfer backend is not available. Please install the package "
        "to enable FlashInfer kernels: "
        "https://github.com/flashinfer-ai/flashinfer"
    )
```

## can\_use\_trtllm\_attention [¶](#vllm.utils.flashinfer.can_use_trtllm_attention "Permanent link")

```
can_use_trtllm_attention(
    num_qo_heads: int, num_kv_heads: int
) -> bool
```

Check if the current configuration supports TRTLLM attention.

Source code in `vllm/utils/flashinfer.py`

```
defcan_use_trtllm_attention(num_qo_heads: int, num_kv_heads: int) -> bool:
"""Check if the current configuration supports TRTLLM attention."""
    if force_use_trtllm_attention() is False:
        return False
    has_trtllm = supports_trtllm_attention()
    return has_trtllm and (num_qo_heads % num_kv_heads == 0)
```

## flashinfer\_mm\_mxfp8 [¶](#vllm.utils.flashinfer.flashinfer_mm_mxfp8 "Permanent link")

MXFP8 MM helper - mirrors flashinfer\_scaled\_fp4\_mm API.

Takes non-transposed weights and handles transpose internally.

CRITICAL: mm\_mxfp8 CUTLASS kernel requires SWIZZLED 1D scales for optimal performance and accuracy. Both input and weight scales should be in swizzled format from FlashInfer's mxfp8\_quantize(is\_sf\_swizzled\_layout=True).

Source code in `vllm/utils/flashinfer.py`

```
defflashinfer_mm_mxfp8(
    a: torch.Tensor,
    b: torch.Tensor,
    block_scale_a: torch.Tensor,
    block_scale_b: torch.Tensor,
    out_dtype: torch.dtype,
    backend: str = "cutlass",
) -> torch.Tensor:
"""MXFP8 MM helper - mirrors flashinfer_scaled_fp4_mm API.

    Takes non-transposed weights and handles transpose internally.

    CRITICAL: mm_mxfp8 CUTLASS kernel requires SWIZZLED 1D scales for optimal
    performance and accuracy. Both input and weight scales should be in
    swizzled format from FlashInfer's mxfp8_quantize(is_sf_swizzled_layout=True).
    """
    # a shape [M, K]
    # b shape [K, N]
    assert a.ndim == 2 and b.ndim == 2
    assert a.shape[1] == b.shape[1]  # K dimension must match

    if block_scale_b.ndim != 1:
        raise ValueError(
            "mm_mxfp8 expects 1D swizzled weight scales for CUTLASS; "
            f"got shape={tuple(block_scale_b.shape)}"
        )

    # Output tensor [M, N]
    return mm_mxfp8(
        a,
        b.t(),  # Transpose weight: [N, K] -> [K, N]
        block_scale_a,
        block_scale_b,
        out_dtype,
        backend=backend,
    )
```

## force\_use\_trtllm\_attention [¶](#vllm.utils.flashinfer.force_use_trtllm_attention "Permanent link")

```
force_use_trtllm_attention() -> bool | None
```

This function should only be called during initialization stage when vllm config is set. Return `None` if --attention-config.use\_trtllm\_attention is not set, return `True` if TRTLLM attention is forced to be used, return `False` if TRTLLM attention is forced to be not used.

Source code in `vllm/utils/flashinfer.py`

```
defforce_use_trtllm_attention() -> bool | None:
"""
    This function should only be called during initialization stage when vllm config
    is set.
    Return `None` if --attention-config.use_trtllm_attention is not set,
    return `True` if TRTLLM attention is forced to be used,
    return `False` if TRTLLM attention is forced to be not used.
    """
    fromvllm.configimport get_current_vllm_config

    vllm_config = get_current_vllm_config()
    return vllm_config.attention_config.use_trtllm_attention
```

## has\_flashinfer `cached` [¶](#vllm.utils.flashinfer.has_flashinfer "Permanent link")

Return `True` if flashinfer-python package is available.

Source code in `vllm/utils/flashinfer.py`

```
@functools.cache
defhas_flashinfer() -> bool:
"""Return `True` if flashinfer-python package is available."""
    # Use find_spec to check if the module exists without importing it
    # This avoids potential CUDA initialization side effects
    if importlib.util.find_spec("flashinfer") is None:
        logger.debug_once("FlashInfer unavailable since package was not found")
        return False
    # When not using flashinfer cubin,
    # Also check if nvcc is available since it's required to JIT compile flashinfer
    if not has_flashinfer_cubin() and shutil.which("nvcc") is None:
        logger.debug_once(
            "FlashInfer unavailable since nvcc was not found "
            "and not using pre-downloaded cubins"
        )
        return False
    return True
```

## has\_flashinfer\_comm `cached` [¶](#vllm.utils.flashinfer.has_flashinfer_comm "Permanent link")

```
has_flashinfer_comm() -> bool
```

Return `True` if FlashInfer comm module is available.

Source code in `vllm/utils/flashinfer.py`

```
@functools.cache
defhas_flashinfer_comm() -> bool:
"""Return `True` if FlashInfer comm module is available."""
    return has_flashinfer() and importlib.util.find_spec("flashinfer.comm") is not None
```

## has\_flashinfer\_cubin `cached` [¶](#vllm.utils.flashinfer.has_flashinfer_cubin "Permanent link")

```
has_flashinfer_cubin() -> bool
```

Return `True` if flashinfer-cubin package is available.

Source code in `vllm/utils/flashinfer.py`

```
@functools.cache
defhas_flashinfer_cubin() -> bool:
"""Return `True` if flashinfer-cubin package is available."""
    if envs.VLLM_HAS_FLASHINFER_CUBIN:
        return True
    if importlib.util.find_spec("flashinfer_cubin") is not None:
        return True
    logger.debug_once("flashinfer-cubin package was not found")
    return False
```

## has\_flashinfer\_cutedsl `cached` [¶](#vllm.utils.flashinfer.has_flashinfer_cutedsl "Permanent link")

```
has_flashinfer_cutedsl() -> bool
```

Return `True` if FlashInfer cutedsl module is available.

Source code in `vllm/utils/flashinfer.py`

```
@functools.cache
defhas_flashinfer_cutedsl() -> bool:
"""Return ``True`` if FlashInfer cutedsl module is available."""
    return (
        has_flashinfer() and importlib.util.find_spec("flashinfer.cute_dsl") is not None
    )
```

## has\_flashinfer\_cutedsl\_grouped\_gemm\_nt\_masked `cached` [¶](#vllm.utils.flashinfer.has_flashinfer_cutedsl_grouped_gemm_nt_masked "Permanent link")

```
has_flashinfer_cutedsl_grouped_gemm_nt_masked() -> bool
```

Return `True` if FlashInfer CUTLASS fused MoE is available.

Source code in `vllm/utils/flashinfer.py`

```
@functools.cache
defhas_flashinfer_cutedsl_grouped_gemm_nt_masked() -> bool:
"""Return ``True`` if FlashInfer CUTLASS fused MoE is available."""
    if not has_flashinfer_cutedsl():
        return False

    # Check if all required functions are available
    required_functions = [
        ("flashinfer.cute_dsl.blockscaled_gemm", "grouped_gemm_nt_masked"),
        ("flashinfer", "scaled_fp4_grouped_quantize"),
        ("flashinfer", "silu_and_mul_scaled_nvfp4_experts_quantize"),
    ]

    for module_name, attr_name in required_functions:
        mod = _get_submodule(module_name)
        if not mod or not hasattr(mod, attr_name):
            return False
    return True
```

## has\_flashinfer\_cutedsl\_moe\_nvfp4 `cached` [¶](#vllm.utils.flashinfer.has_flashinfer_cutedsl_moe_nvfp4 "Permanent link")

```
has_flashinfer_cutedsl_moe_nvfp4() -> bool
```

Return `True` if FlashInfer cute\_dsl\_fused\_moe\_nvfp4 is available.

Source code in `vllm/utils/flashinfer.py`

```
@functools.cache
defhas_flashinfer_cutedsl_moe_nvfp4() -> bool:
"""Return ``True`` if FlashInfer cute_dsl_fused_moe_nvfp4 is available."""
    if not has_flashinfer_cutedsl():
        return False
    mod = _get_submodule("flashinfer")
    return mod is not None and hasattr(mod, "cute_dsl_fused_moe_nvfp4")
```

## has\_flashinfer\_cutlass\_fused\_moe `cached` [¶](#vllm.utils.flashinfer.has_flashinfer_cutlass_fused_moe "Permanent link")

```
has_flashinfer_cutlass_fused_moe() -> bool
```

Return `True` if FlashInfer CUTLASS fused MoE is available.

Source code in `vllm/utils/flashinfer.py`

```
@functools.cache
defhas_flashinfer_cutlass_fused_moe() -> bool:
"""Return `True` if FlashInfer CUTLASS fused MoE is available."""
    if not has_flashinfer_moe():
        return False

    # Check if all required functions are available
    required_functions = [
        ("flashinfer.fused_moe", "cutlass_fused_moe"),
        ("flashinfer", "fp4_quantize"),
        ("flashinfer", "nvfp4_block_scale_interleave"),
        ("flashinfer.fused_moe", "trtllm_fp4_block_scale_moe"),
    ]

    for module_name, attr_name in required_functions:
        mod = _get_submodule(module_name)
        if not mod or not hasattr(mod, attr_name):
            return False
    return True
```

## has\_flashinfer\_fp8\_blockscale\_gemm `cached` [¶](#vllm.utils.flashinfer.has_flashinfer_fp8_blockscale_gemm "Permanent link")

```
has_flashinfer_fp8_blockscale_gemm() -> bool
```

Return `True` if FlashInfer block-scale FP8 GEMM is available.

Source code in `vllm/utils/flashinfer.py`

```
@functools.cache
defhas_flashinfer_fp8_blockscale_gemm() -> bool:
"""Return `True` if FlashInfer block-scale FP8 GEMM is available."""
    return (
        has_flashinfer()
        and current_platform.is_device_capability(90)
        and hasattr(_get_submodule("flashinfer.gemm"), "fp8_blockscale_gemm_sm90")
    )
```

## has\_flashinfer\_moe `cached` [¶](#vllm.utils.flashinfer.has_flashinfer_moe "Permanent link")

```
has_flashinfer_moe() -> bool
```

Return `True` if FlashInfer MoE module is available.

Source code in `vllm/utils/flashinfer.py`

```
@functools.cache
defhas_flashinfer_moe() -> bool:
"""Return `True` if FlashInfer MoE module is available."""
    return (
        has_flashinfer()
        and importlib.util.find_spec("flashinfer.fused_moe") is not None
    )
```

## has\_flashinfer\_nvlink\_one\_sided `cached` [¶](#vllm.utils.flashinfer.has_flashinfer_nvlink_one_sided "Permanent link")

```
has_flashinfer_nvlink_one_sided() -> bool
```

Return `True` if FlashInfer trtllm\_moe\_alltoall module is available.

Source code in `vllm/utils/flashinfer.py`

```
@functools.cache
defhas_flashinfer_nvlink_one_sided() -> bool:
"""Return `True` if FlashInfer trtllm_moe_alltoall module is available."""
    if not has_flashinfer_comm():
        return False
    return importlib.util.find_spec("flashinfer.comm.trtllm_moe_alltoall") is not None
```

## has\_flashinfer\_nvlink\_two\_sided `cached` [¶](#vllm.utils.flashinfer.has_flashinfer_nvlink_two_sided "Permanent link")

```
has_flashinfer_nvlink_two_sided() -> bool
```

Return `True` if FlashInfer mnnvl all2all is available.

Source code in `vllm/utils/flashinfer.py`

```
@functools.cache
defhas_flashinfer_nvlink_two_sided() -> bool:
"""Return `True` if FlashInfer mnnvl all2all is available."""
    if not has_flashinfer_comm():
        return False

    # Check if all required functions are available
    required_functions = [
        ("flashinfer.comm", "Mapping"),
        ("flashinfer.comm.mnnvl", "MnnvlMemory"),
        ("flashinfer.comm.trtllm_alltoall", "MnnvlMoe"),
        ("flashinfer.comm.trtllm_alltoall", "MoEAlltoallInfo"),
    ]

    for module_name, attr_name in required_functions:
        mod = _get_submodule(module_name)
        if not mod or not hasattr(mod, attr_name):
            return False
    return True
```

## has\_flashinfer\_trtllm\_fused\_moe `cached` [¶](#vllm.utils.flashinfer.has_flashinfer_trtllm_fused_moe "Permanent link")

```
has_flashinfer_trtllm_fused_moe() -> bool
```

Return `True` if FlashInfer TRTLLM fused MoE is available.

Source code in `vllm/utils/flashinfer.py`

```
@functools.cache
defhas_flashinfer_trtllm_fused_moe() -> bool:
"""Return `True` if FlashInfer TRTLLM fused MoE is available."""
    if not has_flashinfer_moe():
        return False
    required_functions = [
        ("flashinfer.fused_moe", "trtllm_fp8_block_scale_moe"),
        ("flashinfer.fused_moe", "trtllm_fp8_per_tensor_scale_moe"),
        ("flashinfer.fused_moe", "trtllm_fp4_block_scale_moe"),
        ("flashinfer.fused_moe", "trtllm_mxint4_block_scale_moe"),
        ("flashinfer.fused_moe", "trtllm_bf16_moe"),
    ]
    for module_name, attr_name in required_functions:
        mod = _get_submodule(module_name)
        if not mod or not hasattr(mod, attr_name):
            return False
    return True
```

## has\_nvidia\_artifactory `cached` [¶](#vllm.utils.flashinfer.has_nvidia_artifactory "Permanent link")

```
has_nvidia_artifactory() -> bool
```

Return `True` if NVIDIA's artifactory is accessible.

This checks connectivity to the kernel inference library artifactory which is required for downloading certain cubin kernels like TRTLLM FHMA.

Source code in `vllm/utils/flashinfer.py`

```
@functools.cache
defhas_nvidia_artifactory() -> bool:
"""Return `True` if NVIDIA's artifactory is accessible.

    This checks connectivity to the kernel inference library artifactory
    which is required for downloading certain cubin kernels like TRTLLM FHMA.
    """
    # If we have pre-downloaded cubins, we can assume the cubins are available.
    if has_flashinfer_cubin():
        return True

    try:
        # Use a short timeout to avoid blocking for too long
        response = requests.get(FLASHINFER_CUBINS_REPOSITORY, timeout=5)
        accessible = response.status_code == 200
        if accessible:
            logger.debug_once("NVIDIA artifactory is accessible")
        else:
            logger.warning_once(
                "NVIDIA artifactory returned failed status code: %d",
                response.status_code,
            )
        return accessible
    except Exception as e:
        logger.warning_once("Failed to connect to NVIDIA artifactory: %s", e)
        return False
```

## is\_flashinfer\_cudnn\_fp8\_prefill\_attn\_supported `cached` [¶](#vllm.utils.flashinfer.is_flashinfer_cudnn_fp8_prefill_attn_supported "Permanent link")

```
is_flashinfer_cudnn_fp8_prefill_attn_supported() -> bool
```

Check if FP8 ViT attention is supported on this platform.

Requires native FP8 hardware support, the FlashInfer cuDNN backend, and cuDNN &gt;= 9.17.1.

Source code in `vllm/utils/flashinfer.py`

```
@functools.cache
defis_flashinfer_cudnn_fp8_prefill_attn_supported() -> bool:
"""Check if FP8 ViT attention is supported on this platform.

    Requires native FP8 hardware support, the FlashInfer cuDNN backend,
    and cuDNN >= 9.17.1.
    """
    fromvllm.v1.attention.backends.registryimport AttentionBackendEnum

    # cuDNN SDPA FP8 requires Hopper (SM 90) or newer.
    if not current_platform.has_device_capability(90):
        return False

    try:
        supported = current_platform.get_supported_vit_attn_backends()
        if AttentionBackendEnum.FLASHINFER not in supported:
            return False
    except (ImportError, AttributeError):
        return False

    try:
        importtorch.backends.cudnnascudnn

        if cudnn.is_available() and cudnn.version() < _MIN_CUDNN_FP8:
            return False
    except (ImportError, AttributeError):
        pass

    return True
```

## is\_flashinfer\_fp8\_blockscale\_gemm\_supported `cached` [¶](#vllm.utils.flashinfer.is_flashinfer_fp8_blockscale_gemm_supported "Permanent link")

```
is_flashinfer_fp8_blockscale_gemm_supported() -> bool
```

Return `True` if FlashInfer block-scale FP8 GEMM is supported.

Source code in `vllm/utils/flashinfer.py`

```
@functools.cache
defis_flashinfer_fp8_blockscale_gemm_supported() -> bool:
"""Return `True` if FlashInfer block-scale FP8 GEMM is supported."""
    return (
        envs.VLLM_BLOCKSCALE_FP8_GEMM_FLASHINFER
        and has_flashinfer_fp8_blockscale_gemm()
    )
```

## supports\_trtllm\_attention `cached` [¶](#vllm.utils.flashinfer.supports_trtllm_attention "Permanent link")

```
supports_trtllm_attention() -> bool
```

TRTLLM attention is supported if the platform is SM100, NVIDIA artifactory is accessible, and batch-invariant mode is not enabled.

Source code in `vllm/utils/flashinfer.py`

```
@functools.cache
defsupports_trtllm_attention() -> bool:
"""
    TRTLLM attention is supported if the platform is SM100,
    NVIDIA artifactory is accessible, and batch-invariant mode is not enabled.
    """
    # Batch-invariant mode disables TRTLLM attention
    if envs.VLLM_BATCH_INVARIANT:
        return False

    # Requires SM100 and NVIDIA artifactory to be accessible to download cubins
    return (
        current_platform.is_device_capability_family(100) and has_nvidia_artifactory()
    )
```

## use\_trtllm\_attention [¶](#vllm.utils.flashinfer.use_trtllm_attention "Permanent link")

```
use_trtllm_attention(
    num_qo_heads: int,
    num_kv_heads: int,
    num_tokens: int,
    max_seq_len: int,
    dcp_world_size: int,
    kv_cache_dtype: str,
    q_dtype: dtype,
    is_prefill: bool,
    force_use_trtllm: bool | None = None,
    has_sinks: bool = False,
    has_spec: bool = False,
) -> bool
```

Return `True` if TRTLLM attention is used.

Source code in `vllm/utils/flashinfer.py`

```
defuse_trtllm_attention(
    num_qo_heads: int,
    num_kv_heads: int,
    num_tokens: int,
    max_seq_len: int,
    dcp_world_size: int,
    kv_cache_dtype: str,
    q_dtype: torch.dtype,
    is_prefill: bool,
    # None means auto-detection, True means force on, False means force off
    force_use_trtllm: bool | None = None,
    has_sinks: bool = False,
    has_spec: bool = False,
) -> bool:
"""Return `True` if TRTLLM attention is used."""

    # CLI argument is set to 0 - respect it
    if force_use_trtllm is not None and not force_use_trtllm:
        return False

    # Decode context parallel is not supported
    if dcp_world_size > 1:
        logger.warning_once(
            "Trtllm does not support returning LSE and as a result "
            "does not support DCP, reverting to FlashInfer"
        )
        return False

    # The platform is not supported
    if not supports_trtllm_attention():
        if force_use_trtllm:
            logger.warning_once(
                "TRTLLM attention is not supported on this platform, "
                "but --attention-config.use_trtllm_attention is set to 1"
            )
        return False

    # The combination of query and key heads is not supported
    if num_qo_heads % num_kv_heads != 0:
        if force_use_trtllm:
            logger.warning_once(
                "TRTLLM attention is not supported for this combination of "
                "query and key heads, but --attention-config.use_trtllm_attention is "
                "set to 1"
            )
        return False

    if has_spec and not is_prefill:
        # Speculative decoding requires TRTLLM attention for decodes
        logger.info_once("Using TRTLLM attention (enabled for speculative decoding).")
        return True

    # Must use TRTLLM attention if query is FP8 quantized
    if q_dtype == current_platform.fp8_dtype():
        logger.info_once("Using TRTLLM attention (query is quantized).")
        return True

    # If sinks are being used, we must use TRTLLM attention as it's
    # the only backend that supports them
    if has_sinks:
        logger.info_once("Using TRTLLM attention (required for attention sinks).")
        return True

    if force_use_trtllm is None:
        # CLI argument not set - use auto-detection
        if is_prefill:
            # Prefill auto-detection
            use_trtllm = kv_cache_dtype == "auto"
            if use_trtllm:
                logger.warning_once("Using TRTLLM prefill attention (auto-detected).")
        else:
            # Decode auto-detection
            use_trtllm = num_tokens <= 256 and kv_cache_dtype == "auto"
            if use_trtllm:
                logger.warning_once("Using TRTLLM decode attention (auto-detected).")
        return use_trtllm

    # CLI argument is set to 1 - respect it
    logger.info_once(
        "Using TRTLLM attention (--attention-config.use_trtllm_attention is set to 1)"
    )
    return True
```