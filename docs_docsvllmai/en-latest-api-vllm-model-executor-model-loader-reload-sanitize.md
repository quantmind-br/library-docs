---
title: sanitize - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/reload/sanitize/
source: sitemap
fetched_at: 2026-05-07T21:28:44.858105944-03:00
rendered_js: false
word_count: 88
summary: This document describes a utility function that removes circular references between tensor attributes and model layers to facilitate proper garbage collection and memory management.
tags:
    - memory-management
    - garbage-collection
    - pytorch
    - tensor-manipulation
    - circular-reference
category: reference
---

Removes references to layer held by tensor attributes. Specifically, removes the `__self__` attribute of weight loader methods attached to the tensor.

Used by `capture_layer_to_meta` to avoid circular references to layers in `LAYERWISE_INFO`, leading to modules never being cleaned up. Without sanitation, tensors will reference layers, and the WeakKeyDictionary will never evict entries, even when the model is deleted.

:param tensor: tensor to be sanitized :param layer: layer whose references should be removed :return: sanitized tensor

Source code in `vllm/model_executor/model_loader/reload/sanitize.py`

```
defsanitize_layer_refs(tensor: torch.Tensor, layer: torch.nn.Module) -> torch.Tensor:
"""
    Removes references to layer held by tensor attributes. Specifically, removes the
    `__self__` attribute of weight loader methods attached to the tensor.

    Used by `capture_layer_to_meta` to avoid circular references to layers in
    `LAYERWISE_INFO`, leading to modules never being cleaned up. Without sanitation,
    tensors will reference layers, and the WeakKeyDictionary will never evict entries,
    even when the model is deleted.

    :param tensor: tensor to be sanitized
    :param layer: layer whose references should be removed
    :return: sanitized tensor
    """
    for key, value in tensor.__dict__.items():
        if isinstance(value, MethodType) and value.__self__ is layer:
            tensor.__dict__[key] = value.__func__.__get__(layer_ref_sentinel)

    return tensor
```