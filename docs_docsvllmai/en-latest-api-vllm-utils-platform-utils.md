---
title: platform_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/utils/platform_utils/
source: sitemap
fetched_at: 2026-05-07T21:38:52.172675275-03:00
rendered_js: false
word_count: 73
summary: This document provides an API reference for utility functions used to retrieve hardware information and initialization status for CUDA and XPU devices within the vLLM platform.
tags:
    - cuda
    - xpu
    - device-properties
    - platform-utils
    - hardware-abstraction
    - gpu-initialization
category: api
---

## cuda\_get\_device\_properties [¶](#vllm.utils.platform_utils.cuda_get_device_properties "Permanent link")

Get specified CUDA device property values without initializing CUDA in the current process.

Source code in `vllm/utils/platform_utils.py`

```
defcuda_get_device_properties(
    device, names: Sequence[str], init_cuda=False
) -> tuple[Any, ...]:
"""Get specified CUDA device property values without initializing CUDA in
    the current process."""
    if init_cuda or cuda_is_initialized():
        props = torch.cuda.get_device_properties(device)
        return tuple(getattr(props, name) for name in names)

    # Run in subprocess to avoid initializing CUDA as a side effect.
    mp_ctx = multiprocessing.get_context("fork")
    with ProcessPoolExecutor(max_workers=1, mp_context=mp_ctx) as executor:
        return executor.submit(cuda_get_device_properties, device, names, True).result()
```

## cuda\_is\_initialized [¶](#vllm.utils.platform_utils.cuda_is_initialized "Permanent link")

```
cuda_is_initialized() -> bool
```

Check if CUDA is initialized.

Source code in `vllm/utils/platform_utils.py`

```
defcuda_is_initialized() -> bool:
"""Check if CUDA is initialized."""
    if not torch.cuda._is_compiled():
        return False
    return torch.cuda.is_initialized()
```

## is\_uva\_available `cached` [¶](#vllm.utils.platform_utils.is_uva_available "Permanent link")

```
is_uva_available() -> bool
```

Check if Unified Virtual Addressing (UVA) is available.

Source code in `vllm/utils/platform_utils.py`

```
@cache
defis_uva_available() -> bool:
"""Check if Unified Virtual Addressing (UVA) is available."""
    # UVA requires pinned memory.
    # TODO: Add more requirements for UVA if needed.
    return is_pin_memory_available()
```

## num\_compute\_units `cached` [¶](#vllm.utils.platform_utils.num_compute_units "Permanent link")

```
num_compute_units(device_id: int = 0) -> int
```

Get the number of compute units of the current device.

Source code in `vllm/utils/platform_utils.py`

```
@cache
defnum_compute_units(device_id: int = 0) -> int:
"""Get the number of compute units of the current device."""
    fromvllm.platformsimport current_platform

    return current_platform.num_compute_units(device_id)
```

## xpu\_is\_initialized [¶](#vllm.utils.platform_utils.xpu_is_initialized "Permanent link")

```
xpu_is_initialized() -> bool
```

Check if XPU is initialized.

Source code in `vllm/utils/platform_utils.py`

```
defxpu_is_initialized() -> bool:
"""Check if XPU is initialized."""
    if not torch.xpu._is_compiled():
        return False
    return torch.xpu.is_initialized()
```