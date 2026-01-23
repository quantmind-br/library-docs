---
title: RunwayML - Text-to-Speech | liteLLM
url: https://docs.litellm.ai/docs/providers/runwayml/text-to-speech
source: sitemap
fetched_at: 2026-01-21T19:50:19.601921496-03:00
rendered_js: false
word_count: 298
summary: This document provides a comprehensive guide for integrating RunwayML's text-to-speech API with LiteLLM, covering authentication, voice mapping, and proxy configuration. It explains how LiteLLM simplifies the process by handling task polling and response transformation automatically.
tags:
    - litellm
    - runwayml
    - text-to-speech
    - api-integration
    - audio-generation
    - python
    - async-api
    - proxy-configuration
category: guide
---

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionRunwayML provides high-quality AI-powered text-to-speech with natural-sounding voicesProvider Route on LiteLLM`runwayml/`Supported Operations[`/audio/speech`](#quick-start)Link to Provider Doc[RunwayML API ↗](https://docs.dev.runwayml.com/)

LiteLLM supports RunwayML's text-to-speech API with automatic task polling, allowing you to generate natural-sounding audio from text.

## Quick Start[​](#quick-start "Direct link to Quick Start")

Basic Text-to-Speech

```
from litellm import speech
import os

os.environ["RUNWAYML_API_KEY"]="your-api-key"

response = speech(
    model="runwayml/eleven_multilingual_v2",
input="Step right up, ladies and gentlemen! Have you ever wished for a toaster that's not just a toaster but a marvel of modern ingenuity?",
    voice="alloy"
)

# Save the audio
withopen("output.mp3","wb")as f:
    f.write(response.content)
```

## Authentication[​](#authentication "Direct link to Authentication")

Set your RunwayML API key:

Set API Key

```
import os

os.environ["RUNWAYML_API_KEY"]="your-api-key"
```

## Supported Parameters[​](#supported-parameters "Direct link to Supported Parameters")

ParameterTypeRequiredDescription`model`stringYesModel to use (e.g., `runwayml/eleven_multilingual_v2`)`input`stringYesText to convert to speech`voice`string or dictYesVoice to use (OpenAI name, RunwayML preset, or voice config)

## Voice Options[​](#voice-options "Direct link to Voice Options")

### Using OpenAI Voice Names[​](#using-openai-voice-names "Direct link to Using OpenAI Voice Names")

OpenAI voice names are automatically mapped to appropriate RunwayML voices:

OpenAI Voice Names

```
from litellm import speech

# These OpenAI voice names work automatically
response = speech(
    model="runwayml/eleven_multilingual_v2",
input="Hello, world!",
    voice="alloy"# Maya - neutral, balanced female voice
)
```

**Voice Mappings:**

- `alloy` → Maya (neutral, balanced female voice)
- `echo` → James (male voice)
- `fable` → Bernard (warm, storytelling voice)
- `onyx` → Vincent (deep male voice)
- `nova` → Serene (warm, expressive female voice)
- `shimmer` → Ella (clear, friendly female voice)

### Using RunwayML Preset Voices[​](#using-runwayml-preset-voices "Direct link to Using RunwayML Preset Voices")

You can directly specify any RunwayML preset voice by passing the preset name as a string:

RunwayML Preset Names

```
from litellm import speech

# Pass the RunwayML voice name as a string
response = speech(
    model="runwayml/eleven_multilingual_v2",
input="Hello, world!",
    voice="Maya"# LiteLLM automatically formats this for RunwayML
)

# Try different RunwayML voices
response = speech(
    model="runwayml/eleven_multilingual_v2",
input="Step right up, ladies and gentlemen!",
    voice="Bernard"# Great for storytelling
)
```

**Available RunwayML Voices:**

Maya, Arjun, Serene, Bernard, Billy, Mark, Clint, Mabel, Chad, Leslie, Eleanor, Elias, Elliot, Grungle, Brodie, Sandra, Kirk, Kylie, Lara, Lisa, Malachi, Marlene, Martin, Miriam, Monster, Paula, Pip, Rusty, Ragnar, Xylar, Maggie, Jack, Katie, Noah, James, Rina, Ella, Mariah, Frank, Claudia, Niki, Vincent, Kendrick, Myrna, Tom, Wanda, Benjamin, Kiana, Rachel

tip

Simply pass the voice name as a string - LiteLLM automatically handles the internal RunwayML API format conversion.

## Async Usage[​](#async-usage "Direct link to Async Usage")

Async Text-to-Speech

```
from litellm import aspeech
import os
import asyncio

os.environ["RUNWAYML_API_KEY"]="your-api-key"

asyncdefgenerate_speech():
    response =await aspeech(
        model="runwayml/eleven_multilingual_v2",
input="This is an asynchronous text-to-speech request.",
        voice="nova"
)

withopen("output.mp3","wb")as f:
        f.write(response.content)

print("Audio generated successfully!")

asyncio.run(generate_speech())
```

## LiteLLM Proxy Usage[​](#litellm-proxy-usage "Direct link to LiteLLM Proxy Usage")

Add RunwayML to your proxy configuration:

config.yaml

```
model_list:
-model_name: runway-tts
litellm_params:
model: runwayml/eleven_multilingual_v2
api_key: os.environ/RUNWAYML_API_KEY
```

Start the proxy:

```
litellm --config /path/to/config.yaml
```

Generate speech through the proxy:

Proxy Request

```
curl --location 'http://localhost:4000/v1/audio/speech' \
--header 'Content-Type: application/json' \
--header 'x-litellm-api-key: sk-1234' \
--data '{
    "model": "runwayml/eleven_multilingual_v2",
    "input": "Hello from the LiteLLM proxy!",
    "voice": "alloy"
}'
```

With RunwayML-specific voice:

Proxy Request with RunwayML Voice

```
curl --location 'http://localhost:4000/v1/audio/speech' \
--header 'Content-Type: application/json' \
--header 'x-litellm-api-key: sk-1234' \
--data '{
    "model": "runwayml/eleven_multilingual_v2",
    "input": "Hello with a custom RunwayML voice!",
    "voice": "Bernard"
}'
```

## Supported Models[​](#supported-models "Direct link to Supported Models")

ModelDescription`runwayml/eleven_multilingual_v2`High-quality multilingual text-to-speech

## Cost Tracking[​](#cost-tracking "Direct link to Cost Tracking")

LiteLLM automatically tracks RunwayML text-to-speech costs:

Cost Tracking

```
from litellm import speech, completion_cost

response = speech(
    model="runwayml/eleven_multilingual_v2",
input="Hello, world!",
    voice="alloy"
)

cost = completion_cost(completion_response=response)
print(f"Text-to-speech cost: ${cost}")
```

## Supported Features[​](#supported-features "Direct link to Supported Features")

FeatureSupportedText-to-Speech✅Cost Tracking✅Logging✅Fallbacks✅Load Balancing✅50+ Voice Presets✅

## How It Works[​](#how-it-works "Direct link to How It Works")

RunwayML uses an asynchronous task-based API pattern. LiteLLM handles the polling and response transformation automatically.

### Complete Flow Diagram[​](#complete-flow-diagram "Direct link to Complete Flow Diagram")