---
title: cli_args - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/openai/cli_args/
source: sitemap
fetched_at: 2026-05-07T21:19:55.254446493-03:00
rendered_js: false
word_count: 1662
summary: This document defines the BaseFrontendArgs class and command-line arguments for the vLLM OpenAI-compatible server, covering chat templates, tool calling, logging, and response configuration.
tags:
    - vllm
    - openai-api
    - cli-arguments
    - chat-template
    - server-configuration
    - lora-modules
    - tool-calling
category: reference
---

This file contains the command line arguments for the vLLM's OpenAI-compatible server. It is kept in a separate file for documentation purposes.

## BaseFrontendArgs [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs "Permanent link")

Base arguments for the OpenAI-compatible frontend server.

This base class does not include host, port, and server-specific arguments like SSL, CORS, and HTTP server settings. Those arguments are added by the subclasses.

Source code in `vllm/entrypoints/openai/cli_args.py`

```
@config
classBaseFrontendArgs:
"""Base arguments for the OpenAI-compatible frontend server.

    This base class does not include host, port, and server-specific arguments
    like SSL, CORS, and HTTP server settings. Those arguments are added by
    the subclasses.
    """

    lora_modules: list[LoRAModulePath] | None = None
"""LoRA modules configurations in either 'name=path' format or JSON format
    or JSON list format. Example (old format): `'name=path'` Example (new
    format): `{\"name\": \"name\", \"path\": \"lora_path\",
    \"base_model_name\": \"id\"}`"""
    chat_template: str | None = None
"""The file path to the chat template, or the template in single-line form
    for the specified model."""
    chat_template_content_format: ChatTemplateContentFormatOption = "auto"
"""The format to render message content within a chat template.

    * "string" will render the content as a string. Example: `"Hello World"`
    * "openai" will render the content as a list of dictionaries, similar to
      OpenAI schema. Example: `[{"type": "text", "text": "Hello world!"}]`"""
    trust_request_chat_template: bool = False
"""Whether to trust the chat template provided in the request. If False,
    the server will always use the chat template specified by `--chat-template`
    or the ones from tokenizer."""
    default_chat_template_kwargs: dict[str, Any] | None = None
"""Default keyword arguments to pass to the chat template renderer.
    These will be merged with request-level chat_template_kwargs,
    with request values taking precedence. Useful for setting default
    behavior for reasoning models. Example: '{"enable_thinking": false}'
    to disable thinking mode by default for Qwen3/DeepSeek models."""
    response_role: str = "assistant"
"""The role name to return if `request.add_generation_prompt=true`."""
    return_tokens_as_token_ids: bool = False
"""When `--max-logprobs` is specified, represents single tokens as
    strings of the form 'token_id:{token_id}' so that tokens that are not
    JSON-encodable can be identified."""
    enable_auto_tool_choice: bool = False
"""Enable auto tool choice for supported models. Use `--tool-call-parser`
    to specify which parser to use."""
    exclude_tools_when_tool_choice_none: bool = False
"""If specified, exclude tool definitions in prompts when
    tool_choice='none'."""
    tool_call_parser: str | None = None
"""Select the tool call parser depending on the model that you're using.
    This is used to parse the model-generated tool call into OpenAI API format.
    Required for `--enable-auto-tool-choice`. You can choose any option from
    the built-in parsers or register a plugin via `--tool-parser-plugin`."""
    tool_parser_plugin: str = ""
"""Special the tool parser plugin write to parse the model-generated tool
    into OpenAI API format, the name register in this plugin can be used in
    `--tool-call-parser`."""
    tool_server: str | None = None
"""Comma-separated list of host:port pairs (IPv4, IPv6, or hostname).
    Examples: 127.0.0.1:8000, [::1]:8000, localhost:1234. Or `demo` for
    built-in demo tools (browser and Python code interpreter). WARNING:
    The `demo` Python tool executes model-generated code in Docker without
    network isolation by default. See the security guide for more
    information."""
    log_config_file: str | None = envs.VLLM_LOGGING_CONFIG_PATH
"""Path to logging config JSON file for both vllm and uvicorn"""
    max_log_len: int | None = None
"""Max number of prompt characters or prompt ID numbers being printed in
    log. The default of None means unlimited."""
    enable_prompt_tokens_details: bool = False
"""If set to True, enable prompt_tokens_details in usage."""
    enable_server_load_tracking: bool = False
"""If set to True, enable tracking server_load_metrics in the app state."""
    enable_force_include_usage: bool = False
"""If set to True, including usage on every request."""
    enable_tokenizer_info_endpoint: bool = False
"""Enable the `/tokenizer_info` endpoint. May expose chat
    templates and other tokenizer configuration."""
    enable_log_outputs: bool = False
"""If set to True, log model outputs (generations).
    Requires `--enable-log-requests`. As with `--enable-log-requests`,
    information is only logged at INFO level at maximum."""
    enable_log_deltas: bool = True
"""If set to False, output deltas will not be logged. Relevant only if 
    --enable-log-outputs is set.
    """
    log_error_stack: bool = envs.VLLM_SERVER_DEV_MODE
"""If set to True, log the stack trace of error responses"""
    tokens_only: bool = False
"""
    If set to True, only enable the Tokens In<>Out endpoint.
    This is intended for use in a Disaggregated Everything setup.
    """
    fingerprint_mode: Literal["full", "hash", "custom", "none"] = "full"
"""Controls the ``system_fingerprint`` field on responses.

    - ``full`` (default): ``vllm-<version>[-<parallelism>]-<hash8>``. Encodes
      server version, non-trivial parallelism degrees (tp/pp/dp/ep), and an
      8-char config hash.
    - ``hash``: ``vllm-<version>-<hash8>``. Parallelism stripped.
    - ``custom``: emits the literal string from ``--fingerprint-value``.
    - ``none``: the field is omitted (serialized as ``null``).
    """
    fingerprint_value: str | None = None
"""Literal fingerprint string used when ``--fingerprint-mode=custom``."""

    @classmethod
    def_customize_cli_kwargs(
        cls,
        frontend_kwargs: dict[str, Any],
    ) -> dict[str, Any]:
"""Customize argparse kwargs before arguments are registered.

        Subclasses should override this and call
        ``super()._customize_cli_kwargs(frontend_kwargs)`` first.
        """
        # Special case: default_chat_template_kwargs needs json.loads type
        frontend_kwargs["default_chat_template_kwargs"]["type"] = json.loads

        # Special case: LoRA modules need custom parser action and
        # optional_type(str)
        frontend_kwargs["lora_modules"]["type"] = optional_type(str)
        frontend_kwargs["lora_modules"]["action"] = LoRAParserAction

        # Special case: Tool call parser shows built-in options.
        valid_tool_parsers = list(ToolParserManager.list_registered())
        parsers_str = ",".join(valid_tool_parsers)
        frontend_kwargs["tool_call_parser"]["metavar"] = (
            f"{{{parsers_str}}} or name registered in --tool-parser-plugin"
        )
        return frontend_kwargs

    @classmethod
    defadd_cli_args(cls, parser: FlexibleArgumentParser) -> FlexibleArgumentParser:
"""Register CLI arguments for this frontend class.

        Subclasses should override ``_customize_cli_kwargs`` instead of
        this method so that base-class postprocessing is always applied.
        """
        fromvllm.engine.arg_utilsimport get_kwargs

        frontend_kwargs = get_kwargs(cls)
        frontend_kwargs = cls._customize_cli_kwargs(frontend_kwargs)

        group_name = cls.__name__.replace("Args", "")
        frontend_group = parser.add_argument_group(
            title=group_name,
            description=cls.__doc__,
        )
        for key, value in frontend_kwargs.items():
            extra_flags = value.pop("flags", [])
            frontend_group.add_argument(
                *extra_flags, f"--{key.replace('_','-')}", **value
            )

        return parser
```

### chat\_template `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.chat_template "Permanent link")

```
chat_template: str | None = None
```

The file path to the chat template, or the template in single-line form for the specified model.

### chat\_template\_content\_format `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.chat_template_content_format "Permanent link")

```
chat_template_content_format: ChatTemplateContentFormatOption = "auto"
```

The format to render message content within a chat template.

- "string" will render the content as a string. Example: `"Hello World"`
- "openai" will render the content as a list of dictionaries, similar to OpenAI schema. Example: `[{"type": "text", "text": "Hello world!"}]`

### default\_chat\_template\_kwargs `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.default_chat_template_kwargs "Permanent link")

```
default_chat_template_kwargs: dict[str, Any] | None = None
```

Default keyword arguments to pass to the chat template renderer. These will be merged with request-level chat\_template\_kwargs, with request values taking precedence. Useful for setting default behavior for reasoning models. Example: '{"enable\_thinking": false}' to disable thinking mode by default for Qwen3/DeepSeek models.

### enable\_auto\_tool\_choice `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.enable_auto_tool_choice "Permanent link")

```
enable_auto_tool_choice: bool = False
```

Enable auto tool choice for supported models. Use `--tool-call-parser` to specify which parser to use.

### enable\_force\_include\_usage `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.enable_force_include_usage "Permanent link")

```
enable_force_include_usage: bool = False
```

If set to True, including usage on every request.

### enable\_log\_deltas `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.enable_log_deltas "Permanent link")

```
enable_log_deltas: bool = True
```

If set to False, output deltas will not be logged. Relevant only if --enable-log-outputs is set.

### enable\_log\_outputs `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.enable_log_outputs "Permanent link")

```
enable_log_outputs: bool = False
```

If set to True, log model outputs (generations). Requires `--enable-log-requests`. As with `--enable-log-requests`, information is only logged at INFO level at maximum.

### enable\_prompt\_tokens\_details `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.enable_prompt_tokens_details "Permanent link")

```
enable_prompt_tokens_details: bool = False
```

If set to True, enable prompt\_tokens\_details in usage.

### enable\_server\_load\_tracking `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.enable_server_load_tracking "Permanent link")

```
enable_server_load_tracking: bool = False
```

If set to True, enable tracking server\_load\_metrics in the app state.

### enable\_tokenizer\_info\_endpoint `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.enable_tokenizer_info_endpoint "Permanent link")

```
enable_tokenizer_info_endpoint: bool = False
```

Enable the `/tokenizer_info` endpoint. May expose chat templates and other tokenizer configuration.

### exclude\_tools\_when\_tool\_choice\_none `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.exclude_tools_when_tool_choice_none "Permanent link")

```
exclude_tools_when_tool_choice_none: bool = False
```

If specified, exclude tool definitions in prompts when tool\_choice='none'.

### fingerprint\_mode `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.fingerprint_mode "Permanent link")

```
fingerprint_mode: Literal[
    "full", "hash", "custom", "none"
] = "full"
```

Controls the `system_fingerprint` field on responses.

- `full` (default): `vllm-<version>[-<parallelism>]-<hash8>`. Encodes server version, non-trivial parallelism degrees (tp/pp/dp/ep), and an 8-char config hash.
- `hash`: `vllm-<version>-<hash8>`. Parallelism stripped.
- `custom`: emits the literal string from `--fingerprint-value`.
- `none`: the field is omitted (serialized as `null`).

### fingerprint\_value `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.fingerprint_value "Permanent link")

```
fingerprint_value: str | None = None
```

Literal fingerprint string used when `--fingerprint-mode=custom`.

### log\_config\_file `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.log_config_file "Permanent link")

```
log_config_file: str | None = VLLM_LOGGING_CONFIG_PATH
```

Path to logging config JSON file for both vllm and uvicorn

### log\_error\_stack `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.log_error_stack "Permanent link")

```
log_error_stack: bool = VLLM_SERVER_DEV_MODE
```

If set to True, log the stack trace of error responses

### lora\_modules `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.lora_modules "Permanent link")

```
lora_modules: list[LoRAModulePath] | None = None
```

LoRA modules configurations in either 'name=path' format or JSON format or JSON list format. Example (old format): `'name=path'` Example (new format): `{"name": "name", "path": "lora_path", "base_model_name": "id"}`

### max\_log\_len `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.max_log_len "Permanent link")

```
max_log_len: int | None = None
```

Max number of prompt characters or prompt ID numbers being printed in log. The default of None means unlimited.

### response\_role `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.response_role "Permanent link")

```
response_role: str = 'assistant'
```

The role name to return if `request.add_generation_prompt=true`.

### return\_tokens\_as\_token\_ids `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.return_tokens_as_token_ids "Permanent link")

```
return_tokens_as_token_ids: bool = False
```

When `--max-logprobs` is specified, represents single tokens as strings of the form 'token\_id:{token\_id}' so that tokens that are not JSON-encodable can be identified.

### tokens\_only `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.tokens_only "Permanent link")

```
tokens_only: bool = False
```

If set to True, only enable the Tokens In&lt;&gt;Out endpoint. This is intended for use in a Disaggregated Everything setup.

### tool\_call\_parser `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.tool_call_parser "Permanent link")

```
tool_call_parser: str | None = None
```

Select the tool call parser depending on the model that you're using. This is used to parse the model-generated tool call into OpenAI API format. Required for `--enable-auto-tool-choice`. You can choose any option from the built-in parsers or register a plugin via `--tool-parser-plugin`.

### tool\_parser\_plugin `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.tool_parser_plugin "Permanent link")

```
tool_parser_plugin: str = ''
```

Special the tool parser plugin write to parse the model-generated tool into OpenAI API format, the name register in this plugin can be used in `--tool-call-parser`.

### tool\_server `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.tool_server "Permanent link")

```
tool_server: str | None = None
```

Comma-separated list of host:port pairs (IPv4, IPv6, or hostname). Examples: 127.0.0.1:8000, \[::1]:8000, localhost:1234. Or `demo` for built-in demo tools (browser and Python code interpreter). WARNING: The `demo` Python tool executes model-generated code in Docker without network isolation by default. See the security guide for more information.

### trust\_request\_chat\_template `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.trust_request_chat_template "Permanent link")

```
trust_request_chat_template: bool = False
```

Whether to trust the chat template provided in the request. If False, the server will always use the chat template specified by `--chat-template` or the ones from tokenizer.

### \_customize\_cli\_kwargs `classmethod` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs._customize_cli_kwargs "Permanent link")

Customize argparse kwargs before arguments are registered.

Subclasses should override this and call `super()._customize_cli_kwargs(frontend_kwargs)` first.

Source code in `vllm/entrypoints/openai/cli_args.py`

```
@classmethod
def_customize_cli_kwargs(
    cls,
    frontend_kwargs: dict[str, Any],
) -> dict[str, Any]:
"""Customize argparse kwargs before arguments are registered.

    Subclasses should override this and call
    ``super()._customize_cli_kwargs(frontend_kwargs)`` first.
    """
    # Special case: default_chat_template_kwargs needs json.loads type
    frontend_kwargs["default_chat_template_kwargs"]["type"] = json.loads

    # Special case: LoRA modules need custom parser action and
    # optional_type(str)
    frontend_kwargs["lora_modules"]["type"] = optional_type(str)
    frontend_kwargs["lora_modules"]["action"] = LoRAParserAction

    # Special case: Tool call parser shows built-in options.
    valid_tool_parsers = list(ToolParserManager.list_registered())
    parsers_str = ",".join(valid_tool_parsers)
    frontend_kwargs["tool_call_parser"]["metavar"] = (
        f"{{{parsers_str}}} or name registered in --tool-parser-plugin"
    )
    return frontend_kwargs
```

### add\_cli\_args `classmethod` [¶](#vllm.entrypoints.openai.cli_args.BaseFrontendArgs.add_cli_args "Permanent link")

Register CLI arguments for this frontend class.

Subclasses should override `_customize_cli_kwargs` instead of this method so that base-class postprocessing is always applied.

Source code in `vllm/entrypoints/openai/cli_args.py`

```
@classmethod
defadd_cli_args(cls, parser: FlexibleArgumentParser) -> FlexibleArgumentParser:
"""Register CLI arguments for this frontend class.

    Subclasses should override ``_customize_cli_kwargs`` instead of
    this method so that base-class postprocessing is always applied.
    """
    fromvllm.engine.arg_utilsimport get_kwargs

    frontend_kwargs = get_kwargs(cls)
    frontend_kwargs = cls._customize_cli_kwargs(frontend_kwargs)

    group_name = cls.__name__.replace("Args", "")
    frontend_group = parser.add_argument_group(
        title=group_name,
        description=cls.__doc__,
    )
    for key, value in frontend_kwargs.items():
        extra_flags = value.pop("flags", [])
        frontend_group.add_argument(
            *extra_flags, f"--{key.replace('_','-')}", **value
        )

    return parser
```

## FrontendArgs [¶](#vllm.entrypoints.openai.cli_args.FrontendArgs "Permanent link")

Bases: `BaseFrontendArgs`

Arguments for the OpenAI-compatible frontend server.

