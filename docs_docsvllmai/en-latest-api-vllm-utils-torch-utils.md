---
title: torch_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/utils/torch_utils/
source: sitemap
fetched_at: 2026-05-07T21:38:59.361674074-03:00
rendered_js: false
word_count: 1277
summary: This document provides a collection of utility functions for PyTorch tensor management, including memory handling, stride canonicalization, and custom object wrapping for graph compilation.
tags:
    - pytorch
    - tensor-manipulation
    - cuda-optimization
    - memory-management
    - vllm-utils
category: reference
---

## LayerName [¶](#vllm.utils.torch_utils.LayerName "Permanent link")

Bases: `OpaqueBase`

Wraps a module name string for use as a torch opaque type.

When torch &gt;= 2.11, this is registered as a hoisted value-type opaque object so that torch.compile lifts it as a graph input instead of baking it as a constant. This avoids per-layer recompilation for custom ops that accept layer name strings (attention, MOE, KV cache, etc.).

Source code in `vllm/utils/torch_utils.py`

```
classLayerName(OpaqueBase):  # type: ignore[misc]
"""Wraps a module name string for use as a torch opaque type.

    When torch >= 2.11, this is registered as a hoisted value-type opaque
    object so that torch.compile lifts it as a graph input instead of baking
    it as a constant.  This avoids per-layer recompilation for custom ops
    that accept layer name strings (attention, MOE, KV cache, etc.).
    """

    def__init__(self, value: str):
        self.value = value

    def__eq__(self, other):
        return isinstance(other, LayerName) and self.value == other.value

    def__hash__(self):
        return hash(self.value)

    def__fx_repr__(self):
        return (f"LayerName({self.value!r})", {"LayerName": LayerName})
```

## \_encode\_layer\_name [¶](#vllm.utils.torch_utils._encode_layer_name "Permanent link")

```
_encode_layer_name(layer_name: str) -> str | LayerName
```

Wrap a str layer name as LayerName when enabled.

Source code in `vllm/utils/torch_utils.py`

```
def_encode_layer_name(layer_name: str) -> str | LayerName:
"""Wrap a str layer name as LayerName when enabled."""
    return LayerName(layer_name) if _USE_LAYERNAME else layer_name
```

## \_nvfp4\_split\_data\_scale [¶](#vllm.utils.torch_utils._nvfp4_split_data_scale "Permanent link")

Split a single NVFP4 KV-side buffer into data and scale views.

The input is a 4D tensor for one KV side (K or V) whose last dimension is `full_dim = data_dim + scale_dim`. The physical layout within each side is \[data | scale], both packed contiguously.

Parameters:

Name Type Description Default `kv_side` `Tensor`

4D uint8 tensor with shape `(num_pages, dim_1, dim_2, full_dim)`. May be in any permutation order (NHD or HND).

*required*

Returns:

Type Description `Tensor`

`(data, scale)` where

`Tensor`

`data` is a uint8 view with shape

`tuple[Tensor, Tensor]`

`(num_pages, dim_1, dim_2, data_dim)`.

`tuple[Tensor, Tensor]`

`scale` is a float8\_e4m3fn view with shape

`tuple[Tensor, Tensor]`

`(num_pages, dim_1, dim_2, scale_dim)`.

Source code in `vllm/utils/torch_utils.py`

```
def_nvfp4_split_data_scale(
    kv_side: torch.Tensor,
) -> tuple[torch.Tensor, torch.Tensor]:
"""Split a single NVFP4 KV-side buffer into data and scale views.

    The input is a 4D tensor for one KV side (K or V) whose last
    dimension is ``full_dim = data_dim + scale_dim``.  The physical
    layout within each side is [data | scale], both packed contiguously.

    Args:
        kv_side: 4D uint8 tensor with shape
            ``(num_pages, dim_1, dim_2, full_dim)``.
            May be in any permutation order (NHD or HND).

    Returns:
        ``(data, scale)`` where
        ``data`` is a uint8 view with shape
        ``(num_pages, dim_1, dim_2, data_dim)``.
        ``scale`` is a float8_e4m3fn view with shape
        ``(num_pages, dim_1, dim_2, scale_dim)``.
    """
    num_pages = kv_side.shape[0]
    dim_1, dim_2 = kv_side.shape[1], kv_side.shape[2]
    full_dim = kv_side.shape[3]
    data_dim = full_dim * 8 // 9
    scale_dim = full_dim - data_dim

    data_per_kv = dim_1 * dim_2 * data_dim
    page_bytes = kv_side.stride(0)

    # Derive inner strides from the kv_side strides, scaling by the
    # ratio of the target dim to full_dim.  This preserves the physical
    # layout (NHD vs HND) encoded in the input tensor's strides.
    s1 = kv_side.stride(1) * data_dim // full_dim
    s2 = kv_side.stride(2) * data_dim // full_dim
    data_shape = (num_pages, dim_1, dim_2, data_dim)
    data_strides = (page_bytes, s1, s2, 1)

    s1_s = kv_side.stride(1) * scale_dim // full_dim
    s2_s = kv_side.stride(2) * scale_dim // full_dim
    scale_shape = (num_pages, dim_1, dim_2, scale_dim)
    scale_strides = (page_bytes, s1_s, s2_s, 1)

    base = kv_side.storage_offset()
    data = torch.as_strided(kv_side, data_shape, data_strides, storage_offset=base)
    scale = torch.as_strided(
        kv_side, scale_shape, scale_strides, storage_offset=base + data_per_kv
    ).view(torch.float8_e4m3fn)

    return data, scale
```

