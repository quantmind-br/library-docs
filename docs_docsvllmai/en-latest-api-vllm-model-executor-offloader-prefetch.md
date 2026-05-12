---
title: prefetch - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/offloader/prefetch/
source: sitemap
fetched_at: 2026-05-07T21:33:53.324011089-03:00
rendered_js: false
word_count: 1302
summary: This document describes a prefetch-based CPU offloading system that utilizes static buffers and asynchronous host-to-device transfers to hide latency in deep learning models while maintaining compatibility with torch.compile and CUDA graphs.
tags:
    - cpu-offloading
    - prefetching
    - cuda-graphs
    - torch-compile
    - memory-management
    - gpu-acceleration
category: concept
---

Prefetch-based CPU offloading with async prefetching.

Uses static buffers and event-based stream forking for torch.compile + CUDA graph compatibility. Events allow the copy stream to join CUDA graph captures, ensuring H2D copies are properly captured.

## ParamInfo `dataclass` [¶](#vllm.model_executor.offloader.prefetch.ParamInfo "Permanent link")

Metadata about an offloaded parameter.

Source code in `vllm/model_executor/offloader/prefetch.py`

```
@dataclass
classParamInfo:
"""Metadata about an offloaded parameter."""

    name: str
    shape: tuple[int, ...]
    stride: tuple[int, ...]
    dtype: torch.dtype

    @property
    defkey(self) -> tuple[str, tuple[int, ...], tuple[int, ...], torch.dtype]:
"""Unique key for buffer pool grouping.

        Includes parameter name to prevent different parameters with the same
        shape from sharing buffers within the same layer. Parameters with the
        same name across different layers will share buffers (via slots).

        Includes stride because parameters with same shape but different
        strides need separate buffers to preserve memory layout.
        """
        return (self.name, self.shape, self.stride, self.dtype)

    @property
    defnum_bytes(self) -> int:
"""Size in bytes."""
        numel = 1
        for dim in self.shape:
            numel *= dim
        return numel * get_dtype_size(self.dtype)
```

### key `property` [¶](#vllm.model_executor.offloader.prefetch.ParamInfo.key "Permanent link")

Unique key for buffer pool grouping.

Includes parameter name to prevent different parameters with the same shape from sharing buffers within the same layer. Parameters with the same name across different layers will share buffers (via slots).

Includes stride because parameters with same shape but different strides need separate buffers to preserve memory layout.

### num\_bytes `property` [¶](#vllm.model_executor.offloader.prefetch.ParamInfo.num_bytes "Permanent link")

Size in bytes.

## PrefetchOffloader [¶](#vllm.model_executor.offloader.prefetch.PrefetchOffloader "Permanent link")

Bases: `BaseOffloader`

Prefetching-based offloader with group-based layer selection.

Groups layers and uses async H2D prefetch to hide transfer latency. Uses static buffers and stream synchronization for torch.compile and CUDA graph compatibility.

Parameters:

Name Type Description Default `group_size` `int`

Group every N layers together.

*required* `num_in_group` `int`

Offload this many layers per group (last N of each group).

*required* `prefetch_step` `int`

Number of layers to prefetch ahead.

*required* `mode` `str`

Offload mode ("cpu" is currently supported).

`'cpu'`

Source code in `vllm/model_executor/offloader/prefetch.py`

