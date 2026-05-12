---
title: base_config - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/base_config/
source: sitemap
fetched_at: 2026-05-07T21:26:34.150526444-03:00
rendered_js: false
word_count: 432
summary: This document defines the base class for quantization configurations in vLLM, establishing the interface and required methods for implementing model-specific quantization strategies.
tags:
    - vllm
    - quantization
    - model-config
    - base-class
    - abstract-method
    - deep-learning
    - cuda
category: reference
---

Bases: `ABC`

Base class for quantization configs.

Source code in `vllm/model_executor/layers/quantization/base_config.py`

```
classQuantizationConfig(ABC):
"""Base class for quantization configs."""

    def__init__(self):
        super().__init__()
        # mapping is updated by models as they initialize
        self.packed_modules_mapping: dict[str, list[str]] = dict()

    @abstractmethod
    defget_name(self) -> QuantizationMethods:
"""Name of the quantization method."""
        raise NotImplementedError

    @abstractmethod
    defget_supported_act_dtypes(self) -> list[torch.dtype]:
"""List of supported activation dtypes."""
        raise NotImplementedError

    @classmethod
    @abstractmethod
    defget_min_capability(cls) -> int:
"""Minimum GPU capability to support the quantization method.

        E.g., 70 for Volta, 75 for Turing, 80 for Ampere.
        This requirement is due to the custom CUDA kernels used by the
        quantization method.
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    defget_config_filenames() -> list[str]:
"""List of filenames to search for in the model directory."""
        raise NotImplementedError

    @classmethod
    @abstractmethod
    deffrom_config(cls, config: dict[str, Any]) -> "QuantizationConfig":
"""Create a config class from the model's quantization config."""
        raise NotImplementedError

    @classmethod
    defoverride_quantization_method(
        cls,
        hf_quant_cfg: dict[str, Any],
        user_quant: str | None,
        hf_config: Any = None,
    ) -> QuantizationMethods | None:
"""
        Detects if this quantization method can support a given checkpoint
        format by overriding the user specified quantization method --
        this method should only be overwritten by subclasses in exceptional
        circumstances.

        Args:
            hf_quant_cfg: The checkpoint's quantization config dict.
            user_quant: The user-specified quantization method string.
            hf_config: The HuggingFace model config object (e.g. for
                model_type checks). May be None if not available.
        """
        return None

    @staticmethod
    defget_from_keys(config: dict[str, Any], keys: list[str]) -> Any:
"""Get a value from the model's quantization config."""
        for key in keys:
            if key in config:
                return config[key]
        raise ValueError(
            f"Cannot find any of {keys} in the model's quantization config."
        )

    @staticmethod
    defget_from_keys_or(config: dict[str, Any], keys: list[str], default: Any) -> Any:
"""Get an optional value from the model's quantization config."""
        try:
            return QuantizationConfig.get_from_keys(config, keys)
        except ValueError:
            return default

    @abstractmethod
    defget_quant_method(
        self, layer: torch.nn.Module, prefix: str
    ) -> QuantizeMethodBase | None:
"""Get the quantize method to use for the quantized layer.

        Args:
            layer: The layer for the quant method.
            prefix: The full name of the layer in the state dict
        Returns:
            The quantize method. None if the given layer doesn't support quant
            method.
        """
        raise NotImplementedError

    defget_cache_scale(self, name: str) -> str | None:
        return None

    defapply_vllm_mapper(  # noqa: B027
        self, hf_to_vllm_mapper: "WeightsMapper"
    ):
"""
        Interface for models to update module names referenced in
        quantization configs in order to reflect the vllm model structure

        :param hf_to_vllm_mapper: maps from hf model structure (the assumed
            structure of the qconfig) to vllm model structure
        """
        # TODO (@kylesayrs): add implementations for all subclasses
        pass

    defmaybe_update_config(  # noqa: B027
        self,
        model_name: str,
        hf_config: PretrainedConfig | None = None,
        revision: str | None = None,
    ):
"""
        Interface to update values after config initialization.

        Args:
            model_name: The name of the model
            hf_config: The Hugging Face config of the model
            revision: The revision of the model
        Returns:
        """
        # TODO: revision is never passed currently in vllm.py,
        # but is used in subclasses, should we remove this parameter?
        pass

    defis_mxfp4_quant(self, prefix: str, layer: torch.nn.Module) -> bool:
"""
        Determine if mxfp4 quantization will be used for this config.

        This allows hidden_size rounding to happen before moe_config creation
        without needing to instantiate quant_method first.

        Args:
            prefix: The layer prefix/name in the model
            layer: The layer module

        Returns:
            True if this config uses MXFP4 quantization, False otherwise
        """
        return False
```

