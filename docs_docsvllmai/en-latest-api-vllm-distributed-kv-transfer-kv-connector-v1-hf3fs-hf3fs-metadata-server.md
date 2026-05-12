---
title: hf3fs_metadata_server - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server/
source: sitemap
fetched_at: 2026-05-07T21:18:17.997919928-03:00
rendered_js: false
word_count: 716
summary: This document describes the GlobalMetadataState class, which provides a thread-safe mechanism for managing key-based metadata and page allocation across ranks in a distributed KV transfer system.
tags:
    - metadata-management
    - distributed-computing
    - kv-transfer
    - thread-safe
    - page-allocation
category: api
---

HF3FS Metadata Server with key-based organization.

Manages global metadata state across all ranks and keys.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
classGlobalMetadataState:
"""Manages global metadata state across all ranks and keys."""

    def__init__(self):
        self.global_lock = threading.RLock()
        self.rank_metadata: dict[int, RankFileMetadata] = {}
        self.key_metadata: dict[str, KeyMetadata] = {}

    defclear(self) -> None:
"""Clear all metadata state."""
        with self.global_lock:
            self.rank_metadata.clear()
            self.key_metadata.clear()
            logger.info("Cleared all metadata state")

    definitialize_rank(self, rank: int, num_pages: int) -> None:
"""Initialize a new rank with specified number of pages."""
        with self.global_lock:
            if rank not in self.rank_metadata:
                self.rank_metadata[rank] = RankFileMetadata(
                    rank, num_pages, list(range(num_pages))
                )
                logger.info("Initialized rank %s with %s pages", rank, num_pages)

    defallocate_pages_for_keys(
        self, rank: int, keys: list[tuple[str, str]]
    ) -> dict[str, int]:
"""Allocate one page for each key on the specified rank.

        Args:
            rank: Rank ID to allocate pages on
            keys: List of keys to allocate pages for

        Returns:
            Dictionary mapping key -> allocated page index
        """
        with self.global_lock:
            if rank not in self.rank_metadata:
                raise ValueError(f"Rank {rank} not initialized")

            # Batch allocate pages for all keys
            num_pages_needed = len(keys)
            allocated_pages = self.rank_metadata[rank].allocate_pages(num_pages_needed)

            if len(allocated_pages) < num_pages_needed:
                logger.warning(
                    "Rank %s only allocated %s pages for %s keys",
                    rank,
                    len(allocated_pages),
                    num_pages_needed,
                )

            allocation_results = {}
            for i, (key, prefix_key) in enumerate(keys):
                if key in self.key_metadata:
                    key_meta = self.key_metadata[key]
                    if key_meta.is_complete() and rank in key_meta.rank_to_page:
                        # key is already fully written, reuse the existing page
                        # and release the allocated pages back to the free pool.
                        if i < len(allocated_pages):
                            self.rank_metadata[rank].release_pages([allocated_pages[i]])
                        allocation_results[key] = key_meta.rank_to_page[rank]
                        continue

                if i < len(allocated_pages):
                    allocation_results[key] = allocated_pages[i]
                else:
                    allocation_results[key] = -1  # No pages available

            return allocation_results

    defconfirm_write_for_keys(
        self,
        rank: int,
        key_confirmations: list[tuple[str, int]],
        pages_to_release: list[int] | None = None,
    ) -> None:
"""Confirm write operations for keys and update metadata.

        Args:
            rank: Rank ID that confirmed the writes
            key_confirmations: List of (key, page_index) tuples
            pages_to_release: List of page indices to release back to free pool
        """
        with self.global_lock:
            # Confirm successful writes
            for key, page_index in key_confirmations:
                if key not in self.key_metadata:
                    # Need to determine tp_world_size from rank_metadata
                    tp_world_size = len(self.rank_metadata)
                    self.key_metadata[key] = KeyMetadata(key, {}, tp_world_size)

                # Add confirmed page to key metadata
                self.key_metadata[key].add_rank_page(rank, page_index)

            # Release specified pages back to free pool
            if pages_to_release:
                self.rank_metadata[rank].release_pages(pages_to_release)
                logger.debug(
                    "Released %s pages on rank %s: %s",
                    len(pages_to_release),
                    rank,
                    pages_to_release,
                )

    defbatch_key_exists(self, keys: list[str]) -> list[bool]:
