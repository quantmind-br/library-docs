---
title: xdrope - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/rotary_embedding/xdrope/
source: sitemap
fetched_at: 2026-05-07T21:28:30.10645248-03:00
rendered_js: false
word_count: 0
summary: This document defines the XDRotaryEmbedding class, which extends dynamic NTK-aware rotary positional embeddings to support multimodal data sections for query and key transformation.
tags:
    - rotary-embeddings
    - multimodal-learning
    - pytorch
    - positional-encoding
    - attention-mechanism
    - cuda-optimization
category: api
---

```
classXDRotaryEmbedding(DynamicNTKAlphaRotaryEmbedding):
"""DynamicNTKAlphaRotaryEmbedding extended with MultiModal(XD) Sections.

    Based on the original DynamicNTKAlphaRotaryEmbedding implementation.
    """

    def__init__(
        self,
        head_size: int,
        rotary_dim: int,
        max_position_embeddings: int,
        base: float,
        is_neox_style: bool,
        scaling_alpha: float,
        dtype: torch.dtype,
        xdrope_section: list[int],
    ) -> None:
        self.xdrope_section = xdrope_section
        super().__init__(
            head_size,
            rotary_dim,
            max_position_embeddings,
            base,
            is_neox_style,
            scaling_alpha,
            dtype,
        )

    defforward_native(
        self,
        positions: torch.Tensor,
        query: torch.Tensor,
        key: torch.Tensor | None = None,
        offsets: torch.Tensor | None = None,
    ) -> tuple[torch.Tensor, torch.Tensor | None]:
"""PyTorch-native implementation equivalent to forward().

        Args:
            positions:
                [4, num_tokens] (P/W/H/T positions with multimodal inputs)
            query: [num_tokens, num_heads * head_size]
            key: [num_tokens, num_kv_heads * head_size]
        """
        assert positions.ndim == 2
        assert key is not None

        num_tokens = positions.shape[-1]
        cos_sin = self.cos_sin_cache[positions]
        cos, sin = cos_sin.chunk(2, dim=-1)
        cos = torch.cat(
            [m[i] for i, m in enumerate(cos.split(self.xdrope_section, dim=-1))], dim=-1
        )
        sin = torch.cat(
            [m[i] for i, m in enumerate(sin.split(self.xdrope_section, dim=-1))], dim=-1
        )

        query_shape = query.shape
        query = query.view(num_tokens, -1, self.head_size)
        query_rot = query[..., : self.rotary_dim]
        query_pass = query[..., self.rotary_dim :]
        query_rot = self.apply_rotary_emb.forward_native(
            query_rot,
            cos,
            sin,
        )
        query = torch.cat((query_rot, query_pass), dim=-1).reshape(query_shape)

        key_shape = key.shape
        key = key.view(num_tokens, -1, self.head_size)
        key_rot = key[..., : self.rotary_dim]
        key_pass = key[..., self.rotary_dim :]
        key_rot = self.apply_rotary_emb.forward_native(
            key_rot,
            cos,
            sin,
        )
        key = torch.cat((key_rot, key_pass), dim=-1).reshape(key_shape)
        return query, key

    defforward_cuda(
        self,
        positions: torch.Tensor,
        query: torch.Tensor,
        key: torch.Tensor | None = None,
        offsets: torch.Tensor | None = None,
    ) -> tuple[torch.Tensor, torch.Tensor | None]:
"""PyTorch-native implementation equivalent to forward().

        Args:
            positions:
                [4, num_tokens] (P/W/H/T positions with multimodal inputs)
            query: [num_tokens, num_heads * head_size]
            key: [num_tokens, num_kv_heads * head_size]
        """
        assert positions.ndim == 2
        assert key is not None

        num_tokens = positions.shape[-1]
        cos_sin = self.cos_sin_cache[positions]
        cos, sin = cos_sin.chunk(2, dim=-1)
        cos = torch.cat(
            [m[i] for i, m in enumerate(cos.split(self.xdrope_section, dim=-1))], dim=-1
        )
        sin = torch.cat(
            [m[i] for i, m in enumerate(sin.split(self.xdrope_section, dim=-1))], dim=-1
        )

        query_shape = query.shape
        query = query.view(num_tokens, -1, self.head_size)
        query_rot = query[..., : self.rotary_dim]
        query_pass = query[..., self.rotary_dim :]
        query_rot = self.apply_rotary_emb(
            query_rot,
            cos,
            sin,
        )
        query = torch.cat((query_rot, query_pass), dim=-1).reshape(query_shape)

        key_shape = key.shape
        key = key.view(num_tokens, -1, self.head_size)
        key_rot = key[..., : self.rotary_dim]
        key_pass = key[..., self.rotary_dim :]
        key_rot = self.apply_rotary_emb(
            key_rot,
            cos,
            sin,
        )
        key = torch.cat((key_rot, key_pass), dim=-1).reshape(key_shape)
        return query, key

    @staticmethod
    defget_next_input_positions(
        context_len: int,
        seq_len: int,
        xd_sections: int = 4,
    ) -> list[list[int]]:
        return [list(range(context_len, seq_len)) for _ in range(xd_sections)]

    @staticmethod
    defget_next_input_positions_tensor(
        out: np.ndarray,
        out_offset: int,
        context_len: int,
        num_new_tokens: int,
    ):
        values = np.arange(
            context_len,
            context_len + num_new_tokens,
            dtype=out.dtype,
        )
        out[:, out_offset : out_offset + num_new_tokens] = values
```