---
title: EvaluationResult - DSPy
url: https://dspy.ai/api/evaluation/EvaluationResult/
source: sitemap
fetched_at: 2026-01-23T08:01:33.772793741-03:00
rendered_js: false
word_count: 147
summary: This document specifies the dspy.evaluate.EvaluationResult class, which encapsulates the aggregate score and individual results from an evaluation run. It details the class's attributes and methods for accessing predictions, calculating LM usage, and converting data to serializable formats.
tags:
    - dspy
    - evaluation-result
    - api-reference
    - machine-learning-metrics
    - python-api
category: api
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/evaluation/EvaluationResult.md "Edit this page")

## dspy.evaluate.EvaluationResult[¶](#dspyevaluateevaluationresult "Permanent link")

## `dspy.evaluate.EvaluationResult(score: float, results: list[tuple[dspy.Example, dspy.Example, Any]])` [¶](#dspy.evaluate.EvaluationResult "Permanent link")

Bases: `Prediction`

A class that represents the result of an evaluation. It is a subclass of `dspy.Prediction` that contains the following fields

- score: An float value (e.g., 67.30) representing the overall performance
- results: a list of (example, prediction, score) tuples for each example in devset

Source code in `dspy/evaluate/evaluate.py`

```
def__init__(self, score: float, results: list[tuple["dspy.Example", "dspy.Example", Any]]):
    super().__init__(score=score, results=results)
```

### Functions[¶](#dspy.evaluate.EvaluationResult-functions "Permanent link")

#### `copy(**kwargs)` [¶](#dspy.evaluate.EvaluationResult.copy "Permanent link")

Source code in `dspy/primitives/example.py`

```
defcopy(self, **kwargs):
    return type(self)(base=self, **kwargs)
```

#### `from_completions(list_or_dict, signature=None)` `classmethod` [¶](#dspy.evaluate.EvaluationResult.from_completions "Permanent link")

Source code in `dspy/primitives/prediction.py`

```
@classmethod
deffrom_completions(cls, list_or_dict, signature=None):
    obj = cls()
    obj._completions = Completions(list_or_dict, signature=signature)
    obj._store = {k: v[0] for k, v in obj._completions.items()}

    return obj
```

#### `get(key, default=None)` [¶](#dspy.evaluate.EvaluationResult.get "Permanent link")

Source code in `dspy/primitives/example.py`

```
defget(self, key, default=None):
    return self._store.get(key, default)
```

#### `get_lm_usage()` [¶](#dspy.evaluate.EvaluationResult.get_lm_usage "Permanent link")

Source code in `dspy/primitives/prediction.py`

```
defget_lm_usage(self):
    return self._lm_usage
```

#### `inputs()` [¶](#dspy.evaluate.EvaluationResult.inputs "Permanent link")

Source code in `dspy/primitives/example.py`

```
definputs(self):
    if self._input_keys is None:
        raise ValueError("Inputs have not been set for this example. Use `example.with_inputs()` to set them.")

    # return items that are in input_keys
    d = {key: self._store[key] for key in self._store if key in self._input_keys}
    # return type(self)(d)
    new_instance = type(self)(base=d)
    new_instance._input_keys = self._input_keys  # Preserve input_keys in new instance
    return new_instance
```

#### `items(include_dspy=False)` [¶](#dspy.evaluate.EvaluationResult.items "Permanent link")

Source code in `dspy/primitives/example.py`

```
defitems(self, include_dspy=False):
    return [(k, v) for k, v in self._store.items() if not k.startswith("dspy_") or include_dspy]
```

#### `keys(include_dspy=False)` [¶](#dspy.evaluate.EvaluationResult.keys "Permanent link")

Source code in `dspy/primitives/example.py`

```
defkeys(self, include_dspy=False):
    return [k for k in self._store.keys() if not k.startswith("dspy_") or include_dspy]
```

#### `labels()` [¶](#dspy.evaluate.EvaluationResult.labels "Permanent link")

Source code in `dspy/primitives/example.py`

```
deflabels(self):
    # return items that are NOT in input_keys
    input_keys = self.inputs().keys()
    d = {key: self._store[key] for key in self._store if key not in input_keys}
    return type(self)(d)
```

#### `set_lm_usage(value)` [¶](#dspy.evaluate.EvaluationResult.set_lm_usage "Permanent link")

Source code in `dspy/primitives/prediction.py`

```
defset_lm_usage(self, value):
    self._lm_usage = value
```

#### `toDict()` [¶](#dspy.evaluate.EvaluationResult.toDict "Permanent link")

Source code in `dspy/primitives/example.py`

```
deftoDict(self):  # noqa: N802
    defconvert_to_serializable(value):
        if hasattr(value, "toDict"):
            return value.toDict()
        elif isinstance(value, BaseModel):
            # Handle Pydantic models (e.g., dspy.History)
            return value.model_dump()
        elif isinstance(value, list):
            return [convert_to_serializable(item) for item in value]
        elif isinstance(value, dict):
            return {k: convert_to_serializable(v) for k, v in value.items()}
        else:
            return value

    serializable_store = {}
    for k, v in self._store.items():
        serializable_store[k] = convert_to_serializable(v)

    return serializable_store
```

#### `values(include_dspy=False)` [¶](#dspy.evaluate.EvaluationResult.values "Permanent link")

Source code in `dspy/primitives/example.py`

```
defvalues(self, include_dspy=False):
    return [v for k, v in self._store.items() if not k.startswith("dspy_") or include_dspy]
```

#### `with_inputs(*keys)` [¶](#dspy.evaluate.EvaluationResult.with_inputs "Permanent link")

Source code in `dspy/primitives/example.py`

```
defwith_inputs(self, *keys):
    copied = self.copy()
    copied._input_keys = set(keys)
    return copied
```

#### `without(*keys)` [¶](#dspy.evaluate.EvaluationResult.without "Permanent link")

Source code in `dspy/primitives/example.py`

```
defwithout(self, *keys):
    copied = self.copy()
    for key in keys:
        del copied[key]
    return copied
```

:::