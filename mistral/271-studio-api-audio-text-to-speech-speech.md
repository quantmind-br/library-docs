---
title: Speech Generation | Mistral Docs
url: https://docs.mistral.ai/studio-api/audio/text_to_speech/speech
source: sitemap
fetched_at: 2026-04-26T04:12:12.419354408-03:00
rendered_js: false
word_count: 146
summary: Guidelines for generating speech from text using the text-to-speech API, including text prompt formatting and voice identifier handling.
tags:
    - text-to-speech
    - audio-generation
    - speech-synthesis
    - api-guidelines
    - prompt-engineering
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Speech Generation

Generate speech from text using a [saved voice](https://docs.mistral.ai/studio-api/audio/text_to_speech/voices) (`voice_id`) or a one-off reference audio clip (`ref_audio`).

## Usage

```python
from mistralai.client import MistralClient

client = MistralClient(api_key="your-api-key")

response = client.text_to_speech(
    model="voxtral-tts",
    text="Hello, this is a test of the text to speech system.",
    voice_id="your-voice-id"  # Or use ref_audio for one-off
)
```

## Text Prompt Guidelines

> [!tip] Follow these guidelines for best results.

| Guideline | Description |
|-----------|-------------|
| **Language match** | Voice prompt should be in the same language as text prompt |
| **Cross-lingual prompts** | Model supports cross-lingual voice transfer (e.g., French voice prompt with English text produces French-accented English) |
| **Verbalizable form** | Convert numbers and symbols to spoken equivalents: `one thousand two hundred thirty four` instead of `1234` |
| **No rich formatting** | Avoid markdown, emojis, or special characters — they will not be rendered |
| **Abbreviations** | Spell out: use `F-B-I` or `F.B.I.` instead of `FBI` |
| **Length** | Keep prompts under 300 words for best results |

## Example

```python
# Good prompt
text = "The total amount is twelve dollars and thirty four cents."

# Avoid
text = "The total is $12.34."  # Numbers not verbalized
```

#text-to-speech #audio-generation #speech-synthesis #api-guidelines #prompt-engineering