## \_resolve\_layer\_name [¶](#vllm.utils.torch_utils._resolve_layer_name "Permanent link")

```
_resolve_layer_name(layer_name: str | LayerName) -> str
```

Unwrap a LayerName to str, or return str unchanged.

Source code in `vllm/utils/torch_utils.py`

```
def_resolve_layer_name(layer_name: str | LayerName) -> str:
"""Unwrap a LayerName to str, or return str unchanged."""
    return layer_name.value if isinstance(layer_name, LayerName) else layer_name
```

## async\_tensor\_h2d [¶](#vllm.utils.torch_utils.async_tensor_h2d "Permanent link")

Asynchronously create a tensor and copy it from host to device.

Source code in `vllm/utils/torch_utils.py`

```
defasync_tensor_h2d(
    data: list,
    dtype: torch.dtype,
    target_device: str | torch.device,
    pin_memory: bool,
) -> torch.Tensor:
"""Asynchronously create a tensor and copy it from host to device."""
    t = torch.tensor(data, dtype=dtype, pin_memory=pin_memory, device="cpu")
    return t.to(device=target_device, non_blocking=True)
```

## aux\_stream [¶](#vllm.utils.torch_utils.aux_stream "Permanent link")

Ensures aux\_stream is initialized only once

Source code in `vllm/utils/torch_utils.py`

```
defaux_stream() -> torch.cuda.Stream | None:
"""
    Ensures aux_stream is initialized only once
    """
    global _aux_stream

    fromvllm.platformsimport current_platform

    if _aux_stream is None and current_platform.is_cuda_alike():
        _aux_stream = torch.cuda.Stream()

    return _aux_stream
```

## canonicalize\_singleton\_dim\_strides [¶](#vllm.utils.torch_utils.canonicalize_singleton_dim_strides "Permanent link")

Fix degenerate strides on size=1 dimensions for CUDA TMA compatibility.

PyTorch allows any stride on a size=1 dim (is\_contiguous() is always True there), so a size=1 dim may have stride=1 (2 bytes for bf16) instead of the canonical product(shape\[i+1:]). CUDA TMA on H100+ requires all non-outermost strides to be ≥16-byte aligned; stride=1 triggers cudaErrorIllegalInstruction. Zero-copy: patches stride metadata only via as\_strided; returns t unchanged if all size=1 strides are already canonical.

Source code in `vllm/utils/torch_utils.py`

```
defcanonicalize_singleton_dim_strides(t: torch.Tensor) -> torch.Tensor:
"""Fix degenerate strides on size=1 dimensions for CUDA TMA compatibility.

    PyTorch allows any stride on a size=1 dim (is_contiguous() is always True
    there), so a size=1 dim may have stride=1 (2 bytes for bf16) instead of
    the canonical product(shape[i+1:]).  CUDA TMA on H100+ requires all
    non-outermost strides to be ≥16-byte aligned; stride=1 triggers
    cudaErrorIllegalInstruction.  Zero-copy: patches stride metadata only via
    as_strided; returns t unchanged if all size=1 strides are already canonical.
    """
    if 1 not in t.shape:
        return t
    strides = list(t.stride())
    shape = t.shape
    prev_stride = 1
    changed = False
    for i in range(len(shape) - 1, -1, -1):
        if shape[i] == 1 and strides[i] != prev_stride:
            strides[i] = prev_stride
            changed = True
        prev_stride = strides[i] * shape[i]
    if not changed:
        return t
    return t.as_strided(t.shape, strides)
```

## common\_broadcastable\_dtype [¶](#vllm.utils.torch_utils.common_broadcastable_dtype "Permanent link")

Get the common `dtype` where all of the other `dtypes` can be cast to it without losing any information.

Source code in `vllm/utils/torch_utils.py`

```
defcommon_broadcastable_dtype(dtypes: Collection[torch.dtype]):
"""
    Get the common `dtype` where all of the other `dtypes` can be
    cast to it without losing any information.
    """
    return max(
        dtypes,
        key=lambda dtype: sum(is_lossless_cast(dt, dtype) for dt in dtypes),
    )
```

## current\_stream [¶](#vllm.utils.torch_utils.current_stream "Permanent link")

replace `torch.cuda.current_stream()` with `vllm.utils.current_stream()`. it turns out that `torch.cuda.current_stream()` is quite expensive, as it will construct a new stream object at each call. here we patch `torch.cuda.set_stream` to keep track of the current stream directly, so that we can avoid calling `torch.cuda.current_stream()`.

the underlying hypothesis is that we do not call `torch._C._cuda_setStream` from C/C++ code.

Source code in `vllm/utils/torch_utils.py`

```
defcurrent_stream() -> torch.cuda.Stream:
"""
    replace `torch.cuda.current_stream()` with `vllm.utils.current_stream()`.
    it turns out that `torch.cuda.current_stream()` is quite expensive,
    as it will construct a new stream object at each call.
    here we patch `torch.cuda.set_stream` to keep track of the current stream
    directly, so that we can avoid calling `torch.cuda.current_stream()`.

    the underlying hypothesis is that we do not call `torch._C._cuda_setStream`
    from C/C++ code.
    """
    fromvllm.platformsimport current_platform

    if not hasattr(_current_stream_tls, "value") or _current_stream_tls.value is None:
        # when this function is called before any stream is set,
        # we return the default stream.
        # On ROCm using the default 0 stream in combination with RCCL
        # is hurting performance.
        # On CUDA, we capture and replay cudagraph on the same stream,
        # so we need to avoid using the default stream as well. The default
        # stream cannot be used for cudagraph capture, see
        # https://github.com/pytorch/pytorch/blob/42ad9edfb754743fdae3276ade43de000beb4f60/aten/src/ATen/cuda/CUDAGraph.cpp#L77
        # for more details. Therefore, we create a dedicated stream per process.
        if current_platform.is_rocm() or current_platform.is_cuda():
            # torch.cuda.set_stream here is the alias of _pathed_set_stream
            torch.cuda.set_stream(torch.cuda.Stream())
        elif current_platform.is_cpu():
            _current_stream_tls.value = _StreamPlaceholder()
        else:
            current_stream = current_platform.current_stream
            if current_stream is not None:
                _current_stream_tls.value = current_stream()
            else:
                raise ValueError(
                    "Fail to set current stream, current platform "
                    "may not support current_stream with torch API"
                )
    return _current_stream_tls.value
```

## direct\_register\_custom\_op [¶](#vllm.utils.torch_utils.direct_register_custom_op "Permanent link")

```
direct_register_custom_op(
    op_name: str,
    op_func: Callable,
    mutates_args: list[str] | None = None,
    fake_impl: Callable | None = None,
    target_lib: Library | None = None,
    dispatch_key: str | None = None,
    tags: tuple[Tag, ...] = (),
)
```

`torch.library.custom_op` can have significant overhead because it needs to consider complicated dispatching logic. This function directly registers a custom op and dispatches it to the CUDA backend. See https://gist.github.com/youkaichao/ecbea9ec9fc79a45d2adce1784d7a9a5 for more details.

By default, the custom op is registered to the vLLM library. If you want to register it to a different library, you can pass the library object to the `target_lib` argument.

IMPORTANT: the lifetime of the operator is tied to the lifetime of the library object. If you want to bind the operator to a different library, make sure the library object is alive when the operator is used.

Source code in `vllm/utils/torch_utils.py`

```
defdirect_register_custom_op(
    op_name: str,
    op_func: Callable,
    mutates_args: list[str] | None = None,
    fake_impl: Callable | None = None,
    target_lib: Library | None = None,
    dispatch_key: str | None = None,
    tags: tuple[torch.Tag, ...] = (),
):
"""
    `torch.library.custom_op` can have significant overhead because it
    needs to consider complicated dispatching logic. This function
    directly registers a custom op and dispatches it to the CUDA backend.
    See https://gist.github.com/youkaichao/ecbea9ec9fc79a45d2adce1784d7a9a5
    for more details.

    By default, the custom op is registered to the vLLM library. If you
    want to register it to a different library, you can pass the library
    object to the `target_lib` argument.

    IMPORTANT: the lifetime of the operator is tied to the lifetime of the
    library object. If you want to bind the operator to a different library,
    make sure the library object is alive when the operator is used.
    """
    if mutates_args is None:
        mutates_args = []

    if dispatch_key is None:
        fromvllm.platformsimport current_platform

        dispatch_key = current_platform.dispatch_key

    schema_str = infer_schema(op_func, mutates_args=mutates_args)

    my_lib = target_lib or vllm_lib
    my_lib.define(op_name + schema_str, tags=tags)
    my_lib.impl(op_name, op_func, dispatch_key=dispatch_key)
    if fake_impl is not None:
        my_lib._register_fake(op_name, fake_impl)
```

## get\_accelerator\_view\_from\_cpu\_tensor [¶](#vllm.utils.torch_utils.get_accelerator_view_from_cpu_tensor "Permanent link")

```
get_accelerator_view_from_cpu_tensor(
    cpu_tensor: Tensor,
) -> Tensor
```

Get an accelerator view of a CPU tensor using Unified Virtual Addressing (UVA).

Source code in `vllm/utils/torch_utils.py`

```
defget_accelerator_view_from_cpu_tensor(cpu_tensor: torch.Tensor) -> torch.Tensor:
"""
    Get an accelerator view of a CPU tensor using Unified Virtual Addressing (UVA).
    """
    fromvllm.platformsimport current_platform

    if current_platform.is_xpu():
        assert cpu_tensor.is_pinned(), "CPU tensor must be pinned"
        return torch.ops._C.get_xpu_view_from_cpu_tensor(cpu_tensor)
    elif current_platform.is_cuda_alike():
        return torch.ops._C.get_cuda_view_from_cpu_tensor(cpu_tensor)
    else:
        raise ValueError(
            f"`get_accelerator_view_from_cpu_tensor` is currently "
            f"not supported in: {current_platform.device_name}"
        )
```

## get\_dtype\_size [¶](#vllm.utils.torch_utils.get_dtype_size "Permanent link")

Get the size of the data type in bytes.

Source code in `vllm/utils/torch_utils.py`

```
defget_dtype_size(dtype: torch.dtype) -> int:
"""Get the size of the data type in bytes."""
    return torch.tensor([], dtype=dtype).element_size()
```

## get\_kv\_cache\_quant\_algo\_dtype [¶](#vllm.utils.torch_utils.get_kv_cache_quant_algo_dtype "Permanent link")

```
get_kv_cache_quant_algo_dtype(
    quant_cfg: dict[str, Any],
) -> dtype | None
```

Get the KV cache quantization algorithm dtype from the quantization config.

Source code in `vllm/utils/torch_utils.py`

```
defget_kv_cache_quant_algo_dtype(quant_cfg: dict[str, Any]) -> torch.dtype | None:
"""Get the KV cache quantization algorithm dtype from the quantization config."""
    kv_algo_str = get_kv_cache_quant_algo_string(quant_cfg)
    if kv_algo_str is not None and kv_algo_str != "auto":
        # Only convert if we have a valid dtype string (not "auto" fallback)
        return STR_DTYPE_TO_TORCH_DTYPE[kv_algo_str]
    return None
```

## get\_kv\_cache\_quant\_algo\_string [¶](#vllm.utils.torch_utils.get_kv_cache_quant_algo_string "Permanent link")

```
get_kv_cache_quant_algo_string(
    quant_cfg: dict[str, Any],
) -> str | None
```

Get the KV cache quantization algorithm string from the quantization config.

Maps various FP8 format names to vLLM's standard cache dtype strings. Returns None if no kv\_cache\_quant\_algo is specified. Returns "auto" if the value is not recognized/supported.

Source code in `vllm/utils/torch_utils.py`

