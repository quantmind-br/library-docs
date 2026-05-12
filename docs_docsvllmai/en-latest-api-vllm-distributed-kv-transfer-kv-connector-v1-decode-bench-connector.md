---
title: decode_bench_connector - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector/
source: sitemap
fetched_at: 2026-05-07T21:18:11.33917403-03:00
rendered_js: false
word_count: 459
summary: The DecodeBenchConnector is a benchmarking tool that simulates prefill-decode disaggregated workloads by populating the KV cache with dummy values to test decoder performance under varying sequence lengths.
tags:
    - vllm
    - benchmarking
    - kv-cache
    - performance-testing
    - disaggregated-serving
category: configuration
---

DecodeBenchConnector: A KV Connector for decode instance performance testing.

This connector emulates a prefill-decode disaggregated setting by filling the KV cache with dummy values, allowing measurement of decoder performance under larger input sequence lengths (ISL) in resource-limited environments.

Usage

To use this connector for benchmarking, configure it in the kv\_transfer\_config:

Example: vllm serve --kv-transfer-config '{ "kv\_connector": "DecodeBenchConnector", "kv\_role": "kv\_both", "kv\_connector\_extra\_config": { "fill\_mean": 0.015, "fill\_std": 0.0 } }'

Then run your benchmark with desired input/output lengths: vllm bench serve --base-url http://127.0.0.1:8000 --model \\ --dataset-name random --random-input-len 40000 \\ --random-output-len 100 --max-concurrency 10

Configuration options (via kv\_connector\_extra\_config): - fill\_mean (float): Mean value for random normal fill (default: 0.015) - fill\_std (float): Standard deviation for random fill (default: 0.0) Set to 0 for constant values, &gt;0 for random sampling

## DecodeBenchConnector [¶](#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnector "Permanent link")

Bases: `KVConnectorBase_V1`, `SupportsHMA`

A KV Connector for decode instance performance testing.

This connector fills the KV cache with dummy (non-zero) values to emulate a prefill-decode disaggregated setting, enabling performance testing of the decoder with larger input sequence lengths.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`

```
classDecodeBenchConnector(KVConnectorBase_V1, SupportsHMA):
"""
    A KV Connector for decode instance performance testing.

    This connector fills the KV cache with dummy (non-zero) values to
    emulate a prefill-decode disaggregated setting, enabling performance
    testing of the decoder with larger input sequence lengths.
    """

    def__init__(
        self,
        vllm_config: "VllmConfig",
        role: KVConnectorRole,
        kv_cache_config: "KVCacheConfig | None" = None,
    ):
        super().__init__(vllm_config, role, kv_cache_config)

        self.connector_scheduler: DecodeBenchConnectorScheduler | None = None
        self.connector_worker: DecodeBenchConnectorWorker | None = None

        if role == KVConnectorRole.SCHEDULER:
            self.connector_scheduler = DecodeBenchConnectorScheduler(vllm_config)
        elif role == KVConnectorRole.WORKER:
            self.connector_worker = DecodeBenchConnectorWorker(vllm_config)

    # ==============================
    # Worker-side methods
    # ==============================

    defregister_kv_caches(self, kv_caches: dict[str, torch.Tensor]):
        assert self.connector_worker is not None
        self.connector_worker.register_kv_caches(kv_caches)

    defstart_load_kv(self, forward_context: "ForwardContext", **kwargs: Any) -> None:
        assert self.connector_worker is not None
        assert isinstance(self._connector_metadata, DecodeBenchConnectorMetadata)
        self.connector_worker.start_fill_kv(self._connector_metadata)

    defwait_for_layer_load(self, layer_name: str) -> None:
        # All operations are synchronous, so nothing to wait for
        pass

    defsave_kv_layer(
        self,
        layer_name: str,
        kv_layer: torch.Tensor,
        attn_metadata: AttentionMetadata,
        **kwargs: Any,
    ) -> None:
        # This connector doesn't save KV cache (benchmarking only)
        pass

    defwait_for_save(self):
        # This connector doesn't save KV cache (benchmarking only)
        pass

    # ==============================
    # Scheduler-side methods
    # ==============================

    defget_num_new_matched_tokens(
        self,
        request: "Request",
        num_computed_tokens: int,
    ) -> tuple[int | None, bool]:
        assert self.connector_scheduler is not None
        return self.connector_scheduler.get_num_new_matched_tokens(
            request, num_computed_tokens
        )

    defupdate_state_after_alloc(
        self, request: "Request", blocks: "KVCacheBlocks", num_external_tokens: int
    ):
        assert self.connector_scheduler is not None
        return self.connector_scheduler.update_state_after_alloc(
            request, blocks, num_external_tokens
        )

    defbuild_connector_meta(
        self, scheduler_output: "SchedulerOutput"
    ) -> KVConnectorMetadata:
        assert self.connector_scheduler is not None
        return self.connector_scheduler.build_connector_meta(scheduler_output)

    defrequest_finished(
        self,
        request: "Request",
        block_ids: list[int],
    ) -> tuple[bool, dict[str, Any] | None]:
        assert self.connector_scheduler is not None
        self.connector_scheduler.request_finished(request)
        return False, None

    defrequest_finished_all_groups(
        self,
        request: "Request",
        block_ids: tuple[list[int], ...],
    ) -> tuple[bool, dict[str, Any] | None]:
        # HMA-enabled path: same cleanup as the single-group variant since
        # this connector owns no external state per block.
        assert self.connector_scheduler is not None
        self.connector_scheduler.request_finished(request)
        return False, None
