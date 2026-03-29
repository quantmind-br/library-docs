---
title: answer_passage_match - DSPy
url: https://dspy.ai/api/evaluation/answer_passage_match/
source: sitemap
fetched_at: 2026-01-23T08:01:36.180534447-03:00
rendered_js: false
word_count: 95
summary: This document defines the answer_passage_match function, an evaluation metric used to determine if any retrieved context passage contains the expected answer string.
tags:
    - dspy
    - evaluation-metrics
    - retrieval
    - nlp
    - answer-matching
category: api
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/evaluation/answer_passage_match.md "Edit this page")

## `dspy.evaluate.answer_passage_match(example, pred, trace=None)` [¶](#dspy.evaluate.answer_passage_match "Permanent link")

Return True if any passage in `pred.context` contains the answer(s).

Strings are normalized (and passages also use DPR normalization internally).

Parameters:

Name Type Description Default `example`

`dspy.Example` object with field `answer` (str or list\[str]).

*required* `pred`

`dspy.Prediction` object with field `context` (list\[str]) containing passages.

*required* `trace`

Unused; reserved for compatibility.

`None`

Returns:

Name Type Description `bool`

True if any passage contains any reference answer; otherwise False.

Example

```
importdspy

example = dspy.Example(answer="Eiffel Tower")
pred = dspy.Prediction(context=["The Eiffel Tower is in Paris.", "..."])

answer_passage_match(example, pred)  # True
```

Source code in `dspy/evaluate/metrics.py`

````
defanswer_passage_match(example, pred, trace=None):
"""Return True if any passage in `pred.context` contains the answer(s).

    Strings are normalized (and passages also use DPR normalization internally).

    Args:
        example: `dspy.Example` object with field `answer` (str or list[str]).
        pred: `dspy.Prediction` object with field `context` (list[str]) containing passages.
        trace: Unused; reserved for compatibility.

    Returns:
        bool: True if any passage contains any reference answer; otherwise False.

    Example:
        ```python
        import dspy

        example = dspy.Example(answer="Eiffel Tower")
        pred = dspy.Prediction(context=["The Eiffel Tower is in Paris.", "..."])

        answer_passage_match(example, pred)  # True
        ```
    """
    if isinstance(example.answer, str):
        return _passage_match(pred.context, [example.answer])
    elif isinstance(example.answer, list):
        return _passage_match(pred.context, example.answer)

    raise ValueError(f"Invalid answer type: {type(example.answer)}")
````

:::