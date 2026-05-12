---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/quark/utils/
source: sitemap
fetched_at: 2026-05-07T21:27:41.13977185-03:00
rendered_js: false
word_count: 39
summary: This function provides a utility to evaluate string equality, regex pattern matching, or substring containment for configuration or layer validation.
tags:
    - utility-function
    - regex-matching
    - string-comparison
    - vllm-framework
    - quantization-utils
category: reference
---

Checks whether a value is exactly equal or a regex match for target if target starts with 're:'. If check\_contains is set to True, additionally checks if the target string is contained within the value.

Source code in `vllm/model_executor/layers/quantization/quark/utils.py`

```
def_is_equal_or_regex_match(
    value: str, target: str, check_contains: bool = False
) -> bool:
"""
    Checks whether a value is exactly equal or a regex match for target
    if target starts with 're:'. If check_contains is set to True,
    additionally checks if the target string is contained within the value.
    """

    if target.startswith("re:"):
        pattern = target[3:]
        if re.match(pattern, value):
            return True
    elif check_contains:
        if target.lower() in value.lower():
            return True
    elif target == value:
        return True
    return False
```