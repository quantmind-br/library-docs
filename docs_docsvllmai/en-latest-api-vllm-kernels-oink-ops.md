---
title: oink_ops - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/kernels/oink_ops/
source: sitemap
fetched_at: 2026-05-07T21:22:16.923955696-03:00
rendered_js: false
word_count: 140
summary: This document describes the vLLM module for registering and validating Oink-based kernel operations, including hardware-specific constraints and stride compatibility requirements.
tags:
    - vllm
    - kernel-optimization
    - torch-ops
    - stride-constraints
    - oink-integration
category: reference
---

## vllm.kernels.oink\_ops [¶](#vllm.kernels.oink_ops "Permanent link")

This file registers Oink implementations for vLLM IR ops.

vLLM does not depend on the external Oink repository/package. When an external plugin registers torch.library.custom\_op entrypoints under the `oink::` namespace (e.g. via vLLM's general\_plugins mechanism), these ops will be marked as supported. To dispatch to those ops, set kernel\_config.ir\_op\_priority. to oink. Alternatively, `VLLM_USE_OINK_OPS=1` will add this to priority by default.

## oink\_add\_rms\_supported `module-attribute` [¶](#vllm.kernels.oink_ops.oink_add_rms_supported "Permanent link")

```
oink_add_rms_supported = (
    lambda x, x_residual, weight, epsilon, variance_size=None: (
        variance_size is None
        and weight is not None
        and dim() >= 2
        and dtype == dtype
        and is_contiguous()
        and _can_view_as_2d(x)
        and _is_oink_stride_compatible_2d(
            view(-1, shape[-1])
        )
        and dtype == dtype
        and shape == shape
        and _can_view_as_2d(x_residual)
        and _is_oink_stride_compatible_2d(
            view(-1, shape[-1])
        )
    )
)
```

Oink fused\_add\_rms\_norm has the same constraints as rms\_norm, and residual must be 2d-like with compatible strides.

## oink\_rms\_supported `module-attribute` [¶](#vllm.kernels.oink_ops.oink_rms_supported "Permanent link")

```
oink_rms_supported = (
    lambda x, weight, epsilon, variance_size=None: (
        variance_size is None
        and weight is not None
        and dim() >= 2
        and dtype == dtype
        and is_contiguous()
        and _can_view_as_2d(x)
        and _is_oink_stride_compatible_2d(
            view(-1, shape[-1])
        )
    )
)
```

Oink rms only supports 2d-like inputs with contiguous weight and no variance\_size override.

## \_can\_view\_as\_2d [¶](#vllm.kernels.oink_ops._can_view_as_2d "Permanent link")

Return True if x.view(-1, x.shape\[-1]) is viewable (no copy).

Source code in `vllm/kernels/oink_ops.py`

```
def_can_view_as_2d(x: Tensor) -> bool:
"""Return True if x.view(-1, x.shape[-1]) is viewable (no copy)."""
    if x.dim() < 2:
        return False
    if x.dim() == 2:
        return True
    # For a view(-1, N) to be valid, all leading dims must be contiguous with
    # respect to each other (size-1 dims are ignored).
    for dim in range(x.dim() - 1):
        # Strides for size-1 dims are irrelevant and can be arbitrary.
        if x.size(dim + 1) != 1 and x.stride(dim) != x.stride(dim + 1) * x.size(
            dim + 1
        ):
            return False
    return True
```

## \_is\_oink\_stride\_compatible\_2d [¶](#vllm.kernels.oink_ops._is_oink_stride_compatible_2d "Permanent link")

```
_is_oink_stride_compatible_2d(x_2d: Tensor) -> bool
```

Return True if x\_2d meets Oink's pointer-path stride constraints.

Source code in `vllm/kernels/oink_ops.py`

```
def_is_oink_stride_compatible_2d(x_2d: Tensor) -> bool:
"""Return True if x_2d meets Oink's pointer-path stride constraints."""
    if x_2d.dim() != 2:
        return False
    if x_2d.stride(1) != 1:
        return False
    # Match Oink's vectorization constraint: stride(0) divisible by 256b.
    if x_2d.dtype in (torch.float16, torch.bfloat16):
        divby = 16
    elif x_2d.dtype == torch.float32:
        divby = 8
    else:
        return False
    return (x_2d.stride(0) % divby) == 0
```

## has\_oink\_op [¶](#vllm.kernels.oink_ops.has_oink_op "Permanent link")

Check if a specific oink op is registered.

Source code in `vllm/kernels/oink_ops.py`

```
defhas_oink_op(name: str) -> bool:
"""Check if a specific oink op is registered."""
    return OINK_AVAILABLE and hasattr(torch.ops.oink, name)
```