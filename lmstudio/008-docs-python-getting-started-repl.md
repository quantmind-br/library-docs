---
title: Using `lmstudio-python` in REPL
url: https://lmstudio.ai/docs/python/getting-started/repl
source: sitemap
fetched_at: 2026-04-07T21:30:56.844783164-03:00
rendered_js: false
word_count: 124
summary: This document describes the convenience API offered by lmstudio-python, which utilizes atexit hooks to manage resources for simplified interactive use across multiple commands.
tags:
    - lmstudio-python
    - convenience-api
    - interactive-use
    - atexit-hooks
    - client-session
category: guide
---

To simplify interactive use, `lmstudio-python` offers a convenience API which manages its resources via `atexit` hooks, allowing a default synchronous client session to be used across multiple interactive commands.

This convenience API is shown in the examples throughout the documentation as the `Python (convenience API)` tab (alongside the `Python (scoped resource API)` examples, which use `with` statements to ensure deterministic cleanup of network communication resources).

The convenience API allows the standard Python REPL, or more flexible alternatives like Juypter Notebooks, to be used to interact with AI models loaded into LM Studio. For example:

While not primarily intended for use this way, the SDK's asynchronous structured concurrency API is compatible with the asynchronous Python REPL that is launched by `python -m asyncio`. For example: