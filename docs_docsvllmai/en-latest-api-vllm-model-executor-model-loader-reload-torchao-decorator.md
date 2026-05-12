---
title: torchao_decorator - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/reload/torchao_decorator/
source: sitemap
fetched_at: 2026-05-07T21:28:45.826746062-03:00
rendered_js: false
word_count: 65
summary: This document describes a decorator function designed to enable the reloading of high-precision weights into already quantized torchao models by performing online quantization during the weight loading process.
tags:
    - model-loading
    - torchao
    - weight-quantization
    - python-decorators
    - model-executor
    - vllm-architecture
category: concept
---

Decorator for `load_weights` method for AutoWeightsLoader.load\_weights to support reloading high precision (bfloat16/float16/float32) weight for an already quantized model, this involves restoring the weights to a high precision weights and then online quantize the weights.

Only applies to torchao quantized models. Assumes that all model weights are loaded within a single weights iterator (cannot perform batched updates)

Source code in `vllm/model_executor/model_loader/reload/torchao_decorator.py`

```
defsupport_quantized_model_reload_from_hp_weights(original_load_weights: FunctionType):
"""
    Decorator for `load_weights` method for AutoWeightsLoader.load_weights to support
    reloading high precision (bfloat16/float16/float32) weight for an already quantized
    model, this involves restoring the weights to a high precision weights and
    then online quantize the weights.

    Only applies to torchao quantized models. Assumes that all model weights are
    loaded within a single weights iterator (cannot perform batched updates)
    """

    @wraps(original_load_weights)
    defpatched_model_load_weights(
        self: "AutoWeightsLoader",
        weights: Iterable[tuple[str, torch.Tensor]],
        *args,
        **kwargs,
    ):
        model = self.module

        if not getattr(model, "_do_torchao_reload", False):
            return original_load_weights(self, weights, *args, **kwargs)

        initialize_layerwise_reload(model)
        loaded_weights = original_load_weights(self, weights, *args, **kwargs)
        finalize_layerwise_reload(model, model._model_config)

        return loaded_weights

    return patched_model_load_weights
```