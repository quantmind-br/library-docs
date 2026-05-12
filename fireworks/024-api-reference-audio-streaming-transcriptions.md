---
title: Streaming Transcription
url: https://docs.fireworks.ai/api-reference/audio-streaming-transcriptions
source: sitemap
fetched_at: 2026-04-27T20:15:03.25375168-03:00
rendered_js: false
word_count: 963
summary: This document serves as a comprehensive guide to using Fireworks' real-time Speech-to-Text (ASR) service via WebSockets, detailing API endpoints, required parameters, client and server message formats, and best practices for handling streaming sessions.
tags:
    - api
    - websockets
    - asr
    - streaming
    - audio-transcription
    - fireworks-ai
    - guide
category: guide
optimized: true
optimized_at: 2026-04-27T23:27:00Z
---
Fireworks provides serverless, real-time ASR via WebSocket endpoints.

## URLs

| Version | Description | URL |
|---------|-------------|-----|
| **v1** (default) | Production-ready, recommended for all use cases | `wss://audio-streaming.api.fireworks.ai/v1/audio/transcriptions/streaming` |
| **v2** (preview) | Lower latency, higher accuracy in noisy situations | `wss://audio-streaming-v2.api.fireworks.ai/v1/audio/transcriptions/streaming` |

## Query Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `Authorization` | string | — | Your Fireworks API key (e.g., `Authorization=API_KEY`). Can also be provided as a query param. |
| `api_key` | string | — | Fireworks API key when headers cannot be set (e.g., browser WebSocket connections) |
| `response_format` | string | `"verbose_json"` | Format for response; only `verbose_json` is recommended for streaming |
| `language` | string | — | Target language for transcription. See [Supported Languages](#supported-languages) below. |
| `prompt` | string | — | Input prompt for the model (custom words or transcription style). E.g., `Um, here's, uh, what was recorded.` will include filler words. |
| `temperature` | number | — | Sampling temperature for decoding text tokens |
| `timestamp_granularities` | string \| array | `null` | Set to `word,segment` to enable timestamps. Use an array in client libraries; comma-separated string only works in URLs. |

## Client messages

### Binary audio chunks

Stream short audio chunks (50–400ms) in binary frames:

- Format: PCM 16-bit little-endian
- Sample rate: 16 kHz
- Channels: mono (single channel)
- Chunk size: 50ms = 800 samples at 16kHz

> [!tip]
> Resample audio to 16 kHz if needed, convert to mono, then send 50ms chunks.

### SttStateClear

Initiate context cleanup:

```json
{
  "event_id": "unique-identifier",
  "type": "stt.state.clear",
  "context_id": "session-id-to-clear"
}
```

### SttInputTrace

Initiate tracing:

```json
{
  "event_id": "unique-identifier",
  "type": "stt.input.trace",
  "trace_id": "correlation-id"
}
```

## Server messages

### Transcription message

```json
{
  "task": "transcribe",
  "language": "en",
  "text": "The transcribed text",
  "words": [
    {
      "word": "Hello",
      "language": "en",
      "probability": 0.99,
      "hallucination_score": 0.01,
      "start": 0.5,
      "end": 0.8,
      "spoken": true
    }
  ],
  "segments": [
    {
      "text": "This is the first sentence",
      "language": "en",
      "words": [...],
      "start": 0.5,
      "end": 2.0
    }
  ]
}
```

| Field | Type | Description |
|-------|------|-------------|
| `task` | string | `"transcribe"` or `"translate"` |
| `language` | string | Language code(s) of the text |
| `text` | string | Transcribed/translated text |
| `words` | array | Extracted words with timestamps (when `timestamp_granularities=word,segment`) |
| `segments` | array | Segments with details (when `timestamp_granularities=word,segment`) |

### SttStateCleared

```json
{
  "event_id": "unique-identifier",
  "type": "stt.state.cleared",
  "context_id": "cleared-context-id"
}
```

### SttOutputTrace

```json
{
  "event_id": "unique-identifier",
  "type": "stt.output.trace",
  "trace_id": "correlation-id"
}
```

## Handling responses

The client maintains a state dictionary. When the server sends the first transcription message:

```python
# Server initial message:
{
    "segments": [
        {"id": "0", "text": "This is the first sentence"},
        {"id": "1", "text": "This is the second sentence"}
    ]
}

# Client initial state:
{
    "0": "This is the first sentence",
    "1": "This is the second sentence",
}
```

On updates, the client overwrites existing segments by ID and adds new ones:

```python
# Server update:
{"segments": [
    {"id": "1", "text": "This is the second sentence modified"},
    {"id": "2", "text": "This is the third sentence"}
]}

# Client updated state:
{
    "0": "This is the first sentence",       # unchanged
    "1": "This is the second sentence modified",  # overwritten
    "2": "This is the third sentence",       # new
}
```

## Handling connection interruptions

### When a connection drops

If the WebSocket is disrupted, your application must:
1. Initialize a new WebSocket connection
2. Start a fresh streaming session
3. Begin sending audio as soon as the server confirms connection

### Avoiding audio loss during reconnects

Buffer audio data while reconnecting to minimize dropped segments.

### Keeping timestamps continuous

Each new WebSocket session resets timestamps to `00:00:00`. To maintain a continuous timeline:

1. Track a "stream start offset" in your app
2. Add that offset to timestamps from each new session

## Example usage

- [Python notebook](https://colab.research.google.com/github/fw-ai/cookbook/blob/main/archived/learn/audio/audio_streaming_speech_to_text/audio_streaming_speech_to_text.ipynb)
- [Python sources](https://github.com/fw-ai/cookbook/tree/main/archived/learn/audio/audio_streaming_speech_to_text/python)
- [Node.js sources](https://github.com/fw-ai/cookbook/tree/main/archived/learn/audio/audio_streaming_speech_to_text/nodejs)

## Dedicated endpoint

For fixed throughput and predictable SLAs, request a dedicated endpoint at [inquiries@fireworks.ai](mailto:inquiries@fireworks.ai) or [Discord](https://discord.gg/fireworks-ai).

## Supported Languages

| Code | Language | Code | Language |
|------|----------|------|----------|
| en | English | fr | French |
| zh | Chinese | ja | Japanese |
| de | German | pt | Portuguese |
| es | Spanish | tr | Turkish |
| ru | Russian | pl | Polish |
| ko | Korean | ca | Catalan |
| nl | Dutch | ar | Arabic |
| sv | Swedish | it | Italian |
| id | Indonesian | hi | Hindi |
| fi | Finnish | vi | Vietnamese |
| he | Hebrew | uk | Ukrainian |
| el | Greek | ms | Malay |
| cs | Czech | ro | Romanian |
| da | Danish | hu | Hungarian |
| ta | Tamil | no | Norwegian |
| th | Thai | ur | Urdu |
| hr | Croatian | bg | Bulgarian |
| lt | Lithuanian | la | Latin |
| mi | Maori | ml | Malayalam |
| cy | Welsh | sk | Slovak |
| te | Telugu | fa | Persian |
| lv | Latvian | bn | Bengali |
| sr | Serbian | az | Azerbaijani |
| is | Icelandic | sq | Albanian |
| sl | Slovenian | kn | Kannada |
| et | Estonian | mk | Macedonian |
| br | Breton | eu | Basque |
| hy | Armenian | ne | Nepali |
| mn | Mongolian | bs | Bosnian |
| kk | Kazakh | sw | Swahili |
| gl | Galician | mr | Marathi |
| pa | Punjabi | si | Sinhala |
| km | Khmer | sn | Shona |
| yo | Yoruba | so | Somali |
| af | Afrikaans | oc | Occitan |
| ka | Georgian | be | Belarusian |
| tg | Tajik | sd | Sindhi |
| gu | Gujarati | am | Amharic |
| yi | Yiddish | lo | Lao |
| uz | Uzbek | fo | Faroese |
| ht | Haitian Creole | ps | Pashto |
| tk | Turkmen | nn | Nynorsk |
| mt | Maltese | sa | Sanskrit |
| lb | Luxembourgish | my | Myanmar |
| bo | Tibetan | tl | Tagalog |
| mg | Malagasy | as | Assamese |
| tt | Tatar | haw | Hawaiian |
| ln | Lingala | ha | Hausa |
| ba | Bashkir | jw | Javanese |
| su | Sundanese | yue | Cantonese |
| zh-hant | Traditional Chinese | zh-hans | Simplified Chinese |