---
title: Audio & Transcription | Mistral Docs
url: https://docs.mistral.ai/capabilities/audio_transcription
source: crawler
fetched_at: 2026-01-29T07:33:08.506357293-03:00
rendered_js: false
word_count: 346
summary: This document explains how to utilize audio input capabilities for chat and transcription using Voxtral models, detailing the available endpoints and configuration parameters.
tags:
    - audio-input
    - transcription
    - voxtral
    - multimodal
    - api-integration
    - speech-to-text
category: guide
---

Audio input capabilities enable models to chat and understand audio directly, this can be used for both chat use cases via audio or for optimal transcription purposes.

![audio_graph](https://docs.mistral.ai/img/audio.png)![audio_graph](https://docs.mistral.ai/img/audio_dark.png)

### Models with Audio Capabilities

Audio capable models:

- **Voxtral Small** (`voxtral-small-latest`) with audio input for [chat](#chat-with-audio) use cases.
- **Voxtral Mini** (`voxtral-mini-latest`) with audio input for [chat](#chat-with-audio) use cases
- And **Voxtral Mini Transcribe** (`voxtral-mini-latest` via `audio/transcriptions`), with an efficient [transcription](#transcription) only service.

### Use Audio with Instruction Following models

Our Voxtral models are capable of being used for chat use cases with our chat completions endpoint.

Before continuing, we recommend reading the [Chat Competions](https://docs.mistral.ai/capabilities/completion) documentation to learn more about the chat completions API and how to use it before proceeding.

To pass a local audio file, you can encode it in base64 and pass it as a string.

Below you can find a few of the multiple use cases possible, by leveraging the audio capabilities of our models.

![Cat head](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fcat_head.png&w=48&q=75)

¡Meow! Click one of the tabs above to learn more.

### Transcribe any Audio

Transcription provides an optimized endpoint for transcription purposes and currently supports `voxtral-mini-latest`, which runs **Voxtral Mini Transcribe**.

**Parameters**  
We provide different settings and parameters for transcription, such as:

- `timestamp_granularities`: This allows you to set timestamps to track not only "what" was said but also "when". You can find more about timestamps [here](#transcription-with-timestamps).
- `language`: Our transcription service also works as a language detection service. However, you can manually set the language of the transcription for better accuracy if the language of the audio is already known.

Among the different methods to pass the audio, you can directly provide a path to a local file to upload and transcribe it as follows:

Below you can find a few examples leveraging the audio transcription endpoint.

![Cat head](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fcat_head.png&w=48&q=75)

¡Meow! Click one of the tabs above to learn more.

You can request timestamps for the transcription by passing the `timestamp_granularities` parameter, currently supporting `segment`.  
It will return the start and end time of each segment in the audio file.

`timestamp_granularities` is currently not compatible with `language`, please use either one or the other.