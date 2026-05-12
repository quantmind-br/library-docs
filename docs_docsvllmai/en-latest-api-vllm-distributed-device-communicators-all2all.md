---
title: all2all - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/device_communicators/all2all/
source: sitemap
fetched_at: 2026-05-07T21:17:26.095644216-03:00
rendered_js: false
word_count: 291
summary: This document defines the AgRsAll2AllManager class, which manages all-to-all communication in distributed environments using all-gather and reduce-scatter operations.
tags:
    - distributed-computing
    - all-to-all
    - all-gather
    - reduce-scatter
    - tensor-parallelism
    - vllm-framework
category: reference
---

## AgRsAll2AllManager [¶](#vllm.distributed.device_communicators.all2all.AgRsAll2AllManager "Permanent link")

Bases: `All2AllManagerBase`

An implementation of all2all communication based on all-gather (dispatch) and reduce-scatter (combine).

Source code in `vllm/distributed/device_communicators/all2all.py`

```
classAgRsAll2AllManager(All2AllManagerBase):
"""
    An implementation of all2all communication based on
    all-gather (dispatch) and reduce-scatter (combine).
    """

    def__init__(self, cpu_group, tcp_store_group=None):
        super().__init__(cpu_group, tcp_store_group)

    defdispatch_router_logits(
        self,
        hidden_states: torch.Tensor,
        router_logits: torch.Tensor,
        is_sequence_parallel: bool = False,
        extra_tensors: list[torch.Tensor] | None = None,
    ) -> (
        tuple[torch.Tensor, torch.Tensor]
        | tuple[torch.Tensor, torch.Tensor, list[torch.Tensor]]
    ):
"""
        Gather hidden_states and router_logits from all dp ranks.
        """
        dp_metadata = get_forward_context().dp_metadata
        assert dp_metadata is not None
        sizes = dp_metadata.get_chunk_sizes_across_dp_rank()
        assert sizes is not None
        dist_group = get_ep_group() if is_sequence_parallel else get_dp_group()
        assert sizes[dist_group.rank_in_group] == hidden_states.shape[0]

        tensors_to_gather = [hidden_states, router_logits]
        if extra_tensors is not None:
            tensors_to_gather.extend(extra_tensors)

        gathered_tensors = dist_group.all_gatherv(
            tensors_to_gather,
            dim=0,
            sizes=sizes,
        )

        if extra_tensors is not None:
            return (gathered_tensors[0], gathered_tensors[1], gathered_tensors[2:])
        return gathered_tensors[0], gathered_tensors[1]

    defdispatch(
        self,
        hidden_states: torch.Tensor,
        topk_weights: torch.Tensor,
        topk_ids: torch.Tensor,
        is_sequence_parallel: bool = False,
        extra_tensors: list[torch.Tensor] | None = None,
    ) -> (
        tuple[torch.Tensor, torch.Tensor, torch.Tensor]
        | tuple[torch.Tensor, torch.Tensor, torch.Tensor, list[torch.Tensor]]
    ):
"""
        Gather hidden_states and router_logits from all dp ranks.
        """
        dp_metadata = get_forward_context().dp_metadata
        assert dp_metadata is not None
        sizes = dp_metadata.get_chunk_sizes_across_dp_rank()
        assert sizes is not None
        dist_group = get_ep_group() if is_sequence_parallel else get_dp_group()
        assert sizes[dist_group.rank_in_group] == hidden_states.shape[0]

        tensors_to_gather = [hidden_states, topk_weights, topk_ids]
        if extra_tensors is not None:
            tensors_to_gather.extend(extra_tensors)

        gathered_tensors = dist_group.all_gatherv(
            tensors_to_gather,
            dim=0,
            sizes=sizes,
        )

        hidden_states = gathered_tensors[0]
        topk_weights = gathered_tensors[1]
        topk_ids = gathered_tensors[2]

        if extra_tensors is None:
            return hidden_states, topk_weights, topk_ids

        return hidden_states, topk_weights, topk_ids, gathered_tensors[3:]

    defcombine(
        self, hidden_states: torch.Tensor, is_sequence_parallel: bool = False
    ) -> torch.Tensor:
"""
        Reduce-scatter hidden_states across all dp ranks.
        """
        dp_metadata = get_forward_context().dp_metadata
        assert dp_metadata is not None
        sizes = dp_metadata.get_chunk_sizes_across_dp_rank()
        assert sizes is not None

        dist_group = get_ep_group() if is_sequence_parallel else get_dp_group()
        hidden_states = dist_group.reduce_scatterv(hidden_states, dim=0, sizes=sizes)
        return hidden_states

    defdestroy(self):
        pass
```

### combine [¶](#vllm.distributed.device_communicators.all2all.AgRsAll2AllManager.combine "Permanent link")

Reduce-scatter hidden\_states across all dp ranks.

Source code in `vllm/distributed/device_communicators/all2all.py`

