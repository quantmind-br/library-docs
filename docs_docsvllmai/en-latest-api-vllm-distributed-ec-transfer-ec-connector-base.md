---
title: base - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/ec_transfer/ec_connector/base/
source: sitemap
fetched_at: 2026-05-07T21:17:45.929066477-03:00
rendered_js: false
word_count: 752
summary: Defines the base abstract interface for encoder cache connectors in vLLM, providing a framework for managing distributed multimodal encoder cache transfer between scheduler and worker nodes.
tags:
    - vllm
    - distributed-computing
    - encoder-cache
    - p2p-transfer
    - caching-architecture
    - multimodal-inference
category: reference
---

## vllm.distributed.ec\_transfer.ec\_connector.base [¶](#vllm.distributed.ec_transfer.ec_connector.base "Permanent link")

ECConnectorBase Class for Distributed Encoder Cache & P2P Encoder cache communication in V1

The class provides the following primitives

Scheduler-side: runs in the scheduler, binds metadata, which is used by the worker-side to load/save Encoder cache. check\_caches\_exist() - Check whether Encoder cache of requests exist update\_state\_after\_alloc() - update ECConnector state after allocate. This will decide to load the cache or not request\_finished() - called when a request is finished, free the cache with the requests

Worker-side: runs in each worker, loads/saves Encoder Cache to/from the Connector based on the metadata. start\_load\_ec() - starts loading all ECs (maybe async) wait\_for\_save() - blocks until all saves are done

```
get_finished() - called with ids of finished requests, returns
    ids of requests that have completed async sending/recving.
```

## ECConnectorBase [¶](#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase "Permanent link")

Bases: `ABC`

Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`

```
classECConnectorBase(ABC):
    def__init__(self, vllm_config: "VllmConfig", role: ECConnectorRole):
        self._connector_metadata: ECConnectorMetadata | None = None
        self._vllm_config = vllm_config
        self._role = role
        if vllm_config.ec_transfer_config is not None:
            self._is_producer = vllm_config.ec_transfer_config.is_ec_producer
            self._is_consumer = vllm_config.ec_transfer_config.is_ec_consumer
        else:
            raise ValueError("ec_transfer_config must be set for ECConnectorBase")

    @property
    defrole(self) -> ECConnectorRole:
        return self._role

    @property
    defis_producer(self) -> bool:
        return self._is_producer

    @property
    defis_consumer(self) -> bool:
        return self._is_consumer

    # ==============================
    # Worker-side methods
    # ==============================

    defbind_connector_metadata(self, connector_metadata: ECConnectorMetadata) -> None:
"""Set the connector metadata from the scheduler.

        This function should be called by the model runner every time
        before the model execution. The metadata will be used for runtime
        EC cache loading.

        Args:
            connector_metadata (dict): the connector metadata.
        """
        self._connector_metadata = connector_metadata

    defclear_connector_metadata(self) -> None:
"""Clear the connector metadata.

        This function should be called by the model runner every time
        after the model execution.
        """
        self._connector_metadata = None

    def_get_connector_metadata(self) -> ECConnectorMetadata:
"""Get the connector metadata.

        This function should only be called inside the connector.

        Returns:
            ConnectorMetadata: the connector metadata.
        """

        # Should only be called while set to valid metadata.
        assert self._connector_metadata is not None
        return self._connector_metadata

    defregister_caches(
        self,
        ec_caches: dict[str, torch.Tensor],
    ):
"""
        Initialize with the EC caches.
        Args:
            ec_caches: dictionary of encoder cache
        """
        # TODO: Implement this later for P2P feature
        return

    @abstractmethod
    defstart_load_caches(
        self, encoder_cache: dict[str, torch.Tensor], **kwargs
    ) -> None:
"""
        Start loading the cache from the connector into vLLM's encoder cache.

        This method loads the encoder cache based on metadata provided by the scheduler.
        It is called before `_gather_mm_embeddings` for the EC Connector. For EC,
        the `encoder_cache` and `mm_hash` are stored in `kwargs`.

        Args:
            encoder_cache (dict[str, torch.Tensor]): A dictionary mapping multimodal
                data hashes (`mm_hash`) to encoder cache tensors.
            kwargs (dict): Additional keyword arguments for the connector.
        """
        pass

    @abstractmethod
    defsave_caches(
        self, encoder_cache: dict[str, torch.Tensor], mm_hash: str, **kwargs
    ) -> None:
