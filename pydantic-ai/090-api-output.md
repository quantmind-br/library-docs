---
title: pydantic_ai.output - Pydantic AI
url: https://ai.pydantic.dev/api/output/
source: sitemap
fetched_at: 2026-01-22T22:24:07.152208801-03:00
rendered_js: false
word_count: 844
summary: Defines classes and type variables for controlling and customizing the structured output format of agent runs using tool-based or native model capabilities.
tags:
    - pydantic-ai
    - structured-outputs
    - llm-agents
    - python-api
    - data-validation
category: api
---

### OutputDataT `module-attribute`

```
OutputDataT = TypeVar(
    "OutputDataT", default=str, covariant=True
)
```

Covariant type variable for the output data type of a run.

### ToolOutput `dataclass`

Bases: `Generic[OutputDataT]`

Marker class to use a tool for output and optionally customize the tool.

Example:

tool\_output.py

```
frompydanticimport BaseModel

frompydantic_aiimport Agent, ToolOutput


classFruit(BaseModel):
    name: str
    color: str


classVehicle(BaseModel):
    name: str
    wheels: int


agent = Agent(
    'openai:gpt-4o',
    output_type=[
        ToolOutput(Fruit, name='return_fruit'),
        ToolOutput(Vehicle, name='return_vehicle'),
    ],
)
result = agent.run_sync('What is a banana?')
print(repr(result.output))
#> Fruit(name='banana', color='yellow')
```

Source code in `pydantic_ai_slim/pydantic_ai/output.py`

```
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
```

````
@dataclass(init=False)
classToolOutput(Generic[OutputDataT]):
"""Marker class to use a tool for output and optionally customize the tool.

    Example:
    ```python {title="tool_output.py"}
    from pydantic import BaseModel

    from pydantic_ai import Agent, ToolOutput


    class Fruit(BaseModel):
        name: str
        color: str


    class Vehicle(BaseModel):
        name: str
        wheels: int


    agent = Agent(
        'openai:gpt-4o',
        output_type=[
            ToolOutput(Fruit, name='return_fruit'),
            ToolOutput(Vehicle, name='return_vehicle'),
        ],
    )
    result = agent.run_sync('What is a banana?')
    print(repr(result.output))
    #> Fruit(name='banana', color='yellow')
    ```
    """

    output: OutputTypeOrFunction[OutputDataT]
"""An output type or function."""
    name: str | None
"""The name of the tool that will be passed to the model. If not specified and only one output is provided, `final_result` will be used. If multiple outputs are provided, the name of the output type or function will be added to the tool name."""
    description: str | None
"""The description of the tool that will be passed to the model. If not specified, the docstring of the output type or function will be used."""
    max_retries: int | None
"""The maximum number of retries for the tool."""
    strict: bool | None
"""Whether to use strict mode for the tool."""

    def__init__(
        self,
        type_: OutputTypeOrFunction[OutputDataT],
        *,
        name: str | None = None,
        description: str | None = None,
        max_retries: int | None = None,
        strict: bool | None = None,
    ):
        self.output = type_
        self.name = name
        self.description = description
        self.max_retries = max_retries
        self.strict = strict
````

#### output `instance-attribute`

```
output: OutputTypeOrFunction[OutputDataT] = type_
```

An output type or function.

#### name `instance-attribute`

The name of the tool that will be passed to the model. If not specified and only one output is provided, `final_result` will be used. If multiple outputs are provided, the name of the output type or function will be added to the tool name.

#### description `instance-attribute`

```
description: str | None = description
```

The description of the tool that will be passed to the model. If not specified, the docstring of the output type or function will be used.

#### max\_retries `instance-attribute`

```
max_retries: int | None = max_retries
```

The maximum number of retries for the tool.

#### strict `instance-attribute`

```
strict: bool | None = strict
```

Whether to use strict mode for the tool.

### NativeOutput `dataclass`

Bases: `Generic[OutputDataT]`

Marker class to use the model's native structured outputs functionality for outputs and optionally customize the name and description.

Example:

native\_output.py

```
frompydantic_aiimport Agent, NativeOutput

fromtool_outputimport Fruit, Vehicle

agent = Agent(
    'openai:gpt-4o',
    output_type=NativeOutput(
        [Fruit, Vehicle],
        name='Fruit or vehicle',
        description='Return a fruit or vehicle.'
    ),
)
result = agent.run_sync('What is a Ford Explorer?')
print(repr(result.output))
#> Vehicle(name='Ford Explorer', wheels=4)
```

