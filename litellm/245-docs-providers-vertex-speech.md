---
title: Vertex AI Text to Speech | liteLLM
url: https://docs.litellm.ai/docs/providers/vertex_speech
source: sitemap
fetched_at: 2026-01-21T19:50:50.584611158-03:00
rendered_js: false
word_count: 264
summary: This document provides a comprehensive guide for integrating Google Cloud Text-to-Speech (Chirp3 HD) and Gemini TTS using LiteLLM's Python SDK and AI Gateway, covering configuration, voice mapping, and SSML support.
tags:
    - google-cloud
    - vertex-ai
    - text-to-speech
    - litellm
    - gemini-tts
    - audio-generation
    - ssml
category: guide
---

PropertyDetailsDescriptionGoogle Cloud Text-to-Speech with Chirp3 HD voices and Gemini TTSProvider Route on LiteLLM`vertex_ai/chirp` (Chirp), `vertex_ai/gemini-*-tts` (Gemini)

## Chirp3 HD Voices[​](#chirp3-hd-voices "Direct link to Chirp3 HD Voices")

Google Cloud Text-to-Speech API with high-quality Chirp3 HD voices.

### Quick Start[​](#quick-start "Direct link to Quick Start")

#### LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

Chirp3 Quick Start

```
from litellm import speech
from pathlib import Path

speech_file_path = Path(__file__).parent /"speech.mp3"
response = speech(
    model="vertex_ai/chirp",
    voice="alloy",# OpenAI voice name - automatically mapped
input="Hello, this is Vertex AI Text to Speech",
    vertex_project="your-project-id",
    vertex_location="us-central1",
)
response.stream_to_file(speech_file_path)
```

#### LiteLLM AI Gateway[​](#litellm-ai-gateway "Direct link to LiteLLM AI Gateway")

**1. Setup config.yaml**

config.yaml

```
model_list:
-model_name: vertex-tts
litellm_params:
model: vertex_ai/chirp
vertex_project:"your-project-id"
vertex_location:"us-central1"
vertex_credentials:"/path/to/service_account.json"
```

**2. Start the proxy**

Start LiteLLM Proxy

```
litellm --config /path/to/config.yaml
```

**3. Make requests**

- curl
- OpenAI Python SDK

Chirp3 Quick Start

```
curl http://0.0.0.0:4000/v1/audio/speech \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "vertex-tts",
    "voice": "alloy",
    "input": "Hello, this is Vertex AI Text to Speech"
  }' \
  --output speech.mp3
```

### Voice Mapping[​](#voice-mapping "Direct link to Voice Mapping")

LiteLLM maps OpenAI voice names to Google Cloud voices. You can use either OpenAI voices or Google Cloud voices directly.

OpenAI VoiceGoogle Cloud Voice`alloy`en-US-Studio-O`echo`en-US-Studio-M`fable`en-GB-Studio-B`onyx`en-US-Wavenet-D`nova`en-US-Studio-O`shimmer`en-US-Wavenet-F

### Using Google Cloud Voices Directly[​](#using-google-cloud-voices-directly "Direct link to Using Google Cloud Voices Directly")

#### LiteLLM Python SDK[​](#litellm-python-sdk-1 "Direct link to LiteLLM Python SDK")

Chirp3 HD Voice

```
from litellm import speech

# Pass Chirp3 HD voice name directly
response = speech(
    model="vertex_ai/chirp",
    voice="en-US-Chirp3-HD-Charon",
input="Hello with a Chirp3 HD voice",
    vertex_project="your-project-id",
)
response.stream_to_file("speech.mp3")
```

Voice as Dict (Multilingual)

```
from litellm import speech

# Pass as dict for full control over language and voice
response = speech(
    model="vertex_ai/chirp",
    voice={
"languageCode":"de-DE",
"name":"de-DE-Chirp3-HD-Charon",
},
input="Hallo, dies ist ein Test",
    vertex_project="your-project-id",
)
response.stream_to_file("speech.mp3")
```

#### LiteLLM AI Gateway[​](#litellm-ai-gateway-1 "Direct link to LiteLLM AI Gateway")

- curl
- OpenAI Python SDK

Chirp3 HD Voice

```
curl http://0.0.0.0:4000/v1/audio/speech \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "vertex-tts",
    "voice": "en-US-Chirp3-HD-Charon",
    "input": "Hello with a Chirp3 HD voice"
  }' \
  --output speech.mp3
```

Voice as Dict (Multilingual)

```
curl http://0.0.0.0:4000/v1/audio/speech \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "vertex-tts",
    "voice": {"languageCode": "de-DE", "name": "de-DE-Chirp3-HD-Charon"},
    "input": "Hallo, dies ist ein Test"
  }' \
  --output speech.mp3
```

