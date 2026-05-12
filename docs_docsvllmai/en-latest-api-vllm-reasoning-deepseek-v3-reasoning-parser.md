---
title: deepseek_v3_reasoning_parser - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/reasoning/deepseek_v3_reasoning_parser/
source: sitemap
fetched_at: 2026-05-07T21:34:56.993531004-03:00
rendered_js: false
word_count: 4
summary: This document defines the DeepSeekV3ReasoningParser class, which dynamically selects between different reasoning parsing strategies based on model configuration settings.
tags:
    - python
    - parser
    - deepseek
    - llm-inference
    - tokenization
    - reasoning-extraction
category: reference
---

```
classDeepSeekV3ReasoningParser(ReasoningParser):
"""
    V3 parser that delegates to either DeepSeekR1ReasoningParser or
    IdentityReasoningParser based on `thinking` and `separate_reasoning`.
    """

    def__init__(self, tokenizer: PreTrainedTokenizerBase, *args, **kwargs):
        super().__init__(tokenizer, *args, **kwargs)

        chat_kwargs = kwargs.get("chat_template_kwargs", {}) or {}
        thinking = bool(chat_kwargs.get("thinking", False))
        enable_thinking = bool(chat_kwargs.get("enable_thinking", False))
        thinking = thinking or enable_thinking

        self._parser: ReasoningParser
        if thinking:
            self._parser = DeepSeekR1ReasoningParser(tokenizer, *args, **kwargs)
        else:
            self._parser = IdentityReasoningParser(tokenizer, *args, **kwargs)

    @property
    defreasoning_start_str(self) -> str | None:
        return self._parser.reasoning_start_str

    @property
    defreasoning_end_str(self) -> str | None:
        return self._parser.reasoning_end_str

    defis_reasoning_end(self, input_ids: Sequence[int]) -> bool:
        return self._parser.is_reasoning_end(input_ids)

    defis_reasoning_end_streaming(
        self, input_ids: Sequence[int], delta_ids: Iterable[int]
    ) -> bool:
        return self._parser.is_reasoning_end_streaming(input_ids, delta_ids)

    defextract_content_ids(self, input_ids: list[int]) -> list[int]:
        return self._parser.extract_content_ids(input_ids)

    defextract_reasoning(
        self, model_output: str, request: "ChatCompletionRequest | ResponsesRequest"
    ) -> tuple[str | None, str | None]:
        return self._parser.extract_reasoning(model_output, request)

    defextract_reasoning_streaming(
        self,
        previous_text: str,
        current_text: str,
        delta_text: str,
        previous_token_ids: Sequence[int],
        current_token_ids: Sequence[int],
        delta_token_ids: Sequence[int],
    ) -> "DeltaMessage | None":
        return self._parser.extract_reasoning_streaming(
            previous_text,
            current_text,
            delta_text,
            previous_token_ids,
            current_token_ids,
            delta_token_ids,
        )
```