"""
        Save the encoder cache to the connector.

        This method saves the encoder cache from the worker's local storage
        to shared storage or another external connector.

        Args:
            encoder_cache (dict[str, torch.Tensor]): A dictionary mapping multimodal
                data hashes (`mm_hash`) to encoder cache tensors.
            mm_hash (str): The hash of the multimodal data whose cache is being saved.
            kwargs (dict): Additional keyword arguments for the connector.
        """
        pass

    defget_finished(
        self, finished_req_ids: set[str]
    ) -> tuple[set[str] | None, set[str] | None]:
"""
        Notifies worker-side connector ids of requests that have
        finished generating tokens on the worker.
        The scheduler process (via the Executors) will use this output
        to track which workers are done.

        Returns:
            ids of requests that have finished asynchronous transfer
            (requests that previously returned True from request_finished()),
            tuple of (sending/saving ids, recving/loading ids).
            The finished saves/sends req ids must belong to a set provided in a
            call to this method (this call or a prior one).
        """
        return None, None

    # ==============================
    # Scheduler-side methods
    # ==============================

    @abstractmethod
    defhas_cache_item(
        self,
        identifier: str,
    ) -> bool:
"""
        Check if a single encoder cache exists

        Args:
            identifier (str): the identifier of the media.

        Returns:
            A bool where value is True if cache exist for
            the media
        """
        pass

    @abstractmethod
    defupdate_state_after_alloc(self, request: "Request", index: int):
"""
        Update ECConnector state to decide allocate cache for requests

        Args:
            request (Request): the request object.
        """
        pass

    @abstractmethod
    defbuild_connector_meta(
        self, scheduler_output: SchedulerOutput
    ) -> ECConnectorMetadata:
"""
        Build the connector metadata for this step.

        This function should NOT modify fields in the scheduler_output.
        Also, calling this function will reset the state of the connector.

        Args:
            scheduler_output (SchedulerOutput): the scheduler output object.
        """
        pass

    defupdate_connector_output(self, connector_output: ECConnectorOutput):
"""
        Update ECConnector state from worker-side connectors output.

        Args:
            connector_output (ECConnectorOutput): the worker-side
                connectors output.
        """
        return

    defrequest_finished(
        self, request: "Request"
    ) -> tuple[bool, dict[str, Any] | None]:
"""
        Called when a request has finished, before its encoder cache is freed.

        Returns:
            True if the request is being saved/sent asynchronously and cached
            should not be freed until the request_id is returned from
            get_finished().
        """
        return False, None
```

### \_get\_connector\_metadata [¶](#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase._get_connector_metadata "Permanent link")

```
_get_connector_metadata() -> ECConnectorMetadata
```

Get the connector metadata.

This function should only be called inside the connector.

Returns:

Name Type Description `ConnectorMetadata` `ECConnectorMetadata`

the connector metadata.

Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`

```
def_get_connector_metadata(self) -> ECConnectorMetadata:
"""Get the connector metadata.

    This function should only be called inside the connector.

    Returns:
        ConnectorMetadata: the connector metadata.
    """

    # Should only be called while set to valid metadata.
    assert self._connector_metadata is not None
    return self._connector_metadata
```

### bind\_connector\_metadata [¶](#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.bind_connector_metadata "Permanent link")

```
bind_connector_metadata(
    connector_metadata: ECConnectorMetadata,
) -> None
```

Set the connector metadata from the scheduler.

This function should be called by the model runner every time before the model execution. The metadata will be used for runtime EC cache loading.

Parameters:

Name Type Description Default `connector_metadata` `dict`

the connector metadata.

*required*

Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`

```
defbind_connector_metadata(self, connector_metadata: ECConnectorMetadata) -> None:
"""Set the connector metadata from the scheduler.

    This function should be called by the model runner every time
    before the model execution. The metadata will be used for runtime
    EC cache loading.

    Args:
        connector_metadata (dict): the connector metadata.
    """
    self._connector_metadata = connector_metadata
