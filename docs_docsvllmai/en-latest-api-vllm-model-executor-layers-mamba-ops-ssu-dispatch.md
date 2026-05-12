---
title: ssu_dispatch - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/mamba/ops/ssu_dispatch/
source: sitemap
fetched_at: 2026-05-07T21:26:11.908202496-03:00
rendered_js: false
word_count: 144
summary: This module provides a unified dispatch mechanism for Mamba selective state update operations, allowing the system to switch between Triton and FlashInfer backends.
tags:
    - mamba
    - ssu
    - backend-dispatch
    - triton
    - flashinfer
    - vllm
category: api
---

Dispatch module for Mamba selective state update (SSU) backends.

Provides a unified `selective_state_update` function that dispatches to either the Triton or FlashInfer backend based on the configured `MambaBackendEnum`. Follows SGLang's dispatch pattern adapted for vLLM.

Bases: `MambaSSUBackend`

FlashInfer-based SSU backend.

Source code in `vllm/model_executor/layers/mamba/ops/ssu_dispatch.py`

```
classFlashInferSSUBackend(MambaSSUBackend):
"""FlashInfer-based SSU backend."""

    def__init__(self, mamba_config: MambaConfig):
        super().__init__(mamba_config)
        try:
            fromflashinfer.mambaimport selective_state_update as _fi_ssu
        except ImportError as e:
            raise ImportError(
                "FlashInfer is required for the flashinfer Mamba SSU backend. "
                "Please install flashinfer (>= 0.6.4): "
                "pip install flashinfer-python"
            ) frome
        self._kernel = _fi_ssu

    @property
    defname(self) -> str:
        return "flashinfer"

    def__call__(
        self,
        state: torch.Tensor,
        x: torch.Tensor,
        dt: torch.Tensor,
        A: torch.Tensor,
        B: torch.Tensor,
        C: torch.Tensor,
        D: torch.Tensor,
        dt_bias: torch.Tensor,
        z: torch.Tensor | None = None,
        dt_softplus: bool = False,
        state_batch_indices: torch.Tensor | None = None,
        dst_state_batch_indices: torch.Tensor | None = None,
        null_block_id: int = NULL_BLOCK_ID,
        out: torch.Tensor | None = None,
        num_accepted_tokens: torch.Tensor | None = None,
        cu_seqlens: torch.Tensor | None = None,
        is_blackwell: bool = False,
    ) -> None:
        rand_seed = (
            torch.randint(0, 2**32, (1,), device=state.device)
            if self._mamba_config.enable_stochastic_rounding
            else None
        )

        self._kernel(
            state,
            x,
            dt,
            A,
            B,
            C,
            D=D,
            z=z,
            dt_bias=dt_bias,
            dt_softplus=dt_softplus,
            state_batch_indices=state_batch_indices,
            dst_state_batch_indices=dst_state_batch_indices,
            cu_seqlens=cu_seqlens,
            num_accepted_tokens=num_accepted_tokens,
            cache_steps=state_batch_indices.size(-1)
            if cu_seqlens is not None and state_batch_indices is not None
            else 0,
            pad_slot_id=null_block_id,
            out=out,
            rand_seed=rand_seed,
            philox_rounds=self._mamba_config.stochastic_rounding_philox_rounds or 10,
        )
```

## MambaSSUBackend [¶](#vllm.model_executor.layers.mamba.ops.ssu_dispatch.MambaSSUBackend "Permanent link")

Bases: `ABC`

Abstract base class for Mamba SSU backends.

Source code in `vllm/model_executor/layers/mamba/ops/ssu_dispatch.py`

```
classMambaSSUBackend(ABC):
"""Abstract base class for Mamba SSU backends."""

    def__init__(self, mamba_config: MambaConfig):
        self._mamba_config = mamba_config

    @property
    @abstractmethod
    defname(self) -> str: ...

    @abstractmethod
    def__call__(
        self,
        state: torch.Tensor,
        x: torch.Tensor,
        dt: torch.Tensor,
        A: torch.Tensor,
        B: torch.Tensor,
        C: torch.Tensor,
        D: torch.Tensor,
        dt_bias: torch.Tensor,
        z: torch.Tensor | None = None,
        dt_softplus: bool = False,
        state_batch_indices: torch.Tensor | None = None,
        dst_state_batch_indices: torch.Tensor | None = None,
        null_block_id: int = NULL_BLOCK_ID,
        out: torch.Tensor | None = None,
        num_accepted_tokens: torch.Tensor | None = None,
        cu_seqlens: torch.Tensor | None = None,
        is_blackwell: bool = False,
    ) -> None: ...
```

## TritonSSUBackend [¶](#vllm.model_executor.layers.mamba.ops.ssu_dispatch.TritonSSUBackend "Permanent link")

Bases: `MambaSSUBackend`

Triton-based SSU backend (vLLM's default).

Source code in `vllm/model_executor/layers/mamba/ops/ssu_dispatch.py`

```
classTritonSSUBackend(MambaSSUBackend):
"""Triton-based SSU backend (vLLM's default)."""

    def__init__(self, mamba_config: MambaConfig):
        super().__init__(mamba_config)
        fromvllm.model_executor.layers.mamba.ops.mamba_ssmimport (
            selective_state_update as _triton_selective_state_update,
        )

        self._kernel = _triton_selective_state_update

    @property
    defname(self) -> str:
        return "triton"

    def__call__(
        self,
        state: torch.Tensor,
        x: torch.Tensor,
        dt: torch.Tensor,
        A: torch.Tensor,
        B: torch.Tensor,
        C: torch.Tensor,
        D: torch.Tensor,
        dt_bias: torch.Tensor,
        z: torch.Tensor | None = None,
        dt_softplus: bool = False,
        state_batch_indices: torch.Tensor | None = None,
        dst_state_batch_indices: torch.Tensor | None = None,
        null_block_id: int = NULL_BLOCK_ID,
        out: torch.Tensor | None = None,
        num_accepted_tokens: torch.Tensor | None = None,
        cu_seqlens: torch.Tensor | None = None,
        is_blackwell: bool = False,
    ) -> None:
        self._kernel(
            state,
            x,
            dt,
            A,
            B,
            C,
            D=D,
            z=z,
            dt_bias=dt_bias,
            dt_softplus=dt_softplus,
            state_batch_indices=state_batch_indices,
            dst_state_batch_indices=dst_state_batch_indices,
            null_block_id=null_block_id,
            out=out,
            num_accepted_tokens=num_accepted_tokens,
            cu_seqlens=cu_seqlens,
            is_blackwell=is_blackwell,
            enable_stochastic_rounding=self._mamba_config.enable_stochastic_rounding,
            cache_philox_rounds=self._mamba_config.stochastic_rounding_philox_rounds,
        )
```

## get\_mamba\_ssu\_backend [¶](#vllm.model_executor.layers.mamba.ops.ssu_dispatch.get_mamba_ssu_backend "Permanent link")

```
get_mamba_ssu_backend() -> MambaSSUBackend
```

Get the current Mamba SSU backend. Raises if not initialized.

Source code in `vllm/model_executor/layers/mamba/ops/ssu_dispatch.py`

```
defget_mamba_ssu_backend() -> MambaSSUBackend:
"""Get the current Mamba SSU backend. Raises if not initialized."""
    if _mamba_ssu_backend is None:
        raise RuntimeError(
            "Mamba SSU backend has not been initialized. "
            "Call initialize_mamba_ssu_backend() first."
        )
    return _mamba_ssu_backend
```

## initialize\_mamba\_ssu\_backend [¶](#vllm.model_executor.layers.mamba.ops.ssu_dispatch.initialize_mamba_ssu_backend "Permanent link")

Initialize the global Mamba SSU backend.

No-op if `kv_cache_config` contains no specs that call selective\_state\_update.

Source code in `vllm/model_executor/layers/mamba/ops/ssu_dispatch.py`

```
definitialize_mamba_ssu_backend(
    mamba_config: MambaConfig,
    kv_cache_config: KVCacheConfig,
) -> None:
"""Initialize the global Mamba SSU backend.

    No-op if `kv_cache_config` contains no specs that call
    selective_state_update.
    """
    if not any(
        isinstance(g.kv_cache_spec, MambaSpec)
        and g.kv_cache_spec.mamba_type in ("mamba1", "mamba2")
        for g in kv_cache_config.kv_cache_groups
    ):
        return

    global _mamba_ssu_backend

    backend = mamba_config.backend
    if backend not in _BACKEND_REGISTRY:
        raise ValueError(
            f"Unknown Mamba SSU backend: {backend}. "
            f"Valid options: {list(_BACKEND_REGISTRY.keys())}"
        )

    backend_cls = _BACKEND_REGISTRY[backend]
    if isinstance(_mamba_ssu_backend, backend_cls):
        return

    _mamba_ssu_backend = backend_cls(mamba_config)
    logger.info("Using %s Mamba SSU backend.", _mamba_ssu_backend.name)
```

## selective\_state\_update [¶](#vllm.model_executor.layers.mamba.ops.ssu_dispatch.selective_state_update "Permanent link")

```
selective_state_update(
    state: Tensor,
    x: Tensor,
    dt: Tensor,
    A: Tensor,
    B: Tensor,
    C: Tensor,
    D: Tensor,
    dt_bias: Tensor,
    z: Tensor | None = None,
    dt_softplus: bool = False,
    state_batch_indices: Tensor | None = None,
    dst_state_batch_indices: Tensor | None = None,
    null_block_id: int = NULL_BLOCK_ID,
    out: Tensor | None = None,
    num_accepted_tokens: Tensor | None = None,
    cu_seqlens: Tensor | None = None,
    is_blackwell: bool = False,
) -> None
```

Unified dispatch for Mamba selective state update.

Delegates to the initialized backend (Triton or FlashInfer).

Source code in `vllm/model_executor/layers/mamba/ops/ssu_dispatch.py`

```
defselective_state_update(
    state: torch.Tensor,
    x: torch.Tensor,
    dt: torch.Tensor,
    A: torch.Tensor,
    B: torch.Tensor,
    C: torch.Tensor,
    D: torch.Tensor,
    dt_bias: torch.Tensor,
    z: torch.Tensor | None = None,
    dt_softplus: bool = False,
    state_batch_indices: torch.Tensor | None = None,
    dst_state_batch_indices: torch.Tensor | None = None,
    null_block_id: int = NULL_BLOCK_ID,
    out: torch.Tensor | None = None,
    num_accepted_tokens: torch.Tensor | None = None,
    cu_seqlens: torch.Tensor | None = None,
    is_blackwell: bool = False,
) -> None:
"""Unified dispatch for Mamba selective state update.

    Delegates to the initialized backend (Triton or FlashInfer).
    """
    get_mamba_ssu_backend()(
        state,
        x,
        dt,
        A,
        B,
        C,
        D,
        dt_bias,
        z=z,
        dt_softplus=dt_softplus,
        state_batch_indices=state_batch_indices,
        dst_state_batch_indices=dst_state_batch_indices,
        null_block_id=null_block_id,
        out=out,
        num_accepted_tokens=num_accepted_tokens,
        cu_seqlens=cu_seqlens,
        is_blackwell=is_blackwell,
    )
```