"""Check if keys exist in metadata and all ranks have confirmed writes.

        Args:
            keys: List of keys to check

        Returns:
            List of boolean values indicating key existence and completion
        """
        with self.global_lock:
            results = []
            for key in keys:
                if key not in self.key_metadata:
                    results.append(False)
                else:
                    # Check if all ranks in the TP world have confirmed writes
                    key_meta = self.key_metadata[key]
                    results.append(key_meta.is_complete())
            return results

    defget_key_locations(self, rank: int, keys: list[str]) -> list[int | None]:
"""Get page indices for keys on a specific rank.

        Args:
            rank: Rank ID to query
            keys: List of keys to look up

        Returns:
            List of page indices in the same order as input keys (None if key not found)
        """
        with self.global_lock:
            if rank not in self.rank_metadata:
                raise ValueError(f"Rank {rank} not initialized")

            results = []
            for key in keys:
                if key in self.key_metadata:
                    key_meta = self.key_metadata[key]
                    if key_meta.is_complete():
                        page_index = key_meta.get_rank_page(rank)
                    else:
                        page_index = None

                    results.append(page_index)
                else:
                    results.append(None)

            return results
```

### allocate\_pages\_for\_keys [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState.allocate_pages_for_keys "Permanent link")

Allocate one page for each key on the specified rank.

Parameters:

Name Type Description Default `rank` `int`

Rank ID to allocate pages on

*required* `keys` `list[tuple[str, str]]`

List of keys to allocate pages for

*required*

Returns:

Type Description `dict[str, int]`

Dictionary mapping key -&gt; allocated page index

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
defallocate_pages_for_keys(
    self, rank: int, keys: list[tuple[str, str]]
) -> dict[str, int]:
"""Allocate one page for each key on the specified rank.

    Args:
        rank: Rank ID to allocate pages on
        keys: List of keys to allocate pages for

    Returns:
        Dictionary mapping key -> allocated page index
    """
    with self.global_lock:
        if rank not in self.rank_metadata:
            raise ValueError(f"Rank {rank} not initialized")

        # Batch allocate pages for all keys
        num_pages_needed = len(keys)
        allocated_pages = self.rank_metadata[rank].allocate_pages(num_pages_needed)

        if len(allocated_pages) < num_pages_needed:
            logger.warning(
                "Rank %s only allocated %s pages for %s keys",
                rank,
                len(allocated_pages),
                num_pages_needed,
            )

        allocation_results = {}
        for i, (key, prefix_key) in enumerate(keys):
            if key in self.key_metadata:
                key_meta = self.key_metadata[key]
                if key_meta.is_complete() and rank in key_meta.rank_to_page:
                    # key is already fully written, reuse the existing page
                    # and release the allocated pages back to the free pool.
                    if i < len(allocated_pages):
                        self.rank_metadata[rank].release_pages([allocated_pages[i]])
                    allocation_results[key] = key_meta.rank_to_page[rank]
                    continue

            if i < len(allocated_pages):
                allocation_results[key] = allocated_pages[i]
            else:
                allocation_results[key] = -1  # No pages available

        return allocation_results
```

### batch\_key\_exists [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState.batch_key_exists "Permanent link")

Check if keys exist in metadata and all ranks have confirmed writes.

Parameters:

Name Type Description Default `keys` `list[str]`

List of keys to check

*required*

Returns:

Type Description `list[bool]`

List of boolean values indicating key existence and completion

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
defbatch_key_exists(self, keys: list[str]) -> list[bool]:
"""Check if keys exist in metadata and all ranks have confirmed writes.

    Args:
        keys: List of keys to check

    Returns:
        List of boolean values indicating key existence and completion
    """
    with self.global_lock:
        results = []
        for key in keys:
            if key not in self.key_metadata:
                results.append(False)
            else:
                # Check if all ranks in the TP world have confirmed writes
                key_meta = self.key_metadata[key]
                results.append(key_meta.is_complete())
        return results
```

### clear [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState.clear "Permanent link")

Clear all metadata state.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
defclear(self) -> None:
"""Clear all metadata state."""
    with self.global_lock:
        self.rank_metadata.clear()
        self.key_metadata.clear()
        logger.info("Cleared all metadata state")
```

### confirm\_write\_for\_keys [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState.confirm_write_for_keys "Permanent link")

```
confirm_write_for_keys(
    rank: int,
    key_confirmations: list[tuple[str, int]],
    pages_to_release: list[int] | None = None,
) -> None
```

Confirm write operations for keys and update metadata.

Parameters:

Name Type Description Default `rank` `int`

Rank ID that confirmed the writes

*required* `key_confirmations` `list[tuple[str, int]]`

List of (key, page\_index) tuples

