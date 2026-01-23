---
title: '[BETA] Image Variations | liteLLM'
url: https://docs.litellm.ai/docs/image_variations
source: sitemap
fetched_at: 2026-01-21T19:45:26.763580417-03:00
rendered_js: false
word_count: 6
summary: This document demonstrates how to use the LiteLLM library to generate image variations using OpenAI's DALL-E and Topaz AI models.
tags:
    - litellm
    - image-variation
    - openai
    - topaz
    - dall-e-2
    - python-sdk
category: api
---

OpenAI's `/image/variations` endpoint is now supported.

```
from litellm import image_variation
import os 

# set env vars 
os.environ["OPENAI_API_KEY"]=""
os.environ["TOPAZ_API_KEY"]=""

# openai call
response = image_variation(
    model="dall-e-2", image=image_url
)

# topaz call
response = image_variation(
    model="topaz/Standard V2", image=image_url
)

print(response)
```