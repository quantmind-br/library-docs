---
title: Handling Aborts
url: https://lmstudio.ai/docs/typescript/plugins/prompt-preprocessor/handling-aborts
source: sitemap
fetched_at: 2026-04-07T21:32:24.827708651-03:00
rendered_js: false
word_count: 37
summary: This document informs developers that they must gracefully handle an abortion event by checking for and responding to the `ctl.abortSignal` when a user cancels a running prediction generation.
tags:
    - prediction-generation
    - abort-signal
    - user-control
    - api-handling
category: guide
---

A prediction may be aborted by the user while your generator is still running. In such cases, you should handle the abort gracefully by handling the `ctl.abortSignal`.

You can learn more about `AbortSignal` in the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal).