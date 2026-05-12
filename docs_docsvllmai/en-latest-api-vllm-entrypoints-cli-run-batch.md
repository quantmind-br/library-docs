---
title: run_batch - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/cli/run_batch/
source: sitemap
fetched_at: 2026-05-07T21:19:36.482243756-03:00
rendered_js: false
word_count: 21
summary: This document defines the run-batch subcommand for the vLLM CLI, which enables the execution of batch prompt processing tasks using an OpenAI-compatible API.
tags:
    - vllm-cli
    - batch-processing
    - cli-subcommand
    - openai-api
    - metrics-monitoring
category: reference
---

Bases: `CLISubcommand`

The `run-batch` subcommand for vLLM CLI.

Source code in `vllm/entrypoints/cli/run_batch.py`

```
classRunBatchSubcommand(CLISubcommand):
"""The `run-batch` subcommand for vLLM CLI."""

    name = "run-batch"

    @staticmethod
    defcmd(args: argparse.Namespace) -> None:
        fromvllm.entrypoints.openai.run_batchimport main as run_batch_main

        logger.info(
            "vLLM batch processing API version %s", importlib.metadata.version("vllm")
        )
        logger.info("args: %s", args)

        # Start the Prometheus metrics server.
        # LLMEngine uses the Prometheus client
        # to publish metrics at the /metrics endpoint.
        if args.enable_metrics:
            fromprometheus_clientimport start_http_server

            logger.info("Prometheus metrics enabled")
            start_http_server(port=args.port, addr=args.url)
        else:
            logger.info("Prometheus metrics disabled")

        asyncio.run(run_batch_main(args))

    defsubparser_init(
        self, subparsers: argparse._SubParsersAction
    ) -> FlexibleArgumentParser:
        fromvllm.entrypoints.openai.run_batchimport make_arg_parser

        run_batch_parser = subparsers.add_parser(
            self.name,
            help="Run batch prompts and write results to file.",
            description=(
                "Run batch prompts using vLLM's OpenAI-compatible API.\n"
                "Supports local or HTTP input/output files."
            ),
            usage="vllm run-batch -i INPUT.jsonl -o OUTPUT.jsonl --model <model>",
        )
        run_batch_parser = make_arg_parser(run_batch_parser)
        run_batch_parser.epilog = VLLM_SUBCMD_PARSER_EPILOG.format(subcmd=self.name)
        return run_batch_parser
```