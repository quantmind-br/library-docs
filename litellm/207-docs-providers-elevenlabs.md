---
title: ElevenLabs | liteLLM
url: https://docs.litellm.ai/docs/providers/elevenlabs
source: sitemap
fetched_at: 2026-01-21T19:48:56.077942777-03:00
rendered_js: false
word_count: 345
summary: This document provides instructions for integrating ElevenLabs speech-to-text and text-to-speech services using the LiteLLM Python SDK and proxy server.
tags:
    - elevenlabs
    - litellm
    - speech-to-text
    - text-to-speech
    - audio-transcription
    - voice-mapping
category: guide
---

ElevenLabs provides high-quality AI voice technology, including speech-to-text capabilities through their transcription API.

PropertyDetailsDescriptionElevenLabs offers advanced AI voice technology with speech-to-text transcription and text-to-speech capabilities that support multiple languages and speaker diarization.Provider Route on LiteLLM`elevenlabs/`Provider Doc[ElevenLabs API ↗](https://elevenlabs.io/docs/api-reference)Supported Endpoints`/audio/transcriptions`, `/audio/speech`

## Quick Start[​](#quick-start "Direct link to Quick Start")

### LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

- Basic Usage
- Advanced Features
- Async Usage

Basic audio transcription with ElevenLabs

```
import litellm

# Transcribe audio file
withopen("audio.mp3","rb")as audio_file:
    response = litellm.transcription(
        model="elevenlabs/scribe_v1",
file=audio_file,
        api_key="your-elevenlabs-api-key"# or set ELEVENLABS_API_KEY env var
)

print(response.text)
```

### LiteLLM Proxy[​](#litellm-proxy "Direct link to LiteLLM Proxy")

#### 1. Configure your proxy[​](#1-configure-your-proxy "Direct link to 1. Configure your proxy")

- config.yaml
- Environment Variables

ElevenLabs configuration in config.yaml

```
model_list:
-model_name: elevenlabs-transcription
litellm_params:
model: elevenlabs/scribe_v1
api_key: os.environ/ELEVENLABS_API_KEY

general_settings:
master_key: your-master-key
```

#### 2. Start the proxy[​](#2-start-the-proxy "Direct link to 2. Start the proxy")

Start LiteLLM proxy server

```
litellm --config config.yaml

# Proxy will be available at http://localhost:4000
```

#### 3. Make transcription requests[​](#3-make-transcription-requests "Direct link to 3. Make transcription requests")

- Curl
- OpenAI Python SDK
- JavaScript/Node.js

Audio transcription with curl

```
curl http://localhost:4000/v1/audio/transcriptions \
  -H "Authorization: Bearer $LITELLM_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F file="@audio.mp3" \
  -F model="elevenlabs-transcription" \
  -F language="en" \
  -F temperature="0.3"
```

## Response Format[​](#response-format "Direct link to Response Format")

ElevenLabs returns transcription responses in OpenAI-compatible format:

Example transcription response

```
{
"text":"Hello, this is a sample transcription with multiple speakers.",
"task":"transcribe",
"language":"en",
"words":[
{
"word":"Hello",
"start":0.0,
"end":0.5
},
{
"word":"this",
"start":0.5,
"end":0.8
}
]
}
```

### Common Issues[​](#common-issues "Direct link to Common Issues")

1. **Invalid API Key**: Ensure `ELEVENLABS_API_KEY` is set correctly

* * *

## Text-to-Speech (TTS)[​](#text-to-speech-tts "Direct link to Text-to-Speech (TTS)")

ElevenLabs provides high-quality text-to-speech capabilities through their TTS API, supporting multiple voices, languages, and audio formats.

### Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionConvert text to natural-sounding speech using ElevenLabs' advanced TTS modelsProvider Route on LiteLLM`elevenlabs/`Supported Operations`/audio/speech`Link to Provider Doc[ElevenLabs TTS API ↗](https://elevenlabs.io/docs/api-reference/text-to-speech)

### Quick Start[​](#quick-start-1 "Direct link to Quick Start")

#### LiteLLM Python SDK[​](#litellm-python-sdk-1 "Direct link to LiteLLM Python SDK")

ElevenLabs Text-to-Speech with SDK

```
import litellm
import os

os.environ["ELEVENLABS_API_KEY"]="your-elevenlabs-api-key"

# Basic usage with voice mapping
audio = litellm.speech(
    model="elevenlabs/eleven_multilingual_v2",
input="Testing ElevenLabs speech from LiteLLM.",
    voice="alloy",# Maps to ElevenLabs voice ID automatically
)

# Save audio to file
withopen("test_output.mp3","wb")as f:
    f.write(audio.read())
```

#### Advanced Usage: Overriding Parameters and ElevenLabs-Specific Features[​](#advanced-usage-overriding-parameters-and-elevenlabs-specific-features "Direct link to Advanced Usage: Overriding Parameters and ElevenLabs-Specific Features")

Advanced TTS with custom parameters

```
import litellm
import os

os.environ["ELEVENLABS_API_KEY"]="your-elevenlabs-api-key"

# Example showing parameter overriding and ElevenLabs-specific parameters
audio = litellm.speech(
    model="elevenlabs/eleven_multilingual_v2",
input="Testing ElevenLabs speech from LiteLLM.",
    voice="alloy",# Can use mapped voice name or raw ElevenLabs voice_id
    response_format="pcm",# Maps to ElevenLabs output_format
    speed=1.1,# Maps to voice_settings.speed
# ElevenLabs-specific parameters - passed directly to API
    pronunciation_dictionary_locators=[
{"pronunciation_dictionary_id":"dict_123","version_id":"v1"}
],
    model_id="eleven_multilingual_v2",# Override model if needed
)

# Save audio to file
withopen("test_output.mp3","wb")as f:
    f.write(audio.read())
```

### Voice Mapping[​](#voice-mapping "Direct link to Voice Mapping")

LiteLLM automatically maps common OpenAI voice names to ElevenLabs voice IDs:

OpenAI VoiceElevenLabs Voice IDDescription`alloy``21m00Tcm4TlvDq8ikWAM`Rachel - Neutral and balanced`amber``5Q0t7uMcjvnagumLfvZi`Paul - Warm and friendly`ash``AZnzlk1XvdvUeBnXmlld`Domi - Energetic`august``D38z5RcWu1voky8WS1ja`Fin - Professional`blue``2EiwWnXFnvU5JabPnv8n`Clyde - Deep and authoritative`coral``9BWtsMINqrJLrRacOk9x`Aria - Expressive`lily``EXAVITQu4vr4xnSDxMaL`Sarah - Friendly`onyx``29vD33N1CtxCmqQRPOHJ`Drew - Strong`sage``CwhRBWXzGAHq8TQ4Fs17`Roger - Calm`verse``CYw3kZ02Hs0563khs1Fj`Dave - Conversational

**Using Custom Voice IDs**: You can also pass any ElevenLabs voice ID directly. If the voice name is not in the mapping, LiteLLM will use it as-is:

Using custom ElevenLabs voice ID

```
audio = litellm.speech(
    model="elevenlabs/eleven_multilingual_v2",
input="Testing with a custom voice.",
    voice="21m00Tcm4TlvDq8ikWAM",# Direct ElevenLabs voice ID
)
```

### Response Format Mapping[​](#response-format-mapping "Direct link to Response Format Mapping")

LiteLLM maps OpenAI response formats to ElevenLabs output formats:

OpenAI FormatElevenLabs Format`mp3``mp3_44100_128``pcm``pcm_44100``opus``opus_48000_128`

You can also pass ElevenLabs-specific output formats directly using the `output_format` parameter.

### Supported Parameters[​](#supported-parameters "Direct link to Supported Parameters")

All Supported Parameters

```
audio = litellm.speech(
    model="elevenlabs/eleven_multilingual_v2",# Required
input="Text to convert to speech",# Required
    voice="alloy",# Required: Voice selection (mapped or raw ID)
    response_format="mp3",# Optional: Audio format (mp3, pcm, opus)
    speed=1.0,# Optional: Speech speed (maps to voice_settings.speed)
# ElevenLabs-specific parameters (passed directly):
    model_id="eleven_multilingual_v2",# Optional: Override model
    voice_settings={# Optional: Voice customization
"stability":0.5,
"similarity_boost":0.75,
"speed":1.0
},
    pronunciation_dictionary_locators=[# Optional: Custom pronunciation
{"pronunciation_dictionary_id":"dict_123","version_id":"v1"}
],
)
```

### LiteLLM Proxy[​](#litellm-proxy-1 "Direct link to LiteLLM Proxy")

#### 1. Configure your proxy[​](#1-configure-your-proxy-1 "Direct link to 1. Configure your proxy")

ElevenLabs TTS configuration in config.yaml

```
model_list:
-model_name: elevenlabs-tts
litellm_params:
model: elevenlabs/eleven_multilingual_v2
api_key: os.environ/ELEVENLABS_API_KEY

general_settings:
master_key: your-master-key
```

#### 2. Make TTS requests[​](#2-make-tts-requests "Direct link to 2. Make TTS requests")

##### Simple Usage (OpenAI Parameters)[​](#simple-usage-openai-parameters "Direct link to Simple Usage (OpenAI Parameters)")

You can use standard OpenAI-compatible parameters without any provider-specific configuration:

Simple TTS request with curl

```
curl http://localhost:4000/v1/audio/speech \
  -H "Authorization: Bearer $LITELLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "elevenlabs-tts",
    "input": "Testing ElevenLabs speech via the LiteLLM proxy.",
    "voice": "alloy",
    "response_format": "mp3"
  }' \
  --output speech.mp3
```

Simple TTS with OpenAI SDK

```
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:4000",
    api_key="your-litellm-api-key"
)

response = client.audio.speech.create(
    model="elevenlabs-tts",
input="Testing ElevenLabs speech via the LiteLLM proxy.",
    voice="alloy",
    response_format="mp3"
)

# Save audio
withopen("speech.mp3","wb")as f:
    f.write(response.content)
```

##### Advanced Usage (ElevenLabs-Specific Parameters)[​](#advanced-usage-elevenlabs-specific-parameters "Direct link to Advanced Usage (ElevenLabs-Specific Parameters)")

**Note**: When using the proxy, provider-specific parameters (like `pronunciation_dictionary_locators`, `voice_settings`, etc.) must be passed in the `extra_body` field.

Advanced TTS request with curl

```
curl http://localhost:4000/v1/audio/speech \
  -H "Authorization: Bearer $LITELLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "elevenlabs-tts",
    "input": "Testing ElevenLabs speech via the LiteLLM proxy.",
    "voice": "alloy",
    "response_format": "pcm",
    "extra_body": {
      "pronunciation_dictionary_locators": [
          {"pronunciation_dictionary_id": "dict_123", "version_id": "v1"}
      ],
      "voice_settings": {
        "speed": 1.1,
        "stability": 0.5,
        "similarity_boost": 0.75
      }
    }
  }' \
  --output speech.mp3
```

Advanced TTS with OpenAI SDK

```
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:4000",
    api_key="your-litellm-api-key"
)

response = client.audio.speech.create(
    model="elevenlabs-tts",
input="Testing ElevenLabs speech via the LiteLLM proxy.",
    voice="alloy",
    response_format="pcm",
    extra_body={
"pronunciation_dictionary_locators":[
{"pronunciation_dictionary_id":"dict_123","version_id":"v1"}
],
"voice_settings":{
"speed":1.1,
"stability":0.5,
"similarity_boost":0.75
}
}
)

# Save audio
withopen("speech.mp3","wb")as f:
    f.write(response.content)
```