---
title: AWS Polly Text to Speech (tts) | liteLLM
url: https://docs.litellm.ai/docs/providers/aws_polly
source: sitemap
fetched_at: 2026-01-21T19:48:01.650147039-03:00
rendered_js: false
word_count: 216
summary: This document explains how to integrate AWS Polly for text-to-speech synthesis using the LiteLLM SDK and Proxy, covering engine selection, voice mappings, and SSML support.
tags:
    - aws-polly
    - litellm
    - text-to-speech
    - tts
    - ssml
    - aws-authentication
    - api-proxy
category: guide
---

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionConvert text to natural-sounding speech using AWS Polly's neural and standard TTS enginesProvider Route on LiteLLM`aws_polly/`Supported Operations`/audio/speech`Link to Provider Doc[AWS Polly SynthesizeSpeech ↗](https://docs.aws.amazon.com/polly/latest/dg/API_SynthesizeSpeech.html)

## Quick Start[​](#quick-start "Direct link to Quick Start")

### **LiteLLM SDK**[​](#litellm-sdk "Direct link to litellm-sdk")

SDK Usage

```
import litellm
from pathlib import Path
import os

# Set environment variables
os.environ["AWS_ACCESS_KEY_ID"]=""
os.environ["AWS_SECRET_ACCESS_KEY"]=""
os.environ["AWS_REGION_NAME"]="us-east-1"

# AWS Polly call
speech_file_path = Path(__file__).parent /"speech.mp3"
response = litellm.speech(
    model="aws_polly/neural",
    voice="Joanna",
input="the quick brown fox jumped over the lazy dogs",
)
response.stream_to_file(speech_file_path)
```

### **LiteLLM PROXY**[​](#litellm-proxy "Direct link to litellm-proxy")

proxy\_config.yaml

```
model_list:
-model_name: polly-neural
litellm_params:
model: aws_polly/neural
aws_access_key_id:"os.environ/AWS_ACCESS_KEY_ID"
aws_secret_access_key:"os.environ/AWS_SECRET_ACCESS_KEY"
aws_region_name:"us-east-1"
```

## Polly Engines[​](#polly-engines "Direct link to Polly Engines")

AWS Polly supports different speech synthesis engines. Specify the engine in the model name:

ModelEngineCost (per 1M chars)Description`aws_polly/standard`Standard$4.00Original Polly voices, faster and lowest cost`aws_polly/neural`Neural$16.00More natural, human-like speech (recommended)`aws_polly/generative`Generative$30.00Most expressive, highest quality (limited voices)`aws_polly/long-form`Long-form$100.00Optimized for long content like articles

### **LiteLLM SDK**[​](#litellm-sdk-1 "Direct link to litellm-sdk-1")

Using Different Engines

```
import litellm

# Neural engine (recommended)
response = litellm.speech(
    model="aws_polly/neural",
    voice="Joanna",
input="Hello world",
)

# Standard engine (lower cost)
response = litellm.speech(
    model="aws_polly/standard",
    voice="Joanna",
input="Hello world",
)

# Generative engine (highest quality)
response = litellm.speech(
    model="aws_polly/generative",
    voice="Matthew",
input="Hello world",
)
```

### **LiteLLM PROXY**[​](#litellm-proxy-1 "Direct link to litellm-proxy-1")

proxy\_config.yaml

```
model_list:
-model_name: polly-neural
litellm_params:
model: aws_polly/neural
aws_region_name:"us-east-1"
-model_name: polly-standard
litellm_params:
model: aws_polly/standard
aws_region_name:"us-east-1"
-model_name: polly-generative
litellm_params:
model: aws_polly/generative
aws_region_name:"us-east-1"
```

## Available Voices[​](#available-voices "Direct link to Available Voices")

### Native Polly Voices[​](#native-polly-voices "Direct link to Native Polly Voices")

AWS Polly has many voices across different languages. Here are popular US English voices:

VoiceGenderEngine Support`Joanna`FemaleNeural, Standard`Matthew`MaleNeural, Standard, Generative`Ivy`Female (child)Neural, Standard`Kendra`FemaleNeural, Standard`Amy`Female (British)Neural, Standard`Brian`Male (British)Neural, Standard

### **LiteLLM SDK**[​](#litellm-sdk-2 "Direct link to litellm-sdk-2")

Using Native Polly Voices

```
import litellm

# US English female
response = litellm.speech(
    model="aws_polly/neural",
    voice="Joanna",
input="Hello from Joanna",
)

# US English male
response = litellm.speech(
    model="aws_polly/neural",
    voice="Matthew",
input="Hello from Matthew",
)

# British English female
response = litellm.speech(
    model="aws_polly/neural",
    voice="Amy",
input="Hello from Amy",
)
```

### **LiteLLM PROXY**[​](#litellm-proxy-2 "Direct link to litellm-proxy-2")

proxy\_config.yaml

```
model_list:
-model_name: polly-joanna
litellm_params:
model: aws_polly/neural
voice:"Joanna"
aws_region_name:"us-east-1"
-model_name: polly-matthew
litellm_params:
model: aws_polly/neural
voice:"Matthew"
aws_region_name:"us-east-1"
```

### OpenAI Voice Mappings[​](#openai-voice-mappings "Direct link to OpenAI Voice Mappings")

LiteLLM also supports OpenAI voice names, which are automatically mapped to Polly voices:

