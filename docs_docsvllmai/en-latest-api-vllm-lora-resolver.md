---
title: resolver - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/lora/resolver/
source: sitemap
fetched_at: 2026-05-07T21:23:09.439849795-03:00
rendered_js: false
word_count: 217
summary: This document defines the base class for LoRA adapter resolvers and the registry mechanism used to manage, register, and fetch adapter resolution implementations in vLLM.
tags:
    - lora
    - adapter-resolution
    - vllm
    - model-loading
    - python-api
    - abstract-class
category: reference
---

## LoRAResolver [¶](#vllm.lora.resolver.LoRAResolver "Permanent link")

Bases: `ABC`

Base class for LoRA adapter resolvers.

This class defines the interface for resolving and fetching LoRA adapters. Implementations of this class should handle the logic for locating and downloading LoRA adapters from various sources (e.g. S3, cloud storage, etc.).

Source code in `vllm/lora/resolver.py`

```
classLoRAResolver(ABC):
"""Base class for LoRA adapter resolvers.

    This class defines the interface for resolving and fetching LoRA adapters.
    Implementations of this class should handle the logic for locating and
    downloading LoRA adapters from various sources (e.g. S3, cloud storage,
    etc.).
    """

    @abstractmethod
    async defresolve_lora(
        self, base_model_name: str, lora_name: str
    ) -> LoRARequest | None:
"""Abstract method to resolve and fetch a LoRA model adapter.

        Implements logic to locate and download LoRA adapter based on the name.
        Implementations might fetch from a blob storage or other sources.

        Args:
            base_model_name: The name/identifier of the base model to resolve.
            lora_name: The name/identifier of the LoRA model to resolve.

        Returns:
            Optional[LoRARequest]: The resolved LoRA model information, or None
            if the LoRA model cannot be found.
        """
        pass
```

### resolve\_lora `abstractmethod` `async` [¶](#vllm.lora.resolver.LoRAResolver.resolve_lora "Permanent link")

Abstract method to resolve and fetch a LoRA model adapter.

Implements logic to locate and download LoRA adapter based on the name. Implementations might fetch from a blob storage or other sources.

Parameters:

Name Type Description Default `base_model_name` `str`

The name/identifier of the base model to resolve.

*required* `lora_name` `str`

The name/identifier of the LoRA model to resolve.

*required*

Returns:

Type Description `LoRARequest | None`

Optional\[LoRARequest]: The resolved LoRA model information, or None

`LoRARequest | None`

if the LoRA model cannot be found.

Source code in `vllm/lora/resolver.py`

```
@abstractmethod
async defresolve_lora(
    self, base_model_name: str, lora_name: str
) -> LoRARequest | None:
"""Abstract method to resolve and fetch a LoRA model adapter.

    Implements logic to locate and download LoRA adapter based on the name.
    Implementations might fetch from a blob storage or other sources.

    Args:
        base_model_name: The name/identifier of the base model to resolve.
        lora_name: The name/identifier of the LoRA model to resolve.

    Returns:
        Optional[LoRARequest]: The resolved LoRA model information, or None
        if the LoRA model cannot be found.
    """
    pass
```

## \_LoRAResolverRegistry `dataclass` [¶](#vllm.lora.resolver._LoRAResolverRegistry "Permanent link")

Source code in `vllm/lora/resolver.py`

```
@dataclass
class_LoRAResolverRegistry:
    resolvers: dict[str, LoRAResolver] = field(default_factory=dict)

    defget_supported_resolvers(self) -> Set[str]:
"""Get all registered resolver names."""
        return self.resolvers.keys()

    defregister_resolver(
        self,
        resolver_name: str,
        resolver: LoRAResolver,
    ) -> None:
"""Register a LoRA resolver.
        Args:
            resolver_name: Name to register the resolver under.
            resolver: The LoRA resolver instance to register.
        """
        if resolver_name in self.resolvers:
            logger.warning(
                "LoRA resolver %s is already registered, and will be "
                "overwritten by the new resolver instance %s.",
                resolver_name,
                resolver,
            )

        self.resolvers[resolver_name] = resolver

    defget_resolver(self, resolver_name: str) -> LoRAResolver:
"""Get a registered resolver instance by name.
        Args:
            resolver_name: Name of the resolver to get.
        Returns:
            The resolver instance.
        Raises:
            KeyError: If the resolver is not found in the registry.
        """
        if resolver_name not in self.resolvers:
            raise KeyError(
                f"LoRA resolver '{resolver_name}' not found. "
                f"Available resolvers: {list(self.resolvers.keys())}"
            )
        return self.resolvers[resolver_name]
```

### get\_resolver [¶](#vllm.lora.resolver._LoRAResolverRegistry.get_resolver "Permanent link")

```
get_resolver(resolver_name: str) -> LoRAResolver
```

Get a registered resolver instance by name. Args: resolver\_name: Name of the resolver to get. Returns: The resolver instance. Raises: KeyError: If the resolver is not found in the registry.

Source code in `vllm/lora/resolver.py`

```
defget_resolver(self, resolver_name: str) -> LoRAResolver:
"""Get a registered resolver instance by name.
    Args:
        resolver_name: Name of the resolver to get.
    Returns:
        The resolver instance.
    Raises:
        KeyError: If the resolver is not found in the registry.
    """
    if resolver_name not in self.resolvers:
        raise KeyError(
            f"LoRA resolver '{resolver_name}' not found. "
            f"Available resolvers: {list(self.resolvers.keys())}"
        )
    return self.resolvers[resolver_name]
```

### get\_supported\_resolvers [¶](#vllm.lora.resolver._LoRAResolverRegistry.get_supported_resolvers "Permanent link")

```
get_supported_resolvers() -> Set[str]
```

Get all registered resolver names.

Source code in `vllm/lora/resolver.py`

```
defget_supported_resolvers(self) -> Set[str]:
"""Get all registered resolver names."""
    return self.resolvers.keys()
```

### register\_resolver [¶](#vllm.lora.resolver._LoRAResolverRegistry.register_resolver "Permanent link")

```
register_resolver(
    resolver_name: str, resolver: LoRAResolver
) -> None
```

Register a LoRA resolver. Args: resolver\_name: Name to register the resolver under. resolver: The LoRA resolver instance to register.

Source code in `vllm/lora/resolver.py`

```
defregister_resolver(
    self,
    resolver_name: str,
    resolver: LoRAResolver,
) -> None:
"""Register a LoRA resolver.
    Args:
        resolver_name: Name to register the resolver under.
        resolver: The LoRA resolver instance to register.
    """
    if resolver_name in self.resolvers:
        logger.warning(
            "LoRA resolver %s is already registered, and will be "
            "overwritten by the new resolver instance %s.",
            resolver_name,
            resolver,
        )

    self.resolvers[resolver_name] = resolver
```