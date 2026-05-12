---
title: common - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/common/
source: sitemap
fetched_at: 2026-05-07T21:18:19.898229705-03:00
rendered_js: false
word_count: 157
summary: This document provides the API reference for HF3FS connector utilities in vLLM, including structures for request scheduling state, atomic counters, and metadata management for KV block transfers.
tags:
    - vllm
    - kv-transfer
    - hf3fs
    - distributed-computing
    - metadata-management
    - request-scheduling
category: reference
---

## AtomicCounter [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.AtomicCounter "Permanent link")

Thread-safe atomic counter for round-robin operations.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/common.py`

```
classAtomicCounter:
"""Thread-safe atomic counter for round-robin operations."""

    def__init__(self, n: int):
        assert n > 0, "Counter size must be positive"
        self._n = n
        self._value = 0
        self._lock = threading.Lock()

    defnext(self) -> int:
"""Get next value in round-robin fashion."""
        with self._lock:
            current = self._value
            self._value = (current + 1) % self._n
            return current
```

### next [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.AtomicCounter.next "Permanent link")

Get next value in round-robin fashion.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/common.py`

```
defnext(self) -> int:
"""Get next value in round-robin fashion."""
    with self._lock:
        current = self._value
        self._value = (current + 1) % self._n
        return current
```

Bases: `KVConnectorMetadata`

Container for HF3FS connector metadata.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/common.py`

```
classHF3FSConnectorMetadata(KVConnectorMetadata):
"""Container for HF3FS connector metadata."""

    def__init__(self):
        self.requests: list[HF3FSRequestMetadata] = []

    defadd_request(self, request_metadata: HF3FSRequestMetadata) -> None:
"""Add request to metadata."""
        self.requests.append(request_metadata)
```

### add\_request [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.HF3FSConnectorMetadata.add_request "Permanent link")

```
add_request(request_metadata: HF3FSRequestMetadata) -> None
```

Add request to metadata.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/common.py`

```
defadd_request(self, request_metadata: HF3FSRequestMetadata) -> None:
"""Add request to metadata."""
    self.requests.append(request_metadata)
```

Metadata for a single request in HF3FS connector.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/common.py`

```
@dataclass
classHF3FSRequestMetadata:
"""Metadata for a single request in HF3FS connector."""

    request_id: str
    token_ids: list[int]
    block_ids: list[int]
    load_block_op: LoadBlockInfo | None = None
    save_block_op: SaveBlockInfo | None = None

    @staticmethod
    deffrom_scheduling_state(
        state: "RequestSchedulingState",
        block_size: int,
        load_op: LoadBlockInfo | None = None,
        skip_leading_blocks: int | None = None,
    ) -> Optional["HF3FSRequestMetadata"]:
"""Create request metadata from scheduling state."""
        token_count = len(state.token_ids)
        total_blocks = token_count // block_size

        skip_blocks = (
            state.num_saved_blocks
            if skip_leading_blocks is None
            else skip_leading_blocks
        )

        new_blocks_to_save = total_blocks - state.num_saved_blocks
        if new_blocks_to_save <= 0 and load_op is None:
            return None

        state.num_saved_blocks = total_blocks
        return HF3FSRequestMetadata(
            request_id=state.request_id,
            token_ids=state.token_ids,
            block_ids=state.allocated_block_ids,
            load_block_op=load_op,
            save_block_op=SaveBlockInfo(skip_leading_blocks=skip_blocks),
        )
```

### from\_scheduling\_state `staticmethod` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.HF3FSRequestMetadata.from_scheduling_state "Permanent link")

```
from_scheduling_state(
    state: RequestSchedulingState,
    block_size: int,
    load_op: LoadBlockInfo | None = None,
    skip_leading_blocks: int | None = None,
) -> Optional[HF3FSRequestMetadata]
```

Create request metadata from scheduling state.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/common.py`

```
@staticmethod
deffrom_scheduling_state(
    state: "RequestSchedulingState",
    block_size: int,
    load_op: LoadBlockInfo | None = None,
    skip_leading_blocks: int | None = None,
) -> Optional["HF3FSRequestMetadata"]:
"""Create request metadata from scheduling state."""
    token_count = len(state.token_ids)
    total_blocks = token_count // block_size

    skip_blocks = (
        state.num_saved_blocks
        if skip_leading_blocks is None
        else skip_leading_blocks
    )

    new_blocks_to_save = total_blocks - state.num_saved_blocks
    if new_blocks_to_save <= 0 and load_op is None:
        return None

    state.num_saved_blocks = total_blocks
    return HF3FSRequestMetadata(
        request_id=state.request_id,
        token_ids=state.token_ids,
        block_ids=state.allocated_block_ids,
        load_block_op=load_op,
        save_block_op=SaveBlockInfo(skip_leading_blocks=skip_blocks),
    )
```

