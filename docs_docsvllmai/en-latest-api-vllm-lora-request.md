---
title: request - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/lora/request/
source: sitemap
fetched_at: 2026-05-07T21:23:08.354281418-03:00
rendered_js: false
word_count: 131
summary: This document defines the LoRARequest class, which encapsulates the configuration and identity parameters required to load and manage LoRA adapters within the vLLM framework.
tags:
    - lora
    - adapter-management
    - vllm
    - model-tuning
    - configuration-schema
category: reference
---

## LoRARequest [¶](#vllm.lora.request.LoRARequest "Permanent link")

Bases: `Struct`

Request for a LoRA adapter.

lora\_int\_id must be globally unique for a given adapter. This is currently not enforced in vLLM.

If True, forces reloading the adapter even if one

with the same lora\_int\_id already exists in the cache. This replaces the existing adapter in-place. If False (default), only loads if the adapter is not already loaded.

Source code in `vllm/lora/request.py`

```
classLoRARequest(
    msgspec.Struct,
    omit_defaults=True,  # type: ignore[call-arg]
    array_like=True,
):  # type: ignore[call-arg]
"""
    Request for a LoRA adapter.

    lora_int_id must be globally unique for a given adapter.
    This is currently not enforced in vLLM.

    load_inplace: If True, forces reloading the adapter even if one
        with the same lora_int_id already exists in the cache. This replaces
        the existing adapter in-place. If False (default), only loads if the
        adapter is not already loaded.
    """

    lora_name: str
    lora_int_id: int
    lora_path: str = ""
    base_model_name: str | None = msgspec.field(default=None)
    tensorizer_config_dict: dict | None = None
    load_inplace: bool = False

    def__post_init__(self):
        if self.lora_int_id < 1:
            raise ValueError(f"id must be > 0, got {self.lora_int_id}")

        # Ensure lora_path is not empty
        assert self.lora_path, "lora_path cannot be empty"

    @property
    defadapter_id(self):
        return self.lora_int_id

    @property
    defname(self):
        return self.lora_name

    @property
    defpath(self):
        return self.lora_path

    def__eq__(self, value: object) -> bool:
"""
        Overrides the equality method to compare LoRARequest
        instances based on lora_name. This allows for identification
        and comparison lora adapter across engines.
        """
        return isinstance(value, self.__class__) and self.lora_name == value.lora_name

    def__hash__(self) -> int:
"""
        Overrides the hash method to hash LoRARequest instances
        based on lora_name. This ensures that LoRARequest instances
        can be used in hash-based collections such as sets and dictionaries,
        identified by their names across engines.
        """
        return hash(self.lora_name)
```

### \_\_eq\__ [¶](#vllm.lora.request.LoRARequest.__eq__ "Permanent link")

Overrides the equality method to compare LoRARequest instances based on lora\_name. This allows for identification and comparison lora adapter across engines.

Source code in `vllm/lora/request.py`

```
def__eq__(self, value: object) -> bool:
"""
    Overrides the equality method to compare LoRARequest
    instances based on lora_name. This allows for identification
    and comparison lora adapter across engines.
    """
    return isinstance(value, self.__class__) and self.lora_name == value.lora_name
```

### \_\_hash\__ [¶](#vllm.lora.request.LoRARequest.__hash__ "Permanent link")

Overrides the hash method to hash LoRARequest instances based on lora\_name. This ensures that LoRARequest instances can be used in hash-based collections such as sets and dictionaries, identified by their names across engines.

Source code in `vllm/lora/request.py`

```
def__hash__(self) -> int:
"""
    Overrides the hash method to hash LoRARequest instances
    based on lora_name. This ensures that LoRARequest instances
    can be used in hash-based collections such as sets and dictionaries,
    identified by their names across engines.
    """
    return hash(self.lora_name)
```