*required* `pages_to_release` `list[int] | None`

List of page indices to release back to free pool

`None`

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
defconfirm_write_for_keys(
    self,
    rank: int,
    key_confirmations: list[tuple[str, int]],
    pages_to_release: list[int] | None = None,
) -> None:
"""Confirm write operations for keys and update metadata.

    Args:
        rank: Rank ID that confirmed the writes
        key_confirmations: List of (key, page_index) tuples
        pages_to_release: List of page indices to release back to free pool
    """
    with self.global_lock:
        # Confirm successful writes
        for key, page_index in key_confirmations:
            if key not in self.key_metadata:
                # Need to determine tp_world_size from rank_metadata
                tp_world_size = len(self.rank_metadata)
                self.key_metadata[key] = KeyMetadata(key, {}, tp_world_size)

            # Add confirmed page to key metadata
            self.key_metadata[key].add_rank_page(rank, page_index)

        # Release specified pages back to free pool
        if pages_to_release:
            self.rank_metadata[rank].release_pages(pages_to_release)
            logger.debug(
                "Released %s pages on rank %s: %s",
                len(pages_to_release),
                rank,
                pages_to_release,
            )
```

### get\_key\_locations [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState.get_key_locations "Permanent link")

Get page indices for keys on a specific rank.

Parameters:

Name Type Description Default `rank` `int`

Rank ID to query

*required* `keys` `list[str]`

List of keys to look up

*required*

Returns:

Type Description `list[int | None]`

List of page indices in the same order as input keys (None if key not found)

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
defget_key_locations(self, rank: int, keys: list[str]) -> list[int | None]:
"""Get page indices for keys on a specific rank.

    Args:
        rank: Rank ID to query
        keys: List of keys to look up

    Returns:
        List of page indices in the same order as input keys (None if key not found)
    """
    with self.global_lock:
        if rank not in self.rank_metadata:
            raise ValueError(f"Rank {rank} not initialized")

        results = []
        for key in keys:
            if key in self.key_metadata:
                key_meta = self.key_metadata[key]
                if key_meta.is_complete():
                    page_index = key_meta.get_rank_page(rank)
                else:
                    page_index = None

                results.append(page_index)
            else:
                results.append(None)

        return results
```

### initialize\_rank [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState.initialize_rank "Permanent link")

```
initialize_rank(rank: int, num_pages: int) -> None
```

Initialize a new rank with specified number of pages.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
definitialize_rank(self, rank: int, num_pages: int) -> None:
"""Initialize a new rank with specified number of pages."""
    with self.global_lock:
        if rank not in self.rank_metadata:
            self.rank_metadata[rank] = RankFileMetadata(
                rank, num_pages, list(range(num_pages))
            )
            logger.info("Initialized rank %s with %s pages", rank, num_pages)
```

Bases: `Hf3fsMetadataInterface`

Global HTTP metadata client for HF3FS.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
classHf3fsGlobalMetadataClient(Hf3fsMetadataInterface):
"""Global HTTP metadata client for HF3FS."""

    def__init__(self, base_url: str = "http://localhost:18000", max_retries: int = 3):
        self.base_url = base_url.rstrip("/")
        self._session = requests.Session()

        retry_strategy = Retry(
            total=max_retries,
            backoff_factor=0.3,
            status_forcelist=[500, 502, 503, 504],
            allowed_methods=["GET", "POST"],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self._session.mount("http://", adapter)

    def_post(self, endpoint: str, json_data: dict) -> dict:
"""Make POST request to metadata server."""
        try:
            url = f"{self.base_url}/{endpoint}"
            headers = {"Content-Type": "application/json"}
            if HAS_ORJSON:
                payload = orjson.dumps(json_data)
            else:
                importjson

                payload = json.dumps(json_data).encode("utf-8")
            response = self._session.post(url, data=payload, headers=headers)
            response.raise_for_status()

            if response.status_code == 204 or not response.content:
                return {}
            if HAS_ORJSON:
                return orjson.loads(response.content)
            else:
                return response.json()
        except requests.exceptions.RequestException as e:
            logger.error("Failed to POST to %s after retries: %s", endpoint, e)
            raise RuntimeError(f"Failed to connect to metadata server: {e}") frome

    definitialize(self, rank: int, num_pages: int = 0, role: str = "worker") -> None:
"""Initialize a rank with specified number of pages."""
        self._post(f"rank/{rank}/initialize", {"num_pages": num_pages, "role": role})

    defallocate_pages_for_keys(
        self, rank: int, keys: list[tuple[str, str]]
    ) -> list[tuple[str, int]]:
"""Allocate pages for keys on the specified rank."""
        response = self._post("keys/batch_allocate", {"rank": rank, "keys": keys})

        # Convert response to expected format
        return response.get("results", {})

    defconfirm_write_for_keys(
        self,
        rank: int,
        key_confirmations: list[tuple[str, int]],
        pages_to_release: list[int] | None = None,
    ) -> None:
"""Confirm write operations for keys and optionally release pages."""
        payload = {
            "rank": rank,
            "confirmations": key_confirmations,
            "pages_to_release": pages_to_release or [],
        }

        self._post("keys/confirm_write", payload)

    defbatch_key_exists(self, keys: list[str]) -> list[bool]:
"""Check if keys exist and are complete across all ranks."""
        response = self._post("keys/batch_exists", {"keys": keys})
        return response.get("exists", [])

    defget_key_locations(self, rank: int, keys: list[str]) -> list[int]:
"""Get page indices for keys on a specific rank."""
        response = self._post("keys/get_locations", {"rank": rank, "keys": keys})
        return response.get("locations", [])
```