### apply\_vllm\_mapper [¶](#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.apply_vllm_mapper "Permanent link")

Interface for models to update module names referenced in quantization configs in order to reflect the vllm model structure

:param hf\_to\_vllm\_mapper: maps from hf model structure (the assumed structure of the qconfig) to vllm model structure

Source code in `vllm/model_executor/layers/quantization/base_config.py`

```
defapply_vllm_mapper(  # noqa: B027
    self, hf_to_vllm_mapper: "WeightsMapper"
):
"""
    Interface for models to update module names referenced in
    quantization configs in order to reflect the vllm model structure

    :param hf_to_vllm_mapper: maps from hf model structure (the assumed
        structure of the qconfig) to vllm model structure
    """
    # TODO (@kylesayrs): add implementations for all subclasses
    pass
```

### from\_config `abstractmethod` `classmethod` [¶](#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.from_config "Permanent link")

Create a config class from the model's quantization config.

Source code in `vllm/model_executor/layers/quantization/base_config.py`

```
@classmethod
@abstractmethod
deffrom_config(cls, config: dict[str, Any]) -> "QuantizationConfig":
"""Create a config class from the model's quantization config."""
    raise NotImplementedError
```

### get\_config\_filenames `abstractmethod` `staticmethod` [¶](#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_config_filenames "Permanent link")

```
get_config_filenames() -> list[str]
```

List of filenames to search for in the model directory.

Source code in `vllm/model_executor/layers/quantization/base_config.py`

```
@staticmethod
@abstractmethod
defget_config_filenames() -> list[str]:
"""List of filenames to search for in the model directory."""
    raise NotImplementedError
```

### get\_from\_keys `staticmethod` [¶](#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_from_keys "Permanent link")

Get a value from the model's quantization config.

Source code in `vllm/model_executor/layers/quantization/base_config.py`

```
@staticmethod
defget_from_keys(config: dict[str, Any], keys: list[str]) -> Any:
"""Get a value from the model's quantization config."""
    for key in keys:
        if key in config:
            return config[key]
    raise ValueError(
        f"Cannot find any of {keys} in the model's quantization config."
    )
```

### get\_from\_keys\_or `staticmethod` [¶](#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_from_keys_or "Permanent link")

Get an optional value from the model's quantization config.

Source code in `vllm/model_executor/layers/quantization/base_config.py`

```
@staticmethod
defget_from_keys_or(config: dict[str, Any], keys: list[str], default: Any) -> Any:
"""Get an optional value from the model's quantization config."""
    try:
        return QuantizationConfig.get_from_keys(config, keys)
    except ValueError:
        return default
```

### get\_min\_capability `abstractmethod` `classmethod` [¶](#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_min_capability "Permanent link")

```
get_min_capability() -> int
```

Minimum GPU capability to support the quantization method.

E.g., 70 for Volta, 75 for Turing, 80 for Ampere. This requirement is due to the custom CUDA kernels used by the quantization method.

Source code in `vllm/model_executor/layers/quantization/base_config.py`

```
@classmethod
@abstractmethod
defget_min_capability(cls) -> int:
"""Minimum GPU capability to support the quantization method.

    E.g., 70 for Volta, 75 for Turing, 80 for Ampere.
    This requirement is due to the custom CUDA kernels used by the
    quantization method.
    """
    raise NotImplementedError
```

### get\_name `abstractmethod` [¶](#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_name "Permanent link")

```
get_name() -> QuantizationMethods
```

Name of the quantization method.

Source code in `vllm/model_executor/layers/quantization/base_config.py`

```
@abstractmethod
defget_name(self) -> QuantizationMethods:
"""Name of the quantization method."""
    raise NotImplementedError
```

### get\_quant\_method `abstractmethod` [¶](#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_quant_method "Permanent link")

```
get_quant_method(
    layer: Module, prefix: str
) -> QuantizeMethodBase | None
```

Get the quantize method to use for the quantized layer.

Parameters:

Name Type Description Default `layer` `Module`

The layer for the quant method.

*required* `prefix` `str`

The full name of the layer in the state dict

*required*

