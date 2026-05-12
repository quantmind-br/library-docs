---
title: experts_int8 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/experts_int8/
source: sitemap
fetched_at: 2026-05-07T21:27:12.944121624-03:00
rendered_js: false
word_count: 36
summary: This document defines the configuration class for online int8 quantization of Mixture-of-Experts expert weights within the vLLM model execution framework.
tags:
    - quantization
    - moe
    - int8
    - model-optimization
    - vllm-framework
category: reference
---

Bases: `QuantizationConfig`

Online int8 quantization for MoE expert weights. Linear layers are left unquantized.

Backward-compatible config for `--quantization experts_int8`. Prefer `--quantization int8_per_channel`

Source code in `vllm/model_executor/layers/quantization/experts_int8.py`

```
classExpertsInt8Config(QuantizationConfig):
"""Online int8 quantization for MoE expert weights.
    Linear layers are left unquantized.

    Backward-compatible config for ``--quantization experts_int8``.
    Prefer ``--quantization int8_per_channel``
    """

    def__init__(self) -> None:
        super().__init__()

    @classmethod
    defget_name(cls) -> QuantizationMethods:
        return "experts_int8"

    @classmethod
    defget_supported_act_dtypes(cls) -> list[torch.dtype]:
        return [torch.bfloat16, torch.half]

    @classmethod
    defget_min_capability(cls) -> int:
        return 80

    @classmethod
    defget_config_filenames(cls) -> list[str]:
        return []

    @classmethod
    deffrom_config(cls, config: dict[str, Any]) -> "ExpertsInt8Config":
        return cls()

    defget_quant_method(
        self, layer: torch.nn.Module, prefix: str
    ) -> "QuantizeMethodBase | None":
        if isinstance(layer, LinearBase):
            return UnquantizedLinearMethod()
        elif isinstance(layer, FusedMoE):
            return Int8OnlineMoEMethod(layer=layer)
        return None
```