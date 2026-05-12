---
title: cpu_resource_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/utils/cpu_resource_utils/
source: sitemap
fetched_at: 2026-05-07T21:38:33.211204208-03:00
rendered_js: false
word_count: 15
summary: This function converts a string containing comma-separated integers and ranges into a sorted, unique list of integers.
tags:
    - string-parsing
    - range-expansion
    - integer-lists
    - utility-function
    - data-processing
category: api
---

Parses strings like '0-2,4,7-8' into \[0, 1, 2, 4, 7, 8]

Source code in `vllm/utils/cpu_resource_utils.py`

```
defparse_id_list(raw_str: str) -> list[int]:
"""Parses strings like '0-2,4,7-8' into [0, 1, 2, 4, 7, 8]"""
    result: list[int] = []
    if not raw_str:
        return result

    for part in raw_str.split(","):
        if "-" in part:
            start, end = map(int, part.split("-"))
            result.extend(range(start, end + 1))
        else:
            result.append(int(part))
    return sorted(list(set(result)))
```