Source code in `pydantic_ai_slim/pydantic_ai/output.py`

```
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
```

````
@dataclass(init=False)
classNativeOutput(Generic[OutputDataT]):
"""Marker class to use the model's native structured outputs functionality for outputs and optionally customize the name and description.

    Example:
    ```python {title="native_output.py" requires="tool_output.py"}
    from pydantic_ai import Agent, NativeOutput

    from tool_output import Fruit, Vehicle

    agent = Agent(
        'openai:gpt-4o',
        output_type=NativeOutput(
            [Fruit, Vehicle],
            name='Fruit or vehicle',
            description='Return a fruit or vehicle.'
        ),
    )
    result = agent.run_sync('What is a Ford Explorer?')
    print(repr(result.output))
    #> Vehicle(name='Ford Explorer', wheels=4)
    ```
    """

    outputs: OutputTypeOrFunction[OutputDataT] | Sequence[OutputTypeOrFunction[OutputDataT]]
"""The output types or functions."""
    name: str | None
"""The name of the structured output that will be passed to the model. If not specified and only one output is provided, the name of the output type or function will be used."""
    description: str | None
"""The description of the structured output that will be passed to the model. If not specified and only one output is provided, the docstring of the output type or function will be used."""
    strict: bool | None
"""Whether to use strict mode for the output, if the model supports it."""
    template: str | None
"""Template for the prompt passed to the model.
    The '{schema}' placeholder will be replaced with the output JSON schema.
    If no template is specified but the model's profile indicates that it requires the schema to be sent as a prompt, the default template specified on the profile will be used.
    """

    def__init__(
        self,
        outputs: OutputTypeOrFunction[OutputDataT] | Sequence[OutputTypeOrFunction[OutputDataT]],
        *,
        name: str | None = None,
        description: str | None = None,
        strict: bool | None = None,
        template: str | None = None,
    ):
        self.outputs = outputs
        self.name = name
        self.description = description
        self.strict = strict
        self.template = template
````

#### outputs `instance-attribute`

```
outputs: (
    OutputTypeOrFunction[OutputDataT]
    | Sequence[OutputTypeOrFunction[OutputDataT]]
) = outputs
```

The output types or functions.

#### name `instance-attribute`

The name of the structured output that will be passed to the model. If not specified and only one output is provided, the name of the output type or function will be used.

#### description `instance-attribute`

```
description: str | None = description
```

The description of the structured output that will be passed to the model. If not specified and only one output is provided, the docstring of the output type or function will be used.

#### strict `instance-attribute`

```
strict: bool | None = strict
```

Whether to use strict mode for the output, if the model supports it.

#### template `instance-attribute`

```
template: str | None = template
```

Template for the prompt passed to the model. The '{schema}' placeholder will be replaced with the output JSON schema. If no template is specified but the model's profile indicates that it requires the schema to be sent as a prompt, the default template specified on the profile will be used.

### PromptedOutput `dataclass`

Bases: `Generic[OutputDataT]`

Marker class to use a prompt to tell the model what to output and optionally customize the prompt.

Example:

prompted\_output.py

```
frompydanticimport BaseModel

frompydantic_aiimport Agent, PromptedOutput

fromtool_outputimport Vehicle


classDevice(BaseModel):
    name: str
    kind: str


agent = Agent(
    'openai:gpt-4o',
    output_type=PromptedOutput(
        [Vehicle, Device],
        name='Vehicle or device',
        description='Return a vehicle or device.'
    ),
)
result = agent.run_sync('What is a MacBook?')
print(repr(result.output))
#> Device(name='MacBook', kind='laptop')

agent = Agent(
    'openai:gpt-4o',
    output_type=PromptedOutput(
        [Vehicle, Device],
        template='Gimme some JSON: {schema}'
    ),
)
result = agent.run_sync('What is a Ford Explorer?')
print(repr(result.output))
#> Vehicle(name='Ford Explorer', wheels=4)
```

Source code in `pydantic_ai_slim/pydantic_ai/output.py`

```
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
```

