---
title: kv_transfer - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/config/kv_transfer/
source: sitemap
fetched_at: 2026-05-07T21:16:58.855262698-03:00
rendered_js: false
word_count: 313
summary: This document defines the KVTransferConfig class, which manages the settings for distributing and transferring KV cache data between vLLM instances.
tags:
    - vllm
    - kv-cache
    - distributed-computing
    - configuration
    - inference
    - memory-management
category: reference
---

## vllm.config.kv\_transfer [¶](#vllm.config.kv_transfer "Permanent link")

## KVTransferConfig [¶](#vllm.config.kv_transfer.KVTransferConfig "Permanent link")

Configuration for distributed KV cache transfer.

Source code in `vllm/config/kv_transfer.py`

```
@config
classKVTransferConfig:
"""Configuration for distributed KV cache transfer."""

    kv_connector: str | None = None
"""The KV connector for vLLM to transmit KV caches between vLLM instances.
    """

    engine_id: str | None = None
"""The engine id for KV transfers."""

    kv_buffer_device: str = field(default_factory=kv_buffer_device_default_factory)
"""The device used by kv connector to buffer the KV cache. Choices are
    'cuda', 'cpu' and 'xpu'."""

    kv_buffer_size: float = 1e9
"""The buffer size for TorchDistributedConnector. Measured in number of
    bytes. Recommended value: 1e9 (about 1GB)."""

    kv_role: KVRole | None = None
"""Whether this vLLM instance produces, consumes KV cache, or both. Choices
    are 'kv_producer', 'kv_consumer', and 'kv_both'."""

    kv_rank: int | None = None
"""The rank of this vLLM instance in the KV cache transfer. Typical value:
    0 for prefill instance, 1 for decode instance.
    Currently only 1P1D is supported."""

    kv_parallel_size: int = 1
"""The number of parallel instances for KV cache transfer. For
    P2pNcclConnector, this should be 2."""

    kv_ip: str = "127.0.0.1"
"""The KV connector ip, used to build distributed connection."""

    kv_port: int = 14579
"""The KV connector port, used to build distributed connection."""

    kv_connector_extra_config: dict[str, Any] = field(default_factory=dict)
"""any extra config that the connector may need."""

    kv_connector_module_path: str | None = None
"""The Python module path to dynamically load the KV connector from.
    Only supported in V1."""

    enable_permute_local_kv: bool = False
"""Experiment feature flag to enable HND to NHD KV Transfer"""

    kv_load_failure_policy: Literal["recompute", "fail"] = "fail"
"""Policy for handling KV cache load failures.
    'recompute': reschedule the request to recompute failed blocks
    'fail': immediately fail the request with an error finish reason (default)"""

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
        hash_str = safe_hash(str(factors).encode(), usedforsecurity=False).hexdigest()
        return hash_str

    def__post_init__(self) -> None:
        if self.engine_id is None:
            self.engine_id = str(uuid.uuid4())

        if self.kv_role is not None and self.kv_role not in get_args(KVRole):
            raise ValueError(
                f"Unsupported kv_role: {self.kv_role}. "
                f"Supported roles are {get_args(KVRole)}"
            )

        if self.kv_connector is not None and self.kv_role is None:
            raise ValueError(
                "Please specify kv_role when kv_connector "
                f"is set, supported roles are {get_args(KVRole)}"
            )

    @property
    defis_kv_transfer_instance(self) -> bool:
        return self.kv_connector is not None and self.kv_role in get_args(KVRole)

    @property
    defis_kv_producer(self) -> bool:
        return self.kv_connector is not None and self.kv_role in get_args(KVProducer)

    @property
    defis_kv_consumer(self) -> bool:
        return self.kv_connector is not None and self.kv_role in get_args(KVConsumer)

    defget_from_extra_config(self, key, default) -> Any:
        return self.kv_connector_extra_config.get(key, default)
```

