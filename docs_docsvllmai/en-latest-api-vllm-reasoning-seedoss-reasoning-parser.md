---
title: seedoss_reasoning_parser - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/reasoning/seedoss_reasoning_parser/
source: sitemap
fetched_at: 2026-05-07T21:35:13.585104687-03:00
rendered_js: false
word_count: 65
summary: This document defines the SeedOSSReasoningParser class, which identifies and extracts reasoning content from SeedOSS model outputs by parsing specific start and end tokens.
tags:
    - seedoss
    - reasoning-parser
    - model-output
    - token-extraction
    - vllm-framework
category: reference
---

Bases: `BaseThinkingReasoningParser`

Reasoning parser for SeedOSS model.

The SeedOSS model uses ... tokens to denote reasoning content text. This parser extracts the reasoning content from the model output. Similar to DeepSeek R1, it supports cases where the model doesn't generate the start token.

Source code in `vllm/reasoning/seedoss_reasoning_parser.py`

```
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27

classSeedOSSReasoningParser(BaseThinkingReasoningParser):
"""
    Reasoning parser for SeedOSS model.

    The SeedOSS model uses <seed:think>...</seed:think> tokens to
    denote reasoning content text. This parser extracts
    the reasoning content from the model output.
    Similar to DeepSeek R1, it supports cases
    where the model doesn't generate the start token.
    """

    @property
    defstart_token(self) -> str:
"""The token that starts reasoning content."""
        return "<seed:think>"

    @property
    defend_token(self) -> str:
"""The token that ends reasoning content."""
        return "</seed:think>"
```

### end\_token `property` [¶](#vllm.reasoning.seedoss_reasoning_parser.SeedOSSReasoningParser.end_token "Permanent link")

The token that ends reasoning content.

### start\_token `property` [¶](#vllm.reasoning.seedoss_reasoning_parser.SeedOSSReasoningParser.start_token "Permanent link")

The token that starts reasoning content.