```
defcombine(
    self, hidden_states: torch.Tensor, is_sequence_parallel: bool = False
) -> torch.Tensor:
"""
    Reduce-scatter hidden_states across all dp ranks.
    """
    dp_metadata = get_forward_context().dp_metadata
    assert dp_metadata is not None
    sizes = dp_metadata.get_chunk_sizes_across_dp_rank()
    assert sizes is not None

    dist_group = get_ep_group() if is_sequence_parallel else get_dp_group()
    hidden_states = dist_group.reduce_scatterv(hidden_states, dim=0, sizes=sizes)
    return hidden_states
```

### dispatch [¶](#vllm.distributed.device_communicators.all2all.AgRsAll2AllManager.dispatch "Permanent link")

```
dispatch(
    hidden_states: Tensor,
    topk_weights: Tensor,
    topk_ids: Tensor,
    is_sequence_parallel: bool = False,
    extra_tensors: list[Tensor] | None = None,
) -> (
    tuple[Tensor, Tensor, Tensor]
    | tuple[Tensor, Tensor, Tensor, list[Tensor]]
)
```

Gather hidden\_states and router\_logits from all dp ranks.

Source code in `vllm/distributed/device_communicators/all2all.py`

```
defdispatch(
    self,
    hidden_states: torch.Tensor,
    topk_weights: torch.Tensor,
    topk_ids: torch.Tensor,
    is_sequence_parallel: bool = False,
    extra_tensors: list[torch.Tensor] | None = None,
) -> (
    tuple[torch.Tensor, torch.Tensor, torch.Tensor]
    | tuple[torch.Tensor, torch.Tensor, torch.Tensor, list[torch.Tensor]]
):
"""
    Gather hidden_states and router_logits from all dp ranks.
    """
    dp_metadata = get_forward_context().dp_metadata
    assert dp_metadata is not None
    sizes = dp_metadata.get_chunk_sizes_across_dp_rank()
    assert sizes is not None
    dist_group = get_ep_group() if is_sequence_parallel else get_dp_group()
    assert sizes[dist_group.rank_in_group] == hidden_states.shape[0]

    tensors_to_gather = [hidden_states, topk_weights, topk_ids]
    if extra_tensors is not None:
        tensors_to_gather.extend(extra_tensors)

    gathered_tensors = dist_group.all_gatherv(
        tensors_to_gather,
        dim=0,
        sizes=sizes,
    )

    hidden_states = gathered_tensors[0]
    topk_weights = gathered_tensors[1]
    topk_ids = gathered_tensors[2]

    if extra_tensors is None:
        return hidden_states, topk_weights, topk_ids

    return hidden_states, topk_weights, topk_ids, gathered_tensors[3:]
```

### dispatch\_router\_logits [¶](#vllm.distributed.device_communicators.all2all.AgRsAll2AllManager.dispatch_router_logits "Permanent link")

Gather hidden\_states and router\_logits from all dp ranks.

Source code in `vllm/distributed/device_communicators/all2all.py`

```
defdispatch_router_logits(
    self,
    hidden_states: torch.Tensor,
    router_logits: torch.Tensor,
    is_sequence_parallel: bool = False,
    extra_tensors: list[torch.Tensor] | None = None,
) -> (
    tuple[torch.Tensor, torch.Tensor]
    | tuple[torch.Tensor, torch.Tensor, list[torch.Tensor]]
):
"""
    Gather hidden_states and router_logits from all dp ranks.
    """
    dp_metadata = get_forward_context().dp_metadata
    assert dp_metadata is not None
    sizes = dp_metadata.get_chunk_sizes_across_dp_rank()
    assert sizes is not None
    dist_group = get_ep_group() if is_sequence_parallel else get_dp_group()
    assert sizes[dist_group.rank_in_group] == hidden_states.shape[0]

    tensors_to_gather = [hidden_states, router_logits]
    if extra_tensors is not None:
        tensors_to_gather.extend(extra_tensors)

    gathered_tensors = dist_group.all_gatherv(
        tensors_to_gather,
        dim=0,
        sizes=sizes,
    )

    if extra_tensors is not None:
        return (gathered_tensors[0], gathered_tensors[1], gathered_tensors[2:])
    return gathered_tensors[0], gathered_tensors[1]
```

## DeepEPAll2AllManagerBase [¶](#vllm.distributed.device_communicators.all2all.DeepEPAll2AllManagerBase "Permanent link")

Bases: `All2AllManagerBase`

All2All communication based on DeepEP High-Throughput kernels.

Source code in `vllm/distributed/device_communicators/all2all.py`

