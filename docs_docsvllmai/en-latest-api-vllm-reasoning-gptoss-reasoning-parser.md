---
title: gptoss_reasoning_parser - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/reasoning/gptoss_reasoning_parser/
source: sitemap
fetched_at: 2026-05-07T21:35:00.751440416-03:00
rendered_js: false
word_count: 0
summary: This document defines the reasoning parser implementation for the GptOss model, providing methods for detecting the end of reasoning content in both standard and streaming generation modes.
tags:
    - llm
    - parser
    - reasoning
    - tokenization
    - streaming
    - gpt-oss
    - chat-completion
category: api
---

```
classGptOssReasoningParser(ReasoningParser):
"""
    Reasoning parser for GptOss model.

    The GptOss model uses harmony to extract reasoning content and this parser
    is only used for detecting the end of the reasoning content.
    """

    def__init__(self, tokenizer: PreTrainedTokenizerBase, *args, **kwargs):
        super().__init__(tokenizer, *args, **kwargs)
        # The model can output some special tokens between "final" and "<|message|>"
        # So we need to look for both sequences to determine the end of reasoning.
        self.reasoning_end_token_ids_prefix = self.model_tokenizer.encode(
            "<|channel|>final"
        )
        self.reasoning_end_token_ids_suffix = self.model_tokenizer.encode("<|message|>")
        # We also need to check for the <|end|> token to avoid false positives from
        # previous messages in multi-turn conversations.
        self.eom_token_id = self.vocab["<|end|>"]
        self.reasoning_max_num_between_tokens = 20

    defis_reasoning_end(self, input_ids: Sequence[int]) -> bool:
        end_token_ids_prefix = self.reasoning_end_token_ids_prefix
        end_token_ids_suffix = self.reasoning_end_token_ids_suffix
        assert len(end_token_ids_prefix) > 0, "reasoning_end_token_ids_prefix is empty"
        assert len(end_token_ids_suffix) > 0, "reasoning_end_token_ids_suffix is empty"
        # Check if the end sequence is present in the input_ids.
        # We search from the end of input_ids to find the last match.
        for i in range(len(input_ids) - len(end_token_ids_prefix), -1, -1):
            if input_ids[i] == self.eom_token_id:
                # We looped backwards far enough to find the end of a previous message,
                # which means we have searched the entirety of the current message
                # and can exit early without searching further back into prior
                # messages of the conversation.
                return False
            if input_ids[i : i + len(end_token_ids_prefix)] == end_token_ids_prefix:
                # We have found the prefix, now we look for the suffix after the prefix.
                suffix_start = i + len(end_token_ids_prefix)
                for j in range(
                    suffix_start, len(input_ids) - len(end_token_ids_suffix) + 1
                ):
                    if j - suffix_start >= self.reasoning_max_num_between_tokens:
                        break
                    if (
                        input_ids[j : j + len(end_token_ids_suffix)]
                        == end_token_ids_suffix
                    ):
                        return True
        return False

    defis_reasoning_end_streaming(
        self, input_ids: Sequence[int], delta_ids: Iterable[int]
    ) -> bool:
        # The pattern window covers the end-of-reasoning marker itself.
        # We add len(delta_ids) so that under speculative decoding (where
        # a single step can accept many tokens) the entire accepted chunk
        # is always inside the scan region.
        delta_ids = tuple(delta_ids)
        pattern_len = (
            len(self.reasoning_end_token_ids_prefix)
            + self.reasoning_max_num_between_tokens
            + len(self.reasoning_end_token_ids_suffix)
        )
        window = pattern_len + len(delta_ids)
        n = len(input_ids)
        if n <= window:
            return self.is_reasoning_end(input_ids)
        return self.is_reasoning_end(input_ids[n - window :])

    defextract_content_ids(self, input_ids: list[int]) -> list[int]:
        _, content, _ = parse_chat_output(input_ids)
        if content is None:
            return []
        return self.model_tokenizer.encode(content)

    defextract_reasoning_streaming(
        self,
        previous_text: str,
        current_text: str,
        delta_text: str,
        previous_token_ids: Sequence[int],
        current_token_ids: Sequence[int],
        delta_token_ids: Sequence[int],
    ) -> DeltaMessage | None:
        prev_reasoning, prev_content, _ = parse_chat_output(list(previous_token_ids))
        cur_reasoning, cur_content, _ = parse_chat_output(list(current_token_ids))
        reasoning_delta = None
        content_delta = None
        if cur_reasoning is not None:
            prev_r = prev_reasoning or ""
            if cur_reasoning.startswith(prev_r):
                reasoning_delta = cur_reasoning[len(prev_r) :] or None
            else:
                reasoning_delta = cur_reasoning
        if cur_content is not None:
            prev_c = prev_content or ""
            if cur_content.startswith(prev_c):
                content_delta = cur_content[len(prev_c) :] or None
            else:
                content_delta = cur_content
        if reasoning_delta is None and content_delta is None:
            return None
        return DeltaMessage(reasoning=reasoning_delta, content=content_delta)

    defextract_reasoning(
        self,
        model_output: str,
        request: "ChatCompletionRequest | ResponsesRequest",
    ) -> tuple[str | None, str | None]:
        raise NotImplementedError(
            "gpt-oss has a special branch for parsing reasoning in non-streaming mode. This method shouldn't be used."  # noqa: E501
        )

    # This function prepares the structural tag to format reasoning output
    defprepare_structured_tag(
        self, original_tag: str | None, tool_server: ToolServer | None
    ) -> str | None:
        if original_tag is None:
            if tool_server is None:
                return json.dumps(no_func_reasoning_tag)
            else:
                builtin_tool_list: list[str] = []
                if tool_server.has_tool("browser"):
                    builtin_tool_list.append("browser")
                if tool_server.has_tool("python"):
                    builtin_tool_list.append("python")
                if tool_server.has_tool("container"):
                    builtin_tool_list.append("container")

                if len(builtin_tool_list) > 0:
                    logger.info("Builtin_tool_list: %s", builtin_tool_list)
                    func_tag = json.dumps(
                        tag_with_builtin_funcs(no_func_reasoning_tag, builtin_tool_list)
                    )
                else:
                    logger.info("Builtin_tool_list is empty")
                    func_tag = json.dumps(no_func_reasoning_tag)

                return func_tag
        else:
            # There is potential risk for appending the tag to the original tag
            return original_tag
```