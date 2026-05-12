---
title: qwen_vl - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/tokenizers/qwen_vl/
source: sitemap
fetched_at: 2026-05-07T21:35:47.049148031-03:00
rendered_js: false
word_count: 45
summary: This document describes the utility function used to patch the Qwen-VL tokenizer by removing image pad token logic to ensure proper integration within the vLLM framework.
tags:
    - vllm
    - tokenizer
    - qwen-vl
    - tokenization-patch
    - natural-language-processing
category: api
---

## vllm.tokenizers.qwen\_vl [¶](#vllm.tokenizers.qwen_vl "Permanent link")

## get\_qwen\_vl\_tokenizer [¶](#vllm.tokenizers.qwen_vl.get_qwen_vl_tokenizer "Permanent link")

```
get_qwen_vl_tokenizer(
    tokenizer: HfTokenizer,
) -> HfTokenizer
```

The logic of adding image pad tokens should only be applied in `QwenVLProcessor`, so they are patched out here.

The definition of the wrapped tokenizer can be found here: https://huggingface.co/Qwen/Qwen-VL/blob/main/tokenization\_qwen.py

Source code in `vllm/tokenizers/qwen_vl.py`

```
defget_qwen_vl_tokenizer(tokenizer: HfTokenizer) -> HfTokenizer:
"""
    The logic of adding image pad tokens should only be applied in
    `QwenVLProcessor`, so they are patched out here.

    The definition of the wrapped tokenizer can be found here:
    https://huggingface.co/Qwen/Qwen-VL/blob/main/tokenization_qwen.py
    """
    new_tokenizer = copy.copy(tokenizer)

    classTokenizerWithoutImagePad(tokenizer.__class__):  # type: ignore
        deftokenize(
            self,
            text: str,
            allowed_special: Set[str] | str = "all",
            disallowed_special: Collection[str] | str = (),
            **kwargs,
        ) -> list[bytes | str]:
            text = unicodedata.normalize("NFC", text)

            return [
                self.decoder[t]
                for t in self.tokenizer.encode(
                    text,
                    allowed_special=allowed_special,
                    disallowed_special=disallowed_special,
                )
            ]

        def_decode(
            self,
            token_ids: int | list[int],
            skip_special_tokens: bool = False,
            errors: str | None = None,
            **kwargs,
        ) -> str:
            if isinstance(token_ids, int):
                token_ids = [token_ids]

            return self.tokenizer.decode(
                token_ids,
                errors=errors or self.errors,
            )

    TokenizerWithoutImagePad.__name__ = f"{tokenizer.__class__.__name__}WithoutImagePad"

    new_tokenizer.__class__ = TokenizerWithoutImagePad
    return new_tokenizer
```