````
@dataclass(init=False)
classPromptedOutput(Generic[OutputDataT]):
"""Marker class to use a prompt to tell the model what to output and optionally customize the prompt.

    Example:
    ```python {title="prompted_output.py" requires="tool_output.py"}
    from pydantic import BaseModel

    from pydantic_ai import Agent, PromptedOutput

    from tool_output import Vehicle


    class Device(BaseModel):
        name: str
        kind: str


    agent = Agent(
        'openai:gpt-4o',
        output_type=PromptedOutput(
            [Vehicle, Device],
            name='Vehicle or device',
            description='Return a vehicle or device.'
        ),
    )
    result = agent.run_sync('What is a MacBook?')
    print(repr(result.output))
    #> Device(name='MacBook', kind='laptop')

    agent = Agent(
        'openai:gpt-4o',
        output_type=PromptedOutput(
            [Vehicle, Device],
            template='Gimme some JSON: {schema}'
        ),
    )
    result = agent.run_sync('What is a Ford Explorer?')
    print(repr(result.output))
    #> Vehicle(name='Ford Explorer', wheels=4)
    ```
    """

    outputs: OutputTypeOrFunction[OutputDataT] | Sequence[OutputTypeOrFunction[OutputDataT]]
"""The output types or functions."""
    name: str | None
"""The name of the structured output that will be passed to the model. If not specified and only one output is provided, the name of the output type or function will be used."""
    description: str | None
"""The description that will be passed to the model. If not specified and only one output is provided, the docstring of the output type or function will be used."""
    template: str | None
"""Template for the prompt passed to the model.
    The '{schema}' placeholder will be replaced with the output JSON schema.
    If not specified, the default template specified on the model's profile will be used.
    """

    def__init__(
        self,
        outputs: OutputTypeOrFunction[OutputDataT] | Sequence[OutputTypeOrFunction[OutputDataT]],
        *,
        name: str | None = None,
        description: str | None = None,
        template: str | None = None,
    ):
        self.outputs = outputs
        self.name = name
        self.description = description
        self.template = template
````

#### outputs `instance-attribute`

```
outputs: (
    OutputTypeOrFunction[OutputDataT]
    | Sequence[OutputTypeOrFunction[OutputDataT]]
) = outputs
```

The output types or functions.

#### name `instance-attribute`

The name of the structured output that will be passed to the model. If not specified and only one output is provided, the name of the output type or function will be used.

#### description `instance-attribute`

```
description: str | None = description
```

The description that will be passed to the model. If not specified and only one output is provided, the docstring of the output type or function will be used.

#### template `instance-attribute`

```
template: str | None = template
```

Template for the prompt passed to the model. The '{schema}' placeholder will be replaced with the output JSON schema. If not specified, the default template specified on the model's profile will be used.

### TextOutput `dataclass`

Bases: `Generic[OutputDataT]`

Marker class to use text output for an output function taking a string argument.

Example:

```
frompydantic_aiimport Agent, TextOutput


defsplit_into_words(text: str) -> list[str]:
    return text.split()


agent = Agent(
    'openai:gpt-4o',
    output_type=TextOutput(split_into_words),
)
result = agent.run_sync('Who was Albert Einstein?')
print(result.output)
#> ['Albert', 'Einstein', 'was', 'a', 'German-born', 'theoretical', 'physicist.']
```

Source code in `pydantic_ai_slim/pydantic_ai/output.py`

```
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
```

````
@dataclass
classTextOutput(Generic[OutputDataT]):
"""Marker class to use text output for an output function taking a string argument.

    Example:
    ```python
    from pydantic_ai import Agent, TextOutput


    def split_into_words(text: str) -> list[str]:
        return text.split()


    agent = Agent(
        'openai:gpt-4o',
        output_type=TextOutput(split_into_words),
    )
    result = agent.run_sync('Who was Albert Einstein?')
    print(result.output)
    #> ['Albert', 'Einstein', 'was', 'a', 'German-born', 'theoretical', 'physicist.']
    ```
    """

    output_function: TextOutputFunc[OutputDataT]
"""The function that will be called to process the model's plain text output. The function must take a single string argument."""
````

#### output\_function `instance-attribute`

```
output_function: TextOutputFunc[OutputDataT]
```

The function that will be called to process the model's plain text output. The function must take a single string argument.

### StructuredDict

Returns a `dict[str, Any]` subclass with a JSON schema attached that will be used for structured output.

Parameters:

Name Type Description Default `json_schema` `JsonSchemaValue`

A JSON schema of type `object` defining the structure of the dictionary content.

*required* `name` `str | None`

Optional name of the structured output. If not provided, the `title` field of the JSON schema will be used if it's present.

`None` `description` `str | None`

Optional description of the structured output. If not provided, the `description` field of the JSON schema will be used if it's present.

`None`

Example:

structured\_dict.py

