---
title: torchao - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/torchao/
source: sitemap
fetched_at: 2026-05-07T21:27:44.016273165-03:00
rendered_js: false
word_count: 267
summary: The TorchAOConfig class provides a configuration structure for integrating TorchAO quantization into the vLLM model execution framework, allowing for the initialization of quantization parameters from Hugging Face configs or JSON strings.
tags:
    - vllm
    - torchao
    - quantization
    - configuration
    - deep-learning
    - model-optimization
category: api
---

## TorchAOConfig [¶](#vllm.model_executor.layers.quantization.torchao.TorchAOConfig "Permanent link")

Bases: `QuantizationConfig`

Config class for torchao.

Source code in `vllm/model_executor/layers/quantization/torchao.py`

````
classTorchAOConfig(QuantizationConfig):
"""Config class for torchao."""

    def__init__(
        self,
        torchao_config,
        skip_modules: list[str] | None = None,
        is_checkpoint_torchao_serialized: bool = False,
    ) -> None:
        super().__init__()
        self.torchao_config = torchao_config
        self.skip_modules = skip_modules or []
        self.is_checkpoint_torchao_serialized = is_checkpoint_torchao_serialized

    def__repr__(self) -> str:
        return (
            f"TorchAOConfig({self.torchao_config=}, {self.skip_modules=}, "
            f"{self.is_checkpoint_torchao_serialized=})"
        )

    defget_name(self) -> QuantizationMethods:
        return "torchao"

    defget_supported_act_dtypes(self) -> list[torch.dtype]:
        return [torch.float32, torch.float16, torch.bfloat16]

    @classmethod
    defget_min_capability(cls) -> int:
        return 75

    @staticmethod
    defget_config_filenames() -> list[str]:
"""torchao doesn't require additional config files, we use
        `config.json` from huggingface: `model_config.hf_config`
        """
        return []

    @classmethod
    deffrom_config(cls, config: dict[str, Any]) -> "TorchAOConfig":
"""Create the quant config from an hf model config"""
        try:
            fromtorchao.core.configimport config_from_dict
        except ImportError as err:
            raise ImportError(
                "Please install torchao>=0.10.0 via "
                "`pip install torchao>=0.10.0` to use torchao quantization."
            ) fromerr

        quant_method = cls.get_from_keys_or(config, ["quant_method"], None)
        is_checkpoint_torchao_serialized = (
            quant_method is not None and "torchao" in quant_method
        )

        hf_config = cls.get_from_keys_or(config, ["quant_type"], None)
        assert hf_config is not None, "quant_type must be specified"
        assert len(hf_config) == 1 and "default" in hf_config, (
            "Expected only one key 'default' in quant_type dictionary"
        )
        quant_type = hf_config["default"]
        ao_config = config_from_dict(quant_type)

        # Adds skipped modules defined in "modules_to_not_convert"
        skip_modules = config.get("modules_to_not_convert", []) or []

        # Adds skipped modules defined in "module_fqn_to_config"
        _data = quant_type.get("_data", {})
        if not isinstance(_data, dict):
            _data = {}

        module_fqn = _data.get("module_fqn_to_config", {})
        if not isinstance(module_fqn, dict):
            module_fqn = {}

        for layer, layer_cfg in module_fqn.items():
            if layer_cfg is None:
                skip_modules.append(layer)

        return cls(ao_config, skip_modules, is_checkpoint_torchao_serialized)

    @classmethod
    deffrom_config_file(cls, config_file: str) -> "TorchAOConfig":
"""Initialize class from a config file. Example:
        ```
        config = Float8DynamicActivationFloat8WeightConfig(granularity=PerRow())
        fn = "torchao_config.json"

        with open(fn, "w") as f:
            f.write(json.dumps(config_to_dict(config)))
        ```
        """
        with open(config_file) as f:
            f.seek(0)
            f_read = f.read()
            config_dict = json.loads(f_read)

        hf_config = {"quant_type": {"default": config_dict}}
        return cls.from_config(hf_config)

    @classmethod
    deffrom_config_dict_json(cls, config_dict_json: str) -> "TorchAOConfig":
