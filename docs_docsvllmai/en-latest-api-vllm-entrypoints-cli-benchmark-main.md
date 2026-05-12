---
title: main - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/cli/benchmark/main/
source: sitemap
fetched_at: 2026-05-07T21:19:27.019236527-03:00
rendered_js: false
word_count: 23
summary: This document defines the structure and initialization logic for the vLLM CLI bench subcommand, enabling modular benchmark execution.
tags:
    - vllm
    - cli-subcommand
    - benchmarking
    - argparse
    - python-entrypoints
category: reference
---

Bases: `CLISubcommand`

The `bench` subcommand for the vLLM CLI.

Source code in `vllm/entrypoints/cli/benchmark/main.py`

```
classBenchmarkSubcommand(CLISubcommand):
"""The `bench` subcommand for the vLLM CLI."""

    name = "bench"
    help = "vLLM bench subcommand."

    @staticmethod
    defcmd(args: argparse.Namespace) -> None:
        args.dispatch_function(args)

    defvalidate(self, args: argparse.Namespace) -> None:
        pass

    defsubparser_init(
        self, subparsers: argparse._SubParsersAction
    ) -> FlexibleArgumentParser:
        bench_parser = subparsers.add_parser(
            self.name,
            help=self.help,
            description=self.help,
            usage=f"vllm {self.name} <bench_type> [options]",
        )
        bench_subparsers = bench_parser.add_subparsers(required=True, dest="bench_type")

        # Only build the nested bench subparsers when the user is actually
        # invoking `bench`; otherwise we'd drag in imports
        # unnecessarily on every `vllm --help` and `vllm serve`.
        # Scan for the first positional arg so global flags (e.g. `-v`)
        # before the subcommand don't break detection.
        first_positional = next(
            (arg for arg in sys.argv[1:] if not arg.startswith("-")), None
        )
        if first_positional == self.name:
            _import_bench_subcommand_modules()
            for cmd_cls in BenchmarkSubcommandBase.__subclasses__():
                cmd_subparser = bench_subparsers.add_parser(
                    cmd_cls.name,
                    help=cmd_cls.help,
                    description=cmd_cls.help,
                    usage=f"vllm {self.name}{cmd_cls.name} [options]",
                )
                cmd_subparser.set_defaults(dispatch_function=cmd_cls.cmd)
                cmd_cls.add_cli_args(cmd_subparser)
                cmd_subparser.epilog = VLLM_SUBCMD_PARSER_EPILOG.format(
                    subcmd=f"{self.name}{cmd_cls.name}"
                )
        return bench_parser
```