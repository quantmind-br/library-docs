---
title: deepseekv4_tool_parser - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/tool_parsers/deepseekv4_tool_parser/
source: sitemap
fetched_at: 2026-05-07T21:35:54.924114102-03:00
rendered_js: false
word_count: 31
summary: This document defines the DeepSeekV4ToolParser class, which implements specific token wrappers for tool calls in the DeepSeek V4 DSML framework.
tags:
    - deepseek-v4
    - tool-parsing
    - dsml
    - vllm
    - parser-implementation
category: reference
---

Bases: `DeepSeekV32ToolParser`

DeepSeek V4 DSML tool parser.

V4 keeps the V3.2 DSML invoke/parameter grammar, but wraps tool calls in `<｜DSML｜tool_calls>` instead of `<｜DSML｜function_calls>`.

Source code in `vllm/tool_parsers/deepseekv4_tool_parser.py`

```
classDeepSeekV4ToolParser(DeepSeekV32ToolParser):
"""
    DeepSeek V4 DSML tool parser.

    V4 keeps the V3.2 DSML invoke/parameter grammar, but wraps tool calls in
    ``<｜DSML｜tool_calls>`` instead of ``<｜DSML｜function_calls>``.
    """

    tool_call_start_token: str = "<｜DSML｜tool_calls>"
    tool_call_end_token: str = "</｜DSML｜tool_calls>"

    defget_structural_tag(self, request: ChatCompletionRequest):
        return get_model_structural_tag(
            model="deepseek_v4",
            tools=request.tools,
            tool_choice=request.tool_choice,
            reasoning=get_enable_structured_outputs_in_reasoning(),
        )
```