```
classPrefetchOffloader(BaseOffloader):
"""Prefetching-based offloader with group-based layer selection.

    Groups layers and uses async H2D prefetch to hide transfer latency.
    Uses static buffers and stream synchronization for torch.compile and
    CUDA graph compatibility.

    Args:
        group_size: Group every N layers together.
        num_in_group: Offload this many layers per group (last N of each group).
        prefetch_step: Number of layers to prefetch ahead.
        mode: Offload mode ("cpu" is currently supported).
    """

    def__init__(
        self,
        group_size: int,
        num_in_group: int,
        prefetch_step: int,
        offload_params: set[str] | None = None,
        mode: str = "cpu",
    ):
        self.group_size = group_size
        self.num_in_group = num_in_group
        self.prefetch_step = prefetch_step
        self.offload_params = offload_params or set()
        self.mode = mode

        # Copy stream for async H2D transfers
        self.copy_stream = torch.cuda.Stream()

        # Module offloaders and buffer pool (populated in wrap_modules/post_init)
        self.module_offloaders: list[_ModuleOffloader] = []
        self.buffer_pool: StaticBufferPool | None = None
        self.total_offloaded_bytes = 0

    defwrap_modules(
        self,
        modules_generator: Generator[nn.Module, None, None],
    ) -> list[nn.Module]:
"""Wrap modules with prefetch offloading logic."""
        assert len(self.module_offloaders) == 0, (
            "wrap_modules should only be called once"
        )

        all_modules = []
        offload_modules = []

        for module_index, module in enumerate(modules_generator):
            all_modules.append(module)

            # Select layers to offload based on group pattern
            # Offload last num_in_group layers of each group_size
            if module_index % self.group_size >= self.group_size - self.num_in_group:
                if self.offload_params:
                    whitelist = [
                        name
                        for name, _ in module.named_parameters()
                        if any(f".{p}." in f".{name}." for p in self.offload_params)
                    ]
                else:
                    whitelist = [name for name, _ in module.named_parameters()]

                if not whitelist:
                    continue  # skip layers with no matching params

                offload_modules.append(module)
                self.module_offloaders.append(
                    _ModuleOffloader(
                        mode=self.mode,
                        module=module,
                        copy_stream=self.copy_stream,
                        whitelist_param_names=whitelist,
                        layer_idx=len(self.module_offloaders),
                    )
                )

        for index, module in enumerate(offload_modules):
            self._hook_module_forward(index, module)

        return all_modules

    def_hook_module_forward(self, index: int, module: nn.Module):
"""Hook module's forward with torch.compile-compatible sync."""
        original_forward = module.forward

        defforward(*args, **kwargs):
            # Temporarily restore original forward to avoid recursion
            module.forward = original_forward

            # Wait for this layer's prefetch to complete
            # mutates_args on input_tensor creates data dependency for torch.compile
            input_tensor = args[0] if args else kwargs.get("hidden_states")
            torch.ops.vllm.wait_prefetch(input_tensor, index)

            # No parameter swapping needed - parameters already point to
            # GPU static buffers (set in assign_static_buffer)
            output = original_forward(*args, **kwargs)

            # Start prefetch for next layer (circular)
            # mutates_args on output_tensor creates ordering dependency
            next_index = (index + self.prefetch_step) % len(self.module_offloaders)
            # Handle tuple output (e.g., (hidden_states, residual))
            if isinstance(output, tuple):
                torch.ops.vllm.start_prefetch(output[0], next_index)
            else:
                torch.ops.vllm.start_prefetch(output, next_index)

            # No explicit offload needed - static buffers are reused implicitly

            # Restore hooked forward
            module.forward = forward
            return output

        module.forward = forward

    def_wait_for_layer(self, layer_idx: int):
"""Called by custom op - wait for copy to complete.

        Synchronization strategy:
        - During CUDA graph capture: use event-based wait (graph-compatible)
        - Outside capture (warmup/eager): use wait_stream (more robust)

        During capture, we skip wait for pre-capture prefetches because:
        1. sync_before_graph_capture() ensures pre-capture work is complete
        2. We can't wait on pre-capture events during capture (isolation error)
        """
        offloader = self.module_offloaders[layer_idx]

        if torch.cuda.is_current_stream_capturing():
            # During capture, skip wait for pre-capture prefetches.
            # sync_before_graph_capture() ensures pre-capture work is complete.
            if not offloader._prefetch_in_capture:
                return
            # Event-based wait for in-capture prefetches (graph-compatible)
            torch.cuda.current_stream().wait_event(offloader._copy_done_event)
            # Mark that this prefetch has been waited on (joined).
            offloader._prefetch_in_capture = False
        else:
            if offloader._event_valid_for_eager:
                # Use per-layer event to only wait for THIS layer's copy,
                # allowing other layers' prefetches to run concurrently.
                torch.cuda.current_stream().wait_event(offloader._copy_done_event)
            else:
                # Event not usable (unrecorded or recorded during capture).
                # Fall back to wait_stream to drain all copy_stream work.
                torch.cuda.current_stream().wait_stream(self.copy_stream)

    defsync_prev_onload(self):
"""Sync previous onload operations.

        Ensures any H2D copies in flight on copy_stream complete before
        the compute stream continues. Call this before CUDA graph
        capture/replay or when synchronization is needed.
        """
        torch.cuda.current_stream().wait_stream(self.copy_stream)

    def_start_prefetch(self, layer_idx: int):
"""Called by custom op - start async copy to static buffer."""
        offloader = self.module_offloaders[layer_idx]
        offloader.start_onload_to_static()

    defjoin_after_forward(self):
"""Join copy_stream after model forward completes.

        Call this after the model forward pass but before CUDA graph capture
        ends. This ensures copy_stream is rejoined for any prefetches started
        during the forward pass.

        We join ALL layers that have _prefetch_in_capture=True, meaning their
        prefetch was started during capture but not yet waited on (joined).
        This handles both full and piecewise cudagraph modes correctly:
        - Full mode: joins layers 0..prefetch_step-1 (prefetched by last layers)
        - Piecewise mode: joins only layers prefetched by THIS subgraph's layers
        """
        if not self.module_offloaders:
            return
        # Join all layers whose prefetch was started in capture but not waited on
        for offloader in self.module_offloaders:
            if offloader._prefetch_in_capture:
                torch.cuda.current_stream().wait_event(offloader._copy_done_event)
                offloader._prefetch_in_capture = False

    defpost_init(self):
"""Allocate static buffer pool and start initial prefetches.

        Note: Parameters have already been offloaded to CPU during wrap_modules()
        (in _CpuParamOffloader.__init__), so GPU memory is available for the
        static buffer pool.
        """
        # Sync CPU storage with current param.data BEFORE collecting param info.
        # This is needed because process_weights_after_loading may have:
        # 1. Transformed weights (quantization, transpose, etc.)
        # 2. Created new CPU tensors via device_loading_context
        # Our _cpu_storage would be stale otherwise.
        for offloader in self.module_offloaders:
            offloader.sync_cpu_storage()

        # Collect parameter info (now using synced CPU storage)
        param_infos: list[ParamInfo] = []
        device: torch.device | None = None

        for offloader in self.module_offloaders:
            param_infos.extend(offloader.get_param_infos())
            if device is None:
                device = offloader.device

        if device is None:
            # No modules to offload
            return

        # Allocate static buffer pool
        self.buffer_pool = StaticBufferPool(
            param_infos=param_infos,
            slot_capacity=self.prefetch_step,
            device=device,
        )

        # Assign buffer slots and point parameters to GPU buffers
        for idx, offloader in enumerate(self.module_offloaders):
            slot_idx = idx % self.prefetch_step
            offloader.assign_buffer_slot(self.buffer_pool, slot_idx)

        # Collect offloaded bytes
        for offloader in self.module_offloaders:
            offloader.post_init()
            self.total_offloaded_bytes += offloader.offloaded_bytes

        logger.info_once(
            f"[PrefetchOffloader] Initialized {len(self.module_offloaders)} modules. "
            f"Total GPU memory saved: {self.total_offloaded_bytes/1e9:.4f} GB, "
            f"Static buffer pool: {self.buffer_pool.total_bytes/1e9:.4f} GB "
            f"(group_size={self.group_size}, num_in_group={self.num_in_group}, "
            f"prefetch_step={self.prefetch_step}, mode={self.mode})"
        )

        # Start initial prefetches
        for i in range(min(self.prefetch_step, len(self.module_offloaders))):
            self.module_offloaders[i].start_onload_to_static()
```

### \_hook\_module\_forward [¶](#vllm.model_executor.offloader.prefetch.PrefetchOffloader._hook_module_forward "Permanent link")

```
_hook_module_forward(index: int, module: Module)
```

Hook module's forward with torch.compile-compatible sync.

Source code in `vllm/model_executor/offloader/prefetch.py`

```
def_hook_module_forward(self, index: int, module: nn.Module):
"""Hook module's forward with torch.compile-compatible sync."""
    original_forward = module.forward

    defforward(*args, **kwargs):
        # Temporarily restore original forward to avoid recursion
        module.forward = original_forward

        # Wait for this layer's prefetch to complete
        # mutates_args on input_tensor creates data dependency for torch.compile
        input_tensor = args[0] if args else kwargs.get("hidden_states")
        torch.ops.vllm.wait_prefetch(input_tensor, index)

        # No parameter swapping needed - parameters already point to
        # GPU static buffers (set in assign_static_buffer)
        output = original_forward(*args, **kwargs)

        # Start prefetch for next layer (circular)
        # mutates_args on output_tensor creates ordering dependency
        next_index = (index + self.prefetch_step) % len(self.module_offloaders)
        # Handle tuple output (e.g., (hidden_states, residual))
        if isinstance(output, tuple):
            torch.ops.vllm.start_prefetch(output[0], next_index)
        else:
            torch.ops.vllm.start_prefetch(output, next_index)

        # No explicit offload needed - static buffers are reused implicitly

        # Restore hooked forward
        module.forward = forward
        return output

    module.forward = forward
```

### \_start\_prefetch [¶](#vllm.model_executor.offloader.prefetch.PrefetchOffloader._start_prefetch "Permanent link")

```
_start_prefetch(layer_idx: int)
```

Called by custom op - start async copy to static buffer.

Source code in `vllm/model_executor/offloader/prefetch.py`

```
def_start_prefetch(self, layer_idx: int):
"""Called by custom op - start async copy to static buffer."""
    offloader = self.module_offloaders[layer_idx]
    offloader.start_onload_to_static()
```

### \_wait\_for\_layer [¶](#vllm.model_executor.offloader.prefetch.PrefetchOffloader._wait_for_layer "Permanent link")

```
_wait_for_layer(layer_idx: int)
```

Called by custom op - wait for copy to complete.

Synchronization strategy: - During CUDA graph capture: use event-based wait (graph-compatible) - Outside capture (warmup/eager): use wait\_stream (more robust)