```

### build\_connector\_meta `abstractmethod` [¶](#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.build_connector_meta "Permanent link")

```
build_connector_meta(
    scheduler_output: SchedulerOutput,
) -> ECConnectorMetadata
```

Build the connector metadata for this step.

This function should NOT modify fields in the scheduler\_output. Also, calling this function will reset the state of the connector.

Parameters:

Name Type Description Default `scheduler_output` `SchedulerOutput`

the scheduler output object.

*required*

Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`

```
@abstractmethod
defbuild_connector_meta(
    self, scheduler_output: SchedulerOutput
) -> ECConnectorMetadata:
"""
    Build the connector metadata for this step.

    This function should NOT modify fields in the scheduler_output.
    Also, calling this function will reset the state of the connector.

    Args:
        scheduler_output (SchedulerOutput): the scheduler output object.
    """
    pass
```

### clear\_connector\_metadata [¶](#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.clear_connector_metadata "Permanent link")

```
clear_connector_metadata() -> None
```

Clear the connector metadata.

This function should be called by the model runner every time after the model execution.

Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`

```
defclear_connector_metadata(self) -> None:
"""Clear the connector metadata.

    This function should be called by the model runner every time
    after the model execution.
    """
    self._connector_metadata = None
```

### get\_finished [¶](#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.get_finished "Permanent link")

Notifies worker-side connector ids of requests that have finished generating tokens on the worker. The scheduler process (via the Executors) will use this output to track which workers are done.

Returns:

Type Description `set[str] | None`

ids of requests that have finished asynchronous transfer

`set[str] | None`

(requests that previously returned True from request\_finished()),

`tuple[set[str] | None, set[str] | None]`

tuple of (sending/saving ids, recving/loading ids).

`tuple[set[str] | None, set[str] | None]`

The finished saves/sends req ids must belong to a set provided in a

`tuple[set[str] | None, set[str] | None]`

call to this method (this call or a prior one).

Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`

```
defget_finished(
    self, finished_req_ids: set[str]
) -> tuple[set[str] | None, set[str] | None]:
"""
    Notifies worker-side connector ids of requests that have
    finished generating tokens on the worker.
    The scheduler process (via the Executors) will use this output
    to track which workers are done.

    Returns:
        ids of requests that have finished asynchronous transfer
        (requests that previously returned True from request_finished()),
        tuple of (sending/saving ids, recving/loading ids).
        The finished saves/sends req ids must belong to a set provided in a
        call to this method (this call or a prior one).
    """
    return None, None
```

### has\_cache\_item `abstractmethod` [¶](#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.has_cache_item "Permanent link")

```
has_cache_item(identifier: str) -> bool
```

Check if a single encoder cache exists

Parameters:

Name Type Description Default `identifier` `str`

the identifier of the media.

*required*

Returns:

Type Description `bool`

A bool where value is True if cache exist for

`bool`

the media

Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`

```
@abstractmethod
defhas_cache_item(
    self,
    identifier: str,
) -> bool:
"""
    Check if a single encoder cache exists

    Args:
        identifier (str): the identifier of the media.

    Returns:
        A bool where value is True if cache exist for
        the media
    """
    pass
```

### register\_caches [¶](#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.register_caches "Permanent link")

Initialize with the EC caches. Args: ec\_caches: dictionary of encoder cache

Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`

```
defregister_caches(
    self,
    ec_caches: dict[str, torch.Tensor],
):
"""
    Initialize with the EC caches.
    Args:
        ec_caches: dictionary of encoder cache
    """
    # TODO: Implement this later for P2P feature
    return
```

### request\_finished [¶](#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.request_finished "Permanent link")

Called when a request has finished, before its encoder cache is freed.

Returns:

Type Description `bool`

True if the request is being saved/sent asynchronously and cached

`dict[str, Any] | None`

should not be freed until the request\_id is returned from

`tuple[bool, dict[str, Any] | None]`

get\_finished().

Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`

```
defrequest_finished(
    self, request: "Request"
) -> tuple[bool, dict[str, Any] | None]:
"""
    Called when a request has finished, before its encoder cache is freed.

    Returns:
        True if the request is being saved/sent asynchronously and cached
        should not be freed until the request_id is returned from
        get_finished().
    """
    return False, None
