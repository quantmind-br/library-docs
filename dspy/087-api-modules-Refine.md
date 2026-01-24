---
title: Refine - DSPy
url: https://dspy.ai/api/modules/Refine/
source: sitemap
fetched_at: 2026-01-23T08:02:02.67768759-03:00
rendered_js: false
word_count: 931
summary: The dspy.Refine module iteratively executes a specified DSPy module up to a maximum number of attempts to find a prediction that satisfies a reward-based threshold. It aims to improve prediction quality by leveraging multiple rollouts and automated feedback generation.
tags:
    - dspy
    - refinement
    - module-api
    - reward-function
    - iterative-refinement
    - llm-optimization
category: api
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/modules/Refine.md "Edit this page")

## `dspy.Refine(module: Module, N: int, reward_fn: Callable[[dict, Prediction], float], threshold: float, fail_count: int | None = None)` [¶](#dspy.Refine "Permanent link")

Bases: `Module`

Refines a module by running it up to N times with different rollout IDs at `temperature=1.0` and returns the best prediction.

This module runs the provided module multiple times with varying rollout identifiers and selects either the first prediction that exceeds the specified threshold or the one with the highest reward. If no prediction meets the threshold, it automatically generates feedback to improve future predictions.

Parameters:

Name Type Description Default `module` `Module`

The module to refine.

*required* `N` `int`

The number of times to run the module. must

*required* `reward_fn` `Callable`

The reward function.

*required* `threshold` `float`

The threshold for the reward function.

*required* `fail_count` `Optional[int]`

The number of times the module can fail before raising an error

`None`

Example

```
importdspy

dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))

# Define a QA module with chain of thought
qa = dspy.ChainOfThought("question -> answer")

# Define a reward function that checks for one-word answers
defone_word_answer(args, pred):
    return 1.0 if len(pred.answer.split()) == 1 else 0.0

# Create a refined module that tries up to 3 times
best_of_3 = dspy.Refine(module=qa, N=3, reward_fn=one_word_answer, threshold=1.0)

# Use the refined module
result = best_of_3(question="What is the capital of Belgium?").answer
# Returns: Brussels
```

Source code in `dspy/predict/refine.py`

````
def__init__(
    self,
    module: Module,
    N: int,  # noqa: N803
    reward_fn: Callable[[dict, Prediction], float],
    threshold: float,
    fail_count: int | None = None,
):
"""
    Refines a module by running it up to N times with different rollout IDs at `temperature=1.0`
    and returns the best prediction.

    This module runs the provided module multiple times with varying rollout identifiers and selects
    either the first prediction that exceeds the specified threshold or the one with the highest reward.
    If no prediction meets the threshold, it automatically generates feedback to improve future predictions.


    Args:
        module (Module): The module to refine.
        N (int): The number of times to run the module. must
        reward_fn (Callable): The reward function.
        threshold (float): The threshold for the reward function.
        fail_count (Optional[int], optional): The number of times the module can fail before raising an error

    Example:
        ```python
        import dspy

        dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))

        # Define a QA module with chain of thought
        qa = dspy.ChainOfThought("question -> answer")

        # Define a reward function that checks for one-word answers
        def one_word_answer(args, pred):
            return 1.0 if len(pred.answer.split()) == 1 else 0.0

        # Create a refined module that tries up to 3 times
        best_of_3 = dspy.Refine(module=qa, N=3, reward_fn=one_word_answer, threshold=1.0)

        # Use the refined module
        result = best_of_3(question="What is the capital of Belgium?").answer
        # Returns: Brussels
        ```
    """
    self.module = module
    self.reward_fn = lambda *args: reward_fn(*args)  # to prevent this from becoming a parameter
    self.threshold = threshold
    self.N = N
    self.fail_count = fail_count or N  # default to N if fail_count is not provided
    self.module_code = inspect.getsource(module.__class__)
    try:
        self.reward_fn_code = inspect.getsource(reward_fn)
    except TypeError:
        self.reward_fn_code = inspect.getsource(reward_fn.__class__)
````

### Functions[¶](#dspy.Refine-functions "Permanent link")

#### `__call__(*args, **kwargs) -> Prediction` [¶](#dspy.Refine.__call__ "Permanent link")

Source code in `dspy/primitives/module.py`

