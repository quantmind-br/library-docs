---
title: v1.56.4
url: https://docs.litellm.ai/release_notes/v1.56.4
source: sitemap
fetched_at: 2026-01-21T19:43:15.250551297-03:00
rendered_js: false
word_count: 125
summary: This document outlines recent updates to LiteLLM, including support for Deepgram speech-to-text and Fireworks AI vision models, alongside security fixes and Proxy Admin UI improvements.
tags:
    - litellm
    - deepgram
    - fireworks-ai
    - speech-to-text
    - vision-models
    - dependency-upgrade
    - admin-ui
category: other
---

`deepgram`, `fireworks ai`, `vision`, `admin ui`, `dependency upgrades`

## New Models[​](#new-models "Direct link to New Models")

### **Deepgram Speech to Text**[​](#deepgram-speech-to-text "Direct link to deepgram-speech-to-text")

New Speech to Text support for Deepgram models. [**Start Here**](https://docs.litellm.ai/docs/providers/deepgram)

```
from litellm import transcription
import os 

# set api keys 
os.environ["DEEPGRAM_API_KEY"]=""
audio_file =open("/path/to/audio.mp3","rb")

response = transcription(model="deepgram/nova-2",file=audio_file)

print(f"response: {response}")
```

### **Fireworks AI - Vision** support for all models[​](#fireworks-ai---vision-support-for-all-models "Direct link to fireworks-ai---vision-support-for-all-models")

LiteLLM supports document inlining for Fireworks AI models. This is useful for models that are not vision models, but still need to parse documents/images/etc. LiteLLM will add `#transform=inline` to the url of the image\_url, if the model is not a vision model [See Code](https://github.com/BerriAI/litellm/blob/1ae9d45798bdaf8450f2dfdec703369f3d2212b7/litellm/llms/fireworks_ai/chat/transformation.py#L114)

## Proxy Admin UI[​](#proxy-admin-ui "Direct link to Proxy Admin UI")

- `Test Key` Tab displays `model` used in response

<!--THE END-->

- `Test Key` Tab renders content in `.md`, `.py` (any code/markdown format)

## Dependency Upgrades[​](#dependency-upgrades "Direct link to Dependency Upgrades")

- (Security fix) Upgrade to `fastapi==0.115.5` [https://github.com/BerriAI/litellm/pull/7447](https://github.com/BerriAI/litellm/pull/7447)

## Bug Fixes[​](#bug-fixes "Direct link to Bug Fixes")

- Add health check support for realtime models [Here](https://docs.litellm.ai/docs/proxy/health#realtime-models)
- Health check error with audio\_transcription model [https://github.com/BerriAI/litellm/issues/5999](https://github.com/BerriAI/litellm/issues/5999)