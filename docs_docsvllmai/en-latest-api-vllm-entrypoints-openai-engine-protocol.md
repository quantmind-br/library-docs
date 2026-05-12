---
title: protocol - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/openai/engine/protocol/
source: sitemap
fetched_at: 2026-05-07T21:20:01.776517051-03:00
rendered_js: false
word_count: 14
summary: This document defines a custom exception class used to handle internal server errors encountered during the generation process in the vLLM OpenAI-compatible engine.
tags:
    - python-exception
    - error-handling
    - vllm
    - openai-protocol
    - server-error
category: reference
---

Bases: `Exception`

raised when finish\_reason indicates internal server error (500)

Source code in `vllm/entrypoints/openai/engine/protocol.py`

```
classGenerationError(Exception):
"""raised when finish_reason indicates internal server error (500)"""

    def__init__(self, message: str = "Internal server error"):
        super().__init__(message)
        self.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
```