OpenAI VoiceMaps to Polly Voice`alloy`Joanna`echo`Matthew`fable`Amy`onyx`Brian`nova`Ivy`shimmer`Kendra

### **LiteLLM SDK**[​](#litellm-sdk-3 "Direct link to litellm-sdk-3")

Using OpenAI Voice Names

```
import litellm

# These are equivalent
response = litellm.speech(
    model="aws_polly/neural",
    voice="alloy",# Maps to Joanna
input="Hello world",
)

response = litellm.speech(
    model="aws_polly/neural",
    voice="Joanna",# Native Polly voice
input="Hello world",
)
```

## SSML Support[​](#ssml-support "Direct link to SSML Support")

AWS Polly supports SSML (Speech Synthesis Markup Language) for advanced control over speech output. LiteLLM automatically detects SSML input.

### **LiteLLM SDK**[​](#litellm-sdk-4 "Direct link to litellm-sdk-4")

SSML Example

```
import litellm

ssml_input ="""
<speak>
    Hello, <break time="500ms"/> 
    this is a test with <emphasis level="strong">emphasis</emphasis> 
    and <prosody rate="slow">slower speech</prosody>.
</speak>
"""

response = litellm.speech(
    model="aws_polly/neural",
    voice="Joanna",
input=ssml_input,
)
```

### **LiteLLM PROXY**[​](#litellm-proxy-3 "Direct link to litellm-proxy-3")

cURL Request with SSML

```
curl -X POST http://localhost:4000/v1/audio/speech \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "polly-neural",
    "voice": "Joanna",
    "input": "<speak>Hello <break time=\"500ms\"/> world</speak>"
  }' \
  --output speech.mp3
```

## Supported Parameters[​](#supported-parameters "Direct link to Supported Parameters")

All Parameters

```
response = litellm.speech(
    model="aws_polly/neural",
    voice="Joanna",# Required: Voice selection
input="text to convert",# Required: Input text (or SSML)
    response_format="mp3",# Optional: mp3, ogg_vorbis, pcm

# AWS-specific parameters
    language_code="en-US",# Optional: Language code
    sample_rate="22050",# Optional: Sample rate in Hz
)
```

## Response Formats[​](#response-formats "Direct link to Response Formats")

FormatDescription`mp3`MP3 audio (default)`ogg_vorbis`Ogg Vorbis audio`pcm`Raw PCM audio

### **LiteLLM SDK**[​](#litellm-sdk-5 "Direct link to litellm-sdk-5")

Different Response Formats

```
import litellm

# MP3 (default)
response = litellm.speech(
    model="aws_polly/neural",
    voice="Joanna",
input="Hello",
    response_format="mp3",
)

# Ogg Vorbis
response = litellm.speech(
    model="aws_polly/neural",
    voice="Joanna",
input="Hello",
    response_format="ogg_vorbis",
)
```

## AWS Authentication[​](#aws-authentication "Direct link to AWS Authentication")

LiteLLM supports multiple AWS authentication methods.

### **LiteLLM SDK**[​](#litellm-sdk-6 "Direct link to litellm-sdk-6")

Authentication Options

```
import litellm
import os

# Option 1: Environment variables (recommended)
os.environ["AWS_ACCESS_KEY_ID"]="your-access-key"
os.environ["AWS_SECRET_ACCESS_KEY"]="your-secret-key"
os.environ["AWS_REGION_NAME"]="us-east-1"

response = litellm.speech(model="aws_polly/neural", voice="Joanna",input="Hello")

# Option 2: Pass credentials directly
response = litellm.speech(
    model="aws_polly/neural",
    voice="Joanna",
input="Hello",
    aws_access_key_id="your-access-key",
    aws_secret_access_key="your-secret-key",
    aws_region_name="us-east-1",
)

# Option 3: IAM Role (when running on AWS)
response = litellm.speech(
    model="aws_polly/neural",
    voice="Joanna",
input="Hello",
    aws_region_name="us-east-1",
)

# Option 4: AWS Profile
response = litellm.speech(
    model="aws_polly/neural",
    voice="Joanna",
input="Hello",
    aws_profile_name="my-profile",
)
```

### **LiteLLM PROXY**[​](#litellm-proxy-4 "Direct link to litellm-proxy-4")

proxy\_config.yaml

```
model_list:
# Using environment variables
-model_name: polly-neural
litellm_params:
model: aws_polly/neural
aws_access_key_id:"os.environ/AWS_ACCESS_KEY_ID"
aws_secret_access_key:"os.environ/AWS_SECRET_ACCESS_KEY"
aws_region_name:"us-east-1"

# Using IAM Role (when proxy runs on AWS)
-model_name: polly-neural-iam
litellm_params:
model: aws_polly/neural
aws_region_name:"us-east-1"

# Using AWS Profile
-model_name: polly-neural-profile
litellm_params:
model: aws_polly/neural
aws_profile_name:"my-profile"
```

## Async Support[​](#async-support "Direct link to Async Support")

Async Usage

```
import litellm
import asyncio

asyncdefmain():
    response =await litellm.aspeech(
        model="aws_polly/neural",
        voice="Joanna",
input="Hello from async AWS Polly",
        aws_region_name="us-east-1",
)

withopen("output.mp3","wb")as f:
        f.write(response.content)

asyncio.run(main())
```