## LoadBlockInfo `dataclass` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.LoadBlockInfo "Permanent link")

Operation for loading blocks from external storage.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/common.py`

```
@dataclass
classLoadBlockInfo:
"""Operation for loading blocks from external storage."""

    num_computed_blocks: int
    num_blocks_to_load: int
    need_fetch_block_ids: list[int]
```

## RequestSchedulingState `dataclass` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.RequestSchedulingState "Permanent link")

Unified request scheduling state management.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/common.py`

```
@dataclass
classRequestSchedulingState:
"""Unified request scheduling state management."""

    request_id: str
    request: Request | None = None

    # Token and block tracking
    token_ids: list[int] = field(default_factory=list)
    allocated_block_ids: list[int] = field(default_factory=list)
    num_saved_blocks: int = 0

    # Load operation info
    load_op: LoadBlockInfo | None = None

    # Scheduling phase
    phase: str = "NEW"  # NEW -> WAITING_TO_LOAD -> ACTIVE -> FINISHED

    defneeds_loading(self) -> bool:
"""Check if request needs loading."""
        return self.load_op is not None and self.load_op.num_blocks_to_load > 0

    defis_ready_to_load(self) -> bool:
"""Check if request is ready for loading."""
        return self.phase == "WAITING_TO_LOAD" and self.needs_loading()

    defupdate_tokens_and_blocks(self, new_token_ids: list[int], new_block_ids) -> None:
"""Update with new tokens and blocks."""
        if new_token_ids:
            self.token_ids.extend(new_token_ids)

        if new_block_ids is not None:
            normalized_block_ids = self._normalize_block_ids(new_block_ids)
            self.allocated_block_ids.extend(normalized_block_ids)

    def_normalize_block_ids(self, block_ids) -> list[int]:
"""Normalize block_ids to list format."""
        if not block_ids:
            return []
        if isinstance(block_ids, tuple):
            return block_ids[0] if block_ids else []
        if isinstance(block_ids, list):
            return block_ids
        return []
```

### \_normalize\_block\_ids [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.RequestSchedulingState._normalize_block_ids "Permanent link")

```
_normalize_block_ids(block_ids) -> list[int]
```

Normalize block\_ids to list format.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/common.py`

```
def_normalize_block_ids(self, block_ids) -> list[int]:
"""Normalize block_ids to list format."""
    if not block_ids:
        return []
    if isinstance(block_ids, tuple):
        return block_ids[0] if block_ids else []
    if isinstance(block_ids, list):
        return block_ids
    return []
```

### is\_ready\_to\_load [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.RequestSchedulingState.is_ready_to_load "Permanent link")

```
is_ready_to_load() -> bool
```

Check if request is ready for loading.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/common.py`

```
defis_ready_to_load(self) -> bool:
"""Check if request is ready for loading."""
    return self.phase == "WAITING_TO_LOAD" and self.needs_loading()
```

### needs\_loading [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.RequestSchedulingState.needs_loading "Permanent link")

Check if request needs loading.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/common.py`

```
defneeds_loading(self) -> bool:
"""Check if request needs loading."""
    return self.load_op is not None and self.load_op.num_blocks_to_load > 0
```

### update\_tokens\_and\_blocks [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.RequestSchedulingState.update_tokens_and_blocks "Permanent link")

```
update_tokens_and_blocks(
    new_token_ids: list[int], new_block_ids
) -> None
```

Update with new tokens and blocks.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/common.py`

```
defupdate_tokens_and_blocks(self, new_token_ids: list[int], new_block_ids) -> None:
"""Update with new tokens and blocks."""
    if new_token_ids:
        self.token_ids.extend(new_token_ids)

    if new_block_ids is not None:
        normalized_block_ids = self._normalize_block_ids(new_block_ids)
        self.allocated_block_ids.extend(normalized_block_ids)
```

## SaveBlockInfo `dataclass` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.SaveBlockInfo "Permanent link")

Operation for saving blocks to external storage.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/common.py`

```
@dataclass
classSaveBlockInfo:
"""Operation for saving blocks to external storage."""

    skip_leading_blocks: int
```