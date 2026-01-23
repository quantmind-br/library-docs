---
title: pydantic_ai.models.google - Pydantic AI
url: https://ai.pydantic.dev/api/models/google/
source: sitemap
fetched_at: 2026-01-22T22:24:29.208868723-03:00
rendered_js: false
word_count: 50
summary: This document defines the GoogleModel class, which provides a Python interface for interacting with Google's Gemini generative AI models via the Generative Language and Vertex AI APIs.
tags:
    - google-gemini
    - vertex-ai
    - python-sdk
    - llm-integration
    - api-client
    - token-counting
category: api
---

```
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
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
743
744
745
746
747
748
749
750
751
752
753
754
755
756
757
758
759
760
761
762
763
764
765
766
```

```
@dataclass(init=False)
classGoogleModel(Model):
"""A model that uses Gemini via `generativelanguage.googleapis.com` API.

    This is implemented from scratch rather than using a dedicated SDK, good API documentation is
    available [here](https://ai.google.dev/api).

    Apart from `__init__`, all methods are private or match those of the base class.
    """

    client: Client = field(repr=False)

    _model_name: GoogleModelName = field(repr=False)
    _provider: Provider[Client] = field(repr=False)

    def__init__(
        self,
        model_name: GoogleModelName,
        *,
        provider: Literal['google-gla', 'google-vertex', 'gateway'] | Provider[Client] = 'google-gla',
        profile: ModelProfileSpec | None = None,
        settings: ModelSettings | None = None,
    ):
"""Initialize a Gemini model.

        Args:
            model_name: The name of the model to use.
            provider: The provider to use for authentication and API access. Can be either the string
                'google-gla' or 'google-vertex' or an instance of `Provider[google.genai.AsyncClient]`.
                Defaults to 'google-gla'.
            profile: The model profile to use. Defaults to a profile picked by the provider based on the model name.
            settings: The model settings to use. Defaults to None.
        """
        self._model_name = model_name

        if isinstance(provider, str):
            provider = infer_provider('gateway/google-vertex' if provider == 'gateway' else provider)
        self._provider = provider
        self.client = provider.client

        super().__init__(settings=settings, profile=profile or provider.model_profile)

    @property
    defbase_url(self) -> str:
        return self._provider.base_url

    @property
    defmodel_name(self) -> GoogleModelName:
"""The model name."""
        return self._model_name

    @property
    defsystem(self) -> str:
"""The model provider."""
        return self._provider.name

    @classmethod
    defsupported_builtin_tools(cls) -> frozenset[type[AbstractBuiltinTool]]:
"""Return the set of builtin tool types this model can handle."""
        return frozenset({WebSearchTool, CodeExecutionTool, FileSearchTool, WebFetchTool, ImageGenerationTool})

    defprepare_request(
        self, model_settings: ModelSettings | None, model_request_parameters: ModelRequestParameters
    ) -> tuple[ModelSettings | None, ModelRequestParameters]:
        supports_native_output_with_builtin_tools = GoogleModelProfile.from_profile(
            self.profile
        ).google_supports_native_output_with_builtin_tools
        if model_request_parameters.builtin_tools and model_request_parameters.output_tools:
            if model_request_parameters.output_mode == 'auto':
                output_mode = 'native' if supports_native_output_with_builtin_tools else 'prompted'
                model_request_parameters = replace(model_request_parameters, output_mode=output_mode)
            else:
                output_mode = 'NativeOutput' if supports_native_output_with_builtin_tools else 'PromptedOutput'
                raise UserError(
                    f'Google does not support output tools and built-in tools at the same time. Use `output_type={output_mode}(...)` instead.'
                )
        return super().prepare_request(model_settings, model_request_parameters)

    async defrequest(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> ModelResponse:
        check_allow_model_requests()
        model_settings, model_request_parameters = self.prepare_request(
            model_settings,
            model_request_parameters,
        )
        model_settings = cast(GoogleModelSettings, model_settings or {})
        response = await self._generate_content(messages, False, model_settings, model_request_parameters)
        return self._process_response(response)

    async defcount_tokens(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> usage.RequestUsage:
        check_allow_model_requests()
        model_settings, model_request_parameters = self.prepare_request(
            model_settings,
            model_request_parameters,
        )
        model_settings = cast(GoogleModelSettings, model_settings or {})
        contents, generation_config = await self._build_content_and_config(
            messages, model_settings, model_request_parameters
        )

        # Annoyingly, the type of `GenerateContentConfigDict.get` is "partially `Unknown`" because `response_schema` includes `typing._UnionGenericAlias`,
        # so without this we'd need `pyright: ignore[reportUnknownMemberType]` on every line and wouldn't get type checking anyway.
        generation_config = cast(dict[str, Any], generation_config)

        config = CountTokensConfigDict(
            http_options=generation_config.get('http_options'),
        )
        if self._provider.name != 'google-gla':
            # The fields are not supported by the Gemini API per https://github.com/googleapis/python-genai/blob/7e4ec284dc6e521949626f3ed54028163ef9121d/google/genai/models.py#L1195-L1214
            config.update(  # pragma: lax no cover
                system_instruction=generation_config.get('system_instruction'),
                tools=cast(list[ToolDict], generation_config.get('tools')),
                # Annoyingly, GenerationConfigDict has fewer fields than GenerateContentConfigDict, and no extra fields are allowed.
                generation_config=GenerationConfigDict(
                    temperature=generation_config.get('temperature'),
                    top_p=generation_config.get('top_p'),
                    max_output_tokens=generation_config.get('max_output_tokens'),
                    stop_sequences=generation_config.get('stop_sequences'),
                    presence_penalty=generation_config.get('presence_penalty'),
                    frequency_penalty=generation_config.get('frequency_penalty'),
                    seed=generation_config.get('seed'),
                    thinking_config=generation_config.get('thinking_config'),
                    media_resolution=generation_config.get('media_resolution'),
                    response_mime_type=generation_config.get('response_mime_type'),
                    response_json_schema=generation_config.get('response_json_schema'),
                ),
            )

        response = await self.client.aio.models.count_tokens(
            model=self._model_name,
            contents=contents,
            config=config,
        )
        if response.total_tokens is None:
            raise UnexpectedModelBehavior(  # pragma: no cover
                'Total tokens missing from Gemini response', str(response)
            )
        return usage.RequestUsage(
            input_tokens=response.total_tokens,
        )

    @asynccontextmanager
    async defrequest_stream(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
        run_context: RunContext[Any] | None = None,
    ) -> AsyncIterator[StreamedResponse]:
        check_allow_model_requests()
        model_settings, model_request_parameters = self.prepare_request(
            model_settings,
            model_request_parameters,
        )
        model_settings = cast(GoogleModelSettings, model_settings or {})
        response = await self._generate_content(messages, True, model_settings, model_request_parameters)
        yield await self._process_streamed_response(response, model_request_parameters)  # type: ignore

    def_build_image_config(self, tool: ImageGenerationTool) -> ImageConfigDict:
"""Build ImageConfigDict from ImageGenerationTool with validation."""
        image_config = ImageConfigDict()

        if tool.aspect_ratio is not None:
            image_config['aspect_ratio'] = tool.aspect_ratio

        if tool.size is not None:
            if tool.size not in _GOOGLE_IMAGE_SIZES:
                raise UserError(
                    f'Google image generation only supports `size` values: {_GOOGLE_IMAGE_SIZES}. '
                    f'Got: {tool.size!r}. Omit `size` to use the default (1K).'
                )
            image_config['image_size'] = tool.size

        if self.system == 'google-vertex':
            if tool.output_format is not None:
                if tool.output_format not in _GOOGLE_IMAGE_OUTPUT_FORMATS:
                    raise UserError(
                        f'Google image generation only supports `output_format` values: {_GOOGLE_IMAGE_OUTPUT_FORMATS}. '
                        f'Got: {tool.output_format!r}.'
                    )
                image_config['output_mime_type'] = f'image/{tool.output_format}'

            output_compression = tool.output_compression
            if output_compression is not None:
                if not (0 <= output_compression <= 100):
                    raise UserError(
                        f'Google image generation `output_compression` must be between 0 and 100. '
                        f'Got: {output_compression}.'
                    )
                if tool.output_format not in (None, 'jpeg'):
                    raise UserError(
                        f'Google image generation `output_compression` is only supported for JPEG format. '
                        f'Got format: {tool.output_format!r}. Either set `output_format="jpeg"` or remove `output_compression`.'
                    )
                image_config['output_compression_quality'] = output_compression
                if tool.output_format is None:
                    image_config['output_mime_type'] = 'image/jpeg'

        return image_config

    def_get_tools(
        self, model_request_parameters: ModelRequestParameters
    ) -> tuple[list[ToolDict] | None, ImageConfigDict | None]:
        tools: list[ToolDict] = [
            ToolDict(function_declarations=[_function_declaration_from_tool(t)])
            for t in model_request_parameters.tool_defs.values()
        ]

        image_config: ImageConfigDict | None = None

        if model_request_parameters.builtin_tools:
            if model_request_parameters.function_tools:
                raise UserError('Google does not support function tools and built-in tools at the same time.')

            for tool in model_request_parameters.builtin_tools:
                if isinstance(tool, WebSearchTool):
                    tools.append(ToolDict(google_search=GoogleSearchDict()))
                elif isinstance(tool, WebFetchTool):
                    tools.append(ToolDict(url_context=UrlContextDict()))
                elif isinstance(tool, CodeExecutionTool):
                    tools.append(ToolDict(code_execution=ToolCodeExecutionDict()))
                elif isinstance(tool, FileSearchTool):
                    file_search_config = FileSearchDict(file_search_store_names=list(tool.file_store_ids))
                    tools.append(ToolDict(file_search=file_search_config))
                elif isinstance(tool, ImageGenerationTool):  # pragma: no branch
                    if not self.profile.supports_image_output:
                        raise UserError(
                            "`ImageGenerationTool` is not supported by this model. Use a model with 'image' in the name instead."
                        )
                    image_config = self._build_image_config(tool)
                else:  # pragma: no cover
                    raise UserError(
                        f'`{tool.__class__.__name__}` is not supported by `GoogleModel`. If it should be, please file an issue.'
                    )
        return tools or None, image_config

    def_get_tool_config(
        self, model_request_parameters: ModelRequestParameters, tools: list[ToolDict] | None
    ) -> ToolConfigDict | None:
        if not model_request_parameters.allow_text_output and tools:
            names: list[str] = []
            for tool in tools:
                for function_declaration in tool.get('function_declarations') or []:
                    if name := function_declaration.get('name'):  # pragma: no branch
                        names.append(name)
            return _tool_config(names)
        else:
            return None

    @overload
    async def_generate_content(
        self,
        messages: list[ModelMessage],
        stream: Literal[False],
        model_settings: GoogleModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> GenerateContentResponse: ...

    @overload
    async def_generate_content(
        self,
        messages: list[ModelMessage],
        stream: Literal[True],
        model_settings: GoogleModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> Awaitable[AsyncIterator[GenerateContentResponse]]: ...

    async def_generate_content(
        self,
        messages: list[ModelMessage],
        stream: bool,
        model_settings: GoogleModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> GenerateContentResponse | Awaitable[AsyncIterator[GenerateContentResponse]]:
        contents, config = await self._build_content_and_config(messages, model_settings, model_request_parameters)
        func = self.client.aio.models.generate_content_stream if stream else self.client.aio.models.generate_content
        try:
            return await func(model=self._model_name, contents=contents, config=config)  # type: ignore
        except errors.APIError as e:
            if (status_code := e.code) >= 400:
                raise ModelHTTPError(
                    status_code=status_code,
                    model_name=self._model_name,
                    body=cast(Any, e.details),  # pyright: ignore[reportUnknownMemberType]
                ) frome
            raise ModelAPIError(model_name=self._model_name, message=str(e)) frome

    async def_build_content_and_config(
        self,
        messages: list[ModelMessage],
        model_settings: GoogleModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> tuple[list[ContentUnionDict], GenerateContentConfigDict]:
        tools, image_config = self._get_tools(model_request_parameters)
        if model_request_parameters.function_tools and not self.profile.supports_tools:
            raise UserError('Tools are not supported by this model.')

        response_mime_type = None
        response_schema = None
        if model_request_parameters.output_mode == 'native':
            if model_request_parameters.function_tools:
                raise UserError(
                    'Google does not support `NativeOutput` and function tools at the same time. Use `output_type=ToolOutput(...)` instead.'
                )
            response_mime_type = 'application/json'
            output_object = model_request_parameters.output_object
            assert output_object is not None
            response_schema = self._map_response_schema(output_object)
        elif model_request_parameters.output_mode == 'prompted' and not tools:
            if not self.profile.supports_json_object_output:
                raise UserError('JSON output is not supported by this model.')
            response_mime_type = 'application/json'

        tool_config = self._get_tool_config(model_request_parameters, tools)
        system_instruction, contents = await self._map_messages(messages, model_request_parameters)

        modalities = [Modality.TEXT.value]
        if self.profile.supports_image_output:
            modalities.append(Modality.IMAGE.value)

        http_options: HttpOptionsDict = {
            'headers': {'Content-Type': 'application/json', 'User-Agent': get_user_agent()}
        }
        if timeout := model_settings.get('timeout'):
            if isinstance(timeout, int | float):
                http_options['timeout'] = int(1000 * timeout)
            else:
                raise UserError('Google does not support setting ModelSettings.timeout to a httpx.Timeout')

        config = GenerateContentConfigDict(
            http_options=http_options,
            system_instruction=system_instruction,
            temperature=model_settings.get('temperature'),
            top_p=model_settings.get('top_p'),
            max_output_tokens=model_settings.get('max_tokens'),
            stop_sequences=model_settings.get('stop_sequences'),
            presence_penalty=model_settings.get('presence_penalty'),
            frequency_penalty=model_settings.get('frequency_penalty'),
            seed=model_settings.get('seed'),
            safety_settings=model_settings.get('google_safety_settings'),
            thinking_config=model_settings.get('google_thinking_config'),
            labels=model_settings.get('google_labels'),
            media_resolution=model_settings.get('google_video_resolution'),
            cached_content=model_settings.get('google_cached_content'),
            tools=cast(ToolListUnionDict, tools),
            tool_config=tool_config,
            response_mime_type=response_mime_type,
            response_json_schema=response_schema,
            response_modalities=modalities,
            image_config=image_config,
        )

        return contents, config

    def_process_response(self, response: GenerateContentResponse) -> ModelResponse:
        if not response.candidates:
            raise UnexpectedModelBehavior('Expected at least one candidate in Gemini response')  # pragma: no cover

        candidate = response.candidates[0]

        vendor_id = response.response_id
        finish_reason: FinishReason | None = None
        vendor_details: dict[str, Any] = {}

        raw_finish_reason = candidate.finish_reason
        if raw_finish_reason:  # pragma: no branch
            vendor_details = {'finish_reason': raw_finish_reason.value}
            # Add safety ratings to provider details
            if candidate.safety_ratings:
                vendor_details['safety_ratings'] = [r.model_dump(by_alias=True) for r in candidate.safety_ratings]
            finish_reason = _FINISH_REASON_MAP.get(raw_finish_reason)

        if response.create_time is not None:  # pragma: no branch
            vendor_details['timestamp'] = response.create_time

        if candidate.content is None or candidate.content.parts is None:
            parts = []
        else:
            parts = candidate.content.parts or []

        usage = _metadata_as_usage(response, provider=self._provider.name, provider_url=self._provider.base_url)
        return _process_response_from_parts(
            parts,
            candidate.grounding_metadata,
            response.model_version or self._model_name,
            self._provider.name,
            self._provider.base_url,
            usage,
            vendor_id=vendor_id,
            vendor_details=vendor_details or None,
            finish_reason=finish_reason,
            url_context_metadata=candidate.url_context_metadata,
        )

    async def_process_streamed_response(
        self, response: AsyncIterator[GenerateContentResponse], model_request_parameters: ModelRequestParameters
    ) -> StreamedResponse:
"""Process a streamed response, and prepare a streaming response to return."""
        peekable_response = _utils.PeekableAsyncStream(response)
        first_chunk = await peekable_response.peek()
        if isinstance(first_chunk, _utils.Unset):
            raise UnexpectedModelBehavior('Streamed response ended without content or tool calls')  # pragma: no cover

        return GeminiStreamedResponse(
            model_request_parameters=model_request_parameters,
            _model_name=first_chunk.model_version or self._model_name,
            _response=peekable_response,
            _provider_name=self._provider.name,
            _provider_url=self._provider.base_url,
            _provider_timestamp=first_chunk.create_time,
        )

    async def_map_messages(  # noqa: C901
        self, messages: list[ModelMessage], model_request_parameters: ModelRequestParameters
    ) -> tuple[ContentDict | None, list[ContentUnionDict]]:
        contents: list[ContentUnionDict] = []
        system_parts: list[PartDict] = []

        for m in messages:
            if isinstance(m, ModelRequest):
                message_parts: list[PartDict] = []

                for part in m.parts:
                    if isinstance(part, SystemPromptPart):
                        system_parts.append({'text': part.content})
                    elif isinstance(part, UserPromptPart):
                        message_parts.extend(await self._map_user_prompt(part))
                    elif isinstance(part, ToolReturnPart):
                        message_parts.append(
                            {
                                'function_response': {
                                    'name': part.tool_name,
                                    'response': part.model_response_object(),
                                    'id': part.tool_call_id,
                                }
                            }
                        )
                    elif isinstance(part, RetryPromptPart):
                        if part.tool_name is None:
                            message_parts.append({'text': part.model_response()})
                        else:
                            message_parts.append(
                                {
                                    'function_response': {
                                        'name': part.tool_name,
                                        'response': {'error': part.model_response()},
                                        'id': part.tool_call_id,
                                    }
                                }
                            )
                    else:
                        assert_never(part)

                # Work around a Gemini bug where content objects containing functionResponse parts are treated as
                # role=model even when role=user is explicitly specified.
                #
                # We build `message_parts` first, then split into multiple content objects whenever we transition
                # between function_response and non-function_response parts.
                #
                # TODO: Remove workaround when https://github.com/pydantic/pydantic-ai/issues/3763 is resolved
                if message_parts:
                    content_parts: list[PartDict] = []

                    for part in message_parts:
                        if (
                            content_parts
                            and 'function_response' in content_parts[-1]
                            and 'function_response' not in part
                        ):
                            contents.append({'role': 'user', 'parts': content_parts})
                            content_parts = []

                        content_parts.append(part)

                    contents.append({'role': 'user', 'parts': content_parts})
            elif isinstance(m, ModelResponse):
                maybe_content = _content_model_response(m, self.system)
                if maybe_content:
                    contents.append(maybe_content)
            else:
                assert_never(m)

        # Google GenAI requires at least one part in the message.
        if not contents:
            contents = [{'role': 'user', 'parts': [{'text': ''}]}]

        if instructions := self._get_instructions(messages, model_request_parameters):
            system_parts.append({'text': instructions})
        system_instruction = ContentDict(role='user', parts=system_parts) if system_parts else None

        return system_instruction, contents

    async def_map_user_prompt(self, part: UserPromptPart) -> list[PartDict]:
        if isinstance(part.content, str):
            return [{'text': part.content}]
        else:
            content: list[PartDict] = []
            for item in part.content:
                if isinstance(item, str):
                    content.append({'text': item})
                elif isinstance(item, BinaryContent):
                    inline_data_dict: BlobDict = {'data': item.data, 'mime_type': item.media_type}
                    part_dict: PartDict = {'inline_data': inline_data_dict}
                    if item.vendor_metadata:
                        part_dict['video_metadata'] = cast(VideoMetadataDict, item.vendor_metadata)
                    content.append(part_dict)
                elif isinstance(item, VideoUrl) and (
                    item.is_youtube or (item.url.startswith('gs://') and self.system == 'google-vertex')
                ):
                    # YouTube URLs work on both google-gla and google-vertex
                    # GCS URIs (gs://...) only work on google-vertex (Vertex AI can access GCS buckets)
                    # GCS on google-gla falls through to FileUrl which raises clear error on download attempt
                    # Other URLs fall through to FileUrl handling (download for google-gla)
                    # Note: force_download is not checked here, mirroring the original YouTube behavior.
                    # GCS URIs cannot be downloaded anyway ("gs://" protocol not supported for download).
                    file_data_dict: FileDataDict = {'file_uri': item.url, 'mime_type': item.media_type}
                    part_dict: PartDict = {'file_data': file_data_dict}
                    if item.vendor_metadata:
                        part_dict['video_metadata'] = cast(VideoMetadataDict, item.vendor_metadata)
                    content.append(part_dict)
                elif isinstance(item, FileUrl):
                    if item.force_download or (
                        # google-gla does not support passing file urls directly, except for youtube videos
                        # (see above) and files uploaded to the file API (which cannot be downloaded anyway)
                        self.system == 'google-gla'
                        and not item.url.startswith(r'https://generativelanguage.googleapis.com/v1beta/files')
                    ):
                        downloaded_item = await download_item(item, data_format='bytes')
                        inline_data: BlobDict = {
                            'data': downloaded_item['data'],
                            'mime_type': downloaded_item['data_type'],
                        }
                        part_dict: PartDict = {'inline_data': inline_data}
                        # VideoUrl is a subclass of FileUrl - include video_metadata if present
                        if isinstance(item, VideoUrl) and item.vendor_metadata:
                            part_dict['video_metadata'] = cast(VideoMetadataDict, item.vendor_metadata)
                        content.append(part_dict)
                    else:
                        file_data_dict: FileDataDict = {'file_uri': item.url, 'mime_type': item.media_type}
                        part_dict: PartDict = {'file_data': file_data_dict}
                        # VideoUrl is a subclass of FileUrl - include video_metadata if present
                        if isinstance(item, VideoUrl) and item.vendor_metadata:
                            part_dict['video_metadata'] = cast(VideoMetadataDict, item.vendor_metadata)
                        content.append(part_dict)  # pragma: lax no cover
                elif isinstance(item, CachePoint):
                    # Google doesn't support inline CachePoint markers. Google's caching requires
                    # pre-creating cache objects via the API, then referencing them by name using
                    # `GoogleModelSettings.google_cached_content`. See https://ai.google.dev/gemini-api/docs/caching
                    pass
                else:
                    assert_never(item)
        return content

    def_map_response_schema(self, o: OutputObjectDefinition) -> dict[str, Any]:
        response_schema = o.json_schema.copy()
        if o.name:
            response_schema['title'] = o.name
        if o.description:
            response_schema['description'] = o.description

        return response_schema
```