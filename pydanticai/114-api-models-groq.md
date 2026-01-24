---
title: pydantic_ai.models.groq - Pydantic AI
url: https://ai.pydantic.dev/api/models/groq/
source: sitemap
fetched_at: 2026-01-22T22:24:30.683960081-03:00
rendered_js: false
word_count: 60
summary: This document defines the GroqModel class, which provides an interface for interacting with the Groq API to perform text generation, streaming, and tool calls.
tags:
    - groq
    - python-sdk
    - llm-integration
    - api-client
    - streaming-responses
    - tool-calling
category: reference
---

```
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
```

```
@dataclass(init=False)
classGroqModel(Model):
"""A model that uses the Groq API.

    Internally, this uses the [Groq Python client](https://github.com/groq/groq-python) to interact with the API.

    Apart from `__init__`, all methods are private or match those of the base class.
    """

    client: AsyncGroq = field(repr=False)

    _model_name: GroqModelName = field(repr=False)
    _provider: Provider[AsyncGroq] = field(repr=False)

    def__init__(
        self,
        model_name: GroqModelName,
        *,
        provider: Literal['groq', 'gateway'] | Provider[AsyncGroq] = 'groq',
        profile: ModelProfileSpec | None = None,
        settings: ModelSettings | None = None,
    ):
"""Initialize a Groq model.

        Args:
            model_name: The name of the Groq model to use. List of model names available
                [here](https://console.groq.com/docs/models).
            provider: The provider to use for authentication and API access. Can be either the string
                'groq' or an instance of `Provider[AsyncGroq]`. If not provided, a new provider will be
                created using the other parameters.
            profile: The model profile to use. Defaults to a profile picked by the provider based on the model name.
            settings: Model-specific settings that will be used as defaults for this model.
        """
        self._model_name = model_name

        if isinstance(provider, str):
            provider = infer_provider('gateway/groq' if provider == 'gateway' else provider)
        self._provider = provider
        self.client = provider.client

        super().__init__(settings=settings, profile=profile or provider.model_profile)

    @property
    defbase_url(self) -> str:
        return str(self.client.base_url)

    @property
    defmodel_name(self) -> GroqModelName:
"""The model name."""
        return self._model_name

    @property
    defsystem(self) -> str:
"""The model provider."""
        return self._provider.name

    @classmethod
    defsupported_builtin_tools(cls) -> frozenset[type[AbstractBuiltinTool]]:
"""Return the set of builtin tool types this model can handle."""
        return frozenset({WebSearchTool})

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
        try:
            response = await self._completions_create(
                messages, False, cast(GroqModelSettings, model_settings or {}), model_request_parameters
            )
        except ModelHTTPError as e:
            if isinstance(e.body, dict):  # pragma: no branch
                # The Groq SDK tries to be helpful by raising an exception when generated tool arguments don't match the schema,
                # but we'd rather handle it ourselves so we can tell the model to retry the tool call.
                try:
                    error = _GroqToolUseFailedError.model_validate(e.body)  # pyright: ignore[reportUnknownMemberType]
                    tool_call_part = ToolCallPart(
                        tool_name=error.error.failed_generation.name,
                        args=error.error.failed_generation.arguments,
                    )
                    return ModelResponse(
                        parts=[tool_call_part],
                        model_name=e.model_name,
                        provider_name=self._provider.name,
                        provider_url=self.base_url,
                        finish_reason='error',
                    )
                except ValidationError:
                    pass
            raise
        model_response = self._process_response(response)
        return model_response

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
        response = await self._completions_create(
            messages, True, cast(GroqModelSettings, model_settings or {}), model_request_parameters
        )
        async with response:
            yield await self._process_streamed_response(response, model_request_parameters)

    @overload
    async def_completions_create(
        self,
        messages: list[ModelMessage],
        stream: Literal[True],
        model_settings: GroqModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> AsyncStream[chat.ChatCompletionChunk]:
        pass

    @overload
    async def_completions_create(
        self,
        messages: list[ModelMessage],
        stream: Literal[False],
        model_settings: GroqModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> chat.ChatCompletion:
        pass

    async def_completions_create(
        self,
        messages: list[ModelMessage],
        stream: bool,
        model_settings: GroqModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> chat.ChatCompletion | AsyncStream[chat.ChatCompletionChunk]:
        tools = self._get_tools(model_request_parameters)
        tools += self._get_builtin_tools(model_request_parameters)
        if not tools:
            tool_choice: Literal['none', 'required', 'auto'] | None = None
        elif not model_request_parameters.allow_text_output:
            tool_choice = 'required'
        else:
            tool_choice = 'auto'

        groq_messages = self._map_messages(messages, model_request_parameters)

        response_format: chat.completion_create_params.ResponseFormat | None = None
        if model_request_parameters.output_mode == 'native':
            output_object = model_request_parameters.output_object
            assert output_object is not None
            response_format = self._map_json_schema(output_object)
        elif (
            model_request_parameters.output_mode == 'prompted'
            and not tools
            and self.profile.supports_json_object_output
        ):  # pragma: no branch
            response_format = {'type': 'json_object'}

        try:
            extra_headers = model_settings.get('extra_headers', {})
            extra_headers.setdefault('User-Agent', get_user_agent())
            return await self.client.chat.completions.create(
                model=self._model_name,
                messages=groq_messages,
                n=1,
                parallel_tool_calls=model_settings.get('parallel_tool_calls', NOT_GIVEN),
                tools=tools or NOT_GIVEN,
                tool_choice=tool_choice or NOT_GIVEN,
                stop=model_settings.get('stop_sequences', NOT_GIVEN),
                stream=stream,
                response_format=response_format or NOT_GIVEN,
                max_tokens=model_settings.get('max_tokens', NOT_GIVEN),
                temperature=model_settings.get('temperature', NOT_GIVEN),
                top_p=model_settings.get('top_p', NOT_GIVEN),
                timeout=model_settings.get('timeout', NOT_GIVEN),
                seed=model_settings.get('seed', NOT_GIVEN),
                presence_penalty=model_settings.get('presence_penalty', NOT_GIVEN),
                reasoning_format=model_settings.get('groq_reasoning_format', NOT_GIVEN),
                frequency_penalty=model_settings.get('frequency_penalty', NOT_GIVEN),
                logit_bias=model_settings.get('logit_bias', NOT_GIVEN),
                extra_headers=extra_headers,
                extra_body=model_settings.get('extra_body'),
            )
        except APIStatusError as e:
            if (status_code := e.status_code) >= 400:
                raise ModelHTTPError(status_code=status_code, model_name=self.model_name, body=e.body) frome
            raise ModelAPIError(model_name=self.model_name, message=e.message) frome  # pragma: no cover
        except APIConnectionError as e:
            raise ModelAPIError(model_name=self.model_name, message=e.message) frome

    def_process_response(self, response: chat.ChatCompletion) -> ModelResponse:
"""Process a non-streamed response, and prepare a message to return."""
        choice = response.choices[0]
        items: list[ModelResponsePart] = []
        if choice.message.reasoning is not None:
            # NOTE: The `reasoning` field is only present if `groq_reasoning_format` is set to `parsed`.
            items.append(ThinkingPart(content=choice.message.reasoning))
        if choice.message.executed_tools:
            for tool in choice.message.executed_tools:
                call_part, return_part = _map_executed_tool(tool, self.system)
                if call_part and return_part:  # pragma: no branch
                    items.append(call_part)
                    items.append(return_part)
        if choice.message.content:
            # NOTE: The `<think>` tag is only present if `groq_reasoning_format` is set to `raw`.
            items.extend(split_content_into_text_and_thinking(choice.message.content, self.profile.thinking_tags))
        if choice.message.tool_calls is not None:
            for c in choice.message.tool_calls:
                items.append(ToolCallPart(tool_name=c.function.name, args=c.function.arguments, tool_call_id=c.id))

        raw_finish_reason = choice.finish_reason
        provider_details: dict[str, Any] = {'finish_reason': raw_finish_reason}
        if response.created:  # pragma: no branch
            provider_details['timestamp'] = number_to_datetime(response.created)
        finish_reason = _FINISH_REASON_MAP.get(raw_finish_reason)
        return ModelResponse(
            parts=items,
            usage=_map_usage(response),
            model_name=response.model,
            provider_response_id=response.id,
            provider_name=self._provider.name,
            provider_url=self.base_url,
            finish_reason=finish_reason,
            provider_details=provider_details,
        )

    async def_process_streamed_response(
        self, response: AsyncStream[chat.ChatCompletionChunk], model_request_parameters: ModelRequestParameters
    ) -> GroqStreamedResponse:
"""Process a streamed response, and prepare a streaming response to return."""
        peekable_response = _utils.PeekableAsyncStream(response)
        first_chunk = await peekable_response.peek()
        if isinstance(first_chunk, _utils.Unset):
            raise UnexpectedModelBehavior(  # pragma: no cover
                'Streamed response ended without content or tool calls'
            )

        return GroqStreamedResponse(
            model_request_parameters=model_request_parameters,
            _response=peekable_response,
            _model_name=first_chunk.model,
            _model_profile=self.profile,
            _provider_name=self._provider.name,
            _provider_url=self.base_url,
            _provider_timestamp=number_to_datetime(first_chunk.created),
        )

    def_get_tools(self, model_request_parameters: ModelRequestParameters) -> list[chat.ChatCompletionToolParam]:
        return [self._map_tool_definition(r) for r in model_request_parameters.tool_defs.values()]

    def_get_builtin_tools(
        self, model_request_parameters: ModelRequestParameters
    ) -> list[chat.ChatCompletionToolParam]:
        tools: list[chat.ChatCompletionToolParam] = []
        for tool in model_request_parameters.builtin_tools:
            if isinstance(tool, WebSearchTool):
                if not GroqModelProfile.from_profile(self.profile).groq_always_has_web_search_builtin_tool:
                    raise UserError('`WebSearchTool` is not supported by Groq')  # pragma: no cover
            else:  # pragma: no cover
                raise UserError(
                    f'`{tool.__class__.__name__}` is not supported by `GroqModel`. If it should be, please file an issue.'
                )
        return tools

    def_map_messages(
        self, messages: list[ModelMessage], model_request_parameters: ModelRequestParameters
    ) -> list[chat.ChatCompletionMessageParam]:
"""Just maps a `pydantic_ai.Message` to a `groq.types.ChatCompletionMessageParam`."""
        groq_messages: list[chat.ChatCompletionMessageParam] = []
        for message in messages:
            if isinstance(message, ModelRequest):
                groq_messages.extend(self._map_user_message(message))
            elif isinstance(message, ModelResponse):
                texts: list[str] = []
                tool_calls: list[chat.ChatCompletionMessageToolCallParam] = []
                for item in message.parts:
                    if isinstance(item, TextPart):
                        texts.append(item.content)
                    elif isinstance(item, ToolCallPart):
                        tool_calls.append(self._map_tool_call(item))
                    elif isinstance(item, ThinkingPart):
                        start_tag, end_tag = self.profile.thinking_tags
                        texts.append('\n'.join([start_tag, item.content, end_tag]))
                    elif isinstance(item, BuiltinToolCallPart | BuiltinToolReturnPart):  # pragma: no cover
                        # These are not currently sent back
                        pass
                    elif isinstance(item, FilePart):  # pragma: no cover
                        # Files generated by models are not sent back to models that don't themselves generate files.
                        pass
                    else:
                        assert_never(item)
                message_param = chat.ChatCompletionAssistantMessageParam(role='assistant')
                if texts:
                    # Note: model responses from this model should only have one text item, so the following
                    # shouldn't merge multiple texts into one unless you switch models between runs:
                    message_param['content'] = '\n\n'.join(texts)
                if tool_calls:
                    message_param['tool_calls'] = tool_calls
                groq_messages.append(message_param)
            else:
                assert_never(message)
        if instructions := self._get_instructions(messages, model_request_parameters):
            system_prompt_count = sum(1 for m in groq_messages if m.get('role') == 'system')
            groq_messages.insert(
                system_prompt_count, chat.ChatCompletionSystemMessageParam(role='system', content=instructions)
            )
        return groq_messages

    @staticmethod
    def_map_tool_call(t: ToolCallPart) -> chat.ChatCompletionMessageToolCallParam:
        return chat.ChatCompletionMessageToolCallParam(
            id=_guard_tool_call_id(t=t),
            type='function',
            function={'name': t.tool_name, 'arguments': t.args_as_json_str()},
        )

    @staticmethod
    def_map_tool_definition(f: ToolDefinition) -> chat.ChatCompletionToolParam:
        return {
            'type': 'function',
            'function': {
                'name': f.name,
                'description': f.description or '',
                'parameters': f.parameters_json_schema,
            },
        }

    def_map_json_schema(self, o: OutputObjectDefinition) -> chat.completion_create_params.ResponseFormat:
        response_format_param: chat.completion_create_params.ResponseFormatResponseFormatJsonSchema = {
            'type': 'json_schema',
            'json_schema': {
                'name': o.name or DEFAULT_OUTPUT_TOOL_NAME,
                'schema': o.json_schema,
                'strict': o.strict,
            },
        }
        if o.description:  # pragma: no branch
            response_format_param['json_schema']['description'] = o.description
        return response_format_param

    @classmethod
    def_map_user_message(cls, message: ModelRequest) -> Iterable[chat.ChatCompletionMessageParam]:
        for part in message.parts:
            if isinstance(part, SystemPromptPart):
                yield chat.ChatCompletionSystemMessageParam(role='system', content=part.content)
            elif isinstance(part, UserPromptPart):
                yield cls._map_user_prompt(part)
            elif isinstance(part, ToolReturnPart):
                yield chat.ChatCompletionToolMessageParam(
                    role='tool',
                    tool_call_id=_guard_tool_call_id(t=part),
                    content=part.model_response_str(),
                )
            elif isinstance(part, RetryPromptPart):  # pragma: no branch
                if part.tool_name is None:
                    yield chat.ChatCompletionUserMessageParam(  # pragma: no cover
                        role='user', content=part.model_response()
                    )
                else:
                    yield chat.ChatCompletionToolMessageParam(
                        role='tool',
                        tool_call_id=_guard_tool_call_id(t=part),
                        content=part.model_response(),
                    )

    @staticmethod
    def_map_user_prompt(part: UserPromptPart) -> chat.ChatCompletionUserMessageParam:
        content: str | list[chat.ChatCompletionContentPartParam]
        if isinstance(part.content, str):
            content = part.content
        else:
            content = []
            for item in part.content:
                if isinstance(item, str):
                    content.append(chat.ChatCompletionContentPartTextParam(text=item, type='text'))
                elif isinstance(item, ImageUrl):
                    image_url = ImageURL(url=item.url)
                    content.append(chat.ChatCompletionContentPartImageParam(image_url=image_url, type='image_url'))
                elif isinstance(item, BinaryContent):
                    if item.is_image:
                        image_url = ImageURL(url=item.data_uri)
                        content.append(chat.ChatCompletionContentPartImageParam(image_url=image_url, type='image_url'))
                    else:
                        raise RuntimeError('Only images are supported for binary content in Groq.')
                elif isinstance(item, DocumentUrl):  # pragma: no cover
                    raise RuntimeError('DocumentUrl is not supported in Groq.')
                else:  # pragma: no cover
                    raise RuntimeError(f'Unsupported content type: {type(item)}')

        return chat.ChatCompletionUserMessageParam(role='user', content=content)
```