---
title: kimi_vl - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/kimi_vl/
source: sitemap
fetched_at: 2026-05-07T21:31:16.794666186-03:00
rendered_js: false
word_count: 0
summary: This document defines the schema for Kimi vision-language image inputs, specifying the expected structure and tensor shapes for pixel values and image grid dimensions.
tags:
    - data-schema
    - vision-language
    - tensor-configuration
    - kimi-model
    - pytorch-typing
category: reference
---

```
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148

classKimiVLImagePixelInputs(TensorSchema):
"""
    Dimensions:
        - nc: Number of channels
        - np: Number of patches
        - ps: Patch size
        - ni: Number of images
    """

    type: Literal["pixel_values"] = "pixel_values"

    pixel_values: Annotated[
        torch.Tensor | list[torch.Tensor],
        TensorShape("np", 3, "ps", "ps"),
    ]

    image_grid_hws: Annotated[torch.Tensor, TensorShape("ni", 2)]
```