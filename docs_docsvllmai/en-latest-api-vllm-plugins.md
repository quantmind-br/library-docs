---
title: plugins - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/plugins/
source: sitemap
fetched_at: 2026-05-07T21:34:38.027814636-03:00
rendered_js: false
word_count: 32
summary: This document outlines the implementation requirements and safety considerations for developing plugins that are compatible with multi-process loading in the vLLM framework.
tags:
    - vllm
    - plugin-architecture
    - multi-process
    - python-plugins
    - system-design
category: concept
---

WARNING: plugins can be loaded for multiple times in different processes. They should be designed in a way that they can be loaded multiple times without causing issues.

Source code in `vllm/plugins/__init__.py`

```
defload_general_plugins():
"""WARNING: plugins can be loaded for multiple times in different
    processes. They should be designed in a way that they can be loaded
    multiple times without causing issues.
    """
    global plugins_loaded
    if plugins_loaded:
        return
    plugins_loaded = True

    plugins = load_plugins_by_group(group=DEFAULT_PLUGINS_GROUP)
    # general plugins, we only need to execute the loaded functions
    for func in plugins.values():
        func()
```