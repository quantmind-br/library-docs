---
title: /audio/speech | liteLLM
url: https://docs.litellm.ai/docs/text_to_speech
source: sitemap
fetched_at: 2026-01-21T19:54:54.294561025-03:00
rendered_js: false
word_count: 224
summary: This document provides instructions for implementing and configuring Text-to-Speech (TTS) functionality through LiteLLM's Python SDK and Proxy server across various AI providers.
tags:
    - litellm
    - text-to-speech
    - tts
    - python-sdk
    - api-proxy
    - gemini
    - vertex-ai
    - async-usage
category: guide
---

## Overview[​](#overview "Direct link to Overview")

FeatureSupportedNotesCost Tracking✅Works with all supported modelsLogging✅Works across all integrationsEnd-user Tracking✅Fallbacks✅Works between supported modelsLoadbalancing✅Works between supported modelsGuardrails✅Applies to input text (non-streaming only)Supported ProvidersOpenAI, Azure OpenAI, Vertex AI, AWS Polly, ElevenLabs , MiniMax

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

## **Supported Providers**[​](#supported-providers "Direct link to supported-providers")

ProviderLink to UsageOpenAI[Usage](#quick-start)Azure OpenAI[Usage](https://docs.litellm.ai/docs/providers/azure#azure-text-to-speech-tts)Azure AI Speech Service (AVA)[Usage](https://docs.litellm.ai/docs/providers/azure_ai_speech)AWS Polly[Usage](#aws-polly-text-to-speech)Vertex AI[Usage](https://docs.litellm.ai/docs/providers/vertex#text-to-speech-apis)Gemini[Usage](#gemini-text-to-speech)ElevenLabs[Usage](https://docs.litellm.ai/docs/providers/elevenlabs#text-to-speech-tts)MiniMax[Usage](https://docs.litellm.ai/docs/providers/minimax#minimax---text-to-speech)

## `/audio/speech` to `/chat/completions` Bridge[​](#audiospeech-to-chatcompletions-bridge "Direct link to audiospeech-to-chatcompletions-bridge")

LiteLLM allows you to use `/chat/completions` models to generate speech through the `/audio/speech` endpoint. This is useful for models like Gemini's TTS-enabled models that are only accessible via `/chat/completions`.

### Gemini Text-to-Speech[​](#gemini-text-to-speech "Direct link to Gemini Text-to-Speech")

#### Python SDK Usage[​](#python-sdk-usage "Direct link to Python SDK Usage")

Gemini Text-to-Speech SDK Usage

```
import litellm
import os

# Set your Gemini API key
os.environ["GEMINI_API_KEY"]="your-gemini-api-key"

deftest_audio_speech_gemini():
    result = litellm.speech(
        model="gemini/gemini-2.5-flash-preview-tts",
input="the quick brown fox jumped over the lazy dogs",
        api_key=os.getenv("GEMINI_API_KEY"),
)

# Save to file
from pathlib import Path
    speech_file_path = Path(__file__).parent /"gemini_speech.mp3"
    result.stream_to_file(speech_file_path)
print(f"Audio saved to {speech_file_path}")

test_audio_speech_gemini()
```

#### Async Usage[​](#async-usage-1 "Direct link to Async Usage")

Gemini Text-to-Speech Async Usage

```
import litellm
import asyncio
import os
from pathlib import Path

os.environ["GEMINI_API_KEY"]="your-gemini-api-key"

asyncdeftest_async_gemini_speech():
    speech_file_path = Path(__file__).parent /"gemini_speech.mp3"
    response =await litellm.aspeech(
        model="gemini/gemini-2.5-flash-preview-tts",
input="the quick brown fox jumped over the lazy dogs",
        api_key=os.getenv("GEMINI_API_KEY"),
)
    response.stream_to_file(speech_file_path)
print(f"Audio saved to {speech_file_path}")

asyncio.run(test_async_gemini_speech())
```

#### LiteLLM Proxy Usage[​](#litellm-proxy-usage-1 "Direct link to LiteLLM Proxy Usage")

**Setup Config:**

Gemini Proxy Configuration

```
model_list:
-model_name: gemini-tts
litellm_params:
model: gemini/gemini-2.5-flash-preview-tts
api_key: os.environ/GEMINI_API_KEY
```

**Start Proxy:**

Start LiteLLM Proxy

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

**Make Request:**

Gemini TTS Request

```
curl http://0.0.0.0:4000/v1/audio/speech \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-tts",
    "input": "The quick brown fox jumped over the lazy dog.",
    "voice": "alloy"
  }' \
  --output gemini_speech.mp3
```

### Vertex AI Text-to-Speech[​](#vertex-ai-text-to-speech "Direct link to Vertex AI Text-to-Speech")

#### Python SDK Usage[​](#python-sdk-usage-1 "Direct link to Python SDK Usage")

Vertex AI Text-to-Speech SDK Usage

```
import litellm
import os
from pathlib import Path

# Set your Google credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="path/to/service-account.json"

deftest_audio_speech_vertex():
    result = litellm.speech(
        model="vertex_ai/gemini-2.5-flash-preview-tts",
input="the quick brown fox jumped over the lazy dogs",
)

# Save to file
    speech_file_path = Path(__file__).parent /"vertex_speech.mp3"
    result.stream_to_file(speech_file_path)
print(f"Audio saved to {speech_file_path}")

test_audio_speech_vertex()
```

#### LiteLLM Proxy Usage[​](#litellm-proxy-usage-2 "Direct link to LiteLLM Proxy Usage")

**Setup Config:**

Vertex AI Proxy Configuration

```
model_list:
-model_name: vertex-tts
litellm_params:
model: vertex_ai/gemini-2.5-flash-preview-tts
vertex_project: your-project-id
vertex_location: us-central1
```

**Make Request:**

Vertex AI TTS Request

```
curl http://0.0.0.0:4000/v1/audio/speech \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "vertex-tts",
    "input": "The quick brown fox jumped over the lazy dog.",
    "voice": "en-US-Wavenet-D"
  }' \
  --output vertex_speech.mp3
```

### AWS Polly Text-to-Speech[​](#aws-polly-text-to-speech "Direct link to AWS Polly Text-to-Speech")

AWS Polly provides neural and standard text-to-speech engines with support for multiple voices and languages.

See the [AWS Polly provider documentation](https://docs.litellm.ai/docs/providers/aws_polly) for detailed usage examples.

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