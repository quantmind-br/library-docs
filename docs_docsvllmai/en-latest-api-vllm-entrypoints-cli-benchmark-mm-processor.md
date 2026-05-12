---
title: mm_processor - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/cli/benchmark/mm_processor/
source: sitemap
fetched_at: 2026-05-07T21:19:28.070204171-03:00
rendered_js: false
word_count: 21
summary: This document defines the mm-processor subcommand class used for benchmarking multimodal processor latency within the vLLM framework.
tags:
    - vllm
    - benchmarking
    - multimodal-processor
    - cli-subcommand
    - performance-testing
category: api
---

Bases: `BenchmarkSubcommandBase`

The `mm-processor` subcommand for `vllm bench`.

Source code in `vllm/entrypoints/cli/benchmark/mm_processor.py`

```
classBenchmarkMMProcessorSubcommand(BenchmarkSubcommandBase):
"""The `mm-processor` subcommand for `vllm bench`."""

    name = "mm-processor"
    help = "Benchmark multimodal processor latency across different configurations."

    @classmethod
    defadd_cli_args(cls, parser: argparse.ArgumentParser) -> None:
        add_cli_args(parser)

    @staticmethod
    defcmd(args: argparse.Namespace) -> None:
        main(args)
```