```
classDeepEPAll2AllManagerBase(All2AllManagerBase):
"""
    All2All communication based on DeepEP High-Throughput kernels.
    """

    def__init__(self, cpu_group, tcp_store_group=None):
        assert has_deep_ep(), (
            "DeepEP kernels not found. Please follow https://github.com/vllm-project/vllm/blob/main/tools/ep_kernels/README.md"
            " to install DeepEP kernels."
        )  # noqa
        super().__init__(cpu_group, tcp_store_group)
        self.handle_cache = Cache()

        # This is the DeepEP default. Stick to it till we can establish
        # reasonable defaults based on profiling.
        self.num_sms = 20

    defget_handle(self, kwargs):
        raise NotImplementedError

    defdispatch_router_logits(
        self,
        hidden_states: torch.Tensor,
        router_logits: torch.Tensor,
        is_sequence_parallel: bool = False,
        extra_tensors: list[torch.Tensor] | None = None,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        raise NotImplementedError

    defdispatch(
        self,
        hidden_states: torch.Tensor,
        topk_weights: torch.Tensor,
        topk_ids: torch.Tensor,
        is_sequence_parallel: bool = False,
        extra_tensors: list[torch.Tensor] | None = None,
    ) -> (
        tuple[torch.Tensor, torch.Tensor, torch.Tensor]
        | tuple[torch.Tensor, torch.Tensor, torch.Tensor, list[torch.Tensor]]
    ):
        raise NotImplementedError

    defcombine(
        self, hidden_states: torch.Tensor, is_sequence_parallel: bool = False
    ) -> torch.Tensor:
        raise NotImplementedError

    defdestroy(self):
        with self.handle_cache._lock:
            for _, handle in self.handle_cache._cache.items():
                handle.destroy()
            self.handle_cache._cache.clear()
```

## DeepEPHTAll2AllManager [¶](#vllm.distributed.device_communicators.all2all.DeepEPHTAll2AllManager "Permanent link")

Bases: `DeepEPAll2AllManagerBase`

All2All communication based on DeepEP High-Throughput kernels.

Source code in `vllm/distributed/device_communicators/all2all.py`

```
classDeepEPHTAll2AllManager(DeepEPAll2AllManagerBase):
"""
    All2All communication based on DeepEP High-Throughput kernels.
    """

    def__init__(self, cpu_group, tcp_store_group=None):
        super().__init__(cpu_group, tcp_store_group)

    def_make_all2all_kwargs(self) -> dict[Any, Any]:
        # Defaults for internode and intranode are taken from DeepEP tests.
        num_nvl_bytes = envs.VLLM_DEEPEP_BUFFER_SIZE_MB * 1024 * 1024
        num_rdma_bytes = None
        num_qps_per_rank = None

        if self.internode and not envs.VLLM_DEEPEP_HIGH_THROUGHPUT_FORCE_INTRA_NODE:
            num_rdma_bytes = envs.VLLM_DEEPEP_BUFFER_SIZE_MB * 1024 * 1024
            num_qps_per_rank = self.num_sms // 2
        else:
            num_rdma_bytes = 0
            num_qps_per_rank = 1

        assert num_rdma_bytes is not None
        assert num_qps_per_rank is not None
        # TODO: remove platform-specific logic
        # once ROCm DeepEP is updated with the latest APIs.
        kwargs = dict(
            group=self.cpu_group,
            num_nvl_bytes=num_nvl_bytes,
            num_rdma_bytes=num_rdma_bytes,
            low_latency_mode=False,
            num_qps_per_rank=num_qps_per_rank,
            explicitly_destroy=True,
        )
        return kwargs

    defget_handle(self, kwargs):
        assert len(kwargs) == 0, (
            "DeepEPHTAll2AllManager expects no arguments. All the required "
            "args are computed in the Manager itself."
        )

        importdeep_ep  # type: ignore[import-not-found]

        buffer_kwargs = self._make_all2all_kwargs()
        logger.debug("DeepEP all2all args %s", buffer_kwargs)
        handle: deep_ep.Buffer = self.handle_cache.get_or_create(
            buffer_kwargs, deep_ep.Buffer
        )
        return handle

    defset_num_sms(self, num_sms: int):
        importdeep_ep  # type: ignore[import-not-found]

        # Right now the buffers are sized for only what the kernels were
        # created with. So we can only reduce the number of SMS used
        # but not increase it.
        if num_sms > self.num_sms:
            num_sms = self.num_sms
        deep_ep.Buffer.set_num_sms(num_sms)
```

## DeepEPLLAll2AllManager [¶](#vllm.distributed.device_communicators.all2all.DeepEPLLAll2AllManager "Permanent link")

Bases: `DeepEPAll2AllManagerBase`

All2All communication based on DeepEP Low-Latency kernels.

Source code in `vllm/distributed/device_communicators/all2all.py`

