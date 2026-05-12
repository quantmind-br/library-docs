---
title: serving - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/openai/speech_to_text/serving/
source: sitemap
fetched_at: 2026-05-07T21:20:39.89618837-03:00
rendered_js: false
word_count: 74
summary: This document provides the API reference for the OpenAIServingTranscription and OpenAIServingTranslation classes, which implement OpenAI-compatible speech-to-text functionality within the vLLM framework.
tags:
    - api-reference
    - speech-to-text
    - vllm
    - transcription
    - translation
    - openai-compatibility
    - audio-processing
category: reference
---

## OpenAIServingTranscription [¶](#vllm.entrypoints.openai.speech_to_text.serving.OpenAIServingTranscription "Permanent link")

Bases: `OpenAISpeechToText`

Handles transcription requests.

Source code in `vllm/entrypoints/openai/speech_to_text/serving.py`

```
classOpenAIServingTranscription(OpenAISpeechToText):
"""Handles transcription requests."""

    def__init__(
        self,
        engine_client: EngineClient,
        models: OpenAIServingModels,
        *,
        request_logger: RequestLogger | None,
        return_tokens_as_token_ids: bool = False,
        enable_force_include_usage: bool = False,
    ):
        super().__init__(
            engine_client=engine_client,
            models=models,
            request_logger=request_logger,
            return_tokens_as_token_ids=return_tokens_as_token_ids,
            task_type="transcribe",
            enable_force_include_usage=enable_force_include_usage,
        )

    async defcreate_transcription(
        self,
        audio_data: bytes,
        request: TranscriptionRequest,
        raw_request: Request | None = None,
    ) -> (
        TranscriptionResponse
        | TranscriptionResponseVerbose
        | AsyncGenerator[str, None]
        | ErrorResponse
    ):
"""Transcription API similar to OpenAI's API.

        See https://platform.openai.com/docs/api-reference/audio/createTranscription
        for the API specification. This API mimics the OpenAI transcription API.
        """
        return await self._create_speech_to_text(
            audio_data=audio_data,
            request=request,
            raw_request=raw_request,
            response_class=(
                TranscriptionResponseVerbose
                if request.response_format == "verbose_json"
                else TranscriptionResponse
            ),
            stream_generator_method=self.transcription_stream_generator,
        )

    async deftranscription_stream_generator(
        self,
        request: TranscriptionRequest,
        result_generator: list[AsyncGenerator[RequestOutput, None]],
        request_id: str,
        request_metadata: RequestResponseMetadata,
        audio_duration_s: float,
        separator: str,
    ) -> AsyncGenerator[str, None]:
        generator = self._speech_to_text_stream_generator(
            request=request,
            list_result_generator=result_generator,
            request_id=request_id,
            request_metadata=request_metadata,
            audio_duration_s=audio_duration_s,
            chunk_object_type="transcription.chunk",
            response_stream_choice_class=TranscriptionResponseStreamChoice,
            stream_response_class=TranscriptionStreamResponse,
            separator=separator,
        )
        async for chunk in generator:
            yield chunk
```

### create\_transcription `async` [¶](#vllm.entrypoints.openai.speech_to_text.serving.OpenAIServingTranscription.create_transcription "Permanent link")

Transcription API similar to OpenAI's API.

See https://platform.openai.com/docs/api-reference/audio/createTranscription for the API specification. This API mimics the OpenAI transcription API.

Source code in `vllm/entrypoints/openai/speech_to_text/serving.py`

```
async defcreate_transcription(
    self,
    audio_data: bytes,
    request: TranscriptionRequest,
    raw_request: Request | None = None,
) -> (
    TranscriptionResponse
    | TranscriptionResponseVerbose
    | AsyncGenerator[str, None]
    | ErrorResponse
):
"""Transcription API similar to OpenAI's API.

    See https://platform.openai.com/docs/api-reference/audio/createTranscription
    for the API specification. This API mimics the OpenAI transcription API.
    """
    return await self._create_speech_to_text(
        audio_data=audio_data,
        request=request,
        raw_request=raw_request,
        response_class=(
            TranscriptionResponseVerbose
            if request.response_format == "verbose_json"
            else TranscriptionResponse
        ),
        stream_generator_method=self.transcription_stream_generator,
    )
```

