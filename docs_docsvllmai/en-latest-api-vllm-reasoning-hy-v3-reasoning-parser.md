---
title: hy_v3_reasoning_parser - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/reasoning/hy_v3_reasoning_parser/
source: sitemap
fetched_at: 2026-05-07T21:35:03.87743458-03:00
rendered_js: false
word_count: 16
summary: This document defines the HYV3ReasoningParser class, which manages the extraction of reasoning content from model outputs by dynamically switching between parsers based on the specified reasoning effort.
tags:
    - parser
    - model-output
    - reasoning-extraction
    - python-class
    - llm-tokens
category: api
---

```
classHYV3ReasoningParser(BaseThinkingReasoningParser):
"""
    HYV3 parser that delegates to either HYV3ReasoningParser or
    IdentityReasoningParser based on `reasoning_effort`.

    The HYV3 model uses <think>...</think> tokens to denote reasoning text.
    This parser extracts the reasoning content from the model output.
    """

    def__init__(self, tokenizer: TokenizerLike, *args, **kwargs):
        super().__init__(tokenizer, *args, **kwargs)

        # First, If there is reasoning_effort in chat_kwargs,
        # prioritize using chat_kwargs.reasoning_effort.
        # If it's not present, use the "reasoning_effort" field
        # at the outer level of the chat message.
        # Otherwise, If both are empty, assign "no_think".

        chat_kwargs = kwargs.get("chat_template_kwargs", {}) or {}
        reasoning_effort = (
            chat_kwargs.get("reasoning_effort")
            or kwargs.get("reasoning_effort")
            or "no_think"
        )

        logger.debug("reasoning_effort for choosing parser: %s", reasoning_effort)

        self._identity_parser: IdentityReasoningParser | None
        if reasoning_effort == "no_think":
            self._identity_parser = IdentityReasoningParser(tokenizer, *args, **kwargs)
        else:
            self._identity_parser = None

    @property
    defstart_token(self) -> str:
"""The token that starts reasoning content."""
        return "<think>"

    @property
    defend_token(self) -> str:
"""The token that ends reasoning content."""
        return "</think>"

    defis_reasoning_end(self, input_ids: Sequence[int]) -> bool:
        if self._identity_parser is not None:
            return self._identity_parser.is_reasoning_end(input_ids)

        return super().is_reasoning_end(input_ids)

    defis_reasoning_end_streaming(
        self, input_ids: Sequence[int], delta_ids: Iterable[int]
    ) -> bool:
        if self._identity_parser is not None:
            return self._identity_parser.is_reasoning_end_streaming(
                input_ids, delta_ids
            )

        return super().is_reasoning_end_streaming(input_ids, delta_ids)

    defextract_content_ids(self, input_ids: list[int]) -> list[int]:
        if self._identity_parser is not None:
            return self._identity_parser.extract_content_ids(input_ids)

        return super().extract_content_ids(input_ids)

    defextract_reasoning(
        self, model_output: str, request: "ChatCompletionRequest | ResponsesRequest"
    ) -> tuple[str | None, str | None]:
        if self._identity_parser is not None:
            return self._identity_parser.extract_reasoning(model_output, request)

        return super().extract_reasoning(model_output, request)

    defextract_reasoning_streaming(
        self,
        previous_text: str,
        current_text: str,
        delta_text: str,
        previous_token_ids: Sequence[int],
        current_token_ids: Sequence[int],
        delta_token_ids: Sequence[int],
    ) -> DeltaMessage | None:
        if self._identity_parser is not None:
            return self._identity_parser.extract_reasoning_streaming(
                previous_text,
                current_text,
                delta_text,
                previous_token_ids,
                current_token_ids,
                delta_token_ids,
            )

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