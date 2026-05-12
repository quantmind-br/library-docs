---
title: poolside_v1_reasoning_parser - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/reasoning/poolside_v1_reasoning_parser/
source: sitemap
fetched_at: 2026-05-07T21:35:11.024163821-03:00
rendered_js: false
word_count: 158
summary: This document describes an improvement to reasoning parsers in vLLM by scoping the backward search for reasoning tokens to the current assistant turn, preventing false positives from conversation history.
tags:
    - vllm
    - reasoning-parser
    - token-processing
    - deepseek-v3
    - natural-language-processing
category: concept
---

Laguna reasoning parser.

`DeepSeekV3ReasoningParser.is_reasoning_end` walks the entire token sequence backwards and returns `True` on the first `</think>` it sees. When called on `prompt_token_ids` that mistakes any stray `</think>` in conversation history, few-shot examples or tool descriptions for a template-injected "thinking already ended" marker. In the streaming path (see `vllm/entrypoints/openai/chat_completion/serving.py`, `prompt_is_reasoning_end_arr`) that false positive short-circuits the reasoning parser for the whole response, so any `<think>...</think>` the model emits itself ends up in the content field instead of the reasoning field.

As we have more flexible templates, we instead scope the backward search to the current assistant turn: the walk terminates as soon as we hit the `<assistant>` start-of-message token. A `</think>` in a prior user turn or few-shot example is no longer visible.

## PoolsideV1ReasoningParser [¶](#vllm.reasoning.poolside_v1_reasoning_parser.PoolsideV1ReasoningParser "Permanent link")

Bases: `DeepSeekV3ReasoningParser`

Drop-in replacement for `deepseek_v3` that tolerates `</think>` tokens appearing anywhere in the prompt other than the generation prefix.

Source code in `vllm/reasoning/poolside_v1_reasoning_parser.py`

```
classPoolsideV1ReasoningParser(DeepSeekV3ReasoningParser):
"""Drop-in replacement for ``deepseek_v3`` that tolerates ``</think>``
    tokens appearing anywhere in the prompt other than the generation prefix.
    """

    _start_of_assistant_message = "<assistant>"

    def__init__(self, tokenizer: PreTrainedTokenizerBase, *args, **kwargs):
        super().__init__(tokenizer, *args, **kwargs)

        if self._start_of_assistant_message not in self.vocab:
            raise ValueError(
                f"Tokenizer must contain {self._start_of_assistant_message!r} token"
            )
        self._start_of_assistant_message_token_id = self.vocab[
            self._start_of_assistant_message
        ]

    defis_reasoning_end(self, input_ids: Sequence[int]) -> bool:
        # IdentityReasoningParser always returns True: no reasoning to parse.
        if isinstance(self._parser, IdentityReasoningParser):
            return True

        assert isinstance(self._parser, DeepSeekR1ReasoningParser)
        for tok_id in reversed(input_ids):
            # <think>: reasoning is not yet ended.
            if tok_id == self._parser.start_token_id:
                return False
            # </think>: reasoning has ended.
            if tok_id == self._parser.end_token_id:
                return True
            # <assistant>: reached the start of the current assistant turn
            # without seeing either marker. Anything further back belongs to
            # the prior conversation and should be ignored.
            if tok_id == self._start_of_assistant_message_token_id:
                return False
        return False
```