---
title: ready_checker - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/benchmarks/lib/ready_checker/
source: sitemap
fetched_at: 2026-05-07T21:15:51.08887751-03:00
rendered_js: false
word_count: 91
summary: This document provides documentation for a utility function designed to asynchronously poll an endpoint for readiness before executing benchmark tasks.
tags:
    - vllm
    - endpoint-readiness
    - async-polling
    - benchmarking-utilities
    - api-testing
category: reference
---

## vllm.benchmarks.lib.ready\_checker [¶](#vllm.benchmarks.lib.ready_checker "Permanent link")

Utilities for checking endpoint readiness.

## wait\_for\_endpoint `async` [¶](#vllm.benchmarks.lib.ready_checker.wait_for_endpoint "Permanent link")

Wait for an endpoint to become available before starting benchmarks.

Parameters:

Name Type Description Default `request_func` `RequestFunc`

The async request function to call

*required* `test_input` `RequestFuncInput`

The RequestFuncInput to test with

*required* `timeout_seconds` `int`

Maximum time to wait in seconds (default: 10 minutes)

`600` `retry_interval` `int`

Time between retries in seconds (default: 5 seconds)

`5`

Returns:

Name Type Description `RequestFuncOutput` `RequestFuncOutput`

The successful response

Raises:

Type Description `ValueError`

If the endpoint doesn't become available within the timeout

Source code in `vllm/benchmarks/lib/ready_checker.py`

```
async defwait_for_endpoint(
    request_func: RequestFunc,
    test_input: RequestFuncInput,
    session: aiohttp.ClientSession,
    timeout_seconds: int = 600,
    retry_interval: int = 5,
) -> RequestFuncOutput:
"""
    Wait for an endpoint to become available before starting benchmarks.

    Args:
        request_func: The async request function to call
        test_input: The RequestFuncInput to test with
        timeout_seconds: Maximum time to wait in seconds (default: 10 minutes)
        retry_interval: Time between retries in seconds (default: 5 seconds)

    Returns:
        RequestFuncOutput: The successful response

    Raises:
        ValueError: If the endpoint doesn't become available within the timeout
    """
    deadline = time.perf_counter() + timeout_seconds
    output = RequestFuncOutput(success=False)
    print(f"Waiting for endpoint to become up in {timeout_seconds} seconds")

    with tqdm(
        total=timeout_seconds,
        bar_format="{desc} |{bar}| {elapsed} elapsed, {remaining} remaining",
        unit="s",
    ) as pbar:
        while True:
            # update progress bar
            remaining = deadline - time.perf_counter()
            elapsed = timeout_seconds - remaining
            update_amount = min(elapsed - pbar.n, timeout_seconds - pbar.n)
            pbar.update(update_amount)
            pbar.refresh()
            if remaining <= 0:
                pbar.close()
                break

            # ping the endpoint using request_func
            try:
                output = await request_func(
                    request_func_input=test_input, session=session
                )
                if output.success:
                    pbar.close()
                    return output
                else:
                    err_last_line = str(output.error).rstrip().rsplit("\n", 1)[-1]
                    logger.warning("Endpoint is not ready. Error='%s'", err_last_line)
            except aiohttp.ClientConnectorError:
                pass

            # retry after a delay
            sleep_duration = min(retry_interval, remaining)
            if sleep_duration > 0:
                await asyncio.sleep(sleep_duration)

    return output
```