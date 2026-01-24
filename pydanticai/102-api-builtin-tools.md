---
title: pydantic_ai.builtin_tools - Pydantic AI
url: https://ai.pydantic.dev/api/builtin_tools/
source: sitemap
fetched_at: 2026-01-22T22:23:54.541229068-03:00
rendered_js: false
word_count: 1413
summary: This document defines the base classes and specific implementations for built-in tools in PydanticAI, such as web search capabilities and aspect ratio configurations.
tags:
    - pydantic-ai
    - builtin-tools
    - web-search
    - agent-framework
    - python-api
category: reference
---

### BUILTIN\_TOOL\_TYPES `module-attribute`

Registry of all builtin tool types, keyed by their kind string.

This dict is populated automatically via `__init_subclass__` when tool classes are defined.

### ImageAspectRatio `module-attribute`

```
ImageAspectRatio = Literal[
    "21:9",
    "16:9",
    "4:3",
    "3:2",
    "1:1",
    "9:16",
    "3:4",
    "2:3",
    "5:4",
    "4:5",
]
```

Supported aspect ratios for image generation tools.

### AbstractBuiltinTool `dataclass`

Bases: `ABC`

A builtin tool that can be used by an agent.

This class is abstract and cannot be instantiated directly.

The builtin tools are passed to the model as part of the `ModelRequestParameters`.

Source code in `pydantic_ai_slim/pydantic_ai/builtin_tools.py`

```
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
```

```
@dataclass(kw_only=True)
classAbstractBuiltinTool(ABC):
"""A builtin tool that can be used by an agent.

    This class is abstract and cannot be instantiated directly.

    The builtin tools are passed to the model as part of the `ModelRequestParameters`.
    """

    kind: str = 'unknown_builtin_tool'
"""Built-in tool identifier, this should be available on all built-in tools as a discriminator."""

    @property
    defunique_id(self) -> str:
"""A unique identifier for the builtin tool.

        If multiple instances of the same builtin tool can be passed to the model, subclasses should override this property to allow them to be distinguished.
        """
        return self.kind

    @property
    deflabel(self) -> str:
"""Human-readable label for UI display.

        Subclasses should override this to provide a meaningful label.
        """
        return self.kind.replace('_', ' ').title()

    def__init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        BUILTIN_TOOL_TYPES[cls.kind] = cls

    @classmethod
    def__get_pydantic_core_schema__(
        cls, _source_type: Any, handler: pydantic.GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        if cls is not AbstractBuiltinTool:
            return handler(cls)

        tools = BUILTIN_TOOL_TYPES.values()
        if len(tools) == 1:  # pragma: no cover
            tools_type = next(iter(tools))
        else:
            tools_annotated = [Annotated[tool, pydantic.Tag(tool.kind)] for tool in tools]
            tools_type = Annotated[Union[tuple(tools_annotated)], pydantic.Discriminator(_tool_discriminator)]  # noqa: UP007

        return handler(tools_type)
```

#### kind `class-attribute` `instance-attribute`

```
kind: str = 'unknown_builtin_tool'
```

Built-in tool identifier, this should be available on all built-in tools as a discriminator.

#### unique\_id `property`

A unique identifier for the builtin tool.

If multiple instances of the same builtin tool can be passed to the model, subclasses should override this property to allow them to be distinguished.

#### label `property`

Human-readable label for UI display.

Subclasses should override this to provide a meaningful label.

### WebSearchTool `dataclass`

Bases: `AbstractBuiltinTool`

A builtin tool that allows your agent to search the web for information.

The parameters that PydanticAI passes depend on the model, as some parameters may not be supported by certain models.

Supported by:

- Anthropic
- OpenAI Responses
- Groq
- Google
- xAI

Source code in `pydantic_ai_slim/pydantic_ai/builtin_tools.py`

```
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
```

```
@dataclass(kw_only=True)
classWebSearchTool(AbstractBuiltinTool):
"""A builtin tool that allows your agent to search the web for information.

    The parameters that PydanticAI passes depend on the model, as some parameters may not be supported by certain models.

    Supported by:

    * Anthropic
    * OpenAI Responses
    * Groq
    * Google
    * xAI
    """

    search_context_size: Literal['low', 'medium', 'high'] = 'medium'
"""The `search_context_size` parameter controls how much context is retrieved from the web to help the tool formulate a response.

    Supported by:

    * OpenAI Responses
    """

    user_location: WebSearchUserLocation | None = None
"""The `user_location` parameter allows you to localize search results based on a user's location.

    Supported by:

    * Anthropic
    * OpenAI Responses
    """

    blocked_domains: list[str] | None = None
"""If provided, these domains will never appear in results.

    With Anthropic, you can only use one of `blocked_domains` or `allowed_domains`, not both.

    Supported by:

    * Anthropic, see <https://docs.anthropic.com/en/docs/build-with-claude/tool-use/web-search-tool#domain-filtering>
    * Groq, see <https://console.groq.com/docs/agentic-tooling#search-settings>
    * xAI, see <https://docs.x.ai/docs/guides/tools/search-tools#web-search-parameters>
    """

    allowed_domains: list[str] | None = None
"""If provided, only these domains will be included in results.

    With Anthropic, you can only use one of `blocked_domains` or `allowed_domains`, not both.

    Supported by:

    * Anthropic, see <https://docs.anthropic.com/en/docs/build-with-claude/tool-use/web-search-tool#domain-filtering>
    * Groq, see <https://console.groq.com/docs/agentic-tooling#search-settings>
    * xAI, see <https://docs.x.ai/docs/guides/tools/search-tools#web-search-parameters>
    """

    max_uses: int | None = None
"""If provided, the tool will stop searching the web after the given number of uses.

    Supported by:

    * Anthropic
    """

    kind: str = 'web_search'
"""The kind of tool."""
```

#### search\_context\_size `class-attribute` `instance-attribute`

```
search_context_size: Literal["low", "medium", "high"] = (
    "medium"
)
```

The `search_context_size` parameter controls how much context is retrieved from the web to help the tool formulate a response.

Supported by:

- OpenAI Responses

#### user\_location `class-attribute` `instance-attribute`

```
user_location: WebSearchUserLocation | None = None
```

The `user_location` parameter allows you to localize search results based on a user's location.

Supported by:

- Anthropic
- OpenAI Responses

#### blocked\_domains `class-attribute` `instance-attribute`

```
blocked_domains: list[str] | None = None
```

#### allowed\_domains `class-attribute` `instance-attribute`

```
allowed_domains: list[str] | None = None
```

#### max\_uses `class-attribute` `instance-attribute`

```
max_uses: int | None = None
```

If provided, the tool will stop searching the web after the given number of uses.

Supported by:

- Anthropic

#### kind `class-attribute` `instance-attribute`

The kind of tool.

### WebSearchUserLocation

Bases: `TypedDict`

Allows you to localize search results based on a user's location.

Supported by:

- Anthropic
- OpenAI Responses

Source code in `pydantic_ai_slim/pydantic_ai/builtin_tools.py`

```
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
```

```
classWebSearchUserLocation(TypedDict, total=False):
"""Allows you to localize search results based on a user's location.

    Supported by:

    * Anthropic
    * OpenAI Responses
    """

    city: str
"""The city where the user is located."""

    country: str
"""The country where the user is located. For OpenAI, this must be a 2-letter country code (e.g., 'US', 'GB')."""

    region: str
"""The region or state where the user is located."""

    timezone: str
"""The timezone of the user's location."""
```

#### city `instance-attribute`

The city where the user is located.

#### country `instance-attribute`

The country where the user is located. For OpenAI, this must be a 2-letter country code (e.g., 'US', 'GB').

#### region `instance-attribute`

The region or state where the user is located.

#### timezone `instance-attribute`

The timezone of the user's location.

### CodeExecutionTool `dataclass`

Bases: `AbstractBuiltinTool`

A builtin tool that allows your agent to execute code.

Supported by:

- Anthropic
- OpenAI Responses
- Google
- Bedrock (Nova2.0)
- xAI

Source code in `pydantic_ai_slim/pydantic_ai/builtin_tools.py`

```
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
```

```
@dataclass(kw_only=True)
classCodeExecutionTool(AbstractBuiltinTool):
"""A builtin tool that allows your agent to execute code.

    Supported by:

    * Anthropic
    * OpenAI Responses
    * Google
    * Bedrock (Nova2.0)
    * xAI
    """

    kind: str = 'code_execution'
"""The kind of tool."""
```

#### kind `class-attribute` `instance-attribute`

```
kind: str = 'code_execution'
```

The kind of tool.

### WebFetchTool `dataclass`

Bases: `AbstractBuiltinTool`

Allows your agent to access contents from URLs.

The parameters that PydanticAI passes depend on the model, as some parameters may not be supported by certain models.

Supported by:

- Anthropic
- Google

Source code in `pydantic_ai_slim/pydantic_ai/builtin_tools.py`

```
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
```

```
@dataclass(kw_only=True)
classWebFetchTool(AbstractBuiltinTool):
"""Allows your agent to access contents from URLs.

    The parameters that PydanticAI passes depend on the model, as some parameters may not be supported by certain models.

    Supported by:

    * Anthropic
    * Google
    """

    max_uses: int | None = None
"""If provided, the tool will stop fetching URLs after the given number of uses.

    Supported by:

    * Anthropic
    """

    allowed_domains: list[str] | None = None
"""If provided, only these domains will be fetched.

    With Anthropic, you can only use one of `blocked_domains` or `allowed_domains`, not both.

    Supported by:

    * Anthropic, see <https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-fetch-tool#domain-filtering>
    """

    blocked_domains: list[str] | None = None
"""If provided, these domains will never be fetched.

    With Anthropic, you can only use one of `blocked_domains` or `allowed_domains`, not both.

    Supported by:

    * Anthropic, see <https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-fetch-tool#domain-filtering>
    """

    enable_citations: bool = False
"""If True, enables citations for fetched content.

    Supported by:

    * Anthropic
    """

    max_content_tokens: int | None = None
"""Maximum content length in tokens for fetched content.

    Supported by:

    * Anthropic
    """

    kind: str = 'web_fetch'
"""The kind of tool."""
```

#### max\_uses `class-attribute` `instance-attribute`

```
max_uses: int | None = None
```

If provided, the tool will stop fetching URLs after the given number of uses.

Supported by:

- Anthropic

#### enable\_citations `class-attribute` `instance-attribute`

```
enable_citations: bool = False
```

If True, enables citations for fetched content.

Supported by:

- Anthropic

#### max\_content\_tokens `class-attribute` `instance-attribute`

```
max_content_tokens: int | None = None
```

Maximum content length in tokens for fetched content.

Supported by:

- Anthropic

#### kind `class-attribute` `instance-attribute`

The kind of tool.

### UrlContextTool `dataclass` `deprecated`

Bases: `WebFetchTool`

Deprecated

Use `WebFetchTool` instead.

Deprecated alias for WebFetchTool. Use WebFetchTool instead.

Overrides kind to 'url\_context' so old serialized payloads with {"kind": "url\_context", ...} can be deserialized to UrlContextTool for backward compatibility.

Source code in `pydantic_ai_slim/pydantic_ai/builtin_tools.py`

```
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
```

```
@deprecated('Use `WebFetchTool` instead.')
@dataclass(kw_only=True)
classUrlContextTool(WebFetchTool):
"""Deprecated alias for WebFetchTool. Use WebFetchTool instead.

    Overrides kind to 'url_context' so old serialized payloads with {"kind": "url_context", ...}
    can be deserialized to UrlContextTool for backward compatibility.
    """

    kind: str = 'url_context'
"""The kind of tool (deprecated value for backward compatibility)."""
```

#### kind `class-attribute` `instance-attribute`

```
kind: str = 'url_context'
```

The kind of tool (deprecated value for backward compatibility).

### ImageGenerationTool `dataclass`

Bases: `AbstractBuiltinTool`

A builtin tool that allows your agent to generate images.

Supported by:

- OpenAI Responses
- Google

Source code in `pydantic_ai_slim/pydantic_ai/builtin_tools.py`

```
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
```