```
classDeepEPLLAll2AllManager(DeepEPAll2AllManagerBase):
"""
    All2All communication based on DeepEP Low-Latency kernels.
    """

    def__init__(self, cpu_group, tcp_store_group=None):
        super().__init__(cpu_group, tcp_store_group)

    def_make_all2all_kwargs(
        self,
        max_num_tokens_per_dp_rank: int,
        token_hidden_size: int,
        num_ep_ranks: int,
        num_global_experts: int,
        num_local_experts: int,
    ) -> dict[Any, Any]:
"""
        max_num_tokens_per_dp_rank : the maximum number of tokens a DP rank
          can dispatch all the ranks must hold the same value.
        token_hidden_size: the hidden dimension of each token.
        num_ep_ranks: the number of EP group ranks.
        num_global_experts: Number of experts in the model.
        num_local_experts: Number of experts in an EP rank.
        """
        importdeep_ep  # type: ignore[import-not-found]

        # Defaults for internode and intranode are taken from DeepEP tests.
        num_nvl_bytes = envs.VLLM_DEEPEP_BUFFER_SIZE_MB * 1024 * 1024
        num_qps_per_rank = num_local_experts
        num_rdma_bytes = deep_ep.Buffer.get_low_latency_rdma_size_hint(
            num_max_dispatch_tokens_per_rank=max_num_tokens_per_dp_rank,
            hidden=token_hidden_size,
            num_ranks=num_ep_ranks,
            num_experts=num_global_experts,
        )

        assert num_rdma_bytes is not None
        # TODO: remove platform-specific logic
        # once ROCm DeepEP is updated with the latest APIs.
        kwargs = dict(
            group=self.cpu_group,
            num_nvl_bytes=num_nvl_bytes,
            num_rdma_bytes=num_rdma_bytes,
            low_latency_mode=True,
            num_qps_per_rank=num_qps_per_rank,
            allow_nvlink_for_low_latency_mode=True,
            allow_mnnvl=envs.VLLM_DEEPEP_LOW_LATENCY_USE_MNNVL,
            explicitly_destroy=True,
        )
        return kwargs

    defget_handle(self, kwargs):
"""
        The kwargs for DeepEPLLAll2AllManager is dictated by
        _make_all2all_kwargs.
        """
        importdeep_ep  # type: ignore[import-not-found]

        buffer_kwargs = self._make_all2all_kwargs(**kwargs)
        logger.debug("DeepEP all2all args %s", buffer_kwargs)
        handle: deep_ep.Buffer = self.handle_cache.get_or_create(
            buffer_kwargs, deep_ep.Buffer
        )
        return handle

    # DeepEP LL uses RDMA so no SMs are used for communication
    defmax_sms_used(self) -> int | None:
        return 0
```

### \_make\_all2all\_kwargs [¶](#vllm.distributed.device_communicators.all2all.DeepEPLLAll2AllManager._make_all2all_kwargs "Permanent link")

```
_make_all2all_kwargs(
    max_num_tokens_per_dp_rank: int,
    token_hidden_size: int,
    num_ep_ranks: int,
    num_global_experts: int,
    num_local_experts: int,
) -> dict[Any, Any]
```

the maximum number of tokens a DP rank

can dispatch all the ranks must hold the same value.

token\_hidden\_size: the hidden dimension of each token. num\_ep\_ranks: the number of EP group ranks. num\_global\_experts: Number of experts in the model. num\_local\_experts: Number of experts in an EP rank.

Source code in `vllm/distributed/device_communicators/all2all.py`

```
def_make_all2all_kwargs(
    self,
    max_num_tokens_per_dp_rank: int,
    token_hidden_size: int,
    num_ep_ranks: int,
    num_global_experts: int,
    num_local_experts: int,
) -> dict[Any, Any]:
"""
    max_num_tokens_per_dp_rank : the maximum number of tokens a DP rank
      can dispatch all the ranks must hold the same value.
    token_hidden_size: the hidden dimension of each token.
    num_ep_ranks: the number of EP group ranks.
    num_global_experts: Number of experts in the model.
    num_local_experts: Number of experts in an EP rank.
    """
    importdeep_ep  # type: ignore[import-not-found]

    # Defaults for internode and intranode are taken from DeepEP tests.
    num_nvl_bytes = envs.VLLM_DEEPEP_BUFFER_SIZE_MB * 1024 * 1024
    num_qps_per_rank = num_local_experts
    num_rdma_bytes = deep_ep.Buffer.get_low_latency_rdma_size_hint(
        num_max_dispatch_tokens_per_rank=max_num_tokens_per_dp_rank,
        hidden=token_hidden_size,
        num_ranks=num_ep_ranks,
        num_experts=num_global_experts,
    )

    assert num_rdma_bytes is not None
    # TODO: remove platform-specific logic
    # once ROCm DeepEP is updated with the latest APIs.
    kwargs = dict(
        group=self.cpu_group,
        num_nvl_bytes=num_nvl_bytes,
        num_rdma_bytes=num_rdma_bytes,
        low_latency_mode=True,
        num_qps_per_rank=num_qps_per_rank,
        allow_nvlink_for_low_latency_mode=True,
        allow_mnnvl=envs.VLLM_DEEPEP_LOW_LATENCY_USE_MNNVL,
        explicitly_destroy=True,
    )
    return kwargs
```

### get\_handle [¶](#vllm.distributed.device_communicators.all2all.DeepEPLLAll2AllManager.get_handle "Permanent link")

The kwargs for DeepEPLLAll2AllManager is dictated by \_make\_all2all\_kwargs.

Source code in `vllm/distributed/device_communicators/all2all.py`

