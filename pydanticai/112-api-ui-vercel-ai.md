---
title: pydantic_ai.ui.vercel_ai - Pydantic AI
url: https://ai.pydantic.dev/api/ui/vercel_ai/
source: sitemap
fetched_at: 2026-01-22T22:25:11.152021255-03:00
rendered_js: false
word_count: 0
summary: This document defines the VercelAIAdapter class, which facilitates integration between the Vercel AI protocol and Pydantic AI by transforming message formats and handling event streams.
tags:
    - vercel-ai
    - pydantic-ai
    - ui-adapter
    - message-transformation
    - protocol-bridge
    - python-sdk
category: reference
---

```
 72
 73
 74
 75
 76
 77
 78
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
```

```
@dataclass
classVercelAIAdapter(UIAdapter[RequestData, UIMessage, BaseChunk, AgentDepsT, OutputDataT]):
"""UI adapter for the Vercel AI protocol."""

    @classmethod
    defbuild_run_input(cls, body: bytes) -> RequestData:
"""Build a Vercel AI run input object from the request body."""
        return request_data_ta.validate_json(body)

    defbuild_event_stream(self) -> UIEventStream[RequestData, BaseChunk, AgentDepsT, OutputDataT]:
"""Build a Vercel AI event stream transformer."""
        return VercelAIEventStream(self.run_input, accept=self.accept)

    @cached_property
    defmessages(self) -> list[ModelMessage]:
"""Pydantic AI messages from the Vercel AI run input."""
        return self.load_messages(self.run_input.messages)

    @classmethod
    defload_messages(cls, messages: Sequence[UIMessage]) -> list[ModelMessage]:  # noqa: C901
"""Transform Vercel AI messages into Pydantic AI messages."""
        builder = MessagesBuilder()

        for msg in messages:
            if msg.role == 'system':
                for part in msg.parts:
                    if isinstance(part, TextUIPart):
                        builder.add(SystemPromptPart(content=part.text))
                    else:  # pragma: no cover
                        raise ValueError(f'Unsupported system message part type: {type(part)}')
            elif msg.role == 'user':
                user_prompt_content: str | list[UserContent] = []
                for part in msg.parts:
                    if isinstance(part, TextUIPart):
                        user_prompt_content.append(part.text)
                    elif isinstance(part, FileUIPart):
                        try:
                            file = BinaryContent.from_data_uri(part.url)
                        except ValueError:
                            media_type_prefix = part.media_type.split('/', 1)[0]
                            match media_type_prefix:
                                case 'image':
                                    file = ImageUrl(url=part.url, media_type=part.media_type)
                                case 'video':
                                    file = VideoUrl(url=part.url, media_type=part.media_type)
                                case 'audio':
                                    file = AudioUrl(url=part.url, media_type=part.media_type)
                                case_:
                                    file = DocumentUrl(url=part.url, media_type=part.media_type)
                        user_prompt_content.append(file)
                    else:  # pragma: no cover
                        raise ValueError(f'Unsupported user message part type: {type(part)}')

                if user_prompt_content:  # pragma: no branch
                    if len(user_prompt_content) == 1 and isinstance(user_prompt_content[0], str):
                        user_prompt_content = user_prompt_content[0]
                    builder.add(UserPromptPart(content=user_prompt_content))

            elif msg.role == 'assistant':
                for part in msg.parts:
                    if isinstance(part, TextUIPart):
                        builder.add(TextPart(content=part.text))
                    elif isinstance(part, ReasoningUIPart):
                        pydantic_ai_meta = (part.provider_metadata or {}).get('pydantic_ai', {})
                        builder.add(
                            ThinkingPart(
                                content=part.text,
                                id=pydantic_ai_meta.get('id'),
                                signature=pydantic_ai_meta.get('signature'),
                                provider_name=pydantic_ai_meta.get('provider_name'),
                                provider_details=pydantic_ai_meta.get('provider_details'),
                            )
                        )
                    elif isinstance(part, FileUIPart):
                        try:
                            file = BinaryContent.from_data_uri(part.url)
                        except ValueError as e:  # pragma: no cover
                            # We don't yet handle non-data-URI file URLs returned by assistants, as no Pydantic AI models do this.
                            raise ValueError(
                                'Vercel AI integration can currently only handle assistant file parts with data URIs.'
                            ) frome
                        builder.add(FilePart(content=file))
                    elif isinstance(part, ToolUIPart | DynamicToolUIPart):
                        if isinstance(part, DynamicToolUIPart):
                            tool_name = part.tool_name
                            builtin_tool = False
                        else:
                            tool_name = part.type.removeprefix('tool-')
                            builtin_tool = part.provider_executed

                        tool_call_id = part.tool_call_id

                        args: str | dict[str, Any] | None = part.input

                        if isinstance(args, str):
                            try:
                                parsed = json.loads(args)
                                if isinstance(parsed, dict):
                                    args = cast(dict[str, Any], parsed)
                            except json.JSONDecodeError:
                                pass
                        elif isinstance(args, dict) or args is None:
                            pass
                        else:
                            assert_never(args)

                        if builtin_tool:
                            call_part = BuiltinToolCallPart(tool_name=tool_name, tool_call_id=tool_call_id, args=args)
                            builder.add(call_part)

                            if isinstance(part, ToolOutputAvailablePart | ToolOutputErrorPart):
                                if part.state == 'output-available':
                                    output = part.output
                                else:
                                    output = {'error_text': part.error_text, 'is_error': True}

                                provider_name = (
                                    (part.call_provider_metadata or {}).get('pydantic_ai', {}).get('provider_name')
                                )
                                call_part.provider_name = provider_name

                                builder.add(
                                    BuiltinToolReturnPart(
                                        tool_name=tool_name,
                                        tool_call_id=tool_call_id,
                                        content=output,
                                        provider_name=provider_name,
                                    )
                                )
                        else:
                            builder.add(ToolCallPart(tool_name=tool_name, tool_call_id=tool_call_id, args=args))

                            if part.state == 'output-available':
                                builder.add(
                                    ToolReturnPart(tool_name=tool_name, tool_call_id=tool_call_id, content=part.output)
                                )
                            elif part.state == 'output-error':
                                builder.add(
                                    RetryPromptPart(
                                        tool_name=tool_name, tool_call_id=tool_call_id, content=part.error_text
                                    )
                                )
                    elif isinstance(part, DataUIPart):  # pragma: no cover
                        # Contains custom data that shouldn't be sent to the model
                        pass
                    elif isinstance(part, SourceUrlUIPart):  # pragma: no cover
                        # TODO: Once we support citations: https://github.com/pydantic/pydantic-ai/issues/3126
                        pass
                    elif isinstance(part, SourceDocumentUIPart):  # pragma: no cover
                        # TODO: Once we support citations: https://github.com/pydantic/pydantic-ai/issues/3126
                        pass
                    elif isinstance(part, StepStartUIPart):  # pragma: no cover
                        # Nothing to do here
                        pass
                    else:
                        assert_never(part)
            else:
                assert_never(msg.role)

        return builder.messages

    @staticmethod
    def_dump_request_message(msg: ModelRequest) -> tuple[list[UIMessagePart], list[UIMessagePart]]:
"""Convert a ModelRequest into a UIMessage."""
        system_ui_parts: list[UIMessagePart] = []
        user_ui_parts: list[UIMessagePart] = []

        for part in msg.parts:
            if isinstance(part, SystemPromptPart):
                system_ui_parts.append(TextUIPart(text=part.content, state='done'))
            elif isinstance(part, UserPromptPart):
                user_ui_parts.extend(_convert_user_prompt_part(part))
            elif isinstance(part, ToolReturnPart):
                # Tool returns are merged into the tool call in the assistant message
                pass
            elif isinstance(part, RetryPromptPart):
                if part.tool_name:
                    # Tool-related retries are handled when processing ToolCallPart in ModelResponse
                    pass
                else:
                    # Non-tool retries (e.g., output validation errors) become user text
                    user_ui_parts.append(TextUIPart(text=part.model_response(), state='done'))
            else:
                assert_never(part)

        return system_ui_parts, user_ui_parts

    @staticmethod
    def_dump_response_message(  # noqa: C901
        msg: ModelResponse,
        tool_results: dict[str, ToolReturnPart | RetryPromptPart],
    ) -> list[UIMessagePart]:
"""Convert a ModelResponse into a UIMessage."""
        ui_parts: list[UIMessagePart] = []

        # For builtin tools, returns can be in the same ModelResponse as calls
        local_builtin_returns: dict[str, BuiltinToolReturnPart] = {
            part.tool_call_id: part for part in msg.parts if isinstance(part, BuiltinToolReturnPart)
        }

        for part in msg.parts:
            if isinstance(part, BuiltinToolReturnPart):
                continue
            elif isinstance(part, TextPart):
                # Combine consecutive text parts
                if ui_parts and isinstance(ui_parts[-1], TextUIPart):
                    ui_parts[-1].text += part.content
                else:
                    ui_parts.append(TextUIPart(text=part.content, state='done'))
            elif isinstance(part, ThinkingPart):
                thinking_metadata: dict[str, Any] = {}
                if part.id is not None:
                    thinking_metadata['id'] = part.id
                if part.signature is not None:
                    thinking_metadata['signature'] = part.signature
                if part.provider_name is not None:
                    thinking_metadata['provider_name'] = part.provider_name
                if part.provider_details is not None:
                    thinking_metadata['provider_details'] = part.provider_details

                provider_metadata = {'pydantic_ai': thinking_metadata} if thinking_metadata else None
                ui_parts.append(ReasoningUIPart(text=part.content, state='done', provider_metadata=provider_metadata))
            elif isinstance(part, FilePart):
                ui_parts.append(
                    FileUIPart(
                        url=part.content.data_uri,
                        media_type=part.content.media_type,
                    )
                )
            elif isinstance(part, BuiltinToolCallPart):
                call_provider_metadata = (
                    {'pydantic_ai': {'provider_name': part.provider_name}} if part.provider_name else None
                )

                if builtin_return := local_builtin_returns.get(part.tool_call_id):
                    content = builtin_return.model_response_str()
                    ui_parts.append(
                        ToolOutputAvailablePart(
                            type=f'tool-{part.tool_name}',
                            tool_call_id=part.tool_call_id,
                            input=part.args_as_json_str(),
                            output=content,
                            state='output-available',
                            provider_executed=True,
                            call_provider_metadata=call_provider_metadata,
                        )
                    )
                else:
                    ui_parts.append(
                        ToolInputAvailablePart(
                            type=f'tool-{part.tool_name}',
                            tool_call_id=part.tool_call_id,
                            input=part.args_as_json_str(),
                            state='input-available',
                            provider_executed=True,
                            call_provider_metadata=call_provider_metadata,
                        )
                    )
            elif isinstance(part, ToolCallPart):
                tool_result = tool_results.get(part.tool_call_id)

                if isinstance(tool_result, ToolReturnPart):
                    content = tool_result.model_response_str()
                    ui_parts.append(
                        DynamicToolOutputAvailablePart(
                            tool_name=part.tool_name,
                            tool_call_id=part.tool_call_id,
                            input=part.args_as_json_str(),
                            output=content,
                            state='output-available',
                        )
                    )
                elif isinstance(tool_result, RetryPromptPart):
                    error_text = tool_result.model_response()
                    ui_parts.append(
                        DynamicToolOutputErrorPart(
                            tool_name=part.tool_name,
                            tool_call_id=part.tool_call_id,
                            input=part.args_as_json_str(),
                            error_text=error_text,
                            state='output-error',
                        )
                    )
                else:
                    ui_parts.append(
                        DynamicToolInputAvailablePart(
                            tool_name=part.tool_name,
                            tool_call_id=part.tool_call_id,
                            input=part.args_as_json_str(),
                            state='input-available',
                        )
                    )
            else:
                assert_never(part)

        return ui_parts

    @classmethod
    defdump_messages(
        cls,
        messages: Sequence[ModelMessage],
    ) -> list[UIMessage]:
"""Transform Pydantic AI messages into Vercel AI messages.

        Args:
            messages: A sequence of ModelMessage objects to convert

        Returns:
            A list of UIMessage objects in Vercel AI format
        """
        tool_results: dict[str, ToolReturnPart | RetryPromptPart] = {}

        for msg in messages:
            if isinstance(msg, ModelRequest):
                for part in msg.parts:
                    if isinstance(part, ToolReturnPart):
                        tool_results[part.tool_call_id] = part
                    elif isinstance(part, RetryPromptPart) and part.tool_name:
                        tool_results[part.tool_call_id] = part

        result: list[UIMessage] = []

        for msg in messages:
            if isinstance(msg, ModelRequest):
                system_ui_parts, user_ui_parts = cls._dump_request_message(msg)
                if system_ui_parts:
                    result.append(UIMessage(id=str(uuid.uuid4()), role='system', parts=system_ui_parts))

                if user_ui_parts:
                    result.append(UIMessage(id=str(uuid.uuid4()), role='user', parts=user_ui_parts))

            elif isinstance(  # pragma: no branch
                msg, ModelResponse
            ):
                ui_parts: list[UIMessagePart] = cls._dump_response_message(msg, tool_results)
                if ui_parts:  # pragma: no branch
                    result.append(UIMessage(id=str(uuid.uuid4()), role='assistant', parts=ui_parts))
            else:
                assert_never(msg)

        return result
```