"""Initialize class from a config_dict json string, got from
        torchao_config_object = some AOBaseConfig object
        json.dumps(config_to_dict(torchao_config_object))
        """
        config_dict = json.loads(config_dict_json)
        hf_config = {"quant_type": {"default": config_dict}}
        return cls.from_config(hf_config)

    defget_quant_method(
        self, layer: torch.nn.Module, prefix: str
    ) -> "QuantizeMethodBase | None":
        if not isinstance(layer, LinearBase):
            return None

        fromtorchao.quantizationimport ModuleFqnToConfig

        if should_skip(prefix, self.skip_modules):
            return UnquantizedLinearMethod()

        module_fqn = prefix
        if isinstance(self.torchao_config, ModuleFqnToConfig):
            module_fqn_to_config = self.torchao_config.module_fqn_to_config
            c = None
            if module_fqn in module_fqn_to_config:
                assert not module_fqn.startswith("re:"), (
                    "module fqn should not start with"
                    "`re:`, which is used for specifying regex"
                )
                c = module_fqn_to_config[module_fqn]
            else:
                for maybe_module_fqn_pattern in module_fqn_to_config:
                    if not maybe_module_fqn_pattern.startswith("re:"):
                        continue
                    elif re.fullmatch(maybe_module_fqn_pattern[3:], module_fqn):
                        # we'll apply the config for first fully matched pattern
                        c = module_fqn_to_config[maybe_module_fqn_pattern]
                        break
                else:
                    # fallback to use default if no module specific
                    # config is provided
                    c = module_fqn_to_config.get("_default", None)

            if c is not None:
                current_torchao_config = TorchAOConfig(
                    c, self.skip_modules, self.is_checkpoint_torchao_serialized
                )
                return TorchAOLinearMethod(current_torchao_config)
            else:
                return UnquantizedLinearMethod()

        return TorchAOLinearMethod(self)

    defget_scaled_act_names(self) -> list[str]:
        return []
````

### from\_config `classmethod` [¶](#vllm.model_executor.layers.quantization.torchao.TorchAOConfig.from_config "Permanent link")

Create the quant config from an hf model config

Source code in `vllm/model_executor/layers/quantization/torchao.py`

```
@classmethod
deffrom_config(cls, config: dict[str, Any]) -> "TorchAOConfig":
"""Create the quant config from an hf model config"""
    try:
        fromtorchao.core.configimport config_from_dict
    except ImportError as err:
        raise ImportError(
            "Please install torchao>=0.10.0 via "
            "`pip install torchao>=0.10.0` to use torchao quantization."
        ) fromerr

    quant_method = cls.get_from_keys_or(config, ["quant_method"], None)
    is_checkpoint_torchao_serialized = (
        quant_method is not None and "torchao" in quant_method
    )

    hf_config = cls.get_from_keys_or(config, ["quant_type"], None)
    assert hf_config is not None, "quant_type must be specified"
    assert len(hf_config) == 1 and "default" in hf_config, (
        "Expected only one key 'default' in quant_type dictionary"
    )
    quant_type = hf_config["default"]
    ao_config = config_from_dict(quant_type)

    # Adds skipped modules defined in "modules_to_not_convert"
    skip_modules = config.get("modules_to_not_convert", []) or []

    # Adds skipped modules defined in "module_fqn_to_config"
    _data = quant_type.get("_data", {})
    if not isinstance(_data, dict):
        _data = {}

    module_fqn = _data.get("module_fqn_to_config", {})
    if not isinstance(module_fqn, dict):
        module_fqn = {}

    for layer, layer_cfg in module_fqn.items():
        if layer_cfg is None:
            skip_modules.append(layer)

    return cls(ao_config, skip_modules, is_checkpoint_torchao_serialized)
```

### from\_config\_dict\_json `classmethod` [¶](#vllm.model_executor.layers.quantization.torchao.TorchAOConfig.from_config_dict_json "Permanent link")

```
from_config_dict_json(
    config_dict_json: str,
) -> TorchAOConfig
```

