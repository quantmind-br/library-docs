---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/lora/layers/utils/
source: sitemap
fetched_at: 2026-05-07T21:22:39.13036618-03:00
rendered_js: false
word_count: 58
summary: This document provides a technical reference for utility functions and decorators used to manage LoRA layer replacement and device placement in the vLLM library.
tags:
    - vllm
    - lora
    - model-sharding
    - python-decorators
    - tensor-device-management
    - deep-learning-infrastructure
category: reference
---

## vllm.lora.layers.utils [¶](#vllm.lora.layers.utils "Permanent link")

## \_fully\_sharded\_can\_replace [¶](#vllm.lora.layers.utils._fully_sharded_can_replace "Permanent link")

```
_fully_sharded_can_replace(can_replace)
```

decorator which adds the condition of fully sharded loras intended to wrap can\_replace\_layer()

Source code in `vllm/lora/layers/utils.py`

```
def_fully_sharded_can_replace(can_replace):
"""
    decorator which adds the condition of fully sharded loras
    intended to wrap can_replace_layer()
    """

    defdec(*args, **kwargs):
        return (
            can_replace(*args, **kwargs) and kwargs["lora_config"].fully_sharded_loras
        )

    return dec
```

## \_get\_lora\_device [¶](#vllm.lora.layers.utils._get_lora_device "Permanent link")

Returns the device for where to place the LoRA tensors.

Source code in `vllm/lora/layers/utils.py`

```
def_get_lora_device(base_layer: nn.Module) -> torch.device:
    # code borrowed from https://github.com/fmmoret/vllm/blob/fm-support-lora-on-quantized-models/vllm/lora/layers.py#L34
"""Returns the device for where to place the LoRA tensors."""
    # unquantizedLinear
    if hasattr(base_layer, "weight"):
        return base_layer.weight.device
    # Compressed Tensor
    elif hasattr(base_layer, "weight_packed"):
        return base_layer.weight_packed.device
    # GPTQ/AWQ
    elif hasattr(base_layer, "qweight"):
        return base_layer.qweight.device
    # MoE layer
    elif hasattr(base_layer, "w2_weight"):
        return base_layer.w2_weight.device
    # MoE Compressed Tensor
    elif hasattr(base_layer, "w2_weight_packed"):
        return base_layer.w2_weight_packed.device
    # MoE GPTQ/AWQ/GGUF
    elif hasattr(base_layer, "w2_qweight"):
        return base_layer.w2_qweight.device
    else:
        raise ValueError(f"Unsupported base layer: {base_layer}")
```

## \_not\_fully\_sharded\_can\_replace [¶](#vllm.lora.layers.utils._not_fully_sharded_can_replace "Permanent link")

```
_not_fully_sharded_can_replace(can_replace)
```

decorator which adds the condition of not using fully sharded loras intended to wrap can\_replace\_layer()

Source code in `vllm/lora/layers/utils.py`

```
def_not_fully_sharded_can_replace(can_replace):
"""
    decorator which adds the condition of not using fully sharded loras
    intended to wrap can_replace_layer()
    """

    defdec(*args, **kwargs):
        decorate = kwargs.pop("decorate") if "decorate" in kwargs else True
        condition = not kwargs["lora_config"].fully_sharded_loras if decorate else True
        return can_replace(*args, **kwargs) and condition

    return dec
```