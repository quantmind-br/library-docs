---
title: workspace - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/worker/workspace/
source: sitemap
fetched_at: 2026-05-07T21:43:20.191094856-03:00
rendered_js: false
word_count: 451
summary: The WorkspaceManager class provides a mechanism to manage and allocate workspace memory buffers for active ubatch slots, featuring locking capabilities to enforce static memory requirements during execution.
tags:
    - memory-management
    - workspace-allocation
    - tensor-buffer
    - gpu-memory
    - vllm-infrastructure
category: reference
---

## WorkspaceManager [¶](#vllm.v1.worker.workspace.WorkspaceManager "Permanent link")

Manager for workspace allocation.

Manages one workspace buffer per active ubatch slot. Can be locked to prevent further growth during execution.

Source code in `vllm/v1/worker/workspace.py`

```
classWorkspaceManager:
"""Manager for workspace allocation.

    Manages one workspace buffer per active ubatch slot.
    Can be locked to prevent further growth during execution.
    """

    def__init__(self, device: torch.device, num_ubatches: int | None = None):
        self._device = device
        # Cache num ubatches at init based on configuration (default to 1)
        self._num_ubatches = num_ubatches if num_ubatches is not None else 1
        self._current_workspaces: list[torch.Tensor | None] = [
            None
        ] * self._num_ubatches
        self._locked: bool = False

    @staticmethod
    def_workspace_size_bytes(workspace: torch.Tensor | None) -> int:
"""Get size of workspace in bytes."""
        if workspace is None:
            return 0
        return workspace.numel() * workspace.element_size()

    deflock(self) -> None:
"""Lock the workspace to prevent further growth.

        After locking, any attempt to allocate a larger workspace will raise
        an assertion error. This ensures workspace size is fixed during execution.
        """
        self._locked = True
        if envs.VLLM_DEBUG_WORKSPACE:
            logger.info(
                "[WORKSPACE DEBUG] Workspace locked. Current sizes: %s",
                [
                    self._workspace_size_bytes(ws) / _MB
                    for ws in self._current_workspaces
                    if ws is not None
                ],
            )

    defunlock(self) -> None:
"""Unlock the workspace to allow growth.

        This is used during elastic EP scaling when the workspace size
        needs to grow due to changes in the number of experts.
        """
        self._locked = False
        if envs.VLLM_DEBUG_WORKSPACE:
            logger.info(
                "[WORKSPACE DEBUG] Workspace unlocked. Current sizes: %s",
                [
                    self._workspace_size_bytes(ws) / _MB
                    for ws in self._current_workspaces
                    if ws is not None
                ],
            )

    defis_locked(self) -> bool:
"""Check if workspace is locked."""
        return self._locked

    defget_simultaneous(
        self, *shapes_and_dtypes: tuple[tuple[int, ...], torch.dtype]
    ) -> list[torch.Tensor]:
"""Get multiple workspace tensors simultaneously from a single allocation.

        Args:
            *shapes_and_dtypes: One or more (shape, dtype) tuples.

        Returns:
            List of tensor views into the workspace buffer, one per shape/dtype pair.
        """
        actual_bytes = [_compute_bytes(s, d) for s, d in shapes_and_dtypes]
        aligned_bytes = [round_up(actual, 256) for actual in actual_bytes]
        total_bytes = sum(aligned_bytes)

        # Calculate cumulative offsets using itertools.accumulate
        offsets = list(accumulate([0] + aligned_bytes[:-1]))

        current_workspace = self._ensure_workspace_size(total_bytes)

        return [
            current_workspace[offsets[i] : offsets[i] + actual_bytes[i]]
            .view(shapes_and_dtypes[i][1])
            .reshape(shapes_and_dtypes[i][0])
            for i in range(len(shapes_and_dtypes))
        ]

    def_ensure_workspace_size(self, required_bytes: int) -> torch.Tensor:
"""Ensure workspace is allocated and large enough, return current workspace.

        Args:
            required_bytes: The number of bytes required.

        Returns:
            The current workspace tensor.
        """
        ubatch_id = dbo_current_ubatch_id()
        current_workspace = self._current_workspaces[ubatch_id]
        current_size = self._workspace_size_bytes(current_workspace)

        if current_size < required_bytes:

            defget_caller_info() -> str:
"""Find first frame outside WorkspaceManager."""
                curr_frame = inspect.currentframe()
                if curr_frame is None:
                    return "unknown"
                # Walk up the stack skipping WorkspaceManager frames
                curr_frame = curr_frame.f_back
                while curr_frame is not None:
                    # TODO: This only catches instance methods (self), missing
                    # classmethods and staticmethods. Once Python 3.11+ is the
                    # minimum supported version, use co_qualname instead:
                    #   qualname = curr_frame.f_code.co_qualname
                    #   if qualname.startswith("WorkspaceManager."):
                    if isinstance(curr_frame.f_locals.get("self"), WorkspaceManager):
                        curr_frame = curr_frame.f_back
                        continue
                    filename = os.path.basename(curr_frame.f_code.co_filename)
                    return (
                        f"{filename}:{curr_frame.f_lineno}:{curr_frame.f_code.co_name}"
                    )
                return "unknown"

            if self._locked:
                raise AssertionError(
                    f"Workspace is locked but allocation from '{get_caller_info()}' "
                    f"requires {required_bytes/_MB:.2f} MB, current size is "
                    f"{current_size/_MB:.2f} MB. "
                    "Workspace growth is not allowed after locking."
                )

            # Only resize the requesting ubatch's workspace.  Other
            # ubatches resize lazily on their next get_simultaneous call.
            # Resizing all ubatches here would orphan the other ubatch's
            # old tensor when it still holds views into it (DBO leak).
            self._current_workspaces[ubatch_id] = None
            del current_workspace
            # Release the freed segment back to CUDA so the caching
            # allocator can reuse the GPU memory for the larger
            # allocation below. Without this, each resize may leave a
            # dead segment in reserved memory which can cause higher peak
            # memory usage.
            torch.accelerator.empty_cache()
            self._current_workspaces[ubatch_id] = torch.empty(
                (required_bytes,), dtype=torch.uint8, device=self._device
            )
            current_workspace = self._current_workspaces[ubatch_id]

            if envs.VLLM_DEBUG_WORKSPACE:
                logger.info(
                    "[WORKSPACE DEBUG] Resized workspace from '%s': %.2f MB -> "
                    "%.2f MB (ubatch %d)",
                    get_caller_info(),
                    current_size / _MB,
                    required_bytes / _MB,
                    ubatch_id,
                )

        return current_workspace
```