```
defget_handle(self, kwargs):
"""
    The kwargs for DeepEPLLAll2AllManager is dictated by
    _make_all2all_kwargs.
    """
    importdeep_ep  # type: ignore[import-not-found]

    buffer_kwargs = self._make_all2all_kwargs(**kwargs)
    logger.debug("DeepEP all2all args %s", buffer_kwargs)
    handle: deep_ep.Buffer = self.handle_cache.get_or_create(
        buffer_kwargs, deep_ep.Buffer
    )
    return handle
```

## FlashInferNVLinkOneSidedManager [¶](#vllm.distributed.device_communicators.all2all.FlashInferNVLinkOneSidedManager "Permanent link")

Bases: `All2AllManagerBase`

All2All communication based on FlashInfer's MoeAlltoAll/One-sided NVLink kernel. This is a newer kernel from trtllm that should perform better than the kernel used by flashinfer\_nvlink\_two\_sided.

Source code in `vllm/distributed/device_communicators/all2all.py`

```
classFlashInferNVLinkOneSidedManager(All2AllManagerBase):
"""
    All2All communication based on FlashInfer's MoeAlltoAll/One-sided NVLink kernel.
    This is a newer kernel from trtllm that should perform better than the kernel
    used by flashinfer_nvlink_two_sided.
    """

    rank: int
    world_size: int

    def__init__(self, cpu_group):
        assert has_flashinfer_nvlink_one_sided(), (
            "flashinfer trtllm_moe_alltoall module not found. "
            "Please install/check flashinfer"
        )
        super().__init__(cpu_group)
        logger.debug(
            "Initialize FlashInfer One-sided NVLink rank=%d, world size=%d",
            self.rank,
            self.world_size,
        )
        self.initialized = False
        self.moe_alltoall: MoeAlltoAll | None = None
        self.mapping = None

    definitialize(
        self,
        max_num_tokens: int,
        top_k: int,
        num_experts: int,
        hidden_size: int,
        dispatch_dtype_bytes_per_elem: int = 0,
        dispatch_scale_bytes_per_token: int = 0,
    ):
"""Initialize the MoeAlltoAll workspace."""
        if self.initialized:
            return

        self.cleanup()
        gpus_per_node = torch.accelerator.device_count()
        logger.debug(
            "Making One-sided NVLink mapping: rank=%d, world size=%d",
            self.rank,
            self.world_size,
        )
        self.mapping = Mapping(
            self.world_size,
            self.rank,
            gpus_per_node,
            tp_size=self.world_size,
            moe_ep_size=self.world_size,
        )

        fromvllm.distributed.device_communicators.mnnvl_compatimport (
            CustomCommunicator,
        )

        # MNNVL workspace is allocated per rank in the comm_backend's group; the
        # flashinfer kernel asserts workspace.size(0) == moe_ep_size, so the backend
        # must span the EP group (= DP*PCP*TP), not the DP group.
        ep_config = MnnvlConfig(
            comm_backend=CustomCommunicator(self.cpu_group),
        )
        if dispatch_dtype_bytes_per_elem == 0:
            hidden_bytes = hidden_size // 2
        else:
            hidden_bytes = hidden_size * dispatch_dtype_bytes_per_elem
        total_dispatch_payload_size_per_token = (
            hidden_bytes
            + dispatch_scale_bytes_per_token
            + top_k * 4  # int32 topks ids
            + top_k * 4  # float32 topk weights
        )
        combine_payload_size_per_token = hidden_size * 2  # bf16 hidden states
        self.workspace_size = moe_a2a_get_workspace_size_per_rank(
            ep_size=self.world_size,
            max_num_tokens=max_num_tokens,
            total_dispatch_payload_size_per_token=total_dispatch_payload_size_per_token,
            combine_payload_size_per_token=combine_payload_size_per_token,
        )

        self.moe_alltoall = MoeAlltoAll(
            mapping=self.mapping,
            max_num_tokens=max_num_tokens,
            top_k=top_k,
            num_experts=num_experts,
            workspace_size_per_rank=self.workspace_size,
            mnnvl_config=ep_config,
        )

        self.gpus_per_node = gpus_per_node
        self.max_num_tokens = max_num_tokens
        self.top_k = top_k
        self.num_experts = num_experts
        self.hidden_size = hidden_size
        self.initialized = True

        logger.info(
            "FlashInfer One-sided NVLink initialized for rank %s, size %s",
            self.rank,
            self.world_size,
        )
        dist.barrier()

    defget_handle(self, kwargs):
        return self

    defcleanup(self):
"""Clean up resources."""
        if self.initialized and self.moe_alltoall is not None:
            try:
                del self.moe_alltoall
            except Exception as e:
                logger.warning(
                    "Failed to cleanup FlashInfer One-sided NVLink workspace: %s", e
                )
            finally:
                self.moe_alltoall = None
                self.mapping = None
                self.initialized = False
```

### cleanup [¶](#vllm.distributed.device_communicators.all2all.FlashInferNVLinkOneSidedManager.cleanup "Permanent link")

Clean up resources.

Source code in `vllm/distributed/device_communicators/all2all.py`

