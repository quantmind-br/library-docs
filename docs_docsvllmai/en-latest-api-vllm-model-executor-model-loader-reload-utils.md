---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/reload/utils/
source: sitemap
fetched_at: 2026-05-07T21:28:47.72921579-03:00
rendered_js: false
word_count: 138
summary: This document provides a reference for utility functions used to inspect, measure, and manage model layer weights and tensors during reloading processes.
tags:
    - model-loading
    - tensor-management
    - vllm
    - weight-reloading
    - pytorch-utilities
category: reference
---

## get\_info\_size [¶](#vllm.model_executor.model_loader.reload.utils.get_info_size "Permanent link")

```
get_info_size(info: LayerReloadingInfo) -> int
```

Calculate the number of bytes used by loaded weights for a given layer

:param info: layerwise info to get size of :return: number of bytes used by loaded weights

Source code in `vllm/model_executor/model_loader/reload/utils.py`

```
defget_info_size(info: LayerReloadingInfo) -> int:
"""
    Calculate the number of bytes used by loaded weights for a given layer

    :param info: layerwise info to get size of
    :return: number of bytes used by loaded weights
    """
    return sum(
        value.nbytes
        for _, args in info.loaded_weights
        for value in args.arguments.values()
        if isinstance(value, torch.Tensor) and value.device.type not in ("meta", "cpu")
    )
```

## get\_layer\_params\_buffers [¶](#vllm.model_executor.model_loader.reload.utils.get_layer_params_buffers "Permanent link")

```
get_layer_params_buffers(layer: Module) -> LayerTensors
```

Get all parameters and buffers of a module as a tuple of dicts.

Source code in `vllm/model_executor/model_loader/reload/utils.py`

```
defget_layer_params_buffers(layer: torch.nn.Module) -> LayerTensors:
"""Get all parameters and buffers of a module as a tuple of dicts."""
    return (
        {name: param for name, param in layer._parameters.items() if param is not None},
        {name: buffer for name, buffer in layer._buffers.items() if buffer is not None},
    )
```

## get\_layer\_size [¶](#vllm.model_executor.model_loader.reload.utils.get_layer_size "Permanent link")

Calculate total number of elements across loadable tensors in a layer.

Excludes SKIP\_TENSORS (e.g. \_expert\_map) which are never moved to meta device and never loaded via weight\_loader during layerwise reload.

Source code in `vllm/model_executor/model_loader/reload/utils.py`

```
defget_layer_size(layer: torch.nn.Module) -> int:
"""Calculate total number of elements across loadable tensors in a layer.

    Excludes SKIP_TENSORS (e.g. _expert_map) which are never moved to meta
    device and never loaded via weight_loader during layerwise reload.
    """
    from.metaimport SKIP_TENSORS

    return sum(
        tensor.numel()
        for name, tensor in get_layer_tensors(layer).items()
        if name not in SKIP_TENSORS
    )
```

## get\_layer\_tensors [¶](#vllm.model_executor.model_loader.reload.utils.get_layer_tensors "Permanent link")

Get all parameters and buffers from a module as a dict.

Source code in `vllm/model_executor/model_loader/reload/utils.py`

```
defget_layer_tensors(layer: torch.nn.Module) -> dict[str, torch.Tensor]:
"""Get all parameters and buffers from a module as a dict."""
    params, buffers = get_layer_params_buffers(layer)
    return params | buffers
```

## has\_device\_tensors [¶](#vllm.model_executor.model_loader.reload.utils.has_device_tensors "Permanent link")

Return True if the loaded weights exist on an accelerator device

:param bound\_args: args to load weights :return: True if weights are on accelerator device

Source code in `vllm/model_executor/model_loader/reload/utils.py`

```
defhas_device_tensors(bound_args: BoundArguments) -> bool:
"""
    Return True if the loaded weights exist on an accelerator device

    :param bound_args: args to load weights
    :return: True if weights are on accelerator device
    """
    return any(
        isinstance(value, torch.Tensor) and value.device.type not in ("meta", "cpu")
        for value in bound_args.arguments.values()
    )
```