---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/utils/
source: sitemap
fetched_at: 2026-05-07T21:28:53.013065299-03:00
rendered_js: false
word_count: 133
summary: This document provides utility functions and classes for managing model architecture selection, parameter mapping for weight loading, and model initialization within the vLLM framework.
tags:
    - model-loading
    - parameter-mapping
    - quantization
    - vllm-architecture
    - model-initialization
category: reference
---

## vllm.model\_executor.model\_loader.utils [¶](#vllm.model_executor.model_loader.utils "Permanent link")

Utilities for selecting and loading models.

## \_MODEL\_ARCH\_BY\_HASH `module-attribute` [¶](#vllm.model_executor.model_loader.utils._MODEL_ARCH_BY_HASH "Permanent link")

Caches the outputs of `_get_model_architecture`.

## ParamMapping `dataclass` [¶](#vllm.model_executor.model_loader.utils.ParamMapping "Permanent link")

A class to handle parameter mapping for model weight loading. It creates a bidirectional mapping between packed parameters and their constituent parts.

Source code in `vllm/model_executor/model_loader/utils.py`

```
@dataclass
classParamMapping:
"""
    A class to handle parameter mapping for model weight loading.
    It creates a bidirectional mapping between packed parameters and their
    constituent parts.
    """

    packed_mapping: dict[str, list[str]]
    inverse_packed_mapping: dict[str, tuple[str, int]] = field(default_factory=dict)

    def__post_init__(self):
        for packed_name, sub_params in self.packed_mapping.items():
            # Skip self-contained cases (e.g., {"W_pack": ["W_pack"]})
            if len(sub_params) == 1 and sub_params[0] == packed_name:
                continue
            for index, param_name in enumerate(sub_params):
                self.inverse_packed_mapping[param_name] = (
                    packed_name,
                    index,
                )

    defget_sub_modules(self, module_name: str) -> tuple[str, list[str]] | None:
        for key, value in self.packed_mapping.items():
            if module_name.endswith(key):
                return key, value
        return None
```

## configure\_quant\_config [¶](#vllm.model_executor.model_loader.utils.configure_quant_config "Permanent link")

Pass packed\_modules\_mapping by reference to quant\_config so that quant\_config can properly match fused modules

Note that model attributes are passed by reference to quant\_config, enabling them to be updated by model\_class.**new** (ex. chatglm, qwen)

Once the `SupportsQuant` mixin has been added to all models, this function can be removed

Source code in `vllm/model_executor/model_loader/utils.py`

```
defconfigure_quant_config(
    quant_config: QuantizationConfig, model_class: type[nn.Module]
):
"""
    Pass packed_modules_mapping by reference to quant_config so that
    quant_config can properly match fused modules

    Note that model attributes are passed by reference to quant_config,
    enabling them to be updated by model_class.__new__ (ex. chatglm, qwen)

    Once the `SupportsQuant` mixin has been added to all models, this
    function can be removed
    """
    if not issubclass(model_class, SupportsQuant):
        hf_to_vllm_mapper = getattr(model_class, "hf_to_vllm_mapper", None)
        packed_mapping = getattr(model_class, "packed_modules_mapping", None)

        # pass mappings by reference to quant_config
        if hf_to_vllm_mapper is not None:
            quant_config.apply_vllm_mapper(hf_to_vllm_mapper)
        if packed_mapping is not None:
            quant_config.packed_modules_mapping = packed_mapping
```

## initialize\_model [¶](#vllm.model_executor.model_loader.utils.initialize_model "Permanent link")

Initialize a model with the given configurations.

Source code in `vllm/model_executor/model_loader/utils.py`

```
@instrument(span_name="Initialize model")
definitialize_model(
    vllm_config: VllmConfig,
    *,
    prefix: str = "",
    model_class: type[nn.Module] | None = None,
    model_config: ModelConfig | None = None,
) -> nn.Module:
"""Initialize a model with the given configurations."""
    if model_config is None:
        model_config = vllm_config.model_config
    if model_class is None:
        model_class, _ = get_model_architecture(model_config)

    if vllm_config.quant_config is not None:
        configure_quant_config(vllm_config.quant_config, model_class)

    signatures = inspect.signature(model_class.__init__)
    all_params = [param.name for param in signatures.parameters.values()]
    if "vllm_config" in all_params and "prefix" in all_params:
        # new-style model class
        with set_current_vllm_config(vllm_config, check_compile=True, prefix=prefix):
            model = model_class(vllm_config=vllm_config, prefix=prefix)
            record_metadata_for_reloading(model)
            return model

    msg = (
        "vLLM model class should accept `vllm_config` and `prefix` as "
        "input arguments. Possibly you have an old-style model class"
        " registered from out of tree and it is used for new vLLM version. "
        "Check https://docs.vllm.ai/en/latest/design/arch_overview.html "
        "for the design and update the model class accordingly."
    )
    warnings.warn(msg, DeprecationWarning, stacklevel=2)

    logger.warning(
        "Trying to guess the arguments for old-style model class %s",
        model_class,
    )
    # try to be compatible with old-style model class
    kwargs: dict[str, Any] = {}
    if "prefix" in all_params:
        kwargs["prefix"] = prefix
    if "config" in all_params:
        kwargs["config"] = model_config.hf_config
    if "cache_config" in all_params:
        kwargs["cache_config"] = vllm_config.cache_config
    if "quant_config" in all_params:
        kwargs["quant_config"] = vllm_config.quant_config
    if "lora_config" in all_params:
        kwargs["lora_config"] = vllm_config.lora_config
    if "scheduler_config" in all_params:
        kwargs["scheduler_config"] = vllm_config.scheduler_config
    with set_current_vllm_config(vllm_config, check_compile=True, prefix=prefix):
        model = model_class(**kwargs)
        record_metadata_for_reloading(model)

    return model
```