---
title: pydantic_ai.exceptions - Pydantic AI
url: https://ai.pydantic.dev/api/exceptions/
source: sitemap
fetched_at: 2026-01-22T22:24:00.860452845-03:00
rendered_js: false
word_count: 512
summary: This document defines the custom exception classes used in the Pydantic AI framework to manage tool retries, deferred calls, human-in-the-loop approvals, and runtime errors.
tags:
    - pydantic-ai
    - error-handling
    - exceptions
    - tool-calling
    - python-api
    - agent-framework
category: reference
---

### ModelRetry

Bases: `Exception`

Exception to raise when a tool function should be retried.

The agent will return the message to the model and ask it to try calling the function/tool again.

Source code in `pydantic_ai_slim/pydantic_ai/exceptions.py`

```
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
```

```
classModelRetry(Exception):
"""Exception to raise when a tool function should be retried.

    The agent will return the message to the model and ask it to try calling the function/tool again.
    """

    message: str
"""The message to return to the model."""

    def__init__(self, message: str):
        self.message = message
        super().__init__(message)

    def__eq__(self, other: Any) -> bool:
        return isinstance(other, self.__class__) and other.message == self.message

    def__hash__(self) -> int:
        return hash((self.__class__, self.message))

    @classmethod
    def__get_pydantic_core_schema__(cls, _: Any, __: Any) -> core_schema.CoreSchema:
"""Pydantic core schema to allow `ModelRetry` to be (de)serialized."""
        schema = core_schema.typed_dict_schema(
            {
                'message': core_schema.typed_dict_field(core_schema.str_schema()),
                'kind': core_schema.typed_dict_field(core_schema.literal_schema(['model-retry'])),
            }
        )
        return core_schema.no_info_after_validator_function(
            lambda dct: ModelRetry(dct['message']),
            schema,
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda x: {'message': x.message, 'kind': 'model-retry'},
                return_schema=schema,
            ),
        )
```

#### message `instance-attribute`

The message to return to the model.

#### \_\_get\_pydantic\_core\_schema\__ `classmethod`

```
__get_pydantic_core_schema__(_: Any, __: Any) -> CoreSchema
```

Pydantic core schema to allow `ModelRetry` to be (de)serialized.

Source code in `pydantic_ai_slim/pydantic_ai/exceptions.py`

```
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
```

```
@classmethod
def__get_pydantic_core_schema__(cls, _: Any, __: Any) -> core_schema.CoreSchema:
"""Pydantic core schema to allow `ModelRetry` to be (de)serialized."""
    schema = core_schema.typed_dict_schema(
        {
            'message': core_schema.typed_dict_field(core_schema.str_schema()),
            'kind': core_schema.typed_dict_field(core_schema.literal_schema(['model-retry'])),
        }
    )
    return core_schema.no_info_after_validator_function(
        lambda dct: ModelRetry(dct['message']),
        schema,
        serialization=core_schema.plain_serializer_function_ser_schema(
            lambda x: {'message': x.message, 'kind': 'model-retry'},
            return_schema=schema,
        ),
    )
```

### CallDeferred

Bases: `Exception`

Exception to raise when a tool call should be deferred.

