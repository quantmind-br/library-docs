---
title: MiniMax | liteLLM
url: https://docs.litellm.ai/docs/providers/minimax
source: sitemap
fetched_at: 2026-01-21T19:49:41.817246086-03:00
rendered_js: false
word_count: 427
summary: This document explains how to integrate MiniMax language models using LiteLLM, detailing support for both Anthropic and OpenAI-compatible API specifications, including tool calling and thinking features.
tags:
    - minimax
    - litellm
    - anthropic-api
    - openai-api
    - tool-calling
    - api-integration
    - llm-proxy
category: guide
---

## MiniMax - v1/messages

## Overview[​](#overview "Direct link to Overview")

Litellm provides anthropic specs compatible support for minmax

## Supported Models[​](#supported-models "Direct link to Supported Models")

MiniMax offers three models through their Anthropic-compatible API:

ModelDescriptionInput CostOutput CostPrompt Caching ReadPrompt Caching Write**MiniMax-M2.1**Powerful Multi-Language Programming with Enhanced Programming Experience (~60 tps)$0.3/M tokens$1.2/M tokens$0.03/M tokens$0.375/M tokens**MiniMax-M2.1-lightning**Faster and More Agile (~100 tps)$0.3/M tokens$2.4/M tokens$0.03/M tokens$0.375/M tokens**MiniMax-M2**Agentic capabilities, Advanced reasoning$0.3/M tokens$1.2/M tokens$0.03/M tokens$0.375/M tokens

## Usage Examples[​](#usage-examples "Direct link to Usage Examples")

### Basic Chat Completion[​](#basic-chat-completion "Direct link to Basic Chat Completion")

```
import litellm

response = litellm.anthropic.messages.acreate(
    model="minimax/MiniMax-M2.1",
    messages=[{"role":"user","content":"Hello, how are you?"}],
    api_key="your-minimax-api-key",
    api_base="https://api.minimax.io/anthropic/v1/messages",
    max_tokens=1000
)

print(response.choices[0].message.content)
```

### Using Environment Variables[​](#using-environment-variables "Direct link to Using Environment Variables")

```
export MINIMAX_API_KEY="your-minimax-api-key"
export MINIMAX_API_BASE="https://api.minimax.io/anthropic/v1/messages"
```

```
import litellm

response = litellm.anthropic.messages.acreate(
    model="minimax/MiniMax-M2.1",
    messages=[{"role":"user","content":"Hello!"}],
    max_tokens=1000
)
```

### With Thinking (M2.1 Feature)[​](#with-thinking-m21-feature "Direct link to With Thinking (M2.1 Feature)")

```
response = litellm.anthropic.messages.acreate(
    model="minimax/MiniMax-M2.1",
    messages=[{"role":"user","content":"Solve: 2+2=?"}],
    thinking={"type":"enabled","budget_tokens":1000},
    api_key="your-minimax-api-key"
)

# Access thinking content
for block in response.choices[0].message.content:
ifhasattr(block,'type')and block.type=='thinking':
print(f"Thinking: {block.thinking}")
```

### With Tool Calling[​](#with-tool-calling "Direct link to With Tool Calling")

```
tools =[
{
"type":"function",
"function":{
"name":"get_weather",
"description":"Get current weather",
"parameters":{
"type":"object",
"properties":{
"location":{"type":"string"}
},
"required":["location"]
}
}
}
]

response = litellm.anthropic.messages.acreate(
    model="minimax/MiniMax-M2.1",
    messages=[{"role":"user","content":"What's the weather in SF?"}],
    tools=tools,
    api_key="your-minimax-api-key",
    max_tokens=1000
)
```

## Usage with LiteLLM Proxy[​](#usage-with-litellm-proxy "Direct link to Usage with LiteLLM Proxy")

You can use MiniMax models with the Anthropic SDK by routing through LiteLLM Proxy:

StepDescription**1. Start LiteLLM Proxy**Configure proxy with MiniMax models in `config.yaml`**2. Set Environment Variables**Point Anthropic SDK to proxy endpoint**3. Use Anthropic SDK**Call MiniMax models using native Anthropic SDK

### Step 1: Configure LiteLLM Proxy[​](#step-1-configure-litellm-proxy "Direct link to Step 1: Configure LiteLLM Proxy")

Create a `config.yaml`:

```
model_list:
-model_name: minimax/MiniMax-M2.1
litellm_params:
model: minimax/MiniMax-M2.1
api_key: os.environ/MINIMAX_API_KEY
api_base: https://api.minimax.io/anthropic/v1/messages
```

Start the proxy:

```
litellm --config config.yaml
```

