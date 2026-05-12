---
title: worker_base - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/worker/worker_base/
source: sitemap
fetched_at: 2026-05-07T21:43:18.925410668-03:00
rendered_js: false
word_count: 461
summary: The WorkerBase class defines a standardized interface for vLLM workers to manage hardware abstraction, distributed communication, and model execution lifecycle.
tags:
    - vllm
    - worker-interface
    - distributed-computing
    - hardware-abstraction
    - model-execution
category: reference
---

## WorkerBase [¶](#vllm.v1.worker.worker_base.WorkerBase "Permanent link")

Worker interface that allows vLLM to cleanly separate implementations for different hardware. Also abstracts control plane communication, e.g., to communicate request metadata to other workers.

Source code in `vllm/v1/worker/worker_base.py`

```
classWorkerBase:
"""Worker interface that allows vLLM to cleanly separate implementations for
    different hardware. Also abstracts control plane communication, e.g., to
    communicate request metadata to other workers.
    """

    def__init__(
        self,
        vllm_config: VllmConfig,
        local_rank: int,
        rank: int,
        distributed_init_method: str,
        is_driver_worker: bool = False,
    ) -> None:
"""
        Initialize common worker components.

        Args:
            vllm_config: Complete vLLM configuration
            local_rank: Local device index
            rank: Global rank in distributed setup
            distributed_init_method: Distributed initialization method
            is_driver_worker: Whether this worker handles driver
                responsibilities
        """
        self.vllm_config = vllm_config
        self.model_config = vllm_config.model_config
        self.cache_config = vllm_config.cache_config
        self.lora_config = vllm_config.lora_config
        self.load_config = vllm_config.load_config
        self.parallel_config = vllm_config.parallel_config
        self.scheduler_config = vllm_config.scheduler_config
        self.device_config = vllm_config.device_config
        self.speculative_config = vllm_config.speculative_config
        self.observability_config = vllm_config.observability_config
        self.kv_transfer_config = vllm_config.kv_transfer_config
        self.compilation_config = vllm_config.compilation_config

        fromvllm.platformsimport current_platform

        self.current_platform = current_platform

        self.parallel_config.rank = rank
        self.local_rank = local_rank
        self.rank = rank
        self.distributed_init_method = distributed_init_method
        self.is_driver_worker = is_driver_worker

        # Device and model state
        self.device: torch.device | None = None
        self.model_runner: nn.Module | None = None

    defget_kv_cache_spec(self) -> dict[str, KVCacheSpec]:
"""Get specifications for KV cache implementation."""
        raise NotImplementedError

    defcompile_or_warm_up_model(self) -> CompilationTimes:
"""Prepare model for execution through compilation/warmup.

        Returns:
            Compilation times (language_model, encoder) in seconds.
        """
        raise NotImplementedError

    defcheck_health(self) -> None:
"""Basic health check (override for device-specific checks)."""
        return

    definit_device(self) -> None:
"""Initialize device state, such as loading the model or other on-device
        memory allocations.
        """
        raise NotImplementedError

    defreset_mm_cache(self) -> None:
        reset_fn = getattr(self.model_runner, "reset_mm_cache", None)
        if callable(reset_fn):
            reset_fn()

    defget_model(self) -> nn.Module:
        raise NotImplementedError

    defapply_model(self, fn: Callable[[nn.Module], _R]) -> _R:
"""Apply a function on the model inside this worker."""
        return fn(self.get_model())

    defget_model_inspection(self) -> str:
"""Return a transformers-style hierarchical view of the model."""
        fromvllm.model_inspectionimport format_model_inspection

        return format_model_inspection(self.get_model())

    defload_model(self, *, load_dummy_weights: bool = False) -> None:
"""Load model onto target device."""
        raise NotImplementedError

    defexecute_model(
        self, scheduler_output: SchedulerOutput
    ) -> ModelRunnerOutput | AsyncModelRunnerOutput | None:
"""If this method returns None, sample_tokens should be called immediately after
        to obtain the ModelRunnerOutput.

        Note that this design may be changed in future if/when structured outputs
        parallelism is re-architected.
        """
        raise NotImplementedError

    defsample_tokens(
        self, grammar_output: GrammarOutput
    ) -> ModelRunnerOutput | AsyncModelRunnerOutput:
"""Should be called immediately after execute_model iff it returned None."""
        raise NotImplementedError

    defget_cache_block_size_bytes(self) -> int:
"""Return the size of a single cache block, in bytes. Used in
        speculative decoding.
        """
        raise NotImplementedError

    defadd_lora(self, lora_request: LoRARequest) -> bool:
        raise NotImplementedError

    defremove_lora(self, lora_id: int) -> bool:
        raise NotImplementedError

    defpin_lora(self, lora_id: int) -> bool:
        raise NotImplementedError

    deflist_loras(self) -> set[int]:
        raise NotImplementedError

    @property
    defvocab_size(self) -> int:
"""Get vocabulary size from model configuration."""
        return self.model_config.get_vocab_size()

    defshutdown(self) -> None:
"""Clean up resources held by the worker."""
        return
```

