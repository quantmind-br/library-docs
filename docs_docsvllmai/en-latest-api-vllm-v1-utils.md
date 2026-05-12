---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/utils/
source: sitemap
fetched_at: 2026-05-07T21:42:06.2280108-03:00
rendered_js: false
word_count: 148
summary: This document describes a utility class designed to manage the lifecycle of API server worker processes, including their initialization, concurrent execution, and controlled termination.
tags:
    - multiprocessing
    - process-management
    - api-server
    - concurrency
    - worker-nodes
category: reference
---

Manages a group of API server processes.

Handles creation, monitoring, and termination of API server worker processes. Also monitors extra processes to check if they are healthy.

Source code in `vllm/v1/utils.py`

```
classAPIServerProcessManager:
"""Manages a group of API server processes.

    Handles creation, monitoring, and termination of API server worker
    processes. Also monitors extra processes to check if they are healthy.
    """

    def__init__(
        self,
        listen_address: str,
        sock: Any,
        args: argparse.Namespace,
        num_servers: int,
        input_addresses: list[str],
        output_addresses: list[str],
        target_server_fn: Callable | None = None,
        stats_update_address: str | None = None,
        tensor_queue: Queue | None = None,
    ):
"""Initialize and start API server worker processes.

        Args:
            target_server_fn: Override function to call for each API server process
            listen_address: Address to listen for client connections
            sock: Socket for client connections
            args: Command line arguments
            num_servers: Number of API server processes to start
            input_addresses: Input addresses for each API server
            output_addresses: Output addresses for each API server
            stats_update_address: Optional stats update address
            tensor_queue: Optional tensor IPC queue for sharing MM tensors
        """
        self.listen_address = listen_address
        self.sock = sock
        self.args = args

        # Start API servers
        spawn_context = multiprocessing.get_context("spawn")
        self.processes: list[BaseProcess] = []

        for i, in_addr, out_addr in zip(
            range(num_servers), input_addresses, output_addresses
        ):
            client_config = {
                "input_address": in_addr,
                "output_address": out_addr,
                "client_count": num_servers,
                "client_index": i,
            }
            if stats_update_address is not None:
                client_config["stats_update_address"] = stats_update_address
            if tensor_queue is not None:
                client_config["tensor_queue"] = tensor_queue

            proc = spawn_context.Process(
                target=target_server_fn or run_api_server_worker_proc,
                name=f"ApiServer_{i}",
                args=(listen_address, sock, args, client_config),
            )
            self.processes.append(proc)
            proc.start()

        logger.info("Started %d API server processes", len(self.processes))

        # Shutdown only the API server processes on garbage collection
        # The extra processes are managed by their owners
        self._finalizer = weakref.finalize(self, shutdown, self.processes)

    defshutdown(self, timeout: float | None = None) -> None:
"""Shutdown API server processes with configurable timeout"""
        if self._finalizer.detach() is not None:
            shutdown(self.processes, timeout=timeout)
```

### \_\_init\__ [¶](#vllm.v1.utils.APIServerProcessManager.__init__ "Permanent link")

```
__init__(
    listen_address: str,
    sock: Any,
    args: Namespace,
    num_servers: int,
    input_addresses: list[str],
    output_addresses: list[str],
    target_server_fn: Callable | None = None,
    stats_update_address: str | None = None,
    tensor_queue: Queue | None = None,
)
```

Initialize and start API server worker processes.

Parameters:

Name Type Description Default `target_server_fn` `Callable | None`

Override function to call for each API server process

`None` `listen_address` `str`

Address to listen for client connections

*required* `sock` `Any`

Socket for client connections

*required* `args` `Namespace`

Command line arguments

*required* `num_servers` `int`

Number of API server processes to start

*required* `input_addresses` `list[str]`

Input addresses for each API server

*required* `output_addresses` `list[str]`

Output addresses for each API server

*required* `stats_update_address` `str | None`

Optional stats update address

`None` `tensor_queue` `Queue | None`

Optional tensor IPC queue for sharing MM tensors

`None`

Source code in `vllm/v1/utils.py`

```
def__init__(
    self,
    listen_address: str,
    sock: Any,
    args: argparse.Namespace,
    num_servers: int,
    input_addresses: list[str],
    output_addresses: list[str],
    target_server_fn: Callable | None = None,
    stats_update_address: str | None = None,
    tensor_queue: Queue | None = None,
):
"""Initialize and start API server worker processes.

    Args:
        target_server_fn: Override function to call for each API server process
        listen_address: Address to listen for client connections
        sock: Socket for client connections
        args: Command line arguments
        num_servers: Number of API server processes to start
        input_addresses: Input addresses for each API server
        output_addresses: Output addresses for each API server
        stats_update_address: Optional stats update address
        tensor_queue: Optional tensor IPC queue for sharing MM tensors
    """
    self.listen_address = listen_address
    self.sock = sock
    self.args = args

    # Start API servers
    spawn_context = multiprocessing.get_context("spawn")
    self.processes: list[BaseProcess] = []

    for i, in_addr, out_addr in zip(
        range(num_servers), input_addresses, output_addresses
    ):
        client_config = {
            "input_address": in_addr,
            "output_address": out_addr,
            "client_count": num_servers,
            "client_index": i,
        }
        if stats_update_address is not None:
            client_config["stats_update_address"] = stats_update_address
        if tensor_queue is not None:
            client_config["tensor_queue"] = tensor_queue

        proc = spawn_context.Process(
            target=target_server_fn or run_api_server_worker_proc,
            name=f"ApiServer_{i}",
            args=(listen_address, sock, args, client_config),
        )
        self.processes.append(proc)
        proc.start()

    logger.info("Started %d API server processes", len(self.processes))

    # Shutdown only the API server processes on garbage collection
    # The extra processes are managed by their owners
    self._finalizer = weakref.finalize(self, shutdown, self.processes)
```

### shutdown [¶](#vllm.v1.utils.APIServerProcessManager.shutdown "Permanent link")

```
shutdown(timeout: float | None = None) -> None
```

Shutdown API server processes with configurable timeout

Source code in `vllm/v1/utils.py`

```
defshutdown(self, timeout: float | None = None) -> None:
"""Shutdown API server processes with configurable timeout"""
    if self._finalizer.detach() is not None:
        shutdown(self.processes, timeout=timeout)
```