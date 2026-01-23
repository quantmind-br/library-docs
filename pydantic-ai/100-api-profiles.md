---
title: pydantic_ai.profiles - Pydantic AI
url: https://ai.pydantic.dev/api/profiles/
source: sitemap
fetched_at: 2026-01-22T22:24:09.992252023-03:00
rendered_js: false
word_count: 647
summary: This document defines the OpenAIModelProfile dataclass used to configure settings and compatibility flags for OpenAI and OpenAI-compatible chat models.
tags:
    - pydantic-ai
    - openai-model-profile
    - llm-configuration
    - api-compatibility
    - model-settings
category: api
---

### OpenAIModelProfile `dataclass`

Bases: `ModelProfile`

Profile for models used with `OpenAIChatModel`.

ALL FIELDS MUST BE `openai_` PREFIXED SO YOU CAN MERGE THEM WITH OTHER MODELS.

Source code in `pydantic_ai_slim/pydantic_ai/profiles/openai.py`

```
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
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
```

```
@dataclass(kw_only=True)
classOpenAIModelProfile(ModelProfile):
"""Profile for models used with `OpenAIChatModel`.

    ALL FIELDS MUST BE `openai_` PREFIXED SO YOU CAN MERGE THEM WITH OTHER MODELS.
    """

    openai_chat_thinking_field: str | None = None
"""Non-standard field name used by some providers for model thinking content in Chat Completions API responses.

    Plenty of providers use custom field names for thinking content. Ollama and newer versions of vLLM use `reasoning`,
    while DeepSeek, older vLLM and some others use `reasoning_content`.

    Notice that the thinking field configured here is currently limited to `str` type content.

    If `openai_chat_send_back_thinking_parts` is set to `'field'`, this field must be set to a non-None value."""

    openai_chat_send_back_thinking_parts: Literal['tags', 'field', False] = 'tags'
"""Whether the model includes thinking content in requests.

    This can be:
    * `'tags'` (default): The thinking content is included in the main `content` field, enclosed within thinking tags as
    specified in `thinking_tags` profile option.
    * `'field'`: The thinking content is included in a separate field specified by `openai_chat_thinking_field`.
    * `False`: No thinking content is sent in the request.

    Defaults to `'thinking_tags'` for backward compatibility reasons."""

    openai_supports_strict_tool_definition: bool = True
"""This can be set by a provider or user if the OpenAI-"compatible" API doesn't support strict tool definitions."""

    openai_supports_sampling_settings: bool = True
"""Turn off to don't send sampling settings like `temperature` and `top_p` to models that don't support them, like OpenAI's o-series reasoning models."""

    openai_unsupported_model_settings: Sequence[str] = ()
"""A list of model settings that are not supported by this model."""

    # Some OpenAI-compatible providers (e.g. MoonshotAI) currently do **not** accept
    # `tool_choice="required"`.  This flag lets the calling model know whether it's
    # safe to pass that value along.  Default is `True` to preserve existing
    # behaviour for OpenAI itself and most providers.
    openai_supports_tool_choice_required: bool = True
"""Whether the provider accepts the value ``tool_choice='required'`` in the request payload."""

    openai_system_prompt_role: OpenAISystemPromptRole | None = None
"""The role to use for the system prompt message. If not provided, defaults to `'system'`."""

    openai_chat_supports_web_search: bool = False
"""Whether the model supports web search in Chat Completions API."""

    openai_chat_audio_input_encoding: Literal['base64', 'uri'] = 'base64'
"""The encoding to use for audio input in Chat Completions requests.

    - `'base64'`: Raw base64 encoded string. (Default, used by OpenAI)
    - `'uri'`: Data URI (e.g. `data:audio/wav;base64,...`).
    """

    openai_chat_supports_file_urls: bool = False
"""Whether the Chat API supports file URLs directly in the `file_data` field.

    OpenAI's native Chat API only supports base64-encoded data, but some providers
    like OpenRouter support passing URLs directly.
    """

    openai_supports_encrypted_reasoning_content: bool = False
"""Whether the model supports including encrypted reasoning content in the response."""

    openai_responses_requires_function_call_status_none: bool = False
"""Whether the Responses API requires the `status` field on function tool calls to be `None`.

    This is required by vLLM Responses API versions before https://github.com/vllm-project/vllm/pull/26706.
    See https://github.com/pydantic/pydantic-ai/issues/3245 for more details.
    """

    def__post_init__(self):  # pragma: no cover
        if not self.openai_supports_sampling_settings:
            warnings.warn(
                'The `openai_supports_sampling_settings` has no effect, and it will be removed in future versions. '
                'Use `openai_unsupported_model_settings` instead.',
                DeprecationWarning,
            )
        if self.openai_chat_send_back_thinking_parts == 'field' and not self.openai_chat_thinking_field:
            raise UserError(
                'If `openai_chat_send_back_thinking_parts` is "field", '
                '`openai_chat_thinking_field` must be set to a non-None value.'
            )
```