```
defget_kv_cache_quant_algo_string(quant_cfg: dict[str, Any]) -> str | None:
"""Get the KV cache quantization algorithm string from the quantization config.

    Maps various FP8 format names to vLLM's standard cache dtype strings.
    Returns None if no kv_cache_quant_algo is specified.
    Returns "auto" if the value is not recognized/supported.
    """
    # Mapping from model config values to vLLM cache_dtype strings

    quant_method = quant_cfg.get("quant_method", "")
    if quant_method.startswith("modelopt"):
        quantization_inner = quant_cfg.get("quantization", quant_cfg)
        # Check if quant config is specified and use kv cache quant algo
        kv_algo = (
            quantization_inner.get("kv_cache_scheme")
            or quant_cfg.get("kv_cache_scheme")
            or quantization_inner.get("kv_cache_quant_algo")
            or quant_cfg.get("kv_cache_quant_algo")
        )
        if isinstance(kv_algo, dict):
            if (
                kv_algo.get("dynamic") is False
                and kv_algo.get("num_bits") == 8
                and kv_algo.get("type") == "float"
            ):
                kv_algo = "fp8"
            elif kv_algo.get("num_bits") == 4 and kv_algo.get("type") == "float":
                kv_algo = "nvfp4"
            else:
                # Unknown/unsupported format - return "auto" as safe fallback
                logger.warning(
                    "WARNING: Unknown kv_cache_quant_algo '%s' in model "
                    "config. Supported values: %s. Falling back to 'auto'.",
                    f"{kv_algo}",
                    list(MODELOPT_TO_VLLM_KV_CACHE_DTYPE_MAP.keys()),
                )
                return "auto"
        if isinstance(kv_algo, str):
            kv_algo_lower = kv_algo.lower()

            # Try to map to vLLM's standard format
            if kv_algo_lower in MODELOPT_TO_VLLM_KV_CACHE_DTYPE_MAP:
                return MODELOPT_TO_VLLM_KV_CACHE_DTYPE_MAP[kv_algo_lower]
            else:
                # Unknown/unsupported format - return "auto" as safe fallback
                logger.warning(
                    "WARNING: Unknown kv_cache_quant_algo '%s' in model "
                    "config. Supported values: %s. Falling back to 'auto'.",
                    kv_algo,
                    list(MODELOPT_TO_VLLM_KV_CACHE_DTYPE_MAP.keys()),
                )
                return "auto"
    return None
```

## guard\_cuda\_initialization [¶](#vllm.utils.torch_utils.guard_cuda_initialization "Permanent link")

```
guard_cuda_initialization()
```

Avoid unexpected CUDA initialization.

Source code in `vllm/utils/torch_utils.py`

```
@contextlib.contextmanager
defguard_cuda_initialization():
"""Avoid unexpected CUDA initialization."""
    fromvllm.platformsimport current_platform

    if not current_platform.is_cuda():
        yield
        return

    old_value = os.environ.get("CUDA_VISIBLE_DEVICES")
    os.environ["CUDA_VISIBLE_DEVICES"] = ""
    try:
        yield
    except Exception as e:
        if "No CUDA GPUs are available" in str(e):
            err_msg = "CUDA initialization is blocked."
        else:
            err_msg = str(e)
        raise RuntimeError(err_msg) frome
    finally:
        if old_value is None:
            del os.environ["CUDA_VISIBLE_DEVICES"]
        else:
            os.environ["CUDA_VISIBLE_DEVICES"] = old_value
```

## is\_lossless\_cast [¶](#vllm.utils.torch_utils.is_lossless_cast "Permanent link")

```
is_lossless_cast(src_dtype: dtype, tgt_dtype: dtype)
```

Test whether it is lossless to cast a tensor from `src_dtype` to `tgt_dtype`.

Source code in `vllm/utils/torch_utils.py`

```
defis_lossless_cast(src_dtype: torch.dtype, tgt_dtype: torch.dtype):
"""
    Test whether it is lossless to cast a tensor from
    `src_dtype` to `tgt_dtype`.
    """
    if src_dtype == tgt_dtype:
        return True

    src_level = _get_precision_level(src_dtype)
    tgt_level = _get_precision_level(tgt_dtype)

    if src_level < tgt_level:
        return True
    if src_level > tgt_level:
        return False

    # Compare integral types
    if not src_dtype.is_floating_point and not src_dtype.is_complex:
        src_info = torch.iinfo(src_dtype)
        tgt_info = torch.iinfo(tgt_dtype)
        return src_info.min >= tgt_info.min and src_info.max <= tgt_info.max

    # Compare floating-point types
    src_info = torch.finfo(src_dtype)
    tgt_info = torch.finfo(tgt_dtype)
    return (
        src_info.min >= tgt_info.min
        and src_info.max <= tgt_info.max
        and src_info.resolution >= tgt_info.resolution
    )
```

## is\_strictly\_contiguous [¶](#vllm.utils.torch_utils.is_strictly_contiguous "Permanent link")

Check if tensor is contiguous AND has no degenerate strides.

A degenerate stride occurs when a dimension has size 1 but the stride doesn't match the canonical contiguous layout. This can cause issues in some CUDA kernels that rely on stride values for memory access.

For a C-contiguous tensor of shape (d0, d1, ..., dn), the expected strides are: stride\[i] = product(shape\[i+1:]) for all i, with stride\[-1]=1.

Example with torch.Size(\[16, 1, 8, 32]): - Canonical strides: (256, 256, 32, 1) - Degenerate strides: (256, 1, 32, 1) # dim=1 has size=1, allowing # non-canonical stride in dim=0