```

### save\_caches `abstractmethod` [¶](#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.save_caches "Permanent link")

Save the encoder cache to the connector.

This method saves the encoder cache from the worker's local storage to shared storage or another external connector.

Parameters:

Name Type Description Default `encoder_cache` `dict[str, Tensor]`

A dictionary mapping multimodal data hashes (`mm_hash`) to encoder cache tensors.

*required* `mm_hash` `str`

The hash of the multimodal data whose cache is being saved.

*required* `kwargs` `dict`

Additional keyword arguments for the connector.

`{}`

Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`

```
@abstractmethod
defsave_caches(
    self, encoder_cache: dict[str, torch.Tensor], mm_hash: str, **kwargs
) -> None:
"""
    Save the encoder cache to the connector.

    This method saves the encoder cache from the worker's local storage
    to shared storage or another external connector.

    Args:
        encoder_cache (dict[str, torch.Tensor]): A dictionary mapping multimodal
            data hashes (`mm_hash`) to encoder cache tensors.
        mm_hash (str): The hash of the multimodal data whose cache is being saved.
        kwargs (dict): Additional keyword arguments for the connector.
    """
    pass
```

### start\_load\_caches `abstractmethod` [¶](#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.start_load_caches "Permanent link")

```
start_load_caches(
    encoder_cache: dict[str, Tensor], **kwargs
) -> None
```

Start loading the cache from the connector into vLLM's encoder cache.

This method loads the encoder cache based on metadata provided by the scheduler. It is called before `_gather_mm_embeddings` for the EC Connector. For EC, the `encoder_cache` and `mm_hash` are stored in `kwargs`.

Parameters:

Name Type Description Default `encoder_cache` `dict[str, Tensor]`

A dictionary mapping multimodal data hashes (`mm_hash`) to encoder cache tensors.

*required* `kwargs` `dict`

Additional keyword arguments for the connector.

`{}`

Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`

```
@abstractmethod
defstart_load_caches(
    self, encoder_cache: dict[str, torch.Tensor], **kwargs
) -> None:
"""
    Start loading the cache from the connector into vLLM's encoder cache.

    This method loads the encoder cache based on metadata provided by the scheduler.
    It is called before `_gather_mm_embeddings` for the EC Connector. For EC,
    the `encoder_cache` and `mm_hash` are stored in `kwargs`.

    Args:
        encoder_cache (dict[str, torch.Tensor]): A dictionary mapping multimodal
            data hashes (`mm_hash`) to encoder cache tensors.
        kwargs (dict): Additional keyword arguments for the connector.
    """
    pass
```

### update\_connector\_output [¶](#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.update_connector_output "Permanent link")

```
update_connector_output(
    connector_output: ECConnectorOutput,
)
```

Update ECConnector state from worker-side connectors output.

Parameters:

Name Type Description Default `connector_output` `ECConnectorOutput`

the worker-side connectors output.

*required*

Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`

```
defupdate_connector_output(self, connector_output: ECConnectorOutput):
"""
    Update ECConnector state from worker-side connectors output.

    Args:
        connector_output (ECConnectorOutput): the worker-side
            connectors output.
    """
    return
```

### update\_state\_after\_alloc `abstractmethod` [¶](#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.update_state_after_alloc "Permanent link")

```
update_state_after_alloc(request: Request, index: int)
```

Update ECConnector state to decide allocate cache for requests

Parameters:

Name Type Description Default `request` `Request`

the request object.

*required*

Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`

```
@abstractmethod
defupdate_state_after_alloc(self, request: "Request", index: int):
"""
    Update ECConnector state to decide allocate cache for requests

    Args:
        request (Request): the request object.
    """
    pass
```

Bases: `ABC`

Abstract Metadata used to communicate between the Scheduler ECConnector and Worker ECConnector.

Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`

```
classECConnectorMetadata(ABC):  # noqa: B024
"""
    Abstract Metadata used to communicate between the
    Scheduler ECConnector and Worker ECConnector.
    """

    pass
```