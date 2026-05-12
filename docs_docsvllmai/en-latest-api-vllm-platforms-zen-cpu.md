---
title: zen_cpu - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/platforms/zen_cpu/
source: sitemap
fetched_at: 2026-05-07T21:34:36.981847528-03:00
rendered_js: false
word_count: 33
summary: This document defines the ZenCpuPlatform class, which integrates AMD Zen-specific optimizations including ZenDNN and Zentorch for improved CPU performance in vLLM.
tags:
    - amd-zen
    - zentorch
    - cpu-optimization
    - vllm-platform
    - linear-operations
    - weight-prepacking
category: reference
---

Bases: `CpuPlatform`

CPU platform with AMD Zen (ZenDNN/zentorch) optimizations.

Model-load time (dispatch\_cpu\_unquantized\_gemm in layers/utils.py): - Routes linear ops to zentorch\_linear\_unary. - When VLLM\_ZENTORCH\_WEIGHT\_PREPACK=1 (default), eagerly prepacks weights via zentorch\_weight\_prepack\_for\_linear.

Source code in `vllm/platforms/zen_cpu.py`

```
classZenCpuPlatform(CpuPlatform):
"""CPU platform with AMD Zen (ZenDNN/zentorch) optimizations.

    Model-load time (dispatch_cpu_unquantized_gemm in layers/utils.py):
      - Routes linear ops to zentorch_linear_unary.
      - When VLLM_ZENTORCH_WEIGHT_PREPACK=1 (default), eagerly prepacks
        weights via zentorch_weight_prepack_for_linear.
    """

    device_name: str = "cpu"
    device_type: str = "cpu"

    defis_zen_cpu(self) -> bool:
        # is_cpu() also returns True for this platform (inherited from CpuPlatform).
        return True

    # Currently, AMD CPUs do not support float16 compute.
    # Hence explicitly return bfloat16 and float32.
    @property
    defsupported_dtypes(self) -> list[torch.dtype]:
        return [torch.bfloat16, torch.float32]
```