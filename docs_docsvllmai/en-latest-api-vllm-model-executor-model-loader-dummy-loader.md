---
title: dummy_loader - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/dummy_loader/
source: sitemap
fetched_at: 2026-05-07T21:28:39.023376148-03:00
rendered_js: false
word_count: 32
summary: This document describes the DummyModelLoader class, which is used for performance testing by initializing model weights with random values instead of loading pretrained weights.
tags:
    - vllm
    - model-loading
    - performance-testing
    - random-initialization
    - model-executor
category: reference
---

## DummyModelLoader [¶](#vllm.model_executor.model_loader.dummy_loader.DummyModelLoader "Permanent link")

Bases: `BaseModelLoader`

Model loader that will set model weights to random values.

Source code in `vllm/model_executor/model_loader/dummy_loader.py`

```
classDummyModelLoader(BaseModelLoader):
"""Model loader that will set model weights to random values."""

    def__init__(self, load_config: LoadConfig):
        super().__init__(load_config)
        if load_config.model_loader_extra_config:
            raise ValueError(
                f"Model loader extra config is not supported for "
                f"load format {load_config.load_format}"
            )

    defdownload_model(self, model_config: ModelConfig) -> None:
        pass  # Nothing to download

    defload_weights(self, model: nn.Module, model_config: ModelConfig) -> None:
        for layer in model.modules():
            info = get_layerwise_info(layer)
            if info.can_load():
                self._process_online_quant_layer(layer, info)
            else:
                # NOTE(woosuk): For accurate performance evaluation, we assign
                # random values to the weights.
                initialize_dummy_weights(layer, model_config)

    def_process_online_quant_layer(
        self,
        layer: nn.Module,
        info: LayerReloadingInfo,
    ) -> None:
"""Materialize, apply dummy weights, and run quantization processing."""
        materialize_layer(layer, info)

        for tensor in get_layer_tensors(layer).values():
            initialize_single_dummy_weight(tensor)

        for param in get_layer_tensors(layer).values():
            param.weight_loader = _get_original_loader(param)

        quant_method = getattr(layer, "quant_method", None)
        if isinstance(quant_method, QuantizeMethodBase):
            quant_method.process_weights_after_loading(layer)

        info.reset()
```

### \_process\_online\_quant\_layer [¶](#vllm.model_executor.model_loader.dummy_loader.DummyModelLoader._process_online_quant_layer "Permanent link")

```
_process_online_quant_layer(
    layer: Module, info: LayerReloadingInfo
) -> None
```

Materialize, apply dummy weights, and run quantization processing.

Source code in `vllm/model_executor/model_loader/dummy_loader.py`

```
def_process_online_quant_layer(
    self,
    layer: nn.Module,
    info: LayerReloadingInfo,
) -> None:
"""Materialize, apply dummy weights, and run quantization processing."""
    materialize_layer(layer, info)

    for tensor in get_layer_tensors(layer).values():
        initialize_single_dummy_weight(tensor)

    for param in get_layer_tensors(layer).values():
        param.weight_loader = _get_original_loader(param)

    quant_method = getattr(layer, "quant_method", None)
    if isinstance(quant_method, QuantizeMethodBase):
        quant_method.process_weights_after_loading(layer)

    info.reset()
```