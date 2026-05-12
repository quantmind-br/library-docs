---
title: base - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/online/base/
source: sitemap
fetched_at: 2026-05-07T21:27:26.845730777-03:00
rendered_js: false
word_count: 27
summary: This document defines the configuration class for online quantization in vLLM, which enables weight quantization during model loading without requiring pre-quantized checkpoints.
tags:
    - vllm
    - quantization
    - model-loading
    - online-quantization
    - deep-learning
    - configuration-class
category: reference
---

## vllm.model\_executor.layers.quantization.online.base [¶](#vllm.model_executor.layers.quantization.online.base "Permanent link")

## OnlineQuantizationConfig [¶](#vllm.model_executor.layers.quantization.online.base.OnlineQuantizationConfig "Permanent link")

Bases: `QuantizationConfig`

Model-level config class for online quantization (quantize fp16/bf16 weights during model loading, without requiring a pre-quantized checkpoint).

Source code in `vllm/model_executor/layers/quantization/online/base.py`

```
classOnlineQuantizationConfig(QuantizationConfig):
"""Model-level config class for online quantization (quantize fp16/bf16 weights
    during model loading, without requiring a pre-quantized checkpoint)."""

    def__init__(
        self,
        args: OnlineQuantizationConfigArgs,
    ) -> None:
        super().__init__()
        if (
            args.global_scheme is None
            and args.linear_scheme_override is None
            and args.moe_scheme_override is None
        ):
            raise ValueError(
                "OnlineQuantizationConfig requires at least one of "
                "global_scheme, linear_scheme_override, or "
                "moe_scheme_override to be set."
            )
        self.args = args
        self.quant_scheme = args.global_scheme
        self.ignored_layers: list[str] = args.ignore

    @classmethod
    defget_name(cls) -> QuantizationMethods:
        return "online"

    @classmethod
    defget_supported_act_dtypes(cls) -> list[torch.dtype]:
        return [torch.bfloat16, torch.half]

    @classmethod
    defget_min_capability(cls) -> int:
        # Note: as more online quant schemes will be added, this
        # value will become the minimum across all supported schemes.
        return 75

    @classmethod
    defget_config_filenames(cls) -> list[str]:
        return []

    @classmethod
    deffrom_config(cls, config: dict[str, Any]) -> "OnlineQuantizationConfig":
        raise NotImplementedError(
            "OnlineQuantizationConfig does not support loading from a "
            "checkpoint config. Use quantization_config or "
            "quantization='fp8_per_tensor'/'fp8_per_block' instead."
        )

    defget_quant_method(
        self, layer: torch.nn.Module, prefix: str
    ) -> "QuantizeMethodBase | None":
        if isinstance(layer, LinearBase):
            if should_ignore_layer(
                prefix,
                ignore=self.ignored_layers,
                fused_mapping=self.packed_modules_mapping,
            ):
                return UnquantizedLinearMethod()

            linear_scheme = self.args.linear_scheme_override or self.args.global_scheme
            if linear_scheme == OnlineQuantScheme.INT8_PER_CHANNEL_WEIGHT_ONLY:
                logger.warning_once(
                    "INT8 online quantization only quantizes MoE expert "
                    "weights. linear layers remain in full precision."
                )
                return UnquantizedLinearMethod()
            elif linear_scheme == OnlineQuantScheme.FP8_PER_BLOCK:
                return Fp8PerBlockOnlineLinearMethod()
            elif linear_scheme == OnlineQuantScheme.MXFP8:
                return Mxfp8OnlineLinearMethod()
            else:
                return Fp8PerTensorOnlineLinearMethod()
        elif isinstance(layer, FusedMoE):
            if should_ignore_layer(
                prefix,
                ignore=self.ignored_layers,
                fused_mapping=self.packed_modules_mapping,
            ):
                return UnquantizedFusedMoEMethod(layer.moe_config)

            moe_scheme = self.args.moe_scheme_override or self.args.global_scheme
            if moe_scheme == OnlineQuantScheme.INT8_PER_CHANNEL_WEIGHT_ONLY:
                return Int8OnlineMoEMethod(layer=layer)
            elif moe_scheme == OnlineQuantScheme.FP8_PER_BLOCK:
                return Fp8PerBlockOnlineMoEMethod(layer=layer)
            elif moe_scheme == OnlineQuantScheme.MXFP8:
                return Mxfp8OnlineMoEMethod(layer=layer)
            else:
                return Fp8PerTensorOnlineMoEMethod(layer=layer)
        return None
```