Returns: The quantize method. None if the given layer doesn't support quant method.

Source code in `vllm/model_executor/layers/quantization/base_config.py`

```
@abstractmethod
defget_quant_method(
    self, layer: torch.nn.Module, prefix: str
) -> QuantizeMethodBase | None:
"""Get the quantize method to use for the quantized layer.

    Args:
        layer: The layer for the quant method.
        prefix: The full name of the layer in the state dict
    Returns:
        The quantize method. None if the given layer doesn't support quant
        method.
    """
    raise NotImplementedError
```

### get\_supported\_act\_dtypes `abstractmethod` [¶](#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.get_supported_act_dtypes "Permanent link")

List of supported activation dtypes.

Source code in `vllm/model_executor/layers/quantization/base_config.py`

```
@abstractmethod
defget_supported_act_dtypes(self) -> list[torch.dtype]:
"""List of supported activation dtypes."""
    raise NotImplementedError
```

### is\_mxfp4\_quant [¶](#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.is_mxfp4_quant "Permanent link")

Determine if mxfp4 quantization will be used for this config.

This allows hidden\_size rounding to happen before moe\_config creation without needing to instantiate quant\_method first.

Parameters:

Name Type Description Default `prefix` `str`

The layer prefix/name in the model

*required* `layer` `Module`

The layer module

*required*

Returns:

Type Description `bool`

True if this config uses MXFP4 quantization, False otherwise

Source code in `vllm/model_executor/layers/quantization/base_config.py`

```
defis_mxfp4_quant(self, prefix: str, layer: torch.nn.Module) -> bool:
"""
    Determine if mxfp4 quantization will be used for this config.

    This allows hidden_size rounding to happen before moe_config creation
    without needing to instantiate quant_method first.

    Args:
        prefix: The layer prefix/name in the model
        layer: The layer module

    Returns:
        True if this config uses MXFP4 quantization, False otherwise
    """
    return False
```

### maybe\_update\_config [¶](#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.maybe_update_config "Permanent link")

```
maybe_update_config(
    model_name: str,
    hf_config: PretrainedConfig | None = None,
    revision: str | None = None,
)
```

Interface to update values after config initialization.

Parameters:

Name Type Description Default `model_name` `str`

The name of the model

*required* `hf_config` `PretrainedConfig | None`

The Hugging Face config of the model

`None` `revision` `str | None`

The revision of the model

`None`

Returns:

Source code in `vllm/model_executor/layers/quantization/base_config.py`

```
defmaybe_update_config(  # noqa: B027
    self,
    model_name: str,
    hf_config: PretrainedConfig | None = None,
    revision: str | None = None,
):
"""
    Interface to update values after config initialization.

    Args:
        model_name: The name of the model
        hf_config: The Hugging Face config of the model
        revision: The revision of the model
    Returns:
    """
    # TODO: revision is never passed currently in vllm.py,
    # but is used in subclasses, should we remove this parameter?
    pass
```

### override\_quantization\_method `classmethod` [¶](#vllm.model_executor.layers.quantization.base_config.QuantizationConfig.override_quantization_method "Permanent link")

```
override_quantization_method(
    hf_quant_cfg: dict[str, Any],
    user_quant: str | None,
    hf_config: Any = None,
) -> QuantizationMethods | None
```

Detects if this quantization method can support a given checkpoint format by overriding the user specified quantization method -- this method should only be overwritten by subclasses in exceptional circumstances.

Parameters:

Name Type Description Default `hf_quant_cfg` `dict[str, Any]`

The checkpoint's quantization config dict.

*required* `user_quant` `str | None`

The user-specified quantization method string.

*required* `hf_config` `Any`

The HuggingFace model config object (e.g. for model\_type checks). May be None if not available.

`None`

Source code in `vllm/model_executor/layers/quantization/base_config.py`

```
@classmethod
defoverride_quantization_method(
    cls,
    hf_quant_cfg: dict[str, Any],
    user_quant: str | None,
    hf_config: Any = None,
) -> QuantizationMethods | None:
"""
    Detects if this quantization method can support a given checkpoint
    format by overriding the user specified quantization method --
    this method should only be overwritten by subclasses in exceptional
    circumstances.

    Args:
        hf_quant_cfg: The checkpoint's quantization config dict.
        user_quant: The user-specified quantization method string.
        hf_config: The HuggingFace model config object (e.g. for
            model_type checks). May be None if not available.
    """
    return None
```