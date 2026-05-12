---
title: launch - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/cli/launch/
source: sitemap
fetched_at: 2026-05-07T21:19:33.930250147-03:00
rendered_js: false
word_count: 144
summary: This document defines the class structure and command-line interface implementation for the vLLM launch subcommand, including its nested components and FastAPI server integration.
tags:
    - vllm
    - cli-interface
    - python-api
    - subcommands
    - fastapi-integration
category: reference
---

## LaunchSubcommand [¶](#vllm.entrypoints.cli.launch.LaunchSubcommand "Permanent link")

Bases: `CLISubcommand`

The `launch` subcommand for the vLLM CLI.

Uses nested sub-subcommands so each component can define its own arguments independently (e.g. `vllm launch render`).

Source code in `vllm/entrypoints/cli/launch.py`

```
classLaunchSubcommand(CLISubcommand):
"""The `launch` subcommand for the vLLM CLI.

    Uses nested sub-subcommands so each component can define its own
    arguments independently (e.g. ``vllm launch render``).
    """

    name = "launch"

    @staticmethod
    defcmd(args: argparse.Namespace) -> None:
        if hasattr(args, "model_tag") and args.model_tag is not None:
            args.model = args.model_tag

        args.launch_command(args)

    defvalidate(self, args: argparse.Namespace) -> None:
        validate_parsed_serve_args(args)

    defsubparser_init(
        self, subparsers: argparse._SubParsersAction
    ) -> FlexibleArgumentParser:
        launch_parser = subparsers.add_parser(
            self.name,
            help=DESCRIPTION,
            description=DESCRIPTION,
            usage=f"vllm {self.name} <component> [options]",
        )
        launch_subparsers = launch_parser.add_subparsers(
            required=True, dest="launch_component"
        )

        for cmd_cls in LaunchSubcommandBase.__subclasses__():
            cmd_subparser = launch_subparsers.add_parser(
                cmd_cls.name,
                help=cmd_cls.help,
                description=cmd_cls.help,
                usage=f"vllm {self.name}{cmd_cls.name} [options]",
            )
            cmd_subparser.set_defaults(launch_command=cmd_cls.cmd)
            cmd_cls.add_cli_args(cmd_subparser)
            cmd_subparser.epilog = VLLM_SUBCMD_PARSER_EPILOG.format(
                subcmd=f"{self.name}{cmd_cls.name}"
            )

        return launch_parser
```

## LaunchSubcommandBase [¶](#vllm.entrypoints.cli.launch.LaunchSubcommandBase "Permanent link")

Bases: `CLISubcommand`

The base class of subcommands for `vllm launch`.

Source code in `vllm/entrypoints/cli/launch.py`

```
classLaunchSubcommandBase(CLISubcommand):
"""The base class of subcommands for `vllm launch`."""

    help: str

    @classmethod
    defadd_cli_args(cls, parser: FlexibleArgumentParser) -> None:
"""Add the CLI arguments to the parser.

        By default, adds the standard vLLM serving arguments.
        Subclasses can override to add component-specific arguments.
        """
        make_arg_parser(parser)

    @staticmethod
    defcmd(args: argparse.Namespace) -> None:
        raise NotImplementedError
```

### add\_cli\_args `classmethod` [¶](#vllm.entrypoints.cli.launch.LaunchSubcommandBase.add_cli_args "Permanent link")

Add the CLI arguments to the parser.

By default, adds the standard vLLM serving arguments. Subclasses can override to add component-specific arguments.

Source code in `vllm/entrypoints/cli/launch.py`

```
@classmethod
defadd_cli_args(cls, parser: FlexibleArgumentParser) -> None:
"""Add the CLI arguments to the parser.

    By default, adds the standard vLLM serving arguments.
    Subclasses can override to add component-specific arguments.
    """
    make_arg_parser(parser)
```

## RenderSubcommand [¶](#vllm.entrypoints.cli.launch.RenderSubcommand "Permanent link")

Bases: `LaunchSubcommandBase`

The `render` subcommand for `vllm launch`.

Source code in `vllm/entrypoints/cli/launch.py`

```
classRenderSubcommand(LaunchSubcommandBase):
"""The `render` subcommand for `vllm launch`."""

    name = "render"
    help = "Launch a GPU-less rendering server (preprocessing and postprocessing only)."

    @staticmethod
    defcmd(args: argparse.Namespace) -> None:
        uvloop.run(run_launch_fastapi(args))
```

## run\_launch\_fastapi `async` [¶](#vllm.entrypoints.cli.launch.run_launch_fastapi "Permanent link")

Run the online serving layer with FastAPI (no GPU inference).

Source code in `vllm/entrypoints/cli/launch.py`

```
async defrun_launch_fastapi(args: argparse.Namespace) -> None:
"""Run the online serving layer with FastAPI (no GPU inference)."""
    # 1. Socket binding
    listen_address, sock = setup_server(args)

    # 2. Build and serve the API server
    engine_args = AsyncEngineArgs.from_cli_args(args)
    model_config = engine_args.create_model_config()

    # Render servers preprocess data only — no inference, no quantized kernels.
    # Clear quantization so VllmConfig skips quant dtype/capability validation.
    model_config.quantization = None

    # Render servers never allocate KV cache; suppress the spurious CPU KV
    # cache space warning from CpuPlatform.check_and_update_config.
    envs.VLLM_CPU_KVCACHE_SPACE = 0

    vllm_config = VllmConfig(model_config=model_config)
    shutdown_task = await build_and_serve_renderer(
        vllm_config, listen_address, sock, args
    )
    try:
        await shutdown_task
    finally:
        sock.close()
```