Source code in `vllm/entrypoints/openai/cli_args.py`

```
@config
classFrontendArgs(BaseFrontendArgs):
"""Arguments for the OpenAI-compatible frontend server."""

    host: str | None = None
"""Host name."""
    port: int = 8000
"""Port number."""
    uds: str | None = None
"""Unix domain socket path. If set, host and port arguments are ignored."""
    uvicorn_log_level: Literal[
        "critical", "error", "warning", "info", "debug", "trace"
    ] = "info"
"""Log level for uvicorn."""
    disable_uvicorn_access_log: bool = False
"""Disable uvicorn access log."""
    disable_access_log_for_endpoints: str | None = None
"""Comma-separated list of endpoint paths to exclude from uvicorn access
    logs. This is useful to reduce log noise from high-frequency endpoints
    like health checks. Example: "/health,/metrics,/ping".
    When set, access logs for requests to these paths will be suppressed
    while keeping logs for other endpoints."""
    allow_credentials: bool = False
"""Allow credentials."""
    allowed_origins: list[str] = field(default_factory=lambda: ["*"])
"""Allowed origins."""
    allowed_methods: list[str] = field(default_factory=lambda: ["*"])
"""Allowed methods."""
    allowed_headers: list[str] = field(default_factory=lambda: ["*"])
"""Allowed headers."""
    api_key: list[str] | None = None
"""If provided, the server will require one of these keys to be presented in
    the header."""
    ssl_keyfile: str | None = None
"""The file path to the SSL key file."""
    ssl_certfile: str | None = None
"""The file path to the SSL cert file."""
    ssl_ca_certs: str | None = None
"""The CA certificates file."""
    enable_ssl_refresh: bool = False
"""Refresh SSL Context when SSL certificate files change"""
    ssl_cert_reqs: int = int(ssl.CERT_NONE)
"""Whether client certificate is required (see stdlib ssl module's)."""
    ssl_ciphers: str | None = None
"""SSL cipher suites for HTTPS (TLS 1.2 and below only).
    Example: 'ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-CHACHA20-POLY1305'"""
    root_path: str | None = None
"""FastAPI root_path when app is behind a path based routing proxy."""
    middleware: list[str] = field(default_factory=lambda: [])
"""Additional ASGI middleware to apply to the app. We accept multiple
    --middleware arguments. The value should be an import path. If a function
    is provided, vLLM will add it to the server using
    `@app.middleware('http')`. If a class is provided, vLLM will
    add it to the server using `app.add_middleware()`."""
    enable_request_id_headers: bool = False
"""If specified, API server will add X-Request-Id header to responses."""
    disable_fastapi_docs: bool = False
"""Disable FastAPI's OpenAPI schema, Swagger UI, and ReDoc endpoint."""
    h11_max_incomplete_event_size: int = H11_MAX_INCOMPLETE_EVENT_SIZE_DEFAULT
"""Maximum size (bytes) of an incomplete HTTP event (header or body) for
    h11 parser. Helps mitigate header abuse. Default: 4194304 (4 MB)."""
    h11_max_header_count: int = H11_MAX_HEADER_COUNT_DEFAULT
"""Maximum number of HTTP headers allowed in a request for h11 parser.
    Helps mitigate header abuse. Default: 256."""
    enable_offline_docs: bool = False
"""
    Enable offline FastAPI documentation for air-gapped environments.
    Uses vendored static assets bundled with vLLM.
    """
    enable_flash_late_interaction: bool = True
"""If set, run pooling score MaxSim on GPU in the API server process.
    Can significantly improve late-interaction scoring performance."""

    @classmethod
    def_customize_cli_kwargs(
        cls,
        frontend_kwargs: dict[str, Any],
    ) -> dict[str, Any]:
        frontend_kwargs = super()._customize_cli_kwargs(frontend_kwargs)

        # Special case: allowed_origins, allowed_methods, allowed_headers all
        # need json.loads type
        # Should also remove nargs
        frontend_kwargs["allowed_origins"]["type"] = json.loads
        frontend_kwargs["allowed_methods"]["type"] = json.loads
        frontend_kwargs["allowed_headers"]["type"] = json.loads
        del frontend_kwargs["allowed_origins"]["nargs"]
        del frontend_kwargs["allowed_methods"]["nargs"]
        del frontend_kwargs["allowed_headers"]["nargs"]

        # Special case: Middleware needs to append action
        frontend_kwargs["middleware"]["action"] = "append"
        frontend_kwargs["middleware"]["type"] = str
        if "nargs" in frontend_kwargs["middleware"]:
            del frontend_kwargs["middleware"]["nargs"]
        frontend_kwargs["middleware"]["default"] = []

        # Special case: disable_access_log_for_endpoints is a single
        # comma-separated string, not a list
        if "nargs" in frontend_kwargs["disable_access_log_for_endpoints"]:
            del frontend_kwargs["disable_access_log_for_endpoints"]["nargs"]

        return frontend_kwargs
```

