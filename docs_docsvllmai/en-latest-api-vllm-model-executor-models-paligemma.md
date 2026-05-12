---
title: paligemma - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/paligemma/
source: sitemap
fetched_at: 2026-05-07T21:32:30.921097043-03:00
rendered_js: false
word_count: 51
summary: This document defines the data structures and tensor dimensions for PaliGemma image embedding and pixel input schemas used within the vLLM model execution framework.
tags:
    - paligemma
    - tensor-schema
    - vllm
    - image-embedding
    - machine-learning-models
category: reference
---

## PaliGemmaImageEmbeddingInputs [¶](#vllm.model_executor.models.paligemma.PaliGemmaImageEmbeddingInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- bn: Batch size * number of images
- ifs: Image feature size
- hs: Hidden size (must match language model backbone)

Source code in `vllm/model_executor/models/paligemma.py`

```
classPaliGemmaImageEmbeddingInputs(TensorSchema):
"""
    Dimensions:
        - bn: Batch size * number of images
        - ifs: Image feature size
        - hs: Hidden size (must match language model backbone)
    """

    type: Literal["image_embeds"] = "image_embeds"
    data: Annotated[torch.Tensor, TensorShape("bn", "ifs", "hs")]
```

## PaliGemmaImagePixelInputs [¶](#vllm.model_executor.models.paligemma.PaliGemmaImagePixelInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- bn: Batch size * number of images
- c: Number of channels (3)
- h: Height
- w: Width

Source code in `vllm/model_executor/models/paligemma.py`

```
classPaliGemmaImagePixelInputs(TensorSchema):
"""
    Dimensions:
        - bn: Batch size * number of images
        - c: Number of channels (3)
        - h: Height
        - w: Width
    """

    type: Literal["pixel_values"] = "pixel_values"
    data: Annotated[torch.Tensor, TensorShape("bn", 3, "h", "w")]
```