---
title: protocol - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/anthropic/protocol/
source: sitemap
fetched_at: 2026-05-07T21:19:17.88615233-03:00
rendered_js: false
word_count: 171
summary: Defines the Pydantic data models and request/response structures required to implement the Anthropic API protocol within the vLLM serving framework.
tags:
    - vllm
    - anthropic-api
    - pydantic
    - data-models
    - protocol-specification
    - message-schema
category: reference
---

## vllm.entrypoints.anthropic.protocol [¶](#vllm.entrypoints.anthropic.protocol "Permanent link")

Pydantic models for Anthropic API protocol

## AnthropicContentBlock [¶](#vllm.entrypoints.anthropic.protocol.AnthropicContentBlock "Permanent link")

Bases: `BaseModel`

Content block in message

Source code in `vllm/entrypoints/anthropic/protocol.py`

```
classAnthropicContentBlock(BaseModel):
"""Content block in message"""

    type: Literal[
        "text",
        "image",
        "tool_use",
        "tool_result",
        "tool_reference",
        "thinking",
        "redacted_thinking",
    ]
    text: str | None = None
    # For image content
    source: dict[str, Any] | None = None
    # For tool use/result
    id: str | None = None
    tool_use_id: str | None = None
    name: str | None = None
    input: dict[str, Any] | None = None
    content: str | list[dict[str, Any]] | None = None
    is_error: bool | None = None
    # For tool_reference content
    tool_name: str | None = None
    # For thinking content
    thinking: str | None = None
    signature: str | None = None
    # For redacted thinking content (safety-filtered by the API)
    data: str | None = None
```

## AnthropicContextManagement [¶](#vllm.entrypoints.anthropic.protocol.AnthropicContextManagement "Permanent link")

Bases: `BaseModel`

Context management information for token counting.

Source code in `vllm/entrypoints/anthropic/protocol.py`

```
classAnthropicContextManagement(BaseModel):
"""Context management information for token counting."""

    original_input_tokens: int
```

## AnthropicCountTokensRequest [¶](#vllm.entrypoints.anthropic.protocol.AnthropicCountTokensRequest "Permanent link")

Bases: `BaseModel`

Anthropic messages.count\_tokens request

Source code in `vllm/entrypoints/anthropic/protocol.py`

```
classAnthropicCountTokensRequest(BaseModel):
"""Anthropic messages.count_tokens request"""

    model: str
    messages: list[AnthropicMessage]
    system: str | list[AnthropicContentBlock] | None = None
    tool_choice: AnthropicToolChoice | None = None
    tools: list[AnthropicTool] | None = None

    # vLLM-specific fields that are not in Anthropic spec
    chat_template_kwargs: dict[str, Any] | None = Field(
        default=None,
        description=(
            "Additional keyword args to pass to the chat template renderer. "
            "Will be accessible by the template."
        ),
    )

    @field_validator("model")
    @classmethod
    defvalidate_model(cls, v):
        if not v:
            raise ValueError("Model is required")
        return v
```

## AnthropicCountTokensResponse [¶](#vllm.entrypoints.anthropic.protocol.AnthropicCountTokensResponse "Permanent link")

Bases: `BaseModel`

Anthropic messages.count\_tokens response

Source code in `vllm/entrypoints/anthropic/protocol.py`

```
classAnthropicCountTokensResponse(BaseModel):
"""Anthropic messages.count_tokens response"""

    input_tokens: int
    context_management: AnthropicContextManagement | None = None
```

## AnthropicDelta [¶](#vllm.entrypoints.anthropic.protocol.AnthropicDelta "Permanent link")

Bases: `BaseModel`

Delta for streaming responses

Source code in `vllm/entrypoints/anthropic/protocol.py`

```
classAnthropicDelta(BaseModel):
"""Delta for streaming responses"""

    type: (
        Literal["text_delta", "input_json_delta", "thinking_delta", "signature_delta"]
        | None
    ) = None
    text: str | None = None
    thinking: str | None = None
    partial_json: str | None = None
    signature: str | None = None

    # Message delta
    stop_reason: (
        Literal["end_turn", "max_tokens", "stop_sequence", "tool_use"] | None
    ) = None
    stop_sequence: str | None = None
```

## AnthropicError [¶](#vllm.entrypoints.anthropic.protocol.AnthropicError "Permanent link")

Bases: `BaseModel`

Error structure for Anthropic API

Source code in `vllm/entrypoints/anthropic/protocol.py`

```
classAnthropicError(BaseModel):
"""Error structure for Anthropic API"""

    type: str
    message: str
```

## AnthropicErrorResponse [¶](#vllm.entrypoints.anthropic.protocol.AnthropicErrorResponse "Permanent link")

Bases: `BaseModel`

Error response structure for Anthropic API

Source code in `vllm/entrypoints/anthropic/protocol.py`

```
classAnthropicErrorResponse(BaseModel):
"""Error response structure for Anthropic API"""

    type: Literal["error"] = "error"
    error: AnthropicError
```

## AnthropicMessage [¶](#vllm.entrypoints.anthropic.protocol.AnthropicMessage "Permanent link")

Bases: `BaseModel`

Message structure

Source code in `vllm/entrypoints/anthropic/protocol.py`