```
@with_callbacks
def__call__(self, *args, **kwargs) -> Prediction:
    fromdspy.dsp.utils.settingsimport thread_local_overrides

    caller_modules = settings.caller_modules or []
    caller_modules = list(caller_modules)
    caller_modules.append(self)

    with settings.context(caller_modules=caller_modules):
        if settings.track_usage and thread_local_overrides.get().get("usage_tracker") is None:
            with track_usage() as usage_tracker:
                output = self.forward(*args, **kwargs)
            tokens = usage_tracker.get_total_tokens()
            self._set_lm_usage(tokens, output)

            return output

        return self.forward(*args, **kwargs)
```

#### `acall(*args, **kwargs) -> Prediction` `async` [¶](#dspy.Refine.acall "Permanent link")

Source code in `dspy/primitives/module.py`

```
@with_callbacks
async defacall(self, *args, **kwargs) -> Prediction:
    fromdspy.dsp.utils.settingsimport thread_local_overrides

    caller_modules = settings.caller_modules or []
    caller_modules = list(caller_modules)
    caller_modules.append(self)

    with settings.context(caller_modules=caller_modules):
        if settings.track_usage and thread_local_overrides.get().get("usage_tracker") is None:
            with track_usage() as usage_tracker:
                output = await self.aforward(*args, **kwargs)
                tokens = usage_tracker.get_total_tokens()
                self._set_lm_usage(tokens, output)

                return output

        return await self.aforward(*args, **kwargs)
```

#### `batch(examples: list[Example], num_threads: int | None = None, max_errors: int | None = None, return_failed_examples: bool = False, provide_traceback: bool | None = None, disable_progress_bar: bool = False, timeout: int = 120, straggler_limit: int = 3) -> list[Example] | tuple[list[Example], list[Example], list[Exception]]` [¶](#dspy.Refine.batch "Permanent link")

Processes a list of dspy.Example instances in parallel using the Parallel module.

Parameters:

Name Type Description Default `examples` `list[Example]`

List of dspy.Example instances to process.

*required* `num_threads` `int | None`

Number of threads to use for parallel processing.

`None` `max_errors` `int | None`

Maximum number of errors allowed before stopping execution. If `None`, inherits from `dspy.settings.max_errors`.

`None` `return_failed_examples` `bool`

Whether to return failed examples and exceptions.

`False` `provide_traceback` `bool | None`

Whether to include traceback information in error logs.

`None` `disable_progress_bar` `bool`

Whether to display the progress bar.

`False` `timeout` `int`

Seconds before a straggler task is resubmitted. Set to 0 to disable.

`120` `straggler_limit` `int`

Only check for stragglers when this many or fewer tasks remain.

`3`

Returns:

Type Description `list[Example] | tuple[list[Example], list[Example], list[Exception]]`

List of results, and optionally failed examples and exceptions.

Source code in `dspy/primitives/module.py`

```
defbatch(
    self,
    examples: list[Example],
    num_threads: int | None = None,
    max_errors: int | None = None,
    return_failed_examples: bool = False,
    provide_traceback: bool | None = None,
    disable_progress_bar: bool = False,
    timeout: int = 120,
    straggler_limit: int = 3,
) -> list[Example] | tuple[list[Example], list[Example], list[Exception]]:
"""
    Processes a list of dspy.Example instances in parallel using the Parallel module.

    Args:
        examples: List of dspy.Example instances to process.
        num_threads: Number of threads to use for parallel processing.
        max_errors: Maximum number of errors allowed before stopping execution.
            If ``None``, inherits from ``dspy.settings.max_errors``.
        return_failed_examples: Whether to return failed examples and exceptions.
        provide_traceback: Whether to include traceback information in error logs.
        disable_progress_bar: Whether to display the progress bar.
        timeout: Seconds before a straggler task is resubmitted. Set to 0 to disable.
        straggler_limit: Only check for stragglers when this many or fewer tasks remain.

    Returns:
        List of results, and optionally failed examples and exceptions.
    """
    # Create a list of execution pairs (self, example)
    exec_pairs = [(self, example.inputs()) for example in examples]

    # Create an instance of Parallel
    parallel_executor = Parallel(
        num_threads=num_threads,
        max_errors=max_errors,
        return_failed_examples=return_failed_examples,
        provide_traceback=provide_traceback,
        disable_progress_bar=disable_progress_bar,
        timeout=timeout,
        straggler_limit=straggler_limit,
    )

    # Execute the forward method of Parallel
    if return_failed_examples:
        results, failed_examples, exceptions = parallel_executor.forward(exec_pairs)
        return results, failed_examples, exceptions
    else:
        results = parallel_executor.forward(exec_pairs)
        return results
```

