---
title: Parallel - DSPy
url: https://dspy.ai/api/modules/Parallel/
source: sitemap
fetched_at: 2026-01-23T08:01:50.851581098-03:00
rendered_js: false
word_count: 76
summary: This document defines the dspy.Parallel class, a module designed to facilitate the multi-threaded execution of DSPy tasks over collections of examples with configurable error handling and timeouts.
tags:
    - dspy
    - parallel-execution
    - multithreading
    - python-api
    - batch-processing
    - concurrency
category: api
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/modules/Parallel.md "Edit this page")

## `dspy.Parallel(num_threads: int | None = None, max_errors: int | None = None, access_examples: bool = True, return_failed_examples: bool = False, provide_traceback: bool | None = None, disable_progress_bar: bool = False, timeout: int = 120, straggler_limit: int = 3)` [¶](#dspy.Parallel "Permanent link")

Source code in `dspy/predict/parallel.py`

```
def__init__(
    self,
    num_threads: int | None = None,
    max_errors: int | None = None,
    access_examples: bool = True,
    return_failed_examples: bool = False,
    provide_traceback: bool | None = None,
    disable_progress_bar: bool = False,
    timeout: int = 120,
    straggler_limit: int = 3,
):
    super().__init__()
    self.num_threads = num_threads or settings.num_threads
    self.max_errors = settings.max_errors if max_errors is None else max_errors
    self.access_examples = access_examples
    self.return_failed_examples = return_failed_examples
    self.provide_traceback = provide_traceback
    self.disable_progress_bar = disable_progress_bar
    self.timeout = timeout
    self.straggler_limit = straggler_limit

    self.error_count = 0
    self.error_lock = threading.Lock()
    self.cancel_jobs = threading.Event()
    self.failed_examples = []
    self.exceptions = []
```

### Functions[¶](#dspy.Parallel-functions "Permanent link")

#### `__call__(*args: Any, **kwargs: Any) -> Any` [¶](#dspy.Parallel.__call__ "Permanent link")

Source code in `dspy/predict/parallel.py`

```
def__call__(self, *args: Any, **kwargs: Any) -> Any:
    return self.forward(*args, **kwargs)
```

#### `forward(exec_pairs: list[tuple[Any, Example]], num_threads: int | None = None) -> list[Any]` [¶](#dspy.Parallel.forward "Permanent link")

Source code in `dspy/predict/parallel.py`

```
defforward(self, exec_pairs: list[tuple[Any, Example]], num_threads: int | None = None) -> list[Any]:
    num_threads = num_threads if num_threads is not None else self.num_threads

    executor = ParallelExecutor(
        num_threads=num_threads,
        max_errors=self.max_errors,
        provide_traceback=self.provide_traceback,
        disable_progress_bar=self.disable_progress_bar,
        timeout=self.timeout,
        straggler_limit=self.straggler_limit,
    )

    defprocess_pair(pair):
        result = None
        module, example = pair

        if isinstance(example, Example):
            if self.access_examples:
                result = module(**example.inputs())
            else:
                result = module(example)
        elif isinstance(example, dict):
            result = module(**example)
        elif isinstance(example, list) and module.__class__.__name__ == "Parallel":
            result = module(example)
        elif isinstance(example, tuple):
            result = module(*example)
        else:
            raise ValueError(
                f"Invalid example type: {type(example)}, only supported types are Example, dict, list and tuple"
            )
        return result

    # Execute the processing function over the execution pairs
    results = executor.execute(process_pair, exec_pairs)

    # Populate failed examples and exceptions from the executor
    if self.return_failed_examples:
        for failed_idx in executor.failed_indices:
            if failed_idx < len(exec_pairs):
                _, original_example = exec_pairs[failed_idx]
                self.failed_examples.append(original_example)
                if exception := executor.exceptions_map.get(failed_idx):
                    self.exceptions.append(exception)

        return results, self.failed_examples, self.exceptions
    else:
        return results
```

:::