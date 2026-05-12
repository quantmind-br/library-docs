---
title: worker - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/kv_offload/worker/worker/
source: sitemap
fetched_at: 2026-05-07T21:41:08.621067289-03:00
rendered_js: false
word_count: 418
summary: This document defines the OffloadingHandler and OffloadingWorker classes, which provide an asynchronous framework for managing KV data transfers in vLLM workers.
tags:
    - vllm
    - kv-cache
    - asynchronous-transfer
    - worker-node
    - data-offloading
    - api-reference
category: reference
---

## OffloadingHandler [¶](#vllm.v1.kv_offload.worker.worker.OffloadingHandler "Permanent link")

Bases: `ABC`

OffloadingHandler class for managing asynchronous KV data transfers

This class runs in the worker. It kicks off async KV data transfer requests, and allows collecting back completion statuses.

The class provides the following primitives

transfer\_async() - kicks off a new transfer job get\_finished() - returns a list of newly finished job IDs.

Source code in `vllm/v1/kv_offload/worker/worker.py`

```
classOffloadingHandler(ABC):
"""
    OffloadingHandler class for managing asynchronous KV data transfers

    This class runs in the worker.
    It kicks off async KV data transfer requests, and allows
    collecting back completion statuses.

    The class provides the following primitives:
        transfer_async() - kicks off a new transfer job
        get_finished() - returns a list of newly finished job IDs.
    """

    @abstractmethod
    deftransfer_async(self, job_id: int, spec: TransferSpec) -> bool:
"""
        Initiates an asynchronous transfer of KV data.

        Args:
            job_id: a unique ID that will be used when notifying back on
                transfer completion.
            spec: the (src, dst) spec of the KV data transfer.

        Returns:
            True if transfer was submitted successfully.
        """
        pass

    @abstractmethod
    defget_finished(self) -> list[TransferResult]:
"""
        Get transfers finished since last call.

        Returns:
            A list of (job_id, success) of transfers.
        """
        pass

    @abstractmethod
    defwait(self, job_ids: set[int]) -> None:
"""
        Wait for jobs to finish (blocking).
        Args:
            job_ids: The set of job IDs to wait for.
        """

    defshutdown(self) -> None:
"""Shutdown the handler and release any resources."""
        return
```

### get\_finished `abstractmethod` [¶](#vllm.v1.kv_offload.worker.worker.OffloadingHandler.get_finished "Permanent link")

```
get_finished() -> list[TransferResult]
```

Get transfers finished since last call.

Returns:

Type Description `list[TransferResult]`

A list of (job\_id, success) of transfers.

Source code in `vllm/v1/kv_offload/worker/worker.py`

```
@abstractmethod
defget_finished(self) -> list[TransferResult]:
"""
    Get transfers finished since last call.

    Returns:
        A list of (job_id, success) of transfers.
    """
    pass
```

### shutdown [¶](#vllm.v1.kv_offload.worker.worker.OffloadingHandler.shutdown "Permanent link")

Shutdown the handler and release any resources.

Source code in `vllm/v1/kv_offload/worker/worker.py`

```
defshutdown(self) -> None:
"""Shutdown the handler and release any resources."""
    return
```

### transfer\_async `abstractmethod` [¶](#vllm.v1.kv_offload.worker.worker.OffloadingHandler.transfer_async "Permanent link")

```
transfer_async(job_id: int, spec: TransferSpec) -> bool
```

Initiates an asynchronous transfer of KV data.

Parameters:

Name Type Description Default `job_id` `int`

a unique ID that will be used when notifying back on transfer completion.

*required* `spec` `TransferSpec`

the (src, dst) spec of the KV data transfer.

*required*

Returns:

Type Description `bool`

True if transfer was submitted successfully.

Source code in `vllm/v1/kv_offload/worker/worker.py`

```
@abstractmethod
deftransfer_async(self, job_id: int, spec: TransferSpec) -> bool:
"""
    Initiates an asynchronous transfer of KV data.

    Args:
        job_id: a unique ID that will be used when notifying back on
            transfer completion.
        spec: the (src, dst) spec of the KV data transfer.

    Returns:
        True if transfer was submitted successfully.
    """
    pass
```

