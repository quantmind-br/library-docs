---
title: identity_reasoning_parser - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/reasoning/identity_reasoning_parser/
source: sitemap
fetched_at: 2026-05-07T21:35:05.256403723-03:00
rendered_js: false
word_count: 34
summary: This document defines the IdentityReasoningParser class in vLLM, which treats model output as raw content without attempting to parse or separate reasoning tokens.
tags:
    - vllm
    - reasoning-parser
    - token-processing
    - language-model
    - llm-framework
category: reference
---

## IdentityReasoningParser [¶](#vllm.reasoning.identity_reasoning_parser.IdentityReasoningParser "Permanent link")

Bases: `ReasoningParser`

Identity reasoning parser.

This parser does not attempt to parse or strip out reasoning tokens. It treats the entire model output as content and ignores reasoning.

Source code in `vllm/reasoning/identity_reasoning_parser.py`

```
classIdentityReasoningParser(ReasoningParser):
"""
    Identity reasoning parser.

    This parser does not attempt to parse or strip out reasoning tokens.
    It treats the entire model output as content and ignores reasoning.
    """

    def__init__(self, tokenizer: PreTrainedTokenizerBase, *args, **kwargs):
        super().__init__(tokenizer, *args, **kwargs)
        if not self.model_tokenizer:
            raise ValueError(
                "The model tokenizer must be passed to the ReasoningParser "
                "constructor during construction."
            )

    @property
    defreasoning_start_str(self) -> str | None:
        return None

    @property
    defreasoning_end_str(self) -> str | None:
        return None

    defis_reasoning_end(self, input_ids: Sequence[int]) -> bool:
        # Always return True, since we never treat reasoning specially
        return True

    defis_reasoning_end_streaming(
        self, input_ids: Sequence[int], delta_ids: Iterable[int]
    ) -> bool:
        return True

    defextract_content_ids(self, input_ids: list[int]) -> list[int]:
        # Identity: return all tokens as content
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
        # Just wrap delta_text as content, ignore reasoning
        if delta_text:
            return DeltaMessage(content=delta_text)
        return None

    defextract_reasoning(
        self, model_output: str, request: "ChatCompletionRequest | ResponsesRequest"
    ) -> tuple[str | None, str | None]:
        # No reasoning separation: return None for reasoning,
        # and full model_output as content
        return None, model_output
```