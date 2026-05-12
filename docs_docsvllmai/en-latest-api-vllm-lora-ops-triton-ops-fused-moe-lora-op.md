---
title: fused_moe_lora_op - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/lora/ops/triton_ops/fused_moe_lora_op/
source: sitemap
fetched_at: 2026-05-07T21:22:50.193972893-03:00
rendered_js: false
word_count: 32
summary: This function retrieves and caches memory pointers for LoRA weights using a lookup table to improve efficiency during fused MoE operations.
tags:
    - lora
    - memory-management
    - pointer-caching
    - triton-kernels
    - fused-moe
category: reference
---

`_LORA_PTR_DICT` collects the required information during `profile_run`, After this, it remains constant and subsequent usage is through LUT. Refer to: https://github.com/triton-lang/triton/blob/release/3.1.x/python/tutorials/08-grouped-gemm.py

Source code in `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`

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