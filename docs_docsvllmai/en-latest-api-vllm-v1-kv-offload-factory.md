---
title: factory - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/kv_offload/factory/
source: sitemap
fetched_at: 2026-05-07T21:41:05.750960873-03:00
rendered_js: false
word_count: 23
summary: The OffloadingSpecFactory class provides a registration and factory mechanism for managing KV cache offloading specifications in vLLM.
tags:
    - vllm
    - kv-cache
    - offloading
    - factory-pattern
    - lazy-loading
    - python-api
category: api
---

## OffloadingSpecFactory [¶](#vllm.v1.kv_offload.factory.OffloadingSpecFactory "Permanent link")

Source code in `vllm/v1/kv_offload/factory.py`

```
classOffloadingSpecFactory:
    _registry: dict[str, Callable[[], type[OffloadingSpec]]] = {}

    @classmethod
    defregister_spec(cls, name: str, module_path: str, class_name: str) -> None:
"""Register a spec with a lazy-loading module and class name."""
        if name in cls._registry:
            raise ValueError(f"Connector '{name}' is already registered.")

        defloader() -> type[OffloadingSpec]:
            module = importlib.import_module(module_path)
            return getattr(module, class_name)

        cls._registry[name] = loader

    @classmethod
    defcreate_spec(
        cls,
        config: "VllmConfig",
        kv_cache_config: "KVCacheConfig",
    ) -> OffloadingSpec:
        kv_transfer_config = config.kv_transfer_config
        assert kv_transfer_config is not None
        extra_config = kv_transfer_config.kv_connector_extra_config
        spec_name = extra_config.get("spec_name", "CPUOffloadingSpec")
        if spec_name in cls._registry:
            spec_cls = cls._registry[spec_name]()
        else:
            spec_module_path = extra_config.get("spec_module_path")
            if spec_module_path is None:
                raise ValueError(f"Unsupported spec type: {spec_name}")
            spec_module = importlib.import_module(spec_module_path)
            spec_cls = getattr(spec_module, spec_name)
        assert issubclass(spec_cls, OffloadingSpec)
        logger.info("Creating offloading spec with name: %s", spec_name)
        return spec_cls(config, kv_cache_config)
```

### register\_spec `classmethod` [¶](#vllm.v1.kv_offload.factory.OffloadingSpecFactory.register_spec "Permanent link")

```
register_spec(
    name: str, module_path: str, class_name: str
) -> None
```

Register a spec with a lazy-loading module and class name.

Source code in `vllm/v1/kv_offload/factory.py`

```
@classmethod
defregister_spec(cls, name: str, module_path: str, class_name: str) -> None:
"""Register a spec with a lazy-loading module and class name."""
    if name in cls._registry:
        raise ValueError(f"Connector '{name}' is already registered.")

    defloader() -> type[OffloadingSpec]:
        module = importlib.import_module(module_path)
        return getattr(module, class_name)

    cls._registry[name] = loader
```