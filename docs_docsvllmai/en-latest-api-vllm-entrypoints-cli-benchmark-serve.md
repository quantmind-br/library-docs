---
title: serve - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/cli/benchmark/serve/
source: sitemap
fetched_at: 2026-05-07T21:19:28.861178779-03:00
rendered_js: false
word_count: 21
summary: This document defines the serve subcommand for the vLLM benchmark CLI, which is used to evaluate the online serving throughput of the system.
tags:
    - vllm
    - cli-tool
    - benchmarking
    - throughput-testing
    - command-interface
category: reference
---

Bases: `BenchmarkSubcommandBase`

The `serve` subcommand for `vllm bench`.

Source code in `vllm/entrypoints/cli/benchmark/serve.py`

```
classBenchmarkServingSubcommand(BenchmarkSubcommandBase):
"""The `serve` subcommand for `vllm bench`."""

    name = "serve"
    help = "Benchmark the online serving throughput."

    @classmethod
    defadd_cli_args(cls, parser: argparse.ArgumentParser) -> None:
        add_cli_args(parser)

    @staticmethod
    defcmd(args: argparse.Namespace) -> None:
        main(args)
```