---
title: Speech to Text | Mistral Docs
url: https://docs.mistral.ai/studio-api/audio/speech_to_text
source: sitemap
fetched_at: 2026-04-26T04:12:04.851863299-03:00
rendered_js: false
word_count: 350
summary: Audio transcription services overview covering Voxtral Mini Transcribe V2 for batch processing and Voxtral Realtime for low-latency live applications.
tags:
    - audio-transcription
    - speech-to-text
    - voice-agents
    - streaming-architecture
    - speaker-diarization
    - model-deployment
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Speech to Text

Mistral's Audio & Transcription services convert speech to text with high accuracy and low latency.

![Audio architecture](https://docs.mistral.ai/img/audio.png)

## Models

### Voxtral Mini Transcribe V2

Batch transcription model with:

| Feature | Description |
|---------|-------------|
| High accuracy | Industry-leading transcription quality with low word error rates |
| Speaker diarization | Automatically identifies and labels different speakers |
| Context biasing | Custom vocabulary for domain-specific terms |
| Word-level timestamps | Precise timestamps for each word |
| Multilingual | 13 languages: English, Chinese, Hindi, Spanish, Arabic, French, Portuguese, Russian, German, Japanese, Korean, Italian, Dutch |
| Noise robustness | High accuracy in challenging acoustic environments |
| Long audio | Processes recordings up to 3 hours |

### Voxtral Realtime

Live transcription model with:

| Feature | Description |
|---------|-------------|
| Ultra-low latency | Configurable down to sub-200ms |
| Streaming architecture | Transcribes audio as it arrives |
| Multilingual | Strong performance in 13 languages |
| Edge deployment | 4B parameter footprint for privacy-first applications |
| Open weights | Apache 2.0 license on [Hugging Face](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602) |

> [!info] Both models support GDPR and HIPAA-compliant deployments via secure on-premise or private cloud setups.

## Getting Started

- [**Offline Transcription**](https://docs.mistral.ai/studio-api/audio/speech_to_text/offline_transcription) — Batch transcription with Voxtral Mini Transcribe V2
- [**Realtime Transcription**](https://docs.mistral.ai/studio-api/audio/speech_to_text/realtime_transcription) — Live transcription with Voxtral Realtime

> [!tip] Need to transcribe multiple files? Use the [Batch feature](https://docs.mistral.ai/studio-api/batch-processing) via API.

#audio-transcription #speech-to-text #voice-agents #streaming-architecture #speaker-diarization #model-deployment
