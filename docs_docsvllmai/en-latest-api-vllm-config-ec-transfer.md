---
title: ec_transfer - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/config/ec_transfer/
source: sitemap
fetched_at: 2026-05-07T21:16:56.131051774-03:00
rendered_js: false
word_count: 261
summary: This document defines the configuration parameters for the distributed EC cache transfer system in vLLM, including connection details, role assignment, and buffer management.
tags:
    - vllm
    - ec-transfer
    - distributed-computing
    - cache-management
    - configuration-settings
category: configuration
---

Configuration for distributed EC cache transfer.

Source code in `vllm/config/ec_transfer.py`

```
@config
classECTransferConfig:
"""Configuration for distributed EC cache transfer."""

    ec_connector: str | None = None
"""The EC connector for vLLM to transmit EC caches between vLLM instances.
    """

    engine_id: str | None = None
"""The engine id for EC transfers."""

    ec_buffer_device: str | None = "cuda"
"""The device used by ec connector to buffer the EC cache.
    Currently only support 'cuda'."""

    ec_buffer_size: float = 1e9
"""The buffer size for TorchDistributedConnector. Measured in number of
    bytes. Recommended value: 1e9 (about 1GB)."""

    ec_role: ECRole | None = None
"""Whether this vLLM instance produces, consumes EC cache, or both. Choices
    are 'ec_producer', 'ec_consumer', 'ec_both'."""

    ec_rank: int | None = None
"""The rank of this vLLM instance in the EC cache transfer. Typical value:
    0 for encoder, 1 for pd instance.
    Currently only 1P1D is supported."""

    ec_parallel_size: int = 1
"""The number of parallel instances for EC cache transfer. For
    PyNcclConnector, this should be 2."""

    ec_ip: str = "127.0.0.1"
"""The EC connector ip, used to build distributed connection."""

    ec_port: int = 14579
"""The EC connector port, used to build distributed connection."""

    ec_connector_extra_config: dict[str, Any] = field(default_factory=dict)
"""any extra config that the connector may need."""

    ec_connector_module_path: str | None = None
"""The Python module path to dynamically load the EC connector from.
    Only supported in V1."""

    defcompute_hash(self) -> str:
"""
        WARNING: Whenever a new field is added to this config,
        ensure that it is included in the factors list if
        it affects the computation graph.

        Provide a hash that uniquely identifies all the configs
        that affect the structure of the computation
        graph from input ids/embeddings to the final hidden states,
        excluding anything before input ids/embeddings and after
        the final hidden states.
        """
        # no factors to consider.
        # this config will not affect the computation graph.
        factors: list[Any] = []
        hash_str = hashlib.md5(str(factors).encode(), usedforsecurity=False).hexdigest()
        return hash_str

    def__post_init__(self) -> None:
        if self.engine_id is None:
            self.engine_id = str(uuid.uuid4())

        if self.ec_role is not None and self.ec_role not in get_args(ECRole):
            raise ValueError(
                f"Unsupported ec_role: {self.ec_role}. "
                f"Supported roles are {get_args(ECRole)}"
            )

        if self.ec_connector is not None and self.ec_role is None:
            raise ValueError(
                "Please specify ec_role when ec_connector "
                f"is set, supported roles are {get_args(ECRole)}"
            )

    @property
    defis_ec_transfer_instance(self) -> bool:
        return self.ec_connector is not None and self.ec_role in get_args(ECRole)

    @property
    defis_ec_producer(self) -> bool:
        return self.ec_connector is not None and self.ec_role in get_args(ECProducer)

    @property
    defis_ec_consumer(self) -> bool:
        return self.ec_connector is not None and self.ec_role in get_args(ECConsumer)

    defget_from_extra_config(self, key, default) -> Any:
        return self.ec_connector_extra_config.get(key, default)
```

### ec\_buffer\_device `class-attribute` `instance-attribute` [¶](#vllm.config.ec_transfer.ECTransferConfig.ec_buffer_device "Permanent link")

```
ec_buffer_device: str | None = 'cuda'
```

The device used by ec connector to buffer the EC cache. Currently only support 'cuda'.

### ec\_buffer\_size `class-attribute` `instance-attribute` [¶](#vllm.config.ec_transfer.ECTransferConfig.ec_buffer_size "Permanent link")

```
ec_buffer_size: float = 1000000000.0
```

The buffer size for TorchDistributedConnector. Measured in number of bytes. Recommended value: 1e9 (about 1GB).

### ec\_connector `class-attribute` `instance-attribute` [¶](#vllm.config.ec_transfer.ECTransferConfig.ec_connector "Permanent link")

```
ec_connector: str | None = None
```

The EC connector for vLLM to transmit EC caches between vLLM instances.

any extra config that the connector may need.

### ec\_connector\_module\_path `class-attribute` `instance-attribute` [¶](#vllm.config.ec_transfer.ECTransferConfig.ec_connector_module_path "Permanent link")

```
ec_connector_module_path: str | None = None
```

The Python module path to dynamically load the EC connector from. Only supported in V1.

### ec\_ip `class-attribute` `instance-attribute` [¶](#vllm.config.ec_transfer.ECTransferConfig.ec_ip "Permanent link")

The EC connector ip, used to build distributed connection.

### ec\_parallel\_size `class-attribute` `instance-attribute` [¶](#vllm.config.ec_transfer.ECTransferConfig.ec_parallel_size "Permanent link")

```
ec_parallel_size: int = 1
```

The number of parallel instances for EC cache transfer. For PyNcclConnector, this should be 2.

### ec\_port `class-attribute` `instance-attribute` [¶](#vllm.config.ec_transfer.ECTransferConfig.ec_port "Permanent link")

The EC connector port, used to build distributed connection.

### ec\_rank `class-attribute` `instance-attribute` [¶](#vllm.config.ec_transfer.ECTransferConfig.ec_rank "Permanent link")

```
ec_rank: int | None = None
```

The rank of this vLLM instance in the EC cache transfer. Typical value: 0 for encoder, 1 for pd instance. Currently only 1P1D is supported.

### ec\_role `class-attribute` `instance-attribute` [¶](#vllm.config.ec_transfer.ECTransferConfig.ec_role "Permanent link")

```
ec_role: ECRole | None = None
```

Whether this vLLM instance produces, consumes EC cache, or both. Choices are 'ec\_producer', 'ec\_consumer', 'ec\_both'.

### engine\_id `class-attribute` `instance-attribute` [¶](#vllm.config.ec_transfer.ECTransferConfig.engine_id "Permanent link")

```
engine_id: str | None = None
```

The engine id for EC transfers.

### compute\_hash [¶](#vllm.config.ec_transfer.ECTransferConfig.compute_hash "Permanent link")

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

Source code in `vllm/config/ec_transfer.py`

```
defcompute_hash(self) -> str:
"""
    WARNING: Whenever a new field is added to this config,
    ensure that it is included in the factors list if
    it affects the computation graph.

    Provide a hash that uniquely identifies all the configs
    that affect the structure of the computation
    graph from input ids/embeddings to the final hidden states,
    excluding anything before input ids/embeddings and after
    the final hidden states.
    """
    # no factors to consider.
    # this config will not affect the computation graph.
    factors: list[Any] = []
    hash_str = hashlib.md5(str(factors).encode(), usedforsecurity=False).hexdigest()
    return hash_str
```