---
title: minicpmv - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/minicpmv/
source: sitemap
fetched_at: 2026-05-07T21:31:48.987096421-03:00
rendered_js: false
word_count: 0
summary: This document defines the Resampler4_5 class, which implements a neural network module for attention-based feature resampling with support for spatial and temporal positional embeddings.
tags:
    - pytorch
    - neural-networks
    - positional-encoding
    - attention-mechanism
    - feature-resampling
    - computer-vision
category: reference
---

```
classResampler4_5(Resampler2_5):
    def__init__(
        self,
        num_queries: int,
        embed_dim: int,
        num_heads: int,
        kv_dim: int | None = None,
        norm_layer: Callable[[int], nn.LayerNorm] = DEFAULT_LN,
        max_size: tuple[int, int] = (70, 70),
        max_temporal_size: int = 36000,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ) -> None:
        super().__init__(
            num_queries,
            embed_dim,
            num_heads,
            kv_dim,
            norm_layer,
            max_size,
            quant_config=quant_config,
            prefix=prefix,
        )

        trunc_normal_(self.query, std=0.02)
        self.max_temporal_size = max_temporal_size
        self._set_temporal_pos_cache(self.max_temporal_size)
        self.apply(self._init_weights)

    defget_1d_sincos_pos_embed_from_temporal_size(
        self, embed_dim: int, pos: np.ndarray
    ):
"""
        embed_dim: output dimension for each position
        pos: a list of positions to be encoded: size (M,)
        out: (M, D)
        """
        assert embed_dim % 2 == 0
        omega = np.arange(embed_dim // 2, dtype=np.float32)
        omega /= embed_dim / 2.0
        omega = 1.0 / 10000**omega  # (D/2,)

        pos = pos.reshape(-1)  # (M,)
        out = np.einsum("m,d->md", pos, omega)  # (M, D/2), outer product

        emb_sin = np.sin(out)  # (M, D/2)
        emb_cos = np.cos(out)  # (M, D/2)

        emb = np.concatenate([emb_sin, emb_cos], axis=1)  # (M, D)
        return emb

    def_set_temporal_pos_cache(
        self, max_temporal_size: int, device: torch.types.Device = "cpu"
    ) -> None:
        temporal_size = np.arange(max_temporal_size, dtype=np.float32)
        pos_embed = (
            torch.from_numpy(
                self.get_1d_sincos_pos_embed_from_temporal_size(
                    self.embed_dim, temporal_size
                )
            )
            .float()
            .to(device)
        )
        self.register_buffer("temporal_pos_embed", pos_embed, persistent=False)

    def_adjust_temporal_pos_cache(
        self, max_temporal_size: int, device: torch.types.Device = "cpu"
    ):
        if max_temporal_size > self.max_temporal_size:
            self.max_temporal_size = max_temporal_size
            self._set_temporal_pos_cache(self.max_temporal_size, device)

    def_init_weights(self, m: nn.Linear | nn.LayerNorm):
        if isinstance(m, nn.Linear):
            trunc_normal_(m.weight, std=0.02)
            if isinstance(m, nn.Linear) and m.bias is not None:
                nn.init.constant_(m.bias, 0)
        elif isinstance(m, nn.LayerNorm):
            nn.init.constant_(m.bias, 0)
            nn.init.constant_(m.weight, 1.0)

    defforward(
        self,
        x: torch.Tensor,
        tgt_sizes: torch.Tensor,
        # temporal_ids for high refresh rate videos
        temporal_ids=None,
    ) -> torch.Tensor:
        assert x.shape[0] == tgt_sizes.shape[0]
        bs = x.shape[0]

        device = x.device
        dtype = x.dtype

        patch_len = tgt_sizes[:, 0] * tgt_sizes[:, 1]

        self._adjust_pos_cache(tgt_sizes, device=device)

        temporal_pos_emb = False
        temporal_ids_flatten = None
        if temporal_ids is not None:
            # example: [[-1], [-1], [2, 6, 9]]
            temporal_ids_flatten = list(chain.from_iterable(temporal_ids))
            max_temporal_size = max(temporal_ids_flatten, default=0)
            if max_temporal_size > -1:
                temporal_pos_emb = True
            if max_temporal_size > self.max_temporal_size:
                self._adjust_temporal_pos_cache(max_temporal_size, device)

        max_patch_len = patch_len.max().item()
        assert isinstance(max_patch_len, int)

        key_padding_mask = torch.zeros(
            (bs, max_patch_len), dtype=torch.bool, device=device
        )

        x, _ = self.kv_proj(x)  # B * L * D
        x = self.ln_kv(x).permute(1, 0, 2)  # L * B * D
        q = self.ln_q(self.query)  # Q * D

        pos_embed_2d = []
        pos_embed_temporal = []
        for i in range(bs):
            tgt_h, tgt_w = tgt_sizes[i]
            if temporal_pos_emb:
                if temporal_ids_flatten[i] == -1:
                    pos_embed_temporal.append(
                        torch.zeros(self.embed_dim, dtype=dtype, device=device)
                    )
                else:
                    pos_embed_temporal.append(
                        self.temporal_pos_embed[temporal_ids_flatten[i]].to(dtype)
                    )  # D

            pos_embed_2d.append(
                self.pos_embed[:tgt_h, :tgt_w, :].reshape((tgt_h * tgt_w, -1)).to(dtype)
            )  # patches * D
            key_padding_mask[i, patch_len[i] :] = True

        pos_embed_2d = torch.nn.utils.rnn.pad_sequence(
            pos_embed_2d, batch_first=True, padding_value=0.0
        ).permute(1, 0, 2)  # BLD => L * B * D

        k = x + pos_embed_2d
        v = x
        if pos_embed_temporal:
            k += torch.stack(pos_embed_temporal, dim=0)
            bs = len(temporal_ids)
            merge_k = []
            merge_v = []
            merge_key_padding_mask = []

            start = 0
            for tp in temporal_ids:
                end = start + len(tp)
                # L * (end-start) * D -> (end-start) * L * D
                # -> 1 * L*(end-start) * D
                merge_k.append(
                    k[:, start:end, :].permute(1, 0, 2).reshape(-1, self.embed_dim)
                )
                merge_v.append(
                    v[:, start:end, :].permute(1, 0, 2).reshape(-1, self.embed_dim)
                )
                merge_key_padding_mask.append(
                    key_padding_mask[start:end, :].reshape(-1, 1)
                )

                start = end

            k = torch.nn.utils.rnn.pad_sequence(
                merge_k, batch_first=True, padding_value=0.0
            ).permute(1, 0, 2)  # L*(end-start)
            v = torch.nn.utils.rnn.pad_sequence(
                merge_v, batch_first=True, padding_value=0.0
            ).permute(1, 0, 2)  # L*(end-start)
            key_padding_mask = torch.nn.utils.rnn.pad_sequence(
                merge_key_padding_mask, batch_first=True, padding_value=True
            ).squeeze(-1)

        out = self.attn(
            self._repeat(q, bs),  # Q * B * D
            k,  # L * B * D +  L * B * D
            v,
            key_padding_mask=key_padding_mask,
        )[0]
        #  out: Q * B * D
        x = out.permute(1, 0, 2)  # B * Q * D

        x = self.ln_post(x)
        x = x @ self.proj
        return x
```