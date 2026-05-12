---
title: fused_moe_lora_fp8_op - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/lora/ops/triton_ops/fused_moe_lora_fp8_op/
source: sitemap
fetched_at: 2026-05-07T21:22:49.237473621-03:00
rendered_js: false
word_count: 32
summary: This document explains a mechanism for caching memory pointers of LoRA weights using a dictionary-based lookup table to optimize retrieval during execution.
tags:
    - lora
    - memory-management
    - triton
    - pointer-caching
    - vllm
    - performance-optimization
category: concept
---

`_LORA_PTR_DICT` collects the required information during `profile_run`, After this, it remains constant and subsequent usage is through LUT. Refer to: https://github.com/triton-lang/triton/blob/release/3.1.x/python/tutorials/08-grouped-gemm.py

Source code in `vllm/lora/ops/triton_ops/fused_moe_lora_fp8_op.py`

```
def_get_ptr(lora_weights: list[torch.Tensor], device: torch.device):
"""
    `_LORA_PTR_DICT` collects the required information during `profile_run`,
    After this, it remains constant and subsequent usage is through LUT.
    Refer to:
    https://github.com/triton-lang/triton/blob/release/3.1.x/python/tutorials/08-grouped-gemm.py
    """
    key = tuple(lora_weight.data_ptr() for lora_weight in lora_weights)

    if (ptr_tensor := _LORA_PTR_DICT.get(key)) is not None:
        return ptr_tensor

    tensor_ptrs = []
    for lora_weight in lora_weights:
        tensor_ptrs.append(lora_weight.data_ptr())
    ptr_tensor = torch.tensor(tensor_ptrs, device=device, dtype=torch.uint64)

    _LORA_PTR_DICT[key] = ptr_tensor
    return _LORA_PTR_DICT.get(key)
```