#### `deepcopy()` [¶](#dspy.Refine.deepcopy "Permanent link")

Deep copy the module.

This is a tweak to the default python deepcopy that only deep copies `self.parameters()`, and for other attributes, we just do the shallow copy.

Source code in `dspy/primitives/base_module.py`

```
defdeepcopy(self):
"""Deep copy the module.

    This is a tweak to the default python deepcopy that only deep copies `self.parameters()`, and for other
    attributes, we just do the shallow copy.
    """
    try:
        # If the instance itself is copyable, we can just deep copy it.
        # Otherwise we will have to create a new instance and copy over the attributes one by one.
        return copy.deepcopy(self)
    except Exception:
        pass

    # Create an empty instance.
    new_instance = self.__class__.__new__(self.__class__)
    # Set attribuetes of the copied instance.
    for attr, value in self.__dict__.items():
        if isinstance(value, BaseModule):
            setattr(new_instance, attr, value.deepcopy())
        else:
            try:
                # Try to deep copy the attribute
                setattr(new_instance, attr, copy.deepcopy(value))
            except Exception:
                logging.warning(
                    f"Failed to deep copy attribute '{attr}' of {self.__class__.__name__}, "
                    "falling back to shallow copy or reference copy."
                )
                try:
                    # Fallback to shallow copy if deep copy fails
                    setattr(new_instance, attr, copy.copy(value))
                except Exception:
                    # If even the shallow copy fails, we just copy over the reference.
                    setattr(new_instance, attr, value)

    return new_instance
```

#### `dump_state(json_mode=True)` [¶](#dspy.Refine.dump_state "Permanent link")

Source code in `dspy/primitives/base_module.py`

```
defdump_state(self, json_mode=True):
    return {name: param.dump_state(json_mode=json_mode) for name, param in self.named_parameters()}
```

#### `forward(**kwargs)` [¶](#dspy.Refine.forward "Permanent link")

Source code in `dspy/predict/refine.py`

```
defforward(self, **kwargs):
    lm = self.module.get_lm() or dspy.settings.lm
    start = lm.kwargs.get("rollout_id", 0)
    rollout_ids = [start + i for i in range(self.N)]
    best_pred, best_trace, best_reward = None, None, -float("inf")
    advice = None
    adapter = dspy.settings.adapter or dspy.ChatAdapter()

    for idx, rid in enumerate(rollout_ids):
        lm_ = lm.copy(rollout_id=rid, temperature=1.0)
        mod = self.module.deepcopy()
        mod.set_lm(lm_)

        predictor2name = {predictor: name for name, predictor in mod.named_predictors()}
        signature2name = {predictor.signature: name for name, predictor in mod.named_predictors()}
        module_names = [name for name, _ in mod.named_predictors()]

        try:
            with dspy.context(trace=[]):
                if not advice:
                    outputs = mod(**kwargs)
                else:

                    classWrapperAdapter(adapter.__class__):
                        def__call__(self, lm, lm_kwargs, signature, demos, inputs):
                            inputs["hint_"] = advice.get(signature2name[signature], "N/A")  # noqa: B023
                            signature = signature.append(
                                "hint_", InputField(desc="A hint to the module from an earlier run")
                            )
                            return adapter(lm, lm_kwargs, signature, demos, inputs)

                    with dspy.context(adapter=WrapperAdapter()):
                        outputs = mod(**kwargs)

                trace = dspy.settings.trace.copy()

                # TODO: Remove the hint from the trace, if it's there.

                # NOTE: Not including the trace of reward_fn.
                reward = self.reward_fn(kwargs, outputs)

            if reward > best_reward:
                best_reward, best_pred, best_trace = reward, outputs, trace

            if self.threshold is not None and reward >= self.threshold:
                break

            if idx == self.N - 1:
                break

            modules = {"program_code": self.module_code, "modules_defn": inspect_modules(mod)}
            trajectory = [{"module_name": predictor2name[p], "inputs": i, "outputs": dict(o)} for p, i, o in trace]
            trajectory = {
                "program_inputs": kwargs,
                "program_trajectory": trajectory,
                "program_outputs": dict(outputs),
            }
            reward = {
                "reward_code": self.reward_fn_code,
                "target_threshold": self.threshold,
                "reward_value": reward,
            }

            advise_kwargs = dict(**modules, **trajectory, **reward, module_names=module_names)
            # only dumps if it's a list or dict
            advise_kwargs = {
                k: v if isinstance(v, str) else orjson.dumps(recursive_mask(v), option=orjson.OPT_INDENT_2).decode()
                for k, v in advise_kwargs.items()
            }
            advice = dspy.Predict(OfferFeedback)(**advise_kwargs).advice
            # print(f"Advice for each module: {advice}")

        except Exception as e:
            print(f"Refine: Attempt failed with rollout id {rid}: {e}")
            if idx > self.fail_count:
                raise e
            self.fail_count -= 1
    if best_trace:
        dspy.settings.trace.extend(best_trace)
    return best_pred
```