#### openai\_chat\_thinking\_field `class-attribute` `instance-attribute`

```
openai_chat_thinking_field: str | None = None
```

Non-standard field name used by some providers for model thinking content in Chat Completions API responses.

Plenty of providers use custom field names for thinking content. Ollama and newer versions of vLLM use `reasoning`, while DeepSeek, older vLLM and some others use `reasoning_content`.

Notice that the thinking field configured here is currently limited to `str` type content.

If `openai_chat_send_back_thinking_parts` is set to `'field'`, this field must be set to a non-None value.

#### openai\_chat\_send\_back\_thinking\_parts `class-attribute` `instance-attribute`

```
openai_chat_send_back_thinking_parts: Literal[
    "tags", "field", False
] = "tags"
```

Whether the model includes thinking content in requests.

This can be: * `'tags'` (default): The thinking content is included in the main `content` field, enclosed within thinking tags as specified in `thinking_tags` profile option. * `'field'`: The thinking content is included in a separate field specified by `openai_chat_thinking_field`. * `False`: No thinking content is sent in the request.

Defaults to `'thinking_tags'` for backward compatibility reasons.

#### openai\_supports\_strict\_tool\_definition `class-attribute` `instance-attribute`

```
openai_supports_strict_tool_definition: bool = True
```

This can be set by a provider or user if the OpenAI-"compatible" API doesn't support strict tool definitions.

#### openai\_supports\_sampling\_settings `class-attribute` `instance-attribute`

```
openai_supports_sampling_settings: bool = True
```

Turn off to don't send sampling settings like `temperature` and `top_p` to models that don't support them, like OpenAI's o-series reasoning models.

#### openai\_unsupported\_model\_settings `class-attribute` `instance-attribute`

A list of model settings that are not supported by this model.

#### openai\_supports\_tool\_choice\_required `class-attribute` `instance-attribute`

```
openai_supports_tool_choice_required: bool = True
```

Whether the provider accepts the value `tool_choice='required'` in the request payload.

#### openai\_system\_prompt\_role `class-attribute` `instance-attribute`

```
openai_system_prompt_role: OpenAISystemPromptRole | None = (
    None
)
```

The role to use for the system prompt message. If not provided, defaults to `'system'`.

#### openai\_chat\_supports\_web\_search `class-attribute` `instance-attribute`

```
openai_chat_supports_web_search: bool = False
```

Whether the model supports web search in Chat Completions API.

#### openai\_chat\_audio\_input\_encoding `class-attribute` `instance-attribute`

```
openai_chat_audio_input_encoding: Literal[
    "base64", "uri"
] = "base64"
```

The encoding to use for audio input in Chat Completions requests.

- `'base64'`: Raw base64 encoded string. (Default, used by OpenAI)
- `'uri'`: Data URI (e.g. `data:audio/wav;base64,...`).

