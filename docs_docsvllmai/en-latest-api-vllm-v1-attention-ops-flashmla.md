---
title: flashmla - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/attention/ops/flashmla/
source: sitemap
fetched_at: 2026-05-07T21:39:58.192570976-03:00
rendered_js: false
word_count: 22
summary: This document outlines the function signatures and support requirements for checking the compatibility of FlashMLA dense and sparse operations within the vLLM engine.
tags:
    - vllm
    - flashmla
    - attention-ops
    - gpu-compatibility
    - hopper
    - blackwell
category: api
---

## vllm.v1.attention.ops.flashmla [¶](#vllm.v1.attention.ops.flashmla "Permanent link")

## is\_flashmla\_dense\_supported [¶](#vllm.v1.attention.ops.flashmla.is_flashmla_dense_supported "Permanent link")

Return: is\_supported\_flag, unsupported\_reason (optional).

Source code in `vllm/v1/attention/ops/flashmla.py`

```
defis_flashmla_dense_supported() -> tuple[bool, str | None]:
"""
    Return: is_supported_flag, unsupported_reason (optional).
    """
    is_available, maybe_reason = _is_flashmla_available()
    if not is_available:
        return False, maybe_reason
    if not current_platform.is_device_capability_family(90):
        return False, "FlashMLA Dense is only supported on Hopper devices."
    return True, None
```

## is\_flashmla\_sparse\_supported [¶](#vllm.v1.attention.ops.flashmla.is_flashmla_sparse_supported "Permanent link")

Return: is\_supported\_flag, unsupported\_reason (optional).

Source code in `vllm/v1/attention/ops/flashmla.py`

```
defis_flashmla_sparse_supported() -> tuple[bool, str | None]:
"""
    Return: is_supported_flag, unsupported_reason (optional).
    """
    is_available, maybe_reason = _is_flashmla_available()
    if not is_available:
        return False, maybe_reason
    if not (
        current_platform.is_device_capability_family(90)
        or current_platform.is_device_capability_family(100)
    ):
        return (
            False,
            "FlashMLA Sparse is only supported on Hopper and Blackwell devices.",
        )
    return True, None
```