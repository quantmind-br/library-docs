---
title: OutputField - DSPy
url: https://dspy.ai/api/signatures/OutputField/
source: sitemap
fetched_at: 2026-01-23T08:02:44.979898796-03:00
rendered_js: false
word_count: 11
summary: This document defines the OutputField function in the DSPy framework, which is used to specify output components within signatures by wrapping Pydantic fields.
tags:
    - dspy
    - output-field
    - signatures
    - python-api
    - pydantic-integration
category: api
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/signatures/OutputField.md "Edit this page")

## `dspy.OutputField(**kwargs)` [¶](#dspy.OutputField "Permanent link")

Source code in `dspy/signatures/field.py`

```
defOutputField(**kwargs): # noqa: N802
    return pydantic.Field(**move_kwargs(**kwargs, __dspy_field_type="output"))
```

:::