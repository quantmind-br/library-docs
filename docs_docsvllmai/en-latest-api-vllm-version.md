---
title: version - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/version/
source: sitemap
fetched_at: 2026-05-07T21:43:22.246016192-03:00
rendered_js: false
word_count: 43
summary: This function verifies if a provided version string corresponds to the previous minor version relative to the current application version.
tags:
    - version-control
    - semantic-versioning
    - utility-function
    - vllm-internals
category: reference
---

Check whether a given version matches the previous minor version.

Return True if version\_str matches the previous minor version.

For example - return True if the current version if 0.7.4 and the supplied version\_str is '0.6'.

Used for --show-hidden-metrics-for-version.

Source code in `vllm/version.py`

```
def_prev_minor_version_was(version_str):
"""Check whether a given version matches the previous minor version.

    Return True if version_str matches the previous minor version.

    For example - return True if the current version if 0.7.4 and the
    supplied version_str is '0.6'.

    Used for --show-hidden-metrics-for-version.
    """
    # Match anything if this is a dev tree
    if __version_tuple__[0:2] == (0, 0):
        return True

    # Note - this won't do the right thing when we release 1.0!
    assert __version_tuple__[0] == 0
    assert isinstance(__version_tuple__[1], int)
    return version_str == f"{__version_tuple__[0]}.{__version_tuple__[1]-1}"
```