During capture, we skip wait for pre-capture prefetches because: 1. sync\_before\_graph\_capture() ensures pre-capture work is complete 2. We can't wait on pre-capture events during capture (isolation error)

Source code in `vllm/model_executor/offloader/prefetch.py`

```
def_wait_for_layer(self, layer_idx: int):
"""Called by custom op - wait for copy to complete.

    Synchronization strategy:
    - During CUDA graph capture: use event-based wait (graph-compatible)
    - Outside capture (warmup/eager): use wait_stream (more robust)

    During capture, we skip wait for pre-capture prefetches because:
    1. sync_before_graph_capture() ensures pre-capture work is complete
    2. We can't wait on pre-capture events during capture (isolation error)
    """
    offloader = self.module_offloaders[layer_idx]

    if torch.cuda.is_current_stream_capturing():
        # During capture, skip wait for pre-capture prefetches.
        # sync_before_graph_capture() ensures pre-capture work is complete.
        if not offloader._prefetch_in_capture:
            return
        # Event-based wait for in-capture prefetches (graph-compatible)
        torch.cuda.current_stream().wait_event(offloader._copy_done_event)
        # Mark that this prefetch has been waited on (joined).
        offloader._prefetch_in_capture = False
    else:
        if offloader._event_valid_for_eager:
            # Use per-layer event to only wait for THIS layer's copy,
            # allowing other layers' prefetches to run concurrently.
            torch.cuda.current_stream().wait_event(offloader._copy_done_event)
        else:
            # Event not usable (unrecorded or recorded during capture).
            # Fall back to wait_stream to drain all copy_stream work.
            torch.cuda.current_stream().wait_stream(self.copy_stream)
```

### join\_after\_forward [¶](#vllm.model_executor.offloader.prefetch.PrefetchOffloader.join_after_forward "Permanent link")

Join copy\_stream after model forward completes.

Call this after the model forward pass but before CUDA graph capture ends. This ensures copy\_stream is rejoined for any prefetches started during the forward pass.

We join ALL layers that have \_prefetch\_in\_capture=True, meaning their prefetch was started during capture but not yet waited on (joined). This handles both full and piecewise cudagraph modes correctly: - Full mode: joins layers 0..prefetch\_step-1 (prefetched by last layers) - Piecewise mode: joins only layers prefetched by THIS subgraph's layers

Source code in `vllm/model_executor/offloader/prefetch.py`

```
defjoin_after_forward(self):
"""Join copy_stream after model forward completes.

    Call this after the model forward pass but before CUDA graph capture
    ends. This ensures copy_stream is rejoined for any prefetches started
    during the forward pass.

    We join ALL layers that have _prefetch_in_capture=True, meaning their
    prefetch was started during capture but not yet waited on (joined).
    This handles both full and piecewise cudagraph modes correctly:
    - Full mode: joins layers 0..prefetch_step-1 (prefetched by last layers)
    - Piecewise mode: joins only layers prefetched by THIS subgraph's layers
    """
    if not self.module_offloaders:
        return
    # Join all layers whose prefetch was started in capture but not waited on
    for offloader in self.module_offloaders:
        if offloader._prefetch_in_capture:
            torch.cuda.current_stream().wait_event(offloader._copy_done_event)
            offloader._prefetch_in_capture = False
```

### post\_init [¶](#vllm.model_executor.offloader.prefetch.PrefetchOffloader.post_init "Permanent link")

Allocate static buffer pool and start initial prefetches.

Note: Parameters have already been offloaded to CPU during wrap\_modules() (in \_CpuParamOffloader.**init**), so GPU memory is available for the static buffer pool.

Source code in `vllm/model_executor/offloader/prefetch.py`

```
defpost_init(self):
"""Allocate static buffer pool and start initial prefetches.

    Note: Parameters have already been offloaded to CPU during wrap_modules()
    (in _CpuParamOffloader.__init__), so GPU memory is available for the
    static buffer pool.
    """
    # Sync CPU storage with current param.data BEFORE collecting param info.
    # This is needed because process_weights_after_loading may have:
    # 1. Transformed weights (quantization, transpose, etc.)
    # 2. Created new CPU tensors via device_loading_context
    # Our _cpu_storage would be stale otherwise.
    for offloader in self.module_offloaders:
        offloader.sync_cpu_storage()

    # Collect parameter info (now using synced CPU storage)
    param_infos: list[ParamInfo] = []
    device: torch.device | None = None

    for offloader in self.module_offloaders:
        param_infos.extend(offloader.get_param_infos())
        if device is None:
            device = offloader.device

    if device is None:
        # No modules to offload
        return

    # Allocate static buffer pool
    self.buffer_pool = StaticBufferPool(
        param_infos=param_infos,
        slot_capacity=self.prefetch_step,
        device=device,
    )

    # Assign buffer slots and point parameters to GPU buffers
    for idx, offloader in enumerate(self.module_offloaders):
        slot_idx = idx % self.prefetch_step
        offloader.assign_buffer_slot(self.buffer_pool, slot_idx)

    # Collect offloaded bytes
    for offloader in self.module_offloaders:
        offloader.post_init()
        self.total_offloaded_bytes += offloader.offloaded_bytes

    logger.info_once(
        f"[PrefetchOffloader] Initialized {len(self.module_offloaders)} modules. "
        f"Total GPU memory saved: {self.total_offloaded_bytes/1e9:.4f} GB, "
        f"Static buffer pool: {self.buffer_pool.total_bytes/1e9:.4f} GB "
        f"(group_size={self.group_size}, num_in_group={self.num_in_group}, "
        f"prefetch_step={self.prefetch_step}, mode={self.mode})"
    )

    # Start initial prefetches
    for i in range(min(self.prefetch_step, len(self.module_offloaders))):
        self.module_offloaders[i].start_onload_to_static()
```

### sync\_prev\_onload [¶](#vllm.model_executor.offloader.prefetch.PrefetchOffloader.sync_prev_onload "Permanent link")

Sync previous onload operations.

Ensures any H2D copies in flight on copy\_stream complete before the compute stream continues. Call this before CUDA graph capture/replay or when synchronization is needed.

Source code in `vllm/model_executor/offloader/prefetch.py`

```
defsync_prev_onload(self):
"""Sync previous onload operations.

    Ensures any H2D copies in flight on copy_stream complete before
    the compute stream continues. Call this before CUDA graph
    capture/replay or when synchronization is needed.
    """
    torch.cuda.current_stream().wait_stream(self.copy_stream)
```

### wrap\_modules [¶](#vllm.model_executor.offloader.prefetch.PrefetchOffloader.wrap_modules "Permanent link")

Wrap modules with prefetch offloading logic.

Source code in `vllm/model_executor/offloader/prefetch.py`

