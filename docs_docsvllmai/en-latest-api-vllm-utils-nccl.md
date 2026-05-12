---
title: nccl - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/utils/nccl/
source: sitemap
fetched_at: 2026-05-07T21:38:47.264164189-03:00
rendered_js: false
word_count: 68
summary: This document provides the API reference for utility functions used by vLLM to locate NCCL include paths and shared library files for CUDA and ROCm environments.
tags:
    - nccl
    - vllm-utils
    - environment-configuration
    - cuda
    - rocm
    - library-loading
category: api
---

## vllm.utils.nccl [¶](#vllm.utils.nccl "Permanent link")

## find\_nccl\_include\_paths [¶](#vllm.utils.nccl.find_nccl_include_paths "Permanent link")

```
find_nccl_include_paths() -> list[str] | None
```

Return possible include paths containing `nccl.h`.

Considers `VLLM_NCCL_INCLUDE_PATH` and the `nvidia-nccl-cuXX` package.

Source code in `vllm/utils/nccl.py`

```
deffind_nccl_include_paths() -> list[str] | None:
"""Return possible include paths containing `nccl.h`.

    Considers `VLLM_NCCL_INCLUDE_PATH` and the `nvidia-nccl-cuXX` package.
    """
    paths: list[str] = []
    inc = envs.VLLM_NCCL_INCLUDE_PATH
    if inc and os.path.isdir(inc):
        paths.append(inc)

    try:
        spec = importlib.util.find_spec("nvidia.nccl")
        if spec and (locs := getattr(spec, "submodule_search_locations", None)):
            for loc in locs:
                inc_dir = os.path.join(loc, "include")
                if os.path.exists(os.path.join(inc_dir, "nccl.h")):
                    paths.append(inc_dir)
    except Exception as e:
        logger.debug("Failed to find nccl include path from nvidia.nccl package: %s", e)

    seen: set[str] = set()
    out: list[str] = []
    for p in paths:
        if p and p not in seen:
            out.append(p)
            seen.add(p)
    return out or None
```

## find\_nccl\_library [¶](#vllm.utils.nccl.find_nccl_library "Permanent link")

```
find_nccl_library() -> str
```

Return NCCL/RCCL shared library name to load.

Uses `VLLM_NCCL_SO_PATH` if set; otherwise chooses by torch backend.

Source code in `vllm/utils/nccl.py`

```
deffind_nccl_library() -> str:
"""Return NCCL/RCCL shared library name to load.

    Uses `VLLM_NCCL_SO_PATH` if set; otherwise chooses by torch backend.
    """
    so_file = envs.VLLM_NCCL_SO_PATH
    if so_file:
        logger.info(
            "Found nccl from environment variable VLLM_NCCL_SO_PATH=%s", so_file
        )
    else:
        if torch.version.cuda is not None:
            so_file = "libnccl.so.2"
        elif torch.version.hip is not None:
            so_file = "librccl.so.1"
        else:
            raise ValueError("NCCL only supports CUDA and ROCm backends.")
        logger.debug_once("Found nccl from library %s", so_file)
    return so_file
```