```

Bases: `KVConnectorMetadata`

Metadata for DecodeBenchConnector.

Contains information about which requests need their KV cache filled with dummy values for benchmarking purposes.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`

```
@dataclass
classDecodeBenchConnectorMetadata(KVConnectorMetadata):
"""Metadata for DecodeBenchConnector.

    Contains information about which requests need their KV cache filled
    with dummy values for benchmarking purposes.
    """

    # request_id -> (block_ids_per_group, num_tokens_to_fill)
    # block_ids_per_group is a tuple of lists, one per KV cache group
    # For standard attention: single group, e.g., ([1, 2, 3],)
    # For MLA: multiple groups, e.g., ([1, 2], [1, 2])
    reqs_to_fill: dict[str, tuple[tuple[list[int], ...], int]]
```

## DecodeBenchConnectorScheduler [¶](#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorScheduler "Permanent link")

Scheduler-side implementation for DecodeBenchConnector.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`

```
classDecodeBenchConnectorScheduler:
"""Scheduler-side implementation for DecodeBenchConnector."""

    def__init__(self, vllm_config: "VllmConfig"):
        self.vllm_config = vllm_config
        self.block_size = vllm_config.cache_config.block_size

        # Track which requests have already been filled
        self._filled_requests: set[str] = set()

        # Track pending fills for the current scheduler step
        # request_id -> (block_ids_per_group, num_tokens_to_fill)
        # Note: _pending_fills doesn't need explicit cleanup - it's cleared
        # after build_connector_meta() is called in the same scheduler step
        self._pending_fills: dict[str, tuple[tuple[list[int], ...], int]] = {}

    defget_num_new_matched_tokens(
        self,
        request: "Request",
        num_computed_tokens: int,
    ) -> tuple[int, bool]:
"""
        For new requests, return the number of tokens that should be filled
        with dummy KV cache values.

        Returns:
            (num_tokens_to_fill, is_async)
            - num_tokens_to_fill: number of uncomputed tokens minus 1
                (we fill everything except the last token for decode)
            - is_async: False (synchronous filling)
        """
        req_id = request.request_id

        # Only fill once per request on first scheduling
        if req_id in self._filled_requests:
            return 0, False

        # Calculate how many tokens we need to fill
        # Fill all uncomputed tokens except the last one (which will be decoded)
        # This simulates having processed a long prefill
        num_uncomputed_tokens = request.num_tokens - num_computed_tokens
        num_tokens_to_fill = max(0, num_uncomputed_tokens - 1)

        if num_tokens_to_fill == 0:
            return 0, False

        # Return False for synchronous operation - the fill is fast enough
        # that async overhead isn't worth it
        return num_tokens_to_fill, False

    defupdate_state_after_alloc(
        self, request: "Request", blocks: "KVCacheBlocks", num_external_tokens: int
    ):
"""
        Called after blocks are allocated. Store the block IDs so we can
        fill them with dummy values.

        Supports both standard attention (single KV cache group) and MLA
        (multiple KV cache groups).
        """
        req_id = request.request_id

        if num_external_tokens == 0:
            return

        # Get the block IDs that were allocated
        # block_groups is a tuple of lists, one per KV cache group
        # For standard attention: 1 group
        # For MLA: multiple groups (one per attention type)
        block_groups = blocks.get_block_ids()

        # Calculate how many blocks we need to fill
        # num_external_tokens are the tokens we said we'd provide
        num_blocks_to_fill = cdiv(num_external_tokens, self.block_size)

        # Extract the first num_blocks_to_fill blocks from each group
        # All groups should have the same block IDs for the same request
        block_ids_per_group = tuple(
            group_blocks[:num_blocks_to_fill] for group_blocks in block_groups
        )

        # Store the blocks to fill for all group. _pending_fills doesn't need cleanup
        # as it's cleared after build_connector_meta
        self._pending_fills[req_id] = (
            block_ids_per_group,
            num_external_tokens,
        )
        self._filled_requests.add(req_id)

        logger.debug(
            "DecodeBenchConnector: Allocated %d blocks across %d KV cache groups "
            "for request %s",
            num_blocks_to_fill,
            len(block_groups),
            req_id,
        )

    defbuild_connector_meta(
        self, scheduler_output: "SchedulerOutput"
    ) -> KVConnectorMetadata:
"""
        Build metadata containing information about which blocks to fill
        with dummy KV values.
        """
        meta = DecodeBenchConnectorMetadata(reqs_to_fill=self._pending_fills.copy())

        # Clear pending fills after building metadata
        self._pending_fills.clear()

        return meta

    defrequest_finished(self, request: "Request"):
"""
        Called when a request has finished. Clean up any state.
        """
        self._filled_requests.discard(request.request_id)
```

### build\_connector\_meta [¶](#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorScheduler.build_connector_meta "Permanent link")

Build metadata containing information about which blocks to fill with dummy KV values.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`

```
defbuild_connector_meta(
    self, scheduler_output: "SchedulerOutput"
) -> KVConnectorMetadata:
"""
    Build metadata containing information about which blocks to fill
    with dummy KV values.
    """
    meta = DecodeBenchConnectorMetadata(reqs_to_fill=self._pending_fills.copy())

    # Clear pending fills after building metadata
    self._pending_fills.clear()

    return meta
```

### get\_num\_new\_matched\_tokens [¶](#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorScheduler.get_num_new_matched_tokens "Permanent link")

For new requests, return the number of tokens that should be filled with dummy KV cache values.

Returns:

Type Description `int`

(num\_tokens\_to\_fill, is\_async)

`bool`

- num\_tokens\_to\_fill: number of uncomputed tokens minus 1 (we fill everything except the last token for decode)

`tuple[int, bool]`

- is\_async: False (synchronous filling)

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`

```
defget_num_new_matched_tokens(
    self,
    request: "Request",
    num_computed_tokens: int,
) -> tuple[int, bool]:
"""
    For new requests, return the number of tokens that should be filled
    with dummy KV cache values.

    Returns:
        (num_tokens_to_fill, is_async)
        - num_tokens_to_fill: number of uncomputed tokens minus 1
            (we fill everything except the last token for decode)
        - is_async: False (synchronous filling)
    """
    req_id = request.request_id

    # Only fill once per request on first scheduling
    if req_id in self._filled_requests:
        return 0, False

    # Calculate how many tokens we need to fill
    # Fill all uncomputed tokens except the last one (which will be decoded)
    # This simulates having processed a long prefill
    num_uncomputed_tokens = request.num_tokens - num_computed_tokens
    num_tokens_to_fill = max(0, num_uncomputed_tokens - 1)

    if num_tokens_to_fill == 0:
        return 0, False

    # Return False for synchronous operation - the fill is fast enough
    # that async overhead isn't worth it
    return num_tokens_to_fill, False
