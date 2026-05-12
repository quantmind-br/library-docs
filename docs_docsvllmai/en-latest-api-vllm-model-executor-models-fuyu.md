---
title: fuyu - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/fuyu/
source: sitemap
fetched_at: 2026-05-07T21:30:07.918988272-03:00
rendered_js: false
word_count: 5
summary: This document defines the schema for image patch inputs used in the Fuyu model, specifying the structure and dimensions of tensor data and patch counts.
tags:
    - fuyu-model
    - tensor-schema
    - image-processing
    - data-structure
    - machine-learning
category: reference
---

```
classFuyuImagePatchInputs(TensorSchema):
"""
    Dimensions:
        - bn: Batch size * number of images
        - bnp: Batch size * number of images * number of patches
        - fn: patch_size_x * patch_size_y * num_channels
    """

    type: Literal["image_patches"] = "image_patches"

    image_patches_flat: Annotated[torch.Tensor, TensorShape("bnp", "fn")]

    patches_per_image: Annotated[list[int], TensorShape("bn")]
"""
    The number of total patches for each image in the batch.

    This is used to split the embeddings which has the first two dimensions
    flattened just like `image_patches_flat`.
    """
```