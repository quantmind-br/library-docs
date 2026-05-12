---
title: ssl - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/ssl/
source: sitemap
fetched_at: 2026-05-07T21:21:51.178430748-03:00
rendered_js: false
word_count: 40
summary: This document describes the SSLCertRefresher class, which provides functionality for asynchronously monitoring SSL certificate and CA file changes and automatically reloading them in an SSL context.
tags:
    - ssl-certificates
    - file-monitoring
    - asynchronous-tasks
    - security-configuration
    - vllm-infrastructure
category: reference
---

## SSLCertRefresher [¶](#vllm.entrypoints.ssl.SSLCertRefresher "Permanent link")

A class that monitors SSL certificate files and reloads them when they change.

Source code in `vllm/entrypoints/ssl.py`

```
classSSLCertRefresher:
"""A class that monitors SSL certificate files and
    reloads them when they change.
    """

    def__init__(
        self,
        ssl_context: SSLContext,
        key_path: str | None = None,
        cert_path: str | None = None,
        ca_path: str | None = None,
    ) -> None:
        self.ssl = ssl_context
        self.key_path = key_path
        self.cert_path = cert_path
        self.ca_path = ca_path

        # Setup certification chain watcher
        defupdate_ssl_cert_chain(change: Change, file_path: str) -> None:
            logger.info("Reloading SSL certificate chain")
            assert self.key_path and self.cert_path
            self.ssl.load_cert_chain(self.cert_path, self.key_path)

        self.watch_ssl_cert_task = None
        if self.key_path and self.cert_path:
            self.watch_ssl_cert_task = asyncio.create_task(
                self._watch_files(
                    [self.key_path, self.cert_path], update_ssl_cert_chain
                )
            )

        # Setup CA files watcher
        defupdate_ssl_ca(change: Change, file_path: str) -> None:
            logger.info("Reloading SSL CA certificates")
            assert self.ca_path
            self.ssl.load_verify_locations(self.ca_path)

        self.watch_ssl_ca_task = None
        if self.ca_path:
            self.watch_ssl_ca_task = asyncio.create_task(
                self._watch_files([self.ca_path], update_ssl_ca)
            )

    async def_watch_files(self, paths, fun: Callable[[Change, str], None]) -> None:
"""Watch multiple file paths asynchronously."""
        logger.info("SSLCertRefresher monitors files: %s", paths)
        async for changes in awatch(*paths):
            try:
                for change, file_path in changes:
                    logger.info("File change detected: %s - %s", change.name, file_path)
                    fun(change, file_path)
            except Exception as e:
                logger.error(
                    "SSLCertRefresher failed taking action on file change. Error: %s", e
                )

    defstop(self) -> None:
"""Stop watching files."""
        if self.watch_ssl_cert_task:
            self.watch_ssl_cert_task.cancel()
            self.watch_ssl_cert_task = None
        if self.watch_ssl_ca_task:
            self.watch_ssl_ca_task.cancel()
            self.watch_ssl_ca_task = None
```

### \_watch\_files `async` [¶](#vllm.entrypoints.ssl.SSLCertRefresher._watch_files "Permanent link")

```
_watch_files(
    paths, fun: Callable[[Change, str], None]
) -> None
```

Watch multiple file paths asynchronously.

Source code in `vllm/entrypoints/ssl.py`

```
async def_watch_files(self, paths, fun: Callable[[Change, str], None]) -> None:
"""Watch multiple file paths asynchronously."""
    logger.info("SSLCertRefresher monitors files: %s", paths)
    async for changes in awatch(*paths):
        try:
            for change, file_path in changes:
                logger.info("File change detected: %s - %s", change.name, file_path)
                fun(change, file_path)
        except Exception as e:
            logger.error(
                "SSLCertRefresher failed taking action on file change. Error: %s", e
            )
```

### stop [¶](#vllm.entrypoints.ssl.SSLCertRefresher.stop "Permanent link")

Stop watching files.

Source code in `vllm/entrypoints/ssl.py`

```
defstop(self) -> None:
"""Stop watching files."""
    if self.watch_ssl_cert_task:
        self.watch_ssl_cert_task.cancel()
        self.watch_ssl_cert_task = None
    if self.watch_ssl_ca_task:
        self.watch_ssl_ca_task.cancel()
        self.watch_ssl_ca_task = None
```