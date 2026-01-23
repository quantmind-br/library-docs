---
title: Prediction - DSPy
url: https://dspy.ai/api/primitives/Prediction/
source: sitemap
fetched_at: 2026-01-23T08:02:39.39782139-03:00
rendered_js: false
word_count: 168
summary: This document defines the Prediction class in DSPy, which stores module outputs and supports scoring-based comparison and arithmetic operations.
tags:
    - dspy
    - prediction-class
    - module-outputs
    - api-reference
    - machine-learning
category: api
---

Bases: `Example`

A prediction object that contains the output of a DSPy module.

Prediction inherits from Example.

To allow feedback-augmented scores, Prediction supports comparison operations (&lt;, &gt;, &lt;=, &gt;=) for Predictions with a `score` field. The comparison operations compare the 'score' values as floats. For equality comparison, Predictions are equal if their underlying data stores are equal (inherited from Example).

Arithmetic operations (+, /, etc.) are also supported for Predictions with a 'score' field, operating on the score value.

Source code in `dspy/primitives/prediction.py`

```
def__init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    del self._demos
    del self._input_keys

    self._completions = None
    self._lm_usage = None
```

### Functions[¶](#dspy.Prediction-functions "Permanent link")

#### `copy(**kwargs)` [¶](#dspy.Prediction.copy "Permanent link")

Source code in `dspy/primitives/example.py`

```
defcopy(self, **kwargs):
    return type(self)(base=self, **kwargs)
```

#### `from_completions(list_or_dict, signature=None)` `classmethod` [¶](#dspy.Prediction.from_completions "Permanent link")

Source code in `dspy/primitives/prediction.py`

```
@classmethod
deffrom_completions(cls, list_or_dict, signature=None):
    obj = cls()
    obj._completions = Completions(list_or_dict, signature=signature)
    obj._store = {k: v[0] for k, v in obj._completions.items()}

    return obj
```

#### `get(key, default=None)` [¶](#dspy.Prediction.get "Permanent link")

Source code in `dspy/primitives/example.py`

```
defget(self, key, default=None):
    return self._store.get(key, default)
```

#### `get_lm_usage()` [¶](#dspy.Prediction.get_lm_usage "Permanent link")

Source code in `dspy/primitives/prediction.py`

```
defget_lm_usage(self):
    return self._lm_usage
```

#### `inputs()` [¶](#dspy.Prediction.inputs "Permanent link")

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

#### `items(include_dspy=False)` [¶](#dspy.Prediction.items "Permanent link")

Source code in `dspy/primitives/example.py`

```
defitems(self, include_dspy=False):
    return [(k, v) for k, v in self._store.items() if not k.startswith("dspy_") or include_dspy]
```

#### `keys(include_dspy=False)` [¶](#dspy.Prediction.keys "Permanent link")

Source code in `dspy/primitives/example.py`

```
defkeys(self, include_dspy=False):
    return [k for k in self._store.keys() if not k.startswith("dspy_") or include_dspy]
```

#### `labels()` [¶](#dspy.Prediction.labels "Permanent link")

Source code in `dspy/primitives/example.py`

```
deflabels(self):
    # return items that are NOT in input_keys
    input_keys = self.inputs().keys()
    d = {key: self._store[key] for key in self._store if key not in input_keys}
    return type(self)(d)
```

#### `set_lm_usage(value)` [¶](#dspy.Prediction.set_lm_usage "Permanent link")

Source code in `dspy/primitives/prediction.py`

```
defset_lm_usage(self, value):
    self._lm_usage = value
```

#### `toDict()` [¶](#dspy.Prediction.toDict "Permanent link")

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

#### `values(include_dspy=False)` [¶](#dspy.Prediction.values "Permanent link")

Source code in `dspy/primitives/example.py`

```
defvalues(self, include_dspy=False):
    return [v for k, v in self._store.items() if not k.startswith("dspy_") or include_dspy]
```

#### `with_inputs(*keys)` [¶](#dspy.Prediction.with_inputs "Permanent link")

Source code in `dspy/primitives/example.py`

```
defwith_inputs(self, *keys):
    copied = self.copy()
    copied._input_keys = set(keys)
    return copied
```

#### `without(*keys)` [¶](#dspy.Prediction.without "Permanent link")

Source code in `dspy/primitives/example.py`

```
defwithout(self, *keys):
    copied = self.copy()
    for key in keys:
        del copied[key]
    return copied
```