---
title: ColBERTv2 - DSPy
url: https://dspy.ai/api/tools/ColBERTv2/
source: sitemap
fetched_at: 2026-01-23T08:02:46.389584013-03:00
rendered_js: false
word_count: 51
summary: This document defines the dspy.ColBERTv2 class, a wrapper for performing information retrieval via a ColBERTv2 server.
tags:
    - dspy
    - colbertv2
    - information-retrieval
    - api-wrapper
    - search-engine
category: api
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/tools/ColBERTv2.md "Edit this page")

## `dspy.ColBERTv2(url: str = 'http://0.0.0.0', port: str | int | None = None, post_requests: bool = False)` [¶](#dspy.ColBERTv2 "Permanent link")

Wrapper for the ColBERTv2 Retrieval.

Source code in `dspy/dsp/colbertv2.py`

```
def__init__(
    self,
    url: str = "http://0.0.0.0",
    port: str | int | None = None,
    post_requests: bool = False,
):
    self.post_requests = post_requests
    self.url = f"{url}:{port}" if port else url
```

### Functions[¶](#dspy.ColBERTv2-functions "Permanent link")

#### `__call__(query: str, k: int = 10, simplify: bool = False) -> list[str] | list[dotdict]` [¶](#dspy.ColBERTv2.__call__ "Permanent link")

Source code in `dspy/dsp/colbertv2.py`

```
def__call__(
    self,
    query: str,
    k: int = 10,
    simplify: bool = False,
) -> list[str] | list[dotdict]:
    if self.post_requests:
        topk: list[dict[str, Any]] = colbertv2_post_request(self.url, query, k)
    else:
        topk: list[dict[str, Any]] = colbertv2_get_request(self.url, query, k)

    if simplify:
        return [psg["long_text"] for psg in topk]

    return [dotdict(psg) for psg in topk]
```

:::