Browse available voices: [Google Cloud Text-to-Speech Console](https://console.cloud.google.com/vertex-ai/generative/speech/text-to-speech)

### Passing Raw SSML[​](#passing-raw-ssml "Direct link to Passing Raw SSML")

LiteLLM auto-detects SSML when your input contains `<speak>` tags and passes it through unchanged.

#### LiteLLM Python SDK[​](#litellm-python-sdk-2 "Direct link to LiteLLM Python SDK")

SSML Input

```
from litellm import speech

ssml ="""
<speak>
    <p>Hello, world!</p>
    <p>This is a test of the <break strength="medium" /> text-to-speech API.</p>
</speak>
"""

response = speech(
    model="vertex_ai/chirp",
    voice="en-US-Studio-O",
input=ssml,# Auto-detected as SSML
    vertex_project="your-project-id",
)
response.stream_to_file("speech.mp3")
```

Force SSML Mode

```
from litellm import speech

# Force SSML mode with use_ssml=True
response = speech(
    model="vertex_ai/chirp",
    voice="en-US-Studio-O",
input="<speak><prosody rate='slow'>Speaking slowly</prosody></speak>",
    use_ssml=True,
    vertex_project="your-project-id",
)
response.stream_to_file("speech.mp3")
```

#### LiteLLM AI Gateway[​](#litellm-ai-gateway-2 "Direct link to LiteLLM AI Gateway")

- curl
- OpenAI Python SDK

SSML Input

```
curl http://0.0.0.0:4000/v1/audio/speech \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "vertex-tts",
    "voice": "en-US-Studio-O",
    "input": "<speak><p>Hello!</p><break time=\"500ms\"/><p>How are you?</p></speak>"
  }' \
  --output speech.mp3
```

### Supported Parameters[​](#supported-parameters "Direct link to Supported Parameters")

ParameterDescriptionValues`voice`Voice selectionOpenAI voice, Google Cloud voice name, or dict`input`Text to convertPlain text or SSML`speed`Speaking rate0.25 to 4.0 (default: 1.0)`response_format`Audio format`mp3`, `opus`, `wav`, `pcm`, `flac``use_ssml`Force SSML mode`True` / `False`

### Async Usage[​](#async-usage "Direct link to Async Usage")

Async Speech Generation

```
import asyncio
from litellm import aspeech

asyncdefmain():
    response =await aspeech(
        model="vertex_ai/chirp",
        voice="alloy",
input="Hello from async",
        vertex_project="your-project-id",
)
    response.stream_to_file("speech.mp3")

asyncio.run(main())
```

* * *

## Gemini TTS[​](#gemini-tts "Direct link to Gemini TTS")

Gemini models with audio output capabilities using the chat completions API.

warning

**Limitations:**

- Only supports `pcm16` audio format
- Streaming not yet supported
- Must set `modalities: ["audio"]`

### Quick Start[​](#quick-start-1 "Direct link to Quick Start")

#### LiteLLM Python SDK[​](#litellm-python-sdk-3 "Direct link to LiteLLM Python SDK")

Gemini TTS Quick Start

```
from litellm import completion
import json

# Load credentials
withopen('path/to/service_account.json','r')asfile:
    vertex_credentials = json.dumps(json.load(file))

response = completion(
    model="vertex_ai/gemini-2.5-flash-preview-tts",
    messages=[{"role":"user","content":"Say hello in a friendly voice"}],
    modalities=["audio"],
    audio={
"voice":"Kore",
"format":"pcm16"
},
    vertex_credentials=vertex_credentials
)
print(response)
```

#### LiteLLM AI Gateway[​](#litellm-ai-gateway-3 "Direct link to LiteLLM AI Gateway")

**1. Setup config.yaml**

config.yaml

```
model_list:
-model_name: gemini-tts
litellm_params:
model: vertex_ai/gemini-2.5-flash-preview-tts
vertex_project:"your-project-id"
vertex_location:"us-central1"
vertex_credentials:"/path/to/service_account.json"
```

**2. Start the proxy**

Start LiteLLM Proxy

```
litellm --config /path/to/config.yaml
```

**3. Make requests**

- curl
- OpenAI Python SDK

Gemini TTS Request

```
curl http://0.0.0.0:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "gemini-tts",
    "messages": [{"role": "user", "content": "Say hello in a friendly voice"}],
    "modalities": ["audio"],
    "audio": {"voice": "Kore", "format": "pcm16"}
  }'
```

### Supported Models[​](#supported-models "Direct link to Supported Models")

- `vertex_ai/gemini-2.5-flash-preview-tts`
- `vertex_ai/gemini-2.5-pro-preview-tts`

See [Gemini TTS documentation](https://ai.google.dev/gemini-api/docs/speech-generation) for available voices.

### Advanced Usage[​](#advanced-usage "Direct link to Advanced Usage")

Gemini TTS with System Prompt

```
from litellm import completion

response = completion(
    model="vertex_ai/gemini-2.5-pro-preview-tts",
    messages=[
{"role":"system","content":"You are a helpful assistant that speaks clearly."},
{"role":"user","content":"Explain quantum computing in simple terms"}
],
    modalities=["audio"],
    audio={"voice":"Charon","format":"pcm16"},
    temperature=0.7,
    max_tokens=150,
    vertex_credentials=vertex_credentials
)
```