### \_post [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsGlobalMetadataClient._post "Permanent link")

Make POST request to metadata server.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
def_post(self, endpoint: str, json_data: dict) -> dict:
"""Make POST request to metadata server."""
    try:
        url = f"{self.base_url}/{endpoint}"
        headers = {"Content-Type": "application/json"}
        if HAS_ORJSON:
            payload = orjson.dumps(json_data)
        else:
            importjson

            payload = json.dumps(json_data).encode("utf-8")
        response = self._session.post(url, data=payload, headers=headers)
        response.raise_for_status()

        if response.status_code == 204 or not response.content:
            return {}
        if HAS_ORJSON:
            return orjson.loads(response.content)
        else:
            return response.json()
    except requests.exceptions.RequestException as e:
        logger.error("Failed to POST to %s after retries: %s", endpoint, e)
        raise RuntimeError(f"Failed to connect to metadata server: {e}") frome
```

### allocate\_pages\_for\_keys [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsGlobalMetadataClient.allocate_pages_for_keys "Permanent link")

Allocate pages for keys on the specified rank.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
defallocate_pages_for_keys(
    self, rank: int, keys: list[tuple[str, str]]
) -> list[tuple[str, int]]:
"""Allocate pages for keys on the specified rank."""
    response = self._post("keys/batch_allocate", {"rank": rank, "keys": keys})

    # Convert response to expected format
    return response.get("results", {})
```

### batch\_key\_exists [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsGlobalMetadataClient.batch_key_exists "Permanent link")

Check if keys exist and are complete across all ranks.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
defbatch_key_exists(self, keys: list[str]) -> list[bool]:
"""Check if keys exist and are complete across all ranks."""
    response = self._post("keys/batch_exists", {"keys": keys})
    return response.get("exists", [])
```

### confirm\_write\_for\_keys [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsGlobalMetadataClient.confirm_write_for_keys "Permanent link")

```
confirm_write_for_keys(
    rank: int,
    key_confirmations: list[tuple[str, int]],
    pages_to_release: list[int] | None = None,
) -> None
```

Confirm write operations for keys and optionally release pages.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
defconfirm_write_for_keys(
    self,
    rank: int,
    key_confirmations: list[tuple[str, int]],
    pages_to_release: list[int] | None = None,
) -> None:
"""Confirm write operations for keys and optionally release pages."""
    payload = {
        "rank": rank,
        "confirmations": key_confirmations,
        "pages_to_release": pages_to_release or [],
    }

    self._post("keys/confirm_write", payload)
```

### get\_key\_locations [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsGlobalMetadataClient.get_key_locations "Permanent link")

Get page indices for keys on a specific rank.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
defget_key_locations(self, rank: int, keys: list[str]) -> list[int]:
"""Get page indices for keys on a specific rank."""
    response = self._post("keys/get_locations", {"rank": rank, "keys": keys})
    return response.get("locations", [])
```

### initialize [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsGlobalMetadataClient.initialize "Permanent link")

```
initialize(
    rank: int, num_pages: int = 0, role: str = "worker"
) -> None
```

Initialize a rank with specified number of pages.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
definitialize(self, rank: int, num_pages: int = 0, role: str = "worker") -> None:
"""Initialize a rank with specified number of pages."""
    self._post(f"rank/{rank}/initialize", {"num_pages": num_pages, "role": role})
```

Bases: `ABC`

