---
title: Realtime | Mistral Docs
url: https://docs.mistral.ai/studio-api/audio/speech_to_text/realtime_transcription
source: sitemap
fetched_at: 2026-04-26T04:12:08.821904926-03:00
rendered_js: false
word_count: 945
summary: Implement real-time audio transcription using dual-delay streams to balance processing speed and transcription accuracy.
tags:
    - real-time-transcription
    - audio-streaming
    - dual-delay
    - speech-to-text
    - python-sdk
    - latency-optimization
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Realtime Transcription

Transcribe audio as it is being spoken or recorded. Useful for live captioning, voice assistants, or real-time note-taking.

## Model

**Voxtral Mini Transcribe Realtime** (`voxtral-mini-transcribe-realtime-2602`) — Optimized for live transcription with ultra-low latency and high accuracy.

> [!warning] Realtime is currently **not** compatible with the `diarize` parameter. Use **either one or the other**.

## Installation

```bash
pip install "mistralai[realtime]"
```

## Basic Usage

### Simple Streaming

```python
import asyncio
from mistralai.client import MistralRealtimeTranscription

async def transcribe():
    client = MistralRealtimeTranscription(api_key="your-api-key")

    async for event in client.transcribe(
        model="voxtral-mini-transcribe-realtime-2602",
        audio_stream=your_audio_source
    ):
        print(event.content)
```

### Target Delay

Specify `target_streaming_delay_ms` to gather context and improve accuracy:

```python
async for event in client.transcribe(
    model="voxtral-mini-transcribe-realtime-2602",
    audio_stream=your_audio_source,
    target_streaming_delay_ms=1000  # 1 second delay for context
):
    print(event.content)
```

## Dual Delay Transcription

Balance between speed and accuracy using two parallel streams:

| Stream | Delay | Characteristics |
|--------|-------|----------------|
| **Fast Stream** | ~240ms | Quick but less accurate |
| **Slow Stream** | ~2400ms | More accurate via additional context |

### How It Works

1. **Fast Stream** — Transcribes with minimal delay for immediate feedback
2. **Slow Stream** — Transcribes with longer delay for higher accuracy
3. **Combined Output** — Merges results from both streams

### Use Cases

- Live captioning for presentations or meetings
- Real-time note-taking applications
- Voice assistants requiring immediate feedback

### Implementation

```python
import argparse
import asyncio
from mistralai.client import MistralRealtimeTranscription

async def dual_delay_transcribe(
    api_key: str,
    fast_delay_ms: int = 240,
    slow_delay_ms: int = 2400,
    sample_rate: int = 16000
):
    """Dual delay transcription example."""
    client = MistralRealtimeTranscription(api_key=api_key)

    # Create fast and slow streams
    fast_stream = client.transcribe(
        model="voxtral-mini-transcribe-realtime-2602",
        audio_stream=audio_source,
        target_streaming_delay_ms=fast_delay_ms
    )

    slow_stream = client.transcribe(
        model="voxtral-mini-transcribe-realtime-2602",
        audio_stream=audio_source,
        target_streaming_delay_ms=slow_delay_ms
    )

    # Process both streams
    async for fast_event in fast_stream:
        # Process fast output
        print(f"FAST: {fast_event.content}")

    async for slow_event in slow_stream:
        # Process slow output
        print(f"SLOW: {slow_event.content}")
```

## State Management

`DualTranscriptState` tracks both stream states:

| Field | Description |
|-------|-------------|
| `fast_text` | Current transcription from fast stream |
| `slow_text` | Current transcription from slow stream |
| `fast_status` | Fast stream status |
| `slow_status` | Slow stream status |
| `error` | Any errors encountered |

## Event Status

| Status | Description |
|--------|-------------|
| `session_created` | Transcription session initialized |
| `transcript` | New transcription text available |
| `done` | Transcription complete |

#real-time-transcription #audio-streaming #dual-delay #speech-to-text #python-sdk #latency-optimization
