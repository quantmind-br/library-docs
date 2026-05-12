---
title: mistral - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/utils/mistral/
source: sitemap
fetched_at: 2026-05-07T21:38:45.275868297-03:00
rendered_js: false
word_count: 71
summary: This document outlines utility functions for verifying Mistral-specific tokenizers and tool parsers using lazy-loaded class attribute checks to optimize performance.
tags:
    - vllm
    - mistral
    - tokenizer
    - type-checking
    - lazy-loading
    - utility-functions
category: reference
---

## vllm.utils.mistral [¶](#vllm.utils.mistral "Permanent link")

Provides lazy import of the vllm.tokenizers.mistral module.

## is\_mistral\_tokenizer [¶](#vllm.utils.mistral.is_mistral_tokenizer "Permanent link")

```
is_mistral_tokenizer(
    obj: TokenizerLike | None,
) -> TypeGuard[MistralTokenizer]
```

Return true if the tokenizer is a MistralTokenizer instance.

Source code in `vllm/utils/mistral.py`

```
defis_mistral_tokenizer(obj: TokenizerLike | None) -> TypeGuard[mt.MistralTokenizer]:
"""Return true if the tokenizer is a MistralTokenizer instance."""
    cls = type(obj)
    # Check for special class attribute, this avoids importing the class to
    # do an isinstance() check.  If the attribute is True, do an isinstance
    # check to be sure we have the correct type.
    return bool(
        getattr(cls, "IS_MISTRAL_TOKENIZER", False)
        and isinstance(obj, mt.MistralTokenizer)
    )

is_mistral_tool_parser(cls: type | None) -> bool
```

Return true if *cls* is (a subclass of) MistralToolParser.

Uses a class attribute check so that importing `vllm.tool_parsers.mistral_tool_parser` — and transitively `mistral_common` — is not required.

Source code in `vllm/utils/mistral.py`

```
defis_mistral_tool_parser(cls: type | None) -> bool:
"""Return true if *cls* is (a subclass of) MistralToolParser.

    Uses a class attribute check so that importing
    ``vllm.tool_parsers.mistral_tool_parser`` — and transitively
    ``mistral_common`` — is not required.
    """
    return bool(
        getattr(cls, "IS_MISTRAL_TOOL_PARSER", False)
        and issubclass(cls, mtp.MistralToolParser)  # type: ignore[arg-type]
    )
```