```
defcleanup(self):
"""Clean up resources."""
    if self.initialized and self.moe_alltoall is not None:
        try:
            del self.moe_alltoall
        except Exception as e:
            logger.warning(
                "Failed to cleanup FlashInfer One-sided NVLink workspace: %s", e
            )
        finally:
            self.moe_alltoall = None
            self.mapping = None
            self.initialized = False
```

### initialize [¶](#vllm.distributed.device_communicators.all2all.FlashInferNVLinkOneSidedManager.initialize "Permanent link")

```
initialize(
    max_num_tokens: int,
    top_k: int,
    num_experts: int,
    hidden_size: int,
    dispatch_dtype_bytes_per_elem: int = 0,
    dispatch_scale_bytes_per_token: int = 0,
)
```

Initialize the MoeAlltoAll workspace.

Source code in `vllm/distributed/device_communicators/all2all.py`

```
definitialize(
    self,
    max_num_tokens: int,
    top_k: int,
    num_experts: int,
    hidden_size: int,
    dispatch_dtype_bytes_per_elem: int = 0,
    dispatch_scale_bytes_per_token: int = 0,
):
"""Initialize the MoeAlltoAll workspace."""
    if self.initialized:
        return

    self.cleanup()
    gpus_per_node = torch.accelerator.device_count()
    logger.debug(
        "Making One-sided NVLink mapping: rank=%d, world size=%d",
        self.rank,
        self.world_size,
    )
    self.mapping = Mapping(
        self.world_size,
        self.rank,
        gpus_per_node,
        tp_size=self.world_size,
        moe_ep_size=self.world_size,
    )

    fromvllm.distributed.device_communicators.mnnvl_compatimport (
        CustomCommunicator,
    )

    # MNNVL workspace is allocated per rank in the comm_backend's group; the
    # flashinfer kernel asserts workspace.size(0) == moe_ep_size, so the backend
    # must span the EP group (= DP*PCP*TP), not the DP group.
    ep_config = MnnvlConfig(
        comm_backend=CustomCommunicator(self.cpu_group),
    )
    if dispatch_dtype_bytes_per_elem == 0:
        hidden_bytes = hidden_size // 2
    else:
        hidden_bytes = hidden_size * dispatch_dtype_bytes_per_elem
    total_dispatch_payload_size_per_token = (
        hidden_bytes
        + dispatch_scale_bytes_per_token
        + top_k * 4  # int32 topks ids
        + top_k * 4  # float32 topk weights
    )
    combine_payload_size_per_token = hidden_size * 2  # bf16 hidden states
    self.workspace_size = moe_a2a_get_workspace_size_per_rank(
        ep_size=self.world_size,
        max_num_tokens=max_num_tokens,
        total_dispatch_payload_size_per_token=total_dispatch_payload_size_per_token,
        combine_payload_size_per_token=combine_payload_size_per_token,
    )

    self.moe_alltoall = MoeAlltoAll(
        mapping=self.mapping,
        max_num_tokens=max_num_tokens,
        top_k=top_k,
        num_experts=num_experts,
        workspace_size_per_rank=self.workspace_size,
        mnnvl_config=ep_config,
    )

    self.gpus_per_node = gpus_per_node
    self.max_num_tokens = max_num_tokens
    self.top_k = top_k
    self.num_experts = num_experts
    self.hidden_size = hidden_size
    self.initialized = True

    logger.info(
        "FlashInfer One-sided NVLink initialized for rank %s, size %s",
        self.rank,
        self.world_size,
    )
    dist.barrier()
```

## FlashInferNVLinkTwoSidedManager [¶](#vllm.distributed.device_communicators.all2all.FlashInferNVLinkTwoSidedManager "Permanent link")

Bases: `All2AllManagerBase`

All2All communication based on flashinfer all2allv/two-sided NVLink kernels.

Source code in `vllm/distributed/device_communicators/all2all.py`