### enable\_permute\_local\_kv `class-attribute` `instance-attribute` [¶](#vllm.config.kv_transfer.KVTransferConfig.enable_permute_local_kv "Permanent link")

```
enable_permute_local_kv: bool = False
```

Experiment feature flag to enable HND to NHD KV Transfer

### engine\_id `class-attribute` `instance-attribute` [¶](#vllm.config.kv_transfer.KVTransferConfig.engine_id "Permanent link")

```
engine_id: str | None = None
```

The engine id for KV transfers.

### kv\_buffer\_device `class-attribute` `instance-attribute` [¶](#vllm.config.kv_transfer.KVTransferConfig.kv_buffer_device "Permanent link")

```
kv_buffer_device: str = field(
    default_factory=kv_buffer_device_default_factory
)
```

The device used by kv connector to buffer the KV cache. Choices are 'cuda', 'cpu' and 'xpu'.

### kv\_buffer\_size `class-attribute` `instance-attribute` [¶](#vllm.config.kv_transfer.KVTransferConfig.kv_buffer_size "Permanent link")

```
kv_buffer_size: float = 1000000000.0
```

The buffer size for TorchDistributedConnector. Measured in number of bytes. Recommended value: 1e9 (about 1GB).

### kv\_connector `class-attribute` `instance-attribute` [¶](#vllm.config.kv_transfer.KVTransferConfig.kv_connector "Permanent link")

```
kv_connector: str | None = None
```

The KV connector for vLLM to transmit KV caches between vLLM instances.

any extra config that the connector may need.

### kv\_connector\_module\_path `class-attribute` `instance-attribute` [¶](#vllm.config.kv_transfer.KVTransferConfig.kv_connector_module_path "Permanent link")

```
kv_connector_module_path: str | None = None
```

The Python module path to dynamically load the KV connector from. Only supported in V1.

### kv\_ip `class-attribute` `instance-attribute` [¶](#vllm.config.kv_transfer.KVTransferConfig.kv_ip "Permanent link")

The KV connector ip, used to build distributed connection.

### kv\_load\_failure\_policy `class-attribute` `instance-attribute` [¶](#vllm.config.kv_transfer.KVTransferConfig.kv_load_failure_policy "Permanent link")

```
kv_load_failure_policy: Literal["recompute", "fail"] = (
    "fail"
)
```

Policy for handling KV cache load failures. 'recompute': reschedule the request to recompute failed blocks 'fail': immediately fail the request with an error finish reason (default)

### kv\_parallel\_size `class-attribute` `instance-attribute` [¶](#vllm.config.kv_transfer.KVTransferConfig.kv_parallel_size "Permanent link")

```
kv_parallel_size: int = 1
```

The number of parallel instances for KV cache transfer. For P2pNcclConnector, this should be 2.

### kv\_port `class-attribute` `instance-attribute` [¶](#vllm.config.kv_transfer.KVTransferConfig.kv_port "Permanent link")

The KV connector port, used to build distributed connection.

### kv\_rank `class-attribute` `instance-attribute` [¶](#vllm.config.kv_transfer.KVTransferConfig.kv_rank "Permanent link")

```
kv_rank: int | None = None
```

The rank of this vLLM instance in the KV cache transfer. Typical value: 0 for prefill instance, 1 for decode instance. Currently only 1P1D is supported.

### kv\_role `class-attribute` `instance-attribute` [¶](#vllm.config.kv_transfer.KVTransferConfig.kv_role "Permanent link")

```
kv_role: KVRole | None = None
```

Whether this vLLM instance produces, consumes KV cache, or both. Choices are 'kv\_producer', 'kv\_consumer', and 'kv\_both'.

### compute\_hash [¶](#vllm.config.kv_transfer.KVTransferConfig.compute_hash "Permanent link")

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

Source code in `vllm/config/kv_transfer.py`

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
    hash_str = safe_hash(str(factors).encode(), usedforsecurity=False).hexdigest()
    return hash_str
```