Source code in `vllm/utils/torch_utils.py`

```
defis_strictly_contiguous(t: torch.Tensor) -> bool:
"""
    Check if tensor is contiguous AND has no degenerate strides.

    A degenerate stride occurs when a dimension has size 1 but the stride
    doesn't match the canonical contiguous layout. This can cause issues
    in some CUDA kernels that rely on stride values for memory access.

    For a C-contiguous tensor of shape (d0, d1, ..., dn), the expected
    strides are: stride[i] = product(shape[i+1:]) for all i, with stride[-1]=1.

    Example with torch.Size([16, 1, 8, 32]):
        - Canonical strides: (256, 256, 32, 1)
        - Degenerate strides: (256, 1, 32, 1)  # dim=1 has size=1, allowing
                                                  # non-canonical stride in dim=0
    """
    if not t.is_contiguous():
        return False

    # Check that strides match canonical contiguous layout
    shape = t.shape
    strides = t.stride()
    expected_stride = 1
    for i in range(len(shape) - 1, -1, -1):
        if strides[i] != expected_stride:
            return False
        expected_stride *= shape[i]
    return True
```

## is\_torch\_equal [¶](#vllm.utils.torch_utils.is_torch_equal "Permanent link")

```
is_torch_equal(target: str) -> bool
```

Check if the installed torch version is == the target version.

Parameters:

Name Type Description Default `target` `str`

a version string, like "2.6.0".

*required*

Returns:

Type Description `bool`

Whether the condition meets.

Source code in `vllm/utils/torch_utils.py`

```
defis_torch_equal(target: str) -> bool:
"""Check if the installed torch version is == the target version.

    Args:
        target: a version string, like "2.6.0".

    Returns:
        Whether the condition meets.
    """
    try:
        return _is_torch_equal(target)
    except Exception:
        return Version(importlib.metadata.version("torch")) == Version(target)
```

## is\_torch\_equal\_or\_newer [¶](#vllm.utils.torch_utils.is_torch_equal_or_newer "Permanent link")

```
is_torch_equal_or_newer(target: str) -> bool
```

Check if the installed torch version is &gt;= the target version.

Parameters:

Name Type Description Default `target` `str`

a version string, like "2.6.0".

*required*

Returns:

Type Description `bool`

Whether the condition meets.

Source code in `vllm/utils/torch_utils.py`

```
defis_torch_equal_or_newer(target: str) -> bool:
"""Check if the installed torch version is >= the target version.

    Args:
        target: a version string, like "2.6.0".

    Returns:
        Whether the condition meets.
    """
    try:
        return _is_torch_equal_or_newer(str(torch.__version__), target)
    except Exception:
        # Fallback to PKG-INFO to load the package info, needed by the doc gen.
        return Version(importlib.metadata.version("torch")) >= Version(target)
```

## kv\_cache\_uses\_per\_token\_head\_scales [¶](#vllm.utils.torch_utils.kv_cache_uses_per_token_head_scales "Permanent link")

```
kv_cache_uses_per_token_head_scales(
    kv_cache_dtype: str,
) -> bool
```

Return True if *kv\_cache\_dtype* needs per-token-head scales.

Source code in `vllm/utils/torch_utils.py`

```
defkv_cache_uses_per_token_head_scales(kv_cache_dtype: str) -> bool:
"""Return True if *kv_cache_dtype* needs per-token-head scales."""
    return kv_cache_dtype.endswith("per_token_head")
```

## make\_ndarray\_with\_pad [¶](#vllm.utils.torch_utils.make_ndarray_with_pad "Permanent link")

Make a padded array from 2D inputs.

The padding is applied to the end of each inner list until it reaches `max_len`.

Source code in `vllm/utils/torch_utils.py`

```
defmake_ndarray_with_pad(
    x: list[list[T]],
    pad: T,
    dtype: npt.DTypeLike,
    *,
    max_len: int | None = None,
) -> npt.NDArray:
"""
    Make a padded array from 2D inputs.

    The padding is applied to the end of each inner list until it reaches
    `max_len`.
    """
    if max_len is None:
        # Unlike for most functions, map is faster than a genexpr over `len`
        max_len = max(map(len, x), default=0)

    padded_x = np.full((len(x), max_len), pad, dtype=dtype)
    for ind, blocktb in enumerate(x):
        assert len(blocktb) <= max_len
        padded_x[ind, : len(blocktb)] = blocktb

    return padded_x
```

## make\_tensor\_with\_pad [¶](#vllm.utils.torch_utils.make_tensor_with_pad "Permanent link")