Initialize class from a config\_dict json string, got from torchao\_config\_object = some AOBaseConfig object json.dumps(config\_to\_dict(torchao\_config\_object))

Source code in `vllm/model_executor/layers/quantization/torchao.py`

```
@classmethod
deffrom_config_dict_json(cls, config_dict_json: str) -> "TorchAOConfig":
"""Initialize class from a config_dict json string, got from
    torchao_config_object = some AOBaseConfig object
    json.dumps(config_to_dict(torchao_config_object))
    """
    config_dict = json.loads(config_dict_json)
    hf_config = {"quant_type": {"default": config_dict}}
    return cls.from_config(hf_config)
```

### from\_config\_file `classmethod` [¶](#vllm.model_executor.layers.quantization.torchao.TorchAOConfig.from_config_file "Permanent link")

```
from_config_file(config_file: str) -> TorchAOConfig
```

Initialize class from a config file. Example:

```
config = Float8DynamicActivationFloat8WeightConfig(granularity=PerRow())
fn = "torchao_config.json"

with open(fn, "w") as f:
    f.write(json.dumps(config_to_dict(config)))
```

Source code in `vllm/model_executor/layers/quantization/torchao.py`

````
@classmethod
deffrom_config_file(cls, config_file: str) -> "TorchAOConfig":
"""Initialize class from a config file. Example:
    ```
    config = Float8DynamicActivationFloat8WeightConfig(granularity=PerRow())
    fn = "torchao_config.json"

    with open(fn, "w") as f:
        f.write(json.dumps(config_to_dict(config)))
    ```
    """
    with open(config_file) as f:
        f.seek(0)
        f_read = f.read()
        config_dict = json.loads(f_read)

    hf_config = {"quant_type": {"default": config_dict}}
    return cls.from_config(hf_config)
````

### get\_config\_filenames `staticmethod` [¶](#vllm.model_executor.layers.quantization.torchao.TorchAOConfig.get_config_filenames "Permanent link")

```
get_config_filenames() -> list[str]
```

torchao doesn't require additional config files, we use `config.json` from huggingface: `model_config.hf_config`

Source code in `vllm/model_executor/layers/quantization/torchao.py`

```
@staticmethod
defget_config_filenames() -> list[str]:
"""torchao doesn't require additional config files, we use
    `config.json` from huggingface: `model_config.hf_config`
    """
    return []
```

## TorchAOLinearMethod [¶](#vllm.model_executor.layers.quantization.torchao.TorchAOLinearMethod "Permanent link")

Bases: `LinearMethodBase`

Linear method for torchao.

Parameters:

Name Type Description Default `quant_config` `TorchAOConfig`

The torchao quantization config, a string that encodes the type of quantization and all relevant arguments.

*required*

Source code in `vllm/model_executor/layers/quantization/torchao.py`

```
classTorchAOLinearMethod(LinearMethodBase):
"""Linear method for torchao.

    Args:
        quant_config: The torchao quantization config, a string that encodes
            the type of quantization and all relevant arguments.
    """

    def__init__(self, quant_config: TorchAOConfig):
        self.quant_config = quant_config

    defcreate_weights(
        self,
        layer: torch.nn.Module,
        input_size_per_partition: int,
        output_partition_sizes: list[int],
        input_size: int,
        output_size: int,
        params_dtype: torch.dtype,
        **extra_weight_attrs,
    ):
        weight = Parameter(
            torch.empty(
                sum(output_partition_sizes),
                input_size_per_partition,
                dtype=params_dtype,
            ),
            requires_grad=False,
        )
        if self.quant_config.is_checkpoint_torchao_serialized:
            weight = torchao_quantize_param_data(
                weight, self.quant_config.torchao_config
            )

        set_weight_attrs(weight, {"input_dim": 1, "output_dim": 0})

        layer.register_parameter("weight", weight)
        set_weight_attrs(weight, extra_weight_attrs)

    defapply(
        self,
        layer: torch.nn.Module,
        x: torch.Tensor,
        bias: torch.Tensor | None = None,
    ) -> torch.Tensor:
        return F.linear(x, layer.weight, bias)

    defprocess_weights_after_loading(self, layer: torch.nn.Module) -> None:
        if self.quant_config.is_checkpoint_torchao_serialized:
            if not hasattr(layer, "weight"):
                return

            # record attributes attached to the weight, so we can
            # recover later
            recorded_weight_attr = _get_weight_attrs(layer.weight)

            layer.weight = Parameter(
                convert_to_packed_tensor_based_on_current_hardware(layer.weight),
                requires_grad=layer.weight.requires_grad,
            )

            _restore_weight_attrs(layer.weight, recorded_weight_attr)
            return

        # online quantize the weight if the checkpoint is not already
        # quantized by torchao
        recorded_weight_attr = _get_weight_attrs(layer.weight)

        weight = torchao_quantize_param_data(
            layer.weight, self.quant_config.torchao_config
        )
        weight = torch.nn.Parameter(
            convert_to_packed_tensor_based_on_current_hardware(weight),
            weight.requires_grad,
        )

        _restore_weight_attrs(weight, recorded_weight_attr)
        layer.register_parameter("weight", weight)
```