## OpenAIServingTranslation [¶](#vllm.entrypoints.openai.speech_to_text.serving.OpenAIServingTranslation "Permanent link")

Bases: `OpenAISpeechToText`

Handles translation requests.

Source code in `vllm/entrypoints/openai/speech_to_text/serving.py`

```
classOpenAIServingTranslation(OpenAISpeechToText):
"""Handles translation requests."""

    def__init__(
        self,
        engine_client: EngineClient,
        models: OpenAIServingModels,
        *,
        request_logger: RequestLogger | None,
        return_tokens_as_token_ids: bool = False,
        enable_force_include_usage: bool = False,
    ):
        super().__init__(
            engine_client=engine_client,
            models=models,
            request_logger=request_logger,
            return_tokens_as_token_ids=return_tokens_as_token_ids,
            task_type="translate",
            enable_force_include_usage=enable_force_include_usage,
        )

    async defcreate_translation(
        self,
        audio_data: bytes,
        request: TranslationRequest,
        raw_request: Request | None = None,
    ) -> (
        TranslationResponse
        | TranslationResponseVerbose
        | AsyncGenerator[str, None]
        | ErrorResponse
    ):
"""Translation API similar to OpenAI's API.

        See https://platform.openai.com/docs/api-reference/audio/createTranslation
        for the API specification. This API mimics the OpenAI translation API.
        """
        return await self._create_speech_to_text(
            audio_data=audio_data,
            request=request,
            raw_request=raw_request,
            response_class=(
                TranslationResponseVerbose
                if request.response_format == "verbose_json"
                else TranslationResponse
            ),
            stream_generator_method=self.translation_stream_generator,
        )

    async deftranslation_stream_generator(
        self,
        request: TranslationRequest,
        result_generator: list[AsyncGenerator[RequestOutput, None]],
        request_id: str,
        request_metadata: RequestResponseMetadata,
        audio_duration_s: float,
        separator: str,
    ) -> AsyncGenerator[str, None]:
        generator = self._speech_to_text_stream_generator(
            request=request,
            list_result_generator=result_generator,
            request_id=request_id,
            request_metadata=request_metadata,
            audio_duration_s=audio_duration_s,
            chunk_object_type="translation.chunk",
            response_stream_choice_class=TranslationResponseStreamChoice,
            stream_response_class=TranslationStreamResponse,
            separator=separator,
        )
        async for chunk in generator:
            yield chunk
```

### create\_translation `async` [¶](#vllm.entrypoints.openai.speech_to_text.serving.OpenAIServingTranslation.create_translation "Permanent link")

Translation API similar to OpenAI's API.

See https://platform.openai.com/docs/api-reference/audio/createTranslation for the API specification. This API mimics the OpenAI translation API.

Source code in `vllm/entrypoints/openai/speech_to_text/serving.py`

```
async defcreate_translation(
    self,
    audio_data: bytes,
    request: TranslationRequest,
    raw_request: Request | None = None,
) -> (
    TranslationResponse
    | TranslationResponseVerbose
    | AsyncGenerator[str, None]
    | ErrorResponse
):
"""Translation API similar to OpenAI's API.

    See https://platform.openai.com/docs/api-reference/audio/createTranslation
    for the API specification. This API mimics the OpenAI translation API.
    """
    return await self._create_speech_to_text(
        audio_data=audio_data,
        request=request,
        raw_request=raw_request,
        response_class=(
            TranslationResponseVerbose
            if request.response_format == "verbose_json"
            else TranslationResponse
        ),
        stream_generator_method=self.translation_stream_generator,
    )
```