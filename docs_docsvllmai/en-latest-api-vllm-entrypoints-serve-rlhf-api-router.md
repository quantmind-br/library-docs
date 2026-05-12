---
title: api_router - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/rlhf/api_router/
source: sitemap
fetched_at: 2026-05-07T21:21:42.866329606-03:00
rendered_js: false
word_count: 163
summary: This document provides API documentation for RLHF control endpoints, allowing users to query parallel processing configuration, check engine status, and manage the pausing and resuming of generation tasks.
tags:
    - api-reference
    - vllm
    - rlhf
    - model-serving
    - parallel-processing
    - generation-control
category: api
---

## get\_world\_size `async` [¶](#vllm.entrypoints.serve.rlhf.api_router.get_world_size "Permanent link")

```
get_world_size(
    raw_request: Request, include_dp: bool = Query(True)
)
```

Get the world size from the parallel config.

Parameters:

Name Type Description Default `include_dp` `bool`

If True (default), returns the world size including data parallelism (TP * PP * DP). If False, returns the world size without data parallelism (TP * PP).

`Query(True)`

Source code in `vllm/entrypoints/serve/rlhf/api_router.py`

```
@router.get("/get_world_size")
async defget_world_size(
    raw_request: Request,
    include_dp: bool = Query(True),
):
"""Get the world size from the parallel config.

    Args:
        include_dp: If True (default), returns the world size including
            data parallelism (TP * PP * DP). If False, returns the world
            size without data parallelism (TP * PP).
    """
    parallel_config = engine_client(raw_request).vllm_config.parallel_config
    if include_dp:
        world_size = parallel_config.world_size_across_dp
    else:
        world_size = parallel_config.world_size
    return JSONResponse(content={"world_size": world_size})
```

## is\_paused `async` [¶](#vllm.entrypoints.serve.rlhf.api_router.is_paused "Permanent link")

```
is_paused(raw_request: Request) -> JSONResponse
```

Return the current pause status.

Source code in `vllm/entrypoints/serve/rlhf/api_router.py`

```
@router.get("/is_paused")
async defis_paused(raw_request: Request) -> JSONResponse:
"""Return the current pause status."""

    engine = engine_client(raw_request)

    try:
        paused = await engine.is_paused()
    except Exception as err:  # pragma: no cover - defensive
        logger.exception("Failed to fetch pause status")
        return JSONResponse(
            content={"error": f"Failed to fetch pause status: {err}"},
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value,
        )

    return JSONResponse(content={"is_paused": paused})
```

## pause\_generation `async` [¶](#vllm.entrypoints.serve.rlhf.api_router.pause_generation "Permanent link")

```
pause_generation(
    raw_request: Request,
    mode: Annotated[PauseMode, Query()] = "abort",
    wait_for_inflight_requests: bool = Query(False),
    clear_cache: Annotated[bool, Query()] = True,
) -> JSONResponse
```

Pause generation requests to allow weight updates.

Parameters:

Name Type Description Default `mode` `Annotated[PauseMode, Query()]`

How to handle in-flight requests: - `"abort"`: Abort all in-flight requests immediately (default). - `"wait"`: Wait for in-flight requests to complete. - `"keep"`: Freeze requests in queue; they resume on /resume.

`'abort'` `wait_for_inflight_requests` `bool`

DEPRECATED. Use `mode="wait"` instead.

`Query(False)` `clear_cache` `Annotated[bool, Query()]`

DEPRECATED. Whether to clear KV/prefix caches after draining. Ignored when mode="keep".

`True`

Source code in `vllm/entrypoints/serve/rlhf/api_router.py`

```
@router.post("/pause")
async defpause_generation(
    raw_request: Request,
    mode: Annotated[PauseMode, Query()] = "abort",
    wait_for_inflight_requests: bool = Query(False),
    clear_cache: Annotated[bool, Query()] = True,
) -> JSONResponse:
"""Pause generation requests to allow weight updates.

    Args:
        mode: How to handle in-flight requests:
            - ``"abort"``: Abort all in-flight requests immediately (default).
            - ``"wait"``: Wait for in-flight requests to complete.
            - ``"keep"``: Freeze requests in queue; they resume on /resume.
        wait_for_inflight_requests: DEPRECATED. Use ``mode="wait"`` instead.
        clear_cache: DEPRECATED. Whether to clear KV/prefix caches after
            draining. Ignored when mode="keep".
    """

    engine = engine_client(raw_request)

    try:
        await engine.pause_generation(
            mode=mode,
            clear_cache=clear_cache,
            wait_for_inflight_requests=wait_for_inflight_requests,
        )
        return JSONResponse(
            content={"status": "paused"},
            status_code=HTTPStatus.OK.value,
        )

    except ValueError as err:
        return JSONResponse(
            content={"error": str(err)},
            status_code=HTTPStatus.BAD_REQUEST.value,
        )
    except Exception as err:  # pragma: no cover - defensive
        logger.exception("Failed to pause generation")
        return JSONResponse(
            content={"error": f"Failed to pause generation: {err}"},
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value,
        )
```

## resume\_generation `async` [¶](#vllm.entrypoints.serve.rlhf.api_router.resume_generation "Permanent link")

```
resume_generation(raw_request: Request) -> JSONResponse
```

Resume generation after a pause.

Source code in `vllm/entrypoints/serve/rlhf/api_router.py`

```
@router.post("/resume")
async defresume_generation(raw_request: Request) -> JSONResponse:
"""Resume generation after a pause."""

    engine = engine_client(raw_request)

    try:
        await engine.resume_generation()
        return JSONResponse(
            content={"status": "resumed"},
            status_code=HTTPStatus.OK.value,
        )
    except Exception as err:  # pragma: no cover - defensive
        logger.exception("Failed to resume generation")
        return JSONResponse(
            content={"error": f"Failed to resume generation: {err}"},
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value,
        )
```