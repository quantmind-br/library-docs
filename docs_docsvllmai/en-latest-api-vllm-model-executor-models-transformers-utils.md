---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/transformers/utils/
source: sitemap
fetched_at: 2026-05-07T21:33:39.923339753-03:00
rendered_js: false
word_count: 299
summary: This document provides reference documentation for internal vLLM utility functions designed to adapt and optimize Hugging Face Transformers model layers for the vLLM engine.
tags:
    - vllm
    - model-optimization
    - transformers
    - layer-replacement
    - tensor-parallelism
    - python-utilities
category: reference
---

Transformers modeling backend utilities.

## can\_enable\_torch\_compile [¶](#vllm.model_executor.models.transformers.utils.can_enable_torch_compile "Permanent link")

Callable to be passed to `@support_torch_compile`'s `enable_if` argument.

Defaults to `True` but is disabled in the following situations:

- The model uses dynamic rope scaling.

Source code in `vllm/model_executor/models/transformers/utils.py`

```
defcan_enable_torch_compile(vllm_config: "VllmConfig") -> bool:
"""
    Callable to be passed to `@support_torch_compile`'s `enable_if` argument.

    Defaults to `True` but is disabled in the following situations:

    - The model uses dynamic rope scaling.
    """
    text_config = vllm_config.model_config.hf_config.get_text_config()
    # Dynamic rope scaling is not compatible with torch.compile
    rope_parameters: dict | None = getattr(text_config, "rope_parameters", None) or {}
    if rope_parameters:
        # Nest rope_parameters if not nested already to simplify logic
        if not is_rope_parameters_nested(rope_parameters):
            rope_parameters = {"": rope_parameters}
        return all(rp["rope_type"] != "dynamic" for rp in rope_parameters.values())
    return True
```

## init\_on\_device\_without\_buffers [¶](#vllm.model_executor.models.transformers.utils.init_on_device_without_buffers "Permanent link")

```
init_on_device_without_buffers(device: device)
```

A context manager under which models are initialized with all parameters on the specified device. However buffers are not initialized on specified device.

Parameters:

Name Type Description Default `device` `` `torch.device` ``

Device to initialize all parameters on.

*required*

Source code in `vllm/model_executor/models/transformers/utils.py`

```
@contextmanager
definit_on_device_without_buffers(device: torch.device):
"""
    A context manager under which models are initialized with all
    parameters on the specified device. However buffers are not
    initialized on specified device.

    Args:
        device (`torch.device`):
            Device to initialize all parameters on.
    """

    old_register_parameter = nn.Module.register_parameter

    defregister_empty_parameter(module, name, param):
        old_register_parameter(module, name, param)
        if param is not None:
            param_cls = type(module._parameters[name])
            kwargs = module._parameters[name].__dict__
            kwargs["requires_grad"] = param.requires_grad
            module._parameters[name] = param_cls(
                module._parameters[name].to(device), **kwargs
            )

    tensor_constructors_to_patch = {}

    defpatch_tensor_constructor(fn):
        defwrapper(*args, **kwargs):
            kwargs["device"] = device
            return fn(*args, **kwargs)

        return wrapper

    try:
        nn.Module.register_parameter = register_empty_parameter
        for torch_function_name in tensor_constructors_to_patch:
            setattr(
                torch,
                torch_function_name,
                patch_tensor_constructor(getattr(torch, torch_function_name)),
            )
        yield
    finally:
        nn.Module.register_parameter = old_register_parameter
        for (
            torch_function_name,
            old_torch_function,
        ) in tensor_constructors_to_patch.items():
            setattr(torch, torch_function_name, old_torch_function)
```

## replace\_conv\_class [¶](#vllm.model_executor.models.transformers.utils.replace_conv_class "Permanent link")

```
replace_conv_class(conv: TorchConv) -> VllmConv | TorchConv
```

Replace a Transformers Conv2d/Conv3d with vLLM's Conv2d/Conv3d.

Parameters:

Name Type Description Default `conv` `TorchConv`

`nn.Conv2d` or `nn.Conv3d` to be replaced.

*required*

Returns: The new `Conv2dLayer` or `Conv3dLayer`. If the conv module is not supported, returns the original conv module.

Source code in `vllm/model_executor/models/transformers/utils.py`

```
defreplace_conv_class(conv: TorchConv) -> VllmConv | TorchConv:
"""Replace a Transformers Conv2d/Conv3d with vLLM's Conv2d/Conv3d.

    Args:
        conv: `nn.Conv2d` or `nn.Conv3d` to be replaced.
    Returns:
        The new `Conv2dLayer` or `Conv3dLayer`. If the conv module is not supported,
        returns the original conv module.
    """
    # vLLM does not handle non-zero padding modes
    if conv.padding_mode != "zeros":
        return conv

    vllm_conv_cls = {
        nn.Conv2d: Conv2dLayer,
        nn.Conv3d: Conv3dLayer,
    }.get(type(conv))

    if vllm_conv_cls is None:
        return conv

    return vllm_conv_cls(
        in_channels=conv.in_channels,
        out_channels=conv.out_channels,
        kernel_size=conv.kernel_size,
        stride=conv.stride,
        padding=conv.padding,
        dilation=conv.dilation,
        groups=conv.groups,
        bias=conv.bias is not None,
        padding_mode=conv.padding_mode,
        params_dtype=conv.weight.dtype,
    )
```