```
classFlashInferNVLinkTwoSidedManager(All2AllManagerBase):
"""
    All2All communication based on flashinfer all2allv/two-sided NVLink kernels.
    """

    # This type lint could be removed after all of the work in
    # https://github.com/vllm-project/vllm/issues/26533 done.
    rank: int
    world_size: int

    def__init__(self, cpu_group, tcp_store_group=None):
        assert has_flashinfer_nvlink_two_sided(), (
            "flashinfer all2all module not found. Please install/check flashinfer"
        )  # noqa
        super().__init__(cpu_group, tcp_store_group)
        logger.debug(
            "Initialize for flashinfer All2All rank=%d, world size=%d",
            self.rank,
            self.world_size,
        )
        self.initialized = False
        self.alltoall_info = None

    definitialize(
        self,
        world_size: int,
        rank: int,
        gpus_per_node: int,
    ):
"""Initialize workspace"""
        if self.initialized:
            return

        self.cleanup()
        logger.debug("making map: rank=%d, world size=%d", rank, world_size)
        self.mapping = Mapping(
            world_size,
            rank,
            gpus_per_node,
            tp_size=world_size,
        )

        fromvllm.distributed.device_communicators.mnnvl_compatimport (
            CustomCommunicator,
        )

        # MNNVL workspace is allocated per rank in the comm_backend's group; the
        # flashinfer kernel asserts workspace.size(0) == moe_ep_size, so the backend
        # must span the EP group (= DP*PCP*TP), not the DP group.
        ep_config = MnnvlConfig(
            comm_backend=CustomCommunicator(self.cpu_group),
            fabric_page_size=1 << 29,  # 512MB
            allocation_granularity=0,  # Auto-detect
        )

        self.workspace_tensor = MnnvlMoe.get_moe_workspaces(self.mapping, ep_config)
        self.prepare_workspace_tensor = MnnvlMoe.get_moe_prepare_workspace(
            self.mapping, ep_config
        )

        self.world_size = world_size
        self.rank = rank
        self.gpus_per_node = gpus_per_node
        self.initialized = True

        logger.info(
            "FlashInfer All2All initialized for rank %s, size %s", rank, world_size
        )

    defensure_alltoall_workspace_initialized(self):
"""Ensure workspace is initialized"""
        if not has_flashinfer_nvlink_two_sided():
            return False

        if self.world_size <= 1:
            return False

        if not self.initialized:
            self.initialize(
                world_size=self.world_size,
                rank=self.rank,
                gpus_per_node=torch.accelerator.device_count,
            )
        return self.initialized

    defget_handle(self, kwargs):
        return self

    defcleanup(self):
"""Clean up workspace"""
        if (
            self.initialized
            and self.workspace_tensor is not None
            and self.prepare_workspace_tensor is not None
        ):
            try:
                del self.workspace_tensor
                del self.prepare_workspace_tensor
            except Exception as e:
                logger.warning("Failed to cleanup FlashInfer workspace: %s", e)
            finally:
                self.workspace_tensor = None
                self.prepare_workspace_tensor = None
                self.mapping = None
                self.initialized = False
```

### cleanup [¶](#vllm.distributed.device_communicators.all2all.FlashInferNVLinkTwoSidedManager.cleanup "Permanent link")

Clean up workspace

Source code in `vllm/distributed/device_communicators/all2all.py`

```
defcleanup(self):
"""Clean up workspace"""
    if (
        self.initialized
        and self.workspace_tensor is not None
        and self.prepare_workspace_tensor is not None
    ):
        try:
            del self.workspace_tensor
            del self.prepare_workspace_tensor
        except Exception as e:
            logger.warning("Failed to cleanup FlashInfer workspace: %s", e)
        finally:
            self.workspace_tensor = None
            self.prepare_workspace_tensor = None
            self.mapping = None
            self.initialized = False
```

### ensure\_alltoall\_workspace\_initialized [¶](#vllm.distributed.device_communicators.all2all.FlashInferNVLinkTwoSidedManager.ensure_alltoall_workspace_initialized "Permanent link")

```
ensure_alltoall_workspace_initialized()
```

Ensure workspace is initialized

Source code in `vllm/distributed/device_communicators/all2all.py`

```
defensure_alltoall_workspace_initialized(self):
"""Ensure workspace is initialized"""
    if not has_flashinfer_nvlink_two_sided():
        return False

    if self.world_size <= 1:
        return False

    if not self.initialized:
        self.initialize(
            world_size=self.world_size,
            rank=self.rank,
            gpus_per_node=torch.accelerator.device_count,
        )
    return self.initialized
```

### initialize [¶](#vllm.distributed.device_communicators.all2all.FlashInferNVLinkTwoSidedManager.initialize "Permanent link")

```
initialize(world_size: int, rank: int, gpus_per_node: int)
```

Initialize workspace

Source code in `vllm/distributed/device_communicators/all2all.py`

```
definitialize(
    self,
    world_size: int,
    rank: int,
    gpus_per_node: int,
):
"""Initialize workspace"""
    if self.initialized:
        return

    self.cleanup()
    logger.debug("making map: rank=%d, world size=%d", rank, world_size)
    self.mapping = Mapping(
        world_size,
        rank,
        gpus_per_node,
        tp_size=world_size,
    )

    fromvllm.distributed.device_communicators.mnnvl_compatimport (
        CustomCommunicator,
    )

    # MNNVL workspace is allocated per rank in the comm_backend's group; the
    # flashinfer kernel asserts workspace.size(0) == moe_ep_size, so the backend
    # must span the EP group (= DP*PCP*TP), not the DP group.
    ep_config = MnnvlConfig(
        comm_backend=CustomCommunicator(self.cpu_group),
        fabric_page_size=1 << 29,  # 512MB
        allocation_granularity=0,  # Auto-detect
    )

    self.workspace_tensor = MnnvlMoe.get_moe_workspaces(self.mapping, ep_config)
    self.prepare_workspace_tensor = MnnvlMoe.get_moe_prepare_workspace(
        self.mapping, ep_config
    )

    self.world_size = world_size
    self.rank = rank
    self.gpus_per_node = gpus_per_node
    self.initialized = True

    logger.info(
        "FlashInfer All2All initialized for rank %s, size %s", rank, world_size
    )
```