### \_ensure\_workspace\_size [¶](#vllm.v1.worker.workspace.WorkspaceManager._ensure_workspace_size "Permanent link")

```
_ensure_workspace_size(required_bytes: int) -> Tensor
```

Ensure workspace is allocated and large enough, return current workspace.

Parameters:

Name Type Description Default `required_bytes` `int`

The number of bytes required.

*required*

Returns:

Type Description `Tensor`

The current workspace tensor.

Source code in `vllm/v1/worker/workspace.py`

```
def_ensure_workspace_size(self, required_bytes: int) -> torch.Tensor:
"""Ensure workspace is allocated and large enough, return current workspace.

    Args:
        required_bytes: The number of bytes required.

    Returns:
        The current workspace tensor.
    """
    ubatch_id = dbo_current_ubatch_id()
    current_workspace = self._current_workspaces[ubatch_id]
    current_size = self._workspace_size_bytes(current_workspace)

    if current_size < required_bytes:

        defget_caller_info() -> str:
"""Find first frame outside WorkspaceManager."""
            curr_frame = inspect.currentframe()
            if curr_frame is None:
                return "unknown"
            # Walk up the stack skipping WorkspaceManager frames
            curr_frame = curr_frame.f_back
            while curr_frame is not None:
                # TODO: This only catches instance methods (self), missing
                # classmethods and staticmethods. Once Python 3.11+ is the
                # minimum supported version, use co_qualname instead:
                #   qualname = curr_frame.f_code.co_qualname
                #   if qualname.startswith("WorkspaceManager."):
                if isinstance(curr_frame.f_locals.get("self"), WorkspaceManager):
                    curr_frame = curr_frame.f_back
                    continue
                filename = os.path.basename(curr_frame.f_code.co_filename)
                return (
                    f"{filename}:{curr_frame.f_lineno}:{curr_frame.f_code.co_name}"
                )
            return "unknown"

        if self._locked:
            raise AssertionError(
                f"Workspace is locked but allocation from '{get_caller_info()}' "
                f"requires {required_bytes/_MB:.2f} MB, current size is "
                f"{current_size/_MB:.2f} MB. "
                "Workspace growth is not allowed after locking."
            )

        # Only resize the requesting ubatch's workspace.  Other
        # ubatches resize lazily on their next get_simultaneous call.
        # Resizing all ubatches here would orphan the other ubatch's
        # old tensor when it still holds views into it (DBO leak).
        self._current_workspaces[ubatch_id] = None
        del current_workspace
        # Release the freed segment back to CUDA so the caching
        # allocator can reuse the GPU memory for the larger
        # allocation below. Without this, each resize may leave a
        # dead segment in reserved memory which can cause higher peak
        # memory usage.
        torch.accelerator.empty_cache()
        self._current_workspaces[ubatch_id] = torch.empty(
            (required_bytes,), dtype=torch.uint8, device=self._device
        )
        current_workspace = self._current_workspaces[ubatch_id]

        if envs.VLLM_DEBUG_WORKSPACE:
            logger.info(
                "[WORKSPACE DEBUG] Resized workspace from '%s': %.2f MB -> "
                "%.2f MB (ubatch %d)",
                get_caller_info(),
                current_size / _MB,
                required_bytes / _MB,
                ubatch_id,
            )

    return current_workspace
```

### \_workspace\_size\_bytes `staticmethod` [¶](#vllm.v1.worker.workspace.WorkspaceManager._workspace_size_bytes "Permanent link")

```
_workspace_size_bytes(workspace: Tensor | None) -> int
```

Get size of workspace in bytes.

Source code in `vllm/v1/worker/workspace.py`

```
@staticmethod
def_workspace_size_bytes(workspace: torch.Tensor | None) -> int:
"""Get size of workspace in bytes."""
    if workspace is None:
        return 0
    return workspace.numel() * workspace.element_size()
```

### get\_simultaneous [¶](#vllm.v1.worker.workspace.WorkspaceManager.get_simultaneous "Permanent link")

Get multiple workspace tensors simultaneously from a single allocation.

Parameters:

Name Type Description Default `*shapes_and_dtypes` `tuple[tuple[int, ...], dtype]`

One or more (shape, dtype) tuples.

`()`

Returns:

Type Description `list[Tensor]`

List of tensor views into the workspace buffer, one per shape/dtype pair.

Source code in `vllm/v1/worker/workspace.py`

```
defget_simultaneous(
    self, *shapes_and_dtypes: tuple[tuple[int, ...], torch.dtype]
) -> list[torch.Tensor]:
"""Get multiple workspace tensors simultaneously from a single allocation.

    Args:
        *shapes_and_dtypes: One or more (shape, dtype) tuples.

    Returns:
        List of tensor views into the workspace buffer, one per shape/dtype pair.
    """
    actual_bytes = [_compute_bytes(s, d) for s, d in shapes_and_dtypes]
    aligned_bytes = [round_up(actual, 256) for actual in actual_bytes]
    total_bytes = sum(aligned_bytes)

    # Calculate cumulative offsets using itertools.accumulate
    offsets = list(accumulate([0] + aligned_bytes[:-1]))

    current_workspace = self._ensure_workspace_size(total_bytes)

    return [
        current_workspace[offsets[i] : offsets[i] + actual_bytes[i]]
        .view(shapes_and_dtypes[i][1])
        .reshape(shapes_and_dtypes[i][0])
        for i in range(len(shapes_and_dtypes))
    ]
```

