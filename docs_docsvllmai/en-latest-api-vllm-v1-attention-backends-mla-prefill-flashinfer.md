---
title: flashinfer - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/attention/backends/mla/prefill/flashinfer/
source: sitemap
fetched_at: 2026-05-07T21:39:29.185199137-03:00
rendered_js: false
word_count: 0
summary: This class implements a FlashInfer-based backend for Multi-Head Latent Attention (MLA) prefill operations in a VLLM-compatible environment. It manages prefill planning, workspace buffers, and execution of attention kernels for both standard and chunked sequence processing.
tags:
    - flashinfer
    - mla-attention
    - prefill-optimization
    - vllm-backend
    - attention-kernels
    - ragged-kv-cache
category: api
---

```
classFlashInferPrefillBackend(MLAPrefillBackend):
"""FlashInfer backend for MLA prefill."""

    requires_r1_mla_dimensions = True

    @staticmethod
    defget_name() -> str:
        return "FLASHINFER"

    @classmethod
    defsupports_compute_capability(cls, device_capability: "DeviceCapability") -> bool:
        return device_capability.major == 10

    @classmethod
    defis_available(cls) -> bool:
        try:
            fromflashinferimport (
                BatchPrefillWithRaggedKVCacheWrapper,  # noqa: F401
            )

            return True
        except ImportError:
            return False

    def__init__(
        self,
        num_heads: int,
        scale: float,
        kv_lora_rank: int,
        qk_nope_head_dim: int,
        qk_rope_head_dim: int,
        v_head_dim: int,
        vllm_config: "VllmConfig",
    ) -> None:
        super().__init__(
            num_heads=num_heads,
            scale=scale,
            kv_lora_rank=kv_lora_rank,
            qk_nope_head_dim=qk_nope_head_dim,
            qk_rope_head_dim=qk_rope_head_dim,
            v_head_dim=v_head_dim,
            vllm_config=vllm_config,
        )

        self._prefill_main: BatchPrefillWithRaggedKVCacheWrapper | None = None
        self._prefill_chunks: list[BatchPrefillWithRaggedKVCacheWrapper] = []
        self._global_hyperparameters: PerLayerParameters | None = None

    def_ensure_chunks(
        self,
        num_chunks: int,
        workspace_buffer: torch.Tensor,
    ) -> None:
        if len(self._prefill_chunks) < num_chunks:
            for _ in range(len(self._prefill_chunks), num_chunks):
                self._prefill_chunks.append(
                    BatchPrefillWithRaggedKVCacheWrapper(
                        workspace_buffer, "NHD", backend="cutlass"
                    )
                )

    def_resolve_global_hyperparameters(self) -> PerLayerParameters:
        if self._global_hyperparameters is not None:
            return self._global_hyperparameters

        fromvllm.model_executor.layers.attention.mla_attentionimport (
            MLAAttention,
            MLACommonImpl,
        )

        forward_context = self.vllm_config.compilation_config.static_forward_context
        layer_names = [
            name
            for name, layer in forward_context.items()
            if isinstance(layer, MLAAttention)
        ]

        self._global_hyperparameters = infer_global_hyperparameters(
            get_per_layer_parameters(
                self.vllm_config,
                layer_names,
                MLACommonImpl,  # type: ignore[type-abstract]
            )
        )
        return self._global_hyperparameters

    defprepare_metadata(
        self,
        prefill_metadata: "MLACommonPrefillMetadata",
    ) -> None:
        global_hyperparameters = self._resolve_global_hyperparameters()
        qo_indptr = prefill_metadata.query_start_loc
        has_context = prefill_metadata.chunked_context is not None
        (workspace_buffer,) = current_workspace_manager().get_simultaneous(
            ((envs.VLLM_FLASHINFER_WORKSPACE_BUFFER_SIZE,), torch.uint8),
        )

        if self._prefill_main is None:
            self._prefill_main = BatchPrefillWithRaggedKVCacheWrapper(
                workspace_buffer, "NHD", backend="cutlass"
            )
            self._ensure_chunks(_DEFAULT_NUM_CHUNKS, workspace_buffer)

        if has_context:
            chunked_context = prefill_metadata.chunked_context
            assert chunked_context is not None
            num_chunks = chunked_context.cu_seq_lens.shape[0]
            self._ensure_chunks(num_chunks, workspace_buffer)

        num_qo_heads = self.num_heads
        num_kv_heads = num_qo_heads

        head_dim_qk = self.qk_nope_head_dim + self.qk_rope_head_dim
        head_dim_vo = self.v_head_dim
        kv_indptr = qo_indptr.clone()

        assert self._prefill_main is not None
        self._prefill_main.plan(
            qo_indptr=qo_indptr,
            kv_indptr=kv_indptr,
            num_qo_heads=num_qo_heads,
            num_kv_heads=num_kv_heads,
            head_dim_qk=head_dim_qk,
            head_dim_vo=head_dim_vo,
            causal=True,
            sm_scale=global_hyperparameters.sm_scale,
            window_left=global_hyperparameters.window_left,
            logits_soft_cap=global_hyperparameters.logits_soft_cap,
            q_data_type=prefill_metadata.q_data_type,
            o_data_type=prefill_metadata.output_dtype,
        )

        if has_context:
            chunked_context = prefill_metadata.chunked_context
            assert chunked_context is not None
            for i in range(num_chunks):
                kv_indptr_chunk = chunked_context.cu_seq_lens[i]

                self._prefill_chunks[i].plan(
                    qo_indptr=qo_indptr,
                    kv_indptr=kv_indptr_chunk,
                    num_qo_heads=num_qo_heads,
                    num_kv_heads=num_kv_heads,
                    head_dim_qk=head_dim_qk,
                    head_dim_vo=head_dim_vo,
                    causal=False,
                    sm_scale=global_hyperparameters.sm_scale,
                    window_left=global_hyperparameters.window_left,
                    logits_soft_cap=global_hyperparameters.logits_soft_cap,
                    q_data_type=prefill_metadata.q_data_type,
                    o_data_type=prefill_metadata.output_dtype,
                )

    defrun_prefill_new_tokens(
        self,
        q: torch.Tensor,
        k: torch.Tensor,
        v: torch.Tensor,
        return_softmax_lse: bool,
    ) -> torch.Tensor | tuple[torch.Tensor, torch.Tensor]:
        assert self._prefill_main is not None

        ret = self._prefill_main.run(
            q=q,
            k=k,
            v=v,
            return_lse=return_softmax_lse,
        )

        if isinstance(ret, tuple):
            # Convert from (q_len, num_heads) to (num_heads, q_len)
            return ret[0], ret[1].transpose(0, 1).contiguous()
        return ret

    defrun_prefill_context_chunk(
        self,
        chunk_idx: int,
        q: torch.Tensor,
        k: torch.Tensor,
        v: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        attn_out, lse = self._prefill_chunks[chunk_idx].run(
            q=q,
            k=k,
            v=v,
            return_lse=True,
        )

        # Convert from (q_len, num_heads) to (num_heads, q_len)
        return attn_out, lse.transpose(0, 1).contiguous()
```