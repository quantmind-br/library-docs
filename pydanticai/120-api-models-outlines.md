---
title: pydantic_ai.models.outlines - Pydantic AI
url: https://ai.pydantic.dev/api/models/outlines/
source: sitemap
fetched_at: 2026-01-22T22:24:40.557555818-03:00
rendered_js: false
word_count: 178
summary: This document defines the OutlinesModel class, which integrates the Outlines library to provide structured text generation capabilities across various backends. It includes factory methods for initializing models from Hugging Face, Llama.cpp, MLX, and SGLang.
tags:
    - outlines-library
    - hugging-face
    - llama-cpp
    - mlx
    - sglang
    - structured-generation
    - model-integration
category: api
---

```
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
```

```
@dataclass(init=False)
classOutlinesModel(Model):
"""A model that relies on the Outlines library to run non API-based models."""

    def__init__(
        self,
        model: OutlinesBaseModel | OutlinesAsyncBaseModel,
        *,
        provider: Literal['outlines'] | Provider[OutlinesBaseModel] = 'outlines',
        profile: ModelProfileSpec | None = None,
        settings: ModelSettings | None = None,
    ):
"""Initialize an Outlines model.

        Args:
            model: The Outlines model used for the model.
            provider: The provider to use for OutlinesModel. Can be either the string 'outlines' or an
                instance of `Provider[OutlinesBaseModel]`. If not provided, the other parameters will be used.
            profile: The model profile to use. Defaults to a profile picked by the provider.
            settings: Default model settings for this model instance.
        """
        self.model: OutlinesBaseModel | OutlinesAsyncBaseModel = model
        self._model_name: str = 'outlines-model'

        if isinstance(provider, str):
            provider = infer_provider(provider)

        super().__init__(settings=settings, profile=profile or provider.model_profile)

    @classmethod
    deffrom_transformers(
        cls,
        hf_model: transformers.modeling_utils.PreTrainedModel,
        hf_tokenizer_or_processor: transformers.tokenization_utils.PreTrainedTokenizer
        | transformers.processing_utils.ProcessorMixin,
        *,
        provider: Literal['outlines'] | Provider[OutlinesBaseModel] = 'outlines',
        profile: ModelProfileSpec | None = None,
        settings: ModelSettings | None = None,
    ):
"""Create an Outlines model from a Hugging Face model and tokenizer.

        Args:
            hf_model: The Hugging Face PreTrainedModel or any model that is compatible with the
                `transformers` API.
            hf_tokenizer_or_processor: Either a HuggingFace `PreTrainedTokenizer` or any tokenizer that is compatible
                with the `transformers` API, or a HuggingFace processor inheriting from `ProcessorMixin`. If a
                tokenizer is provided, a regular model will be used, while if you provide a processor, it will be a
                multimodal model.
            provider: The provider to use for OutlinesModel. Can be either the string 'outlines' or an
                instance of `Provider[OutlinesBaseModel]`. If not provided, the other parameters will be used.
            profile: The model profile to use. Defaults to a profile picked by the provider.
            settings: Default model settings for this model instance.
        """
        outlines_model: OutlinesBaseModel = from_transformers(hf_model, hf_tokenizer_or_processor)
        return cls(outlines_model, provider=provider, profile=profile, settings=settings)

    @classmethod
    deffrom_llamacpp(  # pragma: lax no cover
        cls,
        llama_model: llama_cpp.Llama,
        *,
        provider: Literal['outlines'] | Provider[OutlinesBaseModel] = 'outlines',
        profile: ModelProfileSpec | None = None,
        settings: ModelSettings | None = None,
    ):
"""Create an Outlines model from a LlamaCpp model.

        Args:
            llama_model: The llama_cpp.Llama model to use.
            provider: The provider to use for OutlinesModel. Can be either the string 'outlines' or an
                instance of `Provider[OutlinesBaseModel]`. If not provided, the other parameters will be used.
            profile: The model profile to use. Defaults to a profile picked by the provider.
            settings: Default model settings for this model instance.
        """
        outlines_model: OutlinesBaseModel = from_llamacpp(llama_model)
        return cls(outlines_model, provider=provider, profile=profile, settings=settings)

    @classmethod
    deffrom_mlxlm(  # pragma: no cover
        cls,
        mlx_model: nn.Module,  # pyright: ignore[reportUnknownParameterType, reportUnknownMemberType]
        mlx_tokenizer: transformers.tokenization_utils.PreTrainedTokenizer,
        *,
        provider: Literal['outlines'] | Provider[OutlinesBaseModel] = 'outlines',
        profile: ModelProfileSpec | None = None,
        settings: ModelSettings | None = None,
    ):
"""Create an Outlines model from a MLXLM model.

        Args:
            mlx_model: The nn.Module model to use.
            mlx_tokenizer: The PreTrainedTokenizer to use.
            provider: The provider to use for OutlinesModel. Can be either the string 'outlines' or an
                instance of `Provider[OutlinesBaseModel]`. If not provided, the other parameters will be used.
            profile: The model profile to use. Defaults to a profile picked by the provider.
            settings: Default model settings for this model instance.
        """
        outlines_model: OutlinesBaseModel = from_mlxlm(mlx_model, mlx_tokenizer)  # pyright: ignore[reportUnknownArgumentType]
        return cls(outlines_model, provider=provider, profile=profile, settings=settings)

    @classmethod
    deffrom_sglang(
        cls,
        base_url: str,
        api_key: str | None = None,
        model_name: str | None = None,
        *,
        provider: Literal['outlines'] | Provider[OutlinesBaseModel] = 'outlines',
        profile: ModelProfileSpec | None = None,
        settings: ModelSettings | None = None,
    ):
"""Create an Outlines model to send requests to an SGLang server.

        Args:
            base_url: The url of the SGLang server.
            api_key: The API key to use for authenticating requests to the SGLang server.
            model_name: The name of the model to use.
            provider: The provider to use for OutlinesModel. Can be either the string 'outlines' or an
                instance of `Provider[OutlinesBaseModel]`. If not provided, the other parameters will be used.
            profile: The model profile to use. Defaults to a profile picked by the provider.
            settings: Default model settings for this model instance.
        """
        try:
            fromopenaiimport AsyncOpenAI
        except ImportError as _import_error:
            raise ImportError(
                'Please install `openai` to use the Outlines SGLang model, '
                'you can use the `openai` optional group — `pip install "pydantic-ai-slim[openai]"`'
            ) from_import_error

        openai_client = AsyncOpenAI(base_url=base_url, api_key=api_key)
        outlines_model: OutlinesBaseModel | OutlinesAsyncBaseModel = from_sglang(openai_client, model_name)
        return cls(outlines_model, provider=provider, profile=profile, settings=settings)

    @classmethod
    deffrom_vllm_offline(  # pragma: no cover
        cls,
        vllm_model: Any,
        *,
        provider: Literal['outlines'] | Provider[OutlinesBaseModel] = 'outlines',
        profile: ModelProfileSpec | None = None,
        settings: ModelSettings | None = None,
    ):
"""Create an Outlines model from a vLLM offline inference model.

        Args:
            vllm_model: The vllm.LLM local model to use.
            provider: The provider to use for OutlinesModel. Can be either the string 'outlines' or an
                instance of `Provider[OutlinesBaseModel]`. If not provided, the other parameters will be used.
            profile: The model profile to use. Defaults to a profile picked by the provider.
            settings: Default model settings for this model instance.
        """
        outlines_model: OutlinesBaseModel | OutlinesAsyncBaseModel = from_vllm_offline(vllm_model)
        return cls(outlines_model, provider=provider, profile=profile, settings=settings)

    @property
    defmodel_name(self) -> str:
        return self._model_name

    @property
    defsystem(self) -> str:
        return 'outlines'

    async defrequest(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> ModelResponse:
        model_settings, model_request_parameters = self.prepare_request(
            model_settings,
            model_request_parameters,
        )
"""Make a request to the model."""
        prompt, output_type, inference_kwargs = await self._build_generation_arguments(
            messages, model_settings, model_request_parameters
        )
        # Async is available for SgLang
        response: str
        if isinstance(self.model, OutlinesAsyncBaseModel):
            response = await self.model(prompt, output_type, None, **inference_kwargs)
        else:
            response = self.model(prompt, output_type, None, **inference_kwargs)
        return self._process_response(response)

    @asynccontextmanager
    async defrequest_stream(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
        run_context: RunContext[Any] | None = None,
    ) -> AsyncIterator[StreamedResponse]:
        model_settings, model_request_parameters = self.prepare_request(
            model_settings,
            model_request_parameters,
        )

        prompt, output_type, inference_kwargs = await self._build_generation_arguments(
            messages, model_settings, model_request_parameters
        )
        # Async is available for SgLang
        if isinstance(self.model, OutlinesAsyncBaseModel):
            response = self.model.stream(prompt, output_type, None, **inference_kwargs)
            yield await self._process_streamed_response(response, model_request_parameters)
        else:  # pragma: lax no cover
            response = self.model.stream(prompt, output_type, None, **inference_kwargs)

            async defasync_response():
                for chunk in response:
                    yield chunk

            yield await self._process_streamed_response(async_response(), model_request_parameters)

    async def_build_generation_arguments(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> tuple[Chat, JsonSchema | None, dict[str, Any]]:
"""Build the generation arguments for the model."""
        # the builtin_tool check now happens in `Model.prepare_request()`
        if model_request_parameters.function_tools or model_request_parameters.output_tools:
            raise UserError('Outlines does not support function tools yet.')

        if model_request_parameters.output_object:
            output_type = JsonSchema(model_request_parameters.output_object.json_schema)
        else:
            output_type = None

        prompt = await self._format_prompt(messages, model_request_parameters)
        inference_kwargs = self.format_inference_kwargs(model_settings)

        return prompt, output_type, inference_kwargs

    defformat_inference_kwargs(self, model_settings: ModelSettings | None) -> dict[str, Any]:
"""Format the model settings for the inference kwargs."""
        settings_dict: dict[str, Any] = dict(model_settings) if model_settings else {}

        if isinstance(self.model, Transformers):
            settings_dict = self._format_transformers_inference_kwargs(settings_dict)
        elif isinstance(self.model, LlamaCpp):  # pragma: lax no cover
            settings_dict = self._format_llama_cpp_inference_kwargs(settings_dict)
        elif isinstance(self.model, MLXLM):  # pragma: no cover
            settings_dict = self._format_mlxlm_inference_kwargs(settings_dict)
        elif isinstance(self.model, SGLang | AsyncSGLang):
            settings_dict = self._format_sglang_inference_kwargs(settings_dict)
        elif isinstance(self.model, VLLMOffline):  # pragma: no cover
            settings_dict = self._format_vllm_offline_inference_kwargs(settings_dict)

        extra_body = settings_dict.pop('extra_body', {})
        settings_dict.update(extra_body)

        return settings_dict

    def_format_transformers_inference_kwargs(self, model_settings: dict[str, Any]) -> dict[str, Any]:
"""Select the model settings supported by the Transformers model."""
        supported_args = [
            'max_tokens',
            'temperature',
            'top_p',
            'logit_bias',
            'extra_body',
        ]
        filtered_settings = {k: model_settings[k] for k in supported_args if k in model_settings}

        return filtered_settings

    def_format_llama_cpp_inference_kwargs(  # pragma: lax no cover
        self, model_settings: dict[str, Any]
    ) -> dict[str, Any]:
"""Select the model settings supported by the LlamaCpp model."""
        supported_args = [
            'max_tokens',
            'temperature',
            'top_p',
            'seed',
            'presence_penalty',
            'frequency_penalty',
            'logit_bias',
            'extra_body',
        ]
        filtered_settings = {k: model_settings[k] for k in supported_args if k in model_settings}

        return filtered_settings

    def_format_mlxlm_inference_kwargs(  # pragma: no cover
        self, model_settings: dict[str, Any]
    ) -> dict[str, Any]:
"""Select the model settings supported by the MLXLM model."""
        supported_args = [
            'extra_body',
        ]
        filtered_settings = {k: model_settings[k] for k in supported_args if k in model_settings}

        return filtered_settings

    def_format_sglang_inference_kwargs(self, model_settings: dict[str, Any]) -> dict[str, Any]:
"""Select the model settings supported by the SGLang model."""
        supported_args = [
            'max_tokens',
            'temperature',
            'top_p',
            'presence_penalty',
            'frequency_penalty',
            'extra_body',
        ]
        filtered_settings = {k: model_settings[k] for k in supported_args if k in model_settings}

        return filtered_settings

    def_format_vllm_offline_inference_kwargs(  # pragma: no cover
        self, model_settings: dict[str, Any]
    ) -> dict[str, Any]:
"""Select the model settings supported by the vLLMOffline model."""
        fromvllm.sampling_paramsimport (  # pyright: ignore[reportMissingImports]
            SamplingParams,  # pyright: ignore[reportUnknownVariableType]
        )

        supported_args = [
            'max_tokens',
            'temperature',
            'top_p',
            'seed',
            'presence_penalty',
            'frequency_penalty',
            'logit_bias',
            'extra_body',
        ]
        # The arguments that are part of the fields of `ModelSettings` must be put in a `SamplingParams` object and
        # provided through the `sampling_params` argument to vLLM
        sampling_params = model_settings.get('extra_body', {}).pop('sampling_params', SamplingParams())

        for key in supported_args:
            setattr(sampling_params, key, model_settings.get(key, None))

        filtered_settings = {
            'sampling_params': sampling_params,
            **model_settings.get('extra_body', {}),
        }

        return filtered_settings

    async def_format_prompt(  # noqa: C901
        self, messages: list[ModelMessage], model_request_parameters: ModelRequestParameters
    ) -> Chat:
"""Turn the model messages into an Outlines Chat instance."""
        chat = Chat()

        if instructions := self._get_instructions(messages, model_request_parameters):
            chat.add_system_message(instructions)

        for message in messages:
            if isinstance(message, ModelRequest):
                for part in message.parts:
                    if isinstance(part, SystemPromptPart):
                        chat.add_system_message(part.content)
                    elif isinstance(part, UserPromptPart):
                        if isinstance(part.content, str):
                            chat.add_user_message(part.content)
                        elif isinstance(part.content, Sequence):
                            outlines_input: Sequence[str | Image] = []
                            for item in part.content:
                                if isinstance(item, str):
                                    outlines_input.append(item)
                                elif isinstance(item, ImageUrl):
                                    image_content: DownloadedItem[bytes] = await download_item(
                                        item, data_format='bytes', type_format='mime'
                                    )
                                    image = self._create_PIL_image(image_content['data'], image_content['data_type'])
                                    outlines_input.append(Image(image))
                                elif isinstance(item, BinaryContent) and item.is_image:
                                    image = self._create_PIL_image(item.data, item.media_type)
                                    outlines_input.append(Image(image))
                                else:
                                    raise UserError(
                                        'Each element of the content sequence must be a string, an `ImageUrl`'
                                        + ' or a `BinaryImage`.'
                                    )
                            chat.add_user_message(outlines_input)
                        else:
                            assert_never(part.content)
                    elif isinstance(part, RetryPromptPart):
                        chat.add_user_message(part.model_response())
                    elif isinstance(part, ToolReturnPart):
                        raise UserError('Tool calls are not supported for Outlines models yet.')
                    else:
                        assert_never(part)
            elif isinstance(message, ModelResponse):
                text_parts: list[str] = []
                image_parts: list[Image] = []
                for part in message.parts:
                    if isinstance(part, TextPart):
                        text_parts.append(part.content)
                    elif isinstance(part, ThinkingPart):
                        # NOTE: We don't send ThinkingPart to the providers yet.
                        pass
                    elif isinstance(part, ToolCallPart | BuiltinToolCallPart | BuiltinToolReturnPart):
                        raise UserError('Tool calls are not supported for Outlines models yet.')
                    elif isinstance(part, FilePart):
                        if isinstance(part.content, BinaryContent) and part.content.is_image:
                            image = self._create_PIL_image(part.content.data, part.content.media_type)
                            image_parts.append(Image(image))
                        else:
                            raise UserError(
                                'File parts other than `BinaryImage` are not supported for Outlines models yet.'
                            )
                    else:
                        assert_never(part)
                if len(text_parts) == 1 and len(image_parts) == 0:
                    chat.add_assistant_message(text_parts[0])
                else:
                    chat.add_assistant_message([*text_parts, *image_parts])
            else:
                assert_never(message)
        return chat

    def_create_PIL_image(self, data: bytes, data_type: str) -> PILImage.Image:
"""Create a PIL Image from the data and data type."""
        image = PILImage.open(io.BytesIO(data))
        image.format = data_type.split('/')[-1]
        return image

    def_process_response(self, response: str) -> ModelResponse:
"""Turn the Outlines text response into a Pydantic AI model response instance."""
        return ModelResponse(
            parts=cast(
                list[ModelResponsePart], split_content_into_text_and_thinking(response, self.profile.thinking_tags)
            ),
        )

    async def_process_streamed_response(
        self, response: AsyncIterable[str], model_request_parameters: ModelRequestParameters
    ) -> StreamedResponse:
"""Turn the Outlines text response into a Pydantic AI streamed response instance."""
        peekable_response = _utils.PeekableAsyncStream(response)
        first_chunk = await peekable_response.peek()
        if isinstance(first_chunk, _utils.Unset):  # pragma: no cover
            raise UnexpectedModelBehavior('Streamed response ended without content or tool calls')

        return OutlinesStreamedResponse(
            model_request_parameters=model_request_parameters,
            _model_name=self._model_name,
            _model_profile=self.profile,
            _response=peekable_response,
            _provider_name='outlines',
        )
```