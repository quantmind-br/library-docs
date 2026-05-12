---
title: flashinfer_all_reduce - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/device_communicators/flashinfer_all_reduce/
source: sitemap
fetched_at: 2026-05-07T21:17:32.820012055-03:00
rendered_js: false
word_count: 108
summary: This module implements the FlashInfer AllReduce communicator for vLLM, providing managed workspace initialization and execution of fused all-reduce operations on CUDA-enabled devices.
tags:
    - vllm
    - flashinfer
    - all-reduce
    - distributed-computing
    - cuda
    - gpu-acceleration
    - tensor-parallelism
category: api
---

## FlashInferAllReduce [¶](#vllm.distributed.device_communicators.flashinfer_all_reduce.FlashInferAllReduce "Permanent link")

Source code in `vllm/distributed/device_communicators/flashinfer_all_reduce.py`

```
classFlashInferAllReduce:
    def__init__(
        self,
        group: ProcessGroup,
        device: int | str | torch.device,
    ):
        self.disabled = True

        if not fi_ar_available:
            logger.info(
                "FlashInfer All Reduce is disabled because flashinfer is not available"
            )
            return

        if not current_platform.is_cuda():
            logger.info(
                "FlashInfer All Reduce is disabled because it requires CUDA platform"
            )
            return

        self.group = group
        self.world_size = dist.get_world_size(self.group)
        self.rank = dist.get_rank(self.group)
        self.device = device
        if self.world_size == 1:
            return

        # Use the same threshold as the allreduce-rms fusion pass
        # TODO: tune the threshold
        MiB = 1024 * 1024
        max_workspace_size = PassConfig.default_fi_allreduce_fusion_max_size_mb().get(
            self.world_size, None
        )
        if not max_workspace_size:
            logger.warning(
                "FlashInfer All Reduce is disabled because it "
                "is not supported for world_size=%d.",
                self.world_size,
            )
            return
        self.max_workspace_size = max_workspace_size * MiB
        self.max_num_tokens = 0
        self.disabled = False

    def_ensure_workspace(self, hidden_dim: int, dtype: torch.dtype) -> bool:
"""Ensure the all reduce workspace is initialized."""
        if self.max_num_tokens == 0:
            element_size = torch.tensor([], dtype=dtype, device="cpu").element_size()
            self.max_num_tokens = self.max_workspace_size // (hidden_dim * element_size)
        workspace = get_fi_ar_workspace(
            world_size=self.world_size,
            rank=self.rank,
            max_token_num=self.max_num_tokens,
            hidden_dim=hidden_dim,
            dtype=dtype,
            group=self.group,
        )
        if workspace is None:
            self.disabled = True
            return False
        return True

    defshould_use_fi_ar(self, input_tensor: torch.Tensor) -> bool:
        if self.disabled:
            return False

        if not input_tensor.is_cuda:
            return False

        if not input_tensor.is_contiguous():
            return False

        if len(input_tensor.shape) != 2:
            return False

        num_tokens, hidden_dim = input_tensor.shape
        if not self.max_num_tokens:
            element_size = torch.tensor([], dtype=input_tensor.dtype).element_size()
            self.max_num_tokens = self.max_workspace_size // (hidden_dim * element_size)

        if num_tokens > self.max_num_tokens:
            return False

        return self._ensure_workspace(hidden_dim, input_tensor.dtype)

    defall_reduce(self, input_tensor: torch.Tensor) -> torch.Tensor:
        _, hidden_dim = input_tensor.shape
        workspace = get_fi_ar_workspace(
            world_size=self.world_size,
            rank=self.rank,
            max_token_num=self.max_num_tokens,
            hidden_dim=hidden_dim,
            dtype=input_tensor.dtype,
            group=self.group,
        )
        return flashinfer_comm.allreduce_fusion(
            input=input_tensor,
            workspace=workspace,
            pattern=flashinfer_comm.AllReduceFusionPattern.kAllReduce,
        )

    defdestroy(self):
        if not self.disabled:
            destroy_fi_ar_workspace()
```