```

### request\_finished [¶](#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorScheduler.request_finished "Permanent link")

Called when a request has finished. Clean up any state.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`

```
defrequest_finished(self, request: "Request"):
"""
    Called when a request has finished. Clean up any state.
    """
    self._filled_requests.discard(request.request_id)
```

### update\_state\_after\_alloc [¶](#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorScheduler.update_state_after_alloc "Permanent link")

Called after blocks are allocated. Store the block IDs so we can fill them with dummy values.

Supports both standard attention (single KV cache group) and MLA (multiple KV cache groups).

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`

```
defupdate_state_after_alloc(
    self, request: "Request", blocks: "KVCacheBlocks", num_external_tokens: int
):
"""
    Called after blocks are allocated. Store the block IDs so we can
    fill them with dummy values.

    Supports both standard attention (single KV cache group) and MLA
    (multiple KV cache groups).
    """
    req_id = request.request_id

    if num_external_tokens == 0:
        return

    # Get the block IDs that were allocated
    # block_groups is a tuple of lists, one per KV cache group
    # For standard attention: 1 group
    # For MLA: multiple groups (one per attention type)
    block_groups = blocks.get_block_ids()

    # Calculate how many blocks we need to fill
    # num_external_tokens are the tokens we said we'd provide
    num_blocks_to_fill = cdiv(num_external_tokens, self.block_size)

    # Extract the first num_blocks_to_fill blocks from each group
    # All groups should have the same block IDs for the same request
    block_ids_per_group = tuple(
        group_blocks[:num_blocks_to_fill] for group_blocks in block_groups
    )

    # Store the blocks to fill for all group. _pending_fills doesn't need cleanup
    # as it's cleared after build_connector_meta
    self._pending_fills[req_id] = (
        block_ids_per_group,
        num_external_tokens,
    )
    self._filled_requests.add(req_id)

    logger.debug(
        "DecodeBenchConnector: Allocated %d blocks across %d KV cache groups "
        "for request %s",
        num_blocks_to_fill,
        len(block_groups),
        req_id,
    )
```

## DecodeBenchConnectorWorker [¶](#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorWorker "Permanent link")

Worker-side implementation for DecodeBenchConnector.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`

