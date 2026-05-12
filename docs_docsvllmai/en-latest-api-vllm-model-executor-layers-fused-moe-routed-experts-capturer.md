---
title: routed_experts_capturer - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/routed_experts_capturer/
source: sitemap
fetched_at: 2026-05-07T21:25:24.971056443-03:00
rendered_js: false
word_count: 0
summary: Implements a high-performance routed expert data capturer for MoE models using asynchronous device-to-host memory transfers and optimized host-side scattering.
tags:
    - moe
    - cuda-streams
    - memory-optimization
    - data-capture
    - gpu-programming
    - async-copy
category: reference
---

```
class_RoutedExpertsCapturerReal(RoutedExpertsCapturer):
"""Capturer with GPU device cache and CPU host cache.

    Performance strategy -- async D2H with optimized host-cache scatter:

    Every decode step we issue a non-blocking D2H copy on a dedicated
    CUDA stream.  The scatter into per-request host-cache buffers is
    deferred to the start of the NEXT step (by which time the copy has
    finished).  The scatter loop is optimized with direct scalar access
    to avoid numpy slice views, int() conversions, and .max() calls.

    At extraction time (when a request finishes), data is already in a
    contiguous host buffer -- just a numpy slice, no concatenation.
    """

    def__init__(
        self,
        model_config: ModelConfig,
        max_num_batched_tokens: int,
        num_fused_shared_experts: int,
        max_model_len: int,
        device: str,
        shared_host_cache: _RoutedExpertsHostCache | None = None,
        skip_host_cache: bool = False,
    ):
        self.num_fused_shared_experts = num_fused_shared_experts
        self.num_hidden_layers = _count_moe_layers(model_config.hf_text_config)
        self.num_experts_per_tok = model_config.hf_text_config.num_experts_per_tok
        self.max_num_batched_tokens = max_num_batched_tokens
        self.max_model_len = max_model_len
        self._skip_host_cache = skip_host_cache

        if skip_host_cache:
            self.host_cache = None
            logger.info("Skipping host cache for device %s (non-rank-0)", device)
        elif shared_host_cache is not None:
            self.host_cache = shared_host_cache
        else:
            self.host_cache = _RoutedExpertsHostCache(
                num_hidden_layers=self.num_hidden_layers,
                num_experts_per_tok=self.num_experts_per_tok,
                max_model_len=self.max_model_len,
            )

        self.device_cache = _RoutedExpertsDeviceCache(
            max_num_batched_tokens=self.max_num_batched_tokens,
            num_hidden_layers=self.num_hidden_layers,
            num_experts_per_tok=self.num_experts_per_tok,
            device=device,
        )

        # ---- Async D2H pipeline (rank-0 only) ----
        # Non-rank-0 workers only need the device buffer for symmetric
        # CUDA graph capture; they skip the D2H pipeline entirely.
        self._has_pending_copy = False
        self._pending_positions: np.ndarray | None = None
        self._pending_num_scheduled: dict[str, int] | None = None
        self._pending_total_tokens: int = 0

        if not skip_host_cache:
            # Same (L, N, K) layout as device_cache.buffer.
            self._pinned_staging = torch.zeros(
                (
                    self.num_hidden_layers,
                    max_num_batched_tokens,
                    self.num_experts_per_tok,
                ),
                dtype=_RoutedExpertsDeviceCache.DTYPE,
                pin_memory=True,
            )
            # Private device snapshot: source for the async D2H. Decouples
            # the in-flight copy from device_cache.buffer, which the next
            # step's MoE writes overwrite in place on main_stream.
            self._device_staging = torch.empty_like(self.device_cache.buffer)
            self._copy_stream = torch.cuda.Stream(device=device)
            self._copy_event = torch.cuda.Event()

            pinned_mb = self._pinned_staging.nbytes / _MB
            logger.info(
                "Routing experts pinned staging buffer allocated. "
                "shape=%s, size=%.2f MB",
                tuple(self._pinned_staging.shape),
                pinned_mb,
            )
        else:
            self._pinned_staging = None
            self._device_staging = None
            self._copy_stream = None
            self._copy_event = None
            logger.info(
                "Routing experts device-only capturer (rank != 0). "
                "Device buffer shape=%s",
                tuple(self.device_cache.buffer.shape),
            )

    defcapture(self, layer_id: int, topk_ids: torch.Tensor):
        self.device_cache.capture_fwd_routed_experts(layer_id, topk_ids)

    # ------------------------------------------------------------------
    # sync_fwd_experts_buffer_DtoH -- called AFTER the forward pass
    # ------------------------------------------------------------------

    defsync_fwd_experts_buffer_DtoH(
        self,
        positions: torch.Tensor,
        num_scheduled_tokens: dict[str, int],
    ):
        if self.host_cache is None:
            return

        # 1. Finalize previous async copy -- the copy had an entire
        #    forward pass to complete so event.synchronize() is ~free.
        if self._has_pending_copy:
            self._copy_event.synchronize()
            self._scatter_to_host()
            self._has_pending_copy = False

        total_tokens = sum(num_scheduled_tokens.values())
        if total_tokens == 0:
            return

        # 2. Snapshot the device buffer on main_stream into a private
        #    staging buffer, then issue the D2H from the staging buffer
        #    on a dedicated copy stream. The snapshot serializes after
        #    the current step's MoE writes (same stream) and is private
        #    from the next step's MoE writes, so the in-flight D2H is
        #    not aliased by step N+1's forward under async scheduling.
        main_stream = torch.cuda.current_stream(self._copy_stream.device)
        self._device_staging[:, :total_tokens, :].copy_(
            self.device_cache.buffer[:, :total_tokens, :], non_blocking=True
        )
        with torch.cuda.stream(self._copy_stream):
            self._copy_stream.wait_stream(main_stream)
            self._pinned_staging[:, :total_tokens, :].copy_(
                self._device_staging[:, :total_tokens, :], non_blocking=True
            )
            self._copy_event.record()

        # 3. Save metadata for deferred scatter.
        self._pending_positions = positions.numpy().copy()
        self._pending_num_scheduled = num_scheduled_tokens
        self._pending_total_tokens = total_tokens
        self._has_pending_copy = True

    # ------------------------------------------------------------------
    # Optimized scatter into pre-allocated host-cache buffers
    # ------------------------------------------------------------------

    def_scatter_to_host(self):
"""Scatter D2H data into per-request host cache buffers.

        Staging layout is (L, N, K).  Host cache layout is (seq_len, L, K).
        We transpose the staging slice to (N, L, K) before scattering so
        that indexing by token position naturally yields (L, K) rows.
        """
        # Transpose (L, N, K) -> (N, L, K) for the active token range.
        host_values = (
            self._pinned_staging[:, : self._pending_total_tokens, :]
            .numpy()
            .transpose(1, 0, 2)
        )
        positions_np = self._pending_positions
        host_cache = self.host_cache
        assert self._pending_num_scheduled is not None
        assert positions_np is not None
        assert host_cache is not None

        offset = 0
        for req_id, n_tokens in self._pending_num_scheduled.items():
            if n_tokens == 0:
                continue

            if n_tokens == 1:
                pos_val = int(positions_np[offset])
                buf = host_cache.get_or_grow_buffer(req_id, pos_val)
                buf[pos_val] = host_values[offset]
                host_cache.update_filled_len(req_id, pos_val)
            else:
                pos = positions_np[offset : offset + n_tokens]
                max_pos = int(pos[-1]) if n_tokens > 0 else 0
                if n_tokens > 1:
                    max_pos = int(pos.max())
                buf = host_cache.get_or_grow_buffer(req_id, max_pos)
                buf[pos] = host_values[offset : offset + n_tokens]
                host_cache.update_filled_len(req_id, max_pos)

            offset += n_tokens

        self._pending_positions = None
        self._pending_num_scheduled = None
        self._pending_total_tokens = 0

    # ------------------------------------------------------------------
    # finalize_pending_copy -- call before reading host cache
    # ------------------------------------------------------------------

    deffinalize_pending_copy(self):
"""Ensure the most recent async D2H copy has been scattered into
        host cache buffers.  Call before get_routed_experts."""
        if self._has_pending_copy:
            self._copy_event.synchronize()
            self._scatter_to_host()
            self._has_pending_copy = False

    # ------------------------------------------------------------------
    # Extraction -- O(1), just a numpy slice
    # ------------------------------------------------------------------

    defget_routed_experts(
        self,
        req_id: str,
        seqlen: int | None = None,
        free_slot: bool = True,
    ):
        if self.host_cache is None:
            return None
        buf = self.host_cache.get_buffer(req_id)
        if buf is None:
            return None
        filled = self.host_cache.get_filled_len(req_id)
        if filled <= 0:
            return None
        effective_len = min(filled, seqlen) if seqlen is not None else filled
        result = buf[:effective_len].copy()
        if free_slot:
            self.host_cache.free_request(req_id)
        return result

    defget_host_cache(self):
        return self.host_cache

    defget_device_cache(self):
        return self.device_cache
```