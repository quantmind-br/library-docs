---
title: pydantic_ai.models.cohere - Pydantic AI
url: https://ai.pydantic.dev/api/models/cohere/
source: sitemap
fetched_at: 2026-01-22T22:24:25.267322298-03:00
rendered_js: false
word_count: 38
summary: Implementation of the CohereModel class for integrating the Cohere API into a model framework, handling message mapping, chat requests, and response processing.
tags:
    - cohere-api
    - python-sdk
    - model-integration
    - async-client
    - llm-interface
category: api
---

```
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
```

```
@dataclass(init=False)
classCohereModel(Model):
"""A model that uses the Cohere API.

    Internally, this uses the [Cohere Python client](
    https://github.com/cohere-ai/cohere-python) to interact with the API.

    Apart from `__init__`, all methods are private or match those of the base class.
    """

    client: AsyncClientV2 = field(repr=False)

    _model_name: CohereModelName = field(repr=False)
    _provider: Provider[AsyncClientV2] = field(repr=False)

    def__init__(
        self,
        model_name: CohereModelName,
        *,
        provider: Literal['cohere'] | Provider[AsyncClientV2] = 'cohere',
        profile: ModelProfileSpec | None = None,
        settings: ModelSettings | None = None,
    ):
"""Initialize an Cohere model.

        Args:
            model_name: The name of the Cohere model to use. List of model names
                available [here](https://docs.cohere.com/docs/models#command).
            provider: The provider to use for authentication and API access. Can be either the string
                'cohere' or an instance of `Provider[AsyncClientV2]`. If not provided, a new provider will be
                created using the other parameters.
            profile: The model profile to use. Defaults to a profile picked by the provider based on the model name.
            settings: Model-specific settings that will be used as defaults for this model.
        """
        self._model_name = model_name

        if isinstance(provider, str):
            provider = infer_provider(provider)
        self._provider = provider
        self.client = provider.client

        super().__init__(settings=settings, profile=profile or provider.model_profile)

    @property
    defbase_url(self) -> str:
        client_wrapper = self.client._client_wrapper  # type: ignore
        return str(client_wrapper.get_base_url())

    @property
    defmodel_name(self) -> CohereModelName:
"""The model name."""
        return self._model_name

    @property
    defsystem(self) -> str:
"""The model provider."""
        return self._provider.name

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
        response = await self._chat(messages, cast(CohereModelSettings, model_settings or {}), model_request_parameters)
        model_response = self._process_response(response)
        return model_response

    async def_chat(
        self,
        messages: list[ModelMessage],
        model_settings: CohereModelSettings,
        model_request_parameters: ModelRequestParameters,
    ) -> V2ChatResponse:
        tools = self._get_tools(model_request_parameters)

        cohere_messages = self._map_messages(messages, model_request_parameters)
        try:
            return await self.client.chat(
                model=self._model_name,
                messages=cohere_messages,
                tools=tools or OMIT,
                max_tokens=model_settings.get('max_tokens', OMIT),
                stop_sequences=model_settings.get('stop_sequences', OMIT),
                temperature=model_settings.get('temperature', OMIT),
                p=model_settings.get('top_p', OMIT),
                seed=model_settings.get('seed', OMIT),
                presence_penalty=model_settings.get('presence_penalty', OMIT),
                frequency_penalty=model_settings.get('frequency_penalty', OMIT),
            )
        except ApiError as e:
            if (status_code := e.status_code) and status_code >= 400:
                raise ModelHTTPError(status_code=status_code, model_name=self.model_name, body=e.body) frome
            raise ModelAPIError(model_name=self.model_name, message=str(e)) frome

    def_process_response(self, response: V2ChatResponse) -> ModelResponse:
"""Process a non-streamed response, and prepare a message to return."""
        parts: list[ModelResponsePart] = []
        if response.message.content is not None:
            for content in response.message.content:
                if content.type == 'text':
                    parts.append(TextPart(content=content.text))
                elif content.type == 'thinking':  # pragma: no branch
                    parts.append(ThinkingPart(content=content.thinking))
        for c in response.message.tool_calls or []:
            if c.function and c.function.name and c.function.arguments:  # pragma: no branch
                parts.append(
                    ToolCallPart(
                        tool_name=c.function.name,
                        args=c.function.arguments,
                        tool_call_id=c.id or _generate_tool_call_id(),
                    )
                )

        raw_finish_reason = response.finish_reason
        provider_details = {'finish_reason': raw_finish_reason}
        finish_reason = _FINISH_REASON_MAP.get(raw_finish_reason)

        return ModelResponse(
            parts=parts,
            usage=_map_usage(response),
            model_name=self._model_name,
            provider_name=self._provider.name,
            provider_url=self.base_url,
            finish_reason=finish_reason,
            provider_details=provider_details,
        )

    def_map_messages(
        self, messages: list[ModelMessage], model_request_parameters: ModelRequestParameters
    ) -> list[ChatMessageV2]:
"""Just maps a `pydantic_ai.Message` to a `cohere.ChatMessageV2`."""
        cohere_messages: list[ChatMessageV2] = []
        for message in messages:
            if isinstance(message, ModelRequest):
                cohere_messages.extend(self._map_user_message(message))
            elif isinstance(message, ModelResponse):
                texts: list[str] = []
                thinking: list[str] = []
                tool_calls: list[ToolCallV2] = []
                for item in message.parts:
                    if isinstance(item, TextPart):
                        texts.append(item.content)
                    elif isinstance(item, ThinkingPart):
                        thinking.append(item.content)
                    elif isinstance(item, ToolCallPart):
                        tool_calls.append(self._map_tool_call(item))
                    elif isinstance(item, BuiltinToolCallPart | BuiltinToolReturnPart):  # pragma: no cover
                        # This is currently never returned from cohere
                        pass
                    elif isinstance(item, FilePart):  # pragma: no cover
                        # Files generated by models are not sent back to models that don't themselves generate files.
                        pass
                    else:
                        assert_never(item)

                message_param = AssistantChatMessageV2(role='assistant')
                if texts or thinking:
                    contents: list[AssistantMessageV2ContentItem] = []
                    if thinking:
                        contents.append(ThinkingAssistantMessageV2ContentItem(thinking='\n\n'.join(thinking)))
                    if texts:  # pragma: no branch
                        contents.append(TextAssistantMessageV2ContentItem(text='\n\n'.join(texts)))
                    message_param.content = contents
                if tool_calls:
                    message_param.tool_calls = tool_calls
                cohere_messages.append(message_param)
            else:
                assert_never(message)
        if instructions := self._get_instructions(messages, model_request_parameters):
            system_prompt_count = sum(1 for m in cohere_messages if isinstance(m, SystemChatMessageV2))
            cohere_messages.insert(system_prompt_count, SystemChatMessageV2(role='system', content=instructions))
        return cohere_messages

    def_get_tools(self, model_request_parameters: ModelRequestParameters) -> list[ToolV2]:
        return [self._map_tool_definition(r) for r in model_request_parameters.tool_defs.values()]

    @staticmethod
    def_map_tool_call(t: ToolCallPart) -> ToolCallV2:
        return ToolCallV2(
            id=_guard_tool_call_id(t=t),
            type='function',
            function=ToolCallV2Function(
                name=t.tool_name,
                arguments=t.args_as_json_str(),
            ),
        )

    @staticmethod
    def_map_tool_definition(f: ToolDefinition) -> ToolV2:
        return ToolV2(
            type='function',
            function=ToolV2Function(
                name=f.name,
                description=f.description,
                parameters=f.parameters_json_schema,
            ),
        )

    @classmethod
    def_map_user_message(cls, message: ModelRequest) -> Iterable[ChatMessageV2]:
        for part in message.parts:
            if isinstance(part, SystemPromptPart):
                yield SystemChatMessageV2(role='system', content=part.content)
            elif isinstance(part, UserPromptPart):
                if isinstance(part.content, str):
                    yield UserChatMessageV2(role='user', content=part.content)
                else:
                    raise RuntimeError('Cohere does not yet support multi-modal inputs.')
            elif isinstance(part, ToolReturnPart):
                yield ToolChatMessageV2(
                    role='tool',
                    tool_call_id=_guard_tool_call_id(t=part),
                    content=part.model_response_str(),
                )
            elif isinstance(part, RetryPromptPart):
                if part.tool_name is None:
                    yield UserChatMessageV2(role='user', content=part.model_response())  # pragma: no cover
                else:
                    yield ToolChatMessageV2(
                        role='tool',
                        tool_call_id=_guard_tool_call_id(t=part),
                        content=part.model_response(),
                    )
            else:
                assert_never(part)
```