```
defwrap_modules(
    self,
    modules_generator: Generator[nn.Module, None, None],
) -> list[nn.Module]:
"""Wrap modules with prefetch offloading logic."""
    assert len(self.module_offloaders) == 0, (
        "wrap_modules should only be called once"
    )

    all_modules = []
    offload_modules = []

    for module_index, module in enumerate(modules_generator):
        all_modules.append(module)

        # Select layers to offload based on group pattern
        # Offload last num_in_group layers of each group_size
        if module_index % self.group_size >= self.group_size - self.num_in_group:
            if self.offload_params:
                whitelist = [
                    name
                    for name, _ in module.named_parameters()
                    if any(f".{p}." in f".{name}." for p in self.offload_params)
                ]
            else:
                whitelist = [name for name, _ in module.named_parameters()]

            if not whitelist:
                continue  # skip layers with no matching params

            offload_modules.append(module)
            self.module_offloaders.append(
                _ModuleOffloader(
                    mode=self.mode,
                    module=module,
                    copy_stream=self.copy_stream,
                    whitelist_param_names=whitelist,
                    layer_idx=len(self.module_offloaders),
                )
            )

    for index, module in enumerate(offload_modules):
        self._hook_module_forward(index, module)

    return all_modules
```

## StaticBufferPool [¶](#vllm.model_executor.offloader.prefetch.StaticBufferPool "Permanent link")

Pre-allocated GPU buffer pool for offloaded parameters.

Allocates slot\_capacity copies of each unique parameter (name, shape, stride, dtype), allowing for double/triple buffering during prefetch.

Buffer slots are reused circularly: layer N uses slot (N % slot\_capacity).

The key includes parameter name to prevent different parameters within the same layer from sharing buffers. Parameters with the same name across different layers share buffers via the slot mechanism.

Source code in `vllm/model_executor/offloader/prefetch.py`

```
classStaticBufferPool:
"""Pre-allocated GPU buffer pool for offloaded parameters.

    Allocates slot_capacity copies of each unique parameter
    (name, shape, stride, dtype), allowing for double/triple buffering
    during prefetch.

    Buffer slots are reused circularly: layer N uses slot (N % slot_capacity).

    The key includes parameter name to prevent different parameters within
    the same layer from sharing buffers. Parameters with the same name
    across different layers share buffers via the slot mechanism.
    """

    def__init__(
        self,
        param_infos: list[ParamInfo],
        slot_capacity: int,
        device: torch.device,
    ):
        self.slot_capacity = slot_capacity
        self.total_bytes = 0
        self._device = device

        # Group by (shape, stride, dtype) - only allocate unique combinations
        unique_params: dict[tuple, ParamInfo] = {}
        for info in param_infos:
            if info.key not in unique_params:
                unique_params[info.key] = info

        # Allocate buffers: key -> list of tensors (one per slot)
        self._buffers: dict[tuple, list[torch.Tensor]] = {}
        for key, info in unique_params.items():
            slot_tensors = []
            for _ in range(slot_capacity):
                # Use empty_strided to preserve parameter's memory layout
                buf = torch.empty_strided(
                    size=info.shape,
                    stride=info.stride,
                    dtype=info.dtype,
                    device=device,
                )
                slot_tensors.append(buf)
                self.total_bytes += info.num_bytes
            self._buffers[key] = slot_tensors

        logger.debug(
            "[StaticBufferPool] Allocated %d unique (name, shape, stride, dtype), "
            "%d slots each, total %.4f GB",
            len(unique_params),
            slot_capacity,
            self.total_bytes / 1e9,
        )

    defget_buffer(
        self,
        name: str,
        shape: tuple[int, ...],
        stride: tuple[int, ...],
        dtype: torch.dtype,
        slot_idx: int,
    ) -> torch.Tensor:
"""Get a static buffer for the given name/shape/stride/dtype/slot."""
        key = (name, shape, stride, dtype)
        return self._buffers[key][slot_idx % self.slot_capacity]
```

### get\_buffer [¶](#vllm.model_executor.offloader.prefetch.StaticBufferPool.get_buffer "Permanent link")

Get a static buffer for the given name/shape/stride/dtype/slot.

Source code in `vllm/model_executor/offloader/prefetch.py`

```
defget_buffer(
    self,
    name: str,
    shape: tuple[int, ...],
    stride: tuple[int, ...],
    dtype: torch.dtype,
    slot_idx: int,
) -> torch.Tensor:
"""Get a static buffer for the given name/shape/stride/dtype/slot."""
    key = (name, shape, stride, dtype)
    return self._buffers[key][slot_idx % self.slot_capacity]
```

## \_BaseParamOffloader [¶](#vllm.model_executor.offloader.prefetch._BaseParamOffloader "Permanent link")

Bases: `ABC`

Base class for parameter offloading strategies.

Source code in `vllm/model_executor/offloader/prefetch.py`

```
class_BaseParamOffloader(ABC):
"""Base class for parameter offloading strategies."""

    # CPU storage for offloaded parameters (set by subclasses)
    _cpu_storage: torch.Tensor | None
    # GPU buffer reference (set by subclasses when using static buffers)
    _gpu_buffer: torch.Tensor | None

    @staticmethod
    defcreate(mode: str, **kwargs) -> "_BaseParamOffloader":
"""Factory method to create appropriate offloader for mode."""
        if mode == "cpu":
            return _CpuParamOffloader(**kwargs)
        else:
            raise ValueError(f"Unknown offload mode: {mode}")

    def__init__(self, module: nn.Module, param_name: str):
        self._module = module
        self._param_name = param_name
        self.offloaded_bytes = 0
        self._cpu_storage = None
        self._gpu_buffer = None

    @property
    def_param(self) -> nn.Parameter:
"""Get the parameter being offloaded.

        Supports dotted names (e.g. 'self_attn.qkv_proj.weight') by
        traversing the module hierarchy.
        """
        obj: Any = self._module
        for attr in self._param_name.split("."):
            obj = getattr(obj, attr)
        return obj

    defpost_init(self):
"""Initialize offloading (move parameter to storage)."""
        return

    @abstractmethod
    defsync_cpu_storage(self) -> None:
"""Sync CPU storage with current param.data.

        Called after process_weights_after_loading to update _cpu_storage
        with the final processed weights.
        """
        pass

    @abstractmethod
    defassign_static_buffer(self, gpu_buffer: torch.Tensor) -> None:
"""Point parameter data to GPU static buffer."""
        pass
```

### \_param `property` [¶](#vllm.model_executor.offloader.prefetch._BaseParamOffloader._param "Permanent link")

Get the parameter being offloaded.

Supports dotted names (e.g. 'self\_attn.qkv\_proj.weight') by traversing the module hierarchy.

### assign\_static\_buffer `abstractmethod` [¶](#vllm.model_executor.offloader.prefetch._BaseParamOffloader.assign_static_buffer "Permanent link")

```
assign_static_buffer(gpu_buffer: Tensor) -> None
```

Point parameter data to GPU static buffer.

Source code in `vllm/model_executor/offloader/prefetch.py`

```
@abstractmethod
defassign_static_buffer(self, gpu_buffer: torch.Tensor) -> None:
"""Point parameter data to GPU static buffer."""
    pass
```

### create `staticmethod` [¶](#vllm.model_executor.offloader.prefetch._BaseParamOffloader.create "Permanent link")

```
create(mode: str, **kwargs) -> _BaseParamOffloader
```

Factory method to create appropriate offloader for mode.

Source code in `vllm/model_executor/offloader/prefetch.py`