### wait `abstractmethod` [¶](#vllm.v1.kv_offload.worker.worker.OffloadingHandler.wait "Permanent link")

```
wait(job_ids: set[int]) -> None
```

Wait for jobs to finish (blocking). Args: job\_ids: The set of job IDs to wait for.

Source code in `vllm/v1/kv_offload/worker/worker.py`

```
@abstractmethod
defwait(self, job_ids: set[int]) -> None:
"""
    Wait for jobs to finish (blocking).
    Args:
        job_ids: The set of job IDs to wait for.
    """
```

## OffloadingWorker [¶](#vllm.v1.kv_offload.worker.worker.OffloadingWorker "Permanent link")

OffloadingWorker class for managing asynchronous KV data transfers using multiple OffloadingHandlers

This class runs in the worker. It kicks off async KV data transfer requests, by delegating to one of its registered OffloadingHandlers, based on the transfer type.

The class provides the following primitives

register\_handler() - registers a new handler to handle a specific transfer type transfer\_async() - kicks off a new transfer job using one of the registered handlers. get\_finished() - returns a list of newly finished job IDs from all handlers.

Source code in `vllm/v1/kv_offload/worker/worker.py`

```
classOffloadingWorker:
"""
    OffloadingWorker class for managing asynchronous KV data transfers
    using multiple OffloadingHandlers

    This class runs in the worker.
    It kicks off async KV data transfer requests, by delegating
    to one of its registered OffloadingHandlers, based on the transfer type.

    The class provides the following primitives:
        register_handler() - registers a new handler to handle
            a specific transfer type
        transfer_async() - kicks off a new transfer job
            using one of the registered handlers.
        get_finished() - returns a list of newly finished job IDs
            from all handlers.
    """

    def__init__(self):
        self.handlers: set[OffloadingHandler] = set()
        self.transfer_type_to_handler: dict[TransferType, OffloadingHandler] = {}

    defregister_handler(
        self,
        src_cls: type[LoadStoreSpec],
        dst_cls: type[LoadStoreSpec],
        handler: OffloadingHandler,
    ) -> None:
"""
        Registers a new handler.

        Args:
            src_cls: the source type of transfers handled by this handler.
            dst_cls: the destination type of transfers handled by this handler.
            handler: the handler that will handle transfers.
        """
        transfer_type = (src_cls.medium(), dst_cls.medium())
        assert transfer_type not in self.transfer_type_to_handler
        self.handlers.add(handler)
        self.transfer_type_to_handler[transfer_type] = handler

    deftransfer_async(self, job_id: int, spec: TransferSpec) -> bool:
"""
        Initiates an asynchronous transfer of KV data.

        Args:
            job_id: a unique ID that will be used when notifying back on
                transfer completion.
            spec: the (src, dst) spec of the KV data transfer.

        Returns:
            True if transfer was submitted successfully.
        """
        src, dst = spec
        transfer_type = (src.medium(), dst.medium())
        handler = self.transfer_type_to_handler.get(transfer_type)
        assert handler is not None
        try:
            success = handler.transfer_async(job_id, spec)
        except Exception as e:
            logger.warning(
                "Exception in %r transfer %d: %r",
                transfer_type,
                job_id,
                e,
                exc_info=True,
            )
            return False

        if not success:
            logger.warning("Failed to submit %r transfer %d", transfer_type, job_id)
        else:
            logger.debug("Submitted %r transfer %d: %r", transfer_type, job_id, spec)
        return success

    defget_finished(self) -> list[TransferResult]:
"""
        Get transfers finished since last call.

        Returns:
            A list of TransferResults
        """
        finished = []
        for handler in self.handlers:
            finished.extend(handler.get_finished())
        return finished

    defwait(self, job_ids: set[int]) -> None:
"""
        Wait for jobs to finish (blocking).

        Args:
            job_ids: The set of job IDs to wait for.
        """
        for handler in self.handlers:
            handler.wait(job_ids)

    defshutdown(self) -> None:
        for handler in self.handlers:
            handler.shutdown()
```

