---
title: enable_litellm_logging - DSPy
url: https://dspy.ai/api/utils/enable_litellm_logging/
source: sitemap
fetched_at: 2026-01-23T08:03:01.552798467-03:00
rendered_js: false
word_count: 11
summary: This utility function enables detailed logging for LiteLLM within the DSPy framework by setting the log level to DEBUG and unsuppressing debug information.
tags:
    - dspy
    - litellm
    - logging
    - debugging
    - api-utility
category: api
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/utils/enable_litellm_logging.md "Edit this page")

## `dspy.enable_litellm_logging()` [¶](#dspy.enable_litellm_logging "Permanent link")

Source code in `dspy/clients/__init__.py`

```
defenable_litellm_logging():
    litellm.suppress_debug_info = False
    configure_litellm_logging("DEBUG")
```

:::