### vocab\_size `property` [¶](#vllm.v1.worker.worker_base.WorkerBase.vocab_size "Permanent link")

Get vocabulary size from model configuration.

### \_\_init\__ [¶](#vllm.v1.worker.worker_base.WorkerBase.__init__ "Permanent link")

```
__init__(
    vllm_config: VllmConfig,
    local_rank: int,
    rank: int,
    distributed_init_method: str,
    is_driver_worker: bool = False,
) -> None
```

Initialize common worker components.

Parameters:

Name Type Description Default `vllm_config` `VllmConfig`

Complete vLLM configuration

*required* `local_rank` `int`

Local device index

*required* `rank` `int`

Global rank in distributed setup

*required* `distributed_init_method` `str`

Distributed initialization method

*required* `is_driver_worker` `bool`

Whether this worker handles driver responsibilities

`False`

Source code in `vllm/v1/worker/worker_base.py`

```
def__init__(
    self,
    vllm_config: VllmConfig,
    local_rank: int,
    rank: int,
    distributed_init_method: str,
    is_driver_worker: bool = False,
) -> None:
"""
    Initialize common worker components.

    Args:
        vllm_config: Complete vLLM configuration
        local_rank: Local device index
        rank: Global rank in distributed setup
        distributed_init_method: Distributed initialization method
        is_driver_worker: Whether this worker handles driver
            responsibilities
    """
    self.vllm_config = vllm_config
    self.model_config = vllm_config.model_config
    self.cache_config = vllm_config.cache_config
    self.lora_config = vllm_config.lora_config
    self.load_config = vllm_config.load_config
    self.parallel_config = vllm_config.parallel_config
    self.scheduler_config = vllm_config.scheduler_config
    self.device_config = vllm_config.device_config
    self.speculative_config = vllm_config.speculative_config
    self.observability_config = vllm_config.observability_config
    self.kv_transfer_config = vllm_config.kv_transfer_config
    self.compilation_config = vllm_config.compilation_config

    fromvllm.platformsimport current_platform

    self.current_platform = current_platform

    self.parallel_config.rank = rank
    self.local_rank = local_rank
    self.rank = rank
    self.distributed_init_method = distributed_init_method
    self.is_driver_worker = is_driver_worker

    # Device and model state
    self.device: torch.device | None = None
    self.model_runner: nn.Module | None = None
```

### apply\_model [¶](#vllm.v1.worker.worker_base.WorkerBase.apply_model "Permanent link")

Apply a function on the model inside this worker.

Source code in `vllm/v1/worker/worker_base.py`

```
defapply_model(self, fn: Callable[[nn.Module], _R]) -> _R:
"""Apply a function on the model inside this worker."""
    return fn(self.get_model())
```

### check\_health [¶](#vllm.v1.worker.worker_base.WorkerBase.check_health "Permanent link")

Basic health check (override for device-specific checks).

Source code in `vllm/v1/worker/worker_base.py`

```
defcheck_health(self) -> None:
"""Basic health check (override for device-specific checks)."""
    return
```

### compile\_or\_warm\_up\_model [¶](#vllm.v1.worker.worker_base.WorkerBase.compile_or_warm_up_model "Permanent link")

```
compile_or_warm_up_model() -> CompilationTimes
```

Prepare model for execution through compilation/warmup.

Returns:

Type Description `CompilationTimes`

Compilation times (language\_model, encoder) in seconds.

Source code in `vllm/v1/worker/worker_base.py`

```
defcompile_or_warm_up_model(self) -> CompilationTimes:
"""Prepare model for execution through compilation/warmup.

    Returns:
        Compilation times (language_model, encoder) in seconds.
    """
    raise NotImplementedError
```

### execute\_model [¶](#vllm.v1.worker.worker_base.WorkerBase.execute_model "Permanent link")

If this method returns None, sample\_tokens should be called immediately after to obtain the ModelRunnerOutput.

Note that this design may be changed in future if/when structured outputs parallelism is re-architected.

Source code in `vllm/v1/worker/worker_base.py`

```
defexecute_model(
    self, scheduler_output: SchedulerOutput
) -> ModelRunnerOutput | AsyncModelRunnerOutput | None:
"""If this method returns None, sample_tokens should be called immediately after
    to obtain the ModelRunnerOutput.

    Note that this design may be changed in future if/when structured outputs
    parallelism is re-architected.
    """
    raise NotImplementedError
```

### get\_cache\_block\_size\_bytes [¶](#vllm.v1.worker.worker_base.WorkerBase.get_cache_block_size_bytes "Permanent link")

```
get_cache_block_size_bytes() -> int
```

Return the size of a single cache block, in bytes. Used in speculative decoding.

Source code in `vllm/v1/worker/worker_base.py`

```
defget_cache_block_size_bytes(self) -> int:
"""Return the size of a single cache block, in bytes. Used in
    speculative decoding.
    """
    raise NotImplementedError
```

### get\_kv\_cache\_spec [¶](#vllm.v1.worker.worker_base.WorkerBase.get_kv_cache_spec "Permanent link")

Get specifications for KV cache implementation.

Source code in `vllm/v1/worker/worker_base.py`

```
defget_kv_cache_spec(self) -> dict[str, KVCacheSpec]:
"""Get specifications for KV cache implementation."""
    raise NotImplementedError
```

### get\_model\_inspection [¶](#vllm.v1.worker.worker_base.WorkerBase.get_model_inspection "Permanent link")

```
get_model_inspection() -> str
```

Return a transformers-style hierarchical view of the model.

Source code in `vllm/v1/worker/worker_base.py`

```
defget_model_inspection(self) -> str:
"""Return a transformers-style hierarchical view of the model."""
    fromvllm.model_inspectionimport format_model_inspection

    return format_model_inspection(self.get_model())
```

### init\_device [¶](#vllm.v1.worker.worker_base.WorkerBase.init_device "Permanent link")

Initialize device state, such as loading the model or other on-device memory allocations.

Source code in `vllm/v1/worker/worker_base.py`

```
definit_device(self) -> None:
"""Initialize device state, such as loading the model or other on-device
    memory allocations.
    """
    raise NotImplementedError
```

### load\_model [¶](#vllm.v1.worker.worker_base.WorkerBase.load_model "Permanent link")

```
load_model(*, load_dummy_weights: bool = False) -> None
```

Load model onto target device.

Source code in `vllm/v1/worker/worker_base.py`

```
defload_model(self, *, load_dummy_weights: bool = False) -> None:
"""Load model onto target device."""
    raise NotImplementedError
```

### sample\_tokens [¶](#vllm.v1.worker.worker_base.WorkerBase.sample_tokens "Permanent link")

Should be called immediately after execute\_model iff it returned None.

Source code in `vllm/v1/worker/worker_base.py`

```
defsample_tokens(
    self, grammar_output: GrammarOutput
) -> ModelRunnerOutput | AsyncModelRunnerOutput:
"""Should be called immediately after execute_model iff it returned None."""
    raise NotImplementedError
```

### shutdown [¶](#vllm.v1.worker.worker_base.WorkerBase.shutdown "Permanent link")

Clean up resources held by the worker.

Source code in `vllm/v1/worker/worker_base.py`

```
defshutdown(self) -> None:
"""Clean up resources held by the worker."""
    return
```

## WorkerWrapperBase [¶](#vllm.v1.worker.worker_base.WorkerWrapperBase "Permanent link")

This class represents one process in an executor/engine. It is responsible for lazily initializing the worker and handling the worker's lifecycle. We first instantiate the WorkerWrapper, which remembers the worker module and class name. Then, when we call `update_environment_variables`, and the real initialization happens in `init_worker`.

Source code in `vllm/v1/worker/worker_base.py`

