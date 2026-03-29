---
title: One post tagged with "deepgram" | liteLLM
url: https://docs.litellm.ai/release_notes/tags/deepgram
source: sitemap
fetched_at: 2026-01-21T19:41:34.830964141-03:00
rendered_js: false
word_count: 44
summary: This document provides instructions on performing audio transcription with Deepgram using LiteLLM and explains the document inlining feature for Fireworks AI models.
tags:
    - litellm
    - audio-transcription
    - deepgram
    - fireworks-ai
    - document-parsing
category: guide
---

```
from litellm import transcription
import os 

# set api keys 
os.environ["DEEPGRAM_API_KEY"]=""
audio_file =open("/path/to/audio.mp3","rb")

response = transcription(model="deepgram/nova-2",file=audio_file)

print(f"response: {response}")
```

LiteLLM supports document inlining for Fireworks AI models. This is useful for models that are not vision models, but still need to parse documents/images/etc. LiteLLM will add `#transform=inline` to the url of the image\_url, if the model is not a vision model [See Code](https://github.com/BerriAI/litellm/blob/1ae9d45798bdaf8450f2dfdec703369f3d2212b7/litellm/llms/fireworks_ai/chat/transformation.py#L114)