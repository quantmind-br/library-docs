---
title: glm47_moe_tool_parser - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/tool_parsers/glm47_moe_tool_parser/
source: sitemap
fetched_at: 2026-05-07T21:36:00.815917978-03:00
rendered_js: false
word_count: 55
summary: This document outlines the modifications made to the GLM-4.7 tool call parser to support updated function name formatting and zero-argument tool calls.
tags:
    - glm-4-7
    - tool-call-parsing
    - regex-overrides
    - parser-logic
    - api-updates
category: api
---

GLM-4.7 Tool Call Parser.

GLM-4.7 uses a slightly different tool call format compared to GLM-4.5: - The function name may appear on the same line as `<tool_call>` without a newline separator before the first `<arg_key>`. - Tool calls may have zero arguments (e.g. `<tool_call>func</tool_call>`).

This parser overrides the parent regex patterns to handle both formats.