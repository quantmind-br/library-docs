---
title: fa_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/attention/backends/fa_utils/
source: sitemap
fetched_at: 2026-05-07T21:39:06.385598713-03:00
rendered_js: false
word_count: 78
summary: This document describes a utility function that verifies whether a functional implementation of flash_attn_varlen_func is available for the current hardware platform.
tags:
    - flash-attention
    - vllm
    - hardware-compatibility
    - cuda
    - rocm
    - xpu
    - attention-backend
category: api
---

Check if flash\_attn\_varlen\_func is available.

This function determines whether the flash\_attn\_varlen\_func imported at module level is a working implementation or a stub.

Platform-specific sources: - CUDA: vllm.vllm\_flash\_attn.flash\_attn\_varlen\_func - XPU: xpu\_ops.flash\_attn\_varlen\_func - ROCm: upstream flash\_attn.flash\_attn\_varlen\_func (if available)

Note: This is separate from the AITER flash attention backend (rocm\_aiter\_fa.py) which uses rocm\_aiter\_ops.flash\_attn\_varlen\_func. The condition to use AITER is handled separately via \_aiter\_ops.is\_aiter\_found\_and\_supported().

Returns:

Name Type Description `bool` `bool`

True if a working flash\_attn\_varlen\_func implementation is available.

Source code in `vllm/v1/attention/backends/fa_utils.py`

```
defis_flash_attn_varlen_func_available() -> bool:
"""Check if flash_attn_varlen_func is available.

    This function determines whether the flash_attn_varlen_func imported at module
    level is a working implementation or a stub.

    Platform-specific sources:
    - CUDA: vllm.vllm_flash_attn.flash_attn_varlen_func
    - XPU: xpu_ops.flash_attn_varlen_func
    - ROCm: upstream flash_attn.flash_attn_varlen_func (if available)

    Note: This is separate from the AITER flash attention backend (rocm_aiter_fa.py)
    which uses rocm_aiter_ops.flash_attn_varlen_func. The condition to use AITER is
    handled separately via _aiter_ops.is_aiter_found_and_supported().

    Returns:
        bool: True if a working flash_attn_varlen_func implementation is available.
    """
    if current_platform.is_cuda() or current_platform.is_xpu():
        # CUDA and XPU always have flash_attn_varlen_func available
        return True

    if current_platform.is_rocm():
        # Use the flag set during module import to check if
        # upstream flash-attn was successfully imported
        return _ROCM_FLASH_ATTN_AVAILABLE

    return False
```