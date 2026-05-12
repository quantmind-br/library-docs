---
title: moriio_common - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common/
source: sitemap
fetched_at: 2026-05-07T21:18:34.726045003-03:00
rendered_js: false
word_count: 249
summary: This document defines the common data structures, constants, error types, and management utilities used for KV cache transfer operations within the MoRIIO connector architecture.
tags:
    - kv-transfer
    - vllm
    - distributed-computing
    - zmq
    - data-structures
    - moriio
category: reference
---

## HandshakeError [¶](#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.HandshakeError "Permanent link")

Bases: `MoRIIOError`

Exception raised when handshake fails.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`

```
classHandshakeError(MoRIIOError):
"""Exception raised when handshake fails."""

    pass
```

## LayerTransferPlan `dataclass` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.LayerTransferPlan "Permanent link")

Plan for transferring a single layer.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`

```
@dataclass
classLayerTransferPlan:
"""Plan for transferring a single layer."""

    request_id: ReqId
    transfer_id: TransferId
    layer_name: str
    sess_idx: int
    transfer_local_offsets: list[int]
    transfer_remote_offsets: list[int]
    transfer_sizes: list[int]
    use_batch: bool = True
```

## MoRIIOConstants [¶](#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.MoRIIOConstants "Permanent link")

Constants for MoRIIO connector.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`

```
classMoRIIOConstants:
"""Constants for MoRIIO connector."""

    # ZMQ message types
    GET_META_MSG = b"get_meta_msg"
    POP_DONE_RECV = b"pop_done_recv"
    OVER = b"OVER"
    COMPLETION_PREFIX = "cmpl"
    TRANSFER_PREFIX = "tx"

    PING_INTERVAL = 3
    MAX_PING_RETRIES = 100
    DEFAULT_HANDSHAKE_PORT = "6301"
    DEFAULT_NOTIFY_PORT = "61005"

    VLLM_MORI_READ_ABORT_REQUEST_TIMEOUT = 3600
```

## MoRIIOError [¶](#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.MoRIIOError "Permanent link")

Bases: `Exception`

Base exception for MoRIIO operations.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`

```
classMoRIIOError(Exception):
"""Base exception for MoRIIO operations."""

    pass
```

## RemoteAllocInfo `dataclass` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.RemoteAllocInfo "Permanent link")

Information about remote block allocation.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`

```
@dataclass
classRemoteAllocInfo:
"""Information about remote block allocation."""

    block_ids: list[int]
    writes_done: int = 0
    decode_dp_rank: int = 0
    transfer_offset: tuple[list[int], list[int], list[int]] | None = None
```

Metadata for a single request.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`

```
@dataclass
classReqMeta:
"""Metadata for a single request."""

    transfer_id: TransferId
    local_block_ids: list[int]
    remote_block_ids: list[int]
    remote_host: str
    remote_port: int
    remote_handshake_port: int
    remote_notify_port: int
    remote_engine_id: str
    tp_size: int
    remote_dp_size: int
```

## RoleManager [¶](#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.RoleManager "Permanent link")

Manages role state across the connector.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`

```
classRoleManager:
"""Manages role state across the connector."""

    _instance: "RoleManager | None" = None
    _lock = threading.Lock()

    def__init__(self) -> None:
        self._role: ROLE = ROLE.NOTINIT

    @classmethod
    defget_instance(cls) -> "RoleManager":
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance

    defset_role(self, role: ROLE) -> None:
"""Set the current role."""
        with self._lock:
            self._role = role

    defget_role(self) -> ROLE:
"""Get the current role."""
        return self._role
```

### get\_role [¶](#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.RoleManager.get_role "Permanent link")

Get the current role.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`

```
defget_role(self) -> ROLE:
"""Get the current role."""
    return self._role
```

### set\_role [¶](#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.RoleManager.set_role "Permanent link")

```
set_role(role: ROLE) -> None
```

Set the current role.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`

```
defset_role(self, role: ROLE) -> None:
"""Set the current role."""
    with self._lock:
        self._role = role
```

## TransferError [¶](#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.TransferError "Permanent link")

Bases: `MoRIIOError`

Exception raised when transfer fails.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`

```
classTransferError(MoRIIOError):
"""Exception raised when transfer fails."""

    pass
```

## get\_peer\_zmq\_from\_request\_id [¶](#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.get_peer_zmq_from_request_id "Permanent link")

```
get_peer_zmq_from_request_id(
    request_id: str, is_producer: bool
) -> str
```

Extract the *peer's* zmq\_address from the vLLM router request\_id.

The producer (prefill) needs the decode's address; the consumer (decode) needs the prefill's address.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`

```
defget_peer_zmq_from_request_id(request_id: str, is_producer: bool) -> str:
"""Extract the *peer's* zmq_address from the vLLM router request_id.

    The producer (prefill) needs the decode's address; the consumer (decode)
    needs the prefill's address.
    """
    if is_producer:
        m = _DECODE_ZMQ_RE.search(request_id)
    else:
        m = _PREFILL_ZMQ_RE.search(request_id)
    if m is None:
        raise ValueError(
            f"Cannot parse peer zmq_address from request_id: {request_id!r}"
        )
    return m.group(1)
```

## get\_role [¶](#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.get_role "Permanent link")

Get the global role.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`

```
defget_role() -> ROLE:
"""Get the global role."""
    return RoleManager.get_instance().get_role()
```

## parse\_moriio\_zmq\_address [¶](#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.parse_moriio_zmq_address "Permanent link")

Parse the MoRI-IO zmq address into its components.

Parses `"host:IP,handshake:PORT,notify:PORT"` into (host, handshake\_port, notify\_port).

Each key-value pair is split on the *first* colon so that IPv6 addresses (e.g. `host:::1`) are handled correctly. Raises `ValueError` if any of `host`, `handshake`, or `notify` keys are absent or if the port values are non-numeric.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`

```
defparse_moriio_zmq_address(
    zmq_address: str,
) -> tuple[str, int, int]:
"""Parse the MoRI-IO zmq address into its components.

    Parses ``"host:IP,handshake:PORT,notify:PORT"`` into
        (host, handshake_port, notify_port).

    Each key-value pair is split on the *first* colon so that IPv6 addresses
    (e.g. ``host:::1``) are handled correctly.  Raises ``ValueError`` if any
    of ``host``, ``handshake``, or ``notify`` keys are absent or if the port
    values are non-numeric.
    """
    parts: dict[str, str] = {}
    for segment in zmq_address.split(","):
        key, _, val = segment.partition(":")
        parts[key.strip()] = val.strip()
    try:
        host = parts["host"]
        handshake_port = int(parts["handshake"])
        notify_port = int(parts["notify"])
    except (KeyError, ValueError) as e:
        raise ValueError(
            f"Malformed zmq_address {zmq_address!r}: expected "
            f"'host:IP,handshake:PORT,notify:PORT' format"
        ) frome
    return host, handshake_port, notify_port
```

## set\_role [¶](#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.set_role "Permanent link")

Set the global role.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`

```
defset_role(role: ROLE):
"""Set the global role."""
    RoleManager.get_instance().set_role(role)
```

## zmq\_ctx [¶](#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.zmq_ctx "Permanent link")

Context manager for a ZMQ socket

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`

```
@contextlib.contextmanager
defzmq_ctx(socket_type: Any, addr: str) -> Iterator[zmq.Socket]:
"""Context manager for a ZMQ socket"""

    if socket_type not in (zmq.ROUTER, zmq.REQ, zmq.DEALER):
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