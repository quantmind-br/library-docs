---
title: trtllm_ragged - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/attention/backends/mla/prefill/trtllm_ragged/
source: sitemap
fetched_at: 2026-05-07T21:39:32.076960364-03:00
rendered_js: false
word_count: 0
summary: This document defines the TRTLLM-Ragged backend implementation for MLA (Multi-Head Latent Attention) prefill operations in a VLLM environment, leveraging FlashInfer for accelerated attention computation.
tags:
    - trt-llm
    - mla
    - flashinfer
    - prefill-backend
    - attention-optimization
    - vllm-integration
category: reference
---

```
classTrtllmRaggedPrefillBackend(MLAPrefillBackend):
"""TRT-LLM Ragged backend for MLA prefill."""

    requires_r1_mla_dimensions = True

    @staticmethod
    defget_name() -> str:
        return "TRTLLM_RAGGED"

    @classmethod
    defsupports_compute_capability(cls, device_capability: "DeviceCapability") -> bool:
        return device_capability.major == 10

    @classmethod
    defis_available(cls) -> bool:
        try:
            fromflashinfer.prefillimport (
                trtllm_ragged_attention_deepseek,  # noqa: F401
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

    def_get_workspace_buffer(self) -> torch.Tensor:
        (workspace_buffer,) = current_workspace_manager().get_simultaneous(
            (
                (envs.VLLM_FLASHINFER_WORKSPACE_BUFFER_SIZE,),
                torch.uint8,
            ),
        )
        return workspace_buffer

    defprepare_metadata(
        self,
        prefill_metadata: "MLACommonPrefillMetadata",
    ) -> None:
        super().prepare_metadata(prefill_metadata)
        self._query_seq_lens = (
            prefill_metadata.query_start_loc[1:] - prefill_metadata.query_start_loc[:-1]
        )

    defrun_prefill_new_tokens(
        self,
        q: torch.Tensor,
        k: torch.Tensor,
        v: torch.Tensor,
        return_softmax_lse: bool,
    ) -> torch.Tensor | tuple[torch.Tensor, torch.Tensor]:
        fromflashinfer.prefillimport trtllm_ragged_attention_deepseek

        workspace_buffer = self._get_workspace_buffer()
        out = torch.empty(
            q.shape[0],
            q.shape[1],
            v.shape[2],
            device=q.device,
            dtype=self._prefill_metadata.output_dtype,
        )

        ret = trtllm_ragged_attention_deepseek(
            query=q,
            key=k,
            value=v,
            workspace_buffer=workspace_buffer,
            seq_lens=self._query_seq_lens,
            max_q_len=self._prefill_metadata.max_query_len,
            max_kv_len=self._prefill_metadata.max_query_len,
            bmm1_scale=self.scale,
            bmm2_scale=1.0,
            o_sf_scale=1.0,
            batch_size=self._query_seq_lens.shape[0],
            window_left=-1,
            cum_seq_lens_q=self._prefill_metadata.query_start_loc,
            cum_seq_lens_kv=self._prefill_metadata.query_start_loc,
            enable_pdl=False,
            is_causal=True,
            return_lse=return_softmax_lse,
            out=out,
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
        fromflashinfer.prefillimport trtllm_ragged_attention_deepseek

        assert self._prefill_metadata.chunked_context is not None
        assert self._prefill_metadata.chunked_context.seq_lens[chunk_idx] is not None
        workspace_buffer = self._get_workspace_buffer()

        out = torch.empty(
            q.shape[0],
            q.shape[1],
            v.shape[2],
            device=q.device,
            dtype=self._prefill_metadata.output_dtype,
        )

        attn_out, lse = trtllm_ragged_attention_deepseek(
            query=q,
            key=k,
            value=v,
            workspace_buffer=workspace_buffer,
            seq_lens=self._prefill_metadata.chunked_context.seq_lens[chunk_idx],
            max_q_len=self._prefill_metadata.max_query_len,
            max_kv_len=self._prefill_metadata.chunked_context.max_seq_lens[chunk_idx],
            bmm1_scale=self.scale,
            bmm2_scale=1.0,
            o_sf_scale=1.0,
            batch_size=self._prefill_metadata.chunked_context.seq_lens[chunk_idx].shape[
                0
            ],
            window_left=-1,
            cum_seq_lens_q=self._prefill_metadata.query_start_loc,
            cum_seq_lens_kv=self._prefill_metadata.chunked_context.cu_seq_lens[
                chunk_idx
            ],
            enable_pdl=False,
            is_causal=False,
            return_lse=True,
            out=out,
        )

        # Convert from (q_len, num_heads) to (num_heads, q_len)
        return attn_out, lse.transpose(0, 1).contiguous()
```