```
classDecodeBenchConnectorWorker:
"""Worker-side implementation for DecodeBenchConnector."""

    def__init__(self, vllm_config: "VllmConfig"):
        self.vllm_config = vllm_config
        self.block_size = vllm_config.cache_config.block_size

        # Get fill parameters from extra config
        kv_transfer_config = vllm_config.kv_transfer_config
        assert kv_transfer_config is not None
        self.fill_mean = kv_transfer_config.get_from_extra_config("fill_mean", 0.015)
        self.fill_std = kv_transfer_config.get_from_extra_config("fill_std", 0.0)

        # Will be populated via register_kv_caches
        self.kv_caches: dict[str, torch.Tensor] | None = None

        # Mapping from KV cache group index to list of layer names in that group
        self.group_to_layers: dict[int, list[str]] | None = None

    defregister_kv_caches(self, kv_caches: dict[str, torch.Tensor]):
"""Store references to the KV cache tensors and build group mapping."""
        self.kv_caches = kv_caches

        # For simplicity, assume all layers belong to group 0 (standard attention)
        # For MLA models with multiple groups, the metadata will handle the mapping
        # We just need to fill the blocks specified in the metadata
        self.group_to_layers = {0: list(kv_caches.keys())}

        logger.debug(
            "DecodeBenchConnector: Registered %d KV cache layers",
            len(kv_caches),
        )

    defstart_fill_kv(self, metadata: DecodeBenchConnectorMetadata):
"""
        Fill the allocated KV cache blocks with dummy (non-zero) values.

        This simulates having a populated KV cache from a prefill phase,
        allowing decode performance testing with larger context sizes.

        Supports both standard attention (single group) and MLA (multiple groups).
        """
        if not metadata.reqs_to_fill:
            return

        assert self.kv_caches is not None, "KV caches must be registered before filling"
        assert self.group_to_layers is not None, "Group mapping must be initialized"

        for req_id, (block_ids_per_group, num_tokens) in metadata.reqs_to_fill.items():
            # Fill blocks for each KV cache group
            for group_idx, block_ids in enumerate(block_ids_per_group):
                self._fill_blocks(group_idx, block_ids, num_tokens)

            logger.debug(
                "DecodeBenchConnector: Filled %d blocks (%d tokens) across %d groups "
                "for request %s",
                len(block_ids_per_group[0]) if block_ids_per_group else 0,
                num_tokens,
                len(block_ids_per_group),
                req_id,
            )

    def_fill_blocks(self, group_idx: int, block_ids: list[int], num_tokens: int):
"""
        Fill specified blocks with dummy non-zero values for a specific KV cache group.

        Args:
            group_idx: The KV cache group index to fill
            block_ids: List of block IDs to fill in this group
            num_tokens: Total number of tokens to fill across these blocks
        """
        if not block_ids:
            return

        assert self.kv_caches is not None
        assert self.group_to_layers is not None

        # Get the layers that belong to this group
        layer_names = self.group_to_layers.get(group_idx, [])

        # Fill only the layers in this group
        for layer_name in layer_names:
            if layer_name not in self.kv_caches:
                logger.warning(
                    "DecodeBenchConnector: Layer %s not found in KV caches", layer_name
                )
                continue

            kv_cache = self.kv_caches[layer_name]

            # Convert block_ids to tensor on device
            block_ids_tensor = torch.tensor(
                block_ids, dtype=torch.long, device=kv_cache.device
            )

            # Filter invalid block IDs
            valid_mask = block_ids_tensor < kv_cache.shape[0]
            valid_block_ids = block_ids_tensor[valid_mask]

            if len(valid_block_ids) == 0:
                continue

            # Create fill values - either constant or random
            block_shape = kv_cache.shape[1:]
            if self.fill_std > 0:
                # Random normal sampling
                fill_values = torch.normal(
                    mean=self.fill_mean,
                    std=self.fill_std,
                    size=(len(valid_block_ids),) + block_shape,
                    dtype=kv_cache.dtype,
                    device=kv_cache.device,
                )
            else:
                # Constant fill value
                fill_values = torch.full(
                    (len(valid_block_ids),) + block_shape,
                    self.fill_mean,
                    dtype=kv_cache.dtype,
                    device=kv_cache.device,
                )

            # Batch fill operation
            kv_cache[valid_block_ids] = fill_values

        logger.debug(
            "DecodeBenchConnector: Filled %d blocks in group %d with %s values "
            "(mean=%.3f, std=%.3f)",
            len(block_ids),
            group_idx,
            "random" if self.fill_std > 0 else "constant",
            self.fill_mean,
            self.fill_std,
        )
```

### \_fill\_blocks [¶](#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorWorker._fill_blocks "Permanent link")

```
_fill_blocks(
    group_idx: int, block_ids: list[int], num_tokens: int
)
```

Fill specified blocks with dummy non-zero values for a specific KV cache group.

Parameters:

Name Type Description Default `group_idx` `int`

The KV cache group index to fill

*required* `block_ids` `list[int]`

List of block IDs to fill in this group

*required* `num_tokens` `int`

Total number of tokens to fill across these blocks