Interface for HF3FS metadata operations.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
classHf3fsMetadataInterface(ABC):
"""Interface for HF3FS metadata operations."""

    @abstractmethod
    definitialize(self, rank: int, num_pages: int = 0, role: str = "worker") -> None:
"""Initialize the metadata service with specified number of pages."""
        pass

    @abstractmethod
    defallocate_pages_for_keys(
        self, rank: int, keys: list[tuple[str, str]]
    ) -> list[tuple[str, int]]:
"""Allocate one page for each key on the specified rank."""
        pass

    @abstractmethod
    defconfirm_write_for_keys(
        self,
        rank: int,
        key_confirmations: list[tuple[str, int]],
        pages_to_release: list[int] | None = None,
    ) -> None:
"""Confirm write operations for keys and optionally release pages."""
        pass

    @abstractmethod
    defbatch_key_exists(self, keys: list[str]) -> list[bool]:
"""Check if keys exist and are complete across all ranks."""
        pass

    @abstractmethod
    defget_key_locations(self, rank: int, keys: list[str]) -> list[int]:
"""Get page indices for keys on a specific rank."""
        pass
```

### allocate\_pages\_for\_keys `abstractmethod` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataInterface.allocate_pages_for_keys "Permanent link")

Allocate one page for each key on the specified rank.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
@abstractmethod
defallocate_pages_for_keys(
    self, rank: int, keys: list[tuple[str, str]]
) -> list[tuple[str, int]]:
"""Allocate one page for each key on the specified rank."""
    pass
```

### batch\_key\_exists `abstractmethod` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataInterface.batch_key_exists "Permanent link")

Check if keys exist and are complete across all ranks.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
@abstractmethod
defbatch_key_exists(self, keys: list[str]) -> list[bool]:
"""Check if keys exist and are complete across all ranks."""
    pass
```

### confirm\_write\_for\_keys `abstractmethod` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataInterface.confirm_write_for_keys "Permanent link")

```
confirm_write_for_keys(
    rank: int,
    key_confirmations: list[tuple[str, int]],
    pages_to_release: list[int] | None = None,
) -> None
```

Confirm write operations for keys and optionally release pages.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
@abstractmethod
defconfirm_write_for_keys(
    self,
    rank: int,
    key_confirmations: list[tuple[str, int]],
    pages_to_release: list[int] | None = None,
) -> None:
"""Confirm write operations for keys and optionally release pages."""
    pass
```

### get\_key\_locations `abstractmethod` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataInterface.get_key_locations "Permanent link")

Get page indices for keys on a specific rank.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
@abstractmethod
defget_key_locations(self, rank: int, keys: list[str]) -> list[int]:
"""Get page indices for keys on a specific rank."""
    pass
```

### initialize `abstractmethod` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataInterface.initialize "Permanent link")

```
initialize(
    rank: int, num_pages: int = 0, role: str = "worker"
) -> None
```

Initialize the metadata service with specified number of pages.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
@abstractmethod
definitialize(self, rank: int, num_pages: int = 0, role: str = "worker") -> None:
"""Initialize the metadata service with specified number of pages."""
    pass
```

HF3FS Metadata Server with improved key-based organization.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
classHf3fsMetadataServer:
"""HF3FS Metadata Server with improved key-based organization."""

    def__init__(self, persistence_path: str | None = None, save_interval: int = 60):
        self.state = GlobalMetadataState()
        if HAS_ORJSON:
            self.app = FastAPI(default_response_class=ORJSONResponse)
        else:
            self.app = FastAPI()
        self._setup_routes()

    async def_read_json(self, request: Request) -> dict:
"""Parse request JSON using orjson if available."""
        body = await request.body()
        return orjson.loads(body)

    def_json_response(self, content: dict):
"""Return ORJSONResponse when available to bypass jsonable_encoder."""
        if HAS_ORJSON:
            return ORJSONResponse(content)
        else:
            return content

    def_setup_routes(self):
"""Setup FastAPI routes for new API design."""
        self.app.post("/rank/{rank}/initialize")(self.initialize_rank)
        self.app.post("/keys/batch_allocate")(self.batch_allocate_pages_for_keys)
        self.app.post("/keys/confirm_write")(self.confirm_write_for_keys)
        self.app.post("/keys/batch_exists")(self.batch_key_exists)
        self.app.post("/keys/get_locations")(self.get_key_locations)
        self.app.post("/clear")(self.clear)

    async definitialize_rank(self, rank: int, request: Request):
