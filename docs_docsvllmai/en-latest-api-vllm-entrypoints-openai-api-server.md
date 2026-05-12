---
title: api_server - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/openai/api_server/
source: sitemap
fetched_at: 2026-05-07T21:19:47.997973082-03:00
rendered_js: false
word_count: 179
summary: This document provides technical reference documentation for the internal server initialization functions in the vLLM OpenAI-compatible API layer, covering FastAPI application construction, state management, and engine client configuration.
tags:
    - vllm
    - fastapi
    - server-initialization
    - engine-client
    - openai-api
    - python-async
category: api
---

## build\_and\_serve `async` [¶](#vllm.entrypoints.openai.api_server.build_and_serve "Permanent link")

Build FastAPI app, initialize state, and start serving.

Returns the shutdown task for the caller to await.

Source code in `vllm/entrypoints/openai/api_server.py`

```
async defbuild_and_serve(
    engine_client: EngineClient,
    listen_address: str,
    sock: socket.socket,
    args: Namespace,
    **uvicorn_kwargs,
) -> asyncio.Task:
"""Build FastAPI app, initialize state, and start serving.

    Returns the shutdown task for the caller to await.
    """

    # Get uvicorn log config (from file or with endpoint filter)
    log_config = get_uvicorn_log_config(args)
    if log_config is not None:
        uvicorn_kwargs["log_config"] = log_config

    supported_tasks = await engine_client.get_supported_tasks()
    model_config = engine_client.model_config

    logger.info("Supported tasks: %s", supported_tasks)
    app = build_app(args, supported_tasks, model_config)
    await init_app_state(engine_client, app.state, args, supported_tasks)

    logger.info("Starting vLLM server on %s", listen_address)

    return await serve_http(
        app,
        sock=sock,
        enable_ssl_refresh=args.enable_ssl_refresh,
        host=args.host,
        port=args.port,
        log_level=args.uvicorn_log_level,
        # NOTE: When the 'disable_uvicorn_access_log' value is True,
        # no access log will be output.
        access_log=not args.disable_uvicorn_access_log,
        timeout_keep_alive=envs.VLLM_HTTP_TIMEOUT_KEEP_ALIVE,
        ssl_keyfile=args.ssl_keyfile,
        ssl_certfile=args.ssl_certfile,
        ssl_ca_certs=args.ssl_ca_certs,
        ssl_cert_reqs=args.ssl_cert_reqs,
        ssl_ciphers=args.ssl_ciphers,
        h11_max_incomplete_event_size=args.h11_max_incomplete_event_size,
        h11_max_header_count=args.h11_max_header_count,
        **uvicorn_kwargs,
    )
```

## build\_and\_serve\_renderer `async` [¶](#vllm.entrypoints.openai.api_server.build_and_serve_renderer "Permanent link")

Build FastAPI app for a CPU-only render server, initialize state, and start serving.

Returns the shutdown task for the caller to await.

Source code in `vllm/entrypoints/openai/api_server.py`

```
async defbuild_and_serve_renderer(
    vllm_config: VllmConfig,
    listen_address: str,
    sock: socket.socket,
    args: Namespace,
    **uvicorn_kwargs,
) -> asyncio.Task:
"""Build FastAPI app for a CPU-only render server, initialize state, and
    start serving.

    Returns the shutdown task for the caller to await.
    """

    # Get uvicorn log config (from file or with endpoint filter)
    log_config = get_uvicorn_log_config(args)
    if log_config is not None:
        uvicorn_kwargs["log_config"] = log_config

    app = build_app(args, ("render",))
    await init_render_app_state(vllm_config, app.state, args)

    logger.info("Starting vLLM server on %s", listen_address)

    return await serve_http(
        app,
        sock=sock,
        enable_ssl_refresh=args.enable_ssl_refresh,
        host=args.host,
        port=args.port,
        log_level=args.uvicorn_log_level,
        # NOTE: When the 'disable_uvicorn_access_log' value is True,
        # no access log will be output.
        access_log=not args.disable_uvicorn_access_log,
        timeout_keep_alive=envs.VLLM_HTTP_TIMEOUT_KEEP_ALIVE,
        ssl_keyfile=args.ssl_keyfile,
        ssl_certfile=args.ssl_certfile,
        ssl_ca_certs=args.ssl_ca_certs,
        ssl_cert_reqs=args.ssl_cert_reqs,
        ssl_ciphers=args.ssl_ciphers,
        h11_max_incomplete_event_size=args.h11_max_incomplete_event_size,
        h11_max_header_count=args.h11_max_header_count,
        **uvicorn_kwargs,
    )
```

