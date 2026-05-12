---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/utils/
source: sitemap
fetched_at: 2026-05-07T21:18:07.988690618-03:00
rendered_js: false
word_count: 101
summary: This class serves as the central configuration and logic provider for managing KV cache topology, tensor parallel alignment, and inter-engine communication in distributed inference systems.
tags:
    - distributed-inference
    - kv-cache
    - tensor-parallelism
    - engine-coordination
    - memory-management
    - topology-mapping
category: concept
---

```
@dataclass
classTransferTopology:
"""Single source of truth for local TP identity and per-engine remote info."""

    tp_rank: int
    tp_size: int
    block_size: int
    engine_id: EngineId
    is_mla: bool
    is_mamba: bool
    total_num_kv_heads: int
    attn_backends: list[type[AttentionBackend]]
    tensor_shape: torch.Size | None = None

    def__post_init__(self):
        self.local_physical_heads = max(1, self.total_num_kv_heads // self.tp_size)

        self._engines: dict[EngineId, EngineTransferInfo] = {}

        # Figure out whether the first dimension of the cache is K/V
        # or num_blocks.
        attn_backend = self.attn_backends[0]
        if not self.is_mamba:
            _MOCK_BLOCK_SIZE = 16
            kv_cache_shape: tuple[int, ...] = attn_backend.get_kv_cache_shape(
                num_blocks=1,
                block_size=_MOCK_BLOCK_SIZE,
                num_kv_heads=1,
                head_size=1,
            )
            logger.debug("Test kv_cache_shape: %s", kv_cache_shape)
        # Non-MLA backends caches have 5 dims [2, num_blocks, H,N,D],
        # we just mock num_blocks to 1 for the dimension check below.
        # Hybrid SSM models assume a single blocks_first layout
        self._is_kv_layout_blocks_first = self.is_mamba or (
            len(kv_cache_shape) == 5 and kv_cache_shape[0] == 1
        )

        self._cross_layers_blocks = False
        if self.tensor_shape is not None:
            self._cross_layers_blocks = (
                len(self.tensor_shape) == len(kv_cache_shape) + 1
            )

        if self._cross_layers_blocks:
            logger.debug("Using cross-layer KV cache")
            _MOCK_NUM_LAYERS = 80
            kv_cache_shape = (_MOCK_NUM_LAYERS,) + kv_cache_shape
            try:
                kv_cache_stride_order = attn_backend.get_kv_cache_stride_order(
                    include_num_layers_dimension=self._cross_layers_blocks
                )
            except (AttributeError, NotImplementedError):
                assert self.tensor_shape is not None
                kv_cache_stride_order = tuple(range(len(self.tensor_shape)))
            kv_cache_shape = tuple(kv_cache_shape[i] for i in kv_cache_stride_order)

    # ============================================================
    # Engine registration
    # ============================================================

    defregister_remote_engine(
        self,
        remote_engine_id: EngineId,
        info: EngineTransferInfo,
    ) -> EngineTransferInfo:
"""Register a remote engine, unifying worker dicts state.

        The caller (worker) is responsible for computing the info via
        the transfer policy.  This method only stores and deduplicates.
        """
        assert remote_engine_id != self.engine_id, (
            f"Cannot register local engine {self.engine_id} as remote. "
            f"Local identity is set via __init__ params."
        )
        if remote_engine_id in self._engines:
            return self._engines[remote_engine_id]
        self._engines[remote_engine_id] = info
        return info

    defget_engine_info(self, remote_engine_id: EngineId) -> EngineTransferInfo:
        return self._engines[remote_engine_id]

    # ============================================================
    # Layout properties
    # ============================================================

    @property
    defis_kv_layout_blocks_first(self) -> bool:
        return self._is_kv_layout_blocks_first

    @property
    defcross_layers_blocks(self) -> bool:
        return self._cross_layers_blocks

    @property
    defsplit_k_and_v(self) -> bool:
        # Whether to register regions for K and V separately (when present).
        return not (
            self._cross_layers_blocks or self.is_mla or self.is_kv_layout_blocks_first
        )

    # ============================================================
    # Common methods
    # ============================================================

    deftp_ratio(self, remote_tp_size: int) -> int:
"""Calculate the tensor parallel ratio between local and remote TP.

        Positive when local_tp >= remote_tp (local workers read from the
        same remote worker in groups of size ``tp_ratio``).  Negative when
        remote_tp > local_tp (ratio is flipped).
        """
        if self.tp_size >= remote_tp_size:
            assert self.tp_size % remote_tp_size == 0, (
                f"Local tensor parallel size {self.tp_size} is not divisible "
                f"by remote tensor parallel size {remote_tp_size}."
            )
            return self.tp_size // remote_tp_size
        assert remote_tp_size % self.tp_size == 0, (
            f"Remote tensor parallel size {remote_tp_size} is not divisible "
            f"by local tensor parallel size {self.tp_size}."
        )
        return -(remote_tp_size // self.tp_size)

    defblock_size_ratio(self, remote_block_size: int) -> int:
"""Calculate the block size ratio between local and remote."""
        assert self.block_size % remote_block_size == 0, (
            f"Local block size {self.block_size} is not divisible "
            f"by remote block size {remote_block_size} or vice versa."
        )
        return self.block_size // remote_block_size

    defis_kv_replicated(self, remote_engine_id: EngineId) -> bool:
"""Whether the KV cache is replicated across TP workers due to the
        number of TP workers being greater than the number of KV heads.
        """
        return self._engines[remote_engine_id].remote_tp_size > self.total_num_kv_heads

    defreplicates_kv_cache(self, remote_engine_id: EngineId) -> bool:
        # MLA is always replicated as the hidden dim can't be split.
        return self.is_mla or self.is_kv_replicated(remote_engine_id)

    @property
    deflocal_replicates_kv_cache(self) -> bool:
"""Whether the local engine's KV cache is replicated."""
        return self.is_mla or self.tp_size > self.total_num_kv_heads

    defhandshake_target_ranks(self, remote_tp_size: int) -> list[int]:
"""Pre-registration: compute which remote TP ranks to handshake with.

        Pure math based on local/remote TP sizes — does not require
        the remote engine to be registered yet.
        """
        tp_ratio = self.tp_ratio(remote_tp_size)
        if tp_ratio > 0:
            return [self.tp_rank // tp_ratio]
        abs_ratio = -tp_ratio
        return [self.tp_rank * abs_ratio + i for i in range(abs_ratio)]

    deftarget_remote_ranks(self, remote_engine_id: EngineId) -> list[int]:
"""Get the remote TP rank(s) that the current local TP rank will
        read from.  When remote tp_size > local tp_size, reads from
        multiple remote ranks.
        """
        info = self._engines[remote_engine_id]
        tp_ratio = self.tp_ratio(info.remote_tp_size)
        if tp_ratio > 0:
            return [self.tp_rank // tp_ratio]
        # remote TP > local TP: read from |tp_ratio| remote workers
        abs_ratio = -tp_ratio
        return [self.tp_rank * abs_ratio + i for i in range(abs_ratio)]

    defget_transfer_cache_regions(
        self, cache: torch.Tensor, layer_spec: "KVCacheSpec"
    ) -> list[torch.Tensor] | torch.Tensor:
"""Return the cache tensor(s) to register as NIXL memory regions,
        also accounting for hybrid SSM models specificities.
        """
        if isinstance(layer_spec, MambaSpec):
            # Register the whole kv cache shared tensor, including
            # SSM/Conv.
            conv, ssm = cache
            return [conv]

        # Check may be hacky but it's matching
        # `_update_hybrid_attention_mamba_layout`.
        if self.is_mamba and cache.shape[0] == 2:
            # When MAMBA is present, all backends are blocks first, so
            # that blocks can be shared between attention layers and mamba
            # layers.  Runner already adjusted strides for FlashAttn-like
            # backends so its num_blocks first.
            # Swap [2<>num_blocks] dims for hybrid SSM layout.
            cache = cache.transpose(0, 1)

        # Regular case: backends like FA register K/V in separate regions
        return cache if self.split_k_and_v else [cache]

    defdescribe(self, remote_engine_id: EngineId) -> str:
"""One-line summary of transfer config for logging."""
        info = self._engines[remote_engine_id]
        return (
            f"TransferTopology("
            f"tp_ratio={self.tp_ratio(info.remote_tp_size)}, "
            f"K={self.total_num_kv_heads}, "
            f"local_tp={self.tp_size}, "
            f"remote_tp={info.remote_tp_size}, "
            f"local_rank={self.tp_rank}, "
            f"remote_block_len={info.remote_block_len})"
        )
```