Make a padded tensor from 2D inputs.

The padding is applied to the end of each inner list until it reaches `max_len`.

Source code in `vllm/utils/torch_utils.py`

```
defmake_tensor_with_pad(
    x: list[list[T]],
    pad: T,
    dtype: torch.dtype,
    *,
    max_len: int | None = None,
    device: str | torch.device | None = None,
    pin_memory: bool = False,
) -> torch.Tensor:
"""
    Make a padded tensor from 2D inputs.

    The padding is applied to the end of each inner list until it reaches
    `max_len`.
    """
    np_dtype = TORCH_DTYPE_TO_NUMPY_DTYPE[dtype]
    padded_x = make_ndarray_with_pad(x, pad, np_dtype, max_len=max_len)

    tensor = torch.from_numpy(padded_x).to(device)
    if pin_memory:
        tensor = tensor.pin_memory()

    return tensor
```

## nvfp4\_kv\_cache\_full\_dim [¶](#vllm.utils.torch_utils.nvfp4_kv_cache_full_dim "Permanent link")

```
nvfp4_kv_cache_full_dim(head_size: int) -> int
```

Packed last dim for NVFP4 KV cache: fp4 data + fp8 block scales.

Source code in `vllm/utils/torch_utils.py`

```
defnvfp4_kv_cache_full_dim(head_size: int) -> int:
"""Packed last dim for NVFP4 KV cache: fp4 data + fp8 block scales."""
    return head_size // 2 + head_size // 16
```

## nvfp4\_kv\_cache\_split\_views [¶](#vllm.utils.torch_utils.nvfp4_kv_cache_split_views "Permanent link")

Split an NVFP4 KV cache tensor into data and scale views.

Accepts either a 5D tensor `(num_pages, 2, dim_2, dim_3, full_dim)` or a 4D single-side tensor `(num_pages, dim_2, dim_3, full_dim)`.

Per-page layout: \[K\_data | K\_scale | V\_data | V\_scale]. Each KV side is self-contained (data followed by its scale), so the 5D case simply splits each side independently.

The returned views are in the same dim order as the input (NHD or HND), so callers get views matching whichever order they passed in.

Parameters:

Name Type Description Default `kv_cache` `Tensor`

5D or 4D uint8 tensor where the last dimension is `full_dim = data_dim + scale_dim = 9 * head_size / 16`.

*required*

Returns:

Type Description `tuple`

For 5D input: `(k_data, v_data), (k_scale, v_scale)`

`tuple`

For 4D input (single KV side): `(data,), (scale,)`

Source code in `vllm/utils/torch_utils.py`

```
defnvfp4_kv_cache_split_views(kv_cache: torch.Tensor) -> tuple[tuple, tuple]:
"""Split an NVFP4 KV cache tensor into data and scale views.

    Accepts either a 5D tensor ``(num_pages, 2, dim_2, dim_3, full_dim)``
    or a 4D single-side tensor ``(num_pages, dim_2, dim_3, full_dim)``.

    Per-page layout: [K_data | K_scale | V_data | V_scale].
    Each KV side is self-contained (data followed by its scale), so the
    5D case simply splits each side independently.

    The returned views are in the same dim order as the input (NHD or
    HND), so callers get views matching whichever order they passed in.

    Args:
        kv_cache: 5D or 4D uint8 tensor where the last dimension is
            ``full_dim = data_dim + scale_dim = 9 * head_size / 16``.

    Returns:
        For 5D input:
            ``(k_data, v_data), (k_scale, v_scale)``
        For 4D input (single KV side):
            ``(data,), (scale,)``
    """
    if kv_cache.dim() == 4:
        data, scale = _nvfp4_split_data_scale(kv_cache)
        return (data,), (scale,)

    k_data, k_scale = _nvfp4_split_data_scale(kv_cache[:, 0])
    v_data, v_scale = _nvfp4_split_data_scale(kv_cache[:, 1])
    return (k_data, v_data), (k_scale, v_scale)
```

## resolve\_kv\_cache\_dtype\_string [¶](#vllm.utils.torch_utils.resolve_kv_cache_dtype_string "Permanent link")

```
resolve_kv_cache_dtype_string(
    kv_cache_dtype: str, model_config: ModelConfig
) -> str
```

Resolve 'auto' kv\_cache\_dtype to the actual string value from model config. Returns the resolved cache\_dtype string.

Source code in `vllm/utils/torch_utils.py`