```
classWorkerWrapperBase:
"""
    This class represents one process in an executor/engine. It is responsible
    for lazily initializing the worker and handling the worker's lifecycle.
    We first instantiate the WorkerWrapper, which remembers the worker module
    and class name. Then, when we call `update_environment_variables`, and the
    real initialization happens in `init_worker`.
    """

    def__init__(
        self,
        rpc_rank: int = 0,
        global_rank: int | None = None,
    ) -> None:
"""
        Initialize the worker wrapper with the given vllm_config and rpc_rank.
        Note: rpc_rank is the rank of the worker in the executor. In most cases,
        it is also the rank of the worker in the distributed group. However,
        when multiple executors work together, they can be different.
        e.g. in the case of SPMD-style offline inference with TP=2,
        users can launch 2 engines/executors, each with only 1 worker.
        All workers have rpc_rank=0, but they have different ranks in the TP
        group.
        """
        self.rpc_rank: int = rpc_rank
        self.global_rank: int = self.rpc_rank if global_rank is None else global_rank

        # Initialized after init_worker is called
        self.worker: WorkerBase
        self.vllm_config: VllmConfig

    defshutdown(self) -> None:
        if self.worker is not None:
            self.worker.shutdown()

    defupdate_environment_variables(
        self,
        envs_list: list[dict[str, str]],
    ) -> None:
        envs = envs_list[self.rpc_rank]
        update_environment_variables(envs)

    @instrument(span_name="Worker init")
    definit_worker(self, all_kwargs: list[dict[str, Any]]) -> None:
"""
        Here we inject some common logic before initializing the worker.
        Arguments are passed to the worker class constructor.
        """
        kwargs = all_kwargs[self.rpc_rank]

        vllm_config: VllmConfig | None = kwargs.get("vllm_config")
        assert vllm_config is not None, (
            "vllm_config is required to initialize the worker"
        )
        self.vllm_config = vllm_config

        vllm_config.enable_trace_function_call_for_thread()

        fromvllm.pluginsimport load_general_plugins

        load_general_plugins()

        parallel_config = vllm_config.parallel_config
        if isinstance(parallel_config.worker_cls, str):
            worker_class: type[WorkerBase] = resolve_obj_by_qualname(
                parallel_config.worker_cls
            )
        else:
            raise ValueError(
                "passing worker_cls is no longer supported. "
                "Please pass keep the class in a separate module "
                "and pass the qualified name of the class as a string."
            )

        if parallel_config.worker_extension_cls:
            worker_extension_cls = resolve_obj_by_qualname(
                parallel_config.worker_extension_cls
            )
            extended_calls = []
            if worker_extension_cls not in worker_class.__bases__:
                # check any conflicts between worker and worker_extension_cls
                for attr in dir(worker_extension_cls):
                    if attr.startswith("__"):
                        continue
                    assert not hasattr(worker_class, attr), (
                        f"Worker class {worker_class} already has an attribute"
                        f" {attr}, which conflicts with the worker"
                        f" extension class {worker_extension_cls}."
                    )
                    if callable(getattr(worker_extension_cls, attr)):
                        extended_calls.append(attr)
                # dynamically inherit the worker extension class
                worker_class.__bases__ = worker_class.__bases__ + (
                    worker_extension_cls,
                )
                logger.info(
                    "Injected %s into %s for extended collective_rpc calls %s",
                    worker_extension_cls,
                    worker_class,
                    extended_calls,
                )

        shared_worker_lock = kwargs.pop("shared_worker_lock", None)
        if shared_worker_lock is None:
            msg = (
                "Missing `shared_worker_lock` argument from executor. "
                "This argument is needed for mm_processor_cache_type='shm'."
            )

            mm_config = vllm_config.model_config.multimodal_config
            if mm_config and mm_config.mm_processor_cache_type == "shm":
                raise ValueError(msg)
            else:
                logger.warning_once(msg)

            self.mm_receiver_cache = None
        else:
            self.mm_receiver_cache = (
                MULTIMODAL_REGISTRY.worker_receiver_cache_from_config(
                    vllm_config,
                    shared_worker_lock,
                )
            )

        with set_current_vllm_config(self.vllm_config):
            # To make vLLM config available during worker initialization
            self.worker = worker_class(**kwargs)

    definitialize_from_config(self, kv_cache_configs: list[Any]) -> None:
        kv_cache_config = kv_cache_configs[self.global_rank]
        assert self.vllm_config is not None
        with set_current_vllm_config(self.vllm_config):
            self.worker.initialize_from_config(kv_cache_config)  # type: ignore

    definit_device(self):
        assert self.vllm_config is not None
        with set_current_vllm_config(self.vllm_config):
            # To make vLLM config available during device initialization
            self.worker.init_device()  # type: ignore

    def__getattr__(self, attr: str):
        return getattr(self.worker, attr)

    def_apply_mm_cache(self, scheduler_output: SchedulerOutput) -> None:
        mm_cache = self.mm_receiver_cache
        if mm_cache is None:
            return

        for req_data in scheduler_output.scheduled_new_reqs:
            req_data.mm_features = mm_cache.get_and_update_features(
                req_data.mm_features
            )

    defexecute_model(
        self, scheduler_output: SchedulerOutput
    ) -> ModelRunnerOutput | AsyncModelRunnerOutput | None:
        self._apply_mm_cache(scheduler_output)

        return self.worker.execute_model(scheduler_output)

    defreset_mm_cache(self) -> None:
        mm_receiver_cache = self.mm_receiver_cache
        if mm_receiver_cache is not None:
            mm_receiver_cache.clear_cache()

        self.worker.reset_mm_cache()
```

