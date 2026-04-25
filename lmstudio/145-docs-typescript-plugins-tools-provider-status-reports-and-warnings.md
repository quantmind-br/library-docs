---
title: Status Reports & Warnings
url: https://lmstudio.ai/docs/typescript/plugins/tools-provider/status-reports-and-warnings
source: sitemap
fetched_at: 2026-04-07T21:32:12.206207467-03:00
rendered_js: false
word_count: 178
summary: This document explains how to provide status updates and warnings during tool execution, and also details how to gracefully handle prediction aborts using the AbortSignal object.
tags:
    - tool-implementation
    - status-updates
    - user-warnings
    - abortsignal
    - asynchronous-operations
category: guide
---

Sometimes, a tool may take a long time to execute. In such cases, it will be helpful to provide status updates, so the user knows what is happening. In order times, you may want to warn the user about potential issues.

You can use `status` and `warn` methods on the second parameter of the tool's implementation function to send status updates and warnings.

The following example shows how to implement a tool that waits for a specified number of seconds, providing status updates and warnings if the wait time exceeds 10 seconds:

Note status updates and warnings are only visible to the user. If you want the model to also see those messages, you should return them as part of the tool's return value.

## Handling Aborts[](#handling-aborts "Link to 'Handling Aborts'")

A prediction may be aborted by the user while your tool is still running. In such cases, you should handle the abort gracefully by handling the `AbortSignal` object passed as the second parameter to the tool's implementation function.

You can learn more about `AbortSignal` in the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal).