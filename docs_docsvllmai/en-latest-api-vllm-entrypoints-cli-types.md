---
title: types - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/cli/types/
source: sitemap
fetched_at: 2026-05-07T21:19:38.059525281-03:00
rendered_js: false
word_count: 10
summary: This document defines the base class structure for CLI subcommand handlers in the vLLM project, outlining the interface required for command execution, validation, and subparser initialization.
tags:
    - cli-interface
    - command-line-arguments
    - python-base-class
    - subcommand-handler
    - vllm-architecture
category: reference
---

Base class for CLI argument handlers.

Source code in `vllm/entrypoints/cli/types.py`

```
classCLISubcommand:
"""Base class for CLI argument handlers."""

    name: str

    @staticmethod
    defcmd(args: argparse.Namespace) -> None:
        raise NotImplementedError("Subclasses should implement this method")

    defvalidate(self, args: argparse.Namespace) -> None:
        # No validation by default
        pass

    defsubparser_init(
        self, subparsers: argparse._SubParsersAction
    ) -> FlexibleArgumentParser:
        raise NotImplementedError("Subclasses should implement this method")
```