```
@staticmethod
defcreate(mode: str, **kwargs) -> "_BaseParamOffloader":
"""Factory method to create appropriate offloader for mode."""
    if mode == "cpu":
        return _CpuParamOffloader(**kwargs)
    else:
        raise ValueError(f"Unknown offload mode: {mode}")
```

### post\_init [¶](#vllm.model_executor.offloader.prefetch._BaseParamOffloader.post_init "Permanent link")

Initialize offloading (move parameter to storage).

Source code in `vllm/model_executor/offloader/prefetch.py`

```
defpost_init(self):
"""Initialize offloading (move parameter to storage)."""
    return
```

### sync\_cpu\_storage `abstractmethod` [¶](#vllm.model_executor.offloader.prefetch._BaseParamOffloader.sync_cpu_storage "Permanent link")

```
sync_cpu_storage() -> None
```

Sync CPU storage with current param.data.

Called after process\_weights\_after\_loading to update \_cpu\_storage with the final processed weights.

Source code in `vllm/model_executor/offloader/prefetch.py`

```
@abstractmethod
defsync_cpu_storage(self) -> None:
"""Sync CPU storage with current param.data.

    Called after process_weights_after_loading to update _cpu_storage
    with the final processed weights.
    """
    pass
```

## \_CpuParamOffloader [¶](#vllm.model_executor.offloader.prefetch._CpuParamOffloader "Permanent link")

Bases: `_BaseParamOffloader`

Offload parameter to pinned CPU memory.

Uses GPU static buffers as the actual parameter, with CPU storage kept separately. This ensures torch.compile sees GPU tensors at trace time.

The offloading happens in two phases: 1. **init**() - copies GPU data to CPU, frees GPU memory immediately 2. assign\_static\_buffer() - points param.data to GPU static buffer

Source code in `vllm/model_executor/offloader/prefetch.py`

```
class_CpuParamOffloader(_BaseParamOffloader):
"""Offload parameter to pinned CPU memory.

    Uses GPU static buffers as the actual parameter, with CPU storage
    kept separately. This ensures torch.compile sees GPU tensors at trace time.

    The offloading happens in two phases:
    1. __init__() - copies GPU data to CPU, frees GPU memory immediately
    2. assign_static_buffer() - points param.data to GPU static buffer
    """

    def__init__(self, module: nn.Module, param_name: str):
        super().__init__(module, param_name)
        self._cpu_storage: torch.Tensor | None = None
        self._gpu_buffer: torch.Tensor | None = None  # Store reference to GPU buffer
        # Set to True if the underlying nn.Parameter was deleted by
        # process_weights_after_loading (e.g. transient KV-cache scale params
        # such as k_scale/v_scale created by BaseKVCacheMethod.create_weights
        # and deleted after copying into permanent _k_scale buffers).
        self._param_deleted: bool = False

        # Offload to CPU immediately to free GPU memory during model loading
        self._offload_to_cpu_internal()

    def_offload_to_cpu_internal(self):
"""Copy parameter data to pinned CPU storage and free GPU memory.

        This replaces param.data with CPU storage, allowing weight loading
        to continue writing to CPU memory. GPU memory is freed when the
        original GPU tensor is garbage collected.
        """
        param = self._param
        pin_memory = should_pin_memory()

        # Create pinned CPU storage and copy current GPU data
        self._cpu_storage = torch.empty_strided(
            size=param.data.size(),
            stride=param.data.stride(),
            dtype=param.data.dtype,
            layout=param.data.layout,
            device="cpu",
            pin_memory=pin_memory,
        )
        self._cpu_storage.copy_(param.data)

        self.offloaded_bytes = (
            self._cpu_storage.numel() * self._cpu_storage.element_size()
        )

        # Point param.data to CPU storage - this allows weight loading to work
        # and frees GPU memory when the original GPU tensor is garbage collected
        param.data = self._cpu_storage

    def_update_cpu_storage_from_param(self) -> None:
"""Update _cpu_storage from current param.data, ensuring pinned memory.

        After process_weights_after_loading, device_loading_context creates
        non-pinned CPU tensors via `p.data = p.data.to("cpu")`. Using
        non-pinned memory with `copy_(src, non_blocking=True)` causes CUDA to
        perform a stream synchronization before the copy, breaking the
        event-based fork synchronization and potentially allowing the copy
        to overwrite the GPU buffer while the compute stream still reads it.

        This method ensures _cpu_storage always uses pinned memory when
        available, re-pinning if necessary.
        """
        param = self._param

        if param.data.device.type == "cpu":
            if should_pin_memory() and not param.data.is_pinned():
                pinned = torch.empty_strided(
                    size=param.data.size(),
                    stride=param.data.stride(),
                    dtype=param.data.dtype,
                    layout=param.data.layout,
                    device="cpu",
                    pin_memory=True,
                )
                pinned.copy_(param.data)
                self._cpu_storage = pinned
            else:
                self._cpu_storage = param.data
        else:
            # param.data is on GPU - copy to existing CPU storage
            assert self._cpu_storage is not None
            self._cpu_storage.copy_(param.data)

    defassign_static_buffer(self, gpu_buffer: torch.Tensor) -> None:
"""Point parameter data to GPU static buffer.

        This is called after weight loading AND process_weights_after_loading
        complete. At this point:
        - param.data may have been replaced by device_loading_context
          (which creates new CPU tensors after quantization processing)
        - We need to update _cpu_storage to point to current param.data
          so that prefetch copies the processed weights, not stale data
        - Then point param.data to the GPU buffer for torch.compile
        """
        assert self._cpu_storage is not None, (
            "_offload_to_cpu_internal() must be called before assign_static_buffer()"
        )

        # Get current parameter (may have been replaced by
        # process_weights_after_loading)
        param = self._param

        # Update _cpu_storage to current param.data. This is critical because:
        # 1. process_weights_after_loading may transform weights (quantization)
        # 2. device_loading_context creates NEW CPU tensors when moving back
        # 3. Our old _cpu_storage would have pre-processed or stale data
        self._update_cpu_storage_from_param()

        # Store reference to GPU buffer for use in start_onload
        self._gpu_buffer = gpu_buffer

        # Point parameter to static GPU buffer - this is what torch.compile sees
        param.data = gpu_buffer

    defsync_cpu_storage(self) -> None:
"""Sync CPU storage with current param.data.

        Called after process_weights_after_loading to update _cpu_storage
        with the final processed weights. This is critical because:
        1. process_weights_after_loading may transform weights (quantization)
        2. device_loading_context creates NEW CPU tensors when moving back
        3. Our old _cpu_storage would have pre-processed or stale data

        If the parameter no longer exists on the module (e.g. transient
        KV-cache scale parameters such as k_scale/v_scale that are created
        by BaseKVCacheMethod.create_weights() and then deleted by
        process_weights_after_loading() after copying their values into
        permanent _k_scale buffers), the offloader marks itself as deleted
        and skips the sync.  The caller (_ModuleOffloader.sync_cpu_storage)
        is responsible for removing these stale entries.
        """
        try:
            self._update_cpu_storage_from_param()
        except AttributeError:
            # The parameter was deleted by process_weights_after_loading.
            # Drop the now-stale CPU storage so this offloader can be pruned.
            self._param_deleted = True
            self._cpu_storage = None

    defpost_init(self):
"""No-op: offloading done in offload_to_cpu/assign_static_buffer."""
        pass
```