### Step 2: Use with Anthropic SDK[​](#step-2-use-with-anthropic-sdk "Direct link to Step 2: Use with Anthropic SDK")

```
import os
os.environ["ANTHROPIC_BASE_URL"]="http://localhost:4000"
os.environ["ANTHROPIC_API_KEY"]="sk-1234"# Your LiteLLM proxy key

import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="minimax/MiniMax-M2.1",
    max_tokens=1000,
    system="You are a helpful assistant.",
    messages=[
{
"role":"user",
"content":[
{
"type":"text",
"text":"Hi, how are you?"
}
]
}
]
)

for block in message.content:
if block.type=="thinking":
print(f"Thinking:\n{block.thinking}\n")
elif block.type=="text":
print(f"Text:\n{block.text}\n")
```

## MiniMax - v1/chat/completions

## Usage with LiteLLM SDK[​](#usage-with-litellm-sdk "Direct link to Usage with LiteLLM SDK")

You can use MiniMax's OpenAI-compatible API directly with LiteLLM:

### Basic Chat Completion[​](#basic-chat-completion-1 "Direct link to Basic Chat Completion")

```
import litellm

response = litellm.completion(
    model="minimax/MiniMax-M2.1",
    messages=[
{"role":"system","content":"You are a helpful assistant."},
{"role":"user","content":"Hello, how are you?"}
],
    api_key="your-minimax-api-key",
    api_base="https://api.minimax.io/v1"
)

print(response.choices[0].message.content)
```

### Using Environment Variables[​](#using-environment-variables-1 "Direct link to Using Environment Variables")

```
export MINIMAX_API_KEY="your-minimax-api-key"
export MINIMAX_API_BASE="https://api.minimax.io/v1"
```

```
import litellm

response = litellm.completion(
    model="minimax/MiniMax-M2.1",
    messages=[{"role":"user","content":"Hello!"}]
)
```

### With Reasoning Split[​](#with-reasoning-split "Direct link to With Reasoning Split")

```
response = litellm.completion(
    model="minimax/MiniMax-M2.1",
    messages=[
{"role":"system","content":"You are a helpful assistant."},
{"role":"user","content":"Solve: 2+2=?"}
],
    extra_body={"reasoning_split":True},
    api_key="your-minimax-api-key",
    api_base="https://api.minimax.io/v1"
)

# Access reasoning details if available
ifhasattr(response.choices[0].message,'reasoning_details'):
print(f"Thinking: {response.choices[0].message.reasoning_details}")
print(f"Response: {response.choices[0].message.content}")
```

### With Tool Calling[​](#with-tool-calling-1 "Direct link to With Tool Calling")

```
tools =[
{
"type":"function",
"function":{
"name":"get_weather",
"description":"Get current weather",
"parameters":{
"type":"object",
"properties":{
"location":{"type":"string"}
},
"required":["location"]
}
}
}
]

response = litellm.completion(
    model="minimax/MiniMax-M2.1",
    messages=[{"role":"user","content":"What's the weather in SF?"}],
    tools=tools,
    api_key="your-minimax-api-key",
    api_base="https://api.minimax.io/v1"
)
```

### Streaming[​](#streaming "Direct link to Streaming")

```
response = litellm.completion(
    model="minimax/MiniMax-M2.1",
    messages=[{"role":"user","content":"Tell me a story"}],
    stream=True,
    api_key="your-minimax-api-key",
    api_base="https://api.minimax.io/v1"
)

for chunk in response:
if chunk.choices[0].delta.content:
print(chunk.choices[0].delta.content, end="")
```

## Usage with OpenAI SDK via LiteLLM Proxy[​](#usage-with-openai-sdk-via-litellm-proxy "Direct link to Usage with OpenAI SDK via LiteLLM Proxy")

You can also use MiniMax models with the OpenAI SDK by routing through LiteLLM Proxy:

StepDescription**1. Start LiteLLM Proxy**Configure proxy with MiniMax models in `config.yaml`**2. Set Environment Variables**Point OpenAI SDK to proxy endpoint**3. Use OpenAI SDK**Call MiniMax models using native OpenAI SDK

### Step 1: Configure LiteLLM Proxy[​](#step-1-configure-litellm-proxy-1 "Direct link to Step 1: Configure LiteLLM Proxy")

Create a `config.yaml`:

```
model_list:
-model_name: minimax/MiniMax-M2.1
litellm_params:
model: minimax/MiniMax-M2.1
api_key: os.environ/MINIMAX_API_KEY
api_base: https://api.minimax.io/v1
```

Start the proxy:

```
litellm --config config.yaml
```