```
defresolve_kv_cache_dtype_string(
    kv_cache_dtype: str, model_config: ModelConfig
) -> str:
"""Resolve 'auto' kv_cache_dtype to the actual string value from model config.
    Returns the resolved cache_dtype string.
    """
    if kv_cache_dtype != "auto":
        return kv_cache_dtype

    hf_cfg = getattr(model_config, "hf_config", None)
    if hf_cfg is not None:
        quant_cfg = getattr(hf_cfg, "quantization_config", None)
        if quant_cfg is not None:
            kv_algo_str = get_kv_cache_quant_algo_string(quant_cfg)
            if kv_algo_str is not None:
                return kv_algo_str

    # Default to auto (will be handled by downstream code)
    return "auto"
```

## set\_default\_torch\_dtype [¶](#vllm.utils.torch_utils.set_default_torch_dtype "Permanent link")

```
set_default_torch_dtype(dtype: dtype)
```

Sets the default torch dtype to the given dtype.

Source code in `vllm/utils/torch_utils.py`

```
@contextlib.contextmanager
defset_default_torch_dtype(dtype: torch.dtype):
"""Sets the default torch dtype to the given dtype."""
    old_dtype = torch.get_default_dtype()
    torch.set_default_dtype(dtype)
    yield
    torch.set_default_dtype(old_dtype)
```

## set\_default\_torch\_num\_threads [¶](#vllm.utils.torch_utils.set_default_torch_num_threads "Permanent link")

```
set_default_torch_num_threads(
    num_threads: int | None = None,
)
```

Sets the default number of threads for PyTorch to the given value.

`None` means using the value of the environment variable `OMP_NUM_THREADS` (or `1` if that is not available).

Source code in `vllm/utils/torch_utils.py`

```
@contextlib.contextmanager
defset_default_torch_num_threads(num_threads: int | None = None):
"""
    Sets the default number of threads for PyTorch to the given value.

    `None` means using the value of the environment variable `OMP_NUM_THREADS`
    (or `1` if that is not available).
    """
    if num_threads is None:
        num_threads = 1

        try:
            num_threads = int(os.environ["OMP_NUM_THREADS"])
        except KeyError:
            logger.debug_once(
                "OMP_NUM_THREADS is not set; defaulting Torch threads to %d.",
                num_threads,
            )
        except ValueError:
            logger.warning_once(
                "OMP_NUM_THREADS is invalid; defaulting Torch threads to %d.",
                num_threads,
            )

    old_num_threads = torch.get_num_threads()
    torch.set_num_threads(num_threads)

    try:
        yield
    finally:
        torch.set_num_threads(old_num_threads)
```

## weak\_ref\_tensor [¶](#vllm.utils.torch_utils.weak_ref_tensor "Permanent link")

```
weak_ref_tensor(tensor: Any) -> Any
```

Create a weak reference to a tensor. The new tensor will share the same data as the original tensor, but will not keep the original tensor alive. This ignores 0-size tensors as those don't allocate any memory.

Source code in `vllm/utils/torch_utils.py`

```
defweak_ref_tensor(tensor: Any) -> Any:
"""
    Create a weak reference to a tensor.
    The new tensor will share the same data as the original tensor,
    but will not keep the original tensor alive.
    This ignores 0-size tensors as those don't allocate any memory.
    """
    if isinstance(tensor, torch.Tensor) and tensor.numel() > 0:
        return torch.ops._C.weak_ref_tensor(tensor)
    else:
        return tensor
```

## weak\_ref\_tensors [¶](#vllm.utils.torch_utils.weak_ref_tensors "Permanent link")

Convenience function to create weak references to tensors, for single tensor, list of tensors or tuple of tensors.

Source code in `vllm/utils/torch_utils.py`

```
defweak_ref_tensors(
    tensors: torch.Tensor
    | list[torch.Tensor]
    | tuple[torch.Tensor]
    | IntermediateTensors,
) -> torch.Tensor | list[Any] | tuple[Any] | Any:
"""
    Convenience function to create weak references to tensors,
    for single tensor, list of tensors or tuple of tensors.
    """
    if isinstance(tensors, torch.Tensor):
        return weak_ref_tensor(tensors)
    if isinstance(tensors, list):
        return [weak_ref_tensor(t) for t in tensors]
    if isinstance(tensors, tuple):
        return tuple(weak_ref_tensor(t) for t in tensors)

    # For IntermediateTensors used in pipeline parallelism
    fromvllm.sequenceimport IntermediateTensors

    if isinstance(tensors, IntermediateTensors):
        ret = IntermediateTensors(
            {key: weak_ref_tensor(val) for key, val in tensors.tensors.items()}
        )
        return ret
    raise ValueError("Invalid type for tensors")
```