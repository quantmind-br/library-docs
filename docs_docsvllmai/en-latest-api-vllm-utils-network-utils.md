---
title: network_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/utils/network_utils/
source: sitemap
fetched_at: 2026-05-07T21:38:48.166113413-03:00
rendered_js: false
word_count: 201
summary: This document provides utility functions for managing network port allocation and ZeroMQ socket initialization, including configuration for binding, connection, and buffer settings.
tags:
    - network-utils
    - zmq-sockets
    - port-management
    - vllm-infrastructure
    - socket-configuration
category: api
---

## get\_open\_port [¶](#vllm.utils.network_utils.get_open_port "Permanent link")

Get an open port for the vLLM process to listen on. An edge case to handle, is when we run data parallel, we need to avoid ports that are potentially used by the data parallel master process. Right now we reserve 10 ports for the data parallel master process. Currently it uses 2 ports.

Source code in `vllm/utils/network_utils.py`

```
defget_open_port() -> int:
"""
    Get an open port for the vLLM process to listen on.
    An edge case to handle, is when we run data parallel,
    we need to avoid ports that are potentially used by
    the data parallel master process.
    Right now we reserve 10 ports for the data parallel master
    process. Currently it uses 2 ports.
    """
    if "VLLM_DP_MASTER_PORT" in os.environ:
        dp_master_port = envs.VLLM_DP_MASTER_PORT
        reserved_port_range = range(dp_master_port, dp_master_port + 10)
        while True:
            candidate_port = _get_open_port()
            if candidate_port not in reserved_port_range:
                return candidate_port
    return _get_open_port()
```

## get\_open\_ports\_list [¶](#vllm.utils.network_utils.get_open_ports_list "Permanent link")

Get a list of unique open ports.

When VLLM\_PORT is set, scans upward from that port, advancing the start position after each find so every port is unique.

Source code in `vllm/utils/network_utils.py`

```
defget_open_ports_list(count: int = 5) -> list[int]:
"""Get a list of unique open ports.

    When VLLM_PORT is set, scans upward from that port, advancing
    the start position after each find so every port is unique.
    """
    ports_set = set[int]()
    if envs.VLLM_PORT is not None:
        next_port = envs.VLLM_PORT
        for _ in range(count):
            port = _get_open_port(start_port=next_port, max_attempts=1000)
            ports_set.add(port)
            next_port = port + 1
        return list(ports_set)
    else:
        while len(ports_set) < count:
            ports_set.add(get_open_port())

    return list(ports_set)
```

## make\_zmq\_path [¶](#vllm.utils.network_utils.make_zmq_path "Permanent link")

```
make_zmq_path(
    scheme: str, host: str, port: int | None = None
) -> str
```

Make a ZMQ path from its parts.

Parameters:

Name Type Description Default `scheme` `str`

The ZMQ transport scheme (e.g. tcp, ipc, inproc).

*required* `host` `str`

The host - can be an IPv4 address, IPv6 address, or hostname.

*required* `port` `int | None`

Optional port number, only used for TCP sockets.

`None`

Returns:

Type Description `str`

A properly formatted ZMQ path string.

Source code in `vllm/utils/network_utils.py`

```
defmake_zmq_path(scheme: str, host: str, port: int | None = None) -> str:
"""Make a ZMQ path from its parts.

    Args:
        scheme: The ZMQ transport scheme (e.g. tcp, ipc, inproc).
        host: The host - can be an IPv4 address, IPv6 address, or hostname.
        port: Optional port number, only used for TCP sockets.

    Returns:
        A properly formatted ZMQ path string.
    """
    if port is None:
        return f"{scheme}://{host}"
    if is_valid_ipv6_address(host):
        return f"{scheme}://[{host}]:{port}"
    return f"{scheme}://{host}:{port}"
```

## make\_zmq\_socket [¶](#vllm.utils.network_utils.make_zmq_socket "Permanent link")

```
make_zmq_socket(
    ctx: Context | Context,
    path: str,
    socket_type: Any,
    bind: bool | None = None,
    identity: bytes | None = None,
    linger: int | None = None,
    router_handover: bool = False,
) -> Socket | Socket
```

Make a ZMQ socket with the proper bind/connect semantics.

Source code in `vllm/utils/network_utils.py`