### \_offload\_to\_cpu\_internal [¶](#vllm.model_executor.offloader.prefetch._CpuParamOffloader._offload_to_cpu_internal "Permanent link")

```
_offload_to_cpu_internal()
```

Copy parameter data to pinned CPU storage and free GPU memory.

This replaces param.data with CPU storage, allowing weight loading to continue writing to CPU memory. GPU memory is freed when the original GPU tensor is garbage collected.

Source code in `vllm/model_executor/offloader/prefetch.py`

```
def_offload_to_cpu_internal(self):
"""Copy parameter data to pinned CPU storage and free GPU memory.

    This replaces param.data with CPU storage, allowing weight loading
    to continue writing to CPU memory. GPU memory is freed when the
    original GPU tensor is garbage collected.
    """
    param = self._param
    pin_memory = should_pin_memory()

    # Create pinned CPU storage and copy current GPU data
    self._cpu_storage = torch.empty_strided(
        size=param.data.size(),
        stride=param.data.stride(),
        dtype=param.data.dtype,
        layout=param.data.layout,
        device="cpu",
        pin_memory=pin_memory,
    )
    self._cpu_storage.copy_(param.data)

    self.offloaded_bytes = (
        self._cpu_storage.numel() * self._cpu_storage.element_size()
    )

    # Point param.data to CPU storage - this allows weight loading to work
    # and frees GPU memory when the original GPU tensor is garbage collected
    param.data = self._cpu_storage
```

### \_update\_cpu\_storage\_from\_param [¶](#vllm.model_executor.offloader.prefetch._CpuParamOffloader._update_cpu_storage_from_param "Permanent link")

```
_update_cpu_storage_from_param() -> None
```

Update \_cpu\_storage from current param.data, ensuring pinned memory.

After process\_weights\_after\_loading, device\_loading\_context creates non-pinned CPU tensors via `p.data = p.data.to("cpu")`. Using non-pinned memory with `copy_(src, non_blocking=True)` causes CUDA to perform a stream synchronization before the copy, breaking the event-based fork synchronization and potentially allowing the copy to overwrite the GPU buffer while the compute stream still reads it.

This method ensures \_cpu\_storage always uses pinned memory when available, re-pinning if necessary.

Source code in `vllm/model_executor/offloader/prefetch.py`

```
def_update_cpu_storage_from_param(self) -> None:
"""Update _cpu_storage from current param.data, ensuring pinned memory.

    After process_weights_after_loading, device_loading_context creates
    non-pinned CPU tensors via `p.data = p.data.to("cpu")`. Using
    non-pinned memory with `copy_(src, non_blocking=True)` causes CUDA to
    perform a stream synchronization before the copy, breaking the
    event-based fork synchronization and potentially allowing the copy
    to overwrite the GPU buffer while the compute stream still reads it.

    This method ensures _cpu_storage always uses pinned memory when
    available, re-pinning if necessary.
    """
    param = self._param

    if param.data.device.type == "cpu":
        if should_pin_memory() and not param.data.is_pinned():
            pinned = torch.empty_strided(
                size=param.data.size(),
                stride=param.data.stride(),
                dtype=param.data.dtype,
                layout=param.data.layout,
                device="cpu",
                pin_memory=True,
            )
            pinned.copy_(param.data)
            self._cpu_storage = pinned
        else:
            self._cpu_storage = param.data
    else:
        # param.data is on GPU - copy to existing CPU storage
        assert self._cpu_storage is not None
        self._cpu_storage.copy_(param.data)
```

### assign\_static\_buffer [¶](#vllm.model_executor.offloader.prefetch._CpuParamOffloader.assign_static_buffer "Permanent link")

```
assign_static_buffer(gpu_buffer: Tensor) -> None
```

Point parameter data to GPU static buffer.

This is called after weight loading AND process\_weights\_after\_loading complete. At this point: - param.data may have been replaced by device\_loading\_context (which creates new CPU tensors after quantization processing) - We need to update \_cpu\_storage to point to current param.data so that prefetch copies the processed weights, not stale data - Then point param.data to the GPU buffer for torch.compile

Source code in `vllm/model_executor/offloader/prefetch.py`

```
defassign_static_buffer(self, gpu_buffer: torch.Tensor) -> None:
"""Point parameter data to GPU static buffer.

    This is called after weight loading AND process_weights_after_loading
    complete. At this point:
    - param.data may have been replaced by device_loading_context
      (which creates new CPU tensors after quantization processing)
    - We need to update _cpu_storage to point to current param.data
      so that prefetch copies the processed weights, not stale data
    - Then point param.data to the GPU buffer for torch.compile
    """
    assert self._cpu_storage is not None, (
        "_offload_to_cpu_internal() must be called before assign_static_buffer()"
    )

    # Get current parameter (may have been replaced by
    # process_weights_after_loading)
    param = self._param

    # Update _cpu_storage to current param.data. This is critical because:
    # 1. process_weights_after_loading may transform weights (quantization)
    # 2. device_loading_context creates NEW CPU tensors when moving back
    # 3. Our old _cpu_storage would have pre-processed or stale data
    self._update_cpu_storage_from_param()

    # Store reference to GPU buffer for use in start_onload
    self._gpu_buffer = gpu_buffer

    # Point parameter to static GPU buffer - this is what torch.compile sees
    param.data = gpu_buffer
```

### post\_init [¶](#vllm.model_executor.offloader.prefetch._CpuParamOffloader.post_init "Permanent link")

No-op: offloading done in offload\_to\_cpu/assign\_static\_buffer.

Source code in `vllm/model_executor/offloader/prefetch.py`

```
defpost_init(self):
"""No-op: offloading done in offload_to_cpu/assign_static_buffer."""
    pass
```

### sync\_cpu\_storage [¶](#vllm.model_executor.offloader.prefetch._CpuParamOffloader.sync_cpu_storage "Permanent link")

```
sync_cpu_storage() -> None
```

Sync CPU storage with current param.data.

Called after process\_weights\_after\_loading to update \_cpu\_storage with the final processed weights. This is critical because: 1. process\_weights\_after\_loading may transform weights (quantization) 2. device\_loading\_context creates NEW CPU tensors when moving back 3. Our old \_cpu\_storage would have pre-processed or stale data

If the parameter no longer exists on the module (e.g. transient KV-cache scale parameters such as k\_scale/v\_scale that are created by BaseKVCacheMethod.create\_weights() and then deleted by process\_weights\_after\_loading() after copying their values into permanent \_k\_scale buffers), the offloader marks itself as deleted and skips the sync. The caller (\_ModuleOffloader.sync\_cpu\_storage) is responsible for removing these stale entries.

Source code in `vllm/model_executor/offloader/prefetch.py`

