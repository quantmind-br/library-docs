---
title: openai - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/cli/openai/
source: sitemap
fetched_at: 2026-05-07T21:19:36.039061826-03:00
rendered_js: false
word_count: 92
summary: This document defines the CLI subcommands for interacting with vLLM via chat and completion interfaces, detailing the implementation of command-line arguments and request handling.
tags:
    - vllm
    - cli-tool
    - chat-completion
    - text-generation
    - command-line-interface
    - python-api
category: reference
---

## ChatCommand [¶](#vllm.entrypoints.cli.openai.ChatCommand "Permanent link")

Bases: `CLISubcommand`

The `chat` subcommand for the vLLM CLI.

Source code in `vllm/entrypoints/cli/openai.py`

```
classChatCommand(CLISubcommand):
"""The `chat` subcommand for the vLLM CLI."""

    name = "chat"

    @staticmethod
    defcmd(args: argparse.Namespace) -> None:
        model_name, client = _interactive_cli(args)
        system_prompt = args.system_prompt
        conversation: list[ChatCompletionMessageParam] = []

        if system_prompt is not None:
            conversation.append({"role": "system", "content": system_prompt})

        if args.quick:
            conversation.append({"role": "user", "content": args.quick})

            stream = client.chat.completions.create(
                model=model_name, messages=conversation, stream=True
            )
            output = _print_chat_stream(stream)
            conversation.append({"role": "assistant", "content": output})
            return

        print("Please enter a message for the chat model:")
        while True:
            try:
                input_message = input("> ")
            except EOFError:
                break
            conversation.append({"role": "user", "content": input_message})

            stream = client.chat.completions.create(
                model=model_name, messages=conversation, stream=True
            )
            output = _print_chat_stream(stream)
            conversation.append({"role": "assistant", "content": output})

    @staticmethod
    defadd_cli_args(parser: FlexibleArgumentParser) -> FlexibleArgumentParser:
"""Add CLI arguments for the chat command."""
        _add_query_options(parser)
        parser.add_argument(
            "--system-prompt",
            type=str,
            default=None,
            help=(
                "The system prompt to be added to the chat template, "
                "used for models that support system prompts."
            ),
        )
        parser.add_argument(
            "-q",
            "--quick",
            type=str,
            metavar="MESSAGE",
            help=("Send a single prompt as MESSAGE and print the response, then exit."),
        )
        return parser

    defsubparser_init(
        self, subparsers: argparse._SubParsersAction
    ) -> FlexibleArgumentParser:
        parser = subparsers.add_parser(
            "chat",
            help="Generate chat completions via the running API server.",
            description="Generate chat completions via the running API server.",
            usage="vllm chat [options]",
        )
        return ChatCommand.add_cli_args(parser)
```

### add\_cli\_args `staticmethod` [¶](#vllm.entrypoints.cli.openai.ChatCommand.add_cli_args "Permanent link")

Add CLI arguments for the chat command.

Source code in `vllm/entrypoints/cli/openai.py`

```
@staticmethod
defadd_cli_args(parser: FlexibleArgumentParser) -> FlexibleArgumentParser:
"""Add CLI arguments for the chat command."""
    _add_query_options(parser)
    parser.add_argument(
        "--system-prompt",
        type=str,
        default=None,
        help=(
            "The system prompt to be added to the chat template, "
            "used for models that support system prompts."
        ),
    )
    parser.add_argument(
        "-q",
        "--quick",
        type=str,
        metavar="MESSAGE",
        help=("Send a single prompt as MESSAGE and print the response, then exit."),
    )
    return parser
```

## CompleteCommand [¶](#vllm.entrypoints.cli.openai.CompleteCommand "Permanent link")

Bases: `CLISubcommand`

The `complete` subcommand for the vLLM CLI.

Source code in `vllm/entrypoints/cli/openai.py`

```
classCompleteCommand(CLISubcommand):
"""The `complete` subcommand for the vLLM CLI."""

    name = "complete"

    @staticmethod
    defcmd(args: argparse.Namespace) -> None:
        model_name, client = _interactive_cli(args)

        kwargs = {
            "model": model_name,
            "stream": True,
        }
        if args.max_tokens:
            kwargs["max_tokens"] = args.max_tokens

        if args.quick:
            stream = client.completions.create(prompt=args.quick, **kwargs)
            _print_completion_stream(stream)
            return

        print("Please enter prompt to complete:")
        while True:
            try:
                input_prompt = input("> ")
            except EOFError:
                break
            stream = client.completions.create(prompt=input_prompt, **kwargs)
            _print_completion_stream(stream)

    @staticmethod
    defadd_cli_args(parser: FlexibleArgumentParser) -> FlexibleArgumentParser:
"""Add CLI arguments for the complete command."""
        _add_query_options(parser)
        parser.add_argument(
            "--max-tokens",
            type=int,
            help="Maximum number of tokens to generate per output sequence.",
        )
        parser.add_argument(
            "-q",
            "--quick",
            type=str,
            metavar="PROMPT",
            help="Send a single prompt and print the completion output, then exit.",
        )
        return parser

    defsubparser_init(
        self, subparsers: argparse._SubParsersAction
    ) -> FlexibleArgumentParser:
        parser = subparsers.add_parser(
            "complete",
            help=(
                "Generate text completions based on the given prompt "
                "via the running API server."
            ),
            description=(
                "Generate text completions based on the given prompt "
                "via the running API server."
            ),
            usage="vllm complete [options]",
        )
        return CompleteCommand.add_cli_args(parser)
```

### add\_cli\_args `staticmethod` [¶](#vllm.entrypoints.cli.openai.CompleteCommand.add_cli_args "Permanent link")

Add CLI arguments for the complete command.

Source code in `vllm/entrypoints/cli/openai.py`

```
@staticmethod
defadd_cli_args(parser: FlexibleArgumentParser) -> FlexibleArgumentParser:
"""Add CLI arguments for the complete command."""
    _add_query_options(parser)
    parser.add_argument(
        "--max-tokens",
        type=int,
        help="Maximum number of tokens to generate per output sequence.",
    )
    parser.add_argument(
        "-q",
        "--quick",
        type=str,
        metavar="PROMPT",
        help="Send a single prompt and print the completion output, then exit.",
    )
    return parser
```