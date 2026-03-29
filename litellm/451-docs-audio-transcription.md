---
title: /audio/transcriptions | liteLLM
url: https://docs.litellm.ai/docs/audio_transcription
source: sitemap
fetched_at: 2026-01-21T19:44:06.509526448-03:00
rendered_js: false
word_count: 125
summary: This guide explains how to implement audio transcription using LiteLLM, covering supported providers, proxy configuration, and advanced features like model fallbacks.
tags:
    - litellm
    - audio-transcription
    - speech-to-text
    - api-proxy
    - model-fallbacks
    - python-sdk
category: guide
---

## Overview[​](#overview "Direct link to Overview")

FeatureSupportedNotesCost Tracking✅Works with all supported modelsLogging✅Works across all integrationsEnd-user Tracking✅Fallbacks✅Works between supported modelsLoadbalancing✅Works between supported modelsGuardrails✅Applies to output transcribed text (non-streaming only)Supported Providers`openai`, `azure`, `vertex_ai`, `gemini`, `deepgram`, `groq`, `fireworks_ai`, `ovhcloud`

## Quick Start[​](#quick-start "Direct link to Quick Start")

### LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

Python SDK Example

```
from litellm import transcription
import os 

# set api keys 
os.environ["OPENAI_API_KEY"]=""
audio_file =open("/path/to/audio.mp3","rb")

response = transcription(model="whisper",file=audio_file)

print(f"response: {response}")
```

### LiteLLM Proxy[​](#litellm-proxy "Direct link to LiteLLM Proxy")

### Add model to config[​](#add-model-to-config "Direct link to Add model to config")

- OpenAI
- OpenAI + Azure

OpenAI Configuration

```
model_list:
-model_name: whisper
litellm_params:
model: whisper-1
api_key: os.environ/OPENAI_API_KEY
model_info:
mode: audio_transcription

general_settings:
master_key: sk-1234
```

### Start proxy[​](#start-proxy "Direct link to Start proxy")

Start Proxy Server

```
litellm --config /path/to/config.yaml 

# RUNNING on http://0.0.0.0:8000
```

### Test[​](#test "Direct link to Test")

- Curl
- OpenAI Python SDK

Test with cURL

```
curl --location 'http://0.0.0.0:8000/v1/audio/transcriptions' \
--header 'Authorization: Bearer sk-1234' \
--form 'file=@"/Users/krrishdholakia/Downloads/gettysburg.wav"' \
--form 'model="whisper"'
```

## Supported Providers[​](#supported-providers "Direct link to Supported Providers")

- OpenAI
- Azure
- [Fireworks AI](https://docs.litellm.ai/docs/providers/fireworks_ai#audio-transcription)
- [Groq](https://docs.litellm.ai/docs/providers/groq#speech-to-text---whisper)
- [Deepgram](https://docs.litellm.ai/docs/providers/deepgram)
- [OVHcloud AI Endpoints](https://docs.litellm.ai/docs/providers/ovhcloud)

* * *

## Fallbacks[​](#fallbacks "Direct link to Fallbacks")

You can configure fallbacks for audio transcription to automatically retry with different models if the primary model fails.

- Curl
- OpenAI Python SDK

Test with cURL and Fallbacks

```
curl --location 'http://0.0.0.0:4000/v1/audio/transcriptions' \
--header 'Authorization: Bearer sk-1234' \
--form 'file=@"gettysburg.wav"' \
--form 'model="groq/whisper-large-v3"' \
--form 'fallbacks[]="openai/whisper-1"'
```

### Testing Fallbacks[​](#testing-fallbacks "Direct link to Testing Fallbacks")

You can test your fallback configuration using `mock_testing_fallbacks=true` to simulate failures:

- Curl
- OpenAI Python SDK

Test Fallbacks with Mock Testing

```
curl --location 'http://0.0.0.0:4000/v1/audio/transcriptions' \
--header 'Authorization: Bearer sk-1234' \
--form 'file=@"gettysburg.wav"' \
--form 'model="groq/whisper-large-v3"' \
--form 'fallbacks[]="openai/whisper-1"' \
--form 'mock_testing_fallbacks=true'
```