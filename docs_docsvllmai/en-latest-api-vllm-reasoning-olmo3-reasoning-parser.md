---
title: olmo3_reasoning_parser - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/reasoning/olmo3_reasoning_parser/
source: sitemap
fetched_at: 2026-05-07T21:35:10.142258232-03:00
rendered_js: false
word_count: 20
summary: This document defines the Olmo3ReasoningParser class, which identifies and separates reasoning traces encapsulated in <think> tags from main content in model outputs for both streaming and non-streaming modes.
tags:
    - olmo-3
    - reasoning-parser
    - token-extraction
    - streaming-inference
    - nlp-tools
category: api
---

```
classOlmo3ReasoningParser(ReasoningParser):
"""
    Reasoning parser for Olmo 3 model

    Olmo3ReasoningParser

    This class implements a reasoning parser specifically designed for the
    Olmo 3 family of models. Olmo 3 models do not use special tokens to
    indicate reasoning; rather, reasoning trace is wrapped in `<think>` and
    `</think>`, which are tokenized using standard vocabulary entries.
    Because of this, the parser operates in string space, accumulating the
    characters in a buffer until it sees `<think>` or `</think>`. tokens
    to switch modes.

    Key Features:
        - For non-stream output, Recognizes and extracts reasoning (text
          bracketed by `<think>` and `</think>`) and content (everything
          after the first `</think>`).
        - For stream process, it uses a buffer to accumulate delta text,
          and output progressive delta messages as soon as thinking starts
          or ends.
        - For reliability, some Olmo 3 models may hardcode the first
          `<think>` token is the input text (similar to Deepseek R1,
          or reasoning-only Qwen models). To support such variants, the
          parser can optionally work in cases where the first `<think>`
          token is missing from generation.
    """

    think_start: str = r"<think>"
    think_end: str = r"</think>"
    # </think> is split in 3 by the pre-tokenizer, first split can be tokenized
    # with an optional leading space, so there are 2 possible tokenizations
    think_end_first_split: list[str] = [r"Ġ</", r"</"]
    think_end_rest_split: list[str] = [r"think", r">"]
    # notice that the first think is optional; this allows template to
    # work in cases when we hardcode a <think> at the beginning of the
    # reasoning template.
    reasoning_regex: re.Pattern = re.compile(
        rf"^(?:{think_start})?(?P<reasoning>.*?)"
        rf"{think_end}(?P<content>.*)$",
        re.DOTALL,
    )

    def__init__(self, tokenizer: "TokenizerLike", *args, **kwargs):
        super().__init__(tokenizer, *args, **kwargs)
        self.buffer = Olmo3ReasoningBuffer(
            think_start=self.think_start, think_end=self.think_end
        )
        self.think_end_first_token_ids: list[int] = [
            self.vocab[token] for token in self.think_end_first_split
        ]
        self.think_end_rest_token_ids: list[int] = [
            self.vocab[token] for token in self.think_end_rest_split
        ]

    @property
    defreasoning_start_str(self) -> str:
        return self.think_start

    @property
    defreasoning_end_str(self) -> str:
        return self.think_end

    defis_reasoning_end(self, input_ids: Sequence[int]) -> bool:
        rest_ids = self.think_end_rest_token_ids
        rest_len = len(rest_ids)
        for i in range(len(input_ids) - rest_len, -1, -1):
            if (
                list(input_ids[i + 1 : i + 1 + rest_len]) == rest_ids
                and input_ids[i] in self.think_end_first_token_ids
            ):
                return True
        return False

    defextract_content_ids(self, input_ids: list[int]) -> list[int]:
        # for Olmo 3 streaming reason parsing, the stream parse
        # will call first, and the same token will be called in
        # is_reasoning_end and extract_content_ids
        # this id is not part of content, so just return [] here.
        return []

    defextract_reasoning(
        self,
        model_output: str,
        request: "ChatCompletionRequest | ResponsesRequest",
    ) -> tuple[str | None, str | None]:
"""Extract the reasoning content & content sections, respectively.
        If the sequence doesn't match what we expect, i.e., the model generates
        something else, all content is considered non-reasoning content.

        Args:
            model_output: Output of the model to be parsed.
            request: Request being
                processed.

        Returns:
            tuple[Optional[str], Optional[str]]: Tuple pair containing the
            reasoning content and non-reasoning content.
        """

        re_match = self.reasoning_regex.match(model_output)
        if re_match:
            reasoning = re_match.group("reasoning") or None
            content = re_match.group("content") or None
            return reasoning, content

        # no reasoning content
        return None, model_output

    defextract_reasoning_streaming(
        self,
        previous_text: str,
        current_text: str,
        delta_text: str,
        previous_token_ids: Sequence[int],
        current_token_ids: Sequence[int],
        delta_token_ids: Sequence[int],
    ) -> DeltaMessage | None:
"""Extract content using token ID sequence state machine"""

        delta_message = self.buffer.add_text(delta_text)
        if delta_message is None and self.buffer.think_end in self.buffer.buffer:
            # this is a bit hacky, but, because of how the buffer is
            # constructed, if the last delta_text contains characters that
            # marks the end of thinking tokens, then messages in the buffer
            # would never be processed because we get no other turn. To get
            # around that, we check if the text buffer contains the end of
            # thinking tokens, and, if so, we reprocess the buffer again.
            delta_message = self.buffer.process_buffer()

        return delta_message
```