```
defsync_cpu_storage(self) -> None:
"""Sync CPU storage with current param.data.

    Called after process_weights_after_loading to update _cpu_storage
    with the final processed weights. This is critical because:
    1. process_weights_after_loading may transform weights (quantization)
    2. device_loading_context creates NEW CPU tensors when moving back
    3. Our old _cpu_storage would have pre-processed or stale data

    If the parameter no longer exists on the module (e.g. transient
    KV-cache scale parameters such as k_scale/v_scale that are created
    by BaseKVCacheMethod.create_weights() and then deleted by
    process_weights_after_loading() after copying their values into
    permanent _k_scale buffers), the offloader marks itself as deleted
    and skips the sync.  The caller (_ModuleOffloader.sync_cpu_storage)
    is responsible for removing these stale entries.
    """
    try:
        self._update_cpu_storage_from_param()
    except AttributeError:
        # The parameter was deleted by process_weights_after_loading.
        # Drop the now-stale CPU storage so this offloader can be pruned.
        self._param_deleted = True
        self._cpu_storage = None
```

## \_ModuleOffloader [¶](#vllm.model_executor.offloader.prefetch._ModuleOffloader "Permanent link")

Manages offloading for a single module.

Uses static buffers from a shared pool instead of dynamic allocation.

Source code in `vllm/model_executor/offloader/prefetch.py`

```
class_ModuleOffloader:
"""Manages offloading for a single module.

    Uses static buffers from a shared pool instead of dynamic allocation.
    """

    def__init__(
        self,
        mode: str,
        module: nn.Module,
        copy_stream: torch.cuda.Stream,
        whitelist_param_names: list[str],
        layer_idx: int,
    ):
        self.mode = mode
        self.module = module
        self.device = next(module.parameters()).device
        self.copy_stream = copy_stream
        self.layer_idx = layer_idx
        self.offloaded_bytes = 0

        # Event to signal when H2D copy to static buffer is complete.
        # Used for per-layer synchronization (both eager and capture modes).
        self._copy_done_event = torch.cuda.Event()

        # Track whether _copy_done_event is valid for eager-mode wait_event.
        # False when: (1) never recorded, or (2) last recorded during a
        # cudagraph capture (events become invalid after capture ends).
        # In these cases we fall back to wait_stream.
        self._event_valid_for_eager = False

        # Track if last prefetch was started during CUDA graph capture.
        # Used to skip wait_event during capture for pre-capture prefetches.
        self._prefetch_in_capture = False

        assert self.device != torch.device("cpu"), (
            "Module parameters should not already be on CPU "
            "(offloader handles CPU placement)"
        )

        # Buffer pool and slot (assigned in assign_buffer_slot)
        self._buffer_pool: StaticBufferPool | None = None
        self._buffer_slot_idx: int = 0

        param_dict = dict(self.module.named_parameters())
        assert all(name in param_dict for name in whitelist_param_names), (
            f"Whitelist params {whitelist_param_names} not found in module params "
            f"{list(param_dict.keys())}"
        )

        self._param_offloaders = {
            name: _BaseParamOffloader.create(mode, module=module, param_name=name)
            for name in whitelist_param_names
        }

    defpost_init(self):
"""Collect total offloaded bytes (offloading already done in __init__)."""
        for param_offloader in self._param_offloaders.values():
            param_offloader.post_init()
            self.offloaded_bytes += param_offloader.offloaded_bytes

    defsync_cpu_storage(self):
"""Sync CPU storage with current param.data.

        Called after process_weights_after_loading to ensure _cpu_storage
        contains the final processed weights, not stale pre-loading data.

        Parameters whose underlying nn.Parameter was deleted by
        process_weights_after_loading (e.g. transient KV-cache scale params)
        are pruned from self._param_offloaders so they do not participate in
        buffer-pool allocation or prefetching.
        """
        for param_offloader in self._param_offloaders.values():
            param_offloader.sync_cpu_storage()

        # Remove offloaders whose parameter was deleted during
        # process_weights_after_loading (e.g. k_scale / v_scale).
        deleted = [
            name
            for name, offloader in self._param_offloaders.items()
            if getattr(offloader, "_param_deleted", False)
        ]
        if deleted:
            logger.debug(
                "Pruning %d transient offloaded param(s) that were deleted "
                "by process_weights_after_loading: %s",
                len(deleted),
                deleted,
            )
            for name in deleted:
                del self._param_offloaders[name]

    defget_param_infos(self) -> list[ParamInfo]:
"""Get parameter metadata for buffer pool allocation.

        Note: sync_cpu_storage() must be called before this method to ensure
        _cpu_storage reflects the final processed weights (after quantization).
        """
        infos = []
        for name, offloader in self._param_offloaders.items():
            cpu_storage = offloader._cpu_storage
            assert cpu_storage is not None, "CPU storage not initialized"
            infos.append(
                ParamInfo(
                    name=name,
                    shape=tuple(cpu_storage.shape),
                    stride=tuple(cpu_storage.stride()),
                    dtype=cpu_storage.dtype,
                )
            )
        return infos

    defassign_buffer_slot(self, pool: StaticBufferPool, slot_idx: int):
"""Assign this module to a buffer slot in the pool.

        Also assigns static GPU buffers to each parameter offloader,
        which moves the parameter data to point to the GPU buffer.
        """
        self._buffer_pool = pool
        self._buffer_slot_idx = slot_idx

        # Assign static buffers to parameters
        # Use CPU storage shape/stride/dtype since param.data is now empty
        for name, offloader in self._param_offloaders.items():
            cpu_storage = offloader._cpu_storage
            assert cpu_storage is not None, "CPU storage not initialized"
            buffer = pool.get_buffer(
                name=name,
                shape=tuple(cpu_storage.shape),
                stride=tuple(cpu_storage.stride()),
                dtype=cpu_storage.dtype,
                slot_idx=slot_idx,
            )
            offloader.assign_static_buffer(buffer)

    defstart_onload_to_static(self):
"""Start async copy from CPU storage to GPU buffer.

        Uses event-based forking to join copy_stream to CUDA graph capture.
        This ensures H2D copies are properly captured when recording a graph.

        IMPORTANT: We must wait for the compute stream before copying, because
        the previous layer's forward may still be using the buffer (GPU ops are
        async). Without this sync, we could overwrite the buffer while it's
        being read.
        """
        assert self._buffer_pool is not None, "Buffer pool not assigned"

        # Track if this prefetch is being captured (for _wait_for_layer logic)
        self._prefetch_in_capture = torch.cuda.is_current_stream_capturing()

        # Fork: record event on compute stream, copy_stream waits on it
        # This joins copy_stream to any active CUDA graph capture
        fork_event = torch.cuda.Event()
        torch.cuda.current_stream().record_event(fork_event)
        self.copy_stream.wait_event(fork_event)

        with torch.cuda.stream(self.copy_stream):
            for name, offloader in self._param_offloaders.items():
                cpu_storage = offloader._cpu_storage
                gpu_buffer = offloader._gpu_buffer
                assert cpu_storage is not None, "CPU storage not initialized"
                assert gpu_buffer is not None, "GPU buffer not assigned"
                assert not should_pin_memory() or cpu_storage.is_pinned(), (
                    f"CPU storage for {name} is not pinned! "
                    "non_blocking=True H2D copy from non-pinned memory "
                    "causes stream synchronization that breaks "
                    "event-based fork synchronization."
                )
                gpu_buffer.copy_(cpu_storage, non_blocking=True)

        # Record completion event for _wait_for_layer to use
        self._copy_done_event.record(self.copy_stream)
        # Event is only valid for eager wait_event if recorded outside capture.
        # Events recorded during capture become invalid after capture ends.
        self._event_valid_for_eager = not torch.cuda.is_current_stream_capturing()
```

