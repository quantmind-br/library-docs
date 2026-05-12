---
title: fbgemm_fp8 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/fbgemm_fp8/
source: sitemap
fetched_at: 2026-05-07T21:27:13.909631678-03:00
rendered_js: false
word_count: 15
summary: This document defines the configuration class for FBGEMM FP8 quantization within the vLLM model execution framework.
tags:
    - vllm
    - quantization
    - fbgemm
    - fp8
    - model-configuration
    - machine-learning
category: reference
---

## vllm.model\_executor.layers.quantization.fbgemm\_fp8 [¶](#vllm.model_executor.layers.quantization.fbgemm_fp8 "Permanent link")

## FBGEMMFp8Config [¶](#vllm.model_executor.layers.quantization.fbgemm_fp8.FBGEMMFp8Config "Permanent link")

Bases: `QuantizationConfig`

Config class for FBGEMM Fp8.

Source code in `vllm/model_executor/layers/quantization/fbgemm_fp8.py`

```
classFBGEMMFp8Config(QuantizationConfig):
"""Config class for FBGEMM Fp8."""

    def__init__(self, ignore_list: list[str], input_scale_ub: float):
        super().__init__()
        self.ignore_list = ignore_list if ignore_list else []
        self.input_scale_ub = input_scale_ub

        # For GPUs that lack FP8 hardware support, we can leverage the Marlin
        # kernel for fast weight-only FP8 quantization
        self.use_marlin = not current_platform.has_device_capability(89)

    @classmethod
    defget_name(cls) -> QuantizationMethods:
        return "fbgemm_fp8"

    @classmethod
    defget_supported_act_dtypes(cls) -> list[torch.dtype]:
        return [torch.bfloat16, torch.float16]

    @classmethod
    defget_min_capability(cls) -> int:
        return 80

    @classmethod
    defget_config_filenames(cls) -> list[str]:
        return []

    @classmethod
    deffrom_config(cls, config: dict[str, Any]) -> "FBGEMMFp8Config":
        ignore_list = cls.get_from_keys(config, ["modules_to_not_convert"])
        input_scale_ub = cls.get_from_keys(config, ["activation_scale_ub"])
        return cls(ignore_list=ignore_list, input_scale_ub=input_scale_ub)

    defget_quant_method(
        self, layer: torch.nn.Module, prefix: str
    ) -> "QuantizeMethodBase | None":
        if isinstance(layer, LinearBase):
            if is_layer_skipped(
                prefix=prefix,
                ignored_layers=self.ignore_list,
                fused_mapping=self.packed_modules_mapping,
            ):
                return UnquantizedLinearMethod()
            return FBGEMMFp8LinearMethod(self)
        return None
```