"""Initialize a rank with specified number of pages."""
        data = await self._read_json(request)
        role = data.get("role", "worker")
        num_pages = data.get("num_pages", 0)

        if role == "scheduler":
            return self._json_response(
                {"message": "Scheduler role does not require initialization"}
            )

        if role == "worker" and num_pages > 0:
            self.state.initialize_rank(rank, num_pages)
            return self._json_response(
                {"message": f"Rank {rank} initialized with {num_pages} pages"}
            )
        else:
            raise HTTPException(
                status_code=400, detail="Invalid initialization parameters"
            )

    async defbatch_allocate_pages_for_keys(self, request: Request):
"""Allocate one page for each key on a specific rank."""
        data = await self._read_json(request)
        rank = data.get("rank")
        keys = data.get("keys", [])

        # Validate input format
        if rank is None or not isinstance(keys, list):
            raise HTTPException(
                status_code=400, detail="Invalid request format: need 'rank' and 'keys'"
            )

        try:
            # Perform allocation
            results = self.state.allocate_pages_for_keys(rank, keys)

            # Convert results to response format
            response = {"rank": rank, "results": list(results.items())}
            return self._json_response(response)
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Allocation failed: {str(e)}"
            ) frome

    async defconfirm_write_for_keys(self, request: Request):
"""Confirm write operations for keys."""
        data = await self._read_json(request)
        rank = data.get("rank")
        confirmations = data.get("confirmations", [])
        pages_to_release = data.get("pages_to_release", [])

        # Validate input format
        if rank is None or not isinstance(confirmations, list):
            raise HTTPException(
                status_code=400,
                detail="Invalid request format: need 'rank' and 'confirmations'",
            )

        try:
            self.state.confirm_write_for_keys(rank, confirmations, pages_to_release)

            return Response(status_code=204)

        except Exception as e:
            logger.error("Confirm write for keys failed: %s", e)
            raise HTTPException(
                status_code=500, detail=f"Confirmation failed: {str(e)}"
            ) frome

    async defbatch_key_exists(self, request: Request):
"""Check if multiple keys exist in metadata."""
        data = await self._read_json(request)
        keys = data.get("keys", [])

        if not isinstance(keys, list):
            raise HTTPException(status_code=400, detail="Invalid keys format")

        try:
            exists_results = self.state.batch_key_exists(keys)
            return self._json_response({"exists": exists_results})
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Key existence check failed: {str(e)}"
            ) frome

    async defget_key_locations(self, request: Request):
"""Get page indices for keys on a specific rank."""
        data = await self._read_json(request)
        rank = data.get("rank")
        keys = data.get("keys", [])

        # Validate input format
        if rank is None or not isinstance(keys, list):
            raise HTTPException(
                status_code=400, detail="Invalid request format: need 'rank' and 'keys'"
            )

        try:
            # Get key locations
            locations = self.state.get_key_locations(rank, keys)
            return self._json_response({"locations": locations})
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to get key locations: {str(e)}"
            ) frome

    async defclear(self, request: Request):
"""Clear the metadata server."""
        self.state.clear()
        return Response(status_code=204)

    defrun(self, host: str = "0.0.0.0", port: int = 18000):
"""Run the metadata server."""
        importuvicorn

        logger.info("Starting improved metadata server on http://%s:%s", host, port)
        uvicorn.run(self.app, host=host, port=port)
```

### \_json\_response [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer._json_response "Permanent link")

```
_json_response(content: dict)
```

Return ORJSONResponse when available to bypass jsonable\_encoder.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
def_json_response(self, content: dict):
"""Return ORJSONResponse when available to bypass jsonable_encoder."""
    if HAS_ORJSON:
        return ORJSONResponse(content)
    else:
        return content
```

### \_read\_json `async` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer._read_json "Permanent link")

```
_read_json(request: Request) -> dict
```

Parse request JSON using orjson if available.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
async def_read_json(self, request: Request) -> dict:
"""Parse request JSON using orjson if available."""
    body = await request.body()
    return orjson.loads(body)
```

### \_setup\_routes [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer._setup_routes "Permanent link")

Setup FastAPI routes for new API design.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
def_setup_routes(self):
"""Setup FastAPI routes for new API design."""
    self.app.post("/rank/{rank}/initialize")(self.initialize_rank)
    self.app.post("/keys/batch_allocate")(self.batch_allocate_pages_for_keys)
    self.app.post("/keys/confirm_write")(self.confirm_write_for_keys)
    self.app.post("/keys/batch_exists")(self.batch_key_exists)
    self.app.post("/keys/get_locations")(self.get_key_locations)
    self.app.post("/clear")(self.clear)
```

