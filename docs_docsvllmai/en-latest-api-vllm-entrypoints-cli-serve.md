---
title: serve - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/cli/serve/
source: sitemap
fetched_at: 2026-05-07T21:19:36.937923599-03:00
rendered_js: false
word_count: 27
summary: This document defines the ServeSubcommand class within the vLLM CLI, which manages the initialization and configuration of the model serving infrastructure.
tags:
    - vllm
    - cli
    - model-serving
    - api-server
    - load-balancing
    - command-line-interface
category: reference
---

## vllm.entrypoints.cli.serve [¶](#vllm.entrypoints.cli.serve "Permanent link")

## ServeSubcommand [¶](#vllm.entrypoints.cli.serve.ServeSubcommand "Permanent link")

Bases: `CLISubcommand`

The `serve` subcommand for the vLLM CLI.

Source code in `vllm/entrypoints/cli/serve.py`

```
classServeSubcommand(CLISubcommand):
"""The `serve` subcommand for the vLLM CLI."""

    name = "serve"

    @staticmethod
    defcmd(args: argparse.Namespace) -> None:
        # If model is specified in CLI (as positional arg), it takes precedence
        if hasattr(args, "model_tag") and args.model_tag is not None:
            args.model = args.model_tag

        if getattr(args, "grpc", False):
            fromvllm.entrypoints.grpc_serverimport serve_grpc

            uvloop.run(serve_grpc(args))
            return

        if args.headless:
            if args.api_server_count is not None and args.api_server_count > 0:
                raise ValueError(
                    f"--api-server-count={args.api_server_count} cannot be "
                    "used with --headless (no API servers are started in "
                    "headless mode)."
                )
            # Default to 0 in headless mode (no API servers)
            args.api_server_count = 0

        # Detect LB mode for defaulting api_server_count.
        # External LB: --data-parallel-external-lb or --data-parallel-rank
        # Hybrid LB: --data-parallel-hybrid-lb or --data-parallel-start-rank
        is_external_lb = (
            args.data_parallel_external_lb or args.data_parallel_rank is not None
        )
        is_hybrid_lb = (
            args.data_parallel_hybrid_lb or args.data_parallel_start_rank is not None
        )

        if is_external_lb and is_hybrid_lb:
            raise ValueError(
                "Cannot use both external and hybrid data parallel load "
                "balancing modes. External LB is enabled via "
                "--data-parallel-external-lb or --data-parallel-rank. "
                "Hybrid LB is enabled via --data-parallel-hybrid-lb or "
                "--data-parallel-start-rank. Use one mode or the other."
            )

        # Default api_server_count if not explicitly set.
        # - External LB: Leave as 1 (external LB handles distribution)
        # - Hybrid LB: Use local DP size (internal LB for local ranks only)
        # - Internal LB: Use full DP size
        if args.api_server_count is None:
            if is_external_lb:
                args.api_server_count = 1
            elif is_hybrid_lb:
                args.api_server_count = args.data_parallel_size_local or 1
                if args.api_server_count > 1:
                    logger.info(
                        "Defaulting api_server_count to data_parallel_size_local "
                        "(%d) for hybrid LB mode.",
                        args.api_server_count,
                    )
            else:
                args.api_server_count = args.data_parallel_size
                if args.api_server_count > 1:
                    logger.info(
                        "Defaulting api_server_count to data_parallel_size (%d).",
                        args.api_server_count,
                    )

        # Elastic EP currently only supports running with at most one API server.
        if getattr(args, "enable_elastic_ep", False) and args.api_server_count > 1:
            logger.warning(
                "Elastic EP only supports running with with at most one API server. "
                "Capping api_server_count from %d to 1.",
                args.api_server_count,
            )
            args.api_server_count = 1

        if args.api_server_count < 1:
            run_headless(args)
        elif args.api_server_count > 1:
            run_multi_api_server(args)
        else:
            # Single API server (this process).
            args.api_server_count = None
            uvloop.run(run_server(args))

    defvalidate(self, args: argparse.Namespace) -> None:
        validate_parsed_serve_args(args)

    defsubparser_init(
        self, subparsers: argparse._SubParsersAction
    ) -> FlexibleArgumentParser:
        serve_parser = subparsers.add_parser(
            self.name,
            help="Launch a local OpenAI-compatible API server to serve LLM "
            "completions via HTTP.",
            description=DESCRIPTION,
            usage="vllm serve [model_tag] [options]",
        )

        serve_parser = make_arg_parser(serve_parser)
        serve_parser.epilog = VLLM_SUBCMD_PARSER_EPILOG.format(subcmd=self.name)
        return serve_parser
```