### assign\_buffer\_slot [¶](#vllm.model_executor.offloader.prefetch._ModuleOffloader.assign_buffer_slot "Permanent link")

```
assign_buffer_slot(pool: StaticBufferPool, slot_idx: int)
```

Assign this module to a buffer slot in the pool.

Also assigns static GPU buffers to each parameter offloader, which moves the parameter data to point to the GPU buffer.

Source code in `vllm/model_executor/offloader/prefetch.py`

```
defassign_buffer_slot(self, pool: StaticBufferPool, slot_idx: int):
"""Assign this module to a buffer slot in the pool.

    Also assigns static GPU buffers to each parameter offloader,
    which moves the parameter data to point to the GPU buffer.
    """
    self._buffer_pool = pool
    self._buffer_slot_idx = slot_idx

    # Assign static buffers to parameters
    # Use CPU storage shape/stride/dtype since param.data is now empty
    for name, offloader in self._param_offloaders.items():
        cpu_storage = offloader._cpu_storage
        assert cpu_storage is not None, "CPU storage not initialized"
        buffer = pool.get_buffer(
            name=name,
            shape=tuple(cpu_storage.shape),
            stride=tuple(cpu_storage.stride()),
            dtype=cpu_storage.dtype,
            slot_idx=slot_idx,
        )
        offloader.assign_static_buffer(buffer)
```

### get\_param\_infos [¶](#vllm.model_executor.offloader.prefetch._ModuleOffloader.get_param_infos "Permanent link")

```
get_param_infos() -> list[ParamInfo]
```

Get parameter metadata for buffer pool allocation.

Note: sync\_cpu\_storage() must be called before this method to ensure \_cpu\_storage reflects the final processed weights (after quantization).

Source code in `vllm/model_executor/offloader/prefetch.py`

```
defget_param_infos(self) -> list[ParamInfo]:
"""Get parameter metadata for buffer pool allocation.

    Note: sync_cpu_storage() must be called before this method to ensure
    _cpu_storage reflects the final processed weights (after quantization).
    """
    infos = []
    for name, offloader in self._param_offloaders.items():
        cpu_storage = offloader._cpu_storage
        assert cpu_storage is not None, "CPU storage not initialized"
        infos.append(
            ParamInfo(
                name=name,
                shape=tuple(cpu_storage.shape),
                stride=tuple(cpu_storage.stride()),
                dtype=cpu_storage.dtype,
            )
        )
    return infos
```

### post\_init [¶](#vllm.model_executor.offloader.prefetch._ModuleOffloader.post_init "Permanent link")

Collect total offloaded bytes (offloading already done in **init**).

Source code in `vllm/model_executor/offloader/prefetch.py`

```
defpost_init(self):
"""Collect total offloaded bytes (offloading already done in __init__)."""
    for param_offloader in self._param_offloaders.values():
        param_offloader.post_init()
        self.offloaded_bytes += param_offloader.offloaded_bytes
```

### start\_onload\_to\_static [¶](#vllm.model_executor.offloader.prefetch._ModuleOffloader.start_onload_to_static "Permanent link")

Start async copy from CPU storage to GPU buffer.

Uses event-based forking to join copy\_stream to CUDA graph capture. This ensures H2D copies are properly captured when recording a graph.

IMPORTANT: We must wait for the compute stream before copying, because the previous layer's forward may still be using the buffer (GPU ops are async). Without this sync, we could overwrite the buffer while it's being read.

Source code in `vllm/model_executor/offloader/prefetch.py`

```
defstart_onload_to_static(self):
"""Start async copy from CPU storage to GPU buffer.

    Uses event-based forking to join copy_stream to CUDA graph capture.
    This ensures H2D copies are properly captured when recording a graph.

    IMPORTANT: We must wait for the compute stream before copying, because
    the previous layer's forward may still be using the buffer (GPU ops are
    async). Without this sync, we could overwrite the buffer while it's
    being read.
    """
    assert self._buffer_pool is not None, "Buffer pool not assigned"

    # Track if this prefetch is being captured (for _wait_for_layer logic)
    self._prefetch_in_capture = torch.cuda.is_current_stream_capturing()

    # Fork: record event on compute stream, copy_stream waits on it
    # This joins copy_stream to any active CUDA graph capture
    fork_event = torch.cuda.Event()
    torch.cuda.current_stream().record_event(fork_event)
    self.copy_stream.wait_event(fork_event)

    with torch.cuda.stream(self.copy_stream):
        for name, offloader in self._param_offloaders.items():
            cpu_storage = offloader._cpu_storage
            gpu_buffer = offloader._gpu_buffer
            assert cpu_storage is not None, "CPU storage not initialized"
            assert gpu_buffer is not None, "GPU buffer not assigned"
            assert not should_pin_memory() or cpu_storage.is_pinned(), (
                f"CPU storage for {name} is not pinned! "
                "non_blocking=True H2D copy from non-pinned memory "
                "causes stream synchronization that breaks "
                "event-based fork synchronization."
            )
            gpu_buffer.copy_(cpu_storage, non_blocking=True)

    # Record completion event for _wait_for_layer to use
    self._copy_done_event.record(self.copy_stream)
    # Event is only valid for eager wait_event if recorded outside capture.
    # Events recorded during capture become invalid after capture ends.
    self._event_valid_for_eager = not torch.cuda.is_current_stream_capturing()
```

### sync\_cpu\_storage [¶](#vllm.model_executor.offloader.prefetch._ModuleOffloader.sync_cpu_storage "Permanent link")

Sync CPU storage with current param.data.

Called after process\_weights\_after\_loading to ensure \_cpu\_storage contains the final processed weights, not stale pre-loading data.

Parameters whose underlying nn.Parameter was deleted by process\_weights\_after\_loading (e.g. transient KV-cache scale params) are pruned from self.\_param\_offloaders so they do not participate in buffer-pool allocation or prefetching.

Source code in `vllm/model_executor/offloader/prefetch.py`

```
defsync_cpu_storage(self):
"""Sync CPU storage with current param.data.

    Called after process_weights_after_loading to ensure _cpu_storage
    contains the final processed weights, not stale pre-loading data.

    Parameters whose underlying nn.Parameter was deleted by
    process_weights_after_loading (e.g. transient KV-cache scale params)
    are pruned from self._param_offloaders so they do not participate in
    buffer-pool allocation or prefetching.
    """
    for param_offloader in self._param_offloaders.values():
        param_offloader.sync_cpu_storage()

    # Remove offloaders whose parameter was deleted during
    # process_weights_after_loading (e.g. k_scale / v_scale).
    deleted = [
        name
        for name, offloader in self._param_offloaders.items()
        if getattr(offloader, "_param_deleted", False)
    ]
    if deleted:
        logger.debug(
            "Pruning %d transient offloaded param(s) that were deleted "
            "by process_weights_after_loading: %s",
            len(deleted),
            deleted,
        )
        for name in deleted:
            del self._param_offloaders[name]
```