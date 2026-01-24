---
title: pydantic_ai.models.test - Pydantic AI
url: https://ai.pydantic.dev/api/models/test/
source: sitemap
fetched_at: 2026-01-22T22:24:42.82839677-03:00
rendered_js: false
word_count: 79
summary: This document defines the TestModel class, a mock model implementation used for testing AI agents by simulating tool calls and deterministic responses.
tags:
    - python
    - testing
    - mock-model
    - ai-agents
    - pydantic-ai
    - unit-testing
category: api
---

```
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
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
```

```
@dataclass(init=False)
classTestModel(Model):
"""A model specifically for testing purposes.

    This will (by default) call all tools in the agent, then return a tool response if possible,
    otherwise a plain response.

    How useful this model is will vary significantly.

    Apart from `__init__` derived by the `dataclass` decorator, all methods are private or match those
    of the base class.
    """

    # NOTE: Avoid test discovery by pytest.
    __test__ = False

    call_tools: list[str] | Literal['all'] = 'all'
"""List of tools to call. If `'all'`, all tools will be called."""
    custom_output_text: str | None = None
"""If set, this text is returned as the final output."""
    custom_output_args: Any | None = None
"""If set, these args will be passed to the output tool."""
    seed: int = 0
"""Seed for generating random data."""
    last_model_request_parameters: ModelRequestParameters | None = field(default=None, init=False)
"""The last ModelRequestParameters passed to the model in a request.

    The ModelRequestParameters contains information about the function and output tools available during request handling.

    This is set when a request is made, so will reflect the function tools from the last step of the last run.
    """
    _model_name: str = field(default='test', repr=False)
    _system: str = field(default='test', repr=False)

    def__init__(
        self,
        *,
        call_tools: list[str] | Literal['all'] = 'all',
        custom_output_text: str | None = None,
        custom_output_args: Any | None = None,
        seed: int = 0,
        model_name: str = 'test',
        profile: ModelProfileSpec | None = None,
        settings: ModelSettings | None = None,
    ):
"""Initialize TestModel with optional settings and profile."""
        self.call_tools = call_tools
        self.custom_output_text = custom_output_text
        self.custom_output_args = custom_output_args
        self.seed = seed
        self.last_model_request_parameters = None
        self._model_name = model_name
        self._system = 'test'
        super().__init__(settings=settings, profile=profile)

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
        self.last_model_request_parameters = model_request_parameters
        model_response = self._request(messages, model_settings, model_request_parameters)
        model_response.usage = _estimate_usage([*messages, model_response])
        return model_response

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
        self.last_model_request_parameters = model_request_parameters

        model_response = self._request(messages, model_settings, model_request_parameters)
        yield TestStreamedResponse(
            model_request_parameters=model_request_parameters,
            _model_name=self._model_name,
            _structured_response=model_response,
            _messages=messages,
            _provider_name=self._system,
        )

    @property
    defmodel_name(self) -> str:
"""The model name."""
        return self._model_name

    @property
    defsystem(self) -> str:
"""The model provider."""
        return self._system

    @classmethod
    defsupported_builtin_tools(cls) -> frozenset[type[AbstractBuiltinTool]]:
"""TestModel supports all builtin tools for testing flexibility."""
        return SUPPORTED_BUILTIN_TOOLS

    defgen_tool_args(self, tool_def: ToolDefinition) -> Any:
        return _JsonSchemaTestData(tool_def.parameters_json_schema, self.seed).generate()

    def_get_tool_calls(self, model_request_parameters: ModelRequestParameters) -> list[tuple[str, ToolDefinition]]:
        if self.call_tools == 'all':
            return [(r.name, r) for r in model_request_parameters.function_tools]
        else:
            function_tools_lookup = {t.name: t for t in model_request_parameters.function_tools}
            tools_to_call = (function_tools_lookup[name] for name in self.call_tools)
            return [(r.name, r) for r in tools_to_call]

    def_get_output(self, model_request_parameters: ModelRequestParameters) -> _WrappedTextOutput | _WrappedToolOutput:
        if self.custom_output_text is not None:
            assert model_request_parameters.output_mode != 'tool', (
                'Plain response not allowed, but `custom_output_text` is set.'
            )
            assert self.custom_output_args is None, 'Cannot set both `custom_output_text` and `custom_output_args`.'
            return _WrappedTextOutput(self.custom_output_text)
        elif self.custom_output_args is not None:
            assert model_request_parameters.output_tools is not None, (
                'No output tools provided, but `custom_output_args` is set.'
            )
            output_tool = model_request_parameters.output_tools[0]

            if k := output_tool.outer_typed_dict_key:
                return _WrappedToolOutput({k: self.custom_output_args})
            else:
                return _WrappedToolOutput(self.custom_output_args)
        elif model_request_parameters.allow_text_output:
            return _WrappedTextOutput(None)
        elif model_request_parameters.output_tools:
            return _WrappedToolOutput(None)
        else:
            return _WrappedTextOutput(None)

    def_request(
        self,
        messages: list[ModelMessage],
        model_settings: ModelSettings | None,
        model_request_parameters: ModelRequestParameters,
    ) -> ModelResponse:
        if model_request_parameters.builtin_tools:
            raise UserError('TestModel does not support built-in tools')

        tool_calls = self._get_tool_calls(model_request_parameters)
        output_wrapper = self._get_output(model_request_parameters)
        output_tools = model_request_parameters.output_tools

        # if there are tools, the first thing we want to do is call all of them
        if tool_calls and not any(isinstance(m, ModelResponse) for m in messages):
            return ModelResponse(
                parts=[
                    ToolCallPart(name, self.gen_tool_args(args), tool_call_id=f'pyd_ai_tool_call_id__{name}')
                    for name, args in tool_calls
                ],
                model_name=self._model_name,
            )

        if messages:  # pragma: no branch
            last_message = messages[-1]
            assert isinstance(last_message, ModelRequest), 'Expected last message to be a `ModelRequest`.'

            # check if there are any retry prompts, if so retry them
            new_retry_names = {p.tool_name for p in last_message.parts if isinstance(p, RetryPromptPart)}
            if new_retry_names:
                # Handle retries for both function tools and output tools
                # Check function tools first
                retry_parts: list[ModelResponsePart] = [
                    ToolCallPart(name, self.gen_tool_args(args)) for name, args in tool_calls if name in new_retry_names
                ]
                # Check output tools
                if output_tools:
                    retry_parts.extend(
                        [
                            ToolCallPart(
                                tool.name,
                                output_wrapper.value
                                if isinstance(output_wrapper, _WrappedToolOutput) and output_wrapper.value is not None
                                else self.gen_tool_args(tool),
                                tool_call_id=f'pyd_ai_tool_call_id__{tool.name}',
                            )
                            for tool in output_tools
                            if tool.name in new_retry_names
                        ]
                    )
                return ModelResponse(parts=retry_parts, model_name=self._model_name)

        if isinstance(output_wrapper, _WrappedTextOutput):
            if (response_text := output_wrapper.value) is None:
                # build up details of tool responses
                output: dict[str, Any] = {}
                for message in messages:
                    if isinstance(message, ModelRequest):
                        for part in message.parts:
                            if isinstance(part, ToolReturnPart):
                                output[part.tool_name] = part.content
                if output:
                    return ModelResponse(
                        parts=[TextPart(pydantic_core.to_json(output).decode())], model_name=self._model_name
                    )
                else:
                    return ModelResponse(parts=[TextPart('success (no tool calls)')], model_name=self._model_name)
            else:
                return ModelResponse(parts=[TextPart(response_text)], model_name=self._model_name)
        else:
            assert output_tools, 'No output tools provided'
            custom_output_args = output_wrapper.value
            output_tool = output_tools[self.seed % len(output_tools)]
            if custom_output_args is not None:
                return ModelResponse(
                    parts=[
                        ToolCallPart(
                            output_tool.name,
                            custom_output_args,
                            tool_call_id=f'pyd_ai_tool_call_id__{output_tool.name}',
                        )
                    ],
                    model_name=self._model_name,
                )
            else:
                response_args = self.gen_tool_args(output_tool)
                return ModelResponse(
                    parts=[
                        ToolCallPart(
                            output_tool.name,
                            response_args,
                            tool_call_id=f'pyd_ai_tool_call_id__{output_tool.name}',
                        )
                    ],
                    model_name=self._model_name,
                )
```