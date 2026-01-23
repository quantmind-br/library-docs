---
title: LabeledFewShot - DSPy
url: https://dspy.ai/api/optimizers/LabeledFewShot/
source: sitemap
fetched_at: 2026-01-23T08:02:21.023046773-03:00
rendered_js: false
word_count: 48
summary: This document provides a technical specification for the LabeledFewShot teleprompter class in DSPy, which assigns a fixed number of labeled examples from a training set to a model's predictors.
tags:
    - dspy
    - labeled-few-shot
    - teleprompter
    - few-shot-learning
    - machine-learning-optimization
category: api
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/optimizers/LabeledFewShot.md "Edit this page")

## `dspy.LabeledFewShot(k=16)` [¶](#dspy.LabeledFewShot "Permanent link")

Bases: `Teleprompter`

Source code in `dspy/teleprompt/vanilla.py`

```
def__init__(self, k=16):
    self.k = k
```

### Functions[¶](#dspy.LabeledFewShot-functions "Permanent link")

#### `compile(student, *, trainset, sample=True)` [¶](#dspy.LabeledFewShot.compile "Permanent link")

Source code in `dspy/teleprompt/vanilla.py`

```
defcompile(self, student, *, trainset, sample=True):
    self.student = student.reset_copy()
    self.trainset = trainset

    if len(self.trainset) == 0:
        return self.student

    rng = random.Random(0)

    for predictor in self.student.predictors():
        if sample:
            predictor.demos = rng.sample(self.trainset, min(self.k, len(self.trainset)))
        else:
            predictor.demos = self.trainset[: min(self.k, len(self.trainset))]

    return self.student
```

#### `get_params() -> dict[str, Any]` [¶](#dspy.LabeledFewShot.get_params "Permanent link")

Get the parameters of the teleprompter.

Returns:

Type Description `dict[str, Any]`

The parameters of the teleprompter.

Source code in `dspy/teleprompt/teleprompt.py`

```
defget_params(self) -> dict[str, Any]:
"""
    Get the parameters of the teleprompter.

    Returns:
        The parameters of the teleprompter.
    """
    return self.__dict__
```

:::