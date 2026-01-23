---
title: asyncify - DSPy
url: https://dspy.ai/api/utils/asyncify/
source: sitemap
fetched_at: 2026-01-23T08:02:54.928650357-03:00
rendered_js: false
word_count: 104
summary: Explains how to use the dspy.asyncify function to wrap DSPy programs for asynchronous execution while maintaining thread-local configuration.
tags:
    - dspy
    - async-await
    - concurrency
    - api-reference
    - thread-context
category: api
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/utils/asyncify.md "Edit this page")

## `dspy.asyncify(program: Module) -> Callable[[Any, Any], Awaitable[Any]]` [¶](#dspy.asyncify "Permanent link")

Wraps a DSPy program so that it can be called asynchronously. This is useful for running a program in parallel with another task (e.g., another DSPy program).

This implementation propagates the current thread's configuration context to the worker thread.

Parameters:

Name Type Description Default `program` `Module`

The DSPy program to be wrapped for asynchronous execution.

*required*

Returns:

Type Description `Callable[[Any, Any], Awaitable[Any]]`

An async function: An async function that, when awaited, runs the program in a worker thread. The current thread's configuration context is inherited for each call.

Source code in `dspy/utils/asyncify.py`

```
defasyncify(program: "Module") -> Callable[[Any, Any], Awaitable[Any]]:
"""
    Wraps a DSPy program so that it can be called asynchronously. This is useful for running a
    program in parallel with another task (e.g., another DSPy program).

    This implementation propagates the current thread's configuration context to the worker thread.

    Args:
        program: The DSPy program to be wrapped for asynchronous execution.

    Returns:
        An async function: An async function that, when awaited, runs the program in a worker thread.
            The current thread's configuration context is inherited for each call.
    """

    async defasync_program(*args, **kwargs) -> Any:
        # Capture the current overrides at call-time.
        fromdspy.dsp.utils.settingsimport thread_local_overrides

        parent_overrides = thread_local_overrides.get().copy()

        defwrapped_program(*a, **kw):
            fromdspy.dsp.utils.settingsimport thread_local_overrides

            original_overrides = thread_local_overrides.get()
            token = thread_local_overrides.set({**original_overrides, **parent_overrides.copy()})
            try:
                return program(*a, **kw)
            finally:
                thread_local_overrides.reset(token)

        # Create a fresh asyncified callable each time, ensuring the latest context is used.
        call_async = asyncer.asyncify(wrapped_program, abandon_on_cancel=True, limiter=get_limiter())
        return await call_async(*args, **kwargs)

    return async_program
```

:::