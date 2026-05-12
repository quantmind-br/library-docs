---
title: runai_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/runai_utils/
source: sitemap
fetched_at: 2026-05-07T21:38:17.428021509-03:00
rendered_js: false
word_count: 146
summary: This document defines the ObjectStorageModel class and related utility functions for managing, mirroring, and retrieving machine learning model files from object storage into temporary local directories.
tags:
    - object-storage
    - model-caching
    - file-management
    - vllm-utils
    - runai
    - data-loading
category: api
---

## ObjectStorageModel [¶](#vllm.transformers_utils.runai_utils.ObjectStorageModel "Permanent link")

A class representing an ObjectStorage model mirrored into a temporary directory.

Attributes:

Name Type Description `dir`

The temporary created directory.

Methods:

Name Description `pull_files`

Pull model from object storage to the temporary directory.

Source code in `vllm/transformers_utils/runai_utils.py`

```
classObjectStorageModel:
"""
    A class representing an ObjectStorage model mirrored into a
    temporary directory.

    Attributes:
        dir: The temporary created directory.

    Methods:
        pull_files(): Pull model from object storage to the temporary directory.
    """

    def__init__(self, url: str) -> None:
        if envs.VLLM_ASSETS_CACHE_MODEL_CLEAN:
            for sig in (signal.SIGINT, signal.SIGTERM):
                existing_handler = signal.getsignal(sig)
                signal.signal(sig, self._close_by_signal(existing_handler))

        dir_name = os.path.join(
            get_cache_dir(),
            "model_streamer",
            hashlib.sha256(str(url).encode()).hexdigest()[:8],
        )
        os.makedirs(dir_name, exist_ok=True)
        self.dir = dir_name
        logger.debug("Init object storage, model cache path is: %s", dir_name)

    def_close(self) -> None:
        if os.path.exists(self.dir):
            shutil.rmtree(self.dir)

    def_close_by_signal(self, existing_handler=None):
        defnew_handler(signum, frame):
            self._close()
            if existing_handler:
                existing_handler(signum, frame)

        return new_handler

    defpull_files(
        self,
        model_path: str = "",
        allow_pattern: list[str] | None = None,
        ignore_pattern: list[str] | None = None,
    ) -> None:
"""
        Pull files from object storage into the temporary directory.

        Args:
            model_path: The object storage path of the model.
            allow_pattern: A list of patterns of which files to pull.
            ignore_pattern: A list of patterns of which files not to pull.

        """
        if not model_path.endswith("/"):
            model_path = model_path + "/"
        runai_pull_files(model_path, self.dir, allow_pattern, ignore_pattern)
```

### pull\_files [¶](#vllm.transformers_utils.runai_utils.ObjectStorageModel.pull_files "Permanent link")

```
pull_files(
    model_path: str = "",
    allow_pattern: list[str] | None = None,
    ignore_pattern: list[str] | None = None,
) -> None
```

Pull files from object storage into the temporary directory.

Parameters:

Name Type Description Default `model_path` `str`

The object storage path of the model.

`''` `allow_pattern` `list[str] | None`

A list of patterns of which files to pull.

`None` `ignore_pattern` `list[str] | None`

A list of patterns of which files not to pull.

`None`

Source code in `vllm/transformers_utils/runai_utils.py`

```
defpull_files(
    self,
    model_path: str = "",
    allow_pattern: list[str] | None = None,
    ignore_pattern: list[str] | None = None,
) -> None:
"""
    Pull files from object storage into the temporary directory.

    Args:
        model_path: The object storage path of the model.
        allow_pattern: A list of patterns of which files to pull.
        ignore_pattern: A list of patterns of which files not to pull.

    """
    if not model_path.endswith("/"):
        model_path = model_path + "/"
    runai_pull_files(model_path, self.dir, allow_pattern, ignore_pattern)
```

## list\_safetensors [¶](#vllm.transformers_utils.runai_utils.list_safetensors "Permanent link")

List full file names from object path and filter by allow pattern.

Parameters:

Name Type Description Default `path` `str`

The object storage path to list from.

`''`

Returns:

Type Description `list[str]`

list\[str]: List of full object storage paths allowed by the pattern

Source code in `vllm/transformers_utils/runai_utils.py`

```
deflist_safetensors(path: str = "") -> list[str]:
"""
    List full file names from object path and filter by allow pattern.

    Args:
        path: The object storage path to list from.

    Returns:
        list[str]: List of full object storage paths allowed by the pattern
    """
    return runai_list_safetensors(path)
```