### is\_locked [¶](#vllm.v1.worker.workspace.WorkspaceManager.is_locked "Permanent link")

Check if workspace is locked.

Source code in `vllm/v1/worker/workspace.py`

```
defis_locked(self) -> bool:
"""Check if workspace is locked."""
    return self._locked
```

### lock [¶](#vllm.v1.worker.workspace.WorkspaceManager.lock "Permanent link")

Lock the workspace to prevent further growth.

After locking, any attempt to allocate a larger workspace will raise an assertion error. This ensures workspace size is fixed during execution.

Source code in `vllm/v1/worker/workspace.py`

```
deflock(self) -> None:
"""Lock the workspace to prevent further growth.

    After locking, any attempt to allocate a larger workspace will raise
    an assertion error. This ensures workspace size is fixed during execution.
    """
    self._locked = True
    if envs.VLLM_DEBUG_WORKSPACE:
        logger.info(
            "[WORKSPACE DEBUG] Workspace locked. Current sizes: %s",
            [
                self._workspace_size_bytes(ws) / _MB
                for ws in self._current_workspaces
                if ws is not None
            ],
        )
```

### unlock [¶](#vllm.v1.worker.workspace.WorkspaceManager.unlock "Permanent link")

Unlock the workspace to allow growth.

This is used during elastic EP scaling when the workspace size needs to grow due to changes in the number of experts.

Source code in `vllm/v1/worker/workspace.py`

```
defunlock(self) -> None:
"""Unlock the workspace to allow growth.

    This is used during elastic EP scaling when the workspace size
    needs to grow due to changes in the number of experts.
    """
    self._locked = False
    if envs.VLLM_DEBUG_WORKSPACE:
        logger.info(
            "[WORKSPACE DEBUG] Workspace unlocked. Current sizes: %s",
            [
                self._workspace_size_bytes(ws) / _MB
                for ws in self._current_workspaces
                if ws is not None
            ],
        )
```

## current\_workspace\_manager [¶](#vllm.v1.worker.workspace.current_workspace_manager "Permanent link")

```
current_workspace_manager() -> WorkspaceManager
```

Get the current workspace manager instance.

Raises:

Type Description `AssertionError`

If workspace manager has not been initialized.

Source code in `vllm/v1/worker/workspace.py`

```
defcurrent_workspace_manager() -> "WorkspaceManager":
"""Get the current workspace manager instance.

    Raises:
        AssertionError: If workspace manager has not been initialized.
    """
    assert _manager is not None, (
        "WorkspaceManager not initialized. Call init_workspace_manager() "
        "with a device before using workspace functions."
    )
    return _manager
```

## init\_workspace\_manager [¶](#vllm.v1.worker.workspace.init_workspace_manager "Permanent link")

```
init_workspace_manager(
    device: device, num_ubatches: int | None = None
) -> None
```

Initialize the workspace manager with a device.

Must be called before using any workspace functions. Typically called from GPUModelRunner.**init**.

Parameters:

Name Type Description Default `device` `device`

The device to allocate workspace on.

*required* `num_ubatches` `int | None`

Number of workspace ubatch slots. Defaults to 1.

`None`

Source code in `vllm/v1/worker/workspace.py`