See [tools docs](https://ai.pydantic.dev/deferred-tools/#deferred-tools) for more information.

Parameters:

Name Type Description Default `metadata` `dict[str, Any] | None`

Optional dictionary of metadata to attach to the deferred tool call. This metadata will be available in `DeferredToolRequests.metadata` keyed by `tool_call_id`.

`None`

Source code in `pydantic_ai_slim/pydantic_ai/exceptions.py`

```
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
```

```
classCallDeferred(Exception):
"""Exception to raise when a tool call should be deferred.

    See [tools docs](../deferred-tools.md#deferred-tools) for more information.

    Args:
        metadata: Optional dictionary of metadata to attach to the deferred tool call.
            This metadata will be available in `DeferredToolRequests.metadata` keyed by `tool_call_id`.
    """

    def__init__(self, metadata: dict[str, Any] | None = None):
        self.metadata = metadata
        super().__init__()
```

### ApprovalRequired

Bases: `Exception`

Exception to raise when a tool call requires human-in-the-loop approval.

See [tools docs](https://ai.pydantic.dev/deferred-tools/#human-in-the-loop-tool-approval) for more information.

Parameters:

Name Type Description Default `metadata` `dict[str, Any] | None`

Optional dictionary of metadata to attach to the deferred tool call. This metadata will be available in `DeferredToolRequests.metadata` keyed by `tool_call_id`.

`None`

Source code in `pydantic_ai_slim/pydantic_ai/exceptions.py`

```
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
```

```
classApprovalRequired(Exception):
"""Exception to raise when a tool call requires human-in-the-loop approval.

    See [tools docs](../deferred-tools.md#human-in-the-loop-tool-approval) for more information.

    Args:
        metadata: Optional dictionary of metadata to attach to the deferred tool call.
            This metadata will be available in `DeferredToolRequests.metadata` keyed by `tool_call_id`.
    """

    def__init__(self, metadata: dict[str, Any] | None = None):
        self.metadata = metadata
        super().__init__()
```

### UserError

Bases: `RuntimeError`

Error caused by a usage mistake by the application developer — You!

Source code in `pydantic_ai_slim/pydantic_ai/exceptions.py`

```
103
104
105
106
107
108
109
110
111
```

```
classUserError(RuntimeError):
"""Error caused by a usage mistake by the application developer — You!"""

    message: str
"""Description of the mistake."""

    def__init__(self, message: str):
        self.message = message
        super().__init__(message)
```

#### message `instance-attribute`

Description of the mistake.

### AgentRunError

Bases: `RuntimeError`

Base class for errors occurring during an agent run.

Source code in `pydantic_ai_slim/pydantic_ai/exceptions.py`

```
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
```

```
classAgentRunError(RuntimeError):
"""Base class for errors occurring during an agent run."""

    message: str
"""The error message."""

    def__init__(self, message: str):
        self.message = message
        super().__init__(message)

    def__str__(self) -> str:
        return self.message
```

#### message `instance-attribute`

The error message.

### UsageLimitExceeded

Bases: `AgentRunError`

Error raised when a Model's usage exceeds the specified limits.

Source code in `pydantic_ai_slim/pydantic_ai/exceptions.py`

```
classUsageLimitExceeded(AgentRunError):
"""Error raised when a Model's usage exceeds the specified limits."""
```

### UnexpectedModelBehavior

Bases: `AgentRunError`

Error caused by unexpected Model behavior, e.g. an unexpected response code.

Source code in `pydantic_ai_slim/pydantic_ai/exceptions.py`

```
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
```

```
classUnexpectedModelBehavior(AgentRunError):
"""Error caused by unexpected Model behavior, e.g. an unexpected response code."""

    message: str
"""Description of the unexpected behavior."""
    body: str | None
"""The body of the response, if available."""

    def__init__(self, message: str, body: str | None = None):
        self.message = message
        if body is None:
            self.body: str | None = None
        else:
            try:
                self.body = json.dumps(json.loads(body), indent=2)
            except ValueError:
                self.body = body
        super().__init__(message)

    def__str__(self) -> str:
        if self.body:
            return f'{self.message}, body:\n{self.body}'
        else:
            return self.message
```

#### message `instance-attribute`

Description of the unexpected behavior.

#### body `instance-attribute`

The body of the response, if available.

### ContentFilterError

Bases: `UnexpectedModelBehavior`

Raised when content filtering is triggered by the model provider resulting in an empty response.

Source code in `pydantic_ai_slim/pydantic_ai/exceptions.py`

```
classContentFilterError(UnexpectedModelBehavior):
"""Raised when content filtering is triggered by the model provider resulting in an empty response."""
```

### ModelAPIError

Bases: `AgentRunError`

Raised when a model provider API request fails.

Source code in `pydantic_ai_slim/pydantic_ai/exceptions.py`

```
162
163
164
165
166
167
168
169
170
```

```
classModelAPIError(AgentRunError):
"""Raised when a model provider API request fails."""

    model_name: str
"""The name of the model associated with the error."""

    def__init__(self, model_name: str, message: str):
        self.model_name = model_name
        super().__init__(message)
```

#### model\_name `instance-attribute`

```
model_name: str = model_name
```

The name of the model associated with the error.

### ModelHTTPError

Bases: `ModelAPIError`

Raised when an model provider response has a status code of 4xx or 5xx.

Source code in `pydantic_ai_slim/pydantic_ai/exceptions.py`

```
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
```

```
classModelHTTPError(ModelAPIError):
"""Raised when an model provider response has a status code of 4xx or 5xx."""

    status_code: int
"""The HTTP status code returned by the API."""

    body: object | None
"""The body of the response, if available."""

    def__init__(self, status_code: int, model_name: str, body: object | None = None):
        self.status_code = status_code
        self.body = body
        message = f'status_code: {status_code}, model_name: {model_name}, body: {body}'
        super().__init__(model_name=model_name, message=message)
```

#### status\_code `instance-attribute`

```
status_code: int = status_code
```

The HTTP status code returned by the API.

#### body `instance-attribute`

The body of the response, if available.

### FallbackExceptionGroup

Bases: `ExceptionGroup[Any]`

A group of exceptions that can be raised when all fallback models fail.

Source code in `pydantic_ai_slim/pydantic_ai/exceptions.py`

```
classFallbackExceptionGroup(ExceptionGroup[Any]):
"""A group of exceptions that can be raised when all fallback models fail."""
```

### ToolRetryError

Bases: `Exception`

Exception used to signal a `ToolRetry` message should be returned to the LLM.

Source code in `pydantic_ai_slim/pydantic_ai/exceptions.py`

```
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
```

```
classToolRetryError(Exception):
"""Exception used to signal a `ToolRetry` message should be returned to the LLM."""

    def__init__(self, tool_retry: RetryPromptPart):
        self.tool_retry = tool_retry
        message = (
            tool_retry.content
            if isinstance(tool_retry.content, str)
            else self._format_error_details(tool_retry.content, tool_retry.tool_name)
        )
        super().__init__(message)

    @staticmethod
    def_format_error_details(errors: list[pydantic_core.ErrorDetails], tool_name: str | None) -> str:
"""Format ErrorDetails as a human-readable message.

        We format manually rather than using ValidationError.from_exception_data because
        some error types (value_error, assertion_error, etc.) require an 'error' key in ctx,
        but when ErrorDetails are serialized, exception objects are stripped from ctx.
        The 'msg' field already contains the human-readable message, so we use that directly.
        """
        error_count = len(errors)
        lines = [
            f'{error_count} validation error{""iferror_count==1else"s"}{f" for {tool_name!r}"iftool_nameelse""}'
        ]
        for e in errors:
            loc = '.'.join(str(x) for x in e['loc']) if e['loc'] else '__root__'
            lines.append(loc)
            lines.append(f'  {e["msg"]} [type={e["type"]}, input_value={e["input"]!r}]')
        return '\n'.join(lines)
```

### IncompleteToolCall

Bases: `UnexpectedModelBehavior`

Error raised when a model stops due to token limit while emitting a tool call.

Source code in `pydantic_ai_slim/pydantic_ai/exceptions.py`

```
classIncompleteToolCall(UnexpectedModelBehavior):
"""Error raised when a model stops due to token limit while emitting a tool call."""
```