---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/lora/utils/
source: sitemap
fetched_at: 2026-05-07T21:23:10.76588572-03:00
rendered_js: false
word_count: 430
summary: This document provides a reference for utility functions used in vLLM to manage LoRA adapter paths, identify supported modules, and configure LoRA-specific execution logic.
tags:
    - vllm
    - lora
    - model-loading
    - adapter-management
    - python-api
    - machine-learning
category: reference
---

## get\_adapter\_absolute\_path [¶](#vllm.lora.utils.get_adapter_absolute_path "Permanent link")

```
get_adapter_absolute_path(lora_path: str) -> str
```

Resolves the given lora\_path to an absolute local path.

If the lora\_path is identified as a Hugging Face model identifier, it will download the model and return the local snapshot path. Otherwise, it treats the lora\_path as a local file path and converts it to an absolute path.

lora\_path (str): The path to the lora model, which can be an absolute path, a relative path, or a Hugging Face model identifier.

Returns: str: The resolved absolute local path to the lora model.

Source code in `vllm/lora/utils.py`

```
defget_adapter_absolute_path(lora_path: str) -> str:
"""
    Resolves the given lora_path to an absolute local path.

    If the lora_path is identified as a Hugging Face model identifier,
    it will download the model and return the local snapshot path.
    Otherwise, it treats the lora_path as a local file path and
    converts it to an absolute path.

    Parameters:
    lora_path (str): The path to the lora model, which can be an absolute path,
                     a relative path, or a Hugging Face model identifier.

    Returns:
    str: The resolved absolute local path to the lora model.
    """

    # Check if the path is an absolute path. Return it no matter exists or not.
    if os.path.isabs(lora_path):
        return lora_path

    # If the path starts with ~, expand the user home directory.
    if lora_path.startswith("~"):
        return os.path.expanduser(lora_path)

    # Check if the expanded relative path exists locally.
    if os.path.exists(lora_path):
        return os.path.abspath(lora_path)

    # If the path does not exist locally.
    if envs.VLLM_USE_MODELSCOPE:
        # If using ModelScope, we assume the path is a ModelScope repo.
        frommodelscope.hub.snapshot_downloadimport InvalidParameter, snapshot_download
        fromrequestsimport HTTPError

        download_fn = lambda: snapshot_download(model_id=lora_path)
        download_exceptions = (HTTPError, InvalidParameter)
        error_log = "Error downloading the ModelScope model"
    else:
        # Otherwise, we assume the path is a Hugging Face Hub repo.
        download_fn = lambda: huggingface_hub.snapshot_download(repo_id=lora_path)
        download_exceptions = (HfHubHTTPError, HFValidationError)
        error_log = "Error downloading the HuggingFace model"

    try:
        local_snapshot_path = download_fn()
    except download_exceptions:
        # Handle errors that may occur during the download.
        # Return original path instead of throwing error here.
        logger.exception(error_log)
        return lora_path

    return local_snapshot_path
```

## get\_captured\_lora\_counts [¶](#vllm.lora.utils.get_captured_lora_counts "Permanent link")

```
get_captured_lora_counts(
    max_loras: int, specialize: bool
) -> list[int]
```

Returns num\_active\_loras values for cudagraph capture.

When specialize=True: powers of 2 up to max\_loras, plus max\_loras + 1. When specialize=False: just \[max\_loras + 1].

This is the single source of truth for LoRA capture cases, used by both CudagraphDispatcher and PunicaWrapperGPU.

Source code in `vllm/lora/utils.py`

```
defget_captured_lora_counts(max_loras: int, specialize: bool) -> list[int]:
"""
    Returns num_active_loras values for cudagraph capture.

    When specialize=True: powers of 2 up to max_loras, plus max_loras + 1.
    When specialize=False: just [max_loras + 1].

    This is the single source of truth for LoRA capture cases, used by both
    CudagraphDispatcher and PunicaWrapperGPU.
    """
    if not specialize:
        return [max_loras + 1]

    return [
        n for n in range(1, max_loras + 2) if (n & (n - 1)) == 0 or n == max_loras + 1
    ]
```

