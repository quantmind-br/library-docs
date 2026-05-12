---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/core/sched/utils/
source: sitemap
fetched_at: 2026-05-07T21:40:27.205617877-03:00
rendered_js: false
word_count: 184
summary: This document provides utility functions for detecting token repetition patterns in sequences and performing optimized list element removal for scheduling operations.
tags:
    - repetition-detection
    - token-processing
    - list-optimization
    - utility-functions
    - sequence-analysis
category: reference
---

## vllm.v1.core.sched.utils [¶](#vllm.v1.core.sched.utils "Permanent link")

## \_has\_repeating\_pattern [¶](#vllm.v1.core.sched.utils._has_repeating_pattern "Permanent link")

Check if the tail of token\_ids contains a repeating pattern.

Compares the last pattern\_len tokens against the preceding (repetition\_min\_count - 1) repetitions of the same length.

Source code in `vllm/v1/core/sched/utils.py`

```
def_has_repeating_pattern(
    token_ids: Sequence[int],
    pattern_len: int,
    repetition_min_count: int,
) -> bool:
"""Check if the tail of token_ids contains a repeating pattern.

    Compares the last pattern_len tokens against the preceding
    (repetition_min_count - 1) repetitions of the same length.
    """
    for n in range(1, pattern_len + 1):
        target_token = token_ids[-n]
        for m in range(1, repetition_min_count):
            if token_ids[-(pattern_len * m + n)] != target_token:
                return False
    return True
```

## check\_sequence\_repetition [¶](#vllm.v1.core.sched.utils.check_sequence_repetition "Permanent link")

Check if a sequence of token IDs has a repetition pattern. Args: token\_ids: List of token IDs params: Repetition detection parameters. Returns: True if a repetition pattern is found, False otherwise.

Source code in `vllm/v1/core/sched/utils.py`

```
defcheck_sequence_repetition(
    token_ids: Sequence[int],
    params: RepetitionDetectionParams,
) -> bool:
"""Check if a sequence of token IDs has a repetition pattern.
    Args:
        token_ids: List of token IDs
        params: Repetition detection parameters.
    Returns:
        True if a repetition pattern is found, False otherwise.
    """
    max_pattern_size = params.max_pattern_size
    min_pattern_size = params.min_pattern_size
    min_count = params.min_count

    if min_pattern_size <= 0:
        min_pattern_size = 1

    if max_pattern_size <= 0 or min_count < 2 or min_pattern_size > max_pattern_size:
        return False

    for pattern_len in range(
        min_pattern_size,
        max_pattern_size + 1,
    ):
        if pattern_len * min_count > len(token_ids):
            return False

        if _has_repeating_pattern(token_ids, pattern_len, min_count):
            return True

    return False
```

## remove\_all [¶](#vllm.v1.core.sched.utils.remove_all "Permanent link")

Remove all items from a list that are in the items\_to\_remove set.

This method optimizes for the common case of removing a single item, falling back to list comprehension for multiple items.

Parameters:

Name Type Description Default `lst` `list`

The list to remove items from

*required* `items_to_remove` `set`

Set of items to remove

*required*

Returns:

Type Description `list`

Either the modified original list (for single item removal) or

`list`

a new list (for multiple item removal). Callers should use the

`list`

returned value.

Note

For single item removal, this modifies the original list in-place and returns it. For multiple items, it creates and returns a new list.

Source code in `vllm/v1/core/sched/utils.py`

```
defremove_all(lst: list, items_to_remove: set) -> list:
"""Remove all items from a list that are in the items_to_remove set.

    This method optimizes for the common case of removing a single item,
    falling back to list comprehension for multiple items.

    Args:
        lst: The list to remove items from
        items_to_remove: Set of items to remove

    Returns:
        Either the modified original list (for single item removal) or
        a new list (for multiple item removal). Callers should use the
        returned value.

    Note:
        For single item removal, this modifies the original list in-place
        and returns it. For multiple items, it creates and returns a new list.
    """
    if not items_to_remove:
        return lst

    if len(items_to_remove) == 1:
        # Fast path for single item removal (most common case)
        item = next(iter(items_to_remove))
        with contextlib.suppress(ValueError):
            lst.remove(item)
        return lst
    # For multiple items, use list comprehension
    return [item for item in lst if item not in items_to_remove]
```