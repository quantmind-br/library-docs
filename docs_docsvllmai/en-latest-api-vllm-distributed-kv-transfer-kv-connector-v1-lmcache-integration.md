---
title: lmcache_integration - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/
source: sitemap
fetched_at: 2026-05-07T21:18:23.926457636-03:00
rendered_js: false
word_count: 53
summary: This document defines a Python class that acts as an adapter for vLLM to interact with the LMCache server, facilitating the registration, storage, and retrieval of KV caches.
tags:
    - lmcache
    - vllm
    - kv-cache
    - caching
    - gpu-memory
    - distributed-inference
category: api
---

```
classLMCacheMPWorkerAdapter:
    def__init__(
        self,
        server_url: str,
        context: zmq.Context,
        model_name: str,
        vllm_block_size: int,
        parallel_strategy: ParallelStrategy,
    ):
        self.mq_client = MessageQueueClient(server_url, context)

        # Instance id for GPU worker
        self.instance_id = os.getpid()

        # Registered kv caches from vLLM
        self.kv_caches: dict[str, torch.Tensor] = {}

        # Request futures
        # request_id -> (future, other merged requests)
        self.store_futures: dict[
            str, tuple[MessagingFuture[StoreResult], list[str]]
        ] = {}
        self.retrieve_futures: dict[
            str, tuple[MessagingFuture[RetrieveResult], list[str]]
        ] = {}

        # The store requests that have finished execution in LMCache
        self.finished_stores: set[str] = set()
        # The finished request ids that are passed via vLLM and also
        # have corresponding store requests submitted to LMCache before
        self.previously_finished: set[str] = set()

        self.model_name = model_name
        self.parallel_strategy = parallel_strategy

        # Read chunk size from lmcache
        chunk_size = get_lmcache_chunk_size(self.mq_client)
        assert chunk_size % vllm_block_size == 0, (
            "LMCache chunk size should be a multiple of vLLM block size"
        )
        self.blocks_in_chunk = chunk_size // vllm_block_size

    @property
    defworld_size(self) -> int:
"""The world size."""
        return self.parallel_strategy.kv_world_size

    @property
    defworker_id(self) -> int:
"""The worker id."""
        return self.parallel_strategy.kv_worker_id

    @property
    defuse_mla(self) -> bool:
"""Whether to use MLA."""
        return self.parallel_strategy.use_mla

    @property
    defis_first_rank_of_pp_group(self) -> bool:
"""Is the first rank of the pipeline parallel group."""
        return (
            self.parallel_strategy.actual_worker_id % self.parallel_strategy.tp_size
            == 0
        )

    defregister_kv_caches(self, kv_caches: dict[str, torch.Tensor]):
"""
        Register the kv caches with LMCache server

        Args:
            kv_caches: A dict of kv caches to register. The keys are the
                layer names and the values are the corresponding tensors.
        """
        # Register kv cache and send the request
        self.kv_caches = kv_caches
        logger.info("Registering kv caches")
        future = send_lmcache_request(
            self.mq_client,
            RequestType.REGISTER_KV_CACHE,
            [self.instance_id, wrap_kv_caches(kv_caches)],
        )
        future.result()

    @_lmcache_nvtx_annotate
    defsubmit_store_request(
        self, request_id: str, op: LoadStoreOp, event: torch.cuda.Event
    ):
"""
        Submit a KV cache store request to LMCache

        Args:
            request_id: The ID of the request
            op: The LoadStoreOp describing the store operation.
            event: The CUDA event that is recorded after the current
                model inference step
        """
        if op.block_hashes is not None:
            # Hash mode
            chunk_hashes = list(
                striding_block_hashes(op.block_hashes, self.blocks_in_chunk)
            )
            keys = [
                self._create_hash_key(ch, request_id=request_id) for ch in chunk_hashes
            ]
        else:
            # Token mode
            assert op.token_ids is not None
            keys = [
                self._create_key(op.token_ids, op.start, op.end, request_id=request_id)
            ]
        future = send_lmcache_request(
            self.mq_client,
            RequestType.STORE,
            [keys, self.instance_id, op.block_ids, event.ipc_handle()],
        ).to_cuda_future()
        self.store_futures[request_id] = (future, [])

    @_lmcache_nvtx_annotate
    defsubmit_retrieve_request(
        self, request_id: str, op: LoadStoreOp, event: torch.cuda.Event
    ):
"""
        Submit a KV cache retrieve request to LMCache

        Args:
            request_id: The ID of the request
            op: The LoadStoreOp describing the retrieve operation.
            event: The CUDA event that is recorded after the current
                model inference step
        """
        if op.block_hashes is not None:
            # Hash mode
            chunk_hashes = list(
                striding_block_hashes(op.block_hashes, self.blocks_in_chunk)
            )
            keys = [
                self._create_hash_key(ch, request_id=request_id) for ch in chunk_hashes
            ]
        else:
            # Token mode
            assert op.token_ids is not None
            keys = [
                self._create_key(op.token_ids, op.start, op.end, request_id=request_id)
            ]
        future = send_lmcache_request(
            self.mq_client,
            RequestType.RETRIEVE,
            [keys, self.instance_id, op.block_ids, event.ipc_handle()],
        ).to_cuda_future()
        self.retrieve_futures[request_id] = (future, [])

    @_lmcache_nvtx_annotate
    defbatched_submit_store_requests(
        self,
        request_ids: list[str],
        ops: list[LoadStoreOp],
        event: torch.cuda.Event,
    ):
"""
        Submit a batched store request to LMCache

        Args:
            request_ids: The IDs of the requests
            ops: The LoadStoreOps describing the store operations. Should have
                the same length as request_ids
            event: The CUDA event that is recorded after the current
                model inference step
        """
        all_keys: list[IPCCacheEngineKey] = []
        block_ids: list[int] = []
        for request_id, op in zip(request_ids, ops, strict=False):
            if op.block_hashes is not None:
                chunk_hashes = list(
                    striding_block_hashes(op.block_hashes, self.blocks_in_chunk)
                )
                keys = [
                    self._create_hash_key(ch, request_id=request_id)
                    for ch in chunk_hashes
                ]
                all_keys.extend(keys)
            else:
                assert op.token_ids is not None
                all_keys.append(
                    self._create_key(
                        op.token_ids, op.start, op.end, request_id=request_id
                    )
                )
            block_ids.extend(op.block_ids)
        future = send_lmcache_request(
            self.mq_client,
            RequestType.STORE,
            [
                all_keys,
                self.instance_id,
                block_ids,
                event.ipc_handle(),
            ],
        ).to_cuda_future()
        self.store_futures[request_ids[0]] = (future, list(request_ids[1:]))

    @_lmcache_nvtx_annotate
    defbatched_submit_retrieve_requests(
        self,
        request_ids: list[str],
        ops: list[LoadStoreOp],
        event: torch.cuda.Event,
    ):
"""
        Submit a batched retrieve request to LMCache

        Args:
            request_ids: The IDs of the requests
            ops: The LoadStoreOps describing the retrieve operations. Should have
                the same length as request_ids
            event: The CUDA event that is recorded after the current
                model inference step
        """
        all_keys: list[IPCCacheEngineKey] = []
        block_ids: list[int] = []
        for request_id, op in zip(request_ids, ops, strict=False):
            if op.block_hashes is not None:
                chunk_hashes = list(
                    striding_block_hashes(op.block_hashes, self.blocks_in_chunk)
                )
                keys = [
                    self._create_hash_key(ch, request_id=request_id)
                    for ch in chunk_hashes
                ]
                all_keys.extend(keys)
            else:
                assert op.token_ids is not None
                all_keys.append(
                    self._create_key(
                        op.token_ids, op.start, op.end, request_id=request_id
                    )
                )
            block_ids.extend(op.block_ids)
        future = send_lmcache_request(
            self.mq_client,
            RequestType.RETRIEVE,
            [
                all_keys,
                self.instance_id,
                block_ids,
                event.ipc_handle(),
            ],
        ).to_cuda_future()
        self.retrieve_futures[request_ids[0]] = (future, list(request_ids[1:]))

    @_lmcache_nvtx_annotate
    defget_finished(
        self, finished_req_ids_from_engine: set[str]
    ) -> tuple[set[str] | None, set[str] | None]:
"""
        Check and get the finished store and retrieve requests.

        Args:
            finished_req_ids_from_engine: the set of request ids that are
                reported as finished from the vLLM engine side.

        Returns:
            A tuple of two sets:
            - The first set contains the finished store request ids. The returned
                store request ids MUST be seen before in the
                `finished_req_ids_from_engine`.
            - The second set contains the finished retrieve request ids.

        Notes:
            When enabling async scheduling in vLLM, the same request ID may appear
            multiple times in `finished_req_ids_from_engine`. The adapter should
            take care of deduplicating the request IDs and only return the request
            IDs that have not been returned before.
        """
        finished_stores = set()
        finished_retrieves = set()
        for request_id, (s_future, other_reqs) in self.store_futures.items():
            if not s_future.query():
                continue

            s_result = s_future.result()
            finished_stores.add(request_id)
            finished_stores.update(other_reqs)

            if not s_result:
                # TODO: add error handling here
                logger.error(
                    "Something went wrong when processing the "
                    "store request for request_id=%s",
                    request_id,
                )

        for request_id, (r_future, other_reqs) in self.retrieve_futures.items():
            if not r_future.query():
                continue

            r_result = r_future.result()
            finished_retrieves.add(request_id)
            finished_retrieves.update(other_reqs)

            if not all(r_result):
                # TODO: add error handing here
                logger.error(
                    "Something went wrong when processing the "
                    "retrieve request for request_id=%s, result=%s",
                    request_id,
                    r_result,
                )

        # Remove the finished requests from the tracking dicts
        for request_id in finished_stores:
            self.store_futures.pop(request_id, None)
        for request_id in finished_retrieves:
            self.retrieve_futures.pop(request_id, None)

        # Update the internal states
        self.finished_stores.update(finished_stores)

        ret_stores = set()
        for req_id in finished_req_ids_from_engine:
            if req_id in self.finished_stores or req_id in self.store_futures:
                self.previously_finished.add(req_id)
            else:
                ret_stores.add(req_id)

        # Calculate the final finished stores
        ret_stores.update(self._update_and_get_finished_store())

        return ret_stores, finished_retrieves

    defnum_blocks_per_chunk(self) -> int:
"""
        Returns:
            The number of vllm blocks in a LMCache data chunk
        """
        return self.blocks_in_chunk

    defshutdown(self):
"""
        Shutdown the LMCache MP worker adapter
        """
        logger.info("Unregistering kv caches")
        send_lmcache_request(
            self.mq_client, RequestType.UNREGISTER_KV_CACHE, [self.instance_id]
        ).result()

        self.mq_client.close()

    # Helper functions
    def_update_and_get_finished_store(
        self,
    ) -> set[str]:
"""Converge the internal states about finished stores
        and returns the 'safe finished store request ids' back
        """
        safe_finished_s = self.finished_stores.intersection(self.previously_finished)
        self.finished_stores.difference_update(self.previously_finished)
        self.previously_finished.difference_update(safe_finished_s)

        return safe_finished_s

    def_create_key(
        self,
        token_ids: list[int],
        start: int = 0,
        end: int = 0,
        request_id: str | None = None,
    ) -> IPCCacheEngineKey:
"""Convert token IDs to an IPC cache engine key"""
        return IPCCacheEngineKey(
            model_name=self.model_name,
            world_size=self.world_size,
            worker_id=self.worker_id,
            token_ids=tuple(token_ids),
            start=start,
            end=end,
            request_id=request_id,
        )

    def_create_hash_key(
        self, chunk_hash: bytes, request_id: str | None = None
    ) -> IPCCacheEngineKey:
"""Create a hash-mode IPC cache engine key"""
        return IPCCacheEngineKey(
            model_name=self.model_name,
            world_size=self.world_size,
            worker_id=self.worker_id,
            chunk_hash=chunk_hash,
            request_id=request_id,
        )
```