---
title: moriio_engine - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine/
source: sitemap
fetched_at: 2026-05-07T21:18:36.945667322-03:00
rendered_js: false
word_count: 0
summary: The MoRIIOWrapper class provides an interface for the MoRIIO engine to manage RDMA-based KV cache transfers between producer and consumer nodes, handling memory registration, session management, and asynchronous data transfer notifications.
tags:
    - moriio
    - rdma
    - kv-cache
    - distributed-computing
    - data-transfer
    - networking
category: api
---

```
classMoRIIOWrapper:
"""Wrapper for MoRIIO engine operations.

    Handles both producer and consumer roles for KV cache transfers.

    Args:
        moriio_engine:  MoRIIO engine instance
        tp_rank: Tensor parallel rank
        dp_rank: Data parallel rank
    """

    def__init__(
        self,
        moriio_engine: "IOEngine | None" = None,
        tp_rank: int = 0,
        dp_rank: int = 0,
    ):
        self.tp_rank = tp_rank
        self.dp_rank = dp_rank
        self.moriio_engine = moriio_engine
        self.remote_memory_metadata = None
        self.local_memory_registered = False
        self.local_memory_metadata = None
        self.transfer_status: list[Any] = []
        self.remote_engine_ip: str | None = None
        self.notify_port: int | None = None
        self.lock = threading.Lock()
        self.done_req_ids: list[str] = []
        self.done_remote_allocate_req_dict: dict[TransferId, RemoteAllocInfo] = {}
        self.done_write_cache_req_ids: list[str] = []
        self.notify_thread: threading.Thread | None = None
        self.sessions: list[IOEngine.Session] = []
        self.paths: dict[str, zmq.Socket] = {}

    defset_moriio_engine(self, moriio_engine):
        assert moriio_engine is not None, (
            "You Cannot pass None engine to MoRIIOWrapper!"
        )
        self.moriio_engine = moriio_engine

    defset_backend_type(self, backend_type):
        assert self.moriio_engine is not None, "MoRIIO engine must be set first"
        qp_per_transfer = envs.VLLM_MORIIO_QP_PER_TRANSFER
        post_batch_size = envs.VLLM_MORIIO_POST_BATCH_SIZE
        num_worker_threads = envs.VLLM_MORIIO_NUM_WORKERS
        poll_mode = PollCqMode.POLLING
        rdma_cfg = RdmaBackendConfig(
            qp_per_transfer,
            post_batch_size,
            num_worker_threads,
            poll_mode,
        )
        self.moriio_engine.create_backend(backend_type, rdma_cfg)

    defget_agent_metadata(self):
        assert self.moriio_engine is not None, "MoRIIO engine must be set first"
        engine_metadata = self.moriio_engine.get_engine_desc()
        engine_metadata_packed = engine_metadata.pack()
        return engine_metadata_packed

    defregister_remote_engine(self, remote_packed_engine_metadata):
        assert self.moriio_engine is not None, "MoRIIO engine must be set first"
        consumer_engine_metadata = EngineDesc.unpack(remote_packed_engine_metadata)
        self.moriio_engine.register_remote_engine(consumer_engine_metadata)
        return consumer_engine_metadata.key

    defregister_local_tensor(self, tensor: torch.Tensor):
        assert self.moriio_engine is not None, "MoRIIO engine must be set first"
        try:
            self.local_memory_metadata = self.moriio_engine.register_torch_tensor(
                tensor
            )
            assert self.local_memory_metadata is not None, (
                "register_torch_tensor returned None"
            )
            local_memory_metadata_packed = self.local_memory_metadata.pack()
        except Exception as e:
            raise MoRIIOError(f"Failed to register local memory: {e}") frome
        self.local_memory_registered = True
        return local_memory_metadata_packed

    defget_unpack_memory_metadata(self, packed_memory_metadata):
        return MemoryDesc.unpack(packed_memory_metadata)

    defbuild_session(self, local_memory_metadata, remote_memory_metadata):
        assert self.moriio_engine is not None, "MoRIIO engine must be set first"
        return self.moriio_engine.create_session(
            local_memory_metadata, remote_memory_metadata
        )

    defread_remote_data(
        self, transfer_size_byte, local_offset=0, remote_offset=0, session=None
    ):
        assert self.local_memory_registered, "You have not register local memory data!"
        assert self.moriio_engine is not None, "MoRIIO engine must be set first"
        transfer_status = session.batch_read(
            local_offset,
            remote_offset,
            transfer_size_byte,
            self.moriio_engine.allocate_transfer_uid(),
        )

        return transfer_status

    defwrite_remote_data(
        self, transfer_size_byte, local_offset=0, remote_offset=0, session=None
    ):
        assert self.local_memory_registered, "You have not register local memory data!"
        assert self.moriio_engine is not None, "MoRIIO engine must be set first"
        write_uid = self.moriio_engine.allocate_transfer_uid()

        transfer_status = session.batch_write(
            local_offset, remote_offset, transfer_size_byte, write_uid
        )
        with self.lock:
            self.transfer_status.append(transfer_status)

    defwrite_remote_data_single(
        self, transfer_size_byte, local_offset=0, remote_offset=0, sess_idx=0
    ):
        assert self.local_memory_registered, "You have not register local memory data!"
        assert self.moriio_engine is not None, "MoRIIO engine must be set first"
        transfer_status = self.sessions[sess_idx].write(
            local_offset,
            remote_offset,
            transfer_size_byte,
            self.moriio_engine.allocate_transfer_uid(),
        )
        with self.lock:
            self.transfer_status.append(transfer_status)

    defwaiting_for_transfer_complete(self):
        if not self.transfer_status:
            return

        transfers_to_wait = []
        with self.lock:
            transfers_to_wait = self.transfer_status[:]
            self.transfer_status.clear()

        for status in transfers_to_wait:
            try:
                status.Wait()
                if not status.Succeeded():
                    logger.error(
                        "Transfer failed: %s, Code: %s", status.Message(), status.Code()
                    )
                    raise TransferError("MoRIIO transfer failed!")
            except Exception as e:
                logger.error("Transfer %s failed: %s", status, e)
                raise

    defasync_wait_reqid(self):
        assert self.notify_port is not None, "Notify port cannot be None"

        if self.notify_thread is not None:
            return

        def_async_wait():
            host = "*"
            path = make_zmq_path("tcp", host, self.notify_port)
            logger.info("Node starting to listen notify from path = %s", path)

            with zmq_ctx(zmq.ROUTER, path) as sock:
                while True:
                    try:
                        identity, msg = sock.recv_multipart()
                        self._handle_message(msg)
                    except Exception as e:
                        logger.error("Error processing message: %s", e)
                        raise HandshakeError(f"Error processing message: {e}") frome

        self.notify_thread = threading.Thread(
            target=_async_wait, daemon=True, name="moriio-notify-listener"
        )
        self.notify_thread.start()

    def_handle_message(self, msg: bytes):
"""Handles incoming messages from remote nodes."""
        # Handles incoming remote messages:
        # Prefill Role:
        #   [write] mode: receives block information (allocation)
        #   [read]  mode: receives block release messages from decode side
        # Decode Role:
        #   [write] mode: receives KV cache write completion notifications
        handled = False
        try:
            data = msgpack.loads(msg)
            if isinstance(data, dict) and "req_id" in data:
                self._handle_structured_message(data)

                return
        except (msgpack.exceptions.ExtraData, msgpack.exceptions.UnpackException):
            logger.debug("Failed to decode msgpack message, will try as string")
            pass

        try:
            msg_str = msg.decode("UTF-8")
            if msg_str.startswith(MoRIIOConstants.TRANSFER_PREFIX):
                self._handle_completion_message(msg_str)
                handled = True
        except UnicodeDecodeError:
            logger.warning("Received non-UTF8 message: %s", msg_str)
        if not handled:
            raise MoRIIOError(f"Unhandled message format: {msg_str}")

    def_handle_structured_message(self, data: dict):
        assert get_role() == ROLE.PRODUCER, "Only prefill can get block messages"
        transfer_id = data["transfer_id"]
        block_notify_list = data.get("block_notify_list", [])
        decode_dp_rank = data.get("decode_rank", 0)
        assert len(block_notify_list) > 0, (
            "block_notify_list cannot be empty in remote allocate message"
        )

        with self.lock:
            self.done_remote_allocate_req_dict[transfer_id] = RemoteAllocInfo(
                block_ids=block_notify_list, decode_dp_rank=decode_dp_rank
            )

    def_handle_completion_message(self, msg: str):
        with self.lock:
            if get_role() == ROLE.PRODUCER:
                self.done_req_ids.append(msg)
            else:
                self.done_write_cache_req_ids.append(msg)

    defsend_notify(self, req_ids, remote_ip, remote_port):
        if not remote_ip or not remote_port:
            logger.warning("Missing remote_ip or remote_port for notification")
            return

        path = make_zmq_path("tcp", remote_ip, remote_port)

        if path not in self.paths:
            ctx = zmq.Context.instance()
            sock = make_zmq_socket(
                ctx=ctx, path=path, socket_type=zmq.DEALER, bind=False
            )
            self.paths[path] = sock

        req_list = req_ids if isinstance(req_ids, list) else [req_ids]

        sock = self.paths[path]
        try:
            for req_id in req_list:
                if not isinstance(req_id, str):
                    logger.warning(
                        "Invalid req_id type: %s, expected str", type(req_id)
                    )
                    continue
                sock.send(req_id.encode("utf-8"))
        except Exception as e:
            logger.error("Failed to send notification to %s: %s", path, e)
            self.paths.pop(path, None)
            raise

    defpop_finished_req_ids(self):
        # producer invocation: get the set of completed requests at the decode
        with self.lock:
            done_send = set(self.done_req_ids)
            self.done_req_ids = []
        return done_send

    defpop_finished_write_req_ids(self):
        # Call the consumer in write mode to get the collection after write completion
        with self.lock:
            done_write_cache = set(self.done_write_cache_req_ids)
            self.done_write_cache_req_ids = []
        return done_write_cache

    defshutdown(self):
        logger.debug("Closing MoRIIOWrapper and cleaning up ZMQ sockets")
        for path, sock in self.paths.items():
            try:
                sock.close(linger=0)
                logger.debug("Closed ZMQ socket for path: %s", path)
            except Exception as e:
                logger.warning("Error closing ZMQ socket for path %s: %s", path, e)
        self.paths.clear()
```