---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/nixl/utils/
source: sitemap
fetched_at: 2026-05-07T21:18:44.724885102-03:00
rendered_js: false
word_count: 24
summary: This document provides utility functions and helper constants for managing ZMQ sockets within the vLLM NIXL distributed KV transfer connector.
tags:
    - distributed-computing
    - zmq-sockets
    - context-manager
    - kv-transfer
    - vllm-internals
category: reference
---

## vllm.distributed.kv\_transfer.kv\_connector.v1.nixl.utils [¶](#vllm.distributed.kv_transfer.kv_connector.v1.nixl.utils "Permanent link")

Shared constants, lazy imports and helpers for the NIXL connector.

## zmq\_ctx [¶](#vllm.distributed.kv_transfer.kv_connector.v1.nixl.utils.zmq_ctx "Permanent link")

Context manager for a ZMQ socket

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/nixl/utils.py`

```
@contextlib.contextmanager
defzmq_ctx(socket_type: Any, addr: str) -> Iterator[zmq.Socket]:
"""Context manager for a ZMQ socket"""

    if socket_type not in (zmq.ROUTER, zmq.REQ):
        raise ValueError(f"Unexpected socket type: {socket_type}")

    ctx: zmq.Context | None = None
    try:
        ctx = zmq.Context()  # type: ignore[attr-defined]
        yield make_zmq_socket(
            ctx=ctx, path=addr, socket_type=socket_type, bind=socket_type == zmq.ROUTER
        )
    finally:
        if ctx is not None:
            ctx.destroy(linger=0)
```