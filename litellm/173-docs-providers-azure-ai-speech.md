---
title: Azure AI Speech (Cognitive Services) | liteLLM
url: https://docs.litellm.ai/docs/providers/azure_ai_speech
source: sitemap
fetched_at: 2026-01-21T19:48:08.898099997-03:00
rendered_js: false
word_count: 615
summary: This document provides a comprehensive guide on integrating Azure AI Speech with LiteLLM for text-to-speech tasks, including setup, cost tracking, and voice mapping. It details how to use both the LiteLLM SDK and Proxy to access neural voices and implement advanced features like SSML.
tags:
    - azure-ai-speech
    - litellm
    - text-to-speech
    - ssml
    - api-integration
    - cost-tracking
category: guide
---

Azure AI Speech is Azure's Cognitive Services text-to-speech API, separate from Azure OpenAI. It provides high-quality neural voices with broader language support and advanced speech customization.

**When to use this vs Azure OpenAI TTS:**

- **Azure AI Speech** - More languages, neural voices, SSML support, speech customization
- **Azure OpenAI TTS** - OpenAI models, integrated with Azure OpenAI services

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionAzure AI Speech is Azure's Cognitive Services text-to-speech API, separate from Azure OpenAI. It provides high-quality neural voices with broader language support and advanced speech customization.Provider Route on LiteLLM`azure/speech/`

## Quick Start[​](#quick-start "Direct link to Quick Start")

**LiteLLM SDK**

SDK Usage

```
from litellm import speech
from pathlib import Path
import os

os.environ["AZURE_TTS_API_KEY"]="your-cognitive-services-key"

speech_file_path = Path(__file__).parent /"speech.mp3"
response = speech(
    model="azure/speech/azure-tts",
    voice="alloy",
input="Hello, this is Azure AI Speech",
    api_base="https://eastus.tts.speech.microsoft.com",
    api_key=os.environ["AZURE_TTS_API_KEY"],
)
response.stream_to_file(speech_file_path)
```

**LiteLLM Proxy**

proxy\_config.yaml

```
model_list:
-model_name: azure-speech
litellm_params:
model: azure/speech/azure-tts
api_base: https://eastus.tts.speech.microsoft.com
api_key: os.environ/AZURE_TTS_API_KEY
```

## Setup[​](#setup "Direct link to Setup")

