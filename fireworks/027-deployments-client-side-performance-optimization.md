---
title: Client-side performance optimization - Fireworks AI Docs
url: https://docs.fireworks.ai/deployments/client-side-performance-optimization
source: sitemap
fetched_at: 2026-04-27T20:18:57.309068519-03:00
rendered_js: false
word_count: 120
summary: This document explains best practices for optimizing client-side HTTP connection pooling when deploying services, primarily recommending the use of Python's AsyncFireworks SDK with httpx and direct routing for high performance.
tags:
    - connection-pooling
    - performance-optimization
    - asyncio
    - fireworks-sdk
    - http-requests
    - direct-routing
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Optimize client-side HTTP connection pooling when using a dedicated deployment for maximum performance.

## Recommendations

1. Use a client library optimized for high concurrency — [httpx](https://www.python-httpx.org/) in Python or [`http.Agent`](https://nodejs.org/api/http.html#class-httpagent) in Node.js.
2. Use the `AsyncFireworks` client for high-concurrency workloads.
3. Increase concurrency until performance stops improving or you see too many `429` errors.
4. Use [[028-deployments-direct-routing|direct routing]] to bypass the global API load balancer and route requests directly to your deployment.

## Code example: optimal concurrent requests (Python)

Install the [[094-tools-sdks-python-sdk|Python SDK]] first, then:

```python
import asyncio
import time
import statistics
from fireworks import AsyncFireworks


async def make_concurrent_requests(
    messages: list[str],
    model: str,
    max_workers: int = 1000,
):
    """Make concurrent requests with optimized connection pooling"""

    client = AsyncFireworks(
        base_url="https://my-account-abcd1234.eu-iceland-2.direct.fireworks.ai",
        api_key="MY_DIRECT_ROUTE_API_KEY",
        max_retries=5,
    )

    # Semaphore to limit concurrent requests
    semaphore = asyncio.Semaphore(max_workers)
    latencies = []

    async def single_request(message: str):
        """Make a single request with semaphore control"""
        async with semaphore:
            start_time = time.perf_counter()
            response = await client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": message}],
                max_tokens=100,
            )
            latency = time.perf_counter() - start_time
            latencies.append(latency)
            return response.choices[0].message.content

    # Create all request tasks
    tasks = [single_request(message) for message in messages]

    # Execute all requests concurrently
    results = await asyncio.gather(*tasks)
    return results, latencies


# Usage example
async def main():
    messages = ["Hello!"] * 1000  # 1000 requests

    model = "accounts/fireworks/models/qwen3-0p6b"

    start_time = time.perf_counter()
    results, latencies = await make_concurrent_requests(
        messages=messages,
        model=model,
    )
    total_time = time.perf_counter() - start_time

    # Calculate performance metrics
    num_requests = len(results)
    requests_per_second = num_requests / total_time

    # Latency statistics (in milliseconds)
    latencies_ms = [lat * 1000 for lat in latencies]
    avg_latency = statistics.mean(latencies_ms)
    min_latency = min(latencies_ms)
    max_latency = max(latencies_ms)
    p50_latency = statistics.median(latencies_ms)
    p95_latency = statistics.quantiles(latencies_ms, n=20)[18]  # 95th percentile
    p99_latency = statistics.quantiles(latencies_ms, n=100)[98]  # 99th percentile

    print("\n" + "=" * 50)
    print("Performance Results")
    print("=" * 50)
    print(f"Total requests:      {num_requests}")
    print(f"Total time:          {total_time:.2f} seconds")
    print(f"Throughput:          {requests_per_second:.2f} requests/second")
    print("\nLatency Statistics (ms):")
    print(f"  Min:               {min_latency:.2f}")
    print(f"  Max:               {max_latency:.2f}")
    print(f"  Avg:               {avg_latency:.2f}")
    print(f"  P50 (median):      {p50_latency:.2f}")
    print(f"  P95:               {p95_latency:.2f}")
    print(f"  P99:               {p99_latency:.2f}")
    print("=" * 50)


if __name__ == "__main__":
    asyncio.run(main())
```

This implementation:

- Uses `AsyncFireworks` for non-blocking async requests with optimized connection pooling
- Uses `asyncio.Semaphore` to control concurrency to avoid overwhelming the server
- Targets a dedicated deployment with [[028-deployments-direct-routing|direct routing]]

#connection-pooling #asyncio #performance-optimization