### \_\_init\__ [¶](#vllm.v1.worker.worker_base.WorkerWrapperBase.__init__ "Permanent link")

```
__init__(
    rpc_rank: int = 0, global_rank: int | None = None
) -> None
```

Initialize the worker wrapper with the given vllm\_config and rpc\_rank. Note: rpc\_rank is the rank of the worker in the executor. In most cases, it is also the rank of the worker in the distributed group. However, when multiple executors work together, they can be different. e.g. in the case of SPMD-style offline inference with TP=2, users can launch 2 engines/executors, each with only 1 worker. All workers have rpc\_rank=0, but they have different ranks in the TP group.

Source code in `vllm/v1/worker/worker_base.py`

```
def__init__(
    self,
    rpc_rank: int = 0,
    global_rank: int | None = None,
) -> None:
"""
    Initialize the worker wrapper with the given vllm_config and rpc_rank.
    Note: rpc_rank is the rank of the worker in the executor. In most cases,
    it is also the rank of the worker in the distributed group. However,
    when multiple executors work together, they can be different.
    e.g. in the case of SPMD-style offline inference with TP=2,
    users can launch 2 engines/executors, each with only 1 worker.
    All workers have rpc_rank=0, but they have different ranks in the TP
    group.
    """
    self.rpc_rank: int = rpc_rank
    self.global_rank: int = self.rpc_rank if global_rank is None else global_rank

    # Initialized after init_worker is called
    self.worker: WorkerBase
    self.vllm_config: VllmConfig
```

### init\_worker [¶](#vllm.v1.worker.worker_base.WorkerWrapperBase.init_worker "Permanent link")

Here we inject some common logic before initializing the worker. Arguments are passed to the worker class constructor.

Source code in `vllm/v1/worker/worker_base.py`

```
@instrument(span_name="Worker init")
definit_worker(self, all_kwargs: list[dict[str, Any]]) -> None:
"""
    Here we inject some common logic before initializing the worker.
    Arguments are passed to the worker class constructor.
    """
    kwargs = all_kwargs[self.rpc_rank]

    vllm_config: VllmConfig | None = kwargs.get("vllm_config")
    assert vllm_config is not None, (
        "vllm_config is required to initialize the worker"
    )
    self.vllm_config = vllm_config

    vllm_config.enable_trace_function_call_for_thread()

    fromvllm.pluginsimport load_general_plugins

    load_general_plugins()

    parallel_config = vllm_config.parallel_config
    if isinstance(parallel_config.worker_cls, str):
        worker_class: type[WorkerBase] = resolve_obj_by_qualname(
            parallel_config.worker_cls
        )
    else:
        raise ValueError(
            "passing worker_cls is no longer supported. "
            "Please pass keep the class in a separate module "
            "and pass the qualified name of the class as a string."
        )

    if parallel_config.worker_extension_cls:
        worker_extension_cls = resolve_obj_by_qualname(
            parallel_config.worker_extension_cls
        )
        extended_calls = []
        if worker_extension_cls not in worker_class.__bases__:
            # check any conflicts between worker and worker_extension_cls
            for attr in dir(worker_extension_cls):
                if attr.startswith("__"):
                    continue
                assert not hasattr(worker_class, attr), (
                    f"Worker class {worker_class} already has an attribute"
                    f" {attr}, which conflicts with the worker"
                    f" extension class {worker_extension_cls}."
                )
                if callable(getattr(worker_extension_cls, attr)):
                    extended_calls.append(attr)
            # dynamically inherit the worker extension class
            worker_class.__bases__ = worker_class.__bases__ + (
                worker_extension_cls,
            )
            logger.info(
                "Injected %s into %s for extended collective_rpc calls %s",
                worker_extension_cls,
                worker_class,
                extended_calls,
            )

    shared_worker_lock = kwargs.pop("shared_worker_lock", None)
    if shared_worker_lock is None:
        msg = (
            "Missing `shared_worker_lock` argument from executor. "
            "This argument is needed for mm_processor_cache_type='shm'."
        )

        mm_config = vllm_config.model_config.multimodal_config
        if mm_config and mm_config.mm_processor_cache_type == "shm":
            raise ValueError(msg)
        else:
            logger.warning_once(msg)

        self.mm_receiver_cache = None
    else:
        self.mm_receiver_cache = (
            MULTIMODAL_REGISTRY.worker_receiver_cache_from_config(
                vllm_config,
                shared_worker_lock,
            )
        )

    with set_current_vllm_config(self.vllm_config):
        # To make vLLM config available during worker initialization
        self.worker = worker_class(**kwargs)
```