## get\_supported\_lora\_modules [¶](#vllm.lora.utils.get_supported_lora_modules "Permanent link")

In vLLM, all linear layers support LoRA.

Source code in `vllm/lora/utils.py`

```
defget_supported_lora_modules(model: nn.Module) -> list[str]:
"""
    In vLLM, all linear layers support LoRA.
    """

    supported_lora_modules: set[str] = set()
    for name, module in model.named_modules():
        # get the embedding modules if the module's embedding_modules
        # is not empty.
        embedding_modules = getattr(module, "embedding_modules", None)
        if embedding_modules is not None:
            for name in embedding_modules:
                supported_lora_modules.add(name)

        # get all the linear subfixes.
        if isinstance(module, (LinearBase,)):
            supported_lora_modules.add(name.split(".")[-1])

        if isinstance(module, (FusedMoE,)):
            supported_lora_modules.add(name.split(".")[-1])

    return list(supported_lora_modules)
```

## is\_in\_target\_modules [¶](#vllm.lora.utils.is_in_target_modules "Permanent link")

```
is_in_target_modules(
    module_name: str,
    target_modules: list[str] | None,
    packed_modules_mapping: dict[str, list[str]]
    | None = None,
) -> bool
```

Check if a module passes the deployment-time target\_modules filter.

When target\_modules is None (no restriction), all modules pass. Otherwise, the module's suffix must be in the target\_modules list.

Parameters:

Name Type Description Default `module_name` `str`

Full dot-separated module name.

*required* `target_modules` `list[str] | None`

Optional deployment-time restriction list from LoRAConfig.target\_modules.

*required* `packed_modules_mapping` `dict[str, list[str]] | None`

Optional model-defined mapping from packed runtime module names to their adapter-visible submodule names (e.g. `{"gate_up_proj": ["gate_proj", "up_proj"]}`).

`None`

Returns:

Type Description `bool`

True if the module passes the filter, False otherwise.

Source code in `vllm/lora/utils.py`

```
defis_in_target_modules(
    module_name: str,
    target_modules: list[str] | None,
    packed_modules_mapping: dict[str, list[str]] | None = None,
) -> bool:
"""Check if a module passes the deployment-time target_modules filter.

    When target_modules is None (no restriction), all modules pass.
    Otherwise, the module's suffix must be in the target_modules list.

    Args:
        module_name: Full dot-separated module name.
        target_modules: Optional deployment-time restriction list from
            LoRAConfig.target_modules.
        packed_modules_mapping: Optional model-defined mapping from packed
            runtime module names to their adapter-visible submodule names
            (e.g. ``{"gate_up_proj": ["gate_proj", "up_proj"]}``).

    Returns:
        True if the module passes the filter, False otherwise.
    """
    if target_modules is None:
        return True
    target_module_set = set(target_modules)
    module_suffix = module_name.split(".")[-1]
    if module_suffix in target_module_set or module_name in target_module_set:
        return True

    if not packed_modules_mapping:
        return False

    # Runtime packed parent matched by deployment-time child targets.
    packed_children = packed_modules_mapping.get(module_suffix)
    if packed_children and any(child in target_module_set for child in packed_children):
        return True

    # Adapter-visible packed child matched by deployment-time parent target.
    return any(
        module_suffix in children and packed_parent in target_module_set
        for packed_parent, children in packed_modules_mapping.items()
    )
```

## is\_moe\_model [¶](#vllm.lora.utils.is_moe_model "Permanent link")

Checks if the model contains FusedMoE layers and warns the user.

Source code in `vllm/lora/utils.py`

```
defis_moe_model(model: nn.Module) -> bool:
"""Checks if the model contains FusedMoE layers and warns the user."""
    if any(isinstance(module, FusedMoE) for module in model.modules()):
        logger.info_once("MoE model detected. Using fused MoE LoRA implementation.")
        return True
    return False
```

## is\_supported\_lora\_module [¶](#vllm.lora.utils.is_supported_lora_module "Permanent link")

```
is_supported_lora_module(
    module_name: str, supported_lora_modules: list[str]
) -> bool
```

Check if a module is in the model's supported LoRA modules.

Uses regex suffix matching against the model-defined supported modules list (e.g., matching "model.layers.0.self\_attn.o\_proj" against "o\_proj").

Parameters:

Name Type Description Default `module_name` `str`

Full dot-separated module name.

*required* `supported_lora_modules` `list[str]`

List of module suffixes supported by the model.

*required*

Returns:

Type Description `bool`

True if the module is supported, False otherwise.

Source code in `vllm/lora/utils.py`

```
defis_supported_lora_module(
    module_name: str,
    supported_lora_modules: list[str],
) -> bool:
"""Check if a module is in the model's supported LoRA modules.

    Uses regex suffix matching against the model-defined supported modules
    list (e.g., matching "model.layers.0.self_attn.o_proj" against
    "o_proj").

    Args:
        module_name: Full dot-separated module name.
        supported_lora_modules: List of module suffixes supported by the
            model.

    Returns:
        True if the module is supported, False otherwise.
    """
    return any(
        re.match(
            r".*\.{target_module}$".format(target_module=target_module),
            module_name,
        )
        or target_module == module_name
        for target_module in supported_lora_modules
    )
```

## parse\_fine\_tuned\_lora\_name [¶](#vllm.lora.utils.parse_fine_tuned_lora_name "Permanent link")

Parse the name of lora weights.

Parameters:

Name Type Description Default `name` `str`

the name of the fine-tuned LoRA, e.g. base\_model.model.dense1.weight

*required* `weights_mapper` `WeightsMapper | None`

maps the name of weight, e.g. `model.` -&gt; `language_model.model.`,

`None`

return: tuple(module\_name, is\_lora\_a): module\_name: the name of the module, e.g. model.dense1, is\_lora\_a whether the tensor is lora\_a or lora\_b.

Source code in `vllm/lora/utils.py`

```
defparse_fine_tuned_lora_name(
    name: str, weights_mapper: "WeightsMapper | None" = None
) -> tuple[str, bool]:
"""Parse the name of lora weights.

    args:
        name: the name of the fine-tuned LoRA, e.g.
            base_model.model.dense1.weight
        weights_mapper: maps the name of weight, e.g.
            `model.` -> `language_model.model.`,
    return:
        tuple(module_name, is_lora_a):
            module_name: the name of the module, e.g. model.dense1,
            is_lora_a whether the tensor is lora_a or lora_b.
    """

    # LoRA weight qualified name usually starts with `base_model.model.`,
    # so we remove the prefix `base_model.model.` to make the following
    # mapping correctly.
    if name.startswith("base_model.model."):
        name = name.replace("base_model.model.", "")
        name = weights_mapper._map_name(name) if weights_mapper else name
        # recover the prefix `base_model.model.`
        name = "base_model.model." + name
    else:
        name = weights_mapper._map_name(name) if weights_mapper else name

    # In some situations, we may not start with `base_model.model.`.
    # If we don't (e.g., ibm-granite/granite-speech-3.3-8b),
    # we should keep the prefix intact.
    start_index = 2 if name.startswith("base_model.model.") else 0

    parts = name.split(".")
    if parts[-1] == "weight" and (parts[-2] == "lora_A" or parts[-2] == "lora_B"):
        new_name = ".".join(parts[start_index:-2])
        return new_name, parts[-2] == "lora_A"

    if parts[-1] == "lora_embedding_A" or parts[-1] == "lora_embedding_B":
        new_name = ".".join(parts[start_index:-1])
        return new_name, parts[-1] == "lora_embedding_A"

    raise ValueError(f"{name} is unsupported LoRA weight")
```

## replace\_submodule [¶](#vllm.lora.utils.replace_submodule "Permanent link")

Replace a submodule in a model with a new module.

Source code in `vllm/lora/utils.py`

```
defreplace_submodule(
    model: nn.Module, module_name: str, new_module: nn.Module
) -> nn.Module:
"""Replace a submodule in a model with a new module."""
    parent = model.get_submodule(".".join(module_name.split(".")[:-1]))
    target_name = module_name.split(".")[-1]
    setattr(parent, target_name, new_module)
    return new_module
```