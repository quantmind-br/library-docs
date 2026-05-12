---
title: glm4v - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/processors/glm4v/
source: sitemap
fetched_at: 2026-05-07T21:37:55.337419281-03:00
rendered_js: false
word_count: 12
summary: This document defines the GLM4VImageProcessorFast class, a Hugging Face Transformers-compatible image processor for the GLM-4V model architecture.
tags:
    - image-processing
    - transformers
    - vllm
    - computer-vision
    - glm-4v
category: reference
---

Bases: `BaseImageProcessorFast`

Port of https://huggingface.co/zai-org/glm-4v-9b/blob/main/tokenization\_chatglm.py#L177 to HF Transformers.

Source code in `vllm/transformers_utils/processors/glm4v.py`

```
classGLM4VImageProcessorFast(BaseImageProcessorFast):
"""
    Port of https://huggingface.co/zai-org/glm-4v-9b/blob/main/tokenization_chatglm.py#L177
    to HF Transformers.
    """

    resample = PILImageResampling.BICUBIC
    image_mean = [0.48145466, 0.4578275, 0.40821073]
    image_std = [0.26862954, 0.26130258, 0.27577711]
    size = {"height": 1120, "width": 1120}
    do_resize = True
    do_rescale = True
    do_normalize = True
```