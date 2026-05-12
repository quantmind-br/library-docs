---
title: deepseek_v32 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/tokenizers/deepseek_v32/
source: sitemap
fetched_at: 2026-05-07T21:35:35.97704493-03:00
rendered_js: false
word_count: 20
summary: This document describes the implementation of a utility function that wraps standard Hugging Face tokenizers to support the specific chat template encoding and message formatting requirements of DeepSeek V3.2.
tags:
    - vllm
    - tokenizer
    - deepseek
    - chat-template
    - natural-language-processing
    - python-api
category: api
---

## vllm.tokenizers.deepseek\_v32 [¶](#vllm.tokenizers.deepseek_v32 "Permanent link")

## get\_deepseek\_v32\_tokenizer [¶](#vllm.tokenizers.deepseek_v32.get_deepseek_v32_tokenizer "Permanent link")

```
get_deepseek_v32_tokenizer(
    tokenizer: HfTokenizer,
) -> HfTokenizer
```

Wraps a tokenizer to use the custom DeepSeek V3.2 chat template encoding.

Source code in `vllm/tokenizers/deepseek_v32.py`

```
defget_deepseek_v32_tokenizer(tokenizer: HfTokenizer) -> HfTokenizer:
"""
    Wraps a tokenizer to use the custom DeepSeek V3.2 chat template encoding.
    """
    dsv32_tokenizer = copy.copy(tokenizer)

    added_vocab = tokenizer.get_added_vocab()
    added_vocab_size = len(added_vocab)
    tokenizer_vocab_size = tokenizer.vocab_size

    class_DeepseekV32Tokenizer(tokenizer.__class__):  # type: ignore
        defapply_chat_template(
            self,
            messages: list["ChatCompletionMessageParam"],
            tools: list[dict[str, Any]] | None = None,
            **kwargs,
        ) -> str | list[int]:
            thinking = kwargs.get("thinking", False)
            enable_thinking = kwargs.get("enable_thinking", False)
            thinking = thinking or enable_thinking
            thinking_mode = "thinking"
            if not thinking:
                thinking_mode = "chat"
            conversation = kwargs.get("conversation", messages)
            messages = conversation.copy()
            if tools is not None and len(tools) > 0:
                messages.insert(0, {"role": "system"})
                messages[0]["tools"] = tools  # type: ignore[typeddict-unknown-key]

            # Historical reasoning content is dropped when a new user message
            # is introduced
            drop_thinking = messages[-1]["role"] == "user"

            encode_config = dict(
                thinking_mode=thinking_mode, drop_thinking=drop_thinking
            )

            prompt_str = encode_messages(messages, **encode_config)  # type: ignore

            if kwargs.get("tokenize", True):
                tokenizer_kwargs = {
                    k: kwargs[k] for k in ("truncation", "max_length") if k in kwargs
                }
                return self.encode(
                    prompt_str,
                    add_special_tokens=False,
                    **tokenizer_kwargs,
                )

            return prompt_str

        defnum_special_tokens_to_add(self) -> int:
            return len(self.encode(""))

        def__len__(self) -> int:
            # </think> is an added token in DeepseekV32 tokenizer
            return tokenizer_vocab_size + added_vocab_size

        defget_added_vocab(self) -> dict[str, int]:
            return added_vocab.copy()

        def__reduce__(self):
            return get_deepseek_v32_tokenizer, (tokenizer,)

    _DeepseekV32Tokenizer.__name__ = f"DSV32{tokenizer.__class__.__name__}"

    dsv32_tokenizer.__class__ = _DeepseekV32Tokenizer
    return dsv32_tokenizer
```