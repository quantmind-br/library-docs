---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/openai/utils/
source: sitemap
fetched_at: 2026-05-07T21:20:42.135215816-03:00
rendered_js: false
word_count: 14
summary: This function ensures that chat completion responses only contain a single tool call when the parallel_tool_calls request parameter is set to false.
tags:
    - vllm
    - tool-calling
    - openai-api
    - response-filtering
    - python
category: api
---

Filter to first tool call only when parallel\_tool\_calls is False.

Source code in `vllm/entrypoints/openai/utils.py`

```
defmaybe_filter_parallel_tool_calls(
    choice: _ChatCompletionResponseChoiceT, request: ChatCompletionRequest
) -> _ChatCompletionResponseChoiceT:
"""Filter to first tool call only when parallel_tool_calls is False."""

    if request.parallel_tool_calls:
        return choice

    if isinstance(choice, ChatCompletionResponseChoice) and choice.message.tool_calls:
        choice.message.tool_calls = choice.message.tool_calls[:1]
    elif (
        isinstance(choice, ChatCompletionResponseStreamChoice)
        and choice.delta.tool_calls
    ):
        choice.delta.tool_calls = [
            tool_call for tool_call in choice.delta.tool_calls if tool_call.index == 0
        ]

    return choice
```