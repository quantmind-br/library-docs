---
title: InputField - DSPy
url: https://dspy.ai/api/signatures/InputField/
source: sitemap
fetched_at: 2026-01-23T08:02:43.551860095-03:00
rendered_js: false
word_count: 11
summary: This document defines the InputField function in DSPy, which is used to declare input parameters within a signature using Pydantic field logic.
tags:
    - dspy
    - input-field
    - signatures
    - python-api
    - pydantic-fields
category: api
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/signatures/InputField.md "Edit this page")

## `dspy.InputField(**kwargs)` [¶](#dspy.InputField "Permanent link")

Source code in `dspy/signatures/field.py`

```
defInputField(**kwargs): # noqa: N802
    return pydantic.Field(**move_kwargs(**kwargs, __dspy_field_type="input"))
```

:::