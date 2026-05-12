---
title: tensor_ipc - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/engine/tensor_ipc/
source: sitemap
fetched_at: 2026-05-07T21:40:42.127032653-03:00
rendered_js: false
word_count: 193
summary: This module provides a mechanism for zero-copy inter-process communication of tensors using torch.multiprocessing queues within the vLLM engine.
tags:
    - vllm
    - ipc
    - tensor-sharing
    - multiprocessing
    - zero-copy
    - distributed-computing
category: reference
---

## vllm.v1.engine.tensor\_ipc [¶](#vllm.v1.engine.tensor_ipc "Permanent link")

Tensor IPC transport via torch.multiprocessing.Queue.

This module contains the queue-based transport logic for sharing tensors between processes (e.g., API server -&gt; engine core). The msgpack layer emits/consumes lightweight :class:`TensorIpcData` values, while transport state such as request association, handle generation, queue routing, buffering, and cleanup lives here.

## TensorIpcData `dataclass` [¶](#vllm.v1.engine.tensor_ipc.TensorIpcData "Permanent link")

Data sent via torch.multiprocessing.Queue for zero-copy IPC.

Contains the tensor\_id and the actual tensor. The tensor is shared in memory (GPU or CPU) for efficient inter-process communication.

Source code in `vllm/v1/engine/tensor_ipc.py`

```
@dataclasses.dataclass
classTensorIpcData:
"""
    Data sent via torch.multiprocessing.Queue for zero-copy IPC.

    Contains the tensor_id and the actual tensor. The tensor is
    shared in memory (GPU or CPU) for efficient inter-process communication.
    """

    sender_id: str
    message_id: int
    tensor_id: int
    tensor: torch.Tensor
```

## TensorIpcReceiver [¶](#vllm.v1.engine.tensor_ipc.TensorIpcReceiver "Permanent link")

Receive-side logic for tensor IPC via torch.multiprocessing.Queue.

Wraps the queue receive logic previously embedded in MsgpackDecoder.

Source code in `vllm/v1/engine/tensor_ipc.py`

```
classTensorIpcReceiver:
"""Receive-side logic for tensor IPC via torch.multiprocessing.Queue.

    Wraps the queue receive logic previously embedded in MsgpackDecoder.
    """

    def__init__(self, queue: TensorIpcQueue):
        self.queue = queue
        self._tensor_buffers = defaultdict[str, _Sender](_Sender)

    def__call__(
        self, dtype: str, shape: tuple[int, ...], meta: dict[str, Any]
    ) -> torch.Tensor:
"""Retrieve a tensor from torch.multiprocessing.Queue.

        Uses a drain-and-buffer pattern: drains all available tensors from
        the queue, buffering them, until the requested tensor is found.
        Works for CUDA and CPU.
        """

        # Create lookup key from handle
        sender_id: str = meta["sender_id"]
        message_id: int = meta["message_id"]
        tensor_id: int = meta["tensor_id"]

        # Drain all available tensors. We save them regardless if this is
        # the one we're waiting for as they may arrive out of order from
        # multiple producers.
        while True:
            sender = self._tensor_buffers.get(sender_id)
            if sender is not None:
                tensors = sender.tensors
                tensor = tensors.get(message_id, {}).pop(tensor_id, None)
                if tensor is not None:
                    if sender.current_message_id != message_id:
                        while tensors and (mid := next(iter(tensors))) < message_id:
                            if sender.tensors.pop(mid):
                                logger.warning(
                                    "Discarding %d stale tensors from sender %s",
                                    sender_id,
                                )
                        sender.current_message_id = message_id
                    logger.debug(
                        "Received tensor %s from sender %s for (shape=%s, device=%s) "
                        "via IPC queue (shared memory)",
                        (message_id, tensor_id),
                        sender_id,
                        tensor.shape,
                        tensor.device,
                    )
                    return tensor

            ipc_data: TensorIpcData = self.queue.get(timeout=10.0)

            # Store tensor
            sender = self._tensor_buffers[ipc_data.sender_id]
            if sender.current_message_id > ipc_data.message_id:
                logger.warning(
                    "Ignoring stale tensor from sender %s", ipc_data.sender_id
                )
                continue

            sender.tensors.setdefault(ipc_data.message_id, {})[ipc_data.tensor_id] = (
                ipc_data.tensor
            )
```

### \_\_call\__ [¶](#vllm.v1.engine.tensor_ipc.TensorIpcReceiver.__call__ "Permanent link")

Retrieve a tensor from torch.multiprocessing.Queue.

Uses a drain-and-buffer pattern: drains all available tensors from the queue, buffering them, until the requested tensor is found. Works for CUDA and CPU.

Source code in `vllm/v1/engine/tensor_ipc.py`