### \_ensure\_workspace [¶](#vllm.distributed.device_communicators.flashinfer_all_reduce.FlashInferAllReduce._ensure_workspace "Permanent link")

Ensure the all reduce workspace is initialized.

Source code in `vllm/distributed/device_communicators/flashinfer_all_reduce.py`

```
def_ensure_workspace(self, hidden_dim: int, dtype: torch.dtype) -> bool:
"""Ensure the all reduce workspace is initialized."""
    if self.max_num_tokens == 0:
        element_size = torch.tensor([], dtype=dtype, device="cpu").element_size()
        self.max_num_tokens = self.max_workspace_size // (hidden_dim * element_size)
    workspace = get_fi_ar_workspace(
        world_size=self.world_size,
        rank=self.rank,
        max_token_num=self.max_num_tokens,
        hidden_dim=hidden_dim,
        dtype=dtype,
        group=self.group,
    )
    if workspace is None:
        self.disabled = True
        return False
    return True
```

## \_create\_workspace [¶](#vllm.distributed.device_communicators.flashinfer_all_reduce._create_workspace "Permanent link")

```
_create_workspace(
    backend: str,
    world_size: int,
    rank: int,
    max_token_num: int,
    hidden_dim: int,
    dtype: dtype,
    group: ProcessGroup,
)
```

Create a flashinfer allreduce workspace, returning None on failure.

Source code in `vllm/distributed/device_communicators/flashinfer_all_reduce.py`

```
def_create_workspace(
    backend: str,
    world_size: int,
    rank: int,
    max_token_num: int,
    hidden_dim: int,
    dtype: torch.dtype,
    group: ProcessGroup,
):
"""Create a flashinfer allreduce workspace, returning None on failure."""
    comm_backend = TorchDistBackend(group=group)
    rng_state = random.getstate()
    try:
        random.seed(int.from_bytes(os.urandom(16), byteorder="big"))
        workspace = flashinfer_comm.create_allreduce_fusion_workspace(
            backend=backend,
            world_size=world_size,
            rank=rank,
            max_token_num=max_token_num,
            hidden_dim=hidden_dim,
            dtype=dtype,
            comm_backend=comm_backend,
        )
    except Exception as e:
        if "multicast" in str(e).lower():
            logger.warning_once(
                "Failed to initialize FlashInfer All Reduce workspace: %s. "
                "This is expected on GPUs without NVSwitch (e.g., NVLink "
                "bridge-only or PCIe topologies).",
                e,
            )
        else:
            logger.warning_once(
                "Failed to initialize FlashInfer All Reduce workspace: %s.",
                e,
            )
        return None
    finally:
        random.setstate(rng_state)
    logger.debug(
        "Initialized FlashInfer All Reduce workspace: backend=%s, "
        "world_size=%d, rank=%d, max_token_num=%d, hidden_dim=%d, dtype=%s",
        backend,
        world_size,
        rank,
        max_token_num,
        hidden_dim,
        dtype,
    )
    return workspace
```

## get\_fi\_ar\_quant\_workspace [¶](#vllm.distributed.device_communicators.flashinfer_all_reduce.get_fi_ar_quant_workspace "Permanent link")

```
get_fi_ar_quant_workspace(
    world_size: int,
    rank: int,
    max_token_num: int,
    hidden_dim: int,
    dtype: dtype,
    group: ProcessGroup,
)
```

Return the allreduce workspace for quant patterns, initializing if needed.

Always uses trtllm backend as it is the only one supporting quantization fusion (FP8/FP4). Returns None for multi-node setups since not supported by trtllm backend.

Source code in `vllm/distributed/device_communicators/flashinfer_all_reduce.py`

