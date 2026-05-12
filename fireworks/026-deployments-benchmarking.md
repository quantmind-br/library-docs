---
title: Performance benchmarking - Fireworks AI Docs
url: https://docs.fireworks.ai/deployments/benchmarking
source: sitemap
fetched_at: 2026-04-27T20:18:55.706168748-03:00
rendered_js: false
word_count: 192
summary: This document describes the Fireworks Benchmarking Tool and outlines best practices for using it to test and optimize a deployment's performance under various load conditions.
tags:
    - performance-benchmarking
    - load-testing
    - deployment-optimization
    - throughput-latency
    - fireworks-ai
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Use the open-source [Fireworks Benchmark Tool](https://github.com/fw-ai/benchmark) to measure and optimize deployment performance. The tool tests throughput and latency, simulates production traffic patterns, identifies bottlenecks, and compares deployment configurations.

## Installation

```bash
git clone https://github.com/fw-ai/benchmark.git
cd benchmark
pip install -r requirements.txt
```

## Basic Usage

```bash
python benchmark.py \
  --model "accounts/fireworks/models/llama-v3p1-8b-instruct" \
  --deployment "your-deployment-id" \
  --num-requests 1000 \
  --concurrency 10
```

## Key Metrics

| Metric | Description |
|--------|-------------|
| **Throughput** | Requests per second (RPS) |
| **Latency** | Time to first token (TTFT) and end-to-end response time |
| **Token generation rate** | Tokens per second during generation |
| **Error rate** | Failed requests under load |

## Best Practices

1. **Warm up your deployment** — run a few requests before benchmarking to load models
2. **Test realistic scenarios** — use request patterns similar to production workload
3. **Gradually increase load** — start with low concurrency to find deployment limits
4. **Monitor for errors** — track error rates and response codes
5. **Compare configurations** — test different deployment shapes, quantization levels, and hardware

## Custom Benchmarking

Develop custom performance testing scripts or integrate with monitoring tools to track metrics over time:

- Use production-like request patterns and payloads
- Test various concurrency levels
- Monitor resource utilization (GPU, memory, network)
- Test autoscaling behavior under load