### Step 2: Use with OpenAI SDK[​](#step-2-use-with-openai-sdk "Direct link to Step 2: Use with OpenAI SDK")

```
import os
os.environ["OPENAI_BASE_URL"]="http://localhost:4000"
os.environ["OPENAI_API_KEY"]="sk-1234"# Your LiteLLM proxy key

from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="minimax/MiniMax-M2.1",
    messages=[
{"role":"system","content":"You are a helpful assistant."},
{"role":"user","content":"Hi, how are you?"},
],
# Set reasoning_split=True to separate thinking content
    extra_body={"reasoning_split":True},
)

# Access thinking and response
ifhasattr(response.choices[0].message,'reasoning_details'):
print(f"Thinking:\n{response.choices[0].message.reasoning_details[0]['text']}\n")
print(f"Text:\n{response.choices[0].message.content}\n")
```

### Streaming with OpenAI SDK[​](#streaming-with-openai-sdk "Direct link to Streaming with OpenAI SDK")

```
from openai import OpenAI

client = OpenAI()

stream = client.chat.completions.create(
    model="minimax/MiniMax-M2.1",
    messages=[
{"role":"system","content":"You are a helpful assistant."},
{"role":"user","content":"Tell me a story"},
],
    extra_body={"reasoning_split":True},
    stream=True,
)

reasoning_buffer =""
text_buffer =""

for chunk in stream:
ifhasattr(chunk.choices[0].delta,"reasoning_details")and chunk.choices[0].delta.reasoning_details:
for detail in chunk.choices[0].delta.reasoning_details:
if"text"in detail:
                reasoning_text = detail["text"]
                new_reasoning = reasoning_text[len(reasoning_buffer):]
if new_reasoning:
print(new_reasoning, end="", flush=True)
                    reasoning_buffer = reasoning_text

if chunk.choices[0].delta.content:
        content_text = chunk.choices[0].delta.content
        new_text = content_text[len(text_buffer):]if text_buffer else content_text
if new_text:
print(new_text, end="", flush=True)
            text_buffer = content_text
```

## Cost Calculation[​](#cost-calculation "Direct link to Cost Calculation")

Cost calculation works automatically using the pricing information in `model_prices_and_context_window.json`.

Example:

```
response = litellm.completion(
    model="minimax/MiniMax-M2.1",
    messages=[{"role":"user","content":"Hello!"}],
    api_key="your-minimax-api-key"
)

# Access cost information
print(f"Cost: ${response._hidden_params.get('response_cost',0)}")
```

## MiniMax - Text-to-Speech

## Quick Start[​](#quick-start "Direct link to Quick Start")

## **LiteLLM Python SDK Usage**[​](#litellm-python-sdk-usage "Direct link to litellm-python-sdk-usage")

### Basic Usage[​](#basic-usage "Direct link to Basic Usage")

```
from pathlib import Path
from litellm import speech
import os 

os.environ["MINIMAX_API_KEY"]="your-api-key"

speech_file_path = Path(__file__).parent /"speech.mp3"
response = speech(
    model="minimax/speech-2.6-hd",
    voice="alloy",
input="The quick brown fox jumped over the lazy dogs",
)
response.stream_to_file(speech_file_path)
```

### Async Usage[​](#async-usage "Direct link to Async Usage")

```
from litellm import aspeech
from pathlib import Path
import os, asyncio

os.environ["MINIMAX_API_KEY"]="your-api-key"

asyncdeftest_async_speech():
    speech_file_path = Path(__file__).parent /"speech.mp3"
    response =await aspeech(
        model="minimax/speech-2.6-hd",
        voice="alloy",
input="The quick brown fox jumped over the lazy dogs",
)
    response.stream_to_file(speech_file_path)

asyncio.run(test_async_speech())
```

### Voice Selection[​](#voice-selection "Direct link to Voice Selection")

MiniMax supports many voices. LiteLLM provides OpenAI-compatible voice names that map to MiniMax voices:

```
from litellm import speech

# OpenAI-compatible voice names
voices =["alloy","echo","fable","onyx","nova","shimmer"]

for voice in voices:
    response = speech(
        model="minimax/speech-2.6-hd",
        voice=voice,
input=f"This is the {voice} voice",
)
    response.stream_to_file(f"speech_{voice}.mp3")
```

You can also use MiniMax-native voice IDs directly:

```
response = speech(
    model="minimax/speech-2.6-hd",
    voice="male-qn-qingse",# MiniMax native voice ID
input="Using native MiniMax voice ID",
)
```

### Custom Parameters[​](#custom-parameters "Direct link to Custom Parameters")

MiniMax TTS supports additional parameters for fine-tuning audio output:

