---
title: answer_exact_match - DSPy
url: https://dspy.ai/api/evaluation/answer_exact_match/
source: sitemap
fetched_at: 2026-01-23T08:01:35.822731188-03:00
rendered_js: false
word_count: 132
summary: This document defines the answer_exact_match function in DSPy, which evaluates whether a predicted answer matches ground truth references using exact match or an F1-score threshold.
tags:
    - dspy
    - evaluation-metrics
    - exact-match
    - f1-score
    - nlp-validation
category: api
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/evaluation/answer_exact_match.md "Edit this page")

## dspy.evaluate.answer\_exact\_match[¶](#dspyevaluateanswer_exact_match "Permanent link")

## `dspy.evaluate.answer_exact_match(example, pred, trace=None, frac=1.0)` [¶](#dspy.evaluate.answer_exact_match "Permanent link")

Evaluate exact match or F1-thresholded match for an example/prediction pair.

If `example.answer` is a string, compare `pred.answer` against it. If it's a list, compare against any of the references. When `frac >= 1.0` (default), use EM; otherwise require that the maximum F1 across references is at least `frac`.

Parameters:

Name Type Description Default `example`

`dspy.Example` object with field `answer` (str or list\[str]).

*required* `pred`

`dspy.Prediction` object with field `answer` (str).

*required* `trace`

Unused; reserved for compatibility.

`None` `frac` `float`

Threshold in \[0.0, 1.0]. `1.0` means EM.

`1.0`

Returns:

Name Type Description `bool`

True if the match condition holds; otherwise False.

Example

```
importdspy

example = dspy.Example(answer=["Eiffel Tower", "Louvre"])
pred = dspy.Prediction(answer="The Eiffel Tower")

answer_exact_match(example, pred, frac=1.0)  # equivalent to EM, True
answer_exact_match(example, pred, frac=0.5)  # True
```

Source code in `dspy/evaluate/metrics.py`

````
defanswer_exact_match(example, pred, trace=None, frac=1.0):
"""Evaluate exact match or F1-thresholded match for an example/prediction pair.

    If `example.answer` is a string, compare `pred.answer` against it. If it's a list,
    compare against any of the references. When `frac >= 1.0` (default), use EM;
    otherwise require that the maximum F1 across references is at least `frac`.

    Args:
        example: `dspy.Example` object with field `answer` (str or list[str]).
        pred: `dspy.Prediction` object with field `answer` (str).
        trace: Unused; reserved for compatibility.
        frac (float, optional): Threshold in [0.0, 1.0]. `1.0` means EM.

    Returns:
        bool: True if the match condition holds; otherwise False.

    Example:
        ```python
        import dspy

        example = dspy.Example(answer=["Eiffel Tower", "Louvre"])
        pred = dspy.Prediction(answer="The Eiffel Tower")

        answer_exact_match(example, pred, frac=1.0)  # equivalent to EM, True
        answer_exact_match(example, pred, frac=0.5)  # True
        ```
    """
    if isinstance(example.answer, str):
        return _answer_match(pred.answer, [example.answer], frac=frac)
    elif isinstance(example.answer, list):
        return _answer_match(pred.answer, example.answer, frac=frac)

    raise ValueError(f"Invalid answer type: {type(example.answer)}")
````

:::