```
defget_fi_ar_quant_workspace(
    world_size: int,
    rank: int,
    max_token_num: int,
    hidden_dim: int,
    dtype: torch.dtype,
    group: ProcessGroup,
):
"""
    Return the allreduce workspace for quant patterns, initializing if needed.

    Always uses trtllm backend as it is the only one supporting quantization
    fusion (FP8/FP4). Returns None for multi-node setups since not supported
    by trtllm backend.
    """
    global _fi_ar_quant_workspace
    if _fi_ar_quant_workspace is not None:
        return _fi_ar_quant_workspace

    if get_node_count() > 1:
        logger.warning_once(
            "Flashinfer allreduce quantization fusion is not supported for "
            "multi-node allreduce. Disabling quant fusion."
        )
        return None

    # Reuse the non-quant workspace if it was already created with trtllm
    if _fi_ar_workspace is not None and _fi_ar_workspace.backend == "trtllm":
        _fi_ar_quant_workspace = _fi_ar_workspace
        return _fi_ar_quant_workspace

    _fi_ar_quant_workspace = _create_workspace(
        "trtllm", world_size, rank, max_token_num, hidden_dim, dtype, group
    )
    if _fi_ar_quant_workspace is not None:
        logger.info_once(
            "Initialized FlashInfer Allreduce norm quantization "
            "fusion workspace with backend=trtllm"
        )
    else:
        logger.warning_once(
            "Failed to initialize FlashInfer Allreduce norm quantization "
            "fusion workspace with backend=trtllm"
        )

    return _fi_ar_quant_workspace
```

## get\_fi\_ar\_workspace [¶](#vllm.distributed.device_communicators.flashinfer_all_reduce.get_fi_ar_workspace "Permanent link")

```
get_fi_ar_workspace(
    world_size: int,
    rank: int,
    max_token_num: int,
    hidden_dim: int,
    dtype: dtype,
    group: ProcessGroup,
)
```

Return the allreduce workspace for non-quant patterns, initializing if needed.

Used by AllReduceFusionPass (non-quant patterns) and FlashInferAllReduce for standalone allreduce. Backend is controlled by VLLM\_FLASHINFER\_ALLREDUCE\_BACKEND env var.

Source code in `vllm/distributed/device_communicators/flashinfer_all_reduce.py`

```
defget_fi_ar_workspace(
    world_size: int,
    rank: int,
    max_token_num: int,
    hidden_dim: int,
    dtype: torch.dtype,
    group: ProcessGroup,
):
"""
    Return the allreduce workspace for non-quant patterns, initializing if needed.

    Used by AllReduceFusionPass (non-quant patterns) and FlashInferAllReduce
    for standalone allreduce. Backend is controlled by
    VLLM_FLASHINFER_ALLREDUCE_BACKEND env var.
    """
    global _fi_ar_workspace
    if _fi_ar_workspace is not None:
        return _fi_ar_workspace

    backend = _resolve_fi_ar_backend()

    if get_node_count() > 1 and backend == "trtllm":
        raise ValueError(
            "Flashinfer allreduce is not supported for multi-node allreduce with "
            "'trtllm' backend. Please use 'mnnvl' backend instead."
        )

    # Reuse the quant workspace if it was already created with the same backend
    if _fi_ar_quant_workspace is not None and _fi_ar_quant_workspace.backend == backend:
        _fi_ar_workspace = _fi_ar_quant_workspace
        return _fi_ar_workspace

    _fi_ar_workspace = _create_workspace(
        backend, world_size, rank, max_token_num, hidden_dim, dtype, group
    )
    if _fi_ar_workspace is not None:
        logger.info_once(
            "Initialized FlashInfer Allreduce norm fusion workspace "
            f"with backend={backend}"
        )
    else:
        logger.warning_once(
            "Failed to initialize FlashInfer Allreduce norm fusion workspace "
            f"with backend={backend}"
        )

    return _fi_ar_workspace
```