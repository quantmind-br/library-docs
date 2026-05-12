---
title: formatter - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/logging_utils/formatter/
source: sitemap
fetched_at: 2026-05-07T21:22:24.12649333-03:00
rendered_js: false
word_count: 43
summary: This document defines a Python class that extends logging formatters to provide ANSI color-coded terminal output based on log severity levels.
tags:
    - python-logging
    - ansi-colors
    - terminal-output
    - log-formatter
    - developer-tools
category: reference
---

Bases: `NewLineFormatter`

Adds ANSI color codes to log levels for terminal output.

This formatter adds colors by injecting them into the format string for static elements (timestamp, filename, line number) and modifying the levelname attribute for dynamic color selection.

Source code in `vllm/logging_utils/formatter.py`

```
classColoredFormatter(NewLineFormatter):
"""Adds ANSI color codes to log levels for terminal output.

    This formatter adds colors by injecting them into the format string for
    static elements (timestamp, filename, line number) and modifying the
    levelname attribute for dynamic color selection.
    """

    # ANSI color codes
    COLORS = {
        "DEBUG": "\033[37m",  # White
        "INFO": "\033[32m",  # Green
        "WARNING": "\033[33m",  # Yellow
        "ERROR": "\033[31m",  # Red
        "CRITICAL": "\033[35m",  # Magenta
    }
    GREY = "\033[90m"  # Grey for timestamp and file info
    RESET = "\033[0m"

    def__init__(self, fmt, datefmt=None, style="%"):
        # Inject grey color codes into format string for timestamp and file info
        if fmt:
            # Wrap %(asctime)s with grey
            fmt = fmt.replace("%(asctime)s", f"{self.GREY}%(asctime)s{self.RESET}")
            # Wrap [%(fileinfo)s:%(lineno)d] with grey
            fmt = fmt.replace(
                "[%(fileinfo)s:%(lineno)d]",
                f"{self.GREY}[%(fileinfo)s:%(lineno)d]{self.RESET}",
            )

        # Call parent __init__ with potentially modified format string
        super().__init__(fmt, datefmt, style)

    defformat(self, record):
        # Store original levelname to restore later (in case record is reused)
        orig_levelname = record.levelname

        # Only modify levelname - it needs dynamic color based on severity
        if (color_code := self.COLORS.get(record.levelname)) is not None:
            record.levelname = f"{color_code}{record.levelname}{self.RESET}"

        # Call parent format which will handle everything else
        msg = super().format(record)

        # Restore original levelname
        record.levelname = orig_levelname

        return msg
```