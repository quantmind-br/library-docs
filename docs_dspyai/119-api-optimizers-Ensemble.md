---
title: Ensemble - DSPy
url: https://dspy.ai/api/optimizers/Ensemble/
source: sitemap
fetched_at: 2026-01-23T08:02:14.726852713-03:00
rendered_js: false
word_count: 53
summary: The dspy.Ensemble class is a teleprompter that combines multiple DSPy programs into a single ensembled module, optionally using a reduction function to process outputs.
tags:
    - dspy
    - ensemble
    - teleprompter
    - api-reference
    - machine-learning
    - program-compilation
category: api
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/optimizers/Ensemble.md "Edit this page")

## `dspy.Ensemble(*, reduce_fn=None, size=None, deterministic=False)` [¶](#dspy.Ensemble "Permanent link")

Bases: `Teleprompter`

A common reduce\_fn is dspy.majority.

Source code in `dspy/teleprompt/ensemble.py`

```
def__init__(self, *, reduce_fn=None, size=None, deterministic=False):
"""A common reduce_fn is dspy.majority."""

    assert deterministic is False, "TODO: Implement example hashing for deterministic ensemble."

    self.reduce_fn = reduce_fn
    self.size = size
    self.deterministic = deterministic
```

### Functions[¶](#dspy.Ensemble-functions "Permanent link")

#### `compile(programs)` [¶](#dspy.Ensemble.compile "Permanent link")

Source code in `dspy/teleprompt/ensemble.py`

```
defcompile(self, programs):
    size = self.size
    reduce_fn = self.reduce_fn

    importdspy

    classEnsembledProgram(dspy.Module):
        def__init__(self):
            super().__init__()
            self.programs = programs

        defforward(self, *args, **kwargs):
            programs = random.sample(self.programs, size) if size else self.programs
            outputs = [prog(*args, **kwargs) for prog in programs]

            if reduce_fn:
                return reduce_fn(outputs)

            return outputs

    return EnsembledProgram()
```

#### `get_params() -> dict[str, Any]` [¶](#dspy.Ensemble.get_params "Permanent link")

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