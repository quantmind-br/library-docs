---
title: offline_docs - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/instrumentator/offline_docs/
source: sitemap
fetched_at: 2026-05-07T21:21:32.030888954-03:00
rendered_js: false
word_count: 23
summary: This module provides a mechanism to serve FastAPI documentation using locally hosted static assets, enabling access to API documentation in air-gapped environments.
tags:
    - fastapi
    - offline-docs
    - air-gapped-deployment
    - documentation-server
    - static-files
category: api
---

## vllm.entrypoints.serve.instrumentator.offline\_docs [¶](#vllm.entrypoints.serve.instrumentator.offline_docs "Permanent link")

Offline FastAPI documentation support for air-gapped environments.

## attach\_router [¶](#vllm.entrypoints.serve.instrumentator.offline_docs.attach_router "Permanent link")

```
attach_router(app: FastAPI) -> None
```

Attach offline docs router if enabled via args.

Source code in `vllm/entrypoints/serve/instrumentator/offline_docs.py`

```
defattach_router(app: FastAPI) -> None:
"""Attach offline docs router if enabled via args."""
    args = getattr(app.state, "args", None)
    if args is None or not getattr(args, "enable_offline_docs", False):
        return

    static_dir = pathlib.Path(__file__).parent / "static"

    if not static_dir.exists():
        logger.warning(
            "Static directory not found at %s. Offline docs will not be available.",
            static_dir,
        )
        return

    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

    @app.get("/docs", include_in_schema=False)
    async defcustom_swagger_ui_html():
        return get_swagger_ui_html(
            openapi_url=app.openapi_url,
            title=app.title + " - Swagger UI",
            oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
            swagger_js_url="/static/swagger-ui-bundle.js",
            swagger_css_url="/static/swagger-ui.css",
        )

    @app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
    async defswagger_ui_redirect():
        return get_swagger_ui_oauth2_redirect_html()

    logger.info("Offline documentation enabled with vendored static assets")
```