### allow\_credentials `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.FrontendArgs.allow_credentials "Permanent link")

```
allow_credentials: bool = False
```

Allow credentials.

```
allowed_headers: list[str] = field(
    default_factory=lambda: ["*"]
)
```

Allowed headers.

### allowed\_methods `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.FrontendArgs.allowed_methods "Permanent link")

```
allowed_methods: list[str] = field(
    default_factory=lambda: ["*"]
)
```

Allowed methods.

### allowed\_origins `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.FrontendArgs.allowed_origins "Permanent link")

```
allowed_origins: list[str] = field(
    default_factory=lambda: ["*"]
)
```

Allowed origins.

### api\_key `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.FrontendArgs.api_key "Permanent link")

If provided, the server will require one of these keys to be presented in the header.

### disable\_access\_log\_for\_endpoints `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.FrontendArgs.disable_access_log_for_endpoints "Permanent link")

```
disable_access_log_for_endpoints: str | None = None
```

Comma-separated list of endpoint paths to exclude from uvicorn access logs. This is useful to reduce log noise from high-frequency endpoints like health checks. Example: "/health,/metrics,/ping". When set, access logs for requests to these paths will be suppressed while keeping logs for other endpoints.

### disable\_fastapi\_docs `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.FrontendArgs.disable_fastapi_docs "Permanent link")

```
disable_fastapi_docs: bool = False
```

Disable FastAPI's OpenAPI schema, Swagger UI, and ReDoc endpoint.

### disable\_uvicorn\_access\_log `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.FrontendArgs.disable_uvicorn_access_log "Permanent link")

```
disable_uvicorn_access_log: bool = False
```

Disable uvicorn access log.

### enable\_flash\_late\_interaction `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.FrontendArgs.enable_flash_late_interaction "Permanent link")

```
enable_flash_late_interaction: bool = True
```

If set, run pooling score MaxSim on GPU in the API server process. Can significantly improve late-interaction scoring performance.

### enable\_offline\_docs `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.FrontendArgs.enable_offline_docs "Permanent link")

```
enable_offline_docs: bool = False
```

Enable offline FastAPI documentation for air-gapped environments. Uses vendored static assets bundled with vLLM.

```
enable_request_id_headers: bool = False
```

If specified, API server will add X-Request-Id header to responses.

### enable\_ssl\_refresh `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.FrontendArgs.enable_ssl_refresh "Permanent link")

```
enable_ssl_refresh: bool = False
```

Refresh SSL Context when SSL certificate files change

```
h11_max_header_count: int = H11_MAX_HEADER_COUNT_DEFAULT
```

Maximum number of HTTP headers allowed in a request for h11 parser. Helps mitigate header abuse. Default: 256.

### h11\_max\_incomplete\_event\_size `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.FrontendArgs.h11_max_incomplete_event_size "Permanent link")

```
h11_max_incomplete_event_size: int = (
    H11_MAX_INCOMPLETE_EVENT_SIZE_DEFAULT
)
```

Maximum size (bytes) of an incomplete HTTP event (header or body) for h11 parser. Helps mitigate header abuse. Default: 4194304 (4 MB).

### host `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.FrontendArgs.host "Permanent link")

Host name.

### middleware `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.FrontendArgs.middleware "Permanent link")

Additional ASGI middleware to apply to the app. We accept multiple --middleware arguments. The value should be an import path. If a function is provided, vLLM will add it to the server using `@app.middleware('http')`. If a class is provided, vLLM will add it to the server using `app.add_middleware()`.

### port `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.FrontendArgs.port "Permanent link")

Port number.

### root\_path `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.FrontendArgs.root_path "Permanent link")

