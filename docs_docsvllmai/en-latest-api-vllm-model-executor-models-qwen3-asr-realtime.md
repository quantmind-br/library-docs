---
title: qwen3_asr_realtime - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/qwen3_asr_realtime/
source: sitemap
fetched_at: 2026-05-07T21:33:00.267880639-03:00
rendered_js: false
word_count: 32
summary: This document describes the implementation of an audio buffering class designed to accumulate and segment audio samples for real-time inference with the Qwen3-ASR model.
tags:
    - audio-processing
    - real-time-streaming
    - vllm
    - speech-recognition
    - data-buffering
category: reference
---

## vllm.model\_executor.models.qwen3\_asr\_realtime [¶](#vllm.model_executor.models.qwen3_asr_realtime "Permanent link")

Inference-only Qwen3-ASR realtime model.

## Qwen3ASRRealtimeBuffer [¶](#vllm.model_executor.models.qwen3_asr_realtime.Qwen3ASRRealtimeBuffer "Permanent link")

Audio buffer for Qwen3-ASR realtime streaming.

Accumulates audio samples and yields segments when enough audio has been buffered for processing.

Source code in `vllm/model_executor/models/qwen3_asr_realtime.py`

```
classQwen3ASRRealtimeBuffer:
"""Audio buffer for Qwen3-ASR realtime streaming.

    Accumulates audio samples and yields segments when enough
    audio has been buffered for processing.
    """

    def__init__(self, sampling_rate: int, segment_duration_s: float = 5.0):
        self._sampling_rate = sampling_rate
        self._segment_size = int(segment_duration_s * sampling_rate)

        self._buffer_size = _PRE_ALLOCATE_BUFFER_SIZE_IN_S * sampling_rate
        self._buffer: np.ndarray = np.empty(self._buffer_size, dtype=np.float32)
        self._filled_len = 0

    defwrite_audio(self, audio: np.ndarray) -> None:
        put_end = self._filled_len + len(audio)
        if put_end > self._buffer_size:
            new_size = max(self._buffer_size * 2, put_end)
            new_buffer = np.empty(new_size, dtype=np.float32)
            new_buffer[: self._filled_len] = self._buffer[: self._filled_len]
            self._buffer = new_buffer
            self._buffer_size = new_size

        self._buffer[self._filled_len : put_end] = audio
        self._filled_len = put_end

    defread_audio(self) -> np.ndarray | None:
        if self._filled_len < self._segment_size:
            return None

        segment = self._buffer[: self._segment_size].copy()
        remaining = self._filled_len - self._segment_size
        if remaining > 0:
            self._buffer[:remaining] = self._buffer[
                self._segment_size : self._filled_len
            ]
        self._filled_len = remaining
        return segment

    defflush(self) -> np.ndarray | None:
        if self._filled_len == 0:
            return None
        audio = self._buffer[: self._filled_len].copy()
        self._filled_len = 0
        return audio
```