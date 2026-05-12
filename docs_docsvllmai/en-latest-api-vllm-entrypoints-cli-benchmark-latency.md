---
title: latency - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/cli/benchmark/latency/
source: sitemap
fetched_at: 2026-05-07T21:19:25.920437083-03:00
rendered_js: false
word_count: 21
summary: This document defines the latency subcommand for the vLLM benchmark CLI, which is used to evaluate the performance of request batches.
tags:
    - vllm
    - cli
    - latency-benchmarking
    - performance-testing
    - command-line-interface
category: reference
---

Bases: `BenchmarkSubcommandBase`

The `latency` subcommand for `vllm bench`.

Source code in `vllm/entrypoints/cli/benchmark/latency.py`

```
classBenchmarkLatencySubcommand(BenchmarkSubcommandBase):
"""The `latency` subcommand for `vllm bench`."""

    name = "latency"
    help = "Benchmark the latency of a single batch of requests."

    @classmethod
    defadd_cli_args(cls, parser: argparse.ArgumentParser) -> None:
        add_cli_args(parser)

    @staticmethod
    defcmd(args: argparse.Namespace) -> None:
        main(args)
```