### get\_finished [¶](#vllm.v1.kv_offload.worker.worker.OffloadingWorker.get_finished "Permanent link")

```
get_finished() -> list[TransferResult]
```

Get transfers finished since last call.

Returns:

Type Description `list[TransferResult]`

A list of TransferResults

Source code in `vllm/v1/kv_offload/worker/worker.py`

```
defget_finished(self) -> list[TransferResult]:
"""
    Get transfers finished since last call.

    Returns:
        A list of TransferResults
    """
    finished = []
    for handler in self.handlers:
        finished.extend(handler.get_finished())
    return finished
```

### register\_handler [¶](#vllm.v1.kv_offload.worker.worker.OffloadingWorker.register_handler "Permanent link")

Registers a new handler.

Parameters:

Name Type Description Default `src_cls` `type[LoadStoreSpec]`

the source type of transfers handled by this handler.

*required* `dst_cls` `type[LoadStoreSpec]`

the destination type of transfers handled by this handler.

*required* `handler` `OffloadingHandler`

the handler that will handle transfers.

*required*

Source code in `vllm/v1/kv_offload/worker/worker.py`

```
defregister_handler(
    self,
    src_cls: type[LoadStoreSpec],
    dst_cls: type[LoadStoreSpec],
    handler: OffloadingHandler,
) -> None:
"""
    Registers a new handler.

    Args:
        src_cls: the source type of transfers handled by this handler.
        dst_cls: the destination type of transfers handled by this handler.
        handler: the handler that will handle transfers.
    """
    transfer_type = (src_cls.medium(), dst_cls.medium())
    assert transfer_type not in self.transfer_type_to_handler
    self.handlers.add(handler)
    self.transfer_type_to_handler[transfer_type] = handler
```

### transfer\_async [¶](#vllm.v1.kv_offload.worker.worker.OffloadingWorker.transfer_async "Permanent link")

```
transfer_async(job_id: int, spec: TransferSpec) -> bool
```

Initiates an asynchronous transfer of KV data.

Parameters:

Name Type Description Default `job_id` `int`

a unique ID that will be used when notifying back on transfer completion.

*required* `spec` `TransferSpec`

the (src, dst) spec of the KV data transfer.

*required*

Returns:

Type Description `bool`

True if transfer was submitted successfully.

Source code in `vllm/v1/kv_offload/worker/worker.py`

```
deftransfer_async(self, job_id: int, spec: TransferSpec) -> bool:
"""
    Initiates an asynchronous transfer of KV data.

    Args:
        job_id: a unique ID that will be used when notifying back on
            transfer completion.
        spec: the (src, dst) spec of the KV data transfer.

    Returns:
        True if transfer was submitted successfully.
    """
    src, dst = spec
    transfer_type = (src.medium(), dst.medium())
    handler = self.transfer_type_to_handler.get(transfer_type)
    assert handler is not None
    try:
        success = handler.transfer_async(job_id, spec)
    except Exception as e:
        logger.warning(
            "Exception in %r transfer %d: %r",
            transfer_type,
            job_id,
            e,
            exc_info=True,
        )
        return False

    if not success:
        logger.warning("Failed to submit %r transfer %d", transfer_type, job_id)
    else:
        logger.debug("Submitted %r transfer %d: %r", transfer_type, job_id, spec)
    return success
```

### wait [¶](#vllm.v1.kv_offload.worker.worker.OffloadingWorker.wait "Permanent link")

```
wait(job_ids: set[int]) -> None
```

Wait for jobs to finish (blocking).

Parameters:

Name Type Description Default `job_ids` `set[int]`

The set of job IDs to wait for.

*required*

Source code in `vllm/v1/kv_offload/worker/worker.py`

```
defwait(self, job_ids: set[int]) -> None:
"""
    Wait for jobs to finish (blocking).

    Args:
        job_ids: The set of job IDs to wait for.
    """
    for handler in self.handlers:
        handler.wait(job_ids)
```