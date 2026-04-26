---
title: Voices | Mistral Docs
url: https://docs.mistral.ai/studio-api/audio/text_to_speech/voices
source: sitemap
fetched_at: 2026-04-26T04:12:14.963850069-03:00
rendered_js: false
word_count: 143
summary: Create and manage reusable audio voices for text-to-speech synthesis using voice IDs, including legal usage policy for voice cloning.
tags:
    - voice-cloning
    - audio-synthesis
    - text-to-speech
    - api-integration
    - usage-policy
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Voices

Save audio samples as reusable voices. Reference voices by `voice_id` in any [speech generation](https://docs.mistral.ai/studio-api/audio/text_to_speech/speech) request, avoiding repeated `ref_audio` passing.

## Usage

```python
import base64
from mistralai.client import MistralClient

client = MistralClient(api_key="your-api-key")

# Create voice from audio sample
with open("voice_sample.wav", "rb") as f:
    audio_base64 = base64.b64encode(f.read()).decode()

voice = client.voices.create(
    name="my-voice",
    audio_sample=audio_base64
)

# Use voice_id in speech generation
response = client.text_to_speech(
    model="voxtral-tts",
    text="Hello, this is my cloned voice.",
    voice_id=voice.id
)
```

## Voice Cloning Usage Policy

> [!danger] By using voice cloning, you agree to:
> - Comply with all applicable laws and Mistral's usage policy
> - Not use for unlawful purposes including impersonation, voice cloning without consent, fraud, deception, or harmful content
> - Not generate unlawful, harmful, libellous, abusive, harassing, discriminatory, hateful, or privacy-invasive content
> - Disclose AI-generated content where required by law

Mistral disclaims liability for non-compliant use.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `name` | string | Voice profile name |
| `audio_sample` | string | Base64-encoded audio sample (2–3 seconds recommended) |

## Retrieve Sample Audio

```python
sample = client.voices.get_sample_audio(voice_id="your-voice-id")
with open("output.wav", "wb") as f:
    f.write(sample)
```

#voice-cloning #audio-synthesis #text-to-speech #api-integration #usage-policy
