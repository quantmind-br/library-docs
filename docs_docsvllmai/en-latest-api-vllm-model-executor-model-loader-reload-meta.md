---
title: meta - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/reload/meta/
source: sitemap
fetched_at: 2026-05-07T21:28:44.026999161-03:00
rendered_js: false
word_count: 167
summary: This document provides utility functions and classes for managing weight loading and materializing meta tensors within PyTorch models, facilitating efficient model reloading and memory-efficient tensor handling.
tags:
    - pytorch
    - meta-tensors
    - model-loading
    - tensor-management
    - memory-optimization
    - weight-initialization
category: reference
---

Bases: `TorchDispatchMode`

Tracks total number of elements modified with `copy_`.

Useful for keeping track of weight loading where underlying weights can be arbitrarily transformed (such as with `narrow`) before calling copy.

Note: Assumes that copy kwargs are not used.

Source code in `vllm/model_executor/model_loader/reload/meta.py`

```
classCopyCounter(TorchDispatchMode):
"""
    Tracks total number of elements modified with `copy_`.

    Useful for keeping track of weight loading where underlying weights can be
    arbitrarily transformed (such as with `narrow`) before calling copy.

    Note: Assumes that copy kwargs are not used.
    """

    def__init__(self):
        super().__init__()
        self.copied_numel = 0

    def__torch_dispatch__(self, func, types, args=(), kwargs=None):
        if kwargs is None:
            kwargs = {}

        if func is torch.ops.aten.copy_.default:
            assert args[0].numel() == args[1].numel()
            self.copied_numel += args[0].numel()

        return func(*args, **kwargs)
```

Determine how many elements would be loaded by a weight loader call.

:param weight loader: used to load weights :param args: bound arguments to weight loader :return: number of elements loaded by the weight loader, the return value of the weight loader

Source code in `vllm/model_executor/model_loader/reload/meta.py`

```
defget_numel_loaded(
    weight_loader: Callable, args: inspect.BoundArguments
) -> tuple[int, object]:
"""
    Determine how many elements would be loaded by a weight loader call.

    :param weight loader: used to load weights
    :param args: bound arguments to weight loader
    :return: number of elements loaded by the weight loader, the return value of the
        weight loader
    """
    with CopyCounter() as counter:
        return_value = weight_loader(*args.args, **args.kwargs)
    return counter.copied_numel, return_value

materialize_layer(layer: Module, info: LayerReloadingInfo)
```

Materialize all meta tensors in a layer to actual tensors.

Source code in `vllm/model_executor/model_loader/reload/meta.py`

```
defmaterialize_layer(layer: torch.nn.Module, info: LayerReloadingInfo):
"""Materialize all meta tensors in a layer to actual tensors."""
    if layer.__class__.__name__ in SKIP_MODULES:
        return

    with info.restore_device:
        for name, tensor in get_layer_tensors(layer).items():
            if name not in SKIP_TENSORS and tensor.is_meta:
                setattr(layer, name, materialize_meta_tensor(tensor))
```

Materialize a meta tensor into an actual tensor on the current device. Should be called within the torch device context for the given rank.

Source code in `vllm/model_executor/model_loader/reload/meta.py`

```
defmaterialize_meta_tensor(meta_tensor: torch.Tensor) -> torch.Tensor:
"""
    Materialize a meta tensor into an actual tensor on the current device.
    Should be called within the torch device context for the given rank.
    """
    tensor = torch.empty_strided(
        size=tuple(meta_tensor.size()),
        stride=tuple(meta_tensor.stride()),
        dtype=meta_tensor.dtype,
        requires_grad=False,
    )
    tensor.__class__ = meta_tensor.__class__
    tensor.__dict__ = meta_tensor.__dict__.copy()
    return tensor

restore_layer_on_meta(
    layer: Module, info: LayerReloadingInfo
)
```

Restore a layer to model format with tensors on the meta device

Source code in `vllm/model_executor/model_loader/reload/meta.py`

```
defrestore_layer_on_meta(layer: torch.nn.Module, info: LayerReloadingInfo):
"""Restore a layer to model format with tensors on the meta device"""
    if layer.__class__.__name__ in SKIP_MODULES:
        return

    for name in get_layer_tensors(layer):
        if name not in SKIP_TENSORS:
            delattr(layer, name)

    restore_params, restore_buffers = info.restore_metadata
    for name, param in restore_params.items():
        if name not in SKIP_TENSORS:
            param = restore_layer_refs(param, layer)
            layer.register_parameter(name, param)

    for name, buffer in restore_buffers.items():
        if name not in SKIP_TENSORS:
            buffer = restore_layer_refs(buffer, layer)
            layer.register_buffer(name, buffer)
```

Convert a tensor to a meta tensor while preserving class and attributes.

Source code in `vllm/model_executor/model_loader/reload/meta.py`

```
defto_meta_tensor(tensor: torch.Tensor) -> torch.Tensor:
"""Convert a tensor to a meta tensor while preserving class and attributes."""
    meta_tensor = tensor.data.to("meta")
    meta_tensor.__class__ = tensor.__class__
    meta_tensor.__dict__ = tensor.__dict__.copy()
    return meta_tensor
```