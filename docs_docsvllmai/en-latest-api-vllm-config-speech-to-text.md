---
title: speech_to_text - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/config/speech_to_text/
source: sitemap
fetched_at: 2026-05-07T21:17:15.498988688-03:00
rendered_js: false
word_count: 163
summary: This document defines the SpeechToTextParams data class, which serves as a structured container for passing configuration and audio parameters to speech-to-text generation models.
tags:
    - speech-to-text
    - parameter-definition
    - data-class
    - configuration
    - api-structure
category: reference
---

All parameters consumed by `get_generation_prompt()`.

`TranscriptionRequest.build_stt_params()` constructs this object, mapping API-level fields into typed attributes. Models only receive this object, so new parameters can be added here without changing the `get_generation_prompt` signature.

Source code in `vllm/config/speech_to_text.py`

```
@dataclass
classSpeechToTextParams:
"""All parameters consumed by ``get_generation_prompt()``.

    ``TranscriptionRequest.build_stt_params()`` constructs this object,
    mapping API-level fields into typed attributes.  Models only receive
    this object, so new parameters can be added here without changing the
    ``get_generation_prompt`` signature.
    """

    audio: np.ndarray
"""Resampled audio waveform for a single chunk."""

    stt_config: SpeechToTextConfig
"""Server-level speech-to-text configuration."""

    model_config: ModelConfig
"""Model configuration."""

    language: str | None = None
"""ISO 639-1 language code (validated / auto-detected)."""

    hotwords: str | None = None
"""
    hotwords refers to a list of important words or phrases that the model
    should pay extra attention to during transcription.
    """

    task_type: str = "transcribe"
"""``"transcribe"`` or ``"translate"``."""

    request_prompt: str = ""
"""Optional text prompt to guide the model."""

    to_language: str | None = None
"""Target language for translation (model-dependent)."""
```

### audio `instance-attribute` [¶](#vllm.config.speech_to_text.SpeechToTextParams.audio "Permanent link")

Resampled audio waveform for a single chunk.

### hotwords `class-attribute` `instance-attribute` [¶](#vllm.config.speech_to_text.SpeechToTextParams.hotwords "Permanent link")

```
hotwords: str | None = None
```

hotwords refers to a list of important words or phrases that the model should pay extra attention to during transcription.

### language `class-attribute` `instance-attribute` [¶](#vllm.config.speech_to_text.SpeechToTextParams.language "Permanent link")

```
language: str | None = None
```

ISO 639-1 language code (validated / auto-detected).

### model\_config `instance-attribute` [¶](#vllm.config.speech_to_text.SpeechToTextParams.model_config "Permanent link")

Model configuration.

### request\_prompt `class-attribute` `instance-attribute` [¶](#vllm.config.speech_to_text.SpeechToTextParams.request_prompt "Permanent link")

Optional text prompt to guide the model.

### stt\_config `instance-attribute` [¶](#vllm.config.speech_to_text.SpeechToTextParams.stt_config "Permanent link")

```
stt_config: SpeechToTextConfig
```

Server-level speech-to-text configuration.

### task\_type `class-attribute` `instance-attribute` [¶](#vllm.config.speech_to_text.SpeechToTextParams.task_type "Permanent link")

```
task_type: str = 'transcribe'
```

`"transcribe"` or `"translate"`.

### to\_language `class-attribute` `instance-attribute` [¶](#vllm.config.speech_to_text.SpeechToTextParams.to_language "Permanent link")

```
to_language: str | None = None
```

Target language for translation (model-dependent).