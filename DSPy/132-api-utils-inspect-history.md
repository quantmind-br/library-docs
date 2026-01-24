---
title: inspect_history - DSPy
url: https://dspy.ai/api/utils/inspect_history/
source: sitemap
fetched_at: 2026-01-23T08:03:03.923615227-03:00
rendered_js: false
word_count: 21
summary: This document describes the inspect_history utility in DSPy, which allows users to view the global history of interactions across all language models.
tags:
    - dspy
    - inspect-history
    - lm-history
    - debugging
    - llm-tracking
category: api
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/utils/inspect_history.md "Edit this page")

## `dspy.inspect_history(n: int = 1)` [¶](#dspy.inspect_history "Permanent link")

The global history shared across all LMs.

Source code in `dspy/clients/base_lm.py`

```
definspect_history(n: int = 1):
"""The global history shared across all LMs."""
    return pretty_print_history(GLOBAL_HISTORY, n)
```

:::