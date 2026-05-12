---
title: dynamic_module - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/dynamic_module/
source: sitemap
fetched_at: 2026-05-07T21:37:43.97490986-03:00
rendered_js: false
word_count: 9
summary: This function attempts to retrieve a specified class from a dynamic module while suppressing exceptions and providing optional logging on failure.
tags:
    - python
    - dynamic-loading
    - error-handling
    - model-loading
    - transformers-library
category: api
---

```
deftry_get_class_from_dynamic_module(
    class_reference: str,
    pretrained_model_name_or_path: str,
    trust_remote_code: bool,
    cache_dir: str | os.PathLike | None = None,
    force_download: bool = False,
    resume_download: bool | None = None,
    proxies: dict[str, str] | None = None,
    token: bool | str | None = None,
    revision: str | None = None,
    local_files_only: bool = False,
    repo_type: str | None = None,
    code_revision: str | None = None,
    warn_on_fail: bool = True,
    **kwargs,
) -> type | None:
"""
    As `transformers.dynamic_module_utils.get_class_from_dynamic_module`,
    but ignoring any errors.
    """
    try:
        resolve_trust_remote_code(
            trust_remote_code,
            pretrained_model_name_or_path,
            has_local_code=False,
            has_remote_code=True,
        )

        return get_class_from_dynamic_module(
            class_reference,
            pretrained_model_name_or_path,
            cache_dir=cache_dir,
            force_download=force_download,
            resume_download=resume_download,
            proxies=proxies,
            token=token,
            revision=revision,
            local_files_only=local_files_only,
            repo_type=repo_type,
            code_revision=code_revision,
            **kwargs,
        )
    except Exception:
        location = "ModelScope" if envs.VLLM_USE_MODELSCOPE else "HF Hub"

        if warn_on_fail:
            logger.warning(
                "Unable to load %s from %s on %s.",
                class_reference,
                pretrained_model_name_or_path,
                location,
                exc_info=True,
            )

        return None
```