### batch\_allocate\_pages\_for\_keys `async` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer.batch_allocate_pages_for_keys "Permanent link")

```
batch_allocate_pages_for_keys(request: Request)
```

Allocate one page for each key on a specific rank.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
async defbatch_allocate_pages_for_keys(self, request: Request):
"""Allocate one page for each key on a specific rank."""
    data = await self._read_json(request)
    rank = data.get("rank")
    keys = data.get("keys", [])

    # Validate input format
    if rank is None or not isinstance(keys, list):
        raise HTTPException(
            status_code=400, detail="Invalid request format: need 'rank' and 'keys'"
        )

    try:
        # Perform allocation
        results = self.state.allocate_pages_for_keys(rank, keys)

        # Convert results to response format
        response = {"rank": rank, "results": list(results.items())}
        return self._json_response(response)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Allocation failed: {str(e)}"
        ) frome
```

### batch\_key\_exists `async` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer.batch_key_exists "Permanent link")

```
batch_key_exists(request: Request)
```

Check if multiple keys exist in metadata.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
async defbatch_key_exists(self, request: Request):
"""Check if multiple keys exist in metadata."""
    data = await self._read_json(request)
    keys = data.get("keys", [])

    if not isinstance(keys, list):
        raise HTTPException(status_code=400, detail="Invalid keys format")

    try:
        exists_results = self.state.batch_key_exists(keys)
        return self._json_response({"exists": exists_results})
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Key existence check failed: {str(e)}"
        ) frome
```

### clear `async` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer.clear "Permanent link")

Clear the metadata server.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
async defclear(self, request: Request):
"""Clear the metadata server."""
    self.state.clear()
    return Response(status_code=204)
```

### confirm\_write\_for\_keys `async` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer.confirm_write_for_keys "Permanent link")

```
confirm_write_for_keys(request: Request)
```

Confirm write operations for keys.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
async defconfirm_write_for_keys(self, request: Request):
"""Confirm write operations for keys."""
    data = await self._read_json(request)
    rank = data.get("rank")
    confirmations = data.get("confirmations", [])
    pages_to_release = data.get("pages_to_release", [])

    # Validate input format
    if rank is None or not isinstance(confirmations, list):
        raise HTTPException(
            status_code=400,
            detail="Invalid request format: need 'rank' and 'confirmations'",
        )

    try:
        self.state.confirm_write_for_keys(rank, confirmations, pages_to_release)

        return Response(status_code=204)

    except Exception as e:
        logger.error("Confirm write for keys failed: %s", e)
        raise HTTPException(
            status_code=500, detail=f"Confirmation failed: {str(e)}"
        ) frome
```

### get\_key\_locations `async` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer.get_key_locations "Permanent link")

```
get_key_locations(request: Request)
```

Get page indices for keys on a specific rank.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
async defget_key_locations(self, request: Request):
"""Get page indices for keys on a specific rank."""
    data = await self._read_json(request)
    rank = data.get("rank")
    keys = data.get("keys", [])

    # Validate input format
    if rank is None or not isinstance(keys, list):
        raise HTTPException(
            status_code=400, detail="Invalid request format: need 'rank' and 'keys'"
        )

    try:
        # Get key locations
        locations = self.state.get_key_locations(rank, keys)
        return self._json_response({"locations": locations})
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to get key locations: {str(e)}"
        ) frome
```

### initialize\_rank `async` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer.initialize_rank "Permanent link")

```
initialize_rank(rank: int, request: Request)
```

Initialize a rank with specified number of pages.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
async definitialize_rank(self, rank: int, request: Request):
"""Initialize a rank with specified number of pages."""
    data = await self._read_json(request)
    role = data.get("role", "worker")
    num_pages = data.get("num_pages", 0)

    if role == "scheduler":
        return self._json_response(
            {"message": "Scheduler role does not require initialization"}
        )

    if role == "worker" and num_pages > 0:
        self.state.initialize_rank(rank, num_pages)
        return self._json_response(
            {"message": f"Rank {rank} initialized with {num_pages} pages"}
        )
    else:
        raise HTTPException(
            status_code=400, detail="Invalid initialization parameters"
        )
```

### run [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer.run "Permanent link")

```
run(host: str = '0.0.0.0', port: int = 18000)
```

Run the metadata server.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
defrun(self, host: str = "0.0.0.0", port: int = 18000):
"""Run the metadata server."""
    importuvicorn

    logger.info("Starting improved metadata server on http://%s:%s", host, port)
    uvicorn.run(self.app, host=host, port=port)
