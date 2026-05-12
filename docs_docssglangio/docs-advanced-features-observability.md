---
title: Observability - SGLang Documentation
url: https://docs.sglang.io/docs/advanced_features/observability
source: sitemap
fetched_at: 2026-05-11T05:49:27.716971639-03:00
rendered_js: false
word_count: 200
summary: This document outlines production monitoring and diagnostic capabilities in SGLang, including metrics collection, request logging, and tools for dumping and replaying server requests.
tags:
    - sglang
    - production-monitoring
    - prometheus-metrics
    - request-logging
    - debugging
    - crash-dumping
category: guide
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

## Production Metrics

SGLang exposes the following metrics via Prometheus. You can enable them by adding `--enable-metrics` when launching the server. You can query them by:

```
curl http://localhost:30000/metrics
```

See [Production Metrics](https://docs.sglang.io/docs/references/production_metrics) and [Production Request Tracing](https://docs.sglang.io/docs/references/production_request_trace) for more details.

## Logging

By default, SGLang does not log any request contents. You can log them by using `--log-requests`. You can control the verbosity by using `--log-request-level`. See [Logging](https://docs.sglang.io/docs/advanced_features/server_arguments#logging) for more details.

## Request Dump and Replay

You can dump all requests and replay them later for benchmarking or other purposes. To start dumping, use the following command to send a request to a server:

```
python3 -m sglang.srt.managers.configure_logging --url http://localhost:30000 --dump-requests-folder /tmp/sglang_request_dump --dump-requests-threshold 100
```

The server will dump the requests into a pickle file for every 100 requests. To replay the request dump, use `scripts/playground/replay_request_dump.py`.

## Crash Dump and Replay

Sometimes the server might crash, and you may want to debug the cause of the crash. SGLang supports crash dumping, which will dump all requests from the 5 minutes before the crash, allowing you to replay the requests and debug the reason later. To enable crash dumping, use `--crash-dump-folder /tmp/crash_dump`. To replay the crash dump, use `scripts/playground/replay_request_dump.py`.