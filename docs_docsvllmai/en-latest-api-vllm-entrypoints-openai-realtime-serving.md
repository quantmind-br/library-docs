---
title: serving - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/openai/realtime/serving/
source: sitemap
fetched_at: 2026-05-07T21:20:26.831320571-03:00
rendered_js: false
word_count: 115
summary: This document defines the OpenAIServingRealtime class, which facilitates real-time audio-to-text transcription by converting audio streams into formatted inputs for model generation via WebSockets.
tags:
    - audio-transcription
    - websocket-streaming
    - vllm
    - real-time-processing
    - model-serving
    - async-processing
category: reference
---

## OpenAIServingRealtime [¶](#vllm.entrypoints.openai.realtime.serving.OpenAIServingRealtime "Permanent link")

Bases: `OpenAIServing`

Realtime audio transcription service via WebSocket streaming.

Provides streaming audio-to-text transcription by transforming audio chunks into StreamingInput objects that can be consumed by the engine.

Source code in `vllm/entrypoints/openai/realtime/serving.py`

```
classOpenAIServingRealtime(OpenAIServing):
"""Realtime audio transcription service via WebSocket streaming.

    Provides streaming audio-to-text transcription by transforming audio chunks
    into StreamingInput objects that can be consumed by the engine.
    """

    def__init__(
        self,
        engine_client: EngineClient,
        models: OpenAIServingModels,
        *,
        request_logger: RequestLogger | None,
    ):
        super().__init__(
            engine_client=engine_client,
            models=models,
            request_logger=request_logger,
        )

        self.task_type: Literal["realtime"] = "realtime"

        logger.info("OpenAIServingRealtime initialized for task: %s", self.task_type)

    @cached_property
    defmodel_cls(self) -> type[SupportsRealtime]:
"""Get the model class that supports transcription."""
        fromvllm.model_executor.model_loaderimport get_model_cls

        model_cls = get_model_cls(self.model_config)
        return cast(type[SupportsRealtime], model_cls)

    async deftranscribe_realtime(
        self,
        audio_stream: AsyncGenerator[np.ndarray, None],
        input_stream: asyncio.Queue[list[int]],
    ) -> AsyncGenerator[StreamingInput, None]:
"""Transform audio stream into StreamingInput for engine.generate().

        Args:
            audio_stream: Async generator yielding float32 numpy audio arrays
            input_stream: Queue containing context token IDs from previous
                generation outputs. Used for autoregressive multi-turn
                processing where each generation's output becomes the context
                for the next iteration.

        Yields:
            StreamingInput objects containing audio prompts for the engine
        """
        model_config = self.model_config
        renderer = self.renderer

        # mypy is being stupid
        # TODO(Patrick) - fix this
        stream_input_iter = cast(
            AsyncGenerator[PromptType, None],
            self.model_cls.buffer_realtime_audio(
                audio_stream, input_stream, model_config
            ),
        )

        async for prompt in stream_input_iter:
            parsed_prompt = parse_model_prompt(model_config, prompt)
            (engine_input,) = await renderer.render_cmpl_async([parsed_prompt])

            yield StreamingInput(prompt=engine_input)
```

### model\_cls `cached` `property` [¶](#vllm.entrypoints.openai.realtime.serving.OpenAIServingRealtime.model_cls "Permanent link")

Get the model class that supports transcription.

### transcribe\_realtime `async` [¶](#vllm.entrypoints.openai.realtime.serving.OpenAIServingRealtime.transcribe_realtime "Permanent link")

Transform audio stream into StreamingInput for engine.generate().

Parameters:

Name Type Description Default `audio_stream` `AsyncGenerator[ndarray, None]`

Async generator yielding float32 numpy audio arrays

*required* `input_stream` `Queue[list[int]]`

Queue containing context token IDs from previous generation outputs. Used for autoregressive multi-turn processing where each generation's output becomes the context for the next iteration.

*required*

Yields:

Type Description `AsyncGenerator[StreamingInput, None]`

StreamingInput objects containing audio prompts for the engine

Source code in `vllm/entrypoints/openai/realtime/serving.py`

```
async deftranscribe_realtime(
    self,
    audio_stream: AsyncGenerator[np.ndarray, None],
    input_stream: asyncio.Queue[list[int]],
) -> AsyncGenerator[StreamingInput, None]:
"""Transform audio stream into StreamingInput for engine.generate().

    Args:
        audio_stream: Async generator yielding float32 numpy audio arrays
        input_stream: Queue containing context token IDs from previous
            generation outputs. Used for autoregressive multi-turn
            processing where each generation's output becomes the context
            for the next iteration.

    Yields:
        StreamingInput objects containing audio prompts for the engine
    """
    model_config = self.model_config
    renderer = self.renderer

    # mypy is being stupid
    # TODO(Patrick) - fix this
    stream_input_iter = cast(
        AsyncGenerator[PromptType, None],
        self.model_cls.buffer_realtime_audio(
            audio_stream, input_stream, model_config
        ),
    )

    async for prompt in stream_input_iter:
        parsed_prompt = parse_model_prompt(model_config, prompt)
        (engine_input,) = await renderer.render_cmpl_async([parsed_prompt])

        yield StreamingInput(prompt=engine_input)
```