```

Manages metadata for a single key across multiple ranks.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
@dataclass
classKeyMetadata:
"""Manages metadata for a single key across multiple ranks."""

    key: str
    rank_to_page: dict[int, int]  # rank -> allocated page index
    tp_world_size: int

    defadd_rank_page(self, rank: int, page_index: int) -> None:
"""Add page allocation for a specific rank."""
        self.rank_to_page[rank] = page_index

    defget_all_pages(self) -> list[tuple[int, int]]:
"""Get all (rank, page) pairs for this key."""
        return [(rank, page) for rank, page in self.rank_to_page.items()]

    defget_rank_page(self, rank: int) -> int | None:
"""Get page index for a specific rank."""
        return self.rank_to_page.get(rank)

    defis_complete(self) -> bool:
"""Check if all ranks in the TP world have allocated pages."""
        return len(self.rank_to_page) == self.tp_world_size
```

### add\_rank\_page [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.KeyMetadata.add_rank_page "Permanent link")

```
add_rank_page(rank: int, page_index: int) -> None
```

Add page allocation for a specific rank.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
defadd_rank_page(self, rank: int, page_index: int) -> None:
"""Add page allocation for a specific rank."""
    self.rank_to_page[rank] = page_index
```

### get\_all\_pages [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.KeyMetadata.get_all_pages "Permanent link")

Get all (rank, page) pairs for this key.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
defget_all_pages(self) -> list[tuple[int, int]]:
"""Get all (rank, page) pairs for this key."""
    return [(rank, page) for rank, page in self.rank_to_page.items()]
```

### get\_rank\_page [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.KeyMetadata.get_rank_page "Permanent link")

```
get_rank_page(rank: int) -> int | None
```

Get page index for a specific rank.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
defget_rank_page(self, rank: int) -> int | None:
"""Get page index for a specific rank."""
    return self.rank_to_page.get(rank)
```

### is\_complete [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.KeyMetadata.is_complete "Permanent link")

Check if all ranks in the TP world have allocated pages.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
defis_complete(self) -> bool:
"""Check if all ranks in the TP world have allocated pages."""
    return len(self.rank_to_page) == self.tp_world_size
```

Manages file page allocation for a single rank.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
@dataclass
classRankFileMetadata:
"""Manages file page allocation for a single rank."""

    rank_id: int
    num_pages: int
    free_pages: list[int]

    defallocate_pages(self, num_pages: int) -> list[int]:
"""Allocate specified number of free pages."""
        if len(self.free_pages) < num_pages:
            return []

        allocated = self.free_pages[:num_pages]
        self.free_pages = self.free_pages[num_pages:]
        return allocated

    defrelease_pages(self, page_indices: list[int]) -> None:
"""Release pages back to free pool."""
        for page_idx in page_indices:
            if page_idx not in self.free_pages:
                self.free_pages.append(page_idx)

    defget_free_page_count(self) -> int:
"""Get current number of free pages."""
        return len(self.free_pages)
```

### allocate\_pages [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.RankFileMetadata.allocate_pages "Permanent link")

Allocate specified number of free pages.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
defallocate_pages(self, num_pages: int) -> list[int]:
"""Allocate specified number of free pages."""
    if len(self.free_pages) < num_pages:
        return []

    allocated = self.free_pages[:num_pages]
    self.free_pages = self.free_pages[num_pages:]
    return allocated
```

### get\_free\_page\_count [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.RankFileMetadata.get_free_page_count "Permanent link")

```
get_free_page_count() -> int
```

Get current number of free pages.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
defget_free_page_count(self) -> int:
"""Get current number of free pages."""
    return len(self.free_pages)
```

### release\_pages [¶](#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.RankFileMetadata.release_pages "Permanent link")

```
release_pages(page_indices: list[int]) -> None
```

Release pages back to free pool.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
defrelease_pages(self, page_indices: list[int]) -> None:
"""Release pages back to free pool."""
    for page_idx in page_indices:
        if page_idx not in self.free_pages:
            self.free_pages.append(page_idx)

run_metadata_server(
    host: str = "0.0.0.0", port: int = 18000
)
```

Run the improved HF3FS metadata server.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`

```
defrun_metadata_server(
    host: str = "0.0.0.0",
    port: int = 18000,
):
"""Run the improved HF3FS metadata server."""
    server = Hf3fsMetadataServer()
    server.run(host=host, port=port)
```