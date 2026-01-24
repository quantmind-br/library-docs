---
title: enable_logging - DSPy
url: https://dspy.ai/api/utils/enable_logging/
source: sitemap
fetched_at: 2026-01-23T08:03:01.659570868-03:00
rendered_js: false
word_count: 32
summary: This document describes the enable_logging function in DSPy, which activates the logging stream to emit event logs from internal APIs.
tags:
    - dspy
    - logging
    - event-logging
    - python-utilities
    - debugging
category: api
---

Enables the `DSPyLoggingStream` used by event logging APIs throughout DSPy (`eprint()`, `logger.info()`, etc), emitting all subsequent event logs. This reverses the effects of `disable_logging()`.

Source code in `dspy/utils/logging_utils.py`

```
defenable_logging():
"""
    Enables the `DSPyLoggingStream` used by event logging APIs throughout DSPy
    (`eprint()`, `logger.info()`, etc), emitting all subsequent event logs. This
    reverses the effects of `disable_logging()`.
    """
    DSPY_LOGGING_STREAM.enabled = True
```