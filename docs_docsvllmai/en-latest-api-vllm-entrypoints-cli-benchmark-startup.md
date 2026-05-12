---
title: startup - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/cli/benchmark/startup/
source: sitemap
fetched_at: 2026-05-07T21:19:29.725086817-03:00
rendered_js: false
word_count: 21
summary: This document defines the startup subcommand for the vLLM benchmark CLI, providing the class structure for executing model startup time performance tests.
tags:
    - vllm
    - benchmarking
    - cli-command
    - performance-testing
    - startup-time
category: reference
---

Bases: `BenchmarkSubcommandBase`

The `startup` subcommand for `vllm bench`.

Source code in `vllm/entrypoints/cli/benchmark/startup.py`

```
classBenchmarkStartupSubcommand(BenchmarkSubcommandBase):
"""The `startup` subcommand for `vllm bench`."""

    name = "startup"
    help = "Benchmark the startup time of vLLM models."

    @classmethod
    defadd_cli_args(cls, parser: argparse.ArgumentParser) -> None:
        add_cli_args(parser)

    @staticmethod
    defcmd(args: argparse.Namespace) -> None:
        main(args)
```