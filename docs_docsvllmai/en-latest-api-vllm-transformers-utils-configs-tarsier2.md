---
title: tarsier2 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/configs/tarsier2/
source: sitemap
fetched_at: 2026-05-07T21:37:43.961437737-03:00
rendered_js: false
word_count: 51
summary: This document defines a custom configuration class designed to override default AutoConfig behavior for the Tarsier2 model, preventing the generation of redundant nested configuration structures.
tags:
    - model-configuration
    - transformers
    - config-override
    - tarsier2
    - qwen2-vl
    - python-class
category: configuration
---

Bases: `Qwen2VLConfig`

Tarsier2's config.json is written such that AutoConfig.from\_pretrained will create a deeply nested config consisting of:

- LlavaConfig
- Qwen2VLConfig
  
  - Qwen2VLTextConfig
  - Qwen2VLVisionConfig
- Qwen2VLConfig
  
  - Qwen2VLTextConfig
  - Qwen2VLVisionConfig

When it should really just be a single Qwen2VLConfig.

This class is a hack to stop AutoConfig from creating the nested config structure.

Source code in `vllm/transformers_utils/configs/tarsier2.py`

```
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24

classTarsier2Config(Qwen2VLConfig):
"""
    Tarsier2's config.json is written such that AutoConfig.from_pretrained will create
    a deeply nested config consisting of:

    - LlavaConfig
      - Qwen2VLConfig
        - Qwen2VLTextConfig
        - Qwen2VLVisionConfig
      - Qwen2VLConfig
        - Qwen2VLTextConfig
        - Qwen2VLVisionConfig

    When it should really just be a single Qwen2VLConfig.

    This class is a hack to stop AutoConfig from creating the nested config structure.
    """

    model_type = "tarsier2"
```