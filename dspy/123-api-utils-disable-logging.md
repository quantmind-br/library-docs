---
title: disable_logging - DSPy
url: https://dspy.ai/api/utils/disable_logging/
source: sitemap
fetched_at: 2026-01-23T08:03:00.179469143-03:00
rendered_js: false
word_count: 26
summary: Explains how to disable the internal DSPy event logging stream to silence all subsequent event logs from the library.
tags:
    - dspy
    - logging
    - event-logs
    - utilities
    - configuration
category: api
---

Disables the `DSPyLoggingStream` used by event logging APIs throughout DSPy (`eprint()`, `logger.info()`, etc), silencing all subsequent event logs.

Source code in `dspy/utils/logging_utils.py`

```
defdisable_logging():
"""
    Disables the `DSPyLoggingStream` used by event logging APIs throughout DSPy
    (`eprint()`, `logger.info()`, etc), silencing all subsequent event logs.
    """
    DSPY_LOGGING_STREAM.enabled = False
```