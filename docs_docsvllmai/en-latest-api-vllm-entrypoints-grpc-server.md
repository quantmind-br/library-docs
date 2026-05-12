---
title: grpc_server - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/grpc_server/
source: sitemap
fetched_at: 2026-05-07T21:19:39.752904417-03:00
rendered_js: false
word_count: 0
summary: This code implements the main entry point and lifecycle management for a vLLM gRPC server, including engine initialization, service registration, and graceful shutdown handling.
tags:
    - grpc-server
    - vllm-engine
    - asyncio
    - python-backend
    - microservices
category: api
---

```
async defserve_grpc(args: argparse.Namespace):
"""
    Main gRPC serving function.

    Args:
        args: Parsed command line arguments
    """
    log_version_and_model(logger, VLLM_VERSION, args.model)
    logger.info("vLLM gRPC server args: %s", args)

    start_time = time.time()

    # Create engine args
    engine_args = AsyncEngineArgs.from_cli_args(args)

    # Build vLLM config
    vllm_config = engine_args.create_engine_config(
        usage_context=UsageContext.OPENAI_API_SERVER,
    )

    # Create AsyncLLM
    async_llm = AsyncLLM.from_vllm_config(
        vllm_config=vllm_config,
        usage_context=UsageContext.OPENAI_API_SERVER,
        enable_log_requests=args.enable_log_requests,
        disable_log_stats=args.disable_log_stats,
    )

    # Create servicer
    servicer = VllmEngineServicer(async_llm, start_time)

    # Create gRPC server
    server = grpc.aio.server(
        options=[
            ("grpc.max_send_message_length", -1),
            ("grpc.max_receive_message_length", -1),
            # Tolerate client keepalive pings every 10s (default 300s is too
            # strict for non-streaming requests where no DATA frames flow
            # during generation)
            ("grpc.http2.min_recv_ping_interval_without_data_ms", 10000),
            ("grpc.keepalive_permit_without_calls", True),
        ],
    )

    # Add servicer to server
    vllm_engine_pb2_grpc.add_VllmEngineServicer_to_server(servicer, server)

    # Add standard gRPC health service for Kubernetes probes
    health_servicer = VllmHealthServicer(async_llm)
    health_pb2_grpc.add_HealthServicer_to_server(health_servicer, server)

    # Enable reflection for grpcurl and other tools
    service_names = (
        vllm_engine_pb2.DESCRIPTOR.services_by_name["VllmEngine"].full_name,
        "grpc.health.v1.Health",
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(service_names, server)

    # Bind to address
    host = args.host or "0.0.0.0"
    address = f"{host}:{args.port}"
    server.add_insecure_port(address)

    try:
        # Start server
        await server.start()
        logger.info("vLLM gRPC server started on %s", address)
        logger.info("Server is ready to accept requests")

        # Start periodic stats logging (mirrors the HTTP server's lifespan task)
        if not args.disable_log_stats:

            async def_force_log():
                while True:
                    await asyncio.sleep(envs.VLLM_LOG_STATS_INTERVAL)
                    await async_llm.do_log_stats()

            stats_task = asyncio.create_task(_force_log())
        else:
            stats_task = None

        # Handle shutdown signals
        loop = asyncio.get_running_loop()
        stop_event = asyncio.Event()

        defsignal_handler():
            logger.info("Received shutdown signal")
            stop_event.set()

        for sig in (signal.SIGTERM, signal.SIGINT):
            loop.add_signal_handler(sig, signal_handler)

        try:
            await stop_event.wait()
        except KeyboardInterrupt:
            logger.info("Interrupted by user")
    finally:
        logger.info("Shutting down vLLM gRPC server...")
        if stats_task is not None:
            stats_task.cancel()
        try:
            health_servicer.set_not_serving()
        except Exception:  # broad: must not prevent server.stop() / shutdown()
            logger.warning("Failed to set health status to NOT_SERVING", exc_info=True)
        await server.stop(grace=5.0)
        logger.info("gRPC server stopped")
        async_llm.shutdown()
        logger.info("AsyncLLM engine stopped")
        logger.info("Shutdown complete")
```