```
defmake_zmq_socket(
    ctx: zmq.asyncio.Context | zmq.Context,  # type: ignore[name-defined]
    path: str,
    socket_type: Any,
    bind: bool | None = None,
    identity: bytes | None = None,
    linger: int | None = None,
    router_handover: bool = False,
) -> zmq.Socket | zmq.asyncio.Socket:  # type: ignore[name-defined]
"""Make a ZMQ socket with the proper bind/connect semantics."""

    mem = psutil.virtual_memory()
    socket = ctx.socket(socket_type)

    # Calculate buffer size based on system memory
    total_mem = mem.total / 1024**3
    available_mem = mem.available / 1024**3
    # For systems with substantial memory (>32GB total, >16GB available):
    # - Set a large 0.5GB buffer to improve throughput
    # For systems with less memory:
    # - Use system default (-1) to avoid excessive memory consumption
    buf_size = int(0.5 * 1024**3) if total_mem > 32 and available_mem > 16 else -1

    if bind is None:
        bind = socket_type not in (zmq.PUSH, zmq.SUB, zmq.XSUB)

    if socket_type in (zmq.PULL, zmq.DEALER, zmq.ROUTER):
        socket.setsockopt(zmq.RCVHWM, 0)
        socket.setsockopt(zmq.RCVBUF, buf_size)

    if socket_type in (zmq.PUSH, zmq.DEALER, zmq.ROUTER):
        socket.setsockopt(zmq.SNDHWM, 0)
        socket.setsockopt(zmq.SNDBUF, buf_size)

    if socket_type == zmq.ROUTER and router_handover:
        # Let a new connection take over an identity left behind by a dead one.
        socket.setsockopt(zmq.ROUTER_HANDOVER, 1)

    if identity is not None:
        socket.setsockopt(zmq.IDENTITY, identity)

    if linger is not None:
        socket.setsockopt(zmq.LINGER, linger)

    if socket_type == zmq.XPUB:
        socket.setsockopt(zmq.XPUB_VERBOSE, True)

    # Determine if the path is a TCP socket with an IPv6 address.
    # Enable IPv6 on the zmq socket if so.
    scheme, host, _ = split_zmq_path(path)
    if scheme == "tcp" and is_valid_ipv6_address(host):
        socket.setsockopt(zmq.IPV6, 1)

    if bind:
        socket.bind(path)
    else:
        socket.connect(path)

    return socket
```

## split\_zmq\_path [¶](#vllm.utils.network_utils.split_zmq_path "Permanent link")

Split a zmq path into its parts.

Source code in `vllm/utils/network_utils.py`

```
defsplit_zmq_path(path: str) -> tuple[str, str, str]:
"""Split a zmq path into its parts."""
    parsed = parse_url(path)
    if not parsed.scheme:
        raise ValueError(f"Invalid zmq path: {path}")

    scheme = parsed.scheme
    host = parsed.hostname or ""
    port = "" if parsed.port is None else str(parsed.port)
    if host.startswith("[") and host.endswith("]"):
        host = host[1:-1]  # Remove brackets for IPv6 address

    if scheme == "tcp" and not all((host, port)):
        # The host and port fields are required for tcp
        raise ValueError(f"Invalid zmq path: {path}")

    if scheme != "tcp" and port:
        # port only makes sense with tcp
        raise ValueError(f"Invalid zmq path: {path}")

    return scheme, host, port
```

## zmq\_socket\_ctx [¶](#vllm.utils.network_utils.zmq_socket_ctx "Permanent link")

```
zmq_socket_ctx(
    path: str,
    socket_type: Any,
    bind: bool | None = None,
    linger: int = 0,
    identity: bytes | None = None,
    router_handover: bool = False,
) -> Iterator[Socket]
```

Context manager for a ZMQ socket

Source code in `vllm/utils/network_utils.py`

```
@contextlib.contextmanager
defzmq_socket_ctx(
    path: str,
    socket_type: Any,
    bind: bool | None = None,
    linger: int = 0,
    identity: bytes | None = None,
    router_handover: bool = False,
) -> Iterator[zmq.Socket]:
"""Context manager for a ZMQ socket"""

    ctx = zmq.Context()  # type: ignore[attr-defined]
    try:
        yield make_zmq_socket(
            ctx,
            path,
            socket_type,
            bind=bind,
            identity=identity,
            router_handover=router_handover,
        )
    except KeyboardInterrupt:
        logger.debug("Got Keyboard Interrupt.")

    finally:
        ctx.destroy(linger=linger)
```