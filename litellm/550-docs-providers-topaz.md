---
title: Topaz | liteLLM
url: https://docs.litellm.ai/docs/providers/topaz
source: sitemap
fetched_at: 2026-01-21T19:50:31.644726091-03:00
rendered_js: false
word_count: 0
summary: This document provides a code example for generating image variations using the LiteLLM library and the Topaz API.
tags:
    - litellm
    - image-variation
    - topaz-api
    - python
    - image-generation
category: api
---

```
from litellm import image_variation
import os 

os.environ["TOPAZ_API_KEY"]=""
response = image_variation(
    model="topaz/Standard V2", image=image_url
)
```