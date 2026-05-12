---
title: fingerprint - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/openai/fingerprint/
source: sitemap
fetched_at: 2026-05-07T21:20:04.210938879-03:00
rendered_js: false
word_count: 158
summary: This document explains how to configure and generate the system_fingerprint string for the vLLM OpenAI-compatible server, which identifies model configuration and server settings.
tags:
    - vllm
    - system-fingerprint
    - openai-api
    - server-configuration
    - model-identity
category: reference
---

## vllm.entrypoints.openai.fingerprint [¶](#vllm.entrypoints.openai.fingerprint "Permanent link")

Build the `system_fingerprint` string returned by the OpenAI-compatible server.

Four modes, configured via `--fingerprint-mode`:

- `full` (default): `vllm-<version>[-<parallelism>]-<hash8>` — encodes server version, any non-trivial parallelism degree (tp/pp/dp/ep), and an 8-char prefix of `vllm_config.compute_hash()` (covers model identity, quant config, speculative, attention backend, etc.).
- `hash`: `vllm-<version>-<hash8>` — parallelism stripped.
- `custom`: user-provided literal via `--fingerprint-value`.
- `none`: the field is omitted (serialized as `null`).

`get_system_fingerprint` is only called at serving-class init (a handful of times per server); each subclass caches the returned string on `self.system_fingerprint`, so per-request cost is one attribute read.

## get\_system\_fingerprint [¶](#vllm.entrypoints.openai.fingerprint.get_system_fingerprint "Permanent link")

```
get_system_fingerprint(vllm_config: Any) -> str | None
```

Return the fingerprint for `vllm_config` using the mode configured by `set_default_fingerprint_mode`.

Source code in `vllm/entrypoints/openai/fingerprint.py`

```
defget_system_fingerprint(vllm_config: Any) -> str | None:
"""Return the fingerprint for ``vllm_config`` using the mode configured by
    ``set_default_fingerprint_mode``."""
    return build_system_fingerprint(vllm_config, _DEFAULT_MODE, _CUSTOM_VALUE)
```

## set\_default\_fingerprint\_mode [¶](#vllm.entrypoints.openai.fingerprint.set_default_fingerprint_mode "Permanent link")

```
set_default_fingerprint_mode(
    mode: FingerprintMode, custom_value: str | None = None
) -> None
```

Configure the fingerprint mode for subsequent `get_system_fingerprint` calls. Called once at server startup.

Source code in `vllm/entrypoints/openai/fingerprint.py`

```
defset_default_fingerprint_mode(
    mode: FingerprintMode,
    custom_value: str | None = None,
) -> None:
"""Configure the fingerprint mode for subsequent ``get_system_fingerprint``
    calls. Called once at server startup."""
    global _DEFAULT_MODE, _CUSTOM_VALUE
    _DEFAULT_MODE = mode
    _CUSTOM_VALUE = custom_value
```