```
classAnthropicMessage(BaseModel):
"""Message structure"""

    role: Literal["user", "assistant"]
    content: str | list[AnthropicContentBlock]
```

## AnthropicMessagesRequest [¶](#vllm.entrypoints.anthropic.protocol.AnthropicMessagesRequest "Permanent link")

Bases: `BaseModel`

Anthropic Messages API request

Source code in `vllm/entrypoints/anthropic/protocol.py`

```
classAnthropicMessagesRequest(BaseModel):
"""Anthropic Messages API request"""

    model: str
    messages: list[AnthropicMessage]
    max_tokens: int
    metadata: dict[str, Any] | None = None
    stop_sequences: list[str] | None = None
    stream: bool | None = False
    system: str | list[AnthropicContentBlock] | None = None
    temperature: float | None = None
    tool_choice: AnthropicToolChoice | None = None
    tools: list[AnthropicTool] | None = None
    top_k: int | None = None
    top_p: float | None = None

    # vLLM-specific fields that are not in Anthropic spec
    kv_transfer_params: dict[str, Any] | None = Field(
        default=None,
        description="KVTransfer parameters used for disaggregated serving.",
    )
    chat_template_kwargs: dict[str, Any] | None = Field(
        default=None,
        description=(
            "Additional keyword args to pass to the chat template renderer. "
            "Will be accessible by the template."
        ),
    )

    @field_validator("model")
    @classmethod
    defvalidate_model(cls, v):
        if not v:
            raise ValueError("Model is required")
        return v

    @field_validator("max_tokens")
    @classmethod
    defvalidate_max_tokens(cls, v):
        if v <= 0:
            raise ValueError("max_tokens must be positive")
        return v
```

## AnthropicMessagesResponse [¶](#vllm.entrypoints.anthropic.protocol.AnthropicMessagesResponse "Permanent link")

Bases: `BaseModel`

Anthropic Messages API response

Source code in `vllm/entrypoints/anthropic/protocol.py`

```
classAnthropicMessagesResponse(BaseModel):
"""Anthropic Messages API response"""

    id: str
    type: Literal["message"] = "message"
    role: Literal["assistant"] = "assistant"
    content: list[AnthropicContentBlock]
    model: str
    stop_reason: (
        Literal["end_turn", "max_tokens", "stop_sequence", "tool_use"] | None
    ) = None
    stop_sequence: str | None = None
    usage: AnthropicUsage | None = None

    # vLLM-specific fields that are not in Anthropic spec
    kv_transfer_params: dict[str, Any] | None = Field(
        default=None, description="KVTransfer parameters."
    )

    defmodel_post_init(self, __context):
        if not self.id:
            self.id = f"msg_{int(time.time()*1000)}"
```

## AnthropicStreamEvent [¶](#vllm.entrypoints.anthropic.protocol.AnthropicStreamEvent "Permanent link")

Bases: `BaseModel`

Streaming event

Source code in `vllm/entrypoints/anthropic/protocol.py`

```
classAnthropicStreamEvent(BaseModel):
"""Streaming event"""

    type: Literal[
        "message_start",
        "message_delta",
        "message_stop",
        "content_block_start",
        "content_block_delta",
        "content_block_stop",
        "ping",
        "error",
    ]
    message: "AnthropicMessagesResponse | None" = None
    delta: AnthropicDelta | None = None
    content_block: AnthropicContentBlock | None = None
    index: int | None = None
    error: AnthropicError | None = None
    usage: AnthropicUsage | None = None
```

## AnthropicTool [¶](#vllm.entrypoints.anthropic.protocol.AnthropicTool "Permanent link")

Bases: `BaseModel`

Tool definition

Source code in `vllm/entrypoints/anthropic/protocol.py`

```
classAnthropicTool(BaseModel):
"""Tool definition"""

    name: str
    description: str | None = None
    input_schema: dict[str, Any]
    defer_loading: bool | None = None

    @field_validator("input_schema")
    @classmethod
    defvalidate_input_schema(cls, v):
        if not isinstance(v, dict):
            raise ValueError("input_schema must be a dictionary")
        if "type" not in v:
            v["type"] = "object"  # Default to object type
        return v
```

## AnthropicToolChoice [¶](#vllm.entrypoints.anthropic.protocol.AnthropicToolChoice "Permanent link")

Bases: `BaseModel`

Tool Choice definition

Source code in `vllm/entrypoints/anthropic/protocol.py`

```
classAnthropicToolChoice(BaseModel):
"""Tool Choice definition"""

    type: Literal["auto", "any", "tool", "none"]
    name: str | None = None

    @model_validator(mode="after")
    defvalidate_name_required_for_tool(self) -> "AnthropicToolChoice":
        if self.type == "tool" and not self.name:
            raise ValueError("tool_choice.name is required when type is 'tool'")
        return self
```

## AnthropicUsage [¶](#vllm.entrypoints.anthropic.protocol.AnthropicUsage "Permanent link")

Bases: `BaseModel`

Token usage information

Source code in `vllm/entrypoints/anthropic/protocol.py`

```
classAnthropicUsage(BaseModel):
"""Token usage information"""

    input_tokens: int
    output_tokens: int
    cache_creation_input_tokens: int | None = None
    cache_read_input_tokens: int | None = None
```