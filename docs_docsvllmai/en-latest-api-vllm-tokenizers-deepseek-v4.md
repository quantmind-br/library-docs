---
title: deepseek_v4 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/tokenizers/deepseek_v4/
source: sitemap
fetched_at: 2026-05-07T21:35:37.814168452-03:00
rendered_js: false
word_count: 20
summary: This document describes the utility function used to wrap Hugging Face tokenizers with a custom class tailored for DeepSeek V4 chat template encoding and reasoning features.
tags:
    - tokenizer
    - deepseek-v4
    - chat-template
    - vllm
    - nlp
    - encoding
category: api
---

## vllm.tokenizers.deepseek\_v4 [¶](#vllm.tokenizers.deepseek_v4 "Permanent link")

## get\_deepseek\_v4\_tokenizer [¶](#vllm.tokenizers.deepseek_v4.get_deepseek_v4_tokenizer "Permanent link")

```
get_deepseek_v4_tokenizer(
    tokenizer: HfTokenizer,
) -> HfTokenizer
```

Wraps a tokenizer to use the custom DeepSeek V4 chat template encoding.

Source code in `vllm/tokenizers/deepseek_v4.py`

```
defget_deepseek_v4_tokenizer(tokenizer: HfTokenizer) -> HfTokenizer:
"""
    Wraps a tokenizer to use the custom DeepSeek V4 chat template encoding.
    """
    dsv4_tokenizer = copy.copy(tokenizer)

    added_vocab = tokenizer.get_added_vocab()
    added_vocab_size = len(added_vocab)
    tokenizer_vocab_size = tokenizer.vocab_size

    class_DeepseekV4Tokenizer(tokenizer.__class__):  # type: ignore
        defapply_chat_template(
            self,
            messages: list["ChatCompletionMessageParam"],
            tools: list[dict[str, Any]] | None = None,
            **kwargs,
        ) -> str | list[int]:
            thinking = kwargs.get("thinking", False)
            enable_thinking = kwargs.get("enable_thinking", False)
            thinking = thinking or enable_thinking
            thinking_mode = "thinking" if thinking else "chat"

            conversation = kwargs.get("conversation", messages)
            messages = conversation.copy()
            if tools is not None and len(tools) > 0:
                messages.insert(0, {"role": "system"})
                messages[0]["tools"] = tools  # type: ignore[typeddict-unknown-key]

            reasoning_effort = kwargs.get("reasoning_effort")
            if not isinstance(reasoning_effort, str):
                reasoning_effort = None
            elif reasoning_effort == "none":
                thinking_mode = "chat"
                reasoning_effort = None
            elif reasoning_effort in ("max", "xhigh"):
                reasoning_effort = "max"
            else:
                reasoning_effort = "high"

            encode_config = dict(
                thinking_mode=thinking_mode,
                drop_thinking=kwargs.get("drop_thinking", True),
                reasoning_effort=reasoning_effort,
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
            return tokenizer_vocab_size + added_vocab_size

        defget_added_vocab(self) -> dict[str, int]:
            return added_vocab.copy()

        def__reduce__(self):
            return get_deepseek_v4_tokenizer, (tokenizer,)

    _DeepseekV4Tokenizer.__name__ = f"DSV4{tokenizer.__class__.__name__}"

    dsv4_tokenizer.__class__ = _DeepseekV4Tokenizer
    return dsv4_tokenizer
```