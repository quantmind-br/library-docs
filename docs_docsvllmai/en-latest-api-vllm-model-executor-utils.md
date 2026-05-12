---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/utils/
source: sitemap
fetched_at: 2026-05-07T21:33:57.013773358-03:00
rendered_js: false
word_count: 203
summary: This document provides utility functions for managing model layer parameters and tensor attributes within the vLLM model executor, specifically focusing on safe weight replacement and metadata assignment.
tags:
    - model-executor
    - parameter-management
    - weight-loading
    - pytorch-utils
    - cuda-graphs
category: reference
---

## vllm.model\_executor.utils [¶](#vllm.model_executor.utils "Permanent link")

Utils for model executor.

## replace\_parameter [¶](#vllm.model_executor.utils.replace_parameter "Permanent link")

```
replace_parameter(
    layer: Module,
    param_name: str,
    new_data: Tensor | None,
    prefer_copy: bool = False,
)
```

Replace a parameter of a layer while maintaining the ability to reload the weight. Called within implementations of the `process_weights_after_loading` method.

This function should not be called on weights which are tied/shared

Parameters:

Name Type Description Default `layer` `Module`

Layer containing parameter to replace

*required* `param_name` `str`

Name of parameter to replace

*required* `new_data` `Tensor | None`

New data of the new parameter, or None to set the parameter to None

*required* `prefer_copy` `bool`

If True and the existing parameter is compatible with `new_data` (same shape, dtype, and device), copy `new_data` into the existing parameter in place rather than re-registering a new parameter. This preserves the parameter's storage address (`data_ptr`), which is required for captured CUDA graphs to remain valid across weight updates (e.g. in RL training loops).

`False`

Source code in `vllm/model_executor/utils.py`

```
defreplace_parameter(
    layer: torch.nn.Module,
    param_name: str,
    new_data: torch.Tensor | None,
    prefer_copy: bool = False,
):
"""
    Replace a parameter of a layer while maintaining the ability to reload the weight.
    Called within implementations of the `process_weights_after_loading` method.

    This function should not be called on weights which are tied/shared

    Args:
        layer: Layer containing parameter to replace
        param_name: Name of parameter to replace
        new_data: New data of the new parameter, or None to set the parameter to None
        prefer_copy: If True and the existing parameter is compatible with
            ``new_data`` (same shape, dtype, and device), copy ``new_data``
            into the existing parameter in place rather than re-registering
            a new parameter. This preserves the parameter's storage address
            (``data_ptr``), which is required for captured CUDA graphs to
            remain valid across weight updates (e.g. in RL training loops).
    """
    # should not be used on a tied/shared param

    # If new_data is None, set the parameter to None
    if new_data is None:
        setattr(layer, param_name, None)
        return

    if isinstance(new_data, torch.nn.Parameter):
        new_data = new_data.data

    old_param: torch.nn.Parameter | None = getattr(layer, param_name, None)

    if (
        prefer_copy
        and old_param is not None
        and old_param.shape == new_data.shape
        and old_param.dtype == new_data.dtype
        and old_param.device == new_data.device
    ):
        old_param.copy_(new_data)
        return

    new_param = torch.nn.Parameter(new_data, requires_grad=False)

    if old_param is not None and hasattr(old_param, "weight_loader"):
        weight_loader = old_param.weight_loader
        set_weight_attrs(new_param, {"weight_loader": weight_loader})

    setattr(layer, param_name, new_param)
```

## set\_weight\_attrs [¶](#vllm.model_executor.utils.set_weight_attrs "Permanent link")

Set attributes on a weight tensor.

This method is used to set attributes on a weight tensor. This method will not overwrite existing attributes.

Parameters:

Name Type Description Default `weight` `Tensor`

The weight tensor.

*required* `weight_attrs` `dict[str, Any] | None`

A dictionary of attributes to set on the weight tensor.

*required*

Source code in `vllm/model_executor/utils.py`

```
defset_weight_attrs(
    weight: torch.Tensor,
    weight_attrs: dict[str, Any] | None,
):
"""Set attributes on a weight tensor.

    This method is used to set attributes on a weight tensor. This method
    will not overwrite existing attributes.

    Args:
        weight: The weight tensor.
        weight_attrs: A dictionary of attributes to set on the weight tensor.
    """
    if weight_attrs is None:
        return
    for key, value in weight_attrs.items():
        assert not hasattr(weight, key), f"Overwriting existing tensor attribute: {key}"

        # NOTE(woosuk): During weight loading, we often do something like:
        # narrowed_tensor = param.data.narrow(0, offset, len)
        # narrowed_tensor.copy_(real_weight)
        # expecting narrowed_tensor and param.data to share the same storage.
        # However, on TPUs, narrowed_tensor will lazily propagate to the base
        # tensor, which is param.data, leading to the redundant memory usage.
        # This sometimes causes OOM errors during model loading. To avoid this,
        # we sync the param tensor after its weight loader is called.
        # TODO(woosuk): Remove this hack once we have a better solution.
        fromvllm.platformsimport current_platform

        if current_platform.use_sync_weight_loader() and key == "weight_loader":
            value = current_platform.make_synced_weight_loader(value)
        setattr(weight, key, value)
```