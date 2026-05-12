---
title: reload - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/reload/
source: sitemap
fetched_at: 2026-05-07T21:28:41.774785086-03:00
rendered_js: false
word_count: 400
summary: This module provides utilities for performing layerwise weight reloading in vLLM models, allowing for efficient weight updates without requiring full model reconstruction.
tags:
    - vllm
    - model-loading
    - weight-reloading
    - layerwise-processing
    - quantization
    - pytorch
category: reference
---

## vllm.model\_executor.model\_loader.reload [¶](#vllm.model_executor.model_loader.reload "Permanent link")

Layerwise weight reloading utilities for vLLM.

This module provides functionality to reload model weights layer-by-layer, which is useful for weight updates without full model reconstruction.

Limitations: 1. Composition with CPU offloading has not been implemented 2. Tied parameters will only reflect processing from one of the parent layers (for example, only processing from embed\_tokens will have an effect) 3. This design assumes that the number of weights loaded from disk is the same as the number of weights created at model init time. This is not true for quant methods which (1) pad weights or (2) load qkv weights into the same parameter. Both of these cases are non-issues for today's quant methods, but future quantizations may cause reloading to fail

Modules:

Name Description `layerwise` `meta` `sanitize` `torchao_decorator` `utils`

## finalize\_layerwise\_processing [¶](#vllm.model_executor.model_loader.reload.finalize_layerwise_processing "Permanent link")

Apply processing to any layers which were not layerwise processed during loading. This includes attention layers and layers which have weight elements which are not loaded (due to padding).

This function should be applied after `initialize_layerwise_reload` is applied unwrap the layerwise weight loaders.

:param model: model to finalize processing for :param model\_config: config needed for applying processing to attention layers

Source code in `vllm/model_executor/model_loader/reload/layerwise.py`

```
deffinalize_layerwise_processing(model: torch.nn.Module, model_config: ModelConfig):
"""
    Apply processing to any layers which were not layerwise processed during loading.
    This includes attention layers and layers which have weight elements which are not
    loaded (due to padding).

    This function should be applied after `initialize_layerwise_reload` is applied
    unwrap the layerwise weight loaders.

    :param model: model to finalize processing for
    :param model_config: config needed for applying processing to attention layers
    """
    if hasattr(model, "_original_do_torchao_reload"):
        model._do_torchao_reload = model._original_do_torchao_reload

    deferred_attn: list[tuple[torch.nn.Module, LayerReloadingInfo]] = []

    for layer in model.modules():
        info = get_layerwise_info(layer)
        if not info.can_load():
            info.reset()
            continue

        # Attention/MLA layers are processed after all other layers
        if isinstance(layer, (Attention, MLAAttention)):
            deferred_attn.append((layer, info))
            continue

        # No weights were loaded
        if info.load_numel <= 0:
            # first load: checkpoint did not contain weights for this layer
            if info.kernel_tensors is None:
                _layerwise_process(layer, info)
                continue

            # reloading: place kernel tensors back as a fallback
            elif info.load_numel_total > 0:  # type: ignore[operator]
                logger.warning("%s: Failed to load weights", layer.__class__.__name__)
                _place_kernel_tensors(layer, info)

        # Process non-attention layers which did not load all elements. This can happen
        # if the created weight has extra padding elements which are not loaded
        # Having too many of these delayed layers can lead to excess memory usage
        # see Limitations(4)
        elif info.load_numel > 0 and info.load_numel < info.load_numel_total:  # type: ignore[operator]
            logger.debug("%s: Delayed processing", layer.__class__.__name__)
            _layerwise_process(layer, info)

        info.reset()

    # Process attention layers after all other layers are done
    for layer, info in deferred_attn:
        _finalize_attention_layer(layer, info, model_config)
        info.reset()

    LOADING_LAYERS.clear()
```

## initialize\_layerwise\_reload [¶](#vllm.model_executor.model_loader.reload.initialize_layerwise_reload "Permanent link")

```
initialize_layerwise_reload(model: Module)
```

Set up layerwise weight loading with deferred processing.

Must be called after `record_metadata_for_reloading`. This function: 1. Saves current kernel tensors for later copying 2. Restores layer parameters/buffers from metadata (on meta device) 3. Wraps weight loaders to defer processing until all weights are loaded

When all weights for a layer are loaded, the wrapped loaders will: 1. Materialize the layer onto the target device 2. Load all cached weights 3. Run quantization processing if applicable 4. Copy processed values back to original tensor storage

Source code in `vllm/model_executor/model_loader/reload/layerwise.py`

```
@torch.no_grad()
definitialize_layerwise_reload(model: torch.nn.Module):
"""
    Set up layerwise weight loading with deferred processing.

    Must be called after `record_metadata_for_reloading`. This function:
    1. Saves current kernel tensors for later copying
    2. Restores layer parameters/buffers from metadata (on meta device)
    3. Wraps weight loaders to defer processing until all weights are loaded

    When all weights for a layer are loaded, the wrapped loaders will:
    1. Materialize the layer onto the target device
    2. Load all cached weights
    3. Run quantization processing if applicable
    4. Copy processed values back to original tensor storage
    """
    # disable torchao reloading to avoid infinite recursion
    model._original_do_torchao_reload = getattr(model, "_do_torchao_reload", False)
    model._do_torchao_reload = False

    for layer in model.modules():
        info = get_layerwise_info(layer)

        # Skip if the layer has already been initialized
        if info.can_load():
            continue

        # Save current tensors for later copying
        info.kernel_tensors = get_layer_params_buffers(layer)

        # Restore layer parameters/buffers onto meta device
        restore_layer_on_meta(layer, info)

        # Wrap weight loaders to buffer loading
        initialize_online_processing(layer)

record_metadata_for_reloading(model: Module)
```

Record layer metadata needed for later reloading.

Stores parameter and buffer metadata as meta tensors for restoration. Must be called before `initialize_layerwise_reload`.

Source code in `vllm/model_executor/model_loader/reload/layerwise.py`

```
defrecord_metadata_for_reloading(model: torch.nn.Module):
"""
    Record layer metadata needed for later reloading.

    Stores parameter and buffer metadata as meta tensors for restoration.
    Must be called before `initialize_layerwise_reload`.
    """
    for layer in model.modules():
        info = get_layerwise_info(layer)
        info.restore_metadata = capture_layer_to_meta(layer)
        info.restore_device = torch.get_default_device()
```

## support\_quantized\_model\_reload\_from\_hp\_weights [¶](#vllm.model_executor.model_loader.reload.support_quantized_model_reload_from_hp_weights "Permanent link")

```
support_quantized_model_reload_from_hp_weights(
    original_load_weights: FunctionType,
)
```

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