```
def__call__(
    self, dtype: str, shape: tuple[int, ...], meta: dict[str, Any]
) -> torch.Tensor:
"""Retrieve a tensor from torch.multiprocessing.Queue.

    Uses a drain-and-buffer pattern: drains all available tensors from
    the queue, buffering them, until the requested tensor is found.
    Works for CUDA and CPU.
    """

    # Create lookup key from handle
    sender_id: str = meta["sender_id"]
    message_id: int = meta["message_id"]
    tensor_id: int = meta["tensor_id"]

    # Drain all available tensors. We save them regardless if this is
    # the one we're waiting for as they may arrive out of order from
    # multiple producers.
    while True:
        sender = self._tensor_buffers.get(sender_id)
        if sender is not None:
            tensors = sender.tensors
            tensor = tensors.get(message_id, {}).pop(tensor_id, None)
            if tensor is not None:
                if sender.current_message_id != message_id:
                    while tensors and (mid := next(iter(tensors))) < message_id:
                        if sender.tensors.pop(mid):
                            logger.warning(
                                "Discarding %d stale tensors from sender %s",
                                sender_id,
                            )
                    sender.current_message_id = message_id
                logger.debug(
                    "Received tensor %s from sender %s for (shape=%s, device=%s) "
                    "via IPC queue (shared memory)",
                    (message_id, tensor_id),
                    sender_id,
                    tensor.shape,
                    tensor.device,
                )
                return tensor

        ipc_data: TensorIpcData = self.queue.get(timeout=10.0)

        # Store tensor
        sender = self._tensor_buffers[ipc_data.sender_id]
        if sender.current_message_id > ipc_data.message_id:
            logger.warning(
                "Ignoring stale tensor from sender %s", ipc_data.sender_id
            )
            continue

        sender.tensors.setdefault(ipc_data.message_id, {})[ipc_data.tensor_id] = (
            ipc_data.tensor
        )
```

## TensorIpcSender [¶](#vllm.v1.engine.tensor_ipc.TensorIpcSender "Permanent link")

Bases: `OOBTensorConsumer`

Send-side logic for tensor IPC via torch.multiprocessing.Queue.

Uses a single queue targeting rank 0 (the only rank that consumes multimodal tensors during TP&gt;1 / PP&gt;1. Note: DP&gt;1 not supported).

Source code in `vllm/v1/engine/tensor_ipc.py`

```
classTensorIpcSender(OOBTensorConsumer):
"""Send-side logic for tensor IPC via torch.multiprocessing.Queue.

    Uses a single queue targeting rank 0 (the only rank that consumes
    multimodal tensors during TP>1 / PP>1. Note: DP>1 not supported).
    """

    def__init__(self, queue: TensorIpcQueue):
        self.queue = queue
        self._tensor_id_counter = 0
        self._message_counter = 0
        self._sender_id = uuid.uuid4().hex[:8]

    defset_target_engine(self, target_engine: int) -> None:
        if target_engine != 0:
            raise IndexError(
                "TensorIpcSender only supports a single queue; "
                f"got target engine {target_engine}"
            )

    defnew_message(self) -> None:
        self._message_counter += 1
        self._tensor_id_counter = 0

    def__call__(self, tensor: torch.Tensor) -> dict[str, Any] | None:
"""Send tensor via queue, return its handle. Returns None if failed."""
        try:
            # Move tensor to shared memory for IPC
            # This is required for proper inter-process communication
            if not tensor.is_shared():
                tensor = tensor.share_memory_()

            metadata = {
                "sender_id": self._sender_id,
                "message_id": self._message_counter,
                "tensor_id": self._tensor_id_counter,
            }

            self._tensor_id_counter += 1

            ipc_data = TensorIpcData(**metadata, tensor=tensor)  # type: ignore[arg-type]

            # Use a timeout to avoid blocking indefinitely
            self.queue.put(ipc_data, timeout=10.0)

            logger.debug(
                "Sent tensor %s for (shape=%s, device=%s) "
                "via IPC queue (shared memory)",
                metadata,
                tensor.shape,
                tensor.device,
            )

            return metadata
        except Exception as e:
            logger.warning(
                "Failed to send tensor via IPC queue: %s. "
                "Falling back to standard serialization.",
                e,
            )
            return None
```

### \_\_call\__ [¶](#vllm.v1.engine.tensor_ipc.TensorIpcSender.__call__ "Permanent link")

Send tensor via queue, return its handle. Returns None if failed.

Source code in `vllm/v1/engine/tensor_ipc.py`

```
def__call__(self, tensor: torch.Tensor) -> dict[str, Any] | None:
"""Send tensor via queue, return its handle. Returns None if failed."""
    try:
        # Move tensor to shared memory for IPC
        # This is required for proper inter-process communication
        if not tensor.is_shared():
            tensor = tensor.share_memory_()

        metadata = {
            "sender_id": self._sender_id,
            "message_id": self._message_counter,
            "tensor_id": self._tensor_id_counter,
        }

        self._tensor_id_counter += 1

        ipc_data = TensorIpcData(**metadata, tensor=tensor)  # type: ignore[arg-type]

        # Use a timeout to avoid blocking indefinitely
        self.queue.put(ipc_data, timeout=10.0)

        logger.debug(
            "Sent tensor %s for (shape=%s, device=%s) "
            "via IPC queue (shared memory)",
            metadata,
            tensor.shape,
            tensor.device,
        )

        return metadata
    except Exception as e:
        logger.warning(
            "Failed to send tensor via IPC queue: %s. "
            "Falling back to standard serialization.",
            e,
        )
        return None
```