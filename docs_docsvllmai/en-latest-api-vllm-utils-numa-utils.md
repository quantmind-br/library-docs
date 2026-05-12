---
title: numa_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/utils/numa_utils/
source: sitemap
fetched_at: 2026-05-07T21:38:49.310500472-03:00
rendered_js: false
word_count: 119
summary: This document provides an API reference for NUMA binding utilities in vLLM, detailing functions for GPU-to-NUMA node detection, subprocess configuration with numactl wrappers, and affinity state management.
tags:
    - numa
    - vllm
    - cpu-affinity
    - memory-policy
    - gpu-optimization
    - distributed-computing
category: api
---

NUMA binding utilities for vLLM worker processes.

Adapted in part from SGLang's NUMA helper implementation: https://github.com/sgl-project/sglang/blob/ba6d54d0f08f82f42b8224908ae2459a496b31b3/python/sglang/srt/utils/numa\_utils.py

## \_can\_set\_mempolicy [¶](#vllm.utils.numa_utils._can_set_mempolicy "Permanent link")

```
_can_set_mempolicy() -> bool
```

Check whether the current process can use NUMA memory policy syscalls.

Source code in `vllm/utils/numa_utils.py`

```
def_can_set_mempolicy() -> bool:
"""Check whether the current process can use NUMA memory policy syscalls."""
    try:
        libnuma = get_libnuma()
        if libnuma is None or libnuma.numa_available() < 0:
            return False
        mode = ctypes.c_int()
        ret = libnuma.get_mempolicy(
            ctypes.byref(mode), None, ctypes.c_ulong(0), None, ctypes.c_ulong(0)
        )
        return ret == 0
    except Exception:
        return False
```

## \_get\_gpu\_index [¶](#vllm.utils.numa_utils._get_gpu_index "Permanent link")

```
_get_gpu_index(
    parallel_config,
    local_rank: int,
    dp_local_rank: int | None = None,
) -> int
```

Compute the physical GPU index used for NUMA lookup.

Source code in `vllm/utils/numa_utils.py`

```
def_get_gpu_index(
    parallel_config, local_rank: int, dp_local_rank: int | None = None
) -> int:
"""Compute the physical GPU index used for NUMA lookup."""
    if (
        parallel_config.distributed_executor_backend not in ("ray", "external_launcher")
        and parallel_config.data_parallel_backend != "ray"
        and parallel_config.nnodes_within_dp == 1
    ):
        if dp_local_rank is None:
            dp_local_rank = parallel_config.data_parallel_rank_local
            if dp_local_rank is None:
                dp_local_rank = parallel_config.data_parallel_index

        tp_pp_world_size = (
            parallel_config.pipeline_parallel_size
            * parallel_config.tensor_parallel_size
        )
        return local_rank + dp_local_rank * tp_pp_world_size

    return local_rank
```

## \_get\_numactl\_executable [¶](#vllm.utils.numa_utils._get_numactl_executable "Permanent link")

Return the fixed wrapper executable used to launch numactl.

Source code in `vllm/utils/numa_utils.py`

```
def_get_numactl_executable() -> tuple[str, str]:
"""Return the fixed wrapper executable used to launch numactl."""
    fromshutilimport which

    if which("numactl") is None:
        raise RuntimeError(
            "numactl is required for NUMA binding but is not installed or "
            "not available on PATH."
        )

    script_path = Path(__file__).with_name("numa_wrapper.sh")
    return str(script_path), f"{script_path} via {_NUMACTL_ARGS_ENV}"
```

## \_is\_auto\_numa\_available [¶](#vllm.utils.numa_utils._is_auto_numa_available "Permanent link")

```
_is_auto_numa_available() -> bool
```

Check whether automatic GPU-to-NUMA detection should be attempted.

Source code in `vllm/utils/numa_utils.py`

```
def_is_auto_numa_available() -> bool:
"""Check whether automatic GPU-to-NUMA detection should be attempted."""
    fromvllm.platformsimport current_platform

    if not current_platform.is_cuda_alike():
        return False

    if not os.path.isdir("/sys/devices/system/node/node1"):
        return False

    try:
        process = psutil.Process(os.getpid())
        cpu_affinity = process.cpu_affinity()
        cpu_count = psutil.cpu_count()
        if cpu_count is not None and cpu_affinity != list(range(cpu_count)):
            logger.warning(
                "CPU affinity is already constrained for this process. "
                "Skipping automatic NUMA binding; pass --numa-bind-nodes "
                "explicitly to override."
            )
            return False
    except (AttributeError, NotImplementedError, psutil.Error):
        pass

    if not _can_set_mempolicy():
        logger.warning(
            "User lacks permission to set NUMA memory policy. "
            "Automatic NUMA detection may not work; if you are using Docker, "
            "try adding --cap-add SYS_NICE."
        )
        return False

    if not hasattr(current_platform, "get_all_device_numa_nodes"):
        logger.warning(
            "Platform %s does not support automatic NUMA detection",
            type(current_platform).__name__,
        )
        return False

    return True
```

## configure\_subprocess [¶](#vllm.utils.numa_utils.configure_subprocess "Permanent link")

```
configure_subprocess(
    vllm_config: VllmConfig,
    local_rank: int,
    dp_local_rank: int | None = None,
    process_kind: str = "worker",
)
```

Temporarily replace the multiprocessing executable with a numactl wrapper.

Source code in `vllm/utils/numa_utils.py`

```
@contextmanager
defconfigure_subprocess(
    vllm_config: "VllmConfig",
    local_rank: int,
    dp_local_rank: int | None = None,
    process_kind: str = "worker",
):
"""Temporarily replace the multiprocessing executable with a numactl wrapper."""
    numactl_args = _get_numactl_args(
        vllm_config, local_rank, dp_local_rank, process_kind
    )
    if numactl_args is None:
        yield
        return

    executable, debug_str = _get_numactl_executable()
    python_executable = os.fsdecode(multiprocessing.spawn.get_executable())
    with (
        _set_numa_wrapper_env(numactl_args, python_executable),
        _mp_set_executable(executable, debug_str),
    ):
        yield
```

## get\_auto\_numa\_nodes `cached` [¶](#vllm.utils.numa_utils.get_auto_numa_nodes "Permanent link")

```
get_auto_numa_nodes() -> list[int] | None
```

Auto-detect NUMA nodes for all visible GPUs.

Source code in `vllm/utils/numa_utils.py`

```
@cache
defget_auto_numa_nodes() -> list[int] | None:
"""Auto-detect NUMA nodes for all visible GPUs."""
    fromvllm.platformsimport current_platform

    if not _is_auto_numa_available():
        return None

    numa_nodes = current_platform.get_all_device_numa_nodes()
    if numa_nodes is not None:
        logger.info("Auto-detected NUMA nodes for GPUs: %s", numa_nodes)
    return numa_nodes
```

## log\_current\_affinity\_state [¶](#vllm.utils.numa_utils.log_current_affinity_state "Permanent link")

```
log_current_affinity_state(label: str) -> None
```

Log the process's effective NUMA affinity state.

Source code in `vllm/utils/numa_utils.py`

```
deflog_current_affinity_state(label: str) -> None:
"""Log the process's effective NUMA affinity state."""
    _log_numactl_show(label)
```