## NixlEPAll2AllManager [¶](#vllm.distributed.device_communicators.all2all.NixlEPAll2AllManager "Permanent link")

Bases: `All2AllManagerBase`

All2All communication based on NIXL EP kernels. This backend supports elastic EP with dynamic rank connection/disconnection.

Source code in `vllm/distributed/device_communicators/all2all.py`

```
classNixlEPAll2AllManager(All2AllManagerBase):
"""
    All2All communication based on NIXL EP kernels.
    This backend supports elastic EP with dynamic rank connection/disconnection.
    """

    # (nixl_ep_buffer, ep_size)
    _buffer: tuple[Any, int] | None = None
    _lock = threading.Lock()

    def__init__(self, cpu_group, tcp_store_group=None):
        super().__init__(cpu_group, tcp_store_group)

        self.max_num_ep_ranks = envs.VLLM_NIXL_EP_MAX_NUM_RANKS

    def_init_buffer(
        self,
        max_num_tokens_per_dp_rank: int,
        token_hidden_size: int,
        num_experts_per_rank: int,
    ) -> None:
        fromnixl_epimport Buffer  # type: ignore[import-not-found]

        max_num_global_experts = self.max_num_ep_ranks * num_experts_per_rank
        num_rdma_bytes = Buffer.get_rdma_size_hint(
            num_max_dispatch_tokens_per_rank=max_num_tokens_per_dp_rank,
            hidden=token_hidden_size,
            num_ranks=self.max_num_ep_ranks,
            num_experts=max_num_global_experts,
        )
        assert NixlEPAll2AllManager._buffer is None, (
            "NIXL EP buffer already initialized"
        )
        buffer = Buffer(
            rank=self.rank,
            tcp_store_group=self.tcp_store_group.store,
        )
        buffer.update_memory_buffers(
            num_ranks=self.max_num_ep_ranks,
            num_experts_per_rank=num_experts_per_rank,
            num_rdma_bytes=num_rdma_bytes,
        )
        ranks_to_connect = list(range(self.cpu_group.size()))
        buffer.connect_ranks(ranks_to_connect)
        NixlEPAll2AllManager._buffer = (buffer, self.cpu_group.size())

    def_update_buffer(self):
        assert NixlEPAll2AllManager._buffer is not None
        buffer, current_ep_size = NixlEPAll2AllManager._buffer
        current_ranks = list(range(current_ep_size))
        new_ep_size = self.cpu_group.size()
        buffer.set_tcp_store_group(self.tcp_store_group.store)
        if new_ep_size > len(current_ranks):
            ranks_to_connect = list(range(len(current_ranks), new_ep_size))
            buffer.connect_ranks(ranks_to_connect)
        else:
            ranks_to_disconnect = current_ranks[new_ep_size:]
            buffer.disconnect_ranks(ranks_to_disconnect)
        NixlEPAll2AllManager._buffer = (buffer, new_ep_size)

    defget_handle(self, kwargs):
        with NixlEPAll2AllManager._lock:
            if (
                NixlEPAll2AllManager._buffer is not None
                and NixlEPAll2AllManager._buffer[1] == self.cpu_group.size()
            ):
                return NixlEPAll2AllManager._buffer[0]

            num_experts_per_rank = (
                kwargs["num_global_experts"] // kwargs["num_ep_ranks"]
            )
            nixl_kwargs = dict(
                max_num_tokens_per_dp_rank=kwargs["max_num_tokens_per_dp_rank"],
                token_hidden_size=kwargs["token_hidden_size"],
                num_experts_per_rank=num_experts_per_rank,
            )
            if NixlEPAll2AllManager._buffer is None:
                self._init_buffer(**nixl_kwargs)
            else:
                self._update_buffer()

            assert NixlEPAll2AllManager._buffer is not None
            handle = NixlEPAll2AllManager._buffer[0]
            return handle

    defdispatch(
        self,
        hidden_states: torch.Tensor,
        topk_weights: torch.Tensor,
        topk_ids: torch.Tensor,
        is_sequence_parallel: bool = False,
        extra_tensors: list[torch.Tensor] | None = None,
    ) -> (
        tuple[torch.Tensor, torch.Tensor, torch.Tensor]
        | tuple[torch.Tensor, torch.Tensor, torch.Tensor, list[torch.Tensor]]
    ):
        raise NotImplementedError

    defcombine(
        self, hidden_states: torch.Tensor, is_sequence_parallel: bool = False
    ) -> torch.Tensor:
        raise NotImplementedError

    defdestroy(self):
        # NOTE(yongji): NIXLEPAll2AllManager instance is recreated during
        # scale-up/down, so we cannot destroy the persistent buffer here.
        assert NixlEPAll2AllManager._buffer is not None
        buffer = NixlEPAll2AllManager._buffer[0]
        buffer.set_tcp_store_group(None)

    # NIXL EP uses RDMA so no SMs are used for communication
    defmax_sms_used(self) -> int | None:
        return 0
```