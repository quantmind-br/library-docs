---
title: protocol - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/openai/realtime/protocol/
source: sitemap
fetched_at: 2026-05-07T21:20:24.048413848-03:00
rendered_js: false
word_count: 81
summary: This document defines the data models and message schemas for the vLLM OpenAI-compatible realtime protocol, covering error handling, audio processing, session management, and transcription events.
tags:
    - vllm
    - openai-api
    - realtime-protocol
    - data-models
    - audio-processing
    - session-management
    - transcription
category: reference
---

## ErrorEvent [¶](#vllm.entrypoints.openai.realtime.protocol.ErrorEvent "Permanent link")

Bases: `OpenAIBaseModel`

Error notification

Source code in `vllm/entrypoints/openai/realtime/protocol.py`

```
classErrorEvent(OpenAIBaseModel):
"""Error notification"""

    type: Literal["error"] = "error"
    error: str
    code: str | None = None
```

## InputAudioBufferAppend [¶](#vllm.entrypoints.openai.realtime.protocol.InputAudioBufferAppend "Permanent link")

Bases: `OpenAIBaseModel`

Append audio chunk to buffer

Source code in `vllm/entrypoints/openai/realtime/protocol.py`

```
classInputAudioBufferAppend(OpenAIBaseModel):
"""Append audio chunk to buffer"""

    type: Literal["input_audio_buffer.append"] = "input_audio_buffer.append"
    audio: str  # base64-encoded PCM16 @ 16kHz
```

## InputAudioBufferCommit [¶](#vllm.entrypoints.openai.realtime.protocol.InputAudioBufferCommit "Permanent link")

Bases: `OpenAIBaseModel`

Process accumulated audio buffer

Source code in `vllm/entrypoints/openai/realtime/protocol.py`

```
classInputAudioBufferCommit(OpenAIBaseModel):
"""Process accumulated audio buffer"""

    type: Literal["input_audio_buffer.commit"] = "input_audio_buffer.commit"
    final: bool = False
```

## SessionCreated [¶](#vllm.entrypoints.openai.realtime.protocol.SessionCreated "Permanent link")

Bases: `OpenAIBaseModel`

Connection established notification

Source code in `vllm/entrypoints/openai/realtime/protocol.py`

```
classSessionCreated(OpenAIBaseModel):
"""Connection established notification"""

    type: Literal["session.created"] = "session.created"
    id: str = Field(default_factory=lambda: f"sess-{random_uuid()}")
    created: int = Field(default_factory=lambda: int(time.time()))
```

## SessionUpdate [¶](#vllm.entrypoints.openai.realtime.protocol.SessionUpdate "Permanent link")

Bases: `OpenAIBaseModel`

Configure session parameters

Source code in `vllm/entrypoints/openai/realtime/protocol.py`

```
classSessionUpdate(OpenAIBaseModel):
"""Configure session parameters"""

    type: Literal["session.update"] = "session.update"
    model: str | None = None
```

## TranscriptionDelta [¶](#vllm.entrypoints.openai.realtime.protocol.TranscriptionDelta "Permanent link")

Bases: `OpenAIBaseModel`

Incremental transcription text

Source code in `vllm/entrypoints/openai/realtime/protocol.py`

```
classTranscriptionDelta(OpenAIBaseModel):
"""Incremental transcription text"""

    type: Literal["transcription.delta"] = "transcription.delta"
    delta: str  # Incremental text
```

## TranscriptionDone [¶](#vllm.entrypoints.openai.realtime.protocol.TranscriptionDone "Permanent link")

Bases: `OpenAIBaseModel`

Final transcription with usage stats

Source code in `vllm/entrypoints/openai/realtime/protocol.py`

```
classTranscriptionDone(OpenAIBaseModel):
"""Final transcription with usage stats"""

    type: Literal["transcription.done"] = "transcription.done"
    text: str  # Complete transcription
    usage: UsageInfo | None = None
```