#### `get_lm()` [¶](#dspy.Refine.get_lm "Permanent link")

Source code in `dspy/primitives/module.py`

```
defget_lm(self):
    all_used_lms = [param.lm for _, param in self.named_predictors()]

    if len(set(all_used_lms)) == 1:
        return all_used_lms[0]

    raise ValueError("Multiple LMs are being used in the module. There's no unique LM to return.")
```

#### `inspect_history(n: int = 1)` [¶](#dspy.Refine.inspect_history "Permanent link")

Source code in `dspy/primitives/module.py`

```
definspect_history(self, n: int = 1):
    return pretty_print_history(self.history, n)
```

#### `load(path, allow_pickle=False)` [¶](#dspy.Refine.load "Permanent link")

Load the saved module. You may also want to check out dspy.load, if you want to load an entire program, not just the state for an existing program.

Parameters:

Name Type Description Default `path` `str`

Path to the saved state file, which should be a .json or a .pkl file

*required* `allow_pickle` `bool`

If True, allow loading .pkl files, which can run arbitrary code. This is dangerous and should only be used if you are sure about the source of the file and in a trusted environment.

`False`

Source code in `dspy/primitives/base_module.py`

```
defload(self, path, allow_pickle=False):
"""Load the saved module. You may also want to check out dspy.load, if you want to
    load an entire program, not just the state for an existing program.

    Args:
        path (str): Path to the saved state file, which should be a .json or a .pkl file
        allow_pickle (bool): If True, allow loading .pkl files, which can run arbitrary code.
            This is dangerous and should only be used if you are sure about the source of the file and in a trusted environment.
    """
    path = Path(path)

    if path.suffix == ".json":
        with open(path, "rb") as f:
            state = orjson.loads(f.read())
    elif path.suffix == ".pkl":
        if not allow_pickle:
            raise ValueError("Loading .pkl files can run arbitrary code, which may be dangerous. Prefer "
                             "saving with .json files if possible. Set `allow_pickle=True` "
                             "if you are sure about the source of the file and in a trusted environment.")
        with open(path, "rb") as f:
            state = cloudpickle.load(f)
    else:
        raise ValueError(f"`path` must end with `.json` or `.pkl`, but received: {path}")

    dependency_versions = get_dependency_versions()
    saved_dependency_versions = state["metadata"]["dependency_versions"]
    for key, saved_version in saved_dependency_versions.items():
        if dependency_versions[key] != saved_version:
            logger.warning(
                f"There is a mismatch of {key} version between saved model and current environment. "
                f"You saved with `{key}=={saved_version}`, but now you have "
                f"`{key}=={dependency_versions[key]}`. This might cause errors or performance downgrade "
                "on the loaded model, please consider loading the model in the same environment as the "
                "saving environment."
            )
    self.load_state(state)
```

#### `load_state(state)` [¶](#dspy.Refine.load_state "Permanent link")

Source code in `dspy/primitives/base_module.py`

```
defload_state(self, state):
    for name, param in self.named_parameters():
        param.load_state(state[name])
```

#### `map_named_predictors(func)` [¶](#dspy.Refine.map_named_predictors "Permanent link")

Applies a function to all named predictors.

Source code in `dspy/primitives/module.py`

```
defmap_named_predictors(self, func):
"""Applies a function to all named predictors."""
    for name, predictor in self.named_predictors():
        set_attribute_by_name(self, name, func(predictor))
    return self
```

#### `named_parameters()` [¶](#dspy.Refine.named_parameters "Permanent link")

Unlike PyTorch, handles (non-recursive) lists of parameters too.

Source code in `dspy/primitives/base_module.py`

