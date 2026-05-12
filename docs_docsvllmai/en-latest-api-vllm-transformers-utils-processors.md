---
title: processors - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/processors/
source: sitemap
fetched_at: 2026-05-07T21:37:46.24586218-03:00
rendered_js: false
word_count: 105
summary: This document outlines the directory structure and naming conventions for custom multi-modal processors required by vLLM when standard Hugging Face implementations are unavailable or require overrides.
tags:
    - multi-modal
    - vllm
    - processor
    - model-integration
    - custom-modules
    - image-text-processing
category: configuration
---

Multi-modal processors may be defined in this directory for the following reasons:

- There is no processing file defined by HF Hub or Transformers library.
- There is a need to override the existing processor to support vLLM.

Modules:

Name Description `bagel`

BAGEL processor for image and text inputs.

`cheers`

Cheers (UMM) processor for image and text inputs.

`cohere_asr` `deepseek_ocr` `deepseek_vl2` `fireredasr2` `fireredlid`

FireRedLID feature extractor and processor.

`funasr` `glm4v` `granite4_vision` `hunyuan_vl` `hunyuan_vl_image`

Image processor class for HunYuanVL.

`internvl` `isaac` `kimi_audio`

Processor for Kimi-Audio ASR model.

`kimi_k25` `mimo_v2_omni`

MiMo-Omni multimodal processor for vLLM.

`moondream3`

Custom processor for Moondream3 model.

`nano_nemotron_vl` `nemotron_vl` `ovis` `ovis2_5` `pixtral` `qwen3_asr` `qwen_vl` `voxtral`