```
definit_workspace_manager(
    device: torch.device, num_ubatches: int | None = None
) -> None:
"""Initialize the workspace manager with a device.

    Must be called before using any workspace functions. Typically called
    from GPUModelRunner.__init__.

    Args:
        device: The device to allocate workspace on.
        num_ubatches: Number of workspace ubatch slots. Defaults to 1.
    """
    global _manager
    if _manager is not None:
        logger.warning(
            "WorkspaceManager already initialized on device %s, "
            "reinitializing on device %s",
            _manager._device,
            device,
        )
    _manager = WorkspaceManager(device, num_ubatches)
```

## is\_workspace\_manager\_initialized [¶](#vllm.v1.worker.workspace.is_workspace_manager_initialized "Permanent link")

```
is_workspace_manager_initialized() -> bool
```

Check if workspace manager has been initialized.

Returns:

Type Description `bool`

True if workspace manager is initialized, False otherwise.

Source code in `vllm/v1/worker/workspace.py`

```
defis_workspace_manager_initialized() -> bool:
"""Check if workspace manager has been initialized.

    Returns:
        True if workspace manager is initialized, False otherwise.
    """
    return _manager is not None
```

## lock\_workspace [¶](#vllm.v1.worker.workspace.lock_workspace "Permanent link")

Lock the workspace to prevent further growth.

After calling this function, any attempt to allocate a workspace larger than the current size will raise an AssertionError. This ensures that workspace size is fixed during execution and prevents unexpected memory allocations in the hot path.

Example

### During initialization[¶](#vllm.v1.worker.workspace.lock_workspace--during-initialization "Permanent link")

init\_workspace\_manager(device) reserve\_workspace(shape1, dtype1) reserve\_workspace(shape2, dtype2)

### Lock after warmup/profiling[¶](#vllm.v1.worker.workspace.lock_workspace--lock-after-warmupprofiling "Permanent link")

lock\_workspace()

### Now all get\_workspace calls must fit in pre-allocated size[¶](#vllm.v1.worker.workspace.lock_workspace--now-all-get_workspace-calls-must-fit-in-pre-allocated-size "Permanent link")

Source code in `vllm/v1/worker/workspace.py`

```
deflock_workspace() -> None:
"""Lock the workspace to prevent further growth.

    After calling this function, any attempt to allocate a workspace larger
    than the current size will raise an AssertionError. This ensures that
    workspace size is fixed during execution and prevents unexpected memory
    allocations in the hot path.

    Example:
        # During initialization
        init_workspace_manager(device)
        reserve_workspace(shape1, dtype1)
        reserve_workspace(shape2, dtype2)

        # Lock after warmup/profiling
        lock_workspace()

        # Now all get_workspace calls must fit in pre-allocated size
    """
    current_workspace_manager().lock()
```

## reset\_workspace\_manager [¶](#vllm.v1.worker.workspace.reset_workspace_manager "Permanent link")

```
reset_workspace_manager() -> None
```

Reset the workspace manager to uninitialized state.

This is primarily intended for testing purposes to allow tests to reinitialize the workspace manager cleanly.

Source code in `vllm/v1/worker/workspace.py`

```
defreset_workspace_manager() -> None:
"""Reset the workspace manager to uninitialized state.

    This is primarily intended for testing purposes to allow tests
    to reinitialize the workspace manager cleanly.
    """
    global _manager
    _manager = None
```

## unlock\_workspace [¶](#vllm.v1.worker.workspace.unlock_workspace "Permanent link")

```
unlock_workspace() -> None
```

Unlock the workspace to allow growth.

This is used during elastic EP scaling when the workspace size needs to grow due to changes in the number of experts. After scaling operations complete, lock\_workspace() should be called again to prevent unexpected allocations.

Source code in `vllm/v1/worker/workspace.py`

```
defunlock_workspace() -> None:
"""Unlock the workspace to allow growth.

    This is used during elastic EP scaling when the workspace size
    needs to grow due to changes in the number of experts.
    After scaling operations complete, lock_workspace() should be
    called again to prevent unexpected allocations.
    """
    current_workspace_manager().unlock()
```