1. Create an Azure Cognitive Services resource in the [Azure Portal](https://portal.azure.com)
2. Get your API key from the resource
3. Note your region (e.g., `eastus`, `westus`, `westeurope`)
4. Use the regional endpoint: `https://{region}.tts.speech.microsoft.com`

## Cost Tracking (Pricing)[​](#cost-tracking-pricing "Direct link to Cost Tracking (Pricing)")

LiteLLM automatically tracks costs for Azure AI Speech based on the number of characters processed.

### Available Models[​](#available-models "Direct link to Available Models")

ModelVoice TypeCost per 1M Characters`azure/speech/azure-tts`Neural$15`azure/speech/azure-tts-hd`Neural HD$30

### How Costs are Calculated[​](#how-costs-are-calculated "Direct link to How Costs are Calculated")

Azure AI Speech charges based on the number of characters in your input text. LiteLLM automatically:

- Counts the number of characters in your `input` parameter
- Calculates the cost based on the model pricing
- Returns the cost in the response object

View Request Cost

```
from litellm import speech

response = speech(
    model="azure/speech/azure-tts",
    voice="alloy",
input="Hello, this is a test message",
    api_base="https://eastus.tts.speech.microsoft.com",
    api_key=os.environ["AZURE_TTS_API_KEY"],
)

# Access the calculated cost
cost = response._hidden_params.get("response_cost")
print(f"Request cost: ${cost}")
```

### Verify Azure Pricing[​](#verify-azure-pricing "Direct link to Verify Azure Pricing")

To check the latest Azure AI Speech pricing:

1. Visit the [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/)
2. Set **Service** to "AI Services"
3. Set **API** to "Azure AI Speech"
4. Select **Text to Speech** and your region
5. View the current pricing per million characters

**Note:** Pricing may vary by region and Azure subscription type.

## Voice Mapping[​](#voice-mapping "Direct link to Voice Mapping")

LiteLLM automatically maps OpenAI voice names to Azure Neural voices:

OpenAI VoiceAzure Neural VoiceDescription`alloy`en-US-JennyNeuralNeutral and balanced`echo`en-US-GuyNeuralWarm and upbeat`fable`en-GB-RyanNeuralExpressive and dramatic`onyx`en-US-DavisNeuralDeep and authoritative`nova`en-US-AmberNeuralFriendly and conversational`shimmer`en-US-AriaNeuralBright and cheerful

## Supported Parameters[​](#supported-parameters "Direct link to Supported Parameters")

All Parameters

```
response = speech(
    model="azure/speech/azure-tts",
    voice="alloy",# Required: Voice selection
input="text to convert",# Required: Input text
    speed=1.0,# Optional: 0.25 to 4.0 (default: 1.0)
    response_format="mp3",# Optional: mp3, opus, wav, pcm
    api_base="https://eastus.tts.speech.microsoft.com",
    api_key="your-key",
)
```

### Response Formats[​](#response-formats "Direct link to Response Formats")

FormatAzure Output FormatSample Rate`mp3`audio-24khz-48kbitrate-mono-mp324kHz`opus`ogg-48khz-16bit-mono-opus48kHz`wav`riff-24khz-16bit-mono-pcm24kHz`pcm`raw-24khz-16bit-mono-pcm24kHz

## Passing Raw SSML[​](#passing-raw-ssml "Direct link to Passing Raw SSML")

LiteLLM automatically detects when your `input` contains SSML (by checking for `<speak>` tags) and passes it through to Azure without any transformation. This gives you complete control over speech synthesis.

**When to use raw SSML:**

- Using the `<lang>` element with multilingual voices to translate text (e.g., English text → Spanish speech)
- Complex SSML structures with multiple voices or prosody changes
- Fine-grained control over pronunciation, breaks, emphasis, and other speech features

### LiteLLM SDK[​](#litellm-sdk "Direct link to LiteLLM SDK")

Raw SSML for Multilingual Translation

```
from litellm import speech

# Use <lang> element to convert English text to Spanish speech
# The <lang> element forces the output language regardless of input text language
language_code ="es-ES"
text ="Hello, how are you today?"# English text
voice ="en-US-AvaMultilingualNeural"

ssml =f"""<speak version="1.0"
    xmlns="http://www.w3.org/2001/10/synthesis"
    xmlns:mstts="http://www.w3.org/2001/mstts"
    xml:lang="{language_code}">
<voice name="{voice}">
    <lang xml:lang="{language_code}">{text}</lang>
</voice>
</speak>"""

response = speech(
    model="azure/speech/azure-tts",
    voice=voice,
input=ssml,# LiteLLM auto-detects SSML and sends as-is
    api_base="https://eastus.tts.speech.microsoft.com",
    api_key=os.environ["AZURE_TTS_API_KEY"],
)
response.stream_to_file("speech.mp3")
```

Raw SSML with Complex Features

```
from litellm import speech

# Complex SSML with multiple prosody adjustments
ssml ="""<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' 
    xmlns:mstts='https://www.w3.org/2001/mstts' xml:lang='en-US'>
<voice name='en-US-JennyNeural'>
    <mstts:express-as style='cheerful' styledegree='2'>
        <prosody rate='+20%' pitch='high'>
            Welcome to our service!
        </prosody>
    </mstts:express-as>
    <break time='500ms'/>
    <prosody rate='-10%'>
        How can I help you today?
    </prosody>
</voice>
</speak>"""

response = speech(
    model="azure/speech/azure-tts",
    voice="en-US-JennyNeural",
input=ssml,# LiteLLM detects <speak> and passes through unchanged
    api_base="https://eastus.tts.speech.microsoft.com",
    api_key=os.environ["AZURE_TTS_API_KEY"],
)
response.stream_to_file("speech.mp3")
```

### LiteLLM Proxy[​](#litellm-proxy "Direct link to LiteLLM Proxy")

```
curl http://0.0.0.0:4000/v1/audio/speech \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "azure-speech",
    "voice": "en-US-AvaMultilingualNeural",
    "input": "<speak version=\"1.0\" xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:mstts=\"http://www.w3.org/2001/mstts\" xml:lang=\"es-ES\"><voice name=\"en-US-AvaMultilingualNeural\"><lang xml:lang=\"es-ES\">Hello, how are you today?</lang></voice></speak>"
  }' \
  --output speech.mp3
```

## Sending Azure-Specific Params[​](#sending-azure-specific-params "Direct link to Sending Azure-Specific Params")

Azure AI Speech supports advanced SSML features through optional parameters:

- `style`: Speaking style (e.g., "cheerful", "sad", "angry", "whispering")
- `styledegree`: Style intensity (0.01 to 2)
- `role`: Voice role (e.g., "Girl", "Boy", "SeniorFemale", "SeniorMale")
- `lang`: Language code for multilingual voices (e.g., "es-ES", "fr-FR", "hi-IN")

### **LiteLLM SDK**[​](#litellm-sdk-1 "Direct link to litellm-sdk-1")

#### Custom Azure Voice[​](#custom-azure-voice "Direct link to Custom Azure Voice")

Custom Azure Voice

```
from litellm import speech

response = speech(
    model="azure/speech/azure-tts",
    voice="en-US-AndrewNeural",# Use Azure voice directly
input="Hello, this is a test",
    api_base="https://eastus.tts.speech.microsoft.com",
    api_key=os.environ["AZURE_TTS_API_KEY"],
    response_format="mp3"
)
response.stream_to_file("speech.mp3")
```

#### Speaking Style[​](#speaking-style "Direct link to Speaking Style")

Speaking Style

```
from litellm import speech

response = speech(
    model="azure/speech/azure-tts",
    voice="en-US-JennyNeural",# Must be a voice that supports styles
input="Who are you? What is chicken dinner?",
    api_base="https://eastus.tts.speech.microsoft.com",
    api_key=os.environ["AZURE_TTS_API_KEY"],
    style="whispering",# Azure-specific: cheerful, sad, angry, whispering, etc.
)
response.stream_to_file("speech.mp3")
```

#### Style with Degree and Role[​](#style-with-degree-and-role "Direct link to Style with Degree and Role")

Style with Degree and Role

```
from litellm import speech

response = speech(
    model="azure/speech/azure-tts",
    voice="en-US-AriaNeural",
input="Good morning! How are you today?",
    api_base="https://eastus.tts.speech.microsoft.com",
    api_key=os.environ["AZURE_TTS_API_KEY"],
    style="cheerful",# Azure-specific: Speaking style
    styledegree="2",# Azure-specific: 0.01 to 2 (intensity)
    role="SeniorFemale",# Azure-specific: Girl, Boy, SeniorFemale, etc.
)
response.stream_to_file("speech.mp3")
```

#### Language Override for Multilingual Voices[​](#language-override-for-multilingual-voices "Direct link to Language Override for Multilingual Voices")

Language Override

```
from litellm import speech

response = speech(
    model="azure/speech/azure-tts",
    voice="en-US-AvaMultilingualNeural",# Multilingual voice
input="आप कौन हैं? चिकन डिनर क्या है?",# Hindi text
    api_base="https://eastus.tts.speech.microsoft.com",
    api_key=os.environ["AZURE_TTS_API_KEY"],
    lang="hi-IN",# Azure-specific: Override language
)
response.stream_to_file("speech.mp3")
```

### **LiteLLM AI Gateway (CURL)**[​](#litellm-ai-gateway-curl "Direct link to litellm-ai-gateway-curl")

First, ensure you have set up your proxy config as shown in the [LiteLLM Proxy setup](#quick-start) above.

**Using the model name from your config:**

```
model_list:
-model_name: azure-speech  # This is what you'll use in your API calls
litellm_params:
model: azure/speech/azure-tts
api_base: https://eastus.tts.speech.microsoft.com
api_key: os.environ/AZURE_TTS_API_KEY
```

#### Custom Azure Voice[​](#custom-azure-voice-1 "Direct link to Custom Azure Voice")

```
curl http://0.0.0.0:4000/v1/audio/speech \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "azure-speech",
    "voice": "en-US-AndrewNeural",
    "input": "Hello, this is a test"
  }' \
  --output speech.mp3
```

#### Speaking Style[​](#speaking-style-1 "Direct link to Speaking Style")

```
curl http://0.0.0.0:4000/v1/audio/speech \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "azure-speech",
    "input": "Who are you? What is chicken dinner?",
    "voice": "en-US-JennyNeural",
    "style": "whispering"
  }' \
  --output speech.mp3
```

#### Style with Degree and Role[​](#style-with-degree-and-role-1 "Direct link to Style with Degree and Role")

```
curl http://0.0.0.0:4000/v1/audio/speech \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "azure-speech",
    "voice": "en-US-AriaNeural",
    "input": "Good morning! How are you today?",
    "style": "cheerful",
    "styledegree": "2",
    "role": "SeniorFemale"
  }' \
  --output speech.mp3
```

#### Language Override[​](#language-override "Direct link to Language Override")

```
curl http://0.0.0.0:4000/v1/audio/speech \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "azure-speech",
    "input": "आप कौन हैं? चिकन डिनर क्या है?",
    "voice": "en-US-AvaMultilingualNeural",
    "lang": "hi-IN"
  }' \
  --output speech.mp3
```

### Azure-Specific Parameters Reference[​](#azure-specific-parameters-reference "Direct link to Azure-Specific Parameters Reference")

ParameterDescriptionExample ValuesNotes`style`Speaking style`cheerful`, `sad`, `angry`, `excited`, `friendly`, `hopeful`, `shouting`, `terrified`, `unfriendly`, `whispering`Only supported by certain voices. See [Azure voice styles documentation](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-voice#use-speaking-styles-and-roles)`styledegree`Style intensity`0.01` to `2`Higher values = more intense. Default is `1``role`Voice role`Girl`, `Boy`, `YoungAdultFemale`, `YoungAdultMale`, `OlderAdultFemale`, `OlderAdultMale`, `SeniorFemale`, `SeniorMale`Only supported by certain voices`lang`Language code`es-ES`, `fr-FR`, `de-DE`, `hi-IN`, etc.For multilingual voices. Overrides the default language

## Async Support[​](#async-support "Direct link to Async Support")

Async Usage

```
import asyncio
from litellm import aspeech
from pathlib import Path

asyncdefgenerate_speech():
    response =await aspeech(
        model="azure/speech/azure-tts",
        voice="alloy",
input="Hello from async",
        api_base="https://eastus.tts.speech.microsoft.com",
        api_key=os.environ["AZURE_TTS_API_KEY"],
)

    speech_file_path = Path(__file__).parent /"speech.mp3"
    response.stream_to_file(speech_file_path)

asyncio.run(generate_speech())
```

## Regional Endpoints[​](#regional-endpoints "Direct link to Regional Endpoints")

Replace `{region}` with your Azure resource region:

- US East: `https://eastus.tts.speech.microsoft.com`
- US West: `https://westus.tts.speech.microsoft.com`
- Europe West: `https://westeurope.tts.speech.microsoft.com`
- Asia Southeast: `https://southeastasia.tts.speech.microsoft.com`

[Full list of regions](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/regions)

## Advanced Features[​](#advanced-features "Direct link to Advanced Features")

### Custom Neural Voices[​](#custom-neural-voices "Direct link to Custom Neural Voices")

You can use any Azure Neural voice by passing the full voice name:

Custom Voice

```
response = speech(
    model="azure/speech/azure-tts",
    voice="en-US-AriaNeural",# Direct Azure voice name
input="Using a specific neural voice",
    api_base="https://eastus.tts.speech.microsoft.com",
    api_key=os.environ["AZURE_TTS_API_KEY"],
)
```

Browse available voices in the [Azure Speech Gallery](https://speech.microsoft.com/portal/voicegallery).

## Error Handling[​](#error-handling "Direct link to Error Handling")

Error Handling

```
from litellm import speech
from litellm.exceptions import APIError

try:
    response = speech(
        model="azure/speech/azure-tts",
        voice="alloy",
input="Test message",
        api_base="https://eastus.tts.speech.microsoft.com",
        api_key=os.environ["AZURE_TTS_API_KEY"],
)
except APIError as e:
print(f"Azure Speech error: {e}")
```

## Reference[​](#reference "Direct link to Reference")

- [Azure Speech Service Documentation](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/)
- [Text-to-Speech REST API](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/rest-text-to-speech)