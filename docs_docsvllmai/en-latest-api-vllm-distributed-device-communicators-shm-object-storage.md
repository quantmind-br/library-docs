---
title: shm_object_storage - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/device_communicators/shm_object_storage/
source: sitemap
fetched_at: 2026-05-07T21:17:41.013316551-03:00
rendered_js: false
word_count: 1045
summary: This document defines the interfaces and implementation for a shared memory object storage system designed for single-writer, multiple-reader cross-process communication. It provides mechanisms for object serialization, reference counting, and FIFO-based memory management within a ring buffer.
tags:
    - shared-memory
    - serialization
    - fifo-eviction
    - cross-process
    - ipc
    - reference-counting
    - ring-buffer
category: reference
---

## ObjectSerde [¶](#vllm.distributed.device_communicators.shm_object_storage.ObjectSerde "Permanent link")

Bases: `ABC`

Source code in `vllm/distributed/device_communicators/shm_object_storage.py`

```
classObjectSerde(ABC):
    @abstractmethod
    defserialize(self, value: Any) -> tuple[Any, int, bytes, int]:
"""Serialize an object to bytes."""
        raise NotImplementedError

    @abstractmethod
    defdeserialize(self, data: memoryview) -> Any:
"""Deserialize bytes back to an object."""
        raise NotImplementedError
```

### deserialize `abstractmethod` [¶](#vllm.distributed.device_communicators.shm_object_storage.ObjectSerde.deserialize "Permanent link")

Deserialize bytes back to an object.

Source code in `vllm/distributed/device_communicators/shm_object_storage.py`

```
@abstractmethod
defdeserialize(self, data: memoryview) -> Any:
"""Deserialize bytes back to an object."""
    raise NotImplementedError
```

### serialize `abstractmethod` [¶](#vllm.distributed.device_communicators.shm_object_storage.ObjectSerde.serialize "Permanent link")

Serialize an object to bytes.

Source code in `vllm/distributed/device_communicators/shm_object_storage.py`

```
@abstractmethod
defserialize(self, value: Any) -> tuple[Any, int, bytes, int]:
"""Serialize an object to bytes."""
    raise NotImplementedError
```

## SingleWriterShmObjectStorage [¶](#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage "Permanent link")

A single-writer, multiple-reader object storage system built on top of a shared memory ring buffer. Provides key-value storage with automatic memory management and cross-process serialization support.

This storage system follows a FIFO (First-In-First-Out) eviction policy where the oldest objects are automatically freed when memory runs low. Memory is reclaimed based on reader reference counting - objects are only freed when all readers have finished accessing them.

Architecture: - Single writer process can put(key, value) objects - Multiple reader processes can get(address, monotonic\_id) objects - Built on SingleWriterShmRingBuffer for efficient shared memory management - Thread-safe operations with reader synchronization via locks

Key Features: - FIFO Eviction: Oldest objects are evicted first when memory is full - Reference Counting: Objects are only freed when no readers are accessing them - Duplicate Key Handling: Existing keys are not overwritten, just re-referenced - Customized Serialization: By default uses Msgpack for efficient serialization of Python objects, but can be extended for custom types - Cross-Process Safety: Uses shared memory with proper synchronization - Automatic Cleanup: Garbage collection happens transparently during allocation

Memory Layout per Object: `[4-byte reference_count][metadata_size][serialized_object_data]`

Thread Safety: - Writer operations (put, clear) are single-threaded by design - Reader operations (get) are thread-safe with lock-based reference counting - Memory reclamation is handled exclusively by the writer process

Source code in `vllm/distributed/device_communicators/shm_object_storage.py`

```
classSingleWriterShmObjectStorage:
"""
    A single-writer, multiple-reader object storage system built on top of a
    shared memory ring buffer. Provides key-value storage with automatic memory
    management and cross-process serialization support.

    This storage system follows a FIFO (First-In-First-Out) eviction policy
    where the oldest objects are automatically freed when memory runs low.
    Memory is reclaimed based on reader reference counting - objects are only
    freed when all readers have finished accessing them.

    Architecture:
    - Single writer process can put(key, value) objects
    - Multiple reader processes can get(address, monotonic_id) objects
    - Built on SingleWriterShmRingBuffer for efficient shared memory management
    - Thread-safe operations with reader synchronization via locks

    Key Features:
    - FIFO Eviction: Oldest objects are evicted first when memory is full
    - Reference Counting: Objects are only freed when no readers are
      accessing them
    - Duplicate Key Handling: Existing keys are not overwritten, just
      re-referenced
    - Customized Serialization: By default uses Msgpack for efficient
      serialization of Python objects, but can be extended for custom types
    - Cross-Process Safety: Uses shared memory with proper synchronization
    - Automatic Cleanup: Garbage collection happens transparently during
      allocation

    Memory Layout per Object:
    `[4-byte reference_count][metadata_size][serialized_object_data]`

    Thread Safety:
    - Writer operations (put, clear) are single-threaded by design
    - Reader operations (get) are thread-safe with lock-based reference
      counting
    - Memory reclamation is handled exclusively by the writer process
    """

    def__init__(
        self,
        max_object_size: int,
        n_readers: int,
        ring_buffer: SingleWriterShmRingBuffer,
        serde_class: type[ObjectSerde] = MsgpackSerde,
        reader_lock: LockType | None = None,
    ):
"""
        Initialize the object storage.

        Args:
            max_object_size: Maximum size for a single object in bytes.
            n_readers: Number of reader processes that can access the storage.
            ring_buffer: The shared memory ring buffer for storing objects.
            serde_class: Serializer/deserializer for objects.
            reader_lock: Optional lock for synchronizing reader access.
        Raises:
            ValueError: If reader_lock is None for readers.
        """

        self.max_object_size = max_object_size
        self.n_readers = n_readers
        self.serde_class = serde_class
        self.ser_de = serde_class()
        self.ring_buffer = ring_buffer
        self.is_writer = self.ring_buffer.is_writer

        self.flag_bytes = 4  # for in-use flag

        if self.is_writer:
            # Key-value mapping: key -> (address, monotonic_id)
            self.key_index: dict[str, tuple[int, int]] = {}
            # Reverse mapping: monotonic_id -> key
            self.id_index: dict[int, str] = {}
            # Writer flag to track in-use status: monotonic_id -> count
            self.writer_flag: dict[int, int] = {}
        else:
            if reader_lock is None:
                raise ValueError("Lock must be provided for readers.")

        self._reader_lock = reader_lock

    defclear(self) -> None:
"""Clear the object storage."""
        if self.is_writer:
            self.ring_buffer.clear()
            self.key_index.clear()
            self.id_index.clear()
            self.writer_flag.clear()
            logger.debug("Object storage cleared and reinitialized.")

    defcopy_to_buffer(
        self,
        data: bytes | list[bytes],
        data_bytes: int,
        metadata: bytes,
        md_bytes: int,
        data_view: memoryview,
    ) -> None:
        data_view[self.flag_bytes : self.flag_bytes + md_bytes] = metadata
        if isinstance(data, bytes):
            data_view[-data_bytes:] = data
        elif isinstance(data, list):
            start_idx = self.flag_bytes + md_bytes
            for item_bytes in data:
                item_size = len(item_bytes)
                data_view[start_idx : start_idx + item_size] = item_bytes
                start_idx += item_size
        else:
            raise ValueError(f"Unsupported data type for serialization: {type(data)}")

    defincrement_writer_flag(self, id: int) -> None:
"""Set the in-use flag for the writer."""
        self.writer_flag[id] = self.writer_flag.get(id, 0) + 1

    defincrement_reader_flag(self, data_view: memoryview) -> None:
"""Set the in-use flag for the reader."""
        # >0 for in-use flag
        reader_count = self.ring_buffer.byte2int(data_view)
        data_view[:] = self.ring_buffer.int2byte(reader_count + 1)

    deffree_unused(self) -> None:
"""Free unused buffers in the ring buffer."""
        # try to free up 2*max_object_size bytes of space in the ring buffer,
        # since the buffer might be fragmented
        freed_ids = self.ring_buffer.free_buf(
            self.default_is_free_check, 2 * self.max_object_size
        )
        # update the metadata after freeing up space
        for freed_id in freed_ids:
            key_to_free = self.id_index[freed_id]
            del self.key_index[key_to_free]
            del self.id_index[freed_id]
            del self.writer_flag[freed_id]

    defis_cached(self, key: str) -> bool:
"""
        Check if the object with the given key is cached.
        """
        return key in self.key_index

    defget_cached(self, key: str) -> tuple[int, int]:
"""
        Get the cached object by key if it exists.
        """
        address, monotonic_id = self.key_index[key]
        self.increment_writer_flag(monotonic_id)
        return address, monotonic_id

    defput(self, key: str, value: Any) -> tuple[int, int]:
"""
        Store a key-value pair in the object storage.
        Attempts to free max_object_size bytes using FIFO order
        when the ring buffer runs out of space during a put() operation.

        Args:
            key: String key to identify the object
            value: Any serializable Python object

        Raises:
            MemoryError: If there's not enough space in the buffer
            ValueError: If the serialized object is too large
            ValueError: If the key already exists in the storage
        """
        if key in self.key_index:
            raise ValueError(f"Key '{key}' already exists in the storage.")

        object_data, data_bytes, object_metadata, md_bytes = self.ser_de.serialize(
            value
        )
        buffer_size = self.flag_bytes + data_bytes + md_bytes
        # Sanity checks
        if buffer_size > self.max_object_size:
            raise ValueError(
                f"Serialized object size ({buffer_size} bytes) exceeds "
                f"max object size ({self.max_object_size} bytes)"
            )

        # Allocate new buffer
        try:
            address, monotonic_id = self.ring_buffer.allocate_buf(buffer_size)
        except MemoryError:
            self.free_unused()
            # try again after freeing up space
            address, monotonic_id = self.ring_buffer.allocate_buf(buffer_size)

        # Write data to buffer
        with self.ring_buffer.access_buf(address) as (data_view, metadata):
            data_view[: self.flag_bytes] = self.ring_buffer.int2byte(0)
            self.copy_to_buffer(
                object_data, data_bytes, object_metadata, md_bytes, data_view
            )
        self.increment_writer_flag(monotonic_id)

        # Update key index
        self.key_index[key] = (address, monotonic_id)
        self.id_index[monotonic_id] = key
        return address, monotonic_id

    defget(self, address: int, monotonic_id: int) -> Any:
        # Read data from buffer
        with self.ring_buffer.access_buf(address) as (data_view, buf_metadata):
            # check id from metadata
            if buf_metadata[0] != monotonic_id:
                raise ValueError(
                    f"Data for address:id '{address}:{monotonic_id}'"
                    " has been modified or is invalid."
                )

            obj = self.ser_de.deserialize(data_view[self.flag_bytes :])

            # decrease the in-use flag for reader reads
            if self._reader_lock is not None:
                with self._reader_lock:
                    self.increment_reader_flag(data_view[: self.flag_bytes])
            else:
                # if self._reader_lock is None, it means we are the writer
                # in this case, we do not need to decrease the reader count
                assert self.is_writer

        return obj

    deftouch(
        self,
        key: str,
        address: int = 0,
        monotonic_id: int = 0,
    ) -> None:
"""
        Touch an existing cached item to update its eviction status.

        For writers (ShmObjectStoreSenderCache): Increment writer_flag
        For readers (ShmObjectStoreReceiverCache): Increment reader_count

        Args:
            key: String key of the object to touch
            address: Address of the object (only for readers)
            monotonic_id: Monotonic ID of the object (only for readers)

        """
        if self._reader_lock is None:
            if key not in self.key_index:
                return None
            address, monotonic_id = self.key_index[key]
            # Writer side: increment writer_flag to raise eviction threshold
            self.increment_writer_flag(monotonic_id)
        else:
            with (
                self._reader_lock,
                self.ring_buffer.access_buf(address) as (data_view, _),
            ):
                reader_count = self.ring_buffer.byte2int(data_view[: self.flag_bytes])

                # NOTE(Long):
                # Avoid increasing flag on newly added item (sync with sender)
                # Since when a new item is added
                # pre-touch has no effect on writer side
                if reader_count >= self.n_readers:
                    self.increment_reader_flag(data_view[: self.flag_bytes])

    defclose(self) -> None:
"""Close the shared memory."""
        self.ring_buffer.close()

    defhandle(self):
"""Get handle for sharing across processes."""
        return ShmObjectStorageHandle(
            max_object_size=self.max_object_size,
            n_readers=self.n_readers,
            ring_buffer_handle=self.ring_buffer.handle(),
            serde_class=self.serde_class,
            reader_lock=self._reader_lock,
        )

    @staticmethod
    defcreate_from_handle(
        handle: ShmObjectStorageHandle,
    ) -> "SingleWriterShmObjectStorage":
        logger.debug("Creating storage from handle: %s", handle)
        ring_buffer = SingleWriterShmRingBuffer(*handle.ring_buffer_handle)
        return SingleWriterShmObjectStorage(
            max_object_size=handle.max_object_size,
            n_readers=handle.n_readers,
            ring_buffer=ring_buffer,
            serde_class=handle.serde_class,
            reader_lock=handle.reader_lock,
        )

    defdefault_is_free_check(self, id: int, buf: memoryview) -> bool:
"""
        Default is_free function that checks if the first 4 bytes are zero.
        This indicates that the buffer is free.
        """
        reader_count = int.from_bytes(buf[0:4], "little", signed=True)
        writer_count = self.writer_flag[id]
        return reader_count >= writer_count * self.n_readers
```

### \_\_init\__ [¶](#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.__init__ "Permanent link")

```
__init__(
    max_object_size: int,
    n_readers: int,
    ring_buffer: SingleWriterShmRingBuffer,
    serde_class: type[ObjectSerde] = MsgpackSerde,
    reader_lock: Lock | None = None,
)
```

Initialize the object storage.

Parameters:

Name Type Description Default `max_object_size` `int`

Maximum size for a single object in bytes.

*required* `n_readers` `int`

Number of reader processes that can access the storage.

*required* `ring_buffer` `SingleWriterShmRingBuffer`

The shared memory ring buffer for storing objects.

*required* `serde_class` `type[ObjectSerde]`

Serializer/deserializer for objects.

`MsgpackSerde` `reader_lock` `Lock | None`

Optional lock for synchronizing reader access.

`None`

Raises: ValueError: If reader\_lock is None for readers.

Source code in `vllm/distributed/device_communicators/shm_object_storage.py`

```
def__init__(
    self,
    max_object_size: int,
    n_readers: int,
    ring_buffer: SingleWriterShmRingBuffer,
    serde_class: type[ObjectSerde] = MsgpackSerde,
    reader_lock: LockType | None = None,
):
"""
    Initialize the object storage.

    Args:
        max_object_size: Maximum size for a single object in bytes.
        n_readers: Number of reader processes that can access the storage.
        ring_buffer: The shared memory ring buffer for storing objects.
        serde_class: Serializer/deserializer for objects.
        reader_lock: Optional lock for synchronizing reader access.
    Raises:
        ValueError: If reader_lock is None for readers.
    """

    self.max_object_size = max_object_size
    self.n_readers = n_readers
    self.serde_class = serde_class
    self.ser_de = serde_class()
    self.ring_buffer = ring_buffer
    self.is_writer = self.ring_buffer.is_writer

    self.flag_bytes = 4  # for in-use flag

    if self.is_writer:
        # Key-value mapping: key -> (address, monotonic_id)
        self.key_index: dict[str, tuple[int, int]] = {}
        # Reverse mapping: monotonic_id -> key
        self.id_index: dict[int, str] = {}
        # Writer flag to track in-use status: monotonic_id -> count
        self.writer_flag: dict[int, int] = {}
    else:
        if reader_lock is None:
            raise ValueError("Lock must be provided for readers.")

    self._reader_lock = reader_lock
```

### clear [¶](#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.clear "Permanent link")

Clear the object storage.

Source code in `vllm/distributed/device_communicators/shm_object_storage.py`

```
defclear(self) -> None:
"""Clear the object storage."""
    if self.is_writer:
        self.ring_buffer.clear()
        self.key_index.clear()
        self.id_index.clear()
        self.writer_flag.clear()
        logger.debug("Object storage cleared and reinitialized.")
```

### close [¶](#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.close "Permanent link")

Close the shared memory.

Source code in `vllm/distributed/device_communicators/shm_object_storage.py`

```
defclose(self) -> None:
"""Close the shared memory."""
    self.ring_buffer.close()
```

### default\_is\_free\_check [¶](#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.default_is_free_check "Permanent link")

Default is\_free function that checks if the first 4 bytes are zero. This indicates that the buffer is free.

Source code in `vllm/distributed/device_communicators/shm_object_storage.py`

```
defdefault_is_free_check(self, id: int, buf: memoryview) -> bool:
"""
    Default is_free function that checks if the first 4 bytes are zero.
    This indicates that the buffer is free.
    """
    reader_count = int.from_bytes(buf[0:4], "little", signed=True)
    writer_count = self.writer_flag[id]
    return reader_count >= writer_count * self.n_readers
```

### free\_unused [¶](#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.free_unused "Permanent link")

Free unused buffers in the ring buffer.

Source code in `vllm/distributed/device_communicators/shm_object_storage.py`

```
deffree_unused(self) -> None:
"""Free unused buffers in the ring buffer."""
    # try to free up 2*max_object_size bytes of space in the ring buffer,
    # since the buffer might be fragmented
    freed_ids = self.ring_buffer.free_buf(
        self.default_is_free_check, 2 * self.max_object_size
    )
    # update the metadata after freeing up space
    for freed_id in freed_ids:
        key_to_free = self.id_index[freed_id]
        del self.key_index[key_to_free]
        del self.id_index[freed_id]
        del self.writer_flag[freed_id]
```

### get\_cached [¶](#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.get_cached "Permanent link")

Get the cached object by key if it exists.

Source code in `vllm/distributed/device_communicators/shm_object_storage.py`

```
defget_cached(self, key: str) -> tuple[int, int]:
"""
    Get the cached object by key if it exists.
    """
    address, monotonic_id = self.key_index[key]
    self.increment_writer_flag(monotonic_id)
    return address, monotonic_id
```

### handle [¶](#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.handle "Permanent link")

Get handle for sharing across processes.

Source code in `vllm/distributed/device_communicators/shm_object_storage.py`

```
defhandle(self):
"""Get handle for sharing across processes."""
    return ShmObjectStorageHandle(
        max_object_size=self.max_object_size,
        n_readers=self.n_readers,
        ring_buffer_handle=self.ring_buffer.handle(),
        serde_class=self.serde_class,
        reader_lock=self._reader_lock,
    )
```

### increment\_reader\_flag [¶](#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.increment_reader_flag "Permanent link")

```
increment_reader_flag(data_view: memoryview) -> None
```

Set the in-use flag for the reader.

Source code in `vllm/distributed/device_communicators/shm_object_storage.py`

```
defincrement_reader_flag(self, data_view: memoryview) -> None:
"""Set the in-use flag for the reader."""
    # >0 for in-use flag
    reader_count = self.ring_buffer.byte2int(data_view)
    data_view[:] = self.ring_buffer.int2byte(reader_count + 1)
```

### increment\_writer\_flag [¶](#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.increment_writer_flag "Permanent link")

```
increment_writer_flag(id: int) -> None
```

Set the in-use flag for the writer.

Source code in `vllm/distributed/device_communicators/shm_object_storage.py`

```
defincrement_writer_flag(self, id: int) -> None:
"""Set the in-use flag for the writer."""
    self.writer_flag[id] = self.writer_flag.get(id, 0) + 1
```

### is\_cached [¶](#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.is_cached "Permanent link")

Check if the object with the given key is cached.

Source code in `vllm/distributed/device_communicators/shm_object_storage.py`

```
defis_cached(self, key: str) -> bool:
"""
    Check if the object with the given key is cached.
    """
    return key in self.key_index
```

### put [¶](#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.put "Permanent link")

Store a key-value pair in the object storage. Attempts to free max\_object\_size bytes using FIFO order when the ring buffer runs out of space during a put() operation.

Parameters:

Name Type Description Default `key` `str`

String key to identify the object

*required* `value` `Any`

Any serializable Python object

*required*

Raises:

Type Description `MemoryError`

If there's not enough space in the buffer

`ValueError`

If the serialized object is too large

`ValueError`

If the key already exists in the storage

Source code in `vllm/distributed/device_communicators/shm_object_storage.py`

```
defput(self, key: str, value: Any) -> tuple[int, int]:
"""
    Store a key-value pair in the object storage.
    Attempts to free max_object_size bytes using FIFO order
    when the ring buffer runs out of space during a put() operation.

    Args:
        key: String key to identify the object
        value: Any serializable Python object

    Raises:
        MemoryError: If there's not enough space in the buffer
        ValueError: If the serialized object is too large
        ValueError: If the key already exists in the storage
    """
    if key in self.key_index:
        raise ValueError(f"Key '{key}' already exists in the storage.")

    object_data, data_bytes, object_metadata, md_bytes = self.ser_de.serialize(
        value
    )
    buffer_size = self.flag_bytes + data_bytes + md_bytes
    # Sanity checks
    if buffer_size > self.max_object_size:
        raise ValueError(
            f"Serialized object size ({buffer_size} bytes) exceeds "
            f"max object size ({self.max_object_size} bytes)"
        )

    # Allocate new buffer
    try:
        address, monotonic_id = self.ring_buffer.allocate_buf(buffer_size)
    except MemoryError:
        self.free_unused()
        # try again after freeing up space
        address, monotonic_id = self.ring_buffer.allocate_buf(buffer_size)

    # Write data to buffer
    with self.ring_buffer.access_buf(address) as (data_view, metadata):
        data_view[: self.flag_bytes] = self.ring_buffer.int2byte(0)
        self.copy_to_buffer(
            object_data, data_bytes, object_metadata, md_bytes, data_view
        )
    self.increment_writer_flag(monotonic_id)

    # Update key index
    self.key_index[key] = (address, monotonic_id)
    self.id_index[monotonic_id] = key
    return address, monotonic_id
```

### touch [¶](#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.touch "Permanent link")

```
touch(
    key: str, address: int = 0, monotonic_id: int = 0
) -> None
```

Touch an existing cached item to update its eviction status.

For writers (ShmObjectStoreSenderCache): Increment writer\_flag For readers (ShmObjectStoreReceiverCache): Increment reader\_count

Parameters:

Name Type Description Default `key` `str`

String key of the object to touch

*required* `address` `int`

Address of the object (only for readers)

`0` `monotonic_id` `int`

Monotonic ID of the object (only for readers)

`0`

Source code in `vllm/distributed/device_communicators/shm_object_storage.py`

```
deftouch(
    self,
    key: str,
    address: int = 0,
    monotonic_id: int = 0,
) -> None:
"""
    Touch an existing cached item to update its eviction status.

    For writers (ShmObjectStoreSenderCache): Increment writer_flag
    For readers (ShmObjectStoreReceiverCache): Increment reader_count

    Args:
        key: String key of the object to touch
        address: Address of the object (only for readers)
        monotonic_id: Monotonic ID of the object (only for readers)

    """
    if self._reader_lock is None:
        if key not in self.key_index:
            return None
        address, monotonic_id = self.key_index[key]
        # Writer side: increment writer_flag to raise eviction threshold
        self.increment_writer_flag(monotonic_id)
    else:
        with (
            self._reader_lock,
            self.ring_buffer.access_buf(address) as (data_view, _),
        ):
            reader_count = self.ring_buffer.byte2int(data_view[: self.flag_bytes])

            # NOTE(Long):
            # Avoid increasing flag on newly added item (sync with sender)
            # Since when a new item is added
            # pre-touch has no effect on writer side
            if reader_count >= self.n_readers:
                self.increment_reader_flag(data_view[: self.flag_bytes])
```

## SingleWriterShmRingBuffer [¶](#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmRingBuffer "Permanent link")

A single-writer, multiple-reader ring buffer implementation using shared memory. This class provides a thread-safe ring buffer where one process can write data while multiple processes/threads can read from it.

Architecture: - Uses shared memory for cross-process communication - Maintains metadata for each allocated buffer chunk in the writer process - Supports custom "is\_free\_fn" functions to determine when buffers can be reused - Each buffer chunk contains: `[4-byte id][4-byte size][actual_data]`

Key Concepts: - monotonic\_id\_start/end: Track the range of active buffer IDs - data\_buffer\_start/end: Track the physical memory range in use - Automatic wraparound when reaching buffer end - Lazy garbage collection based on is\_free\_fn checks

Example Usage Scenarios:

Scenario 1: Simple Linear Allocation

```
Buffer size: 100 bytes
Initial state: [................................................. ]
               ^start=end(0)

After allocating 20 bytes (id=0):
[id:0|size:20|data........][...................................]
^start(0)                  ^end(28)

After allocating 30 bytes (id=1):
[id:0|size:20|data........][id:1|size:30|data..............][..]
^start(0)                                                   ^end(66)
```

Scenario 2: Memory Reclamation

```
Before freeing (both buffers still in use):
[id:0|size:20|data........][id:1|size:30|data..............][..]
^start(0)                                                   ^end(66)

After id:0 is marked free by readers:
[FREED.................... ][id:1|size:30|data..............][..]
                            ^start(28)                       ^end(66)

After both are freed:
[FREED..............................................][..]
                                                     ^start=end(66)
```

Scenario 3: Wraparound Allocation (continuing from Scenario 2)

```
Starting from after memory reclamation in Scenario 2:
[FREED..............................................][..]
                                                     ^start=end(66)

Allocate 40 bytes (id=2) - only 34 bytes available at end, so wraparound:
[id:2|size:40|data........................][FREED.............][..]
                                          ^end(148)            ^start(66)
```

Scenario 4: Error Handling - Out of Space

```
Starting from after wraparound allocation in Scenario 3:
[id:2|size:40|data........................][FREED.............][..]
                                          ^end(148)            ^start(66)

Trying to allocate 20 more bytes:
occupied_size_new = end + size - start = 148 + 28 - 66 > buffer_size(100)
-> Raises MemoryError: "Not enough space in the data buffer"
```

Thread Safety: - Single writer: Only one process/thread should write (allocate\_buf) - Multiple readers: Multiple processes/threads can read (access\_buf) - Reader synchronization handled by is\_free\_fn callback - Writer handles garbage collection (free\_buf) based on reader feedback

Memory Layout per Buffer Chunk: `[4-byte monotonic_id][4-byte chunk_size][actual_data...]` ^metadata\_start ^data\_start

The monotonic\_id ensures data integrity - readers can verify they're accessing the correct data even after buffer wraparound or reuse.

Source code in `vllm/distributed/device_communicators/shm_object_storage.py`

````
classSingleWriterShmRingBuffer:
"""
    A single-writer, multiple-reader ring buffer implementation using shared
    memory. This class provides a thread-safe ring buffer where one process
    can write data while multiple processes/threads can read from it.

    Architecture:
    - Uses shared memory for cross-process communication
    - Maintains metadata for each allocated buffer chunk in the writer process
    - Supports custom "is_free_fn" functions to determine when buffers can be
      reused
    - Each buffer chunk contains: `[4-byte id][4-byte size][actual_data]`

    Key Concepts:
    - monotonic_id_start/end: Track the range of active buffer IDs
    - data_buffer_start/end: Track the physical memory range in use
    - Automatic wraparound when reaching buffer end
    - Lazy garbage collection based on is_free_fn checks

    Example Usage Scenarios:

    Scenario 1: Simple Linear Allocation
    ```
    Buffer size: 100 bytes
    Initial state: [................................................. ]
                   ^start=end(0)

    After allocating 20 bytes (id=0):
    [id:0|size:20|data........][...................................]
    ^start(0)                  ^end(28)

    After allocating 30 bytes (id=1):
    [id:0|size:20|data........][id:1|size:30|data..............][..]
    ^start(0)                                                   ^end(66)
    ```

    Scenario 2: Memory Reclamation
    ```
    Before freeing (both buffers still in use):
    [id:0|size:20|data........][id:1|size:30|data..............][..]
    ^start(0)                                                   ^end(66)

    After id:0 is marked free by readers:
    [FREED.................... ][id:1|size:30|data..............][..]
                                ^start(28)                       ^end(66)

    After both are freed:
    [FREED..............................................][..]
                                                         ^start=end(66)
    ```

    Scenario 3: Wraparound Allocation (continuing from Scenario 2)
    ```
    Starting from after memory reclamation in Scenario 2:
    [FREED..............................................][..]
                                                         ^start=end(66)

    Allocate 40 bytes (id=2) - only 34 bytes available at end, so wraparound:
    [id:2|size:40|data........................][FREED.............][..]
                                              ^end(148)            ^start(66)
    ```

    Scenario 4: Error Handling - Out of Space
    ```
    Starting from after wraparound allocation in Scenario 3:
    [id:2|size:40|data........................][FREED.............][..]
                                              ^end(148)            ^start(66)

    Trying to allocate 20 more bytes:
    occupied_size_new = end + size - start = 148 + 28 - 66 > buffer_size(100)
    -> Raises MemoryError: "Not enough space in the data buffer"
    ```

    Thread Safety:
    - Single writer: Only one process/thread should write (allocate_buf)
    - Multiple readers: Multiple processes/threads can read (access_buf)
    - Reader synchronization handled by is_free_fn callback
    - Writer handles garbage collection (free_buf) based on reader feedback

    Memory Layout per Buffer Chunk:
    `[4-byte monotonic_id][4-byte chunk_size][actual_data...]`
    ^metadata_start                         ^data_start

    The monotonic_id ensures data integrity - readers can verify they're
    accessing the correct data even after buffer wraparound or reuse.
    """

    def__init__(
        self,
        data_buffer_size: int,
        name: str | None = None,
        create: bool = False,
    ):
        self.data_buffer_size = data_buffer_size
        self.is_writer = create

        self.ID_NBYTES = 4
        self.ID_MAX = 2**31  # exclusive, so 2**31 - 1 is the max value
        self.SIZE_NBYTES = 4
        # 4 bytes for id, 4 bytes for buffer size
        self.MD_SIZE = self.ID_NBYTES + self.SIZE_NBYTES
        self.monotonic_id_end = 0
        self.monotonic_id_start = 0
        self.data_buffer_start = 0
        self.data_buffer_end = 0

        if create:
            logger.debug("Creating new shared memory buffer: %s", name)
            # we are creating a buffer
            self.metadata: dict[int, int] = {}  # monotonic_id -> start address
            self.shared_memory = shared_memory.SharedMemory(
                create=True, size=self.data_buffer_size, name=name
            )
        else:
            # we are opening an existing buffer
            # fix to https://stackoverflow.com/q/62748654/9191338
            # Python incorrectly tracks shared memory even if it is not
            # created by the process. The following patch is a workaround.
            with patch(
                "multiprocessing.resource_tracker.register",
                lambda *args, **kwargs: None,
            ):
                self.shared_memory = shared_memory.SharedMemory(name=name)
                # See https://docs.python.org/3/library/multiprocessing.shared_memory.html # noqa
                # Some platforms allocate memory based on page size,
                # so the shared memory block size may be larger or equal
                # to the requested size. The size parameter is ignored
                # when attaching to an existing block.
                assert self.shared_memory.size >= self.data_buffer_size

        logger.debug(
            "Shared memory created/opened with name: %s, size: %d",
            self.shared_memory.name,
            self.data_buffer_size,
        )

    defhandle(self):
        return (
            self.data_buffer_size,
            self.shared_memory.name,
        )

    defclear(self) -> None:
"""Clear the ring buffer."""
        assert self.is_writer, "Only the writer can clear the buffer."
        self.metadata.clear()
        self.monotonic_id_end = 0
        self.monotonic_id_start = 0
        self.data_buffer_start = 0
        self.data_buffer_end = 0

    defclose(self) -> None:
"""Close the shared memory."""
        if hasattr(self, "shared_memory"):
            self.shared_memory.close()
            if self.is_writer:
                with suppress(FileNotFoundError):
                    self.shared_memory.unlink()

    def__del__(self):
        self.close()

    defint2byte(self, integer: int) -> bytes:
"""Convert an integer to bytes."""
        return integer.to_bytes(self.ID_NBYTES, "little", signed=True)

    defbyte2int(self, byte_data: bytes) -> int:
"""Convert bytes back to an integer."""
        return int.from_bytes(byte_data, "little", signed=True)

    defallocate_buf(self, size: int) -> tuple[int, int]:
"""
        Allocate a buffer `MD_SIZE` + `size` bytes in the shared memory.
        Memory layout:
        `[4-byte monotonic_id][4-byte size][buffer data...]`
        """
        assert self.is_writer, "Only the writer can allocate buffers."
        assert size > 0, "Size must be greater than 0"
        assert self.shared_memory.buf is not None, "Buffer has been closed"
        size += self.MD_SIZE  # add metadata size to the buffer size
        # reset to beginning if the buffer does have enough contiguous space
        buffer_end_reset = self.data_buffer_end % self.data_buffer_size
        if buffer_end_reset + size > self.data_buffer_size:
            buffer_end_reset = (
                self.data_buffer_end // self.data_buffer_size + 1
            ) * self.data_buffer_size
        else:  # no reset needed
            buffer_end_reset = self.data_buffer_end

        # check if we have enough space in the data buffer
        # i.e. if the new end (self.data_buffer_end + size)
        # exceeds the start of the data buffer
        occupied_size_new = buffer_end_reset + size - self.data_buffer_start
        if occupied_size_new > self.data_buffer_size:
            raise MemoryError(
                "Not enough space in the data buffer, "
                "try calling free_buf() to free up space"
            )
        self.data_buffer_end = buffer_end_reset

        # first 4 bytes as the monotonic id
        buf_idx = self.data_buffer_end % self.data_buffer_size
        self.shared_memory.buf[buf_idx : buf_idx + self.ID_NBYTES] = self.int2byte(
            self.monotonic_id_end
        )
        # next 4 bytes as the size of the data buffer
        self.shared_memory.buf[buf_idx + self.ID_NBYTES : buf_idx + self.MD_SIZE] = (
            self.int2byte(size)
        )

        # record metadata
        self.metadata[self.monotonic_id_end % self.ID_MAX] = self.data_buffer_end
        # update buffer and monotonic id indices
        current_buffer_end = self.data_buffer_end
        current_id_end = self.monotonic_id_end
        self.data_buffer_end += size
        self.monotonic_id_end = (self.monotonic_id_end + 1) % self.ID_MAX
        return current_buffer_end, current_id_end

    @contextmanager
    defaccess_buf(self, address: int):
        assert self.shared_memory.buf is not None, "Buffer has been closed"
        buf_idx = address % self.data_buffer_size

        # read metadata
        metadata_buff = self.shared_memory.buf[buf_idx : buf_idx + self.MD_SIZE]
        id = self.byte2int(metadata_buff[: self.ID_NBYTES])
        size = self.byte2int(metadata_buff[self.ID_NBYTES : self.MD_SIZE])

        # yield the data buffer and metadata
        data_buff = self.shared_memory.buf[buf_idx + self.MD_SIZE : buf_idx + size]
        with (
            memoryview(data_buff) as data_view,
        ):
            yield data_view, (id, size)

    deffree_buf(
        self,
        is_free_fn: Callable[[int, memoryview], bool],
        nbytes: int | None = None,
    ) -> Iterable[int]:
"""
        Free a buffer of the given size. This is a no-op in shared memory,
        but we need to keep track of the metadata.

        If freed memory spreads across the end and start of the ring buffer,
        the actual freed memory will be in two segments. In this case there
        still might not be a contiguous space of `nbytes` available.

        Args:
            nbytes (int, optional): The size of the buffer to free. If None,
                frees the maximum size of the ring buffer.
        """

        assert self.is_writer, "Only the writer can free buffers."
        logger.debug(
            "Freeing up space in the ring buffer, "
            "monotonic_id_start: %d, monotonic_id_end: %d",
            self.monotonic_id_start,
            self.monotonic_id_end,
        )
        monotonic_id_before = self.monotonic_id_start
        # if nbytes is None, free up the maximum size of the ring buffer
        if nbytes is None:
            nbytes = self.data_buffer_size
        freed_bytes = 0
        while self.monotonic_id_start in self.metadata and freed_bytes < nbytes:
            address = self.metadata[self.monotonic_id_start]
            with self.access_buf(address) as (data_buff, metadata):
                if is_free_fn(self.monotonic_id_start, data_buff):
                    # check passed, we can free the buffer
                    del self.metadata[self.monotonic_id_start]
                    self.monotonic_id_start = (
                        self.monotonic_id_start + 1
                    ) % self.ID_MAX
                    if self.monotonic_id_start in self.metadata:
                        # pointing to the start addr of next allocation
                        self.data_buffer_start += (
                            self.metadata[self.monotonic_id_start]
                            - self.data_buffer_start
                        ) % self.data_buffer_size
                    else:
                        # no remaining allocation, reset to zero
                        self.data_buffer_start = self.data_buffer_end = 0
                    freed_bytes += metadata[1]
                else:
                    # there are still readers, we cannot free the buffer
                    break

        logger.debug(
            "Freed %d bytes from the ring buffer, "
            "monotonic_id_start: %d, monotonic_id_end: %d",
            freed_bytes,
            self.monotonic_id_start,
            self.monotonic_id_end,
        )

        # buffer wrap around
        if self.data_buffer_start >= self.data_buffer_size:
            self.data_buffer_start -= self.data_buffer_size
            self.data_buffer_end -= self.data_buffer_size

        monotonic_id_after = self.monotonic_id_start
        # id wrap around
        if monotonic_id_after >= monotonic_id_before:
            return range(monotonic_id_before, monotonic_id_after)
        else:
            return chain(
                range(monotonic_id_before, self.ID_MAX), range(0, monotonic_id_after)
            )
````

### allocate\_buf [¶](#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmRingBuffer.allocate_buf "Permanent link")

Allocate a buffer `MD_SIZE` + `size` bytes in the shared memory. Memory layout: `[4-byte monotonic_id][4-byte size][buffer data...]`

Source code in `vllm/distributed/device_communicators/shm_object_storage.py`

```
defallocate_buf(self, size: int) -> tuple[int, int]:
"""
    Allocate a buffer `MD_SIZE` + `size` bytes in the shared memory.
    Memory layout:
    `[4-byte monotonic_id][4-byte size][buffer data...]`
    """
    assert self.is_writer, "Only the writer can allocate buffers."
    assert size > 0, "Size must be greater than 0"
    assert self.shared_memory.buf is not None, "Buffer has been closed"
    size += self.MD_SIZE  # add metadata size to the buffer size
    # reset to beginning if the buffer does have enough contiguous space
    buffer_end_reset = self.data_buffer_end % self.data_buffer_size
    if buffer_end_reset + size > self.data_buffer_size:
        buffer_end_reset = (
            self.data_buffer_end // self.data_buffer_size + 1
        ) * self.data_buffer_size
    else:  # no reset needed
        buffer_end_reset = self.data_buffer_end

    # check if we have enough space in the data buffer
    # i.e. if the new end (self.data_buffer_end + size)
    # exceeds the start of the data buffer
    occupied_size_new = buffer_end_reset + size - self.data_buffer_start
    if occupied_size_new > self.data_buffer_size:
        raise MemoryError(
            "Not enough space in the data buffer, "
            "try calling free_buf() to free up space"
        )
    self.data_buffer_end = buffer_end_reset

    # first 4 bytes as the monotonic id
    buf_idx = self.data_buffer_end % self.data_buffer_size
    self.shared_memory.buf[buf_idx : buf_idx + self.ID_NBYTES] = self.int2byte(
        self.monotonic_id_end
    )
    # next 4 bytes as the size of the data buffer
    self.shared_memory.buf[buf_idx + self.ID_NBYTES : buf_idx + self.MD_SIZE] = (
        self.int2byte(size)
    )

    # record metadata
    self.metadata[self.monotonic_id_end % self.ID_MAX] = self.data_buffer_end
    # update buffer and monotonic id indices
    current_buffer_end = self.data_buffer_end
    current_id_end = self.monotonic_id_end
    self.data_buffer_end += size
    self.monotonic_id_end = (self.monotonic_id_end + 1) % self.ID_MAX
    return current_buffer_end, current_id_end
```

