---
title: hf3fs_connector - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector/
source: sitemap
fetched_at: 2026-05-07T21:18:17.101241758-03:00
rendered_js: false
word_count: 0
summary: This class implements a key-value cache connector for the vLLM framework using the HF3FS distributed storage system, facilitating the saving and loading of KV cache blocks.
tags:
    - vllm
    - kv-cache
    - distributed-storage
    - hf3fs
    - machine-learning
    - connector-pattern
category: api
---

```
classHF3FSKVConnector(KVConnectorBase_V1):
"""HF3FS KV Connector implementation."""

    def__init__(
        self,
        vllm_config: "VllmConfig",
        role: KVConnectorRole,
        kv_cache_config: "KVCacheConfig",
    ):
        super().__init__(
            vllm_config=vllm_config, role=role, kv_cache_config=kv_cache_config
        )

        # Core configuration
        self._vllm_config = vllm_config
        self._role = role
        self._block_size = vllm_config.cache_config.block_size
        self._use_mla = vllm_config.model_config.use_mla
        self._model_config = vllm_config.model_config

        logger.info("Using MLA: %s", self._use_mla)

        # HF3FS configuration
        kv_config = vllm_config.kv_transfer_config
        assert kv_config is not None

        self._storage_path = kv_config.get_from_extra_config(
            "hf3fs_storage_path", "/vllm-workspace/mnt/hf3fs"
        )
        self._metadata_server_url = kv_config.get_from_extra_config(
            "hf3fs_metadata_server_url", "http://localhost:18000"
        )
        self._file_size = kv_config.get_from_extra_config(
            "hf3fs_file_size", 1024 * 1024 * 1024
        )
        self._numjobs = kv_config.get_from_extra_config("hf3fs_client_numjobs", 16)
        self._max_device_buffer_count = kv_config.get_from_extra_config(
            "hf3fs_max_device_buffer_count", 128
        )
        self._max_device_buffer_count = max(
            self._max_device_buffer_count, self._numjobs * DEFAULT_MAX_IO_ENTRIES
        )

        if self._role == KVConnectorRole.SCHEDULER:
            self._scheduling_states: dict[str, RequestSchedulingState] = {}
            self._metadata_client = Hf3fsMetadataClient()
            self._metadata_client.initialize(0, role="scheduler")

        atexit.register(self.close)
        signal.signal(signal.SIGINT, lambda sig, frame: self.close())
        signal.signal(signal.SIGTERM, lambda sig, frame: self.close())
        signal.signal(signal.SIGQUIT, lambda sig, frame: self.close())

        logger.info(
            "HF3FSKVConnector initialized: path=%s, role=%s",
            self._storage_path,
            self._role.name,
        )

    ############################################################
    # Worker Side Methods
    ############################################################

    defregister_kv_caches(self, kv_caches: dict[str, torch.Tensor]) -> None:
        self._kv_caches = kv_caches
        self._setup_kv_cache_config()
        self._setup_storage_clients()
        self._async_manager = AsyncOperationManager(self)

    def_setup_kv_cache_config(self):
        first_cache = next(iter(self._kv_caches.values()))
        self._device = first_cache.device
        self._dtype = first_cache.dtype
        element_size = first_cache.element_size()

        if self._use_mla:
            assert len(first_cache.shape) == 3, "MLA format should have 3 dimensions"
            # MLA format: [num_blocks, block_size, head_size]
            num_blocks, block_size, head_size = first_cache.shape
            num_heads = 1
        else:
            # MHA format: [2, num_blocks, block_size, num_heads, head_size]
            _, num_blocks, block_size, num_heads, head_size = first_cache.shape

        self._local_total_tokens = num_blocks * block_size
        self._local_block_size = block_size

        if self._use_mla:
            layer_block_size = block_size * head_size * element_size
            self._bytes_per_page = layer_block_size * len(self._kv_caches)
            self._shape_per_page = [
                len(self._kv_caches),
                block_size,
                head_size,
            ]
        else:
            layer_block_size = 2 * block_size * num_heads * head_size * element_size
            self._bytes_per_page = layer_block_size * len(self._kv_caches)
            self._shape_per_page = [
                len(self._kv_caches),
                2,
                block_size,
                num_heads * head_size,
            ]

        self._kvcache_ptrs = torch.tensor(
            [cache.data_ptr() for cache in self._kv_caches.values()],
            dtype=torch.int64,
            device=self._device,
        )

    def_setup_storage_clients(self):
        os.makedirs(self._storage_path, exist_ok=True)

        self._rank = get_tensor_model_parallel_rank()
        file_path = os.path.join(
            self._storage_path, f"hf3fs_vllm_data_file_{self._rank}"
        )

        try:
            # Initialize HF3FS clients
            self._ac = AtomicCounter(self._numjobs)
            assert Hf3fsClient is not None
            self._clients = [
                Hf3fsClient(
                    path=file_path,
                    size=self._file_size,
                    bytes_per_page=self._bytes_per_page,
                    entries=DEFAULT_MAX_IO_ENTRIES,
                )
                for _ in range(self._numjobs)
            ]

            # Initialize metadata client
            num_pages = self._file_size // self._bytes_per_page
            self._metadata_client = Hf3fsMetadataClient()
            self._metadata_client.initialize(self._rank, num_pages, role="worker")
        except Exception as e:
            logger.error("HF3FS client initialization failed: %s", e)
            raise

    defsave_kv_layer(
        self,
        layer_name: str,
        kv_layer: torch.Tensor,
        attn_metadata: "AttentionMetadata",
        **kwargs,
    ) -> None:
"""HF3FSConnector does not do layerwise saving."""
        pass

    defwait_for_save(self) -> None:
        metadata = self._get_connector_metadata()
        if not isinstance(metadata, HF3FSConnectorMetadata):
            logger.error("Invalid metadata type: %s", type(metadata))
            return

        for request in metadata.requests:
            if request.save_block_op is None:
                continue

            skip_blocks = request.save_block_op.skip_leading_blocks
            block_hashes = self._generate_block_hashes(request.token_ids, skip_blocks)
            block_ids = request.block_ids[skip_blocks : skip_blocks + len(block_hashes)]

            for i in range(0, len(block_ids), self._max_device_buffer_count):
                batch_block_ids = block_ids[i : i + self._max_device_buffer_count]
                batch_block_hashes = block_hashes[i : i + self._max_device_buffer_count]
                self._async_manager.submit_save_operation(
                    request.request_id, batch_block_ids, batch_block_hashes
                )

    defstart_load_kv(self, forward_context: "ForwardContext", **kwargs) -> None:
        metadata = self._get_connector_metadata()
        if not isinstance(metadata, HF3FSConnectorMetadata):
            logger.error("Invalid metadata type for loading")
            return

        for request in metadata.requests:
            if request.load_block_op is None:
                continue

            load_op = request.load_block_op
            block_ids = request.block_ids[: load_op.num_blocks_to_load]
            block_hashes = self._generate_block_hashes(
                request.token_ids, load_op.num_computed_blocks, len(block_ids)
            )

            for i in range(0, len(block_ids), self._max_device_buffer_count):
                batch_block_ids = block_ids[i : i + self._max_device_buffer_count]
                batch_block_hashes = block_hashes[i : i + self._max_device_buffer_count]
                self._async_manager.submit_load_operation(
                    request.request_id, batch_block_ids, batch_block_hashes
                )

    defwait_for_layer_load(self, layer_name: str) -> None:
        pass

    defget_finished(
        self, finished_req_ids: set[str]
    ) -> tuple[set[str] | None, set[str] | None]:
        return self._async_manager.get_finished_operations(finished_req_ids)

    defget_kv_connector_stats(self) -> Optional["KVConnectorStats"]:
"""
        Get the KV connector stats collected during the last interval.
        """
        # Clear stats for next iteration
        if (
            hasattr(self, "_async_manager")
            and not self._async_manager.hf3fs_stats.is_empty()
        ):
            return self._async_manager.hf3fs_stats.clone_and_reset()
        return None

    ############################################################
    # Scheduler Side Methods
    ############################################################

    defrequest_finished(
        self,
        request: "Request",
        block_ids: list[int],
    ) -> tuple[bool, dict[str, Any] | None]:
        return True, None

    defget_num_new_matched_tokens(
        self, request: "Request", num_computed_tokens: int
    ) -> tuple[int, bool]:
"""Get number of new tokens that can be loaded from external cache."""
        try:
            state = self._get_or_create_scheduling_state(request.request_id)
            state.request = request
            assert request.prompt_token_ids is not None

            num_tokens_to_check = self._align_to_block_size(
                len(request.prompt_token_ids) - 1
            )

            if num_tokens_to_check <= num_computed_tokens:
                state.load_op = LoadBlockInfo(
                    num_computed_blocks=num_computed_tokens // self._block_size,
                    num_blocks_to_load=0,
                    need_fetch_block_ids=[],
                )
                return 0, False

            token_ids_to_check = request.prompt_token_ids[:num_tokens_to_check]
            block_hashes = self._generate_block_hashes(token_ids_to_check, 0)

            # Check existence
            exists_results = self._metadata_client.batch_key_exists(block_hashes)

            # Count consecutive matches
            matched_blocks = next(
                (i for i, exists in enumerate(exists_results) if not exists),
                len(exists_results),
            )
            matched_tokens = matched_blocks * self._block_size
            new_hit_tokens = max(0, matched_tokens - num_computed_tokens)

            # Store load operation
            state.load_op = LoadBlockInfo(
                num_computed_blocks=num_computed_tokens // self._block_size,
                num_blocks_to_load=new_hit_tokens // self._block_size,
                need_fetch_block_ids=[],
            )

            logger.info(
                (
                    "Token matching for %s: "
                    "%d matched (%d blocks), "
                    "%d new hits, "
                    "prompt len %d"
                ),
                request.request_id,
                matched_tokens,
                matched_blocks,
                new_hit_tokens,
                len(request.prompt_token_ids),
            )
            return new_hit_tokens, new_hit_tokens > 0

        except Exception as e:
            logger.error(
                "Error calculating matches for request %s: %s", request.request_id, e
            )
            return 0, False

    defupdate_state_after_alloc(
        self, request: "Request", blocks: "KVCacheBlocks", num_external_tokens: int
    ) -> None:
"""Update state after block allocation."""
        state = self._get_or_create_scheduling_state(request.request_id)
        state.request = request

        if num_external_tokens <= 0 or not state.needs_loading():
            return

        # Validate block allocation
        assert state.load_op is not None
        expected_blocks = state.load_op.num_blocks_to_load
        actual_blocks = num_external_tokens // self._block_size
        assert actual_blocks == expected_blocks, (
            f"Block count mismatch for {request.request_id}: "
            f"expected {expected_blocks}, got {actual_blocks}"
        )

        # Update load operation with allocated block IDs
        if actual_blocks > 0:
            local_block_ids = blocks.get_unhashed_block_ids()
            state.load_op.need_fetch_block_ids.extend(local_block_ids)
            state.phase = "WAITING_TO_LOAD"

    defbuild_connector_meta(
        self, scheduler_output: SchedulerOutput
    ) -> KVConnectorMetadata:
"""Build connector metadata for scheduling step."""
        metadata = HF3FSConnectorMetadata()

        for request_id in scheduler_output.finished_req_ids:
            self._scheduling_states.pop(request_id, None)

        # Process requests by phase
        self._process_waiting_to_load_requests(metadata)
        self._process_new_requests(scheduler_output, metadata)
        self._process_cached_requests(scheduler_output, metadata)

        return metadata

    def_process_waiting_to_load_requests(
        self, metadata: HF3FSConnectorMetadata
    ) -> None:
"""Process requests waiting to load."""
        for state in list(self._scheduling_states.values()):
            if not state.is_ready_to_load():
                continue
            assert state.load_op is not None
            assert (
                state.request is not None and state.request.prompt_token_ids is not None
            )
            # Create load request metadata
            num_cached_blocks = (
                state.load_op.num_computed_blocks + state.load_op.num_blocks_to_load
            )
            num_tokens_to_compute = num_cached_blocks * self._block_size

            # Initialize token_ids and allocated_block_ids for loading
            state.token_ids = state.request.prompt_token_ids[
                :num_tokens_to_compute
            ].copy()
            state.allocated_block_ids = state.load_op.need_fetch_block_ids.copy()

            request_metadata = HF3FSRequestMetadata.from_scheduling_state(
                state, self._block_size, state.load_op, num_cached_blocks
            )

            if request_metadata:
                metadata.add_request(request_metadata)
                state.phase = "ACTIVE"

    def_process_new_requests(
        self, scheduler_output: SchedulerOutput, metadata: HF3FSConnectorMetadata
    ) -> None:
"""Process new requests."""
        for request in scheduler_output.scheduled_new_reqs:
            state = self._get_or_create_scheduling_state(request.req_id)

            # Calculate tokens to compute
            num_tokens_to_compute = (
                request.num_computed_tokens
                + scheduler_output.num_scheduled_tokens[request.req_id]
            )
            self._initialize_state_from_new_request(
                state, request, num_tokens_to_compute
            )

            # Create save metadata (skip cached blocks if any)
            num_cached_blocks = None
            if state.load_op:
                num_cached_blocks = (
                    state.load_op.num_computed_blocks + state.load_op.num_blocks_to_load
                )

            request_metadata = HF3FSRequestMetadata.from_scheduling_state(
                state, self._block_size, None, num_cached_blocks
            )

            if request_metadata:
                metadata.add_request(request_metadata)
                state.phase = "ACTIVE"

    def_process_cached_requests(
        self, scheduler_output: SchedulerOutput, metadata: HF3FSConnectorMetadata
    ) -> None:
"""Process cached requests."""
        cached_reqs = scheduler_output.scheduled_cached_reqs
        for i, request_id in enumerate(cached_reqs.req_ids):
            state = self._get_or_create_scheduling_state(request_id)
            assert state.request is not None

            # Update with new tokens and blocks
            num_new_tokens = scheduler_output.num_scheduled_tokens[request_id]
            num_current_tokens = len(state.token_ids)
            new_token_ids = state.request.all_token_ids[
                num_current_tokens : num_current_tokens + num_new_tokens
            ]
            new_block_ids = cached_reqs.new_block_ids[i]

            state.update_tokens_and_blocks(new_token_ids, new_block_ids)

            # Create save metadata
            request_metadata = HF3FSRequestMetadata.from_scheduling_state(
                state, self._block_size, None
            )

            if request_metadata:
                metadata.add_request(request_metadata)

    @classmethod
    defbuild_kv_connector_stats(
        cls, data: dict[str, Any] | None = None
    ) -> Optional["KVConnectorStats"]:
"""
        KVConnectorStats resolution method. This method allows dynamically
        registered connectors to return their own KVConnectorStats object,
        which can implement custom aggregation logic on the data dict.
        """
        return (
            HF3FSKVConnectorStats(data=data)
            if data is not None
            else HF3FSKVConnectorStats()
        )

    @classmethod
    defbuild_prom_metrics(
        cls,
        vllm_config: VllmConfig,
        metric_types: dict[type[PromMetric], type[PromMetricT]],
        labelnames: list[str],
        per_engine_labelvalues: dict[int, list[object]],
    ) -> KVConnectorPromMetrics:
        return HF3FSPromMetrics(
            vllm_config, metric_types, labelnames, per_engine_labelvalues
        )

    defclose(self) -> None:
        try:
            if hasattr(self, "_async_manager"):
                self._async_manager.shutdown()

            if hasattr(self, "_clients"):
                for client in self._clients:
                    client.close()
                logger.info("HF3FS clients closed")
        except Exception as e:
            logger.error("Connector shutdown error: %s", e)

    ############################################################
    # Utility Methods
    ############################################################

    def_get_or_create_scheduling_state(
        self, request_id: str
    ) -> RequestSchedulingState:
"""Get existing or create new scheduling state."""
        if request_id not in self._scheduling_states:
            self._scheduling_states[request_id] = RequestSchedulingState(
                request_id=request_id
            )
        return self._scheduling_states[request_id]

    def_initialize_state_from_new_request(
        self, state: RequestSchedulingState, request, num_tokens_to_compute: int
    ) -> None:
"""Initialize state from new request data."""
        # Handle different block_ids formats in vLLM 0.9.0+
        if isinstance(request.block_ids[0], list):
            unfolded_block_ids = request.block_ids[0].copy()
        else:
            unfolded_block_ids = request.block_ids.copy()

        state.token_ids = request.prompt_token_ids[:num_tokens_to_compute].copy()
        state.allocated_block_ids = unfolded_block_ids
        state.num_saved_blocks = 0

    def_generate_block_hashes(
        self,
        token_ids: list[int],
        start_block_id: int,
        max_blocks_count: int | None = None,
    ) -> list[str]:
"""Generate block hashes for token sequence."""
        block_hashes = []
        previous_hash = ""

        for start_idx in range(0, len(token_ids), self._block_size):
            if start_idx + self._block_size > len(token_ids):
                break

            end_idx = start_idx + self._block_size
            block_hash = self._compute_prefix_hash(
                token_ids[start_idx:end_idx], previous_hash
            )

            block_index = start_idx // self._block_size
            if block_index >= start_block_id:
                block_hashes.append(block_hash)

            if max_blocks_count and len(block_hashes) >= max_blocks_count:
                break
            previous_hash = block_hash

        return block_hashes

    def_gather_or_scatter_kv_caches(
        self, block_ids: list[int], block_buffers, operation: str
    ):
        for buffer_tensor, block_id in zip(block_buffers, block_ids):
            start_idx = block_id * self._local_block_size
            token_indices = list(range(start_idx, start_idx + self._local_block_size))
            if operation == "gather":
                gather_scatter_helper.gather_kv_caches(
                    self._kvcache_ptrs,
                    self._local_total_tokens,
                    buffer_tensor,
                    token_indices,
                    is_mla=self._use_mla,
                )
            else:
                gather_scatter_helper.scatter_kv_caches(
                    self._kvcache_ptrs,
                    self._local_total_tokens,
                    buffer_tensor,
                    token_indices,
                    is_mla=self._use_mla,
                )

    def_compute_prefix_hash(
        self, token_ids: list[int], previous_hash: str = ""
    ) -> str:
"""Compute prefix hash for token block."""
        combined_string = f"{previous_hash}_{token_ids}"
        return hashlib.md5(combined_string.encode()).hexdigest()

    def_align_to_block_size(self, num_tokens: int) -> int:
"""Align token count to block size."""
        return (num_tokens // self._block_size) * self._block_size
```