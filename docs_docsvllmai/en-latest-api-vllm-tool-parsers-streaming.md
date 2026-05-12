---
title: streaming - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/tool_parsers/streaming/
source: sitemap
fetched_at: 2026-05-07T21:36:30.998830875-03:00
rendered_js: false
word_count: 42
summary: This document provides the reference implementation for utility functions used to parse, validate, and build streaming tool-call deltas for LLM interactions.
tags:
    - python-api
    - streaming-tools
    - llm-integration
    - string-parsing
    - function-calls
    - tokenization
category: api
---

```
_bracket_level(
    s: str, opening: str = "{", closing: str = "}"
) -> int
```

Calculate the current level of nested brackets in a string.

Source code in `vllm/tool_parsers/streaming.py`

```
def_bracket_level(s: str, opening: str = "{", closing: str = "}") -> int:
"""Calculate the current level of nested brackets in a string."""
    level = 0
    for char in s:
        if char == opening:
            level += 1
        elif char == closing:
            level -= 1
    return level

extract_named_tool_call_streaming(
    *,
    delta_text: str,
    function_name: str,
    function_name_returned: bool,
    tool_call_idx: int | None,
    tool_call_id_type: str,
    tokenizer: TokenizerLike,
    tool_call_array_index: int = 0,
) -> tuple[DeltaMessage | None, bool]
```

Build a streaming tool-call delta for forced named tool choice.

Source code in `vllm/tool_parsers/streaming.py`

```
defextract_named_tool_call_streaming(
    *,
    delta_text: str,
    function_name: str,
    function_name_returned: bool,
    tool_call_idx: int | None,
    tool_call_id_type: str,
    tokenizer: "TokenizerLike",
    tool_call_array_index: int = 0,
) -> tuple[DeltaMessage | None, bool]:
"""Build a streaming tool-call delta for forced named tool choice."""
    if function_name_returned:
        delta_tool_call = DeltaToolCall(
            function=DeltaFunctionCall(arguments=delta_text),
            index=tool_call_array_index,
        )
    else:
        if is_mistral_tokenizer(tokenizer):
            tool_call_id = MistralToolCall.generate_random_id()
        else:
            tool_call_id = make_tool_call_id(
                id_type=tool_call_id_type,
                func_name=function_name,
                idx=tool_call_idx,
            )
        delta_tool_call = DeltaToolCall(
            id=tool_call_id,
            type="function",
            function=DeltaFunctionCall(
                name=function_name,
                arguments=delta_text,
            ),
            index=tool_call_array_index,
        )
        function_name_returned = True
    return (
        DeltaMessage(tool_calls=[delta_tool_call]),
        function_name_returned,
    )
```

## filter\_delta\_text [¶](#vllm.tool_parsers.streaming.filter_delta_text "Permanent link")

Trim trailing tool-list delimiters from required-tool streaming text.

Source code in `vllm/tool_parsers/streaming.py`

```
deffilter_delta_text(
    delta_text: str,
    previous_text: str,
) -> tuple[str, bool]:
"""Trim trailing tool-list delimiters from required-tool streaming text."""
    bracket_level = _bracket_level(previous_text)
    updated_delta = ""
    passed_zero = False
    for char in delta_text:
        if char == "{":
            bracket_level += 1
            passed_zero = bracket_level == 0
        elif char == "}":
            bracket_level -= 1
            passed_zero = bracket_level == 0

        if bracket_level != 0:
            updated_delta += char
        else:
            if char == ",":
                break
    return updated_delta, passed_zero
```