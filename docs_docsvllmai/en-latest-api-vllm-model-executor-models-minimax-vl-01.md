---
title: minimax_vl_01 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/minimax_vl_01/
source: sitemap
fetched_at: 2026-05-07T21:31:51.845215411-03:00
rendered_js: false
word_count: 58
summary: This document defines the data schema and input dimensions for the MiniMaxVL01 image pixel inputs, specifying the expected structure for pixel values and image metadata.
tags:
    - minimax-vl-01
    - image-processing
    - tensor-schema
    - computer-vision
    - data-structure
category: reference
---

Bases: `TensorSchema`

Dimensions

- bn: Batch size * number of images
- np: Number of patches + 1
- c: Number of channels (3)
- h: Height
- w: Width

Note that `num_patches` may be different per batch and image, in which case the data is passed as a list instead of a batched tensor.

Source code in `vllm/model_executor/models/minimax_vl_01.py`

```
classMiniMaxVL01ImagePixelInputs(TensorSchema):
"""
    Dimensions:
        - bn: Batch size * number of images
        - np: Number of patches + 1
        - c: Number of channels (3)
        - h: Height
        - w: Width

    Note that `num_patches` may be different per batch and image,
    in which case the data is passed as a list instead of a batched tensor.
    """

    type: Literal["pixel_values"] = "pixel_values"
    pixel_values: Annotated[
        torch.Tensor | list[torch.Tensor],
        TensorShape("bn", "np", 3, "h", "w", dynamic_dims={"np", "h", "w"}),
    ]

    image_sizes: Annotated[torch.Tensor | None, TensorShape("bn", 2)]
```