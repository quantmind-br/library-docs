---
title: image - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/multimodal/image/
source: sitemap
fetched_at: 2026-05-07T21:34:08.18940968-03:00
rendered_js: false
word_count: 14
summary: This document provides a utility function for rescaling image dimensions by a specified factor and optionally applying a transpose transformation.
tags:
    - image-processing
    - resizing
    - python-utility
    - vllm-multimodal
category: api
---

Rescale the dimensions of an image by a constant factor.

Source code in `vllm/multimodal/image.py`

```
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

defrescale_image_size(
    image: Image.Image, size_factor: float, transpose: int = -1
) -> Image.Image:
"""Rescale the dimensions of an image by a constant factor."""
    new_width = int(image.width * size_factor)
    new_height = int(image.height * size_factor)
    image = image.resize((new_width, new_height))
    if transpose >= 0:
        image = image.transpose(Image.Transpose(transpose))
    return image
```