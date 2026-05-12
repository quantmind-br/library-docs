---
title: skyworkr1v - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/skyworkr1v/
source: sitemap
fetched_at: 2026-05-07T21:33:17.854418999-03:00
rendered_js: false
word_count: 63
summary: This document defines the data structures and tensor schemas for processing image embeddings and pixel inputs within the SkyworkR1V model architecture.
tags:
    - skyworkr1v
    - tensor-schema
    - vllm
    - image-embedding
    - model-architecture
    - data-structure
category: reference
---

## SkyworkR1VImageEmbeddingInputs [¶](#vllm.model_executor.models.skyworkr1v.SkyworkR1VImageEmbeddingInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- ni: Number of images
- ifs: Image feature size
- hs: Hidden size (must match the hidden size of language model backbone)

Source code in `vllm/model_executor/models/skyworkr1v.py`

```
classSkyworkR1VImageEmbeddingInputs(TensorSchema):
"""
    Dimensions:
        - ni: Number of images
        - ifs: Image feature size
        - hs: Hidden size (must match the hidden size of language model
          backbone)
    """

    type: Literal["image_embeds"] = "image_embeds"

    data: Annotated[
        torch.Tensor | list[torch.Tensor],
        TensorShape("ni", "ifs", "hs"),
    ]
```

## SkyworkR1VImagePixelInputs [¶](#vllm.model_executor.models.skyworkr1v.SkyworkR1VImagePixelInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- bnp: Batch size * number of images * (1 + num\_patches)
- c: Number of channels (3)
- h: Height
- w: Width
- bn: Batch size * number of images

Source code in `vllm/model_executor/models/skyworkr1v.py`

```
classSkyworkR1VImagePixelInputs(TensorSchema):
"""
    Dimensions:
        - bnp: Batch size * number of images * (1 + num_patches)
        - c: Number of channels (3)
        - h: Height
        - w: Width
        - bn: Batch size * number of images
    """

    type: Literal["pixel_values"] = "pixel_values"

    pixel_values_flat: Annotated[
        torch.Tensor,
        TensorShape("bnp", 3, "h", "w"),
    ]

    num_patches: Annotated[
        torch.Tensor,
        TensorShape("bn"),
    ]
```