## build\_async\_engine\_client\_from\_engine\_args `async` [¶](#vllm.entrypoints.openai.api_server.build_async_engine_client_from_engine_args "Permanent link")

Create EngineClient, either: - in-process using the AsyncLLMEngine Directly - multiprocess using AsyncLLMEngine RPC

Returns the Client or None if the creation failed.

Source code in `vllm/entrypoints/openai/api_server.py`

```
@asynccontextmanager
async defbuild_async_engine_client_from_engine_args(
    engine_args: AsyncEngineArgs,
    *,
    usage_context: UsageContext = UsageContext.OPENAI_API_SERVER,
    client_config: dict[str, Any] | None = None,
) -> AsyncIterator[EngineClient]:
"""
    Create EngineClient, either:
        - in-process using the AsyncLLMEngine Directly
        - multiprocess using AsyncLLMEngine RPC

    Returns the Client or None if the creation failed.
    """

    # Create the EngineConfig (determines if we can use V1).
    vllm_config = engine_args.create_engine_config(usage_context=usage_context)

    fromvllm.v1.engine.async_llmimport AsyncLLM

    async_llm: AsyncLLM | None = None

    # Don't mutate the input client_config
    client_config = dict(client_config) if client_config else {}
    client_count = client_config.pop("client_count", 1)
    client_index = client_config.pop("client_index", 0)

    try:
        async_llm = AsyncLLM.from_vllm_config(
            vllm_config=vllm_config,
            usage_context=usage_context,
            enable_log_requests=engine_args.enable_log_requests,
            aggregate_engine_logging=engine_args.aggregate_engine_logging,
            disable_log_stats=engine_args.disable_log_stats,
            client_addresses=client_config,
            client_count=client_count,
            client_index=client_index,
        )

        # Don't keep the dummy data in memory
        assert async_llm is not None
        await async_llm.reset_mm_cache()

        yield async_llm
    finally:
        if async_llm:
            async_llm.shutdown()
```

## init\_render\_app\_state `async` [¶](#vllm.entrypoints.openai.api_server.init_render_app_state "Permanent link")

Initialise FastAPI app state for a CPU-only render server.

Unlike :func:`init_app_state` this function does not require an :class:`~vllm.engine.protocol.EngineClient`; it bootstraps the preprocessing pipeline (renderer, input\_processor) directly from the :class:`~vllm.config.VllmConfig`.

Source code in `vllm/entrypoints/openai/api_server.py`

```
async definit_render_app_state(
    vllm_config: VllmConfig,
    state: State,
    args: Namespace,
) -> None:
"""Initialise FastAPI app state for a CPU-only render server.

    Unlike :func:`init_app_state` this function does not require an
    :class:`~vllm.engine.protocol.EngineClient`; it bootstraps the
    preprocessing pipeline (renderer, input_processor)
    directly from the :class:`~vllm.config.VllmConfig`.
    """
    fromvllm.entrypoints.chat_utilsimport load_chat_template
    fromvllm.entrypoints.openai.models.servingimport OpenAIModelRegistry
    fromvllm.entrypoints.serve.render.servingimport OpenAIServingRender
    fromvllm.renderersimport renderer_from_config

    served_model_names = args.served_model_name or [args.model]
    model_registry = OpenAIModelRegistry(
        model_config=vllm_config.model_config,
        base_model_paths=[
            BaseModelPath(name=name, model_path=args.model)
            for name in served_model_names
        ],
    )

    if args.enable_log_requests:
        request_logger = RequestLogger(max_log_len=args.max_log_len)
    else:
        request_logger = None

    renderer = renderer_from_config(vllm_config)
    resolved_chat_template = load_chat_template(args.chat_template)

    state.openai_serving_render = OpenAIServingRender(
        model_config=vllm_config.model_config,
        renderer=renderer,
        model_registry=model_registry,
        request_logger=request_logger,
        chat_template=resolved_chat_template,
        chat_template_content_format=args.chat_template_content_format,
        trust_request_chat_template=args.trust_request_chat_template,
        enable_auto_tools=args.enable_auto_tool_choice,
        exclude_tools_when_tool_choice_none=args.exclude_tools_when_tool_choice_none,
        tool_parser=args.tool_call_parser,
        reasoning_parser=args.structured_outputs_config.reasoning_parser,
        default_chat_template_kwargs=args.default_chat_template_kwargs,
        log_error_stack=args.log_error_stack,
    )

    state.openai_serving_models = model_registry

    # Expose tokenization via the render handler (no engine required).
    state.openai_serving_tokenization = state.openai_serving_render

    state.vllm_config = vllm_config
    # Disable stats logging — there is no engine to poll.
    state.log_stats = False
    state.engine_client = None
    state.args = args
    state.enable_server_load_tracking = False
    state.server_load_metrics = 0
```

