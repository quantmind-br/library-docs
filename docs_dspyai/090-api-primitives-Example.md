---
title: Example - DSPy
url: https://dspy.ai/api/primitives/Example/
source: sitemap
fetched_at: 2026-01-23T08:02:34.826443986-03:00
rendered_js: false
word_count: 294
summary: This document details the dspy.Example class, a flexible data container used for training and evaluation data within the DSPy framework, including its methods for input/output separation and serialization.
tags:
    - dspy
    - example-class
    - data-management
    - api-reference
    - training-data
    - serialization
category: api
---

A flexible data container for DSPy examples and training data.

The `Example` class is the standard data format used in DSPy evaluation and optimization.

Key features

- Dictionary-like access patterns (item access, iteration, etc.)
- Flexible initialization from dictionaries, other `Example` instances, or keyword arguments
- Input/output field separation for training data
- Serialization support for saving/loading `Example` instances
- Immutable operations that return new `Example` instances

Examples:

````
Basic usage with keyword arguments:

```python
import dspy

# Create an example with input and output fields
example = dspy.Example(
    question="What is the capital of France?",
    answer="Paris",
)
print(example.question)  # "What is the capital of France?"
print(example.answer)   # "Paris"
```

Initialize from a dictionary:

```python
data = {"question": "What is 2+2?", "answer": "4"}
example = dspy.Example(data)
print(example["question"])  # "What is 2+2?"
```

Copy from another Example:

```python
original = dspy.Example(question="Hello", answer="World")
copy = dspy.Example(original)
print(copy.question)  # "Hello"
```

Working with input/output separation:

```python
# Mark which fields are inputs for training
example = dspy.Example(
    question="What is the weather?",
    answer="It's sunny",
).with_inputs("question")

# Get only input fields
inputs = example.inputs()
print(inputs.question)  # "What is the weather?"

# Get only output fields (labels)
labels = example.labels()
print(labels.answer)  # "It's sunny"
```

Dictionary-like operations:

```python
example = dspy.Example(name="Alice", age=30)

# Check if key exists
if "name" in example:
    print("Name field exists")

# Get with default value
city = example.get("city", "Unknown")
print(city)  # "Unknown"
```
````

Initialize an Example instance.

Parameters:

Name Type Description Default `base`

Optional base data source. Can be: - Another Example instance (copies its data) - A dictionary (copies its key-value pairs) - None (creates empty Example)

`None` `**kwargs`

Additional key-value pairs to store in the Example.

`{}`

Source code in `dspy/primitives/example.py`

```
def__init__(self, base=None, **kwargs):
"""Initialize an Example instance.

    Args:
        base: Optional base data source. Can be:
            - Another Example instance (copies its data)
            - A dictionary (copies its key-value pairs)
            - None (creates empty Example)
        **kwargs: Additional key-value pairs to store in the Example.
    """
    # Internal storage and other attributes
    self._store = {}
    self._demos = []
    self._input_keys = None

    # Initialize from a base Example if provided
    if base and isinstance(base, type(self)):
        self._store = base._store.copy()

    # Initialize from a dict if provided
    elif base and isinstance(base, dict):
        self._store = base.copy()

    # Update with provided kwargs
    self._store.update(kwargs)
```

### Functions[¶](#dspy.Example-functions "Permanent link")

#### `copy(**kwargs)` [¶](#dspy.Example.copy "Permanent link")

Source code in `dspy/primitives/example.py`

```
defcopy(self, **kwargs):
    return type(self)(base=self, **kwargs)
```

#### `get(key, default=None)` [¶](#dspy.Example.get "Permanent link")

Source code in `dspy/primitives/example.py`

```
defget(self, key, default=None):
    return self._store.get(key, default)
```

#### `inputs()` [¶](#dspy.Example.inputs "Permanent link")

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

#### `items(include_dspy=False)` [¶](#dspy.Example.items "Permanent link")

Source code in `dspy/primitives/example.py`

```
defitems(self, include_dspy=False):
    return [(k, v) for k, v in self._store.items() if not k.startswith("dspy_") or include_dspy]
```

#### `keys(include_dspy=False)` [¶](#dspy.Example.keys "Permanent link")

Source code in `dspy/primitives/example.py`

```
defkeys(self, include_dspy=False):
    return [k for k in self._store.keys() if not k.startswith("dspy_") or include_dspy]
```

#### `labels()` [¶](#dspy.Example.labels "Permanent link")

Source code in `dspy/primitives/example.py`

```
deflabels(self):
    # return items that are NOT in input_keys
    input_keys = self.inputs().keys()
    d = {key: self._store[key] for key in self._store if key not in input_keys}
    return type(self)(d)
```

#### `toDict()` [¶](#dspy.Example.toDict "Permanent link")

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

#### `values(include_dspy=False)` [¶](#dspy.Example.values "Permanent link")

Source code in `dspy/primitives/example.py`

```
defvalues(self, include_dspy=False):
    return [v for k, v in self._store.items() if not k.startswith("dspy_") or include_dspy]
```

#### `with_inputs(*keys)` [¶](#dspy.Example.with_inputs "Permanent link")

Source code in `dspy/primitives/example.py`

```
defwith_inputs(self, *keys):
    copied = self.copy()
    copied._input_keys = set(keys)
    return copied
```

#### `without(*keys)` [¶](#dspy.Example.without "Permanent link")

Source code in `dspy/primitives/example.py`

```
defwithout(self, *keys):
    copied = self.copy()
    for key in keys:
        del copied[key]
    return copied
```