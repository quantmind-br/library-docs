---
title: base - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/cli/benchmark/base/
source: sitemap
fetched_at: 2026-05-07T21:19:25.154474362-03:00
rendered_js: false
word_count: 94
summary: This document defines the base class for implementing custom benchmarking subcommands within the vLLM command-line interface.
tags:
    - vllm
    - benchmarking
    - cli-subcommand
    - python-base-class
    - api-reference
category: reference
---

## vllm.entrypoints.cli.benchmark.base [¶](#vllm.entrypoints.cli.benchmark.base "Permanent link")

## BenchmarkSubcommandBase [¶](#vllm.entrypoints.cli.benchmark.base.BenchmarkSubcommandBase "Permanent link")

Bases: `CLISubcommand`

The base class of subcommands for `vllm bench`.

Source code in `vllm/entrypoints/cli/benchmark/base.py`

```
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25

classBenchmarkSubcommandBase(CLISubcommand):
"""The base class of subcommands for `vllm bench`."""

    help: str

    @classmethod
    defadd_cli_args(cls, parser: argparse.ArgumentParser) -> None:
"""Add the CLI arguments to the parser."""
        raise NotImplementedError

    @staticmethod
    defcmd(args: argparse.Namespace) -> None:
"""Run the benchmark.

        Args:
            args: The arguments to the command.
        """
        raise NotImplementedError
```

### add\_cli\_args `classmethod` [¶](#vllm.entrypoints.cli.benchmark.base.BenchmarkSubcommandBase.add_cli_args "Permanent link")

Add the CLI arguments to the parser.

Source code in `vllm/entrypoints/cli/benchmark/base.py`

```
@classmethod
defadd_cli_args(cls, parser: argparse.ArgumentParser) -> None:
"""Add the CLI arguments to the parser."""
    raise NotImplementedError
```

### cmd `staticmethod` [¶](#vllm.entrypoints.cli.benchmark.base.BenchmarkSubcommandBase.cmd "Permanent link")

Run the benchmark.

Parameters:

Name Type Description Default `args` `Namespace`

The arguments to the command.

*required*

Source code in `vllm/entrypoints/cli/benchmark/base.py`

```
@staticmethod
defcmd(args: argparse.Namespace) -> None:
"""Run the benchmark.

    Args:
        args: The arguments to the command.
    """
    raise NotImplementedError
```