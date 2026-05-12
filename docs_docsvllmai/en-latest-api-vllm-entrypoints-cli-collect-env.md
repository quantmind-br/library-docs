---
title: collect_env - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/cli/collect_env/
source: sitemap
fetched_at: 2026-05-07T21:19:32.858456633-03:00
rendered_js: false
word_count: 15
summary: This document defines the collect-env CLI subcommand in vLLM, which is used to gather diagnostic information about the current execution environment.
tags:
    - vllm
    - cli-tool
    - environment-diagnostics
    - subcommand-definition
    - python-argparse
category: api
---

```
classCollectEnvSubcommand(CLISubcommand):
"""The `collect-env` subcommand for the vLLM CLI."""

    name = "collect-env"

    @staticmethod
    defcmd(args: argparse.Namespace) -> None:
"""Collect information about the environment."""
        collect_env_main()

    defsubparser_init(
        self, subparsers: argparse._SubParsersAction
    ) -> FlexibleArgumentParser:
        return subparsers.add_parser(
            "collect-env",
            help="Start collecting environment information.",
            description="Start collecting environment information.",
            usage="vllm collect-env",
        )
```