```
from litellm import speech

response = speech(
    model="minimax/speech-2.6-hd",
    voice="alloy",
input="Custom audio parameters",
    speed=1.5,# Speed: 0.5 to 2.0
    response_format="mp3",# Format: mp3, pcm, wav, flac
    extra_body={
"vol":1.2,# Volume: 0.1 to 10
"pitch":2,# Pitch adjustment: -12 to 12
"sample_rate":32000,# 16000, 24000, or 32000
"bitrate":128000,# For MP3: 64000, 128000, 192000, 256000
"channel":1,# 1 for mono, 2 for stereo
}
)
response.stream_to_file("custom_speech.mp3")
```

### Response Formats[​](#response-formats "Direct link to Response Formats")

```
from litellm import speech

# MP3 format (default)
response = speech(
    model="minimax/speech-2.6-hd",
    voice="alloy",
input="MP3 format audio",
    response_format="mp3",
)

# PCM format
response = speech(
    model="minimax/speech-2.6-hd",
    voice="alloy",
input="PCM format audio",
    response_format="pcm",
)

# WAV format
response = speech(
    model="minimax/speech-2.6-hd",
    voice="alloy",
input="WAV format audio",
    response_format="wav",
)

# FLAC format
response = speech(
    model="minimax/speech-2.6-hd",
    voice="alloy",
input="FLAC format audio",
    response_format="flac",
)
```

## **LiteLLM Proxy Usage**[​](#litellm-proxy-usage "Direct link to litellm-proxy-usage")

LiteLLM provides an OpenAI-compatible `/audio/speech` endpoint for MiniMax TTS.

### Setup[​](#setup "Direct link to Setup")

Add MiniMax to your proxy configuration:

```
model_list:
-model_name: tts
litellm_params:
model: minimax/speech-2.6-hd
api_key: os.environ/MINIMAX_API_KEY

-model_name: tts-turbo
litellm_params:
model: minimax/speech-2.6-turbo
api_key: os.environ/MINIMAX_API_KEY
```

Start the proxy:

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

### Making Requests[​](#making-requests "Direct link to Making Requests")

```
curl http://0.0.0.0:4000/v1/audio/speech \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tts",
    "input": "The quick brown fox jumped over the lazy dog.",
    "voice": "alloy"
  }' \
  --output speech.mp3
```

With custom parameters:

```
curl http://0.0.0.0:4000/v1/audio/speech \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tts",
    "input": "Custom parameters example.",
    "voice": "nova",
    "speed": 1.5,
    "response_format": "mp3",
    "extra_body": {
      "vol": 1.2,
      "pitch": 1,
      "sample_rate": 32000
    }
  }' \
  --output custom_speech.mp3
```

## Voice Mappings[​](#voice-mappings "Direct link to Voice Mappings")

LiteLLM maps OpenAI-compatible voice names to MiniMax voice IDs:

OpenAI VoiceMiniMax Voice IDDescriptionalloymale-qn-qingseMale voiceechomale-qn-jingyingMale voicefablefemale-shaonvFemale voiceonyxmale-qn-badaoMale voicenovafemale-yujieFemale voiceshimmerfemale-tianmeiFemale voice

You can also use any MiniMax-native voice ID directly by passing it as the `voice` parameter.

### Streaming (WebSocket)[​](#streaming-websocket "Direct link to Streaming (WebSocket)")

note

The current implementation uses MiniMax's HTTP endpoint. For WebSocket streaming support, please refer to MiniMax's official documentation at [https://platform.minimax.io/docs](https://platform.minimax.io/docs).

## Error Handling[​](#error-handling "Direct link to Error Handling")

```
from litellm import speech
import litellm

try:
    response = speech(
        model="minimax/speech-2.6-hd",
        voice="alloy",
input="Test input",
)
    response.stream_to_file("output.mp3")
except litellm.exceptions.BadRequestError as e:
print(f"Bad request: {e}")
except litellm.exceptions.AuthenticationError as e:
print(f"Authentication failed: {e}")
except Exception as e:
print(f"Error: {e}")
```

### Extra Body Parameters[​](#extra-body-parameters "Direct link to Extra Body Parameters")

Pass these via `extra_body`:

ParameterTypeDescriptionDefaultvolfloatVolume (0.1 to 10)1.0pitchintPitch adjustment (-12 to 12)0sample\_rateintSample rate: 16000, 24000, 3200032000bitrateintBitrate for MP3: 64000, 128000, 192000, 256000128000channelintAudio channels: 1 (mono) or 2 (stereo)1output\_formatstringOutput format: "hex" or "url" (url returns a URL valid for 24 hours)hex