---
title: qwen_vl - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/processors/qwen_vl/
source: sitemap
fetched_at: 2026-05-07T21:38:13.183175552-03:00
rendered_js: false
word_count: 12
summary: This document defines the QwenVLImageProcessorFast class, which implements image preprocessing logic for the Qwen-VL model within the vLLM framework.
tags:
    - qwen-vl
    - image-processing
    - computer-vision
    - hugging-face
    - data-preprocessing
category: reference
---

Bases: `BaseImageProcessorFast`

Port of https://huggingface.co/Qwen/Qwen-VL/blob/main/visual.py#L354 to HF Transformers.

Source code in `vllm/transformers_utils/processors/qwen_vl.py`

```
classQwenVLImageProcessorFast(BaseImageProcessorFast):
"""
    Port of https://huggingface.co/Qwen/Qwen-VL/blob/main/visual.py#L354
    to HF Transformers.
    """

    resample = PILImageResampling.BICUBIC
    image_mean = [0.48145466, 0.4578275, 0.40821073]
    image_std = [0.26862954, 0.26130258, 0.27577711]
    size = {"height": 448, "width": 448}
    do_resize = True
    do_rescale = True
    do_normalize = True
```