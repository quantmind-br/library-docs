---
title: sweep - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/cli/benchmark/sweep/
source: sitemap
fetched_at: 2026-05-07T21:19:31.247453696-03:00
rendered_js: false
word_count: 21
summary: This document defines the sweep subcommand for the vLLM benchmark CLI, providing the interface for executing parameter sweep benchmarks.
tags:
    - vllm
    - cli-tool
    - benchmarking
    - parameter-sweep
    - command-line-interface
category: api
---

Bases: `BenchmarkSubcommandBase`

The `sweep` subcommand for `vllm bench`.

Source code in `vllm/entrypoints/cli/benchmark/sweep.py`

```
classBenchmarkSweepSubcommand(BenchmarkSubcommandBase):
"""The `sweep` subcommand for `vllm bench`."""

    name = "sweep"
    help = "Benchmark for a parameter sweep."

    @classmethod
    defadd_cli_args(cls, parser: argparse.ArgumentParser) -> None:
        add_cli_args(parser)

    @staticmethod
    defcmd(args: argparse.Namespace) -> None:
        main(args)
```