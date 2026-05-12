---
title: Guides Querying Asr Models
url: https://docs.fireworks.ai/guides/querying-asr-models
source: sitemap
fetched_at: 2026-04-27T20:18:21.195684604-03:00
rendered_js: false
word_count: 218
summary: 'This guide introduces and explains the three primary Automatic Speech Recognition (ASR) features provided by Fireworks AI: Streaming Transcription, Pre-recorded Transcription, and Pre-recorded Translation. It provides quick start information and links to detailed API documentation for each service.'
tags:
    - asr-features
    - speech-recognition
    - audio-processing
    - streaming-transcription
    - api-guide
    - fireworks-ai
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Fireworks AI provides three ASR (Automatic Speech Recognition) features: Streaming Transcription, Pre-recorded Transcription, and Pre-recorded Translation.

## Streaming Transcription

Convert audio to text in real-time via WebSocket connections. Ideal for voice agents and live applications.

**Available Models:**
- [`fireworks-asr-large`](https://app.fireworks.ai/models/fireworks/fireworks-asr-large): Cost-efficient for real-time transcription
- [`fireworks-asr-v2`](https://app.fireworks.ai/models/fireworks/fireworks-asr-v2): Next-generation, ultra-low latency

> [!example]
> - [Python notebook](https://colab.research.google.com/github/fw-ai/cookbook/blob/main/archived/learn/audio/audio_streaming_speech_to_text/audio_streaming_speech_to_text.ipynb)
> - [Python cookbook](https://github.com/fw-ai/cookbook/blob/main/archived/learn/audio/audio_streaming_speech_to_text/python)
> - [Source code](https://github.com/fw-ai/cookbook/tree/main/archived/learn/audio/audio_streaming_speech_to_text)

For full details, see [[024-api-reference-audio-streaming-transcriptions|Audio Streaming Transcriptions]].

## Pre-recorded Transcription

Convert audio files to text. Supports files up to 1GB in MP3, FLAC, WAV formats. Transcribe hours of audio in minutes.

**Available Models:**
- [`whisper-v3`](https://app.fireworks.ai/models/fireworks/whisper-v3): Highest accuracy
- [`whisper-v3-turbo`](https://app.fireworks.ai/models/fireworks/whisper-v3-turbo): Faster processing

> [!example]
> [Python notebook](https://colab.research.google.com/github/fw-ai/cookbook/blob/main/archived/learn/audio/audio_prerecorded_speech_to_text/audio_prerecorded_speech_to_text.ipynb)

For full details, see [[287-api-reference-audio-transcriptions|Audio Transcriptions]].

## Pre-recorded Translation

Translate audio from any supported language to English. Supports files up to 1GB in MP3, FLAC, WAV formats.

For full details, see [[288-api-reference-audio-translations|Audio Translations]].

## Supported Languages

95+ languages supported including English, Spanish, French, German, Chinese, Japanese, Russian, Portuguese, and more. See the [complete language list](https://docs.fireworks.ai/api-reference/audio-transcriptions#supported-languages).

## Common Use Cases

- **Call Center / Customer Service**: Transcribe or translate customer calls
- **Note Taking**: Transcribe audio for automated note taking
- **Content Accessibility**: Add captions and transcripts to audio/video content

> [!tip]
> For advanced features like speaker diarization and custom prompts, see the full [[287-api-reference-audio-transcriptions|Transcription API documentation]].

#asr-features #speech-recognition #audio-processing
