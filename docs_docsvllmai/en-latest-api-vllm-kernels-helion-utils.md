---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/kernels/helion/utils/
source: sitemap
fetched_at: 2026-05-07T21:22:16.032163893-03:00
rendered_js: false
word_count: 59
summary: This document describes a utility function for canonicalizing GPU names into standardized platform identifiers by normalizing string formatting and applying predefined aliases.
tags:
    - gpu-management
    - kernel-utils
    - string-normalization
    - platform-identification
    - vllm-framework
category: reference
---

## vllm.kernels.helion.utils [¶](#vllm.kernels.helion.utils "Permanent link")

Utility functions for Helion kernel management.

## canonicalize\_gpu\_name [¶](#vllm.kernels.helion.utils.canonicalize_gpu_name "Permanent link")

```
canonicalize_gpu_name(name: str) -> str
```

Canonicalize GPU name for use as a platform identifier.

Converts to lowercase, replaces spaces and hyphens with underscores, and maps known variant names to their canonical form via \_GPU\_NAME\_ALIASES. e.g., "NVIDIA H100 80GB HBM3" -&gt; "nvidia\_h100" "NVIDIA A100-SXM4-80GB" -&gt; "nvidia\_a100" "AMD Instinct MI300X" -&gt; "amd\_instinct\_mi300x"

Source code in `vllm/kernels/helion/utils.py`

```
defcanonicalize_gpu_name(name: str) -> str:
"""
    Canonicalize GPU name for use as a platform identifier.

    Converts to lowercase, replaces spaces and hyphens with underscores,
    and maps known variant names to their canonical form via _GPU_NAME_ALIASES.
    e.g., "NVIDIA H100 80GB HBM3" -> "nvidia_h100"
          "NVIDIA A100-SXM4-80GB" -> "nvidia_a100"
          "AMD Instinct MI300X"   -> "amd_instinct_mi300x"
    """
    if not name or not name.strip():
        raise ValueError("GPU name cannot be empty")
    name = name.lower()
    name = name.replace(" ", "_")
    name = name.replace("-", "_")
    if name in _GPU_NAME_ALIASES:
        return _GPU_NAME_ALIASES[name]
    return name
```