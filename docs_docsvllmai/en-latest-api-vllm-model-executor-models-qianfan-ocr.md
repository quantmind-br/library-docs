---
title: qianfan_ocr - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/qianfan_ocr/
source: sitemap
fetched_at: 2026-05-07T21:32:45.817493503-03:00
rendered_js: false
word_count: 49
summary: This document defines the QianfanOCR multimodal model architecture within vLLM, detailing its registration and specific quantization configuration overrides.
tags:
    - qianfan-ocr
    - multimodal-model
    - vllm-architecture
    - model-registration
    - quantization-config
category: reference
---

Bases: `InternVLChatModel`

QianfanOCR multimodal model.

Identical in structure to InternVLChatModel (InternViT vision encoder + pixel-shuffle MLP connector + Qwen3 language model). This class exists solely to register the `QianfanOCRForConditionalGeneration` architecture name that appears in the model's config.json.

Source code in `vllm/model_executor/models/qianfan_ocr.py`

```
@MULTIMODAL_REGISTRY.register_processor(
    BaseInternVLMultiModalProcessor,
    info=QianfanOCRProcessingInfo,
    dummy_inputs=BaseInternVLDummyInputsBuilder,
)
classQianfanOCRForConditionalGeneration(InternVLChatModel):
"""QianfanOCR multimodal model.

    Identical in structure to InternVLChatModel (InternViT vision encoder +
    pixel-shuffle MLP connector + Qwen3 language model).  This class exists
    solely to register the ``QianfanOCRForConditionalGeneration`` architecture
    name that appears in the model's config.json.
    """

    def_patch_quant_config(
        self, config: PretrainedConfig, quant_config: QuantizationConfig
    ) -> None:
        super()._patch_quant_config(config, quant_config)
        # ignore vit layers to preserve model performance
        if isinstance(quant_config, Fp8Config):
            _FP8_IGNORED_LAYERS = [
                *(
                    layer
                    for i in range(config.vision_config.num_hidden_layers)
                    for layer in [
                        f"vision_model.encoder.layers.{i}.attn.qkv",
                        f"vision_model.encoder.layers.{i}.attn.proj",
                        f"vision_model.encoder.layers.{i}.mlp.fc1",
                        f"vision_model.encoder.layers.{i}.mlp.fc2",
                    ]
                ),
                "language_model.lm_head",
                "mlp1.1",
                "mlp1.3",
            ]
            for layer in _FP8_IGNORED_LAYERS:
                if layer not in quant_config.ignored_layers:
                    quant_config.ignored_layers.append(layer)
```