---
title: OpenAI - Text-to-speech | liteLLM
url: https://docs.litellm.ai/docs/providers/openai/text_to_speech
source: sitemap
fetched_at: 2026-01-21T19:50:01.105985581-03:00
rendered_js: false
word_count: 95
summary: This document provides instructions for implementing text-to-speech and audio transcription services using the LiteLLM Python SDK and Proxy server. It covers synchronous and asynchronous usage, supported models, and enterprise configuration options like file size limits.
tags:
    - litellm
    - text-to-speech
    - python-sdk
    - audio-transcription
    - openai-compatible
    - proxy-server
category: guide
---

## Overview[​](#overview "Direct link to Overview")

FeatureSupportedNotesCost Tracking✅Works with all supported modelsLogging✅Works across all integrationsEnd-user Tracking✅Fallbacks✅Works between supported modelsLoadbalancing✅Works between supported modelsGuardrails✅Applies to input textSupported Modelstts-1, tts-1-hd, gpt-4o-mini-tts

## **LiteLLM Python SDK Usage**[​](#litellm-python-sdk-usage "Direct link to litellm-python-sdk-usage")

### Quick Start[​](#quick-start "Direct link to Quick Start")

```
from pathlib import Path
from litellm import speech
import os 

os.environ["OPENAI_API_KEY"]="sk-.."

speech_file_path = Path(__file__).parent /"speech.mp3"
response = speech(
        model="openai/tts-1",
        voice="alloy",
input="the quick brown fox jumped over the lazy dogs",
)
response.stream_to_file(speech_file_path)
```

### Async Usage[​](#async-usage "Direct link to Async Usage")

```
from litellm import aspeech
from pathlib import Path
import os, asyncio

os.environ["OPENAI_API_KEY"]="sk-.."

asyncdeftest_async_speech():
    speech_file_path = Path(__file__).parent /"speech.mp3"
    response =await aspeech(
            model="openai/tts-1",
            voice="alloy",
input="the quick brown fox jumped over the lazy dogs",
            api_base=None,
            api_key=None,
            organization=None,
            project=None,
            max_retries=1,
            timeout=600,
            client=None,
            optional_params={},
)
    response.stream_to_file(speech_file_path)

asyncio.run(test_async_speech())
```

## **LiteLLM Proxy Usage**[​](#litellm-proxy-usage "Direct link to litellm-proxy-usage")

LiteLLM provides an openai-compatible `/audio/speech` endpoint for Text-to-speech calls.

```
curl http://0.0.0.0:4000/v1/audio/speech \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tts-1",
    "input": "The quick brown fox jumped over the lazy dog.",
    "voice": "alloy"
  }' \
  --output speech.mp3
```

**Setup**

```
- model_name: tts
  litellm_params:
    model: openai/tts-1
    api_key: os.environ/OPENAI_API_KEY
```

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

## Supported Models[​](#supported-models "Direct link to Supported Models")

ModelExampletts-1speech(model="tts-1", voice="alloy", input="Hello, world!")tts-1-hdspeech(model="tts-1-hd", voice="alloy", input="Hello, world!")gpt-4o-mini-ttsspeech(model="gpt-4o-mini-tts", voice="alloy", input="Hello, world!")

## ✨ Enterprise LiteLLM Proxy - Set Max Request File Size[​](#-enterprise-litellm-proxy---set-max-request-file-size "Direct link to ✨ Enterprise LiteLLM Proxy - Set Max Request File Size")

Use this when you want to limit the file size for requests sent to `audio/transcriptions`

```
-model_name: whisper
litellm_params:
model: whisper-1
api_key: sk-*******
max_file_size_mb:0.00001# 👈 max file size in MB  (Set this intentionally very small for testing)
model_info:
mode: audio_transcription
```

Make a test Request with a valid file

```
curl --location 'http://localhost:4000/v1/audio/transcriptions' \
--header 'Authorization: Bearer sk-1234' \
--form 'file=@"/Users/ishaanjaffer/Github/litellm/tests/gettysburg.wav"' \
--form 'model="whisper"'
```

Expect to see the follow response

```
{"error":{"message":"File size is too large. Please check your file size. Passed file size: 0.7392807006835938 MB. Max file size: 0.0001 MB","type":"bad_request","param":"file","code":500}}%  
```