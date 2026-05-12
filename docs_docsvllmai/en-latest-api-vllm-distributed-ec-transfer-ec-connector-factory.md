---
title: factory - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/ec_transfer/ec_connector/factory/
source: sitemap
fetched_at: 2026-05-07T21:17:47.870373877-03:00
rendered_js: false
word_count: 34
summary: This document defines a factory class for registering and instantiating connector types used in distributed data transfer, supporting lazy loading of modules.
tags:
    - factory-pattern
    - distributed-systems
    - lazy-loading
    - vllm-infrastructure
    - connector-pattern
category: api
---

Source code in `vllm/distributed/ec_transfer/ec_connector/factory.py`

```
classECConnectorFactory:
    _registry: dict[str, Callable[[], type[ECConnectorBase]]] = {}

    @classmethod
    defregister_connector(cls, name: str, module_path: str, class_name: str) -> None:
"""Register a connector with a lazy-loading module and class name."""
        if name in cls._registry:
            raise ValueError(f"Connector '{name}' is already registered.")

        defloader() -> type[ECConnectorBase]:
            module = importlib.import_module(module_path)
            return getattr(module, class_name)

        cls._registry[name] = loader

    @classmethod
    defcreate_connector(
        cls,
        config: "VllmConfig",
        role: ECConnectorRole,
    ) -> ECConnectorBase:
        ec_transfer_config = config.ec_transfer_config
        if ec_transfer_config is None:
            raise ValueError("ec_transfer_config must be set to create a connector")
        connector_cls = cls.get_connector_class(ec_transfer_config)
        logger.info(
            "Creating connector with name: %s and engine_id: %s",
            connector_cls.__name__,
            ec_transfer_config.engine_id,
        )
        # Connector is explicitly separated into two roles.
        # Scheduler connector:
        # - Co-locate with scheduler process
        # - Should only be used inside the Scheduler class
        # Worker connector:
        # - Co-locate with worker process
        return connector_cls(config, role)

    @classmethod
    defget_connector_class(
        cls, ec_transfer_config: "ECTransferConfig"
    ) -> type[ECConnectorBase]:
"""Get the connector class by name."""
        connector_name = ec_transfer_config.ec_connector
        if connector_name is None:
            raise ValueError("EC connect must not be None")
        elif connector_name in cls._registry:
            connector_cls = cls._registry[connector_name]()
        else:
            connector_module_path = ec_transfer_config.ec_connector_module_path
            if connector_module_path is None:
                raise ValueError(f"Unsupported connector type: {connector_name}")
            connector_module = importlib.import_module(connector_module_path)
            connector_cls = getattr(connector_module, connector_name)
        return connector_cls
```

### get\_connector\_class `classmethod` [¶](#vllm.distributed.ec_transfer.ec_connector.factory.ECConnectorFactory.get_connector_class "Permanent link")

Get the connector class by name.

Source code in `vllm/distributed/ec_transfer/ec_connector/factory.py`

```
@classmethod
defget_connector_class(
    cls, ec_transfer_config: "ECTransferConfig"
) -> type[ECConnectorBase]:
"""Get the connector class by name."""
    connector_name = ec_transfer_config.ec_connector
    if connector_name is None:
        raise ValueError("EC connect must not be None")
    elif connector_name in cls._registry:
        connector_cls = cls._registry[connector_name]()
    else:
        connector_module_path = ec_transfer_config.ec_connector_module_path
        if connector_module_path is None:
            raise ValueError(f"Unsupported connector type: {connector_name}")
        connector_module = importlib.import_module(connector_module_path)
        connector_cls = getattr(connector_module, connector_name)
    return connector_cls
```

### register\_connector `classmethod` [¶](#vllm.distributed.ec_transfer.ec_connector.factory.ECConnectorFactory.register_connector "Permanent link")

```
register_connector(
    name: str, module_path: str, class_name: str
) -> None
```

Register a connector with a lazy-loading module and class name.

Source code in `vllm/distributed/ec_transfer/ec_connector/factory.py`

```
@classmethod
defregister_connector(cls, name: str, module_path: str, class_name: str) -> None:
"""Register a connector with a lazy-loading module and class name."""
    if name in cls._registry:
        raise ValueError(f"Connector '{name}' is already registered.")

    defloader() -> type[ECConnectorBase]:
        module = importlib.import_module(module_path)
        return getattr(module, class_name)

    cls._registry[name] = loader
```