### byte2int [¶](#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmRingBuffer.byte2int "Permanent link")

Convert bytes back to an integer.

Source code in `vllm/distributed/device_communicators/shm_object_storage.py`

```
defbyte2int(self, byte_data: bytes) -> int:
"""Convert bytes back to an integer."""
    return int.from_bytes(byte_data, "little", signed=True)
```

### clear [¶](#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmRingBuffer.clear "Permanent link")

Clear the ring buffer.

Source code in `vllm/distributed/device_communicators/shm_object_storage.py`

```
defclear(self) -> None:
"""Clear the ring buffer."""
    assert self.is_writer, "Only the writer can clear the buffer."
    self.metadata.clear()
    self.monotonic_id_end = 0
    self.monotonic_id_start = 0
    self.data_buffer_start = 0
    self.data_buffer_end = 0
```

### close [¶](#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmRingBuffer.close "Permanent link")

Close the shared memory.

Source code in `vllm/distributed/device_communicators/shm_object_storage.py`

```
defclose(self) -> None:
"""Close the shared memory."""
    if hasattr(self, "shared_memory"):
        self.shared_memory.close()
        if self.is_writer:
            with suppress(FileNotFoundError):
                self.shared_memory.unlink()
```

### free\_buf [¶](#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmRingBuffer.free_buf "Permanent link")

Free a buffer of the given size. This is a no-op in shared memory, but we need to keep track of the metadata.

If freed memory spreads across the end and start of the ring buffer, the actual freed memory will be in two segments. In this case there still might not be a contiguous space of `nbytes` available.

Parameters:

Name Type Description Default `nbytes` `int`

The size of the buffer to free. If None, frees the maximum size of the ring buffer.

`None`

Source code in `vllm/distributed/device_communicators/shm_object_storage.py`

```
deffree_buf(
    self,
    is_free_fn: Callable[[int, memoryview], bool],
    nbytes: int | None = None,
) -> Iterable[int]:
"""
    Free a buffer of the given size. This is a no-op in shared memory,
    but we need to keep track of the metadata.

    If freed memory spreads across the end and start of the ring buffer,
    the actual freed memory will be in two segments. In this case there
    still might not be a contiguous space of `nbytes` available.

    Args:
        nbytes (int, optional): The size of the buffer to free. If None,
            frees the maximum size of the ring buffer.
    """

    assert self.is_writer, "Only the writer can free buffers."
    logger.debug(
        "Freeing up space in the ring buffer, "
        "monotonic_id_start: %d, monotonic_id_end: %d",
        self.monotonic_id_start,
        self.monotonic_id_end,
    )
    monotonic_id_before = self.monotonic_id_start
    # if nbytes is None, free up the maximum size of the ring buffer
    if nbytes is None:
        nbytes = self.data_buffer_size
    freed_bytes = 0
    while self.monotonic_id_start in self.metadata and freed_bytes < nbytes:
        address = self.metadata[self.monotonic_id_start]
        with self.access_buf(address) as (data_buff, metadata):
            if is_free_fn(self.monotonic_id_start, data_buff):
                # check passed, we can free the buffer
                del self.metadata[self.monotonic_id_start]
                self.monotonic_id_start = (
                    self.monotonic_id_start + 1
                ) % self.ID_MAX
                if self.monotonic_id_start in self.metadata:
                    # pointing to the start addr of next allocation
                    self.data_buffer_start += (
                        self.metadata[self.monotonic_id_start]
                        - self.data_buffer_start
                    ) % self.data_buffer_size
                else:
                    # no remaining allocation, reset to zero
                    self.data_buffer_start = self.data_buffer_end = 0
                freed_bytes += metadata[1]
            else:
                # there are still readers, we cannot free the buffer
                break

    logger.debug(
        "Freed %d bytes from the ring buffer, "
        "monotonic_id_start: %d, monotonic_id_end: %d",
        freed_bytes,
        self.monotonic_id_start,
        self.monotonic_id_end,
    )

    # buffer wrap around
    if self.data_buffer_start >= self.data_buffer_size:
        self.data_buffer_start -= self.data_buffer_size
        self.data_buffer_end -= self.data_buffer_size

    monotonic_id_after = self.monotonic_id_start
    # id wrap around
    if monotonic_id_after >= monotonic_id_before:
        return range(monotonic_id_before, monotonic_id_after)
    else:
        return chain(
            range(monotonic_id_before, self.ID_MAX), range(0, monotonic_id_after)
        )
```

### int2byte [¶](#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmRingBuffer.int2byte "Permanent link")

Convert an integer to bytes.

Source code in `vllm/distributed/device_communicators/shm_object_storage.py`

```
defint2byte(self, integer: int) -> bytes:
"""Convert an integer to bytes."""
    return integer.to_bytes(self.ID_NBYTES, "little", signed=True)
```