```
@dataclass(kw_only=True)
classImageGenerationTool(AbstractBuiltinTool):
"""A builtin tool that allows your agent to generate images.

    Supported by:

    * OpenAI Responses
    * Google
    """

    background: Literal['transparent', 'opaque', 'auto'] = 'auto'
"""Background type for the generated image.

    Supported by:

    * OpenAI Responses. 'transparent' is only supported for 'png' and 'webp' output formats.
    """

    input_fidelity: Literal['high', 'low'] | None = None
"""
    Control how much effort the model will exert to match the style and features,
    especially facial features, of input images.

    Supported by:

    * OpenAI Responses. Default: 'low'.
    """

    moderation: Literal['auto', 'low'] = 'auto'
"""Moderation level for the generated image.

    Supported by:

    * OpenAI Responses
    """

    output_compression: int | None = None
"""Compression level for the output image.

    Supported by:

    * OpenAI Responses. Only supported for 'jpeg' and 'webp' output formats. Default: 100.
    * Google (Vertex AI only). Only supported for 'jpeg' output format. Default: 75.
      Setting this will default `output_format` to 'jpeg' if not specified.
    """

    output_format: Literal['png', 'webp', 'jpeg'] | None = None
"""The output format of the generated image.

    Supported by:

    * OpenAI Responses. Default: 'png'.
    * Google (Vertex AI only). Default: 'png', or 'jpeg' if `output_compression` is set.
    """

    partial_images: int = 0
"""
    Number of partial images to generate in streaming mode.

    Supported by:

    * OpenAI Responses. Supports 0 to 3.
    """

    quality: Literal['low', 'medium', 'high', 'auto'] = 'auto'
"""The quality of the generated image.

    Supported by:

    * OpenAI Responses
    """

    size: Literal['auto', '1024x1024', '1024x1536', '1536x1024', '1K', '2K', '4K'] | None = None
"""The size of the generated image.

    * OpenAI Responses: 'auto' (default: model selects the size based on the prompt), '1024x1024', '1024x1536', '1536x1024'
    * Google (Gemini 3 Pro Image and later): '1K' (default), '2K', '4K'
    """

    aspect_ratio: ImageAspectRatio | None = None
"""The aspect ratio to use for generated images.

    Supported by:

    * Google image-generation models (Gemini)
    * OpenAI Responses (maps '1:1', '2:3', and '3:2' to supported sizes)
    """

    kind: str = 'image_generation'
"""The kind of tool."""
```

#### background `class-attribute` `instance-attribute`

```
background: Literal["transparent", "opaque", "auto"] = (
    "auto"
)
```

Background type for the generated image.

Supported by:

- OpenAI Responses. 'transparent' is only supported for 'png' and 'webp' output formats.

#### input\_fidelity `class-attribute` `instance-attribute`

```
input_fidelity: Literal['high', 'low'] | None = None
```

Control how much effort the model will exert to match the style and features, especially facial features, of input images.

Supported by:

- OpenAI Responses. Default: 'low'.

#### moderation `class-attribute` `instance-attribute`

```
moderation: Literal['auto', 'low'] = 'auto'
```

Moderation level for the generated image.

Supported by:

- OpenAI Responses

#### output\_compression `class-attribute` `instance-attribute`

```
output_compression: int | None = None
```

Compression level for the output image.

Supported by:

- OpenAI Responses. Only supported for 'jpeg' and 'webp' output formats. Default: 100.
- Google (Vertex AI only). Only supported for 'jpeg' output format. Default: 75. Setting this will default `output_format` to 'jpeg' if not specified.

#### output\_format `class-attribute` `instance-attribute`

```
output_format: Literal['png', 'webp', 'jpeg'] | None = None
```

The output format of the generated image.

Supported by:

- OpenAI Responses. Default: 'png'.
- Google (Vertex AI only). Default: 'png', or 'jpeg' if `output_compression` is set.

#### partial\_images `class-attribute` `instance-attribute`

Number of partial images to generate in streaming mode.

Supported by:

- OpenAI Responses. Supports 0 to 3.

#### quality `class-attribute` `instance-attribute`

```
quality: Literal['low', 'medium', 'high', 'auto'] = 'auto'
```

The quality of the generated image.

Supported by:

- OpenAI Responses

#### size `class-attribute` `instance-attribute`

```
size: (
    Literal[
        "auto",
        "1024x1024",
        "1024x1536",
        "1536x1024",
        "1K",
        "2K",
        "4K",
    ]
    | None
) = None
```

The size of the generated image.

- OpenAI Responses: 'auto' (default: model selects the size based on the prompt), '1024x1024', '1024x1536', '1536x1024'
- Google (Gemini 3 Pro Image and later): '1K' (default), '2K', '4K'

#### aspect\_ratio `class-attribute` `instance-attribute`

```
aspect_ratio: ImageAspectRatio | None = None
```

The aspect ratio to use for generated images.

Supported by:

- Google image-generation models (Gemini)
- OpenAI Responses (maps '1:1', '2:3', and '3:2' to supported sizes)

#### kind `class-attribute` `instance-attribute`

```
kind: str = 'image_generation'
```

The kind of tool.

### MemoryTool `dataclass`

Bases: `AbstractBuiltinTool`

A builtin tool that allows your agent to use memory.

Supported by:

- Anthropic

Source code in `pydantic_ai_slim/pydantic_ai/builtin_tools.py`

```
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
```

```
@dataclass(kw_only=True)
classMemoryTool(AbstractBuiltinTool):
"""A builtin tool that allows your agent to use memory.

    Supported by:

    * Anthropic
    """

    kind: str = 'memory'
"""The kind of tool."""
```

#### kind `class-attribute` `instance-attribute`

The kind of tool.