## replace\_linear\_class [¶](#vllm.model_executor.models.transformers.utils.replace_linear_class "Permanent link")

Replace nn.Linear with one of vLLM's tensor parallel linear classes.

Parameters:

Name Type Description Default `linear` `Linear`

`nn.Linear` to be replaced.

*required* `style` `Style`

Tensor parallel style of the new linear, e.g. "colwise".

`'replicate'` `quant_config` `QuantizationConfig | None`

Quantization config for the new linear.

`None`

Returns: The new linear.

Source code in `vllm/model_executor/models/transformers/utils.py`

```
defreplace_linear_class(
    linear: nn.Linear,
    style: Style = "replicate",
    quant_config: "QuantizationConfig | None" = None,
    *,
    prefix: str = "",
) -> ColumnParallelLinear | RowParallelLinear | ReplicatedLinear:
"""
    Replace nn.Linear with one of vLLM's tensor parallel linear classes.

    Args:
        linear: `nn.Linear` to be replaced.
        style: Tensor parallel style of the new linear, e.g. "colwise".
        quant_config: Quantization config for the new linear.
    Returns:
        The new linear.
    """

    if not isinstance(style, str):
        raise ValueError(f"Unsupported parallel style type {type(style)}, expected str")

    vllm_linear_cls, vllm_linear_kwargs = {
        "colwise": (ColumnParallelLinear, {}),
        "rowwise": (RowParallelLinear, {}),
        "replicate": (ReplicatedLinear, {}),
        # Transformers v5
        "colwise_gather_output": (ColumnParallelLinear, {"gather_output": True}),
        "rowwise_split_input": (RowParallelLinear, {"input_is_parallel": False}),
        # Transformers v4
        "colwise_rep": (ColumnParallelLinear, {"gather_output": True}),
        "rowwise_rep": (RowParallelLinear, {"input_is_parallel": False}),
    }.get(style, (ReplicatedLinear, {}))

    return vllm_linear_cls(
        input_size=linear.in_features,
        output_size=linear.out_features,
        bias=linear.bias is not None,
        quant_config=quant_config,
        prefix=prefix,
        return_bias=False,
        **vllm_linear_kwargs,
    )
```

## replace\_rms\_norm\_class [¶](#vllm.model_executor.models.transformers.utils.replace_rms_norm_class "Permanent link")

Replace a Transformers RMSNorm with vLLM's RMSNorm.

This method assumes: - Weight is stored as `weight`. - Epsilon is stored as `eps` or `variance_epsilon`. - `with_scale` indicates whether the layer has a weight (Gemma3n only). - `var_hidden_size` is only ever used for Intern vision encoder in vLLM and Transformers doesn't appear to have the same concept.

Source code in `vllm/model_executor/models/transformers/utils.py`

```
defreplace_rms_norm_class(rms_norm: nn.Module, hidden_size: int) -> RMSNorm:
"""Replace a Transformers RMSNorm with vLLM's RMSNorm.

    This method assumes:
    - Weight is stored as `weight`.
    - Epsilon is stored as `eps` or `variance_epsilon`.
    - `with_scale` indicates whether the layer has a weight (Gemma3n only).
    - `var_hidden_size` is only ever used for Intern vision encoder in vLLM
    and Transformers doesn't appear to have the same concept.
    """
    eps = getattr_iter(rms_norm, ("eps", "variance_epsilon"), 1e-6)
    kwargs = {"hidden_size": hidden_size, "eps": eps}
    # Update hidden size if weight is available
    weight_meta = getattr(rms_norm, "weight", None)
    if weight_meta is not None:
        kwargs["hidden_size"] = weight_meta.size(0)
    # Check if weight is all zeros, which indicates GemmaRMSNorm
    # We must create a new instance because rms_norm is on meta
    try:
        with torch.device("cpu"):
            weight_test = getattr(rms_norm.__class__(1), "weight", None)
    except Exception:
        logger.warning(
            "Failed to determine if RMSNorm weight is centered on zero or one. "
            "Defaulting to one."
        )
        weight_test = None
    if weight_test is not None and torch.all(weight_test == 0):
        return GemmaRMSNorm(**kwargs)
    # Otherwise assume it's a regular RMSNorm
    kwargs["has_weight"] = getattr(rms_norm, "with_scale", True)
    if weight_meta is not None:
        kwargs["dtype"] = weight_meta.dtype
    else:
        # No weight, fall back to weightless RMSNorm
        kwargs["has_weight"] = False
    return RMSNorm(**kwargs)
```