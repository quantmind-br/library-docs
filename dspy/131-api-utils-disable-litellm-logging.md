---
title: disable_litellm_logging - DSPy
url: https://dspy.ai/api/utils/disable_litellm_logging/
source: sitemap
fetched_at: 2026-01-23T08:02:59.122982864-03:00
rendered_js: false
word_count: 11
summary: This document describes the dspy.disable_litellm_logging function, which suppresses debug information and sets the LiteLLM logging level to error-only.
tags:
    - dspy
    - litellm
    - logging
    - configuration
    - debugging
category: api
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/utils/disable_litellm_logging.md "Edit this page")

## `dspy.disable_litellm_logging()` [¶](#dspy.disable_litellm_logging "Permanent link")

Source code in `dspy/clients/__init__.py`

```
defdisable_litellm_logging():
    litellm.suppress_debug_info = True
    configure_litellm_logging("ERROR")
```

:::