### MCPServerTool `dataclass`

Bases: `AbstractBuiltinTool`

A builtin tool that allows your agent to use MCP servers.

Supported by:

- OpenAI Responses
- Anthropic
- xAI

Source code in `pydantic_ai_slim/pydantic_ai/builtin_tools.py`

```
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
```

```
@dataclass(kw_only=True)
classMCPServerTool(AbstractBuiltinTool):
"""A builtin tool that allows your agent to use MCP servers.

    Supported by:

    * OpenAI Responses
    * Anthropic
    * xAI
    """

    id: str
"""A unique identifier for the MCP server."""

    url: str
"""The URL of the MCP server to use.

    For OpenAI Responses, it is possible to use `connector_id` by providing it as `x-openai-connector:<connector_id>`.
    """

    authorization_token: str | None = None
"""Authorization header to use when making requests to the MCP server.

    Supported by:

    * OpenAI Responses
    * Anthropic
    * xAI
    """

    description: str | None = None
"""A description of the MCP server.

    Supported by:

    * OpenAI Responses
    * xAI
    """

    allowed_tools: list[str] | None = None
"""A list of tools that the MCP server can use.

    Supported by:

    * OpenAI Responses
    * Anthropic
    * xAI
    """

    headers: dict[str, str] | None = None
"""Optional HTTP headers to send to the MCP server.

    Use for authentication or other purposes.

    Supported by:

    * OpenAI Responses
    * xAI
    """

    kind: str = 'mcp_server'

    @property
    defunique_id(self) -> str:
        return ':'.join([self.kind, self.id])

    @property
    deflabel(self) -> str:
        return f'MCP: {self.id}'
```

#### id `instance-attribute`

A unique identifier for the MCP server.

#### url `instance-attribute`

The URL of the MCP server to use.

For OpenAI Responses, it is possible to use `connector_id` by providing it as `x-openai-connector:<connector_id>`.

```
authorization_token: str | None = None
```

Authorization header to use when making requests to the MCP server.

Supported by:

- OpenAI Responses
- Anthropic
- xAI

#### description `class-attribute` `instance-attribute`

```
description: str | None = None
```

A description of the MCP server.

Supported by:

- OpenAI Responses
- xAI

#### allowed\_tools `class-attribute` `instance-attribute`

```
allowed_tools: list[str] | None = None
```

A list of tools that the MCP server can use.

Supported by:

- OpenAI Responses
- Anthropic
- xAI

Optional HTTP headers to send to the MCP server.

Use for authentication or other purposes.

Supported by:

- OpenAI Responses
- xAI

### FileSearchTool `dataclass`

Bases: `AbstractBuiltinTool`

A builtin tool that allows your agent to search through uploaded files using vector search.

This tool provides a fully managed Retrieval-Augmented Generation (RAG) system that handles file storage, chunking, embedding generation, and context injection into prompts.

Supported by:

- OpenAI Responses
- Google (Gemini)

Source code in `pydantic_ai_slim/pydantic_ai/builtin_tools.py`

```
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
```

```
@dataclass(kw_only=True)
classFileSearchTool(AbstractBuiltinTool):
"""A builtin tool that allows your agent to search through uploaded files using vector search.

    This tool provides a fully managed Retrieval-Augmented Generation (RAG) system that handles
    file storage, chunking, embedding generation, and context injection into prompts.

    Supported by:

    * OpenAI Responses
    * Google (Gemini)
    """

    file_store_ids: Sequence[str]
"""The file store IDs to search through.

    For OpenAI, these are the IDs of vector stores created via the OpenAI API.
    For Google, these are file search store names that have been uploaded and processed via the Gemini Files API.
    """

    kind: str = 'file_search'
"""The kind of tool."""
```

#### file\_store\_ids `instance-attribute`

The file store IDs to search through.

For OpenAI, these are the IDs of vector stores created via the OpenAI API. For Google, these are file search store names that have been uploaded and processed via the Gemini Files API.

#### kind `class-attribute` `instance-attribute`

```
kind: str = 'file_search'
```

The kind of tool.

### DEPRECATED\_BUILTIN\_TOOLS `module-attribute`

Set of deprecated builtin tool IDs that should not be offered in new UIs.

### SUPPORTED\_BUILTIN\_TOOLS `module-attribute`

```
SUPPORTED_BUILTIN_TOOLS = frozenset(
    cls
    for cls in (values())
    if cls not in DEPRECATED_BUILTIN_TOOLS
)
```

Get the set of all builtin tool types (excluding deprecated tools).