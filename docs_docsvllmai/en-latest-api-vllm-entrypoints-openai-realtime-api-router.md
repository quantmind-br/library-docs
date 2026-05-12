---
title: api_router - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/openai/realtime/api_router/
source: sitemap
fetched_at: 2026-05-07T21:20:19.810201027-03:00
rendered_js: false
word_count: 91
summary: This document outlines the WebSocket protocol for streaming realtime audio transcription, including connection steps, event flow, and required audio encoding formats.
tags:
    - websocket
    - realtime-audio
    - transcription
    - api-protocol
    - pcm16
    - streaming-data
category: api
---

WebSocket endpoint for realtime audio transcription.

Protocol: 1. Client connects to ws://host/v1/realtime 2. Server sends session.created event 3. Client optionally sends session.update with model/params 4. Client sends input\_audio\_buffer.commit when ready 5. Client sends input\_audio\_buffer.append events with base64 PCM16 chunks 6. Server processes and sends transcription.delta events 7. Server sends transcription.done with final text + usage 8. Repeat from step 5 for next utterance 9. Optionally, client sends input\_audio\_buffer.commit with final=True to signal audio input is finished. Useful when streaming audio files

Audio format: PCM16, 16kHz, mono, base64-encoded

Source code in `vllm/entrypoints/openai/realtime/api_router.py`

```
@router.websocket("/v1/realtime")
async defrealtime_endpoint(websocket: WebSocket):
"""WebSocket endpoint for realtime audio transcription.

    Protocol:
    1. Client connects to ws://host/v1/realtime
    2. Server sends session.created event
    3. Client optionally sends session.update with model/params
    4. Client sends input_audio_buffer.commit when ready
    5. Client sends input_audio_buffer.append events with base64 PCM16 chunks
    6. Server processes and sends transcription.delta events
    7. Server sends transcription.done with final text + usage
    8. Repeat from step 5 for next utterance
    9. Optionally, client sends input_audio_buffer.commit with final=True
       to signal audio input is finished. Useful when streaming audio files

    Audio format: PCM16, 16kHz, mono, base64-encoded
    """
    app = websocket.app
    serving = app.state.openai_serving_realtime

    connection = RealtimeConnection(websocket, serving)
    await connection.handle_connection()
```