## should\_skip [¶](#vllm.model_executor.layers.quantization.torchao.should_skip "Permanent link")

Robust skipping logic: should\_skip("model.model.layers.1.q\_proj", \["model.model.layers.1.q\_proj"]) # True should\_skip("model.model.layers.10.o\_proj", \["o\_proj"]) -&gt; True should\_skip("visual.model.layers.1.q\_proj", \["visual"]) -&gt; True should\_skip("model.model.layers.1.q\_proj", \["layers.1"]) -&gt; True should\_skip("model.model.layers.11.q\_proj", \["layers.1"]) -&gt; False

Source code in `vllm/model_executor/layers/quantization/torchao.py`

```
defshould_skip(prefix: str, skip_modules: list[str]) -> bool:
"""
    Robust skipping logic:
    should_skip("model.model.layers.1.q_proj",
                ["model.model.layers.1.q_proj"])  # True
    should_skip("model.model.layers.10.o_proj", ["o_proj"])  -> True
    should_skip("visual.model.layers.1.q_proj", ["visual"])   -> True
    should_skip("model.model.layers.1.q_proj", ["layers.1"])  -> True
    should_skip("model.model.layers.11.q_proj", ["layers.1"]) -> False
    """
    for s in skip_modules:
        if prefix == s:
            return True
        if f".{s}." in f".{prefix}.":
            return True
    return False
```

## torchao\_quantize\_param\_data [¶](#vllm.model_executor.layers.quantization.torchao.torchao_quantize_param_data "Permanent link")

```
torchao_quantize_param_data(
    param: Tensor, torchao_config: Any
) -> Parameter
```

Quantize a Tensor with torchao quantization specified by torchao\_config

Parameters:

Name Type Description Default `param` `Tensor`

weight parameter of the linear module

*required* `torchao_config` `Any`

type of quantization and their arguments we want to use to quantize the Tensor

*required*

Source code in `vllm/model_executor/layers/quantization/torchao.py`

```
deftorchao_quantize_param_data(
    param: torch.Tensor, torchao_config: Any
) -> torch.nn.Parameter:
"""Quantize a Tensor with torchao quantization specified by torchao_config

    Args:
        param: weight parameter of the linear module
        torchao_config: type of quantization and their arguments we want to
            use to quantize the Tensor
    """
    fromtorchao.core.configimport AOBaseConfig
    fromtorchao.quantizationimport quantize_

    assert isinstance(torchao_config, AOBaseConfig), f"{torchao_config}"
"""
    Avoid real weight allocation for faster load, since we will
    end up setting it to param.
    """
    with torch.device("meta"):
        # linear can't be top level module since quantize_ is inplace
        # while some of our configs need to do module swap, and only non-top
        # level modules support module swap
        dummy_linear = torch.nn.Sequential(
            torch.nn.Linear(param.shape[1], param.shape[0], bias=False)
        )

    dummy_linear[0].weight = param
    quantize_(dummy_linear, torchao_config)
    return dummy_linear[0].weight
```