---
title: Azure Text to Speech (tts) | liteLLM
url: https://docs.litellm.ai/docs/providers/azure/azure_speech
source: sitemap
fetched_at: 2026-01-21T19:48:21.490865746-03:00
rendered_js: false
word_count: 0
summary: This document provides a code implementation for converting text to speech using an Azure-hosted model, detailing parameters for voice selection, speed, and output format.
tags:
    - text-to-speech
    - azure-openai
    - speech-synthesis
    - api-usage
    - audio-generation
category: reference
---

```
response = speech(
    model="azure/<your-deployment-name>",
    voice="alloy",# Required: Voice selection
input="text to convert",# Required: Input text
    speed=1.0,# Optional: 0.25 to 4.0 (default: 1.0)
    response_format="mp3"# Optional: mp3, opus, aac, flac, wav, pcm
)
```