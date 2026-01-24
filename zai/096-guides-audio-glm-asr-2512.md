---
title: GLM-ASR-2512 - Overview - Z.AI DEVELOPER DOCUMENT
url: https://docs.z.ai/guides/audio/glm-asr-2512
source: llms
fetched_at: 2026-01-24T11:22:10.024597767-03:00
rendered_js: false
word_count: 102
summary: This document introduces the GLM-ASR-2512 speech recognition model and provides instructions for implementing audio transcriptions through basic and streaming API calls.
tags:
    - speech-recognition
    - asr
    - audio-transcription
    - glm-asr-2512
    - curl
    - api-integration
category: tutorial
---

GLM-ASR-2512 is Z.AI’s next-generation speech recognition model, enabling real-time conversion of speech into high-quality text. Whether for daily conversations, meeting minutes, work documents, or scenarios involving specialized terminology, it delivers precise recognition and conversion, significantly boosting input and recording efficiency. The model maintains industry-leading recognition performance across diverse scenarios and accents, achieving a Character Error Rate (CER) of just 0.0717. This delivers a fast and reliable voice input experience.

## Usage

## Resources

- [API Documentation](https://docs.z.ai/api-reference/audio/audio-transcriptions): Learn how to call the API.

## Introducing GLM-ASR-2512

## Quick Start

The following is a full sample code to help you onboard `GLM-ASR-2512` with ease.

- cURL

**Basic Call**

```
curl --request POST \
    --url https://api.z.ai/api/paas/v4/audio/transcriptions \
    --header 'Authorization: Bearer API_Key' \
    --header 'Content-Type: multipart/form-data' \
    --form model=glm-asr-2512 \
    --form stream=false \
    --form file=@example-file
```

**Streaming Call**

```
curl --request POST \
    --url https://api.z.ai/api/paas/v4/audio/transcriptions \
    --header 'Authorization: Bearer API_Key' \
    --header 'Content-Type: multipart/form-data' \
    --form model=glm-asr-2512 \
    --form stream=true \
    --form file=@example-file
```