```
root_path: str | None = None
```

FastAPI root\_path when app is behind a path based routing proxy.

### ssl\_ca\_certs `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.FrontendArgs.ssl_ca_certs "Permanent link")

```
ssl_ca_certs: str | None = None
```

The CA certificates file.

### ssl\_cert\_reqs `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.FrontendArgs.ssl_cert_reqs "Permanent link")

Whether client certificate is required (see stdlib ssl module's).

### ssl\_certfile `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.FrontendArgs.ssl_certfile "Permanent link")

```
ssl_certfile: str | None = None
```

The file path to the SSL cert file.

### ssl\_ciphers `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.FrontendArgs.ssl_ciphers "Permanent link")

```
ssl_ciphers: str | None = None
```

SSL cipher suites for HTTPS (TLS 1.2 and below only). Example: 'ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-CHACHA20-POLY1305'

### ssl\_keyfile `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.FrontendArgs.ssl_keyfile "Permanent link")

```
ssl_keyfile: str | None = None
```

The file path to the SSL key file.

### uds `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.FrontendArgs.uds "Permanent link")

Unix domain socket path. If set, host and port arguments are ignored.

### uvicorn\_log\_level `class-attribute` `instance-attribute` [¶](#vllm.entrypoints.openai.cli_args.FrontendArgs.uvicorn_log_level "Permanent link")

```
uvicorn_log_level: Literal[
    "critical", "error", "warning", "info", "debug", "trace"
] = "info"
```

Log level for uvicorn.

## make\_arg\_parser [¶](#vllm.entrypoints.openai.cli_args.make_arg_parser "Permanent link")

Create the CLI argument parser used by the OpenAI API server.

We rely on the helper methods of `FrontendArgs` and `AsyncEngineArgs` to register all arguments instead of manually enumerating them here. This avoids code duplication and keeps the argument definitions in one place.

Source code in `vllm/entrypoints/openai/cli_args.py`

```
defmake_arg_parser(parser: FlexibleArgumentParser) -> FlexibleArgumentParser:
"""Create the CLI argument parser used by the OpenAI API server.

    We rely on the helper methods of `FrontendArgs` and `AsyncEngineArgs` to
    register all arguments instead of manually enumerating them here. This
    avoids code duplication and keeps the argument definitions in one place.
    """
    parser.add_argument(
        "model_tag",
        type=str,
        nargs="?",
        help="The model tag to serve (optional if specified in config)",
    )
    parser.add_argument(
        "--headless",
        action="store_true",
        default=False,
        help="Run in headless mode. See multi-node data parallel "
        "documentation for more details.",
    )
    parser.add_argument(
        "--api-server-count",
        "-asc",
        type=int,
        default=None,
        help="How many API server processes to run. "
        "Defaults to data_parallel_size if not specified.",
    )
    parser.add_argument(
        "--config",
        help="Read CLI options from a config file. "
        "Must be a YAML with the following options: "
        "https://docs.vllm.ai/en/latest/configuration/serve_args.html",
    )
    parser.add_argument(
        "--grpc",
        action="store_true",
        default=False,
        help="Launch a gRPC server instead of the HTTP OpenAI-compatible "
        "server. Requires: pip install vllm[grpc].",
    )
    parser = FrontendArgs.add_cli_args(parser)
    parser = AsyncEngineArgs.add_cli_args(parser)

    return parser
```

## validate\_parsed\_serve\_args [¶](#vllm.entrypoints.openai.cli_args.validate_parsed_serve_args "Permanent link")

Quick checks for model serve args that raise prior to loading.

Source code in `vllm/entrypoints/openai/cli_args.py`

```
defvalidate_parsed_serve_args(args: argparse.Namespace):
"""Quick checks for model serve args that raise prior to loading."""
    if hasattr(args, "subparser") and args.subparser != "serve":
        return

    # Ensure that the chat template is valid; raises if it likely isn't
    validate_chat_template(args.chat_template)

    # Enable auto tool needs a tool call parser to be valid
    if args.enable_auto_tool_choice and not args.tool_call_parser:
        raise TypeError("Error: --enable-auto-tool-choice requires --tool-call-parser")
    if args.enable_log_outputs and not args.enable_log_requests:
        raise TypeError("Error: --enable-log-outputs requires --enable-log-requests")
```