```
frompydantic_aiimport Agent, StructuredDict

schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'age': {'type': 'integer'}
    },
    'required': ['name', 'age']
}

agent = Agent('openai:gpt-4o', output_type=StructuredDict(schema))
result = agent.run_sync('Create a person')
print(result.output)
#> {'name': 'John Doe', 'age': 30}
```

Source code in `pydantic_ai_slim/pydantic_ai/output.py`

```
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
```

````
defStructuredDict(
    json_schema: JsonSchemaValue, name: str | None = None, description: str | None = None
) -> type[JsonSchemaValue]:
"""Returns a `dict[str, Any]` subclass with a JSON schema attached that will be used for structured output.

    Args:
        json_schema: A JSON schema of type `object` defining the structure of the dictionary content.
        name: Optional name of the structured output. If not provided, the `title` field of the JSON schema will be used if it's present.
        description: Optional description of the structured output. If not provided, the `description` field of the JSON schema will be used if it's present.

    Example:
    ```python {title="structured_dict.py"}
    from pydantic_ai import Agent, StructuredDict

    schema = {
        'type': 'object',
        'properties': {
            'name': {'type': 'string'},
            'age': {'type': 'integer'}
        },
        'required': ['name', 'age']
    }

    agent = Agent('openai:gpt-4o', output_type=StructuredDict(schema))
    result = agent.run_sync('Create a person')
    print(result.output)
    #> {'name': 'John Doe', 'age': 30}
    ```
    """
    json_schema = _utils.check_object_json_schema(json_schema)

    # Pydantic `TypeAdapter` fails when `object.__get_pydantic_json_schema__` has `$defs`, so we inline them
    # See https://github.com/pydantic/pydantic/issues/12145
    if '$defs' in json_schema:
        json_schema = InlineDefsJsonSchemaTransformer(json_schema).walk()
        if '$defs' in json_schema:
            raise exceptions.UserError(
                '`StructuredDict` does not currently support recursive `$ref`s and `$defs`. See https://github.com/pydantic/pydantic/issues/12145 for more information.'
            )

    if name:
        json_schema['title'] = name

    if description:
        json_schema['description'] = description

    class_StructuredDict(JsonSchemaValue):
        __is_model_like__ = True

        @classmethod
        def__get_pydantic_core_schema__(
            cls, source_type: Any, handler: GetCoreSchemaHandler
        ) -> core_schema.CoreSchema:
            return core_schema.dict_schema(
                keys_schema=core_schema.str_schema(),
                values_schema=core_schema.any_schema(),
            )

        @classmethod
        def__get_pydantic_json_schema__(
            cls, core_schema: core_schema.CoreSchema, handler: GetJsonSchemaHandler
        ) -> JsonSchemaValue:
            return json_schema

    return _StructuredDict
````

### DeferredToolRequests `dataclass`

Tool calls that require approval or external execution.

This can be used as an agent's `output_type` and will be used as the output of the agent run if the model called any deferred tools.

Results can be passed to the next agent run using a [`DeferredToolResults`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DeferredToolResults "DeferredToolResults            dataclass   ") object with the same tool call IDs.

See [deferred tools docs](https://ai.pydantic.dev/deferred-tools/#deferred-tools) for more information.

Source code in `pydantic_ai_slim/pydantic_ai/tools.py`

```
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
```

```
@dataclass(kw_only=True)
classDeferredToolRequests:
"""Tool calls that require approval or external execution.

    This can be used as an agent's `output_type` and will be used as the output of the agent run if the model called any deferred tools.

    Results can be passed to the next agent run using a [`DeferredToolResults`][pydantic_ai.tools.DeferredToolResults] object with the same tool call IDs.

    See [deferred tools docs](../deferred-tools.md#deferred-tools) for more information.
    """

    calls: list[ToolCallPart] = field(default_factory=list)
"""Tool calls that require external execution."""
    approvals: list[ToolCallPart] = field(default_factory=list)
"""Tool calls that require human-in-the-loop approval."""
    metadata: dict[str, dict[str, Any]] = field(default_factory=dict)
"""Metadata for deferred tool calls, keyed by `tool_call_id`."""
```

#### calls `class-attribute` `instance-attribute`

Tool calls that require external execution.

#### approvals `class-attribute` `instance-attribute`

Tool calls that require human-in-the-loop approval.

#### metadata `class-attribute` `instance-attribute`

Metadata for deferred tool calls, keyed by `tool_call_id`.