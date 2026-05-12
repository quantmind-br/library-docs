---
title: server_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/openai/server_utils/
source: sitemap
fetched_at: 2026-05-07T21:20:36.23931054-03:00
rendered_js: false
word_count: 150
summary: This document describes the exception handling architecture for the VLLM V1 AsyncLLM engine, detailing how specific engine errors are caught, classified, and managed within a FastAPI application.
tags:
    - vllm
    - exception-handling
    - error-management
    - fastapi
    - async-llm
    - backend-development
category: concept
---

VLLM V1 AsyncLLM catches exceptions and returns only two types: EngineGenerateError and EngineDeadError.

EngineGenerateError is raised by the per request generate() method. This error could be request specific (and therefore recoverable - e.g. if there is an error in input processing).

EngineDeadError is raised by the background output\_handler method. This error is global and therefore not recoverable.

We register these @app.exception\_handlers to return nice responses to the end user if they occur and shut down if needed. See https://fastapi.tiangolo.com/tutorial/handling-errors/ for more details on how exception handlers work.

If an exception is encountered in a StreamingResponse generator, the exception is not raised, since we already sent a 200 status. Rather, we send an error message as the next chunk. Since the exception is not raised, this means that the server will not automatically shut down. Instead, we use the watchdog background task for check for errored state.

Source code in `vllm/entrypoints/openai/server_utils.py`

```
async defengine_error_handler(
    req: Request, exc: EngineDeadError | EngineGenerateError
):
"""
    VLLM V1 AsyncLLM catches exceptions and returns
    only two types: EngineGenerateError and EngineDeadError.

    EngineGenerateError is raised by the per request generate()
    method. This error could be request specific (and therefore
    recoverable - e.g. if there is an error in input processing).

    EngineDeadError is raised by the background output_handler
    method. This error is global and therefore not recoverable.

    We register these @app.exception_handlers to return nice
    responses to the end user if they occur and shut down if needed.
    See https://fastapi.tiangolo.com/tutorial/handling-errors/
    for more details on how exception handlers work.

    If an exception is encountered in a StreamingResponse
    generator, the exception is not raised, since we already sent
    a 200 status. Rather, we send an error message as the next chunk.
    Since the exception is not raised, this means that the server
    will not automatically shut down. Instead, we use the watchdog
    background task for check for errored state.
    """

    if req.app.state.args.log_error_stack:
        logger.exception(
            "Engine Exception caught. Request id: %s",
            req.state.request_metadata.request_id
            if hasattr(req.state, "request_metadata")
            else None,
        )

    terminate_if_errored(
        server=req.app.state.server,
        engine=req.app.state.engine_client,
    )
    err = create_error_response(exc)
    return JSONResponse(err.model_dump(), status_code=err.error.code)
```