#### openai\_chat\_supports\_file\_urls `class-attribute` `instance-attribute`

```
openai_chat_supports_file_urls: bool = False
```

Whether the Chat API supports file URLs directly in the `file_data` field.

OpenAI's native Chat API only supports base64-encoded data, but some providers like OpenRouter support passing URLs directly.

#### openai\_supports\_encrypted\_reasoning\_content `class-attribute` `instance-attribute`

```
openai_supports_encrypted_reasoning_content: bool = False
```

Whether the model supports including encrypted reasoning content in the response.

#### openai\_responses\_requires\_function\_call\_status\_none `class-attribute` `instance-attribute`

```
openai_responses_requires_function_call_status_none: (
    bool
) = False
```

Whether the Responses API requires the `status` field on function tool calls to be `None`.

This is required by vLLM Responses API versions before https://github.com/vllm-project/vllm/pull/26706. See https://github.com/pydantic/pydantic-ai/issues/3245 for more details.

### openai\_model\_profile

```
openai_model_profile(model_name: str) -> ModelProfile
```

Get the model profile for an OpenAI model.

Source code in `pydantic_ai_slim/pydantic_ai/profiles/openai.py`

```
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
```

```
defopenai_model_profile(model_name: str) -> ModelProfile:
"""Get the model profile for an OpenAI model."""
    is_gpt_5 = model_name.startswith('gpt-5')
    is_o_series = model_name.startswith('o')
    is_reasoning_model = is_o_series or (is_gpt_5 and 'gpt-5-chat' not in model_name)

    # Check if the model supports web search (only specific search-preview models)
    supports_web_search = '-search-preview' in model_name

    # Structured Outputs (output mode 'native') is only supported with the gpt-4o-mini, gpt-4o-mini-2024-07-18, and gpt-4o-2024-08-06 model snapshots and later.
    # We leave it in here for all models because the `default_structured_output_mode` is `'tool'`, so `native` is only used
    # when the user specifically uses the `NativeOutput` marker, so an error from the API is acceptable.

    if is_reasoning_model:
        openai_unsupported_model_settings = (
            'temperature',
            'top_p',
            'presence_penalty',
            'frequency_penalty',
            'logit_bias',
            'logprobs',
            'top_logprobs',
        )
    else:
        openai_unsupported_model_settings = ()

    # The o1-mini model doesn't support the `system` role, so we default to `user`.
    # See https://github.com/pydantic/pydantic-ai/issues/974 for more details.
    openai_system_prompt_role = 'user' if model_name.startswith('o1-mini') else None

    return OpenAIModelProfile(
        json_schema_transformer=OpenAIJsonSchemaTransformer,
        supports_json_schema_output=True,
        supports_json_object_output=True,
        supports_image_output=is_gpt_5 or 'o3' in model_name or '4.1' in model_name or '4o' in model_name,
        openai_unsupported_model_settings=openai_unsupported_model_settings,
        openai_system_prompt_role=openai_system_prompt_role,
        openai_chat_supports_web_search=supports_web_search,
        openai_supports_encrypted_reasoning_content=is_reasoning_model,
    )
```

### OpenAIJsonSchemaTransformer `dataclass`

Bases: `JsonSchemaTransformer`

Recursively handle the schema to make it compatible with OpenAI strict mode.

See https://platform.openai.com/docs/guides/function-calling?api-mode=responses#strict-mode for more details, but this basically just requires: * `additionalProperties` must be set to false for each object in the parameters * all fields in properties must be marked as required

Source code in `pydantic_ai_slim/pydantic_ai/profiles/openai.py`

```
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
```

