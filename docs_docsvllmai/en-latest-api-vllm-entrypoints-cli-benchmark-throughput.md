---
title: throughput - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/cli/benchmark/throughput/
source: sitemap
fetched_at: 2026-05-07T21:19:31.824424858-03:00
rendered_js: false
word_count: 21
summary: This document defines the throughput subcommand for the vLLM benchmark CLI, which is used to measure offline inference performance.
tags:
    - vllm
    - benchmarking
    - inference-throughput
    - cli-subcommand
    - performance-testing
category: reference
---

Bases: `BenchmarkSubcommandBase`

The `throughput` subcommand for `vllm bench`.

Source code in `vllm/entrypoints/cli/benchmark/throughput.py`

```
classBenchmarkThroughputSubcommand(BenchmarkSubcommandBase):
"""The `throughput` subcommand for `vllm bench`."""

    name = "throughput"
    help = "Benchmark offline inference throughput."

    @classmethod
    defadd_cli_args(cls, parser: argparse.ArgumentParser) -> None:
        add_cli_args(parser)

    @staticmethod
    defcmd(args: argparse.Namespace) -> None:
        main(args)
```