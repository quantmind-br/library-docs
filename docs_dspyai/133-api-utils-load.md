---
title: load - DSPy
url: https://dspy.ai/api/utils/load/
source: sitemap
fetched_at: 2026-01-23T08:03:04.691181198-03:00
rendered_js: false
word_count: 108
summary: This document defines the dspy.load function, which is used to deserialize and load saved DSPy modules from a specified path using cloudpickle.
tags:
    - dspy
    - model-loading
    - serialization
    - cloudpickle
    - python-api
    - module-persistence
category: api
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/utils/load.md "Edit this page")

## `dspy.load(path: str, allow_pickle: bool = False) -> Module` [¶](#dspy.load "Permanent link")

Load saved DSPy model.

This method is used to load a saved DSPy model with `save_program=True`, i.e., the model is saved with cloudpickle.

Parameters:

Name Type Description Default `path` `str`

Path to the saved model.

*required* `allow_pickle` `bool`

Whether to allow loading the model with pickle. This is dangerous and should only be used if you are sure you trust the source of the model.

`False`

Returns:

Type Description `Module`

The loaded model, a `dspy.Module` instance.

Source code in `dspy/utils/saving.py`

```
defload(path: str, allow_pickle: bool = False) -> "Module":
"""Load saved DSPy model.

    This method is used to load a saved DSPy model with `save_program=True`, i.e., the model is saved with cloudpickle.

    Args:
        path (str): Path to the saved model.
        allow_pickle (bool): Whether to allow loading the model with pickle. This is dangerous and should only be used if you are sure you trust the source of the model.

    Returns:
        The loaded model, a `dspy.Module` instance.
    """
    if not allow_pickle:
        raise ValueError("Loading with pickle is not allowed. Please set `allow_pickle=True` if you are sure you trust the source of the model.")

    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"The path '{path}' does not exist.")

    with open(path / "metadata.json") as f:
        metadata = orjson.loads(f.read())

    dependency_versions = get_dependency_versions()
    saved_dependency_versions = metadata["dependency_versions"]
    for key, saved_version in saved_dependency_versions.items():
        if dependency_versions[key] != saved_version:
            logger.warning(
                f"There is a mismatch of {key} version between saved model and current environment. You saved with "
                f"`{key}=={saved_version}`, but now you have `{key}=={dependency_versions[key]}`. This might cause "
                "errors or performance downgrade on the loaded model, please consider loading the model in the same "
                "environment as the saving environment."
            )

    with open(path / "program.pkl", "rb") as f:
        return cloudpickle.load(f)
```

:::