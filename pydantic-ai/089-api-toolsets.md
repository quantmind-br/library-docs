---
title: pydantic_ai.toolsets - Pydantic AI
url: https://ai.pydantic.dev/api/toolsets/
source: sitemap
fetched_at: 2026-01-22T22:24:19.039554155-03:00
rendered_js: false
word_count: 46
summary: This document defines the FunctionToolset class, which allows Python functions to be registered and managed as tools for AI agents with support for retries, timeouts, and automated schema generation.
tags:
    - pydantic-ai
    - function-tools
    - agent-framework
    - python-api
    - tool-management
    - json-schema
category: api
---

```
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
```

````
classFunctionToolset(AbstractToolset[AgentDepsT]):
"""A toolset that lets Python functions be used as tools.

    See [toolset docs](../toolsets.md#function-toolset) for more information.
    """

    tools: dict[str, Tool[Any]]
    max_retries: int
    timeout: float | None
    _id: str | None
    docstring_format: DocstringFormat
    require_parameter_descriptions: bool
    schema_generator: type[GenerateJsonSchema]

    def__init__(
        self,
        tools: Sequence[Tool[AgentDepsT] | ToolFuncEither[AgentDepsT, ...]] = [],
        *,
        max_retries: int = 1,
        timeout: float | None = None,
        docstring_format: DocstringFormat = 'auto',
        require_parameter_descriptions: bool = False,
        schema_generator: type[GenerateJsonSchema] = GenerateToolJsonSchema,
        strict: bool | None = None,
        sequential: bool = False,
        requires_approval: bool = False,
        metadata: dict[str, Any] | None = None,
        id: str | None = None,
    ):
