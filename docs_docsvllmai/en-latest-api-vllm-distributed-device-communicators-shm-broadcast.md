---
title: shm_broadcast - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/device_communicators/shm_broadcast/
source: sitemap
fetched_at: 2026-05-07T21:17:40.018127058-03:00
rendered_js: false
word_count: 68
summary: This document defines a MessageQueue class that facilitates inter-process communication between writers and readers using shared memory or ZeroMQ sockets.
tags:
    - message-queue
    - inter-process-communication
    - shared-memory
    - zeromq
    - parallel-processing
    - vllm
category: api
---

```
classMessageQueue:
    def__init__(
        self,
        n_reader,  # number of all readers
        n_local_reader,  # number of local readers through shared memory
        local_reader_ranks: list[int] | None = None,
        # Default of 24MiB chosen to be large enough to accommodate grammar
        # bitmask tensors for large batches (1024 requests).
        max_chunk_bytes: int = 1024 * 1024 * 24,
        max_chunks: int = 10,
        connect_ip: str | None = None,
    ):
        if local_reader_ranks is None:
            local_reader_ranks = list(range(n_local_reader))
        else:
            assert len(local_reader_ranks) == n_local_reader
        self.n_local_reader = n_local_reader
        n_remote_reader = n_reader - n_local_reader
        self.n_remote_reader = n_remote_reader
        self.shutting_down = False
        context = Context()

        if n_local_reader > 0:
            # for local readers, we will:
            # 1. create a shared memory ring buffer to communicate small data
            # 2. create a publish-subscribe socket to communicate large data
            self.buffer = ShmRingBuffer(n_local_reader, max_chunk_bytes, max_chunks)

            # XPUB is very similar to PUB,
            # except that it can receive subscription messages
            # to confirm the number of subscribers
            self.local_socket = context.socket(XPUB)
            # set the verbose option so that we can receive every subscription
            # message. otherwise, we will only receive the first subscription
            # see http://api.zeromq.org/3-3:zmq-setsockopt for more details
            self.local_socket.setsockopt(XPUB_VERBOSE, True)
            local_subscribe_addr = get_open_zmq_ipc_path()
            logger.debug("Binding to %s", local_subscribe_addr)
            self.local_socket.bind(local_subscribe_addr)

            self.current_idx = 0

            # Create the notification side of the SpinCondition
            local_notify_addr = get_open_zmq_ipc_path()
            self._spin_condition = SpinCondition(
                is_reader=False, context=context, notify_address=local_notify_addr
            )
        else:
            self.buffer = None  # type: ignore
            local_subscribe_addr = None
            self.local_socket = None
            self.current_idx = -1
            local_notify_addr = None
            self._spin_condition = None  # type: ignore

        remote_addr_ipv6 = False
        if n_remote_reader > 0:
            # for remote readers, we will:
            # create a publish-subscribe socket to communicate large data
            if not connect_ip:
                connect_ip = get_ip()
            self.remote_socket = context.socket(XPUB)
            self.remote_socket.setsockopt(XPUB_VERBOSE, True)
            remote_subscribe_port = get_open_port()
            if is_valid_ipv6_address(connect_ip):
                self.remote_socket.setsockopt(IPV6, 1)
                remote_addr_ipv6 = True
                connect_ip = f"[{connect_ip}]"
            socket_addr = f"tcp://{connect_ip}:{remote_subscribe_port}"
            self.remote_socket.bind(socket_addr)
            remote_subscribe_addr = f"tcp://{connect_ip}:{remote_subscribe_port}"
        else:
            remote_subscribe_addr = None
            self.remote_socket = None

        self._is_writer = True
        self._is_local_reader = False
        self.local_reader_rank = -1
        # rank does not matter for remote readers
        self._is_remote_reader = False

        self.handle = Handle(
            local_reader_ranks=local_reader_ranks,
            buffer_handle=self.buffer.handle() if self.buffer is not None else None,
            local_subscribe_addr=local_subscribe_addr,
            local_notify_addr=local_notify_addr,
            remote_subscribe_addr=remote_subscribe_addr,
            remote_addr_ipv6=remote_addr_ipv6,
        )

        logger.debug("vLLM message queue communication handle: %s", self.handle)

    defexport_handle(self) -> Handle:
        return self.handle

    @staticmethod
    defcreate_from_handle(handle: Handle, rank) -> "MessageQueue":
        self = MessageQueue.__new__(MessageQueue)
        self.handle = handle
        self._is_writer = False

        context = Context()

        if rank in handle.local_reader_ranks:
            assert handle.buffer_handle is not None
            self.buffer = ShmRingBuffer(*handle.buffer_handle)
            self.current_idx = 0
            self.local_reader_rank = handle.local_reader_ranks.index(rank)
            self._is_local_reader = True
            self._is_remote_reader = False

            self.local_socket = context.socket(SUB)
            self.local_socket.setsockopt_string(SUBSCRIBE, "")
            socket_addr = handle.local_subscribe_addr
            logger.debug("Connecting to %s", socket_addr)
            self.local_socket.connect(socket_addr)

            self.remote_socket = None
            assert isinstance(handle.local_notify_addr, str)
            self._spin_condition = SpinCondition(
                is_reader=True, context=context, notify_address=handle.local_notify_addr
            )
        else:
            self.buffer = None  # type: ignore
            self.current_idx = -1
            self.local_reader_rank = -1
            self._is_local_reader = False
            self._is_remote_reader = True

            self.local_socket = None

            self.remote_socket = context.socket(SUB)
            self.remote_socket.setsockopt_string(SUBSCRIBE, "")
            if handle.remote_addr_ipv6:
                self.remote_socket.setsockopt(IPV6, 1)
            socket_addr = handle.remote_subscribe_addr
            logger.debug("Connecting to %s", socket_addr)
            self.remote_socket.connect(socket_addr)
            self._spin_condition = None  # type: ignore

        self.shutting_down = False
        return self

    defwait_until_ready(self):
"""This is a collective operation. All processes (including the
        readers and the writer) should call this function.
        """
        if self._is_writer:
            # wait for all readers to connect

            # local readers
            for i in range(self.n_local_reader):
                # wait for subscription messages from all local readers
                self.local_socket.recv()
            if self.n_local_reader > 0:
                # send a message to all local readers
                # to make sure the publish channel is working
                self.local_socket.send(b"READY")

            # remote readers
            for i in range(self.n_remote_reader):
                # wait for subscription messages from all remote readers
                self.remote_socket.recv()
            if self.n_remote_reader > 0:
                # send a message to all remote readers
                # to make sure the publish channel is working
                self.remote_socket.send(b"READY")
        elif self._is_local_reader:
            # wait for the writer to send a message
            recv = self.local_socket.recv()
            assert recv == b"READY"
        elif self._is_remote_reader:
            # wait for the writer to send a message
            recv = self.remote_socket.recv()
            assert recv == b"READY"

    defshutdown(self):
"""If this is an idle reader, wakes it up so it can clean up and shut
        down"""
        self.shutting_down = True
        if self._spin_condition is not None:
            self._spin_condition.cancel()

    @contextmanager
    defacquire_write(self, timeout: float | None = None):
        assert self._is_writer, "Only writers can acquire write"
        start_time = time.monotonic()
        n_warning = 1
        while True:
            with self.buffer.get_metadata(self.current_idx) as metadata_buffer:
                # Memory fence ensures we see the latest read flags from readers.
                # Without this, we may read stale flags from our CPU cache and
                # spin indefinitely even though readers have completed.
                memory_fence()
                read_count = sum(metadata_buffer[1:])
                written_flag = metadata_buffer[0]
                if written_flag and read_count != self.buffer.n_reader:
                    # this block is written and not read by all readers
                    # for writers, `self.current_idx` is the next block to write
                    # if this block is not ready to write,
                    # we need to wait until it is read by all readers

                    # Release the processor to other threads
                    sched_yield()

                    # if we time out, raise an exception
                    elapsed = time.monotonic() - start_time
                    if timeout is not None and elapsed > timeout:
                        raise TimeoutError

                    # if we wait for a long time, log a message
                    if elapsed > VLLM_RINGBUFFER_WARNING_INTERVAL * n_warning:
                        logger.info(
                            LONG_WAIT_TIME_LOG_MSG, VLLM_RINGBUFFER_WARNING_INTERVAL
                        )
                        n_warning += 1

                    continue
                # found a block that is either
                # (1) not written
                # (2) read by all readers

                # mark the block as not written
                metadata_buffer[0] = 0
                # let caller write to the buffer
                with self.buffer.get_data(self.current_idx) as buf:
                    yield buf

                # caller has written to the buffer
                # NOTE: order is important here
                # first set the read flags to 0
                # then set the written flag to 1
                # otherwise, the readers may think they already read the block
                for i in range(1, self.buffer.n_reader + 1):
                    # set read flag to 0, meaning it is not read yet
                    metadata_buffer[i] = 0
                # Memory fence here ensures the order of the buffer and flag
                # writes. This guarantees that when `metadata_buffer[0] = 1` is
                # visible to readers, `buf` can be completely ready. Without
                # this, some CPU architectures with weak ordering may incur
                # memory inconsistency.
                memory_fence()
                # mark the block as written
                metadata_buffer[0] = 1
                # Memory fence ensures the write is visible to readers on other cores
                # before we proceed. Without this, readers may spin indefinitely
                # waiting for a write that's stuck in our CPU's store buffer.
                memory_fence()
                self.current_idx = (self.current_idx + 1) % self.buffer.max_chunks
                break

    classReadTimeoutWithWarnings:
        def__init__(self, timeout: float | None, should_warn: bool) -> None:
            self.started = time.monotonic()
            self.deadline = sys.maxsize if timeout is None else self.started + timeout

            # if should_warn, we need to wake up periodically to log
            self.warning_wait_time_ms: int | None = (
                VLLM_RINGBUFFER_WARNING_INTERVAL * 1000 if should_warn else None
            )

            self._should_warn = should_warn
            self.n_warning = 1
            self.timeout = timeout

        deftimeout_ms(self) -> int | None:
"""Returns a timeout that is:
            - min(time to deadline, time to next warning) if we're logging warnings
            - time to deadline, if we're not logging warnings
            - None if the timeout is None and we're not logging warnings
            - raise TimeoutError if we are past the deadline
            """
            warning_wait_time = self.warning_wait_time_ms
            if self.timeout is None:
                return warning_wait_time

            time_left_ms = int((self.deadline - time.monotonic()) * 1000)
            if time_left_ms <= 0:
                raise TimeoutError

            if warning_wait_time and warning_wait_time < time_left_ms:
                return warning_wait_time

            return time_left_ms

        defshould_warn(self) -> bool:
"""Returns true if it's time to log a warning for a timeout that is not
            indefinite"""
            if self._should_warn:
                elapsed = time.monotonic() - self.started
                if elapsed >= VLLM_RINGBUFFER_WARNING_INTERVAL * self.n_warning:
                    self.n_warning += 1
                    return True
            return False

    @contextmanager
    defacquire_read(
        self,
        timeout: float | None = None,
        indefinite: bool = False,
    ):
        assert self._is_local_reader, "Only readers can acquire read"
        read_timeout = self.ReadTimeoutWithWarnings(
            timeout=timeout, should_warn=not indefinite
        )
        with self.buffer.get_metadata(self.current_idx) as metadata_buffer:
            while True:
                # Memory fence ensures we see the latest writes from the writer.
                # Without this, we may read stale flags from our CPU cache
                # and spin indefinitely even though writer has updated them.
                memory_fence()
                read_flag = metadata_buffer[self.local_reader_rank + 1]
                written_flag = metadata_buffer[0]
                if not written_flag or read_flag:
                    # this block is either
                    # (1) not written
                    # (2) already read by this reader

                    # for readers, `self.current_idx` is the next block to read
                    # if this block is not ready,
                    # we need to wait until it is written
                    self._spin_condition.wait(timeout_ms=read_timeout.timeout_ms())

                    if self.shutting_down:
                        raise RuntimeError("cancelled")

                    # if we wait for a long time, log a message
                    if read_timeout.should_warn():
                        logger.info(
                            LONG_WAIT_TIME_LOG_MSG, VLLM_RINGBUFFER_WARNING_INTERVAL
                        )

                    continue
                # found a block that is not read by this reader
                # let caller read from the buffer
                with self.buffer.get_data(self.current_idx) as buf:
                    yield buf

                # caller has read from the buffer
                # set the read flag
                metadata_buffer[self.local_reader_rank + 1] = 1
                # Memory fence ensures the read flag is visible to the writer.
                # Without this, writer may not see our read completion and
                # could wait indefinitely for all readers to finish.
                memory_fence()
                self.current_idx = (self.current_idx + 1) % self.buffer.max_chunks

                self._spin_condition.record_read()
                break

    defenqueue(self, obj, timeout: float | None = None):
"""Write to message queue with optional timeout (in seconds)"""
        assert self._is_writer, "Only writers can enqueue"
        all_buffers: list[SizedBuffer] = [b""]
        total_bytes = 6  # 2 bytes for oob buffer count, 4 for main buffer size

        defoob_callback(buf: PickleBuffer) -> bool:
            raw_buf = buf.raw()
            if len(raw_buf) < 1024 * 1024:
                # In-line buffers smaller than 1MiB.
                return True
            all_buffers.append(raw_buf)
            nonlocal total_bytes
            total_bytes += len(raw_buf) + 4
            return False

        all_buffers[0] = pickle.dumps(
            obj, protocol=pickle.HIGHEST_PROTOCOL, buffer_callback=oob_callback
        )
        if self.n_local_reader > 0:
            if total_bytes + len(all_buffers[0]) >= self.buffer.max_chunk_bytes:
                with self.acquire_write(timeout) as buf:
                    buf[0] = 1  # overflow
                self.local_socket.send_multipart(all_buffers, copy=False)
            else:
                # Byte 0: 0
                # Bytes 1-2: Count of buffers
                # Then each buffer follows, preceded by 4 bytes containing its length:
                # [4 byte int L][L bytes of buffer content] ...
                with self.acquire_write(timeout) as buf:
                    buf[0] = 0  # not overflow
                    offset = 3
                    buf[1:offset] = to_bytes_big(len(all_buffers), 2)  # oob buf count
                    for buffer in all_buffers:
                        buf_len = len(buffer)
                        # prepend each buffer with 4 bytes containing its size.
                        buf_offset = offset + 4
                        buf[offset:buf_offset] = to_bytes_big(buf_len, 4)
                        buf[buf_offset : (offset := buf_offset + buf_len)] = buffer

            self._spin_condition.notify()

        if self.n_remote_reader > 0:
            self.remote_socket.send_multipart(all_buffers, copy=False)

    defdequeue(
        self,
        timeout: float | None = None,
        indefinite: bool = False,
    ):
"""Read from message queue with optional timeout (in seconds)"""
        if self._is_local_reader:
            with self.acquire_read(timeout, indefinite) as buf:
                overflow = buf[0] == 1
                if not overflow:
                    offset = 3
                    buf_count = from_bytes_big(buf[1:offset])
                    all_buffers = []
                    for i in range(buf_count):
                        buf_offset = offset + 4
                        buf_len = from_bytes_big(buf[offset:buf_offset])
                        offset = buf_offset + buf_len
                        all_buffers.append(buf[buf_offset:offset])
                    obj = pickle.loads(all_buffers[0], buffers=all_buffers[1:])
            if overflow:
                obj = MessageQueue.recv(self.local_socket, timeout)
        elif self._is_remote_reader:
            obj = MessageQueue.recv(self.remote_socket, timeout)
        else:
            raise RuntimeError("Only readers can dequeue")
        return obj

    @staticmethod
    defrecv(socket: zmq.Socket, timeout: float | None) -> Any:
        timeout_ms = None if timeout is None else int(timeout * 1000)
        if not socket.poll(timeout=timeout_ms):
            raise TimeoutError
        recv, *recv_oob = socket.recv_multipart(copy=False)
        return pickle.loads(recv, buffers=recv_oob)

    defbroadcast_object(self, obj=None):
        if self._is_writer:
            self.enqueue(obj)
            return obj
        return self.dequeue()

    @staticmethod
    defcreate_from_process_group_single_reader(
        pg: ProcessGroup,
        max_chunk_bytes,
        max_chunks,
        reader_rank: int = 0,
        blocking: bool = False,
    ) -> tuple["MessageQueue", list[Handle]]:
"""
        Creates a MessageQueue for a process group with a single reader.

        This method is designed for scenarios where only one process (the reader)
        will consume messages, and all other processes are writers. It sets up
        the shared memory buffer and communication handles accordingly, and
        gathers the handles from all processes to the reader.

        Args:
            pg (ProcessGroup): The torch distributed process group.
            max_chunk_bytes (int): Maximum size in bytes for each chunk in the buffer.
            max_chunks (int): Maximum number of chunks in the buffer.
            reader_rank (int, optional): The global rank that will act as the reader.
                Defaults to 0.
            blocking (bool, optional): If True, blocks until all processes are ready.
                Defaults to False.

        Returns:
            tuple[MessageQueue, list[Handle]]:
            The MessageQueue instance for the calling process,
            and a list of handles (only non-empty for the reader process).
        """
        local_size = current_platform.device_count()
        rank = dist.get_rank()
        same_node = rank // local_size == reader_rank // local_size
        buffer_io = MessageQueue(
            n_reader=1,
            n_local_reader=1 if same_node else 0,
            max_chunk_bytes=max_chunk_bytes,
            max_chunks=max_chunks,
        )
        handle = buffer_io.export_handle()
        handles = [None] * dist.get_world_size(pg) if rank == reader_rank else None
        dist.gather_object(handle, handles, dst=reader_rank, group=pg)
        if blocking:
            buffer_io.wait_until_ready()
        return buffer_io, cast(list[Handle], handles or [])

    @staticmethod
    defcreate_from_process_group(
        pg: ProcessGroup | StatelessProcessGroup,
        max_chunk_bytes,
        max_chunks,
        writer_rank: int = 0,
        external_writer_handle=None,
        blocking: bool = True,
    ) -> "MessageQueue":
"""
        Creates a MessageQueue for a distributed process group with one writer and
        multiple readers.

        This method is designed for scenarios where one process (the writer) sends
        messages, and all other processes (the readers) receive messages. It sets up
        the shared memory buffer and socket communication handles accordingly, and
        broadcasts the handle from the writer to all readers.

        Args:
            pg (ProcessGroup | StatelessProcessGroup): The torch distributed process
                group.
            max_chunk_bytes (int): Maximum size in bytes for each chunk in the buffer.
            max_chunks (int): Maximum number of chunks in the buffer.
            writer_rank (int, optional): The global rank that will act as the writer.
                Defaults to 0.
            external_writer_handle (Handle, optional): Used when there is a handle
                from an external Message Queue. If provided, use this handle to init
                PG writer message queue instead of creating a new one. Defaults to None.
            blocking (bool, optional): If True, blocks until all processes are ready.
                Defaults to True.

        Returns:
            MessageQueue: The MessageQueue instance for the calling process.

        """
        if isinstance(pg, ProcessGroup):
            group_rank = dist.get_rank(pg)
            group_world_size = dist.get_world_size(pg)
            global_ranks = dist.get_process_group_ranks(pg)
        else:
            group_rank = pg.rank
            group_world_size = pg.world_size
            global_ranks = list(range(pg.world_size))
        fromvllm.distributed.parallel_stateimport in_the_same_node_as

        status = in_the_same_node_as(pg, source_rank=writer_rank)
        if group_rank == writer_rank:
            if external_writer_handle is not None:
                buffer_io = MessageQueue.create_from_handle(
                    external_writer_handle, group_rank
                )
            else:
                same_node_ranks = [i for i, s in enumerate(status) if s]
                n_reader = group_world_size - 1
                n_local_reader = len(same_node_ranks) - 1
                local_reader_ranks = [i for i in same_node_ranks if i != writer_rank]
                buffer_io = MessageQueue(
                    n_reader=n_reader,
                    n_local_reader=n_local_reader,
                    local_reader_ranks=local_reader_ranks,
                    max_chunk_bytes=max_chunk_bytes,
                    max_chunks=max_chunks,
                )
            handle = buffer_io.export_handle()
            if isinstance(pg, ProcessGroup):
                dist.broadcast_object_list(
                    [handle], src=global_ranks[writer_rank], group=pg
                )
            else:
                pg.broadcast_obj(handle, writer_rank)
        else:
            if isinstance(pg, ProcessGroup):
                recv = [None]
                dist.broadcast_object_list(
                    recv, src=global_ranks[writer_rank], group=pg
                )
                handle = recv[0]  # type: ignore
            else:
                handle = pg.broadcast_obj(None, writer_rank)
            buffer_io = MessageQueue.create_from_handle(handle, group_rank)
        if blocking:
            buffer_io.wait_until_ready()
        return buffer_io
```