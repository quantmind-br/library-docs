---
title: Quantization - vLLM
url: https://docs.vllm.ai/en/latest/features/quantization/
source: sitemap
fetched_at: 2026-05-07T21:14:19.93729181-03:00
rendered_js: false
word_count: 533
summary: This document provides an overview of quantization methods supported by vLLM, including hardware compatibility charts and instructions for implementing custom out-of-tree quantization plugins.
tags:
    - quantization
    - vllm
    - model-optimization
    - hardware-compatibility
    - custom-plugins
    - llm-inference
category: concept
---

[](https://github.com/vllm-project/vllm/edit/main/docs/features/quantization/README.md "Edit this page")

Quantization trades off model precision for smaller memory footprint, allowing large models to be run on a wider range of devices.

Tip

To get started with quantization, see [LLM Compressor](https://docs.vllm.ai/en/latest/features/quantization/llm_compressor/), a library for optimizing models for deployment with vLLM that supports FP8, INT8, INT4, and other quantization formats.

The following are the supported quantization formats for vLLM:

- [AutoAWQ](https://docs.vllm.ai/en/latest/features/quantization/auto_awq/)
- [BitsAndBytes](https://docs.vllm.ai/en/latest/features/quantization/bnb/)
- [GGUF](https://docs.vllm.ai/en/latest/features/quantization/gguf/)
- [GPTQModel](https://docs.vllm.ai/en/latest/features/quantization/gptqmodel/)
- [Intel Neural Compressor](https://docs.vllm.ai/en/latest/features/quantization/inc/)
- [INT4 W4A16](https://docs.vllm.ai/en/latest/features/quantization/int4/)
- [INT8 W8A8](https://docs.vllm.ai/en/latest/features/quantization/int8/)
- [FP8 W8A8](https://docs.vllm.ai/en/latest/features/quantization/fp8/)
- [NVIDIA Model Optimizer](https://docs.vllm.ai/en/latest/features/quantization/modelopt/)
- [Online Quantization](https://docs.vllm.ai/en/latest/features/quantization/online/)
- [AMD Quark](https://docs.vllm.ai/en/latest/features/quantization/quark/)
- [Quantized KV Cache](https://docs.vllm.ai/en/latest/features/quantization/quantized_kvcache/)
- [TorchAO](https://docs.vllm.ai/en/latest/features/quantization/torchao/)
- [FP8 ViT Encoder Attention](https://docs.vllm.ai/en/latest/features/quantization/fp8_vit_attn/)

## Supported Hardware[¶](#supported-hardware "Permanent link")

The table below shows the compatibility of various quantization implementations with different hardware platforms in vLLM:

Implementation Volta Turing Ampere Ada Hopper AMD GPU Intel GPU x86 CPU AWQ ❌ ✅︎ ✅︎ ✅︎ ✅︎ ❌ ✅︎ ✅︎ GPTQ ✅︎ ✅︎ ✅︎ ✅︎ ✅︎ ❌ ✅︎ ✅︎ Marlin (GPTQ/AWQ/FP8/FP4) ❌ ✅︎* ✅︎ ✅︎ ✅︎ ❌ ❌ ❌ INT8 (W8A8) ❌ ✅︎ ✅︎ ✅︎ ✅︎ ❌ ❌ ✅︎ FP8 (W8A8) ❌ ❌ ❌ ✅︎ ✅︎ ✅︎ ❌ ❌ bitsandbytes ✅︎ ✅︎ ✅︎ ✅︎ ✅︎ ❌ ❌ ❌ DeepSpeedFP ✅︎ ✅︎ ✅︎ ✅︎ ✅︎ ❌ ❌ ❌ GGUF ✅︎ ✅︎ ✅︎ ✅︎ ✅︎ ✅︎ ❌ ❌

- Volta refers to SM 7.0, Turing to SM 7.5, Ampere to SM 8.0/8.6, Ada to SM 8.9, and Hopper to SM 9.0.
- ✅︎ indicates that the quantization method is supported on the specified hardware.
- ❌ indicates that the quantization method is not supported on the specified hardware.
- All Intel Gaudi quantization support has been migrated to [vLLM-Gaudi](https://github.com/vllm-project/vllm-gaudi).
- \*Turing does not support Marlin MXFP4.

Note

This compatibility chart is subject to change as vLLM continues to evolve and expand its support for different hardware platforms and quantization methods.

For the most up-to-date information on hardware support and quantization methods, please refer to [vllm/model\_executor/layers/quantization](https://github.com/vllm-project/vllm/tree/main/vllm/model_executor/layers/quantization) or consult with the vLLM development team.

## Out-of-Tree Quantization Plugins[¶](#out-of-tree-quantization-plugins "Permanent link")

vLLM supports registering custom, out-of-tree quantization methods using the `@register_quantization_config` decorator. This allows you to implement and use your own quantization schemes without modifying the vLLM codebase.

### Registering a Custom Quantization Method[¶](#registering-a-custom-quantization-method "Permanent link")

To register a custom quantization method, create a class that inherits from [`QuantizationConfig`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizationConfig "            QuantizationConfig") and decorate it with `@register_quantization_config`. The `get_quant_method` dispatches to the appropriate quantize method based on the layer type:

```
importtorch
fromvllm.model_executor.layers.quantizationimport (
    register_quantization_config,
)
fromvllm.model_executor.layers.quantization.base_configimport (
    QuantizationConfig,
    QuantizeMethodBase,
)
fromvllm.model_executor.layers.linearimport LinearBase
fromvllm.model_executor.layers.fused_moeimport FusedMoE

@register_quantization_config("my_quant")
classMyQuantConfig(QuantizationConfig):
"""Custom quantization config."""

    defget_name(self) -> str:
        return "my_quant"

    defget_supported_act_dtypes(self) -> list:
        return [torch.float16, torch.bfloat16]

    @classmethod
    defget_min_capability(cls) -> int:
        # Minimum GPU compute capability, -1 for no restriction
        return -1

    @staticmethod
    defget_config_filenames() -> list[str]:
        # Config files to search for in model directory
        return []

    @classmethod
    deffrom_config(cls, config: dict) -> "MyQuantConfig":
        # Create config from model's quantization config
        return cls()

    defget_quant_method(
        self, layer: torch.nn.Module, prefix: str
    ) -> QuantizeMethodBase | None:
        # Dispatch based on layer type
        # NOTE: you only need to implement methods you care about
        if isinstance(layer, LinearBase):
            return MyQuantLinearMethod()
        elif isinstance(layer, FusedMoE):
            return MyQuantMoEMethod(layer.moe_config)
        return None
```

### Required QuantizationConfig Methods[¶](#required-quantizationconfig-methods "Permanent link")

Your custom [`QuantizationConfig`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizationConfig "            QuantizationConfig") subclass must implement these abstract methods:

Method Description `get_name()` Returns the name of the quantization method `get_supported_act_dtypes()` Returns list of supported activation dtypes (e.g., `torch.float16`) `get_min_capability()` Returns minimum GPU compute capability (e.g., 80 for Ampere, -1 for no restriction) `get_config_filenames()` Returns list of config filenames to search for in model directory `from_config(config)` Class method to create config from model's quantization config dict `get_quant_method(layer, prefix)` Returns the quantization method for a given layer, or `None` to skip

### Implementing a Quantized Linear Method[¶](#implementing-a-quantized-linear-method "Permanent link")

For linear layers, return a [`QuantizeMethodBase`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase "            QuantizeMethodBase") subclass from `get_quant_method`. You can extend [`UnquantizedLinearMethod`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/linear/#vllm.model_executor.layers.linear.UnquantizedLinearMethod "            UnquantizedLinearMethod") as a starting point:

```
fromvllm.model_executor.layers.linearimport UnquantizedLinearMethod

classMyQuantLinearMethod(UnquantizedLinearMethod):
"""Custom quantization method for linear layers."""

    defcreate_weights(
        self, layer: torch.nn.Module, *weight_args, **extra_weight_attrs
    ):
        # Create quantized weights for the layer
        ...

    defapply(
        self,
        layer: torch.nn.Module,
        x: torch.Tensor,
        bias: torch.Tensor | None = None,
    ) -> torch.Tensor:
        # Apply custom quantization logic here
        ...
```

### Implementing a Quantized MoE Method[¶](#implementing-a-quantized-moe-method "Permanent link")

For Mixture of Experts (MoE) models, return a `FusedMoEMethodBase` subclass from `get_quant_method`. You can use [`UnquantizedFusedMoEMethod`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method/#vllm.model_executor.layers.fused_moe.unquantized_fused_moe_method.UnquantizedFusedMoEMethod "            UnquantizedFusedMoEMethod") to skip MoE quantization:

```
fromvllm.model_executor.layers.fused_moe.layerimport UnquantizedFusedMoEMethod
fromvllm.model_executor.layers.fused_moe.fused_moe_method_baseimport (
    FusedMoEMethodBase,
)
fromvllm.model_executor.layers.fused_moe.configimport FusedMoEQuantConfig

classMyQuantMoEMethod(FusedMoEMethodBase):
"""Custom quantization method for MoE layers."""

    defcreate_weights(
        self,
        layer: torch.nn.Module,
        num_experts: int,
        hidden_size: int,
        intermediate_size_per_partition: int,
        params_dtype: torch.dtype,
        **extra_weight_attrs,
    ):
        # Create quantized weights for the MoE layer
        ...

    defapply(
        self,
        layer: torch.nn.Module,
        router: "FusedMoERouter",
        x: torch.Tensor,
        router_logits: torch.Tensor,
    ) -> torch.Tensor:
        # Apply MoE computation with quantized weights
        ...

    defget_fused_moe_quant_config(
        self, layer: torch.nn.Module
    ) -> FusedMoEQuantConfig | None:
        # Return the MoE quantization configuration
        ...
```

See existing implementations like [`Fp8MoEMethod`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/fp8/#vllm.model_executor.layers.quantization.fp8.Fp8MoEMethod "            Fp8MoEMethod") in `vllm/model_executor/layers/quantization/fp8.py` for reference.

### Using the Plugin[¶](#using-the-plugin "Permanent link")

Once registered, you can use your custom quantization method with vLLM:

```
# Register your quantization method (import the module containing your config)
importmy_quant_plugin

fromvllmimport LLM

# Use the custom quantization method
llm = LLM(model="your-model", quantization="my_quant")
```

For more information on the plugin system, see the [Plugin System documentation](https://docs.vllm.ai/en/latest/design/plugin_system/).