---
title: WatsonX Audio Transcription | liteLLM
url: https://docs.litellm.ai/docs/providers/watsonx/audio_transcription
source: sitemap
fetched_at: 2026-01-21T19:50:58.309891014-03:00
rendered_js: false
word_count: 0
summary: This document provides a code example for transcribing audio files using the LiteLLM library with the IBM WatsonX Whisper model.
tags:
    - litellm
    - audio-transcription
    - ibm-watsonx
    - whisper-v3
    - api-integration
category: tutorial
---

```
import litellm

response = litellm.transcription(
    model="watsonx/whisper-large-v3-turbo",
file=open("audio.mp3","rb"),
    api_base="https://us-south.ml.cloud.ibm.com",
    api_key="your-api-key",
    project_id="your-project-id"
)
print(response.text)
```