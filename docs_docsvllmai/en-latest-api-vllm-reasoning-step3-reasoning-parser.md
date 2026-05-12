---
title: step3_reasoning_parser - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/reasoning/step3_reasoning_parser/
source: sitemap
fetched_at: 2026-05-07T21:35:13.889538403-03:00
rendered_js: false
word_count: 0
summary: This document defines a reasoning parser class for the Step3 model, which extracts and separates reasoning content from final output using the <think> and </think> delimiters.
tags:
    - python
    - nlp
    - token-parsing
    - machine-learning
    - text-processing
    - llm-inference
category: reference
---

```
classStep3ReasoningParser(ReasoningParser):
"""
    Reasoning parser for Step3 model.

    The Step3 model uses </think> token to denote the end of reasoning
    text. This parser extracts all content before </think> as reasoning content.
    """

    def__init__(self, tokenizer: PreTrainedTokenizerBase, *args, **kwargs):
        super().__init__(tokenizer, *args, **kwargs)
        self.think_start_token = "<think>"
        self.think_end_token = "</think>"

        self.reasoning_regex = re.compile(rf"(.*?){self.think_end_token}", re.DOTALL)

        if not self.model_tokenizer:
            raise ValueError(
                "The model tokenizer must be passed to the ReasoningParser "
                "constructor during construction."
            )

        think_end_token_id = self.vocab.get(self.think_end_token)
        if think_end_token_id is None:
            raise RuntimeError(
                "Step3 reasoning parser could not locate think end "
                "token in the tokenizer!"
            )
        self.think_end_token_id: int = think_end_token_id

    @property
    defreasoning_start_str(self) -> str:
        return self.think_start_token

    @property
    defreasoning_end_str(self) -> str:
        return self.think_end_token

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
        Extract reasoning content from a delta message.
        Handles streaming output where previous + delta = current.
        Uses token IDs for faster processing.
        For text "abc</think>xyz":
        - 'abc' goes to reasoning
        - 'xyz' goes to content
        """
        # Skip single special token
        if len(delta_token_ids) == 1 and delta_token_ids[0] == self.think_end_token_id:
            return None

        if self.think_end_token_id in delta_token_ids:
            # </think> in delta, extract reasoning content and remaining content
            end_index = delta_text.find(self.think_end_token)
            reasoning = delta_text[:end_index]
            content = delta_text[end_index + len(self.think_end_token) :]
            return DeltaMessage(
                reasoning=reasoning,
                content=content if content else None,
            )
        elif self.think_end_token_id in previous_token_ids:
            # </think> already seen in previous text, everything is content
            return DeltaMessage(content=delta_text)
        else:
            # No </think> seen yet, everything is reasoning
            return DeltaMessage(reasoning=delta_text)

    defextract_reasoning(
        self, model_output: str, request: "ChatCompletionRequest | ResponsesRequest"
    ) -> tuple[str | None, str | None]:
        # Check if the model output contains the </think> token
        if self.think_end_token not in model_output:
            # If no </think> token, everything is reasoning content
            return model_output, None
        else:
            # Find the first occurrence of </think>
            end_index = model_output.find(self.think_end_token)
            reasoning = model_output[:end_index]

            # Content after </think> token
            content = model_output[end_index + len(self.think_end_token) :] or None

            return reasoning, content

    defis_reasoning_end(self, input_ids: Sequence[int]) -> bool:
        return self.think_end_token_id in input_ids

    defis_reasoning_end_streaming(
        self, input_ids: Sequence[int], delta_ids: Iterable[int]
    ) -> bool:
        end_token_id = self.think_end_token_id
        return end_token_id in delta_ids

    defextract_content_ids(self, input_ids: list[int]) -> list[int]:
        if self.think_end_token_id not in islice(
            input_ids, 0, max(0, len(input_ids) - 1)
        ):
            return []
        else:
            return input_ids[input_ids.index(self.think_end_token_id) + 1 :]
```