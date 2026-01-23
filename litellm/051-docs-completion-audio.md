---
title: Using Audio Models | liteLLM
url: https://docs.litellm.ai/docs/completion/audio
source: sitemap
fetched_at: 2026-01-21T19:44:19.32475599-03:00
rendered_js: false
word_count: 0
summary: This document provides a code example for using litellm to process audio inputs and generate multimodal responses using models like gpt-4o-audio-preview.
tags:
    - litellm
    - audio-processing
    - python-sdk
    - multimodal-ai
    - gpt-4o-audio
    - base64-encoding
category: tutorial
---

```
import base64
import requests

url ="https://openaiassets.blob.core.windows.net/$web/API/docs/audio/alloy.wav"
response = requests.get(url)
response.raise_for_status()
wav_data = response.content
encoded_string = base64.b64encode(wav_data).decode("utf-8")

completion = litellm.completion(
    model="gpt-4o-audio-preview",
    modalities=["text","audio"],
    audio={"voice":"alloy","format":"wav"},
    messages=[
{
"role":"user",
"content":[
{"type":"text","text":"What is in this recording?"},
{
"type":"input_audio",
"input_audio":{"data": encoded_string,"format":"wav"},
},
],
},
],
)

print(completion.choices[0].message)
```