## run\_server `async` [¶](#vllm.entrypoints.openai.api_server.run_server "Permanent link")

```
run_server(args, **uvicorn_kwargs) -> None
```

Run a single-worker API server.

Source code in `vllm/entrypoints/openai/api_server.py`

```
async defrun_server(args, **uvicorn_kwargs) -> None:
"""Run a single-worker API server."""

    # Add process-specific prefix to stdout and stderr.
    decorate_logs("APIServer")

    listen_address, sock = setup_server(args)
    await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
```

## run\_server\_worker `async` [¶](#vllm.entrypoints.openai.api_server.run_server_worker "Permanent link")

```
run_server_worker(
    listen_address,
    sock,
    args,
    client_config=None,
    **uvicorn_kwargs,
) -> None
```

Run a single API server worker.

Source code in `vllm/entrypoints/openai/api_server.py`

```
async defrun_server_worker(
    listen_address, sock, args, client_config=None, **uvicorn_kwargs
) -> None:
"""Run a single API server worker."""

    if args.tool_parser_plugin and len(args.tool_parser_plugin) > 3:
        ToolParserManager.import_tool_parser(args.tool_parser_plugin)

    if args.reasoning_parser_plugin and len(args.reasoning_parser_plugin) > 3:
        ReasoningParserManager.import_reasoning_parser(args.reasoning_parser_plugin)

    async with build_async_engine_client(
        args,
        client_config=client_config,
    ) as engine_client:
        shutdown_task = await build_and_serve(
            engine_client, listen_address, sock, args, **uvicorn_kwargs
        )
    # NB: Await server shutdown only after the backend context is exited
    try:
        await shutdown_task
    finally:
        sock.close()
```

## setup\_server [¶](#vllm.entrypoints.openai.api_server.setup_server "Permanent link")

Validate API server args, set up signal handler, create socket ready to serve.

Source code in `vllm/entrypoints/openai/api_server.py`

```
@instrument(span_name="API server setup")
defsetup_server(args):
"""Validate API server args, set up signal handler, create socket
    ready to serve."""

    log_version_and_model(logger, VLLM_VERSION, args.model)
    log_non_default_args(args)

    if args.tool_parser_plugin and len(args.tool_parser_plugin) > 3:
        ToolParserManager.import_tool_parser(args.tool_parser_plugin)

    if args.reasoning_parser_plugin and len(args.reasoning_parser_plugin) > 3:
        ReasoningParserManager.import_reasoning_parser(args.reasoning_parser_plugin)

    validate_api_server_args(args)

    # workaround to make sure that we bind the port before the engine is set up.
    # This avoids race conditions with ray.
    # see https://github.com/vllm-project/vllm/issues/8204
    if args.uds:
        sock = create_server_unix_socket(args.uds)
    else:
        sock_addr = (args.host or "", args.port)
        sock = create_server_socket(sock_addr)

    # workaround to avoid footguns where uvicorn drops requests with too
    # many concurrent requests active
    set_ulimit()

    defsignal_handler(*_) -> None:
        # Interrupt server on sigterm while initializing
        raise KeyboardInterrupt("terminated")

    signal.signal(signal.SIGTERM, signal_handler)

    if args.uds:
        listen_address = f"unix:{args.uds}"
    else:
        addr, port = sock_addr
        is_ssl = args.ssl_keyfile and args.ssl_certfile
        host_part = f"[{addr}]" if is_valid_ipv6_address(addr) else addr or "0.0.0.0"
        listen_address = f"http{'s'ifis_sslelse''}://{host_part}:{port}"
    return listen_address, sock
```