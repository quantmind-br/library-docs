---
title: logging_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/logging_utils/
source: sitemap
fetched_at: 2026-05-07T21:22:20.912355183-03:00
rendered_js: false
word_count: 7
summary: This document provides a utility function to generate a customized logging configuration dictionary for Uvicorn, specifically enabling the filtering of access logs for defined URL paths.
tags:
    - uvicorn
    - logging-configuration
    - python-api
    - access-logs
    - log-filtering
category: api
---

```
defcreate_uvicorn_log_config(
    excluded_paths: list[str] | None = None,
    log_level: str = "info",
) -> dict:
"""
    Create a uvicorn logging configuration with access log filtering.

    This function generates a logging configuration dictionary that can be
    passed to uvicorn's `log_config` parameter. It sets up the access log
    filter to exclude specified paths.

    Args:
        excluded_paths: List of URL paths to exclude from access logs.
        log_level: The log level for uvicorn loggers.

    Returns:
        A dictionary containing the logging configuration.

    Example:
        >>> config = create_uvicorn_log_config(["/health", "/metrics"])
        >>> uvicorn.run(app, log_config=config)
    """
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {
            "access_log_filter": {
                "()": UvicornAccessLogFilter,
                "excluded_paths": excluded_paths or [],
            },
        },
        "formatters": {
            "default": {
                "()": "uvicorn.logging.DefaultFormatter",
                "fmt": "%(levelprefix)s%(message)s",
                "use_colors": None,
            },
            "access": {
                "()": "uvicorn.logging.AccessFormatter",
                "fmt": '%(levelprefix)s%(client_addr)s - "%(request_line)s" %(status_code)s',  # noqa: E501
            },
        },
        "handlers": {
            "default": {
                "formatter": "default",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stderr",
            },
            "access": {
                "formatter": "access",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "filters": ["access_log_filter"],
            },
        },
        "loggers": {
            "uvicorn": {
                "handlers": ["default"],
                "level": log_level.upper(),
                "propagate": False,
            },
            "uvicorn.error": {
                "level": log_level.upper(),
                "handlers": ["default"],
                "propagate": False,
            },
            "uvicorn.access": {
                "handlers": ["access"],
                "level": log_level.upper(),
                "propagate": False,
            },
        },
    }
    return config
```