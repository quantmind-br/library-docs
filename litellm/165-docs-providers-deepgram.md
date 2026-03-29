---
title: Deepgram | liteLLM
url: https://docs.litellm.ai/docs/providers/deepgram
source: sitemap
fetched_at: 2026-01-21T19:48:54.288500421-03:00
rendered_js: false
word_count: 42
summary: This document provides instructions for integrating Deepgram's speech-to-text services using LiteLLM, covering both Python SDK usage and proxy configuration.
tags:
    - litellm
    - deepgram
    - audio-transcription
    - speech-to-text
    - api-integration
    - python
category: guide
---

LiteLLM supports Deepgram's `/listen` endpoint.

PropertyDetailsDescriptionDeepgram's voice AI platform provides APIs for speech-to-text, text-to-speech, and language understanding.Provider Route on LiteLLM`deepgram/`Provider Doc[Deepgram ↗](https://developers.deepgram.com/docs/introduction)Supported OpenAI Endpoints`/audio/transcriptions`

## Quick Start[​](#quick-start "Direct link to Quick Start")

```
from litellm import transcription
import os 

# set api keys 
os.environ["DEEPGRAM_API_KEY"]=""
audio_file =open("/path/to/audio.mp3","rb")

response = transcription(model="deepgram/nova-2",file=audio_file)

print(f"response: {response}")
```

## LiteLLM Proxy Usage[​](#litellm-proxy-usage "Direct link to LiteLLM Proxy Usage")

### Add model to config[​](#add-model-to-config "Direct link to Add model to config")

1. Add model to config.yaml

```
model_list:
-model_name: nova-2
litellm_params:
model: deepgram/nova-2
api_key: os.environ/DEEPGRAM_API_KEY
model_info:
mode: audio_transcription

general_settings:
master_key: sk-1234
```

### Start proxy[​](#start-proxy "Direct link to Start proxy")

```
litellm --config /path/to/config.yaml 

# RUNNING on http://0.0.0.0:4000
```

### Test[​](#test "Direct link to Test")

- Curl
- OpenAI

```
curl --location 'http://0.0.0.0:4000/v1/audio/transcriptions' \
--header 'Authorization: Bearer sk-1234' \
--form 'file=@"/Users/krrishdholakia/Downloads/gettysburg.wav"' \
--form 'model="nova-2"'
```