---
title: registry - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/renderers/registry/
source: sitemap
fetched_at: 2026-05-07T21:35:27.919853695-03:00
rendered_js: false
word_count: 7
summary: This document defines the RENDERER_REGISTRY, a global registry instance used for mapping rendering modes to their corresponding Python modules and classes within the vLLM framework.
tags:
    - vllm
    - renderer-registry
    - module-mapping
    - global-instance
    - python-metadata
category: reference
---

## RENDERER\_REGISTRY `module-attribute` [¶](#vllm.renderers.registry.RENDERER_REGISTRY "Permanent link")

```
RENDERER_REGISTRY = RendererRegistry(
    {
        mode: (f"vllm.renderers.{mod_relname}", cls_name)
        for mode, (mod_relname, cls_name) in (items())
    }
)
```

The global `RendererRegistry` instance.