```
defnamed_parameters(self):
"""
    Unlike PyTorch, handles (non-recursive) lists of parameters too.
    """

    importdspy
    fromdspy.predict.parameterimport Parameter

    visited = set()
    named_parameters = []

    defadd_parameter(param_name, param_value):
        if isinstance(param_value, Parameter):
            if id(param_value) not in visited:
                visited.add(id(param_value))
                named_parameters.append((param_name, param_value))

        elif isinstance(param_value, dspy.Module):
            # When a sub-module is pre-compiled, keep it frozen.
            if not getattr(param_value, "_compiled", False):
                for sub_name, param in param_value.named_parameters():
                    add_parameter(f"{param_name}.{sub_name}", param)

    if isinstance(self, Parameter):
        add_parameter("self", self)

    for name, value in self.__dict__.items():
        if isinstance(value, Parameter):
            add_parameter(name, value)

        elif isinstance(value, dspy.Module):
            # When a sub-module is pre-compiled, keep it frozen.
            if not getattr(value, "_compiled", False):
                for sub_name, param in value.named_parameters():
                    add_parameter(f"{name}.{sub_name}", param)

        elif isinstance(value, (list, tuple)):
            for idx, item in enumerate(value):
                add_parameter(f"{name}[{idx}]", item)

        elif isinstance(value, dict):
            for key, item in value.items():
                add_parameter(f"{name}['{key}']", item)

    return named_parameters
```

#### `named_predictors()` [¶](#dspy.Refine.named_predictors "Permanent link")

Source code in `dspy/primitives/module.py`

```
defnamed_predictors(self):
    fromdspy.predict.predictimport Predict

    return [(name, param) for name, param in self.named_parameters() if isinstance(param, Predict)]
```

#### `named_sub_modules(type_=None, skip_compiled=False) -> Generator[tuple[str, BaseModule], None, None]` [¶](#dspy.Refine.named_sub_modules "Permanent link")

Find all sub-modules in the module, as well as their names.

Say `self.children[4]['key'].sub_module` is a sub-module. Then the name will be `children[4]['key'].sub_module`. But if the sub-module is accessible at different paths, only one of the paths will be returned.

Source code in `dspy/primitives/base_module.py`

```
defnamed_sub_modules(self, type_=None, skip_compiled=False) -> Generator[tuple[str, "BaseModule"], None, None]:
"""Find all sub-modules in the module, as well as their names.

    Say `self.children[4]['key'].sub_module` is a sub-module. Then the name will be
    `children[4]['key'].sub_module`. But if the sub-module is accessible at different
    paths, only one of the paths will be returned.
    """
    if type_ is None:
        type_ = BaseModule

    queue = deque([("self", self)])
    seen = {id(self)}

    defadd_to_queue(name, item):
        if id(item) not in seen:
            seen.add(id(item))
            queue.append((name, item))

    while queue:
        name, item = queue.popleft()

        if isinstance(item, type_):
            yield name, item

        if isinstance(item, BaseModule):
            if skip_compiled and getattr(item, "_compiled", False):
                continue
            for sub_name, sub_item in item.__dict__.items():
                add_to_queue(f"{name}.{sub_name}", sub_item)

        elif isinstance(item, (list, tuple)):
            for i, sub_item in enumerate(item):
                add_to_queue(f"{name}[{i}]", sub_item)

        elif isinstance(item, dict):
            for key, sub_item in item.items():
                add_to_queue(f"{name}[{key}]", sub_item)
```

#### `parameters()` [¶](#dspy.Refine.parameters "Permanent link")

Source code in `dspy/primitives/base_module.py`

```
defparameters(self):
    return [param for _, param in self.named_parameters()]
```

#### `predictors()` [¶](#dspy.Refine.predictors "Permanent link")

Source code in `dspy/primitives/module.py`

```
defpredictors(self):
    return [param for _, param in self.named_predictors()]
```

#### `reset_copy()` [¶](#dspy.Refine.reset_copy "Permanent link")

Deep copy the module and reset all parameters.

Source code in `dspy/primitives/base_module.py`

```
defreset_copy(self):
"""Deep copy the module and reset all parameters."""
    new_instance = self.deepcopy()

    for param in new_instance.parameters():
        param.reset()

    return new_instance
```

#### `save(path, save_program=False, modules_to_serialize=None)` [¶](#dspy.Refine.save "Permanent link")

Save the module.

Save the module to a directory or a file. There are two modes: - `save_program=False`: Save only the state of the module to a json or pickle file, based on the value of the file extension. - `save_program=True`: Save the whole module to a directory via cloudpickle, which contains both the state and architecture of the model.

If `save_program=True` and `modules_to_serialize` are provided, it will register those modules for serialization with cloudpickle's `register_pickle_by_value`. This causes cloudpickle to serialize the module by value rather than by reference, ensuring the module is fully preserved along with the saved program. This is useful when you have custom modules that need to be serialized alongside your program. If None, then no modules will be registered for serialization.

