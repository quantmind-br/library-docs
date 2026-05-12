---
title: minimax_m2_parser - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/parser/minimax_m2_parser/
source: sitemap
fetched_at: 2026-05-07T21:34:28.100786377-03:00
rendered_js: false
word_count: 110
summary: This document describes the MiniMaxM2Parser, a unified interface for handling reasoning extraction and tool call parsing specifically designed for MiniMax M2 language models.
tags:
    - minimax-m2
    - vllm
    - parser-implementation
    - reasoning-extraction
    - tool-calling
    - model-parsing
category: reference
---

MiniMax M2 Parser - A unified parser for MiniMax M2 models.

This parser combines the existing MiniMaxM2ReasoningParser and MinimaxM2ToolParser into a single unified interface by delegating to those implementations.

## MiniMaxM2Parser [¶](#vllm.parser.minimax_m2_parser.MiniMaxM2Parser "Permanent link")

Bases: `DelegatingParser`

Unified parser for MiniMax M2 models that handles both reasoning extraction and tool call parsing.

This parser delegates to the existing implementations: - MiniMaxM2ReasoningParser for reasoning extraction - MinimaxM2ToolParser for tool call parsing

MiniMax M2 models have two special behaviors: 1. Reasoning: They don't generate start token, only end token. All content before is reasoning, content after is the actual response. 2. Tool Calls: They use ... tags with ... and ... syntax.

Source code in `vllm/parser/minimax_m2_parser.py`

```
classMiniMaxM2Parser(DelegatingParser):
"""
    Unified parser for MiniMax M2 models that handles both reasoning
    extraction and tool call parsing.

    This parser delegates to the existing implementations:
    - MiniMaxM2ReasoningParser for reasoning extraction
    - MinimaxM2ToolParser for tool call parsing

    MiniMax M2 models have two special behaviors:
    1. Reasoning: They don't generate <think> start token, only </think> end
       token. All content before </think> is reasoning, content after is the
       actual response.
    2. Tool Calls: They use <minimax:tool_call>...</minimax:tool_call> tags
       with <invoke name="...">...</invoke> and <parameter name="...">...</parameter>
       syntax.
    """

    # Class-level parser classes for compatibility
    reasoning_parser_cls = MiniMaxM2ReasoningParser
    tool_parser_cls = MinimaxM2ToolParser

    def__init__(
        self,
        tokenizer: TokenizerLike,
        tools: list[Tool] | None = None,
        *args,
        **kwargs,
    ):
        super().__init__(tokenizer, *args, **kwargs)

        # Initialize the underlying parsers
        self._reasoning_parser = MiniMaxM2ReasoningParser(tokenizer, *args, **kwargs)
        self._tool_parser = MinimaxM2ToolParser(tokenizer, tools)

        logger.debug(
            "vLLM Successfully initialized parser %s!", self.__class__.__name__
        )
```