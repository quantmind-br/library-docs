---
title: deepseek_r1_reasoning_parser - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/reasoning/deepseek_r1_reasoning_parser/
source: sitemap
fetched_at: 2026-05-07T21:34:56.421296165-03:00
rendered_js: false
word_count: 53
summary: This document defines the DeepSeekR1ReasoningParser class, which parses and extracts reasoning content delimited by <think> and </think> tokens from DeepSeek R1 model outputs.
tags:
    - deepseek-r1
    - reasoning-parser
    - vllm
    - token-extraction
    - model-output-parsing
category: reference
---

## DeepSeekR1ReasoningParser [¶](#vllm.reasoning.deepseek_r1_reasoning_parser.DeepSeekR1ReasoningParser "Permanent link")

Bases: `BaseThinkingReasoningParser`

Reasoning parser for DeepSeek R1 model.

The DeepSeek R1 model uses ... tokens to denote reasoning text. This parser extracts the reasoning content from the model output.

Source code in `vllm/reasoning/deepseek_r1_reasoning_parser.py`

```
classDeepSeekR1ReasoningParser(BaseThinkingReasoningParser):
"""
    Reasoning parser for DeepSeek R1 model.

    The DeepSeek R1 model uses <think>...</think> tokens to denote reasoning
    text. This parser extracts the reasoning content from the model output.
    """

    @property
    defstart_token(self) -> str:
"""The token that starts reasoning content."""
        return "<think>"

    @property
    defend_token(self) -> str:
"""The token that ends reasoning content."""
        return "</think>"

    defextract_reasoning_streaming(
        self,
        previous_text: str,
        current_text: str,
        delta_text: str,
        previous_token_ids: Sequence[int],
        current_token_ids: Sequence[int],
        delta_token_ids: Sequence[int],
    ) -> DeltaMessage | None:
        ret = super().extract_reasoning_streaming(
            previous_text,
            current_text,
            delta_text,
            previous_token_ids,
            current_token_ids,
            delta_token_ids,
        )
        if (
            ret is not None
            and self.start_token_id not in previous_token_ids
            and self.start_token_id not in delta_token_ids
        ):
            if self.end_token_id in delta_token_ids:
                # end token in delta with more tokens,
                # extract reasoning content and content
                end_index = delta_text.find(self.end_token)
                reasoning = delta_text[:end_index]
                content = delta_text[end_index + len(self.end_token) :]
                return DeltaMessage(
                    reasoning=reasoning,
                    content=content if content else None,
                )
            elif self.end_token_id in previous_token_ids:
                # end token in previous, thinking content ends
                return DeltaMessage(content=delta_text)
            else:
                # no end token in previous or delta, reasoning content continues
                return DeltaMessage(reasoning=delta_text)

        return ret
```

### end\_token `property` [¶](#vllm.reasoning.deepseek_r1_reasoning_parser.DeepSeekR1ReasoningParser.end_token "Permanent link")

The token that ends reasoning content.

### start\_token `property` [¶](#vllm.reasoning.deepseek_r1_reasoning_parser.DeepSeekR1ReasoningParser.start_token "Permanent link")

The token that starts reasoning content.