```
@dataclass(init=False)
classOpenAIJsonSchemaTransformer(JsonSchemaTransformer):
"""Recursively handle the schema to make it compatible with OpenAI strict mode.

    See https://platform.openai.com/docs/guides/function-calling?api-mode=responses#strict-mode for more details,
    but this basically just requires:
    * `additionalProperties` must be set to false for each object in the parameters
    * all fields in properties must be marked as required
    """

    def__init__(self, schema: JsonSchema, *, strict: bool | None = None):
        super().__init__(schema, strict=strict)
        self.root_ref = schema.get('$ref')

    defwalk(self) -> JsonSchema:
        # Note: OpenAI does not support anyOf at the root in strict mode
        # However, we don't need to check for it here because we ensure in pydantic_ai._utils.check_object_json_schema
        # that the root schema either has type 'object' or is recursive.
        result = super().walk()

        # For recursive models, we need to tweak the schema to make it compatible with strict mode.
        # Because the following should never change the semantics of the schema we apply it unconditionally.
        if self.root_ref is not None:
            result.pop('$ref', None)  # We replace references to the self.root_ref with just '#' in the transform method
            root_key = re.sub(r'^#/\$defs/', '', self.root_ref)
            result.update(self.defs.get(root_key) or {})

        return result

    deftransform(self, schema: JsonSchema) -> JsonSchema:  # noqa: C901
        # Remove unnecessary keys
        schema.pop('title', None)
        schema.pop('$schema', None)
        schema.pop('discriminator', None)

        default = schema.get('default', _sentinel)
        if default is not _sentinel:
            # the "default" keyword is not allowed in strict mode, but including it makes some Ollama models behave
            # better, so we keep it around when not strict
            if self.strict is True:
                schema.pop('default', None)
            elif self.strict is None:  # pragma: no branch
                self.is_strict_compatible = False

        if schema_ref := schema.get('$ref'):
            if schema_ref == self.root_ref:
                schema['$ref'] = '#'
            if len(schema) > 1:
                # OpenAI Strict mode doesn't support siblings to "$ref", but _does_ allow siblings to "anyOf".
                # So if there is a "description" field or any other extra info, we move the "$ref" into an "anyOf":
                schema['anyOf'] = [{'$ref': schema.pop('$ref')}]

        # Track strict-incompatible keys
        incompatible_values: dict[str, Any] = {}
        for key in _STRICT_INCOMPATIBLE_KEYS:
            value = schema.get(key, _sentinel)
            if value is not _sentinel:
                incompatible_values[key] = value
        if format := schema.get('format'):
            if format not in _STRICT_COMPATIBLE_STRING_FORMATS:
                incompatible_values['format'] = format
        description = schema.get('description')
        if incompatible_values:
            if self.strict is True:
                notes: list[str] = []
                for key, value in incompatible_values.items():
                    schema.pop(key)
                    notes.append(f'{key}={value}')
                notes_string = ', '.join(notes)
                schema['description'] = notes_string if not description else f'{description} ({notes_string})'
            elif self.strict is None:  # pragma: no branch
                self.is_strict_compatible = False

        schema_type = schema.get('type')
        if 'oneOf' in schema:
            # OpenAI does not support oneOf in strict mode
            if self.strict is True:
                schema['anyOf'] = schema.pop('oneOf')
            else:
                self.is_strict_compatible = False

        if schema_type == 'object':
            # Always ensure 'properties' key exists - OpenAI drops objects without it
            if 'properties' not in schema:
                schema['properties'] = dict[str, Any]()

            if self.strict is True:
                # additional properties are disallowed
                schema['additionalProperties'] = False

                # all properties are required
                schema['required'] = list(schema['properties'].keys())

            elif self.strict is None:
                if schema.get('additionalProperties', None) not in (None, False):
                    self.is_strict_compatible = False
                else:
                    # additional properties are disallowed by default
                    schema['additionalProperties'] = False

                if 'properties' not in schema or 'required' not in schema:
                    self.is_strict_compatible = False
                else:
                    required = schema['required']
                    for k in schema['properties'].keys():
                        if k not in required:
                            self.is_strict_compatible = False
        return schema
```