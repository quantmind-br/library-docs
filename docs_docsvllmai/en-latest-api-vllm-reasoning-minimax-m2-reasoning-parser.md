---
title: minimax_m2_reasoning_parser - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/reasoning/minimax_m2_reasoning_parser/
source: sitemap
fetched_at: 2026-05-07T21:35:07.09893357-03:00
rendered_js: false
word_count: 100
summary: This document defines the reasoning parser classes used to identify and extract thought processes from MiniMax M2 model outputs. It details how the system handles streaming tokens and identifies the transition between reasoning content and final responses.
tags:
    - minimax-m2
    - reasoning-parser
    - vllm
    - tokenization
    - streaming
    - llm-inference
category: reference
---

## MiniMaxM2AppendThinkReasoningParser [¶](#vllm.reasoning.minimax_m2_reasoning_parser.MiniMaxM2AppendThinkReasoningParser "Permanent link")

Bases: `ReasoningParser`

Reasoning parser for MiniMax M2 model.

Source code in `vllm/reasoning/minimax_m2_reasoning_parser.py`

```
classMiniMaxM2AppendThinkReasoningParser(ReasoningParser):
"""
    Reasoning parser for MiniMax M2 model.
    """

    def__init__(self, tokenizer: TokenizerLike, *args, **kwargs):
        super().__init__(tokenizer, *args, **kwargs)
        self.end_token_id = self.vocab.get("</think>")
        self.start_token_id = self.vocab.get("<think>")

    defis_reasoning_end(self, input_ids: Sequence[int]) -> bool:
        end_token_id = self.end_token_id
        start_token_id = self.start_token_id
        for input_id in reversed(input_ids):
            if input_id in (end_token_id, start_token_id):
                return input_id == end_token_id
        return False

    defextract_content_ids(self, input_ids: list[int]) -> list[int]:
        return input_ids

    defextract_reasoning_streaming(
        self,
        previous_text: str,
        current_text: str,
        delta_text: str,
        previous_token_ids: Sequence[int],
        current_token_ids: Sequence[int],
        delta_token_ids: Sequence[int],
    ) -> DeltaMessage | None:
        if len(previous_token_ids) == 0:
            delta_text = "<think>" + delta_text
        return DeltaMessage(content=delta_text)

    defextract_reasoning(
        self, model_output: str, request: "ChatCompletionRequest | ResponsesRequest"
    ) -> tuple[str | None, str | None]:
        return None, "<think>" + model_output
```

## MiniMaxM2ReasoningParser [¶](#vllm.reasoning.minimax_m2_reasoning_parser.MiniMaxM2ReasoningParser "Permanent link")

Bases: `BaseThinkingReasoningParser`

Reasoning parser for MiniMax M2 model.

MiniMax M2 models don't generate start token, only end token. All content before is reasoning, content after is the actual response.

Source code in `vllm/reasoning/minimax_m2_reasoning_parser.py`

```
classMiniMaxM2ReasoningParser(BaseThinkingReasoningParser):
"""
    Reasoning parser for MiniMax M2 model.

    MiniMax M2 models don't generate <think> start token, only </think> end
    token. All content before </think> is reasoning, content after is the
    actual response.
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
"""
        Extract reasoning content from a delta message for streaming.

        MiniMax M2 models don't generate <think> start token, so we assume
        all content is reasoning until we encounter the </think> end token.
        """
        # Skip single end token
        if len(delta_token_ids) == 1 and delta_token_ids[0] == self.end_token_id:
            return None

        # Check if end token has already appeared in previous tokens
        # meaning we're past the reasoning phase
        if self.end_token_id in previous_token_ids:
            # We're past the reasoning phase, this is content
            return DeltaMessage(content=delta_text)

        # Check if end token is in delta tokens
        if self.end_token_id in delta_token_ids:
            # End token in delta, split reasoning and content
            end_index = delta_text.find(self.end_token)
            reasoning = delta_text[:end_index]
            content = delta_text[end_index + len(self.end_token) :]
            return DeltaMessage(
                reasoning=reasoning if reasoning else None,
                content=content if content else None,
            )

        # No end token yet, all content is reasoning
        return DeltaMessage(reasoning=delta_text)
```

### end\_token `property` [¶](#vllm.reasoning.minimax_m2_reasoning_parser.MiniMaxM2ReasoningParser.end_token "Permanent link")

The token that ends reasoning content.

### start\_token `property` [¶](#vllm.reasoning.minimax_m2_reasoning_parser.MiniMaxM2ReasoningParser.start_token "Permanent link")

The token that starts reasoning content.

```
extract_reasoning_streaming(
    previous_text: str,
    current_text: str,
    delta_text: str,
    previous_token_ids: Sequence[int],
    current_token_ids: Sequence[int],
    delta_token_ids: Sequence[int],
) -> DeltaMessage | None
```

Extract reasoning content from a delta message for streaming.

MiniMax M2 models don't generate start token, so we assume all content is reasoning until we encounter the end token.

Source code in `vllm/reasoning/minimax_m2_reasoning_parser.py`

```
defextract_reasoning_streaming(
    self,
    previous_text: str,
    current_text: str,
    delta_text: str,
    previous_token_ids: Sequence[int],
    current_token_ids: Sequence[int],
    delta_token_ids: Sequence[int],
) -> DeltaMessage | None:
"""
    Extract reasoning content from a delta message for streaming.

    MiniMax M2 models don't generate <think> start token, so we assume
    all content is reasoning until we encounter the </think> end token.
    """
    # Skip single end token
    if len(delta_token_ids) == 1 and delta_token_ids[0] == self.end_token_id:
        return None

    # Check if end token has already appeared in previous tokens
    # meaning we're past the reasoning phase
    if self.end_token_id in previous_token_ids:
        # We're past the reasoning phase, this is content
        return DeltaMessage(content=delta_text)

    # Check if end token is in delta tokens
    if self.end_token_id in delta_token_ids:
        # End token in delta, split reasoning and content
        end_index = delta_text.find(self.end_token)
        reasoning = delta_text[:end_index]
        content = delta_text[end_index + len(self.end_token) :]
        return DeltaMessage(
            reasoning=reasoning if reasoning else None,
            content=content if content else None,
        )

    # No end token yet, all content is reasoning
    return DeltaMessage(reasoning=delta_text)
```