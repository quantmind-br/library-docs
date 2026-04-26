---
title: Audio Speech
url: https://docs.mistral.ai/api/endpoint/audio/speech
source: sitemap
fetched_at: 2026-04-26T04:01:17.144366259-03:00
rendered_js: false
word_count: 68
summary: API specification for the speech generation endpoint, detailing request parameters and response formats for converting text into audio.
tags:
    - text-to-speech
    - audio-generation
    - api-endpoint
    - speech-synthesis
    - voice-cloning
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## POST /v1/audio/speech

Generate speech from text using a saved voice or reference audio clip.

### Parameters

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `input` | string | - | Text to generate speech from |
| `AdditionalProperties` | map | - | Additional configuration |
| `audio_reference` | string (base64) | - | Base64-encoded audio for zero-shot voice cloning |
| `response_format` | "pcm"\|"wav"\|"mp3"\|"flac"\|"opus" | - | Output audio format |
| `stream` | boolean | `false` | Stream audio data |
| `voice` | string | - | Preset or custom voice identifier |

### Response Formats

- `200 (application/json)` — Speech audio data
- `200 (text/event-stream)` — Streaming audio

### Code Example

```bash
curl https://api.mistral.ai/v1/audio/speech \
  -X POST \
  -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
  -H 'Content-Type: application/json' \
  -d '{"input": "ipsum eiusmod"}'
```

### Response Example

```json
{"audio_data": "ipsum eiusmod"}
```

#text-to-speech #audio-generation #speech-synthesis
