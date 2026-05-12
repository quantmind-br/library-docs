---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/openai/responses/utils/
source: sitemap
fetched_at: 2026-05-07T21:20:34.313768654-03:00
rendered_js: false
word_count: 214
summary: This document provides a reference for utility functions used in the vLLM OpenAI entrypoint to process response items, manage chat message construction with tool calls, and determine whether to continue partial model generations.
tags:
    - vllm
    - openai-api
    - tool-calling
    - chat-completion
    - message-processing
    - model-generation
category: reference
---

## \_maybe\_combine\_reasoning\_and\_tool\_call [¶](#vllm.entrypoints.openai.responses.utils._maybe_combine_reasoning_and_tool_call "Permanent link")

```
_maybe_combine_reasoning_and_tool_call(
    item: ResponseInputOutputItem,
    messages: list[ChatCompletionMessageParam],
) -> ChatCompletionMessageParam | None
```

Many models treat MCP calls and reasoning as a single message. This function checks if the last message is a reasoning message and the current message is a tool call

Source code in `vllm/entrypoints/openai/responses/utils.py`

```
def_maybe_combine_reasoning_and_tool_call(
    item: ResponseInputOutputItem, messages: list[ChatCompletionMessageParam]
) -> ChatCompletionMessageParam | None:
"""Many models treat MCP calls and reasoning as a single message.
    This function checks if the last message is a reasoning message and
    the current message is a tool call"""
    if not (
        isinstance(item, ResponseFunctionToolCall)
        and item.id
        and item.id.startswith(MCP_PREFIX)
    ):
        return None
    if len(messages) == 0:
        return None
    last_message = messages[-1]
    if not (
        last_message.get("role") == "assistant"
        and last_message.get("reasoning") is not None
    ):
        return None

    last_message["tool_calls"] = [
        ChatCompletionMessageToolCallParam(
            id=item.call_id,
            function=FunctionCallTool(
                name=item.name,
                arguments=item.arguments,
            ),
            type="function",
        )
    ]
    return last_message
```

## construct\_chat\_messages\_with\_tool\_call [¶](#vllm.entrypoints.openai.responses.utils.construct_chat_messages_with_tool_call "Permanent link")

```
construct_chat_messages_with_tool_call(
    input_messages: list[ResponseInputOutputItem],
) -> list[ChatCompletionMessageParam]
```

This function wraps \_construct\_single\_message\_from\_response\_item Because some chatMessages come from multiple response items for example a reasoning item and a MCP tool call are two response items but are one chat message

Source code in `vllm/entrypoints/openai/responses/utils.py`

```
defconstruct_chat_messages_with_tool_call(
    input_messages: list[ResponseInputOutputItem],
) -> list[ChatCompletionMessageParam]:
"""This function wraps _construct_single_message_from_response_item
    Because some chatMessages come from multiple response items
    for example a reasoning item and a MCP tool call are two response items
    but are one chat message
    """
    messages: list[ChatCompletionMessageParam] = []
    for item in input_messages:
        maybe_combined_message = _maybe_combine_reasoning_and_tool_call(item, messages)
        if maybe_combined_message is not None:
            messages[-1] = maybe_combined_message
        else:
            messages.append(_construct_single_message_from_response_item(item))

    return messages
```

## convert\_tool\_responses\_to\_completions\_format [¶](#vllm.entrypoints.openai.responses.utils.convert_tool_responses_to_completions_format "Permanent link")

```
convert_tool_responses_to_completions_format(
    tool: dict,
) -> dict
```

Convert a flat tool schema

{"type": "function", "name": "...", "description": "...", "parameters": {...}}

into: {"type": "function", "function": {...}}

Source code in `vllm/entrypoints/openai/responses/utils.py`

```
defconvert_tool_responses_to_completions_format(tool: dict) -> dict:
"""
    Convert a flat tool schema:
        {"type": "function", "name": "...", "description": "...", "parameters": {...}}
    into:
        {"type": "function", "function": {...}}
    """
    return {
        "type": "function",
        "function": tool,
    }
```

Extracts the tool types from the given tools.

Source code in `vllm/entrypoints/openai/responses/utils.py`

```
defextract_tool_types(tools: list[Tool]) -> set[str]:
"""
    Extracts the tool types from the given tools.
    """
    tool_types: set[str] = set()
    for tool in tools:
        if tool.type == "mcp":
            # Allow the MCP Tool type to enable built in tools if the
            # server_label is allowlisted in
            # envs.VLLM_GPT_OSS_SYSTEM_TOOL_MCP_LABELS
            if tool.server_label in envs.VLLM_GPT_OSS_SYSTEM_TOOL_MCP_LABELS:
                tool_types.add(tool.server_label)
        else:
            tool_types.add(tool.type)
    return tool_types
```

## should\_continue\_final\_message [¶](#vllm.entrypoints.openai.responses.utils.should_continue_final_message "Permanent link")

```
should_continue_final_message(
    request_input: str | list[ResponseInputOutputItem],
) -> bool
```

Determine if the last input message is a partial assistant message that should be continued rather than starting a new generation.

This enables partial message completion similar to Anthropic's Messages API, where users can provide an incomplete assistant message and have the model continue from where it left off.

A message is considered partial if: 1. It's a ResponseOutputMessage or ResponseReasoningItem 2. Its status is "in\_progress" or "incomplete"

Parameters:

Name Type Description Default `request_input` `str | list[ResponseInputOutputItem]`

The input to the Responses API request

*required*

Returns:

Type Description `bool`

True if the final message should be continued, False otherwise

Source code in `vllm/entrypoints/openai/responses/utils.py`

```
defshould_continue_final_message(
    request_input: str | list[ResponseInputOutputItem],
) -> bool:
"""
    Determine if the last input message is a partial assistant message
    that should be continued rather than starting a new generation.

    This enables partial message completion similar to Anthropic's Messages API,
    where users can provide an incomplete assistant message and have the model
    continue from where it left off.

    A message is considered partial if:
    1. It's a ResponseOutputMessage or ResponseReasoningItem
    2. Its status is "in_progress" or "incomplete"

    Args:
        request_input: The input to the Responses API request

    Returns:
        True if the final message should be continued, False otherwise
    """
    if isinstance(request_input, str):
        # Simple string input is always a user message
        return False

    if not request_input:
        return False

    last_item = request_input[-1]

    # Check if the last item is a partial assistant message
    if isinstance(last_item, ResponseOutputMessage):
        return last_item.status in ("in_progress", "incomplete")

    # Check if the last item is a partial reasoning item
    if isinstance(last_item, ResponseReasoningItem):
        return last_item.status in ("in_progress", "incomplete")

    if isinstance(last_item, dict):
        # only support partial completion for messages for now
        if last_item.get("type", "message") not in ("message", "reasoning"):
            return False
        return last_item.get("status") in ("in_progress", "incomplete")

    return False
```