*required*

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`

```
def_fill_blocks(self, group_idx: int, block_ids: list[int], num_tokens: int):
"""
    Fill specified blocks with dummy non-zero values for a specific KV cache group.

    Args:
        group_idx: The KV cache group index to fill
        block_ids: List of block IDs to fill in this group
        num_tokens: Total number of tokens to fill across these blocks
    """
    if not block_ids:
        return

    assert self.kv_caches is not None
    assert self.group_to_layers is not None

    # Get the layers that belong to this group
    layer_names = self.group_to_layers.get(group_idx, [])

    # Fill only the layers in this group
    for layer_name in layer_names:
        if layer_name not in self.kv_caches:
            logger.warning(
                "DecodeBenchConnector: Layer %s not found in KV caches", layer_name
            )
            continue

        kv_cache = self.kv_caches[layer_name]

        # Convert block_ids to tensor on device
        block_ids_tensor = torch.tensor(
            block_ids, dtype=torch.long, device=kv_cache.device
        )

        # Filter invalid block IDs
        valid_mask = block_ids_tensor < kv_cache.shape[0]
        valid_block_ids = block_ids_tensor[valid_mask]

        if len(valid_block_ids) == 0:
            continue

        # Create fill values - either constant or random
        block_shape = kv_cache.shape[1:]
        if self.fill_std > 0:
            # Random normal sampling
            fill_values = torch.normal(
                mean=self.fill_mean,
                std=self.fill_std,
                size=(len(valid_block_ids),) + block_shape,
                dtype=kv_cache.dtype,
                device=kv_cache.device,
            )
        else:
            # Constant fill value
            fill_values = torch.full(
                (len(valid_block_ids),) + block_shape,
                self.fill_mean,
                dtype=kv_cache.dtype,
                device=kv_cache.device,
            )

        # Batch fill operation
        kv_cache[valid_block_ids] = fill_values

    logger.debug(
        "DecodeBenchConnector: Filled %d blocks in group %d with %s values "
        "(mean=%.3f, std=%.3f)",
        len(block_ids),
        group_idx,
        "random" if self.fill_std > 0 else "constant",
        self.fill_mean,
        self.fill_std,
    )
```

### register\_kv\_caches [¶](#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorWorker.register_kv_caches "Permanent link")

Store references to the KV cache tensors and build group mapping.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`

```
defregister_kv_caches(self, kv_caches: dict[str, torch.Tensor]):
"""Store references to the KV cache tensors and build group mapping."""
    self.kv_caches = kv_caches

    # For simplicity, assume all layers belong to group 0 (standard attention)
    # For MLA models with multiple groups, the metadata will handle the mapping
    # We just need to fill the blocks specified in the metadata
    self.group_to_layers = {0: list(kv_caches.keys())}

    logger.debug(
        "DecodeBenchConnector: Registered %d KV cache layers",
        len(kv_caches),
    )
```

### start\_fill\_kv [¶](#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorWorker.start_fill_kv "Permanent link")

```
start_fill_kv(metadata: DecodeBenchConnectorMetadata)
```

Fill the allocated KV cache blocks with dummy (non-zero) values.

This simulates having a populated KV cache from a prefill phase, allowing decode performance testing with larger context sizes.

Supports both standard attention (single group) and MLA (multiple groups).

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`

```
defstart_fill_kv(self, metadata: DecodeBenchConnectorMetadata):
"""
    Fill the allocated KV cache blocks with dummy (non-zero) values.

    This simulates having a populated KV cache from a prefill phase,
    allowing decode performance testing with larger context sizes.

    Supports both standard attention (single group) and MLA (multiple groups).
    """
    if not metadata.reqs_to_fill:
        return

    assert self.kv_caches is not None, "KV caches must be registered before filling"
    assert self.group_to_layers is not None, "Group mapping must be initialized"

    for req_id, (block_ids_per_group, num_tokens) in metadata.reqs_to_fill.items():
        # Fill blocks for each KV cache group
        for group_idx, block_ids in enumerate(block_ids_per_group):
            self._fill_blocks(group_idx, block_ids, num_tokens)

        logger.debug(
            "DecodeBenchConnector: Filled %d blocks (%d tokens) across %d groups "
            "for request %s",
            len(block_ids_per_group[0]) if block_ids_per_group else 0,
            num_tokens,
            len(block_ids_per_group),
            req_id,
        )
```