"""Build a new function toolset.

        Args:
            tools: The tools to add to the toolset.
            max_retries: The maximum number of retries for each tool during a run.
                Applies to all tools, unless overridden when adding a tool.
            timeout: Timeout in seconds for tool execution. If a tool takes longer than this,
                a retry prompt is returned to the model. Individual tools can override this with their own timeout.
                Defaults to None (no timeout).
            docstring_format: Format of tool docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].
                Defaults to `'auto'`, such that the format is inferred from the structure of the docstring.
                Applies to all tools, unless overridden when adding a tool.
            require_parameter_descriptions: If True, raise an error if a parameter description is missing. Defaults to False.
                Applies to all tools, unless overridden when adding a tool.
            schema_generator: The JSON schema generator class to use for this tool. Defaults to `GenerateToolJsonSchema`.
                Applies to all tools, unless overridden when adding a tool.
            strict: Whether to enforce JSON schema compliance (only affects OpenAI).
                See [`ToolDefinition`][pydantic_ai.tools.ToolDefinition] for more info.
            sequential: Whether the function requires a sequential/serial execution environment. Defaults to False.
                Applies to all tools, unless overridden when adding a tool.
            requires_approval: Whether this tool requires human-in-the-loop approval. Defaults to False.
                See the [tools documentation](../deferred-tools.md#human-in-the-loop-tool-approval) for more info.
                Applies to all tools, unless overridden when adding a tool.
            metadata: Optional metadata for the tool. This is not sent to the model but can be used for filtering and tool behavior customization.
                Applies to all tools, unless overridden when adding a tool, which will be merged with the toolset's metadata.
            id: An optional unique ID for the toolset. A toolset needs to have an ID in order to be used in a durable execution environment like Temporal,
                in which case the ID will be used to identify the toolset's activities within the workflow.
        """
        self.max_retries = max_retries
        self.timeout = timeout
        self._id = id
        self.docstring_format = docstring_format
        self.require_parameter_descriptions = require_parameter_descriptions
        self.schema_generator = schema_generator
        self.strict = strict
        self.sequential = sequential
        self.requires_approval = requires_approval
        self.metadata = metadata

        self.tools = {}
        for tool in tools:
            if isinstance(tool, Tool):
                self.add_tool(tool)
            else:
                self.add_function(tool)

    @property
    defid(self) -> str | None:
        return self._id

    @overload
    deftool(self, func: ToolFuncEither[AgentDepsT, ToolParams], /) -> ToolFuncEither[AgentDepsT, ToolParams]: ...

    @overload
    deftool(
        self,
        /,
        *,
        name: str | None = None,
        description: str | None = None,
        retries: int | None = None,
        prepare: ToolPrepareFunc[AgentDepsT] | None = None,
        docstring_format: DocstringFormat | None = None,
        require_parameter_descriptions: bool | None = None,
        schema_generator: type[GenerateJsonSchema] | None = None,
        strict: bool | None = None,
        sequential: bool | None = None,
        requires_approval: bool | None = None,
        metadata: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> Callable[[ToolFuncEither[AgentDepsT, ToolParams]], ToolFuncEither[AgentDepsT, ToolParams]]: ...

    deftool(
        self,
        func: ToolFuncEither[AgentDepsT, ToolParams] | None = None,
        /,
        *,
        name: str | None = None,
        description: str | None = None,
        retries: int | None = None,
        prepare: ToolPrepareFunc[AgentDepsT] | None = None,
        docstring_format: DocstringFormat | None = None,
        require_parameter_descriptions: bool | None = None,
        schema_generator: type[GenerateJsonSchema] | None = None,
        strict: bool | None = None,
        sequential: bool | None = None,
        requires_approval: bool | None = None,
        metadata: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> Any:
"""Decorator to register a tool function which takes [`RunContext`][pydantic_ai.tools.RunContext] as its first argument.

        Can decorate a sync or async functions.

        The docstring is inspected to extract both the tool description and description of each parameter,
        [learn more](../tools.md#function-tools-and-schema).

        We can't add overloads for every possible signature of tool, since the return type is a recursive union
        so the signature of functions decorated with `@toolset.tool` is obscured.

        Example:
        ```python
        from pydantic_ai import Agent, FunctionToolset, RunContext

        toolset = FunctionToolset()

        @toolset.tool
        def foobar(ctx: RunContext[int], x: int) -> int:
            return ctx.deps + x

        @toolset.tool(retries=2)
        async def spam(ctx: RunContext[str], y: float) -> float:
            return ctx.deps + y

        agent = Agent('test', toolsets=[toolset], deps_type=int)
        result = agent.run_sync('foobar', deps=1)
        print(result.output)
        #> {"foobar":1,"spam":1.0}
        ```

        Args:
            func: The tool function to register.
            name: The name of the tool, defaults to the function name.
            description: The description of the tool,defaults to the function docstring.
            retries: The number of retries to allow for this tool, defaults to the agent's default retries,
                which defaults to 1.
            prepare: custom method to prepare the tool definition for each step, return `None` to omit this
                tool from a given step. This is useful if you want to customise a tool at call time,
                or omit it completely from a step. See [`ToolPrepareFunc`][pydantic_ai.tools.ToolPrepareFunc].
            docstring_format: The format of the docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].
                If `None`, the default value is determined by the toolset.
            require_parameter_descriptions: If True, raise an error if a parameter description is missing.
                If `None`, the default value is determined by the toolset.
            schema_generator: The JSON schema generator class to use for this tool.
                If `None`, the default value is determined by the toolset.
            strict: Whether to enforce JSON schema compliance (only affects OpenAI).
                See [`ToolDefinition`][pydantic_ai.tools.ToolDefinition] for more info.
                If `None`, the default value is determined by the toolset.
            sequential: Whether the function requires a sequential/serial execution environment. Defaults to False.
                If `None`, the default value is determined by the toolset.
            requires_approval: Whether this tool requires human-in-the-loop approval. Defaults to False.
                See the [tools documentation](../deferred-tools.md#human-in-the-loop-tool-approval) for more info.
                If `None`, the default value is determined by the toolset.
            metadata: Optional metadata for the tool. This is not sent to the model but can be used for filtering and tool behavior customization.
                If `None`, the default value is determined by the toolset. If provided, it will be merged with the toolset's metadata.
            timeout: Timeout in seconds for tool execution. If the tool takes longer, a retry prompt is returned to the model.
                Defaults to None (no timeout).
        """

        deftool_decorator(
            func_: ToolFuncEither[AgentDepsT, ToolParams],
        ) -> ToolFuncEither[AgentDepsT, ToolParams]:
            # noinspection PyTypeChecker
            self.add_function(
                func=func_,
                takes_ctx=None,
                name=name,
                description=description,
                retries=retries,
                prepare=prepare,
                docstring_format=docstring_format,
                require_parameter_descriptions=require_parameter_descriptions,
                schema_generator=schema_generator,
                strict=strict,
                sequential=sequential,
                requires_approval=requires_approval,
                metadata=metadata,
                timeout=timeout,
            )
            return func_

        return tool_decorator if func is None else tool_decorator(func)

    defadd_function(
        self,
        func: ToolFuncEither[AgentDepsT, ToolParams],
        takes_ctx: bool | None = None,
        name: str | None = None,
        description: str | None = None,
        retries: int | None = None,
        prepare: ToolPrepareFunc[AgentDepsT] | None = None,
        docstring_format: DocstringFormat | None = None,
        require_parameter_descriptions: bool | None = None,
        schema_generator: type[GenerateJsonSchema] | None = None,
        strict: bool | None = None,
        sequential: bool | None = None,
        requires_approval: bool | None = None,
        metadata: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> None:
"""Add a function as a tool to the toolset.

        Can take a sync or async function.

        The docstring is inspected to extract both the tool description and description of each parameter,
        [learn more](../tools.md#function-tools-and-schema).

        Args:
            func: The tool function to register.
            takes_ctx: Whether the function takes a [`RunContext`][pydantic_ai.tools.RunContext] as its first argument. If `None`, this is inferred from the function signature.
            name: The name of the tool, defaults to the function name.
            description: The description of the tool, defaults to the function docstring.
            retries: The number of retries to allow for this tool, defaults to the agent's default retries,
                which defaults to 1.
            prepare: custom method to prepare the tool definition for each step, return `None` to omit this
                tool from a given step. This is useful if you want to customise a tool at call time,
                or omit it completely from a step. See [`ToolPrepareFunc`][pydantic_ai.tools.ToolPrepareFunc].
            docstring_format: The format of the docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].
                If `None`, the default value is determined by the toolset.
            require_parameter_descriptions: If True, raise an error if a parameter description is missing.
                If `None`, the default value is determined by the toolset.
            schema_generator: The JSON schema generator class to use for this tool.
                If `None`, the default value is determined by the toolset.
            strict: Whether to enforce JSON schema compliance (only affects OpenAI).
                See [`ToolDefinition`][pydantic_ai.tools.ToolDefinition] for more info.
                If `None`, the default value is determined by the toolset.
            sequential: Whether the function requires a sequential/serial execution environment. Defaults to False.
                If `None`, the default value is determined by the toolset.
            requires_approval: Whether this tool requires human-in-the-loop approval. Defaults to False.
                See the [tools documentation](../deferred-tools.md#human-in-the-loop-tool-approval) for more info.
                If `None`, the default value is determined by the toolset.
            metadata: Optional metadata for the tool. This is not sent to the model but can be used for filtering and tool behavior customization.
                If `None`, the default value is determined by the toolset. If provided, it will be merged with the toolset's metadata.
            timeout: Timeout in seconds for tool execution. If the tool takes longer, a retry prompt is returned to the model.
                Defaults to None (no timeout).
        """
        if docstring_format is None:
            docstring_format = self.docstring_format
        if require_parameter_descriptions is None:
            require_parameter_descriptions = self.require_parameter_descriptions
        if schema_generator is None:
            schema_generator = self.schema_generator
        if strict is None:
            strict = self.strict
        if sequential is None:
            sequential = self.sequential
        if requires_approval is None:
            requires_approval = self.requires_approval

        tool = Tool[AgentDepsT](
            func,
            takes_ctx=takes_ctx,
            name=name,
            description=description,
            max_retries=retries,
            prepare=prepare,
            docstring_format=docstring_format,
            require_parameter_descriptions=require_parameter_descriptions,
            schema_generator=schema_generator,
            strict=strict,
            sequential=sequential,
            requires_approval=requires_approval,
            metadata=metadata,
            timeout=timeout,
        )
        self.add_tool(tool)

    defadd_tool(self, tool: Tool[AgentDepsT]) -> None:
"""Add a tool to the toolset.

        Args:
            tool: The tool to add.
        """
        if tool.name in self.tools:
            raise UserError(f'Tool name conflicts with existing tool: {tool.name!r}')
        if tool.max_retries is None:
            tool.max_retries = self.max_retries
        if self.metadata is not None:
            tool.metadata = self.metadata | (tool.metadata or {})
        self.tools[tool.name] = tool

    async defget_tools(self, ctx: RunContext[AgentDepsT]) -> dict[str, ToolsetTool[AgentDepsT]]:
        tools: dict[str, ToolsetTool[AgentDepsT]] = {}
        for original_name, tool in self.tools.items():
            max_retries = tool.max_retries if tool.max_retries is not None else self.max_retries
            run_context = replace(
                ctx,
                tool_name=original_name,
                retry=ctx.retries.get(original_name, 0),
                max_retries=max_retries,
            )
            tool_def = await tool.prepare_tool_def(run_context)
            if not tool_def:
                continue

            new_name = tool_def.name
            if new_name in tools:
                if new_name != original_name:
                    raise UserError(f'Renaming tool {original_name!r} to {new_name!r} conflicts with existing tool.')
                else:
                    raise UserError(f'Tool name conflicts with previously renamed tool: {new_name!r}.')

            tools[new_name] = FunctionToolsetTool(
                toolset=self,
                tool_def=tool_def,
                max_retries=max_retries,
                args_validator=tool.function_schema.validator,
                call_func=tool.function_schema.call,
                is_async=tool.function_schema.is_async,
                timeout=tool_def.timeout,
            )
        return tools

    async defcall_tool(
        self, name: str, tool_args: dict[str, Any], ctx: RunContext[AgentDepsT], tool: ToolsetTool[AgentDepsT]
    ) -> Any:
        assert isinstance(tool, FunctionToolsetTool)

        # Per-tool timeout takes precedence over toolset timeout
        timeout = tool.timeout if tool.timeout is not None else self.timeout
        if timeout is not None:
            try:
                with anyio.fail_after(timeout):
                    return await tool.call_func(tool_args, ctx)
            except TimeoutError:
                raise ModelRetry(f'Timed out after {timeout} seconds.') fromNone
        else:
            return await tool.call_func(tool_args, ctx)
````