We also save the dependency versions, so that the loaded model can check if there is a version mismatch on critical dependencies or DSPy version.

Parameters:

Name Type Description Default `path` `str`

Path to the saved state file, which should be a .json or .pkl file when `save_program=False`, and a directory when `save_program=True`.

*required* `save_program` `bool`

If True, save the whole module to a directory via cloudpickle, otherwise only save the state.

`False` `modules_to_serialize` `list`

A list of modules to serialize with cloudpickle's `register_pickle_by_value`. If None, then no modules will be registered for serialization.

`None`

Source code in `dspy/primitives/base_module.py`

```
defsave(self, path, save_program=False, modules_to_serialize=None):
"""Save the module.

    Save the module to a directory or a file. There are two modes:
    - `save_program=False`: Save only the state of the module to a json or pickle file, based on the value of
        the file extension.
    - `save_program=True`: Save the whole module to a directory via cloudpickle, which contains both the state and
        architecture of the model.

    If `save_program=True` and `modules_to_serialize` are provided, it will register those modules for serialization
    with cloudpickle's `register_pickle_by_value`. This causes cloudpickle to serialize the module by value rather
    than by reference, ensuring the module is fully preserved along with the saved program. This is useful
    when you have custom modules that need to be serialized alongside your program. If None, then no modules
    will be registered for serialization.

    We also save the dependency versions, so that the loaded model can check if there is a version mismatch on
    critical dependencies or DSPy version.

    Args:
        path (str): Path to the saved state file, which should be a .json or .pkl file when `save_program=False`,
            and a directory when `save_program=True`.
        save_program (bool): If True, save the whole module to a directory via cloudpickle, otherwise only save
            the state.
        modules_to_serialize (list): A list of modules to serialize with cloudpickle's `register_pickle_by_value`.
            If None, then no modules will be registered for serialization.

    """
    metadata = {}
    metadata["dependency_versions"] = get_dependency_versions()
    path = Path(path)

    if save_program:
        if path.suffix:
            raise ValueError(
                f"`path` must point to a directory without a suffix when `save_program=True`, but received: {path}"
            )
        if path.exists() and not path.is_dir():
            raise NotADirectoryError(f"The path '{path}' exists but is not a directory.")

        if not path.exists():
            # Create the directory (and any parent directories)
            path.mkdir(parents=True)
        logger.warning("Loading untrusted .pkl files can run arbitrary code, which may be dangerous. To avoid "
                      'this, prefer saving using json format using module.save("module.json").')
        try:
            modules_to_serialize = modules_to_serialize or []
            for module in modules_to_serialize:
                cloudpickle.register_pickle_by_value(module)

            with open(path / "program.pkl", "wb") as f:
                cloudpickle.dump(self, f)
        except Exception as e:
            raise RuntimeError(
                f"Saving failed with error: {e}. Please remove the non-picklable attributes from your DSPy program, "
                "or consider using state-only saving by setting `save_program=False`."
            )
        with open(path / "metadata.json", "wb") as f:
            f.write(orjson.dumps(metadata, option=orjson.OPT_INDENT_2 | orjson.OPT_APPEND_NEWLINE))

        return

    if path.suffix == ".json":
        state = self.dump_state()
        state["metadata"] = metadata
        try:
            with open(path, "wb") as f:
                f.write(orjson.dumps(state, option=orjson.OPT_INDENT_2 | orjson.OPT_APPEND_NEWLINE))
        except Exception as e:
            raise RuntimeError(
                f"Failed to save state to {path} with error: {e}. Your DSPy program may contain non "
                "json-serializable objects, please consider saving the state in .pkl by using `path` ending "
                "with `.pkl`, or saving the whole program by setting `save_program=True`."
            )
    elif path.suffix == ".pkl":
        logger.warning("Loading untrusted .pkl files can run arbitrary code, which may be dangerous. To avoid "
                      'this, prefer saving using json format using module.save("module.json").')
        state = self.dump_state(json_mode=False)
        state["metadata"] = metadata
        with open(path, "wb") as f:
            cloudpickle.dump(state, f)
    else:
        raise ValueError(f"`path` must end with `.json` or `.pkl` when `save_program=False`, but received: {path}")
```

#### `set_lm(lm)` [¶](#dspy.Refine.set_lm "Permanent link")

Source code in `dspy/primitives/module.py`

```
defset_lm(self, lm):
    for _, param in self.named_predictors():
        param.lm = lm
```

:::