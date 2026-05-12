---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/utils/
source: sitemap
fetched_at: 2026-05-07T21:38:20.552435926-03:00
rendered_js: false
word_count: 75
summary: This document provides a reference for utility functions used to manage model repositories, file paths, and configuration redirection within the VLLM framework.
tags:
    - model-management
    - utility-functions
    - vllm
    - modelscope
    - path-handling
    - configuration-redirection
category: reference
---

## convert\_model\_repo\_to\_path [¶](#vllm.transformers_utils.utils.convert_model_repo_to_path "Permanent link")

```
convert_model_repo_to_path(model_repo: str) -> str
```

When VLLM\_USE\_MODELSCOPE is True convert a model repository string to a Path str.

Source code in `vllm/transformers_utils/utils.py`

```
defconvert_model_repo_to_path(model_repo: str) -> str:
"""When VLLM_USE_MODELSCOPE is True convert a model
    repository string to a Path str."""
    if not envs.VLLM_USE_MODELSCOPE or Path(model_repo).exists():
        return model_repo
    frommodelscope.utils.file_utilsimport get_model_cache_root

    return os.path.join(get_model_cache_root(), model_repo)
```

## maybe\_model\_redirect `cached` [¶](#vllm.transformers_utils.utils.maybe_model_redirect "Permanent link")

```
maybe_model_redirect(model: str) -> str
```

Use model\_redirect to redirect the model name to a local folder.

:param model: hf model name :return: maybe redirect to a local folder

Source code in `vllm/transformers_utils/utils.py`

```
@cache
defmaybe_model_redirect(model: str) -> str:
"""
    Use model_redirect to redirect the model name to a local folder.

    :param model: hf model name
    :return: maybe redirect to a local folder
    """

    model_redirect_path = envs.VLLM_MODEL_REDIRECT_PATH

    if not model_redirect_path:
        return model

    if not Path(model_redirect_path).exists():
        return model

    redirect_dict = _maybe_json_dict(model_redirect_path) or _maybe_space_split_dict(
        model_redirect_path
    )
    if redirect_model := redirect_dict.get(model):
        logger.info("model redirect: [ %s ] -> [ %s ]", model, redirect_model)
        return redirect_model

    return model
```

## modelscope\_list\_repo\_files [¶](#vllm.transformers_utils.utils.modelscope_list_repo_files "Permanent link")

```
modelscope_list_repo_files(
    repo_id: str,
    revision: str | None = None,
    token: str | bool | None = None,
) -> list[str]
```

List files in a modelscope repo.

Source code in `vllm/transformers_utils/utils.py`

```
defmodelscope_list_repo_files(
    repo_id: str,
    revision: str | None = None,
    token: str | bool | None = None,
) -> list[str]:
"""List files in a modelscope repo."""
    frommodelscope.hub.apiimport HubApi

    api = HubApi()
    api.login(token)
    # same as huggingface_hub.list_repo_files
    files = [
        file["Path"]
        for file in api.get_model_files(
            model_id=repo_id, revision=revision, recursive=True
        )
        if file["Type"] == "blob"
    ]
    return files
```

## without\_trust\_remote\_code [¶](#vllm.transformers_utils.utils.without_trust_remote_code "Permanent link")

Return kwargs without trust\_remote\_code without modifying original dict.

Source code in `vllm/transformers_utils/utils.py`

```
defwithout_trust_remote_code(kwargs: dict[str, Any]) -> dict[str, Any]:
"""Return kwargs without trust_remote_code without modifying original dict."""
    if "trust_remote_code" not in kwargs:
        return kwargs
    return {k: v for k, v in kwargs.items() if k != "trust_remote_code"}
```