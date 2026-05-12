---
title: cohere_asr - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/cohere_asr/
source: sitemap
fetched_at: 2026-05-07T21:29:21.887227831-03:00
rendered_js: false
word_count: 0
summary: This code implements the Conformer encoder module for automatic speech recognition, utilizing convolution-augmented transformer layers and relative positional encoding.
tags:
    - conformer
    - asr
    - pytorch
    - speech-recognition
    - encoder
    - transformer
    - deep-learning
category: concept
---

```
classConformerEncoder(nn.Module):
"""
    The encoder for ASR model of Conformer.
    Based on this paper:
    'Conformer: Convolution-augmented Transformer for
    Speech Recognition' by Anmol Gulati et al.
    https://arxiv.org/abs/2005.08100
    """

    def__init__(self, *, vllm_config: VllmConfig):
        super().__init__()

        self.hf_config = vllm_config.model_config.hf_config

        feat_in = self.hf_config.encoder["feat_in"]
        n_layers = self.hf_config.encoder["n_layers"]
        d_model = self.hf_config.encoder["d_model"]
        feat_out = self.hf_config.encoder["feat_out"]
        causal_downsampling = self.hf_config.encoder["causal_downsampling"]
        subsampling = self.hf_config.encoder["subsampling"]
        subsampling_factor = self.hf_config.encoder["subsampling_factor"]
        subsampling_conv_chunking_factor = self.hf_config.encoder.get(
            "subsampling_conv_chunking_factor", 1
        )
        subsampling_conv_channels = self.hf_config.encoder["subsampling_conv_channels"]
        ff_expansion_factor = self.hf_config.encoder["ff_expansion_factor"]
        self_attention_model = self.hf_config.encoder["self_attention_model"]
        n_heads = self.hf_config.encoder["n_heads"]
        att_context_size = self.hf_config.encoder["att_context_size"]
        att_context_probs = self.hf_config.encoder.get("att_context_probs", None)
        att_context_style = self.hf_config.encoder.get("att_context_style", "regular")
        xscaling = self.hf_config.encoder["xscaling"]
        untie_biases = self.hf_config.encoder["untie_biases"]
        pos_emb_max_len = self.hf_config.encoder["pos_emb_max_len"]
        conv_kernel_size = self.hf_config.encoder["conv_kernel_size"]
        conv_norm_type = self.hf_config.encoder["conv_norm_type"]
        conv_context_size = self.hf_config.encoder["conv_context_size"]
        use_bias = self.hf_config.encoder.get("use_bias", True)

        d_ff = d_model * ff_expansion_factor
        self.d_model = d_model
        self._feat_in = feat_in
        self.att_context_style = att_context_style
        self.subsampling_factor = subsampling_factor

        self.self_attention_model = self_attention_model

        # Setting up the att_context_size
        (
            _,
            self.att_context_size,
            _,
            self.conv_context_size,
        ) = self._calc_context_sizes(
            att_context_style=att_context_style,
            att_context_size=att_context_size,
            att_context_probs=att_context_probs,
            conv_context_size=conv_context_size,
            conv_kernel_size=conv_kernel_size,
        )

        if xscaling:
            self.xscale = math.sqrt(d_model)
        else:
            self.xscale = None

        # Subsampling
        if subsampling_conv_channels == -1:
            subsampling_conv_channels = d_model
        assert subsampling and subsampling_factor > 1 and subsampling == "dw_striding"

        self.pre_encode = ConvSubsampling(
            subsampling=subsampling,
            subsampling_factor=subsampling_factor,
            feat_in=feat_in,
            feat_out=d_model,
            conv_channels=subsampling_conv_channels,
            subsampling_conv_chunking_factor=subsampling_conv_chunking_factor,
            activation=nn.ReLU(True),
            is_causal=causal_downsampling,
        )

        self._feat_out = d_model

        # Biases for relative positional encoding
        if not untie_biases and self_attention_model == "rel_pos":
            d_head = d_model // n_heads
            # Register as buffers instead of parameters since they're not trainable
            # and need to respect dtype during weight loading
            self.register_buffer(
                "pos_bias_u", torch.zeros(n_heads, d_head), persistent=True
            )
            self.register_buffer(
                "pos_bias_v", torch.zeros(n_heads, d_head), persistent=True
            )
            pos_bias_u = self.pos_bias_u
            pos_bias_v = self.pos_bias_v
        else:
            pos_bias_u = None
            pos_bias_v = None

        # Positional encodings
        self.pos_emb_max_len = pos_emb_max_len
        assert self_attention_model == "rel_pos"
        self.pos_enc = RelPositionalEncoding(
            d_model=d_model,
            max_len=pos_emb_max_len,
            xscale=self.xscale,
        )

        self.layers = nn.ModuleList()
        for i in range(n_layers):
            layer = ConformerLayer(
                d_model=d_model,
                d_ff=d_ff,
                self_attention_model=self_attention_model,
                n_heads=n_heads,
                conv_kernel_size=conv_kernel_size,
                conv_norm_type=conv_norm_type,
                conv_context_size=self.conv_context_size,
                pos_bias_u=pos_bias_u,
                pos_bias_v=pos_bias_v,
                att_context_size=self.att_context_size,
                use_bias=use_bias,
            )
            self.layers.append(layer)

        if feat_out > 0 and feat_out != self._feat_out:
            self.out_proj = nn.Linear(self._feat_out, feat_out)
            self._feat_out = feat_out
        else:
            self.out_proj = None
            self._feat_out = d_model
        self.set_max_audio_length(self.pos_emb_max_len)

    defget_num_encoder_cross_attn_tokens(self, num_encoder_input_tokens: int) -> int:
        num_encoder_cross_attn_tokens = math.ceil(
            num_encoder_input_tokens / self.subsampling_factor
        )
        return num_encoder_cross_attn_tokens

    defset_max_audio_length(self, max_audio_length: int) -> None:
"""
        Sets maximum input length.
        Pre-calculates internal seq_range mask.

        Args:
            max_audio_length (int): New maximum sequence length.
        """
        device = next(self.parameters()).device
        dtype = next(self.parameters()).dtype
        self.pos_enc.extend_pe(max_audio_length, device, dtype)

    defforward(
        self,
        audio_signal: torch.Tensor,
        length: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        if audio_signal.shape[-2] != self._feat_in:
            raise ValueError(
                f"audio_signal should have shape "
                f"(batch, {self._feat_in}, n_frame) but "
                f"got last dimension "
                f"{audio_signal.shape[-2]}."
            )

        return self.forward_internal(
            audio_signal,
            length,
        )

    defforward_internal(
        self,
        audio_signal: torch.Tensor,
        length: torch.Tensor | None = None,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        if length is None:
            length = audio_signal.new_full(
                (audio_signal.size(0),),
                audio_signal.size(-1),
                dtype=torch.int64,
                device=audio_signal.device,
            )

        cur_att_context_size = self.att_context_size
        audio_signal = torch.transpose(audio_signal, 1, 2)

        audio_signal, length = self.pre_encode(x=audio_signal, lengths=length)
        length = length.to(torch.int64)

        max_audio_length = audio_signal.size(1)

        padding_length = length

        audio_signal, pos_emb = self.pos_enc(x=audio_signal, cache_len=0)

        pad_mask, att_mask = self._create_masks(
            att_context_size=cur_att_context_size,
            padding_length=padding_length,
            max_audio_length=max_audio_length,
            offset=None,
            device=audio_signal.device,
        )

        for lth, layer in enumerate(self.layers):
            audio_signal = layer(
                x=audio_signal,
                att_mask=att_mask,
                pos_emb=pos_emb,
                pad_mask=pad_mask,
            )

        if self.out_proj is not None:
            audio_signal = self.out_proj(audio_signal)

        audio_signal = torch.transpose(audio_signal, 1, 2)
        length = length.to(dtype=torch.int64)

        return audio_signal, length

    def_create_masks(
        self,
        att_context_size: list[int],
        padding_length: torch.Tensor,
        max_audio_length: int,
        offset: torch.Tensor | None,
        device: torch.device,
    ) -> tuple[torch.Tensor, torch.Tensor | None]:
        if self.self_attention_model != "rel_pos_local_attn":
            att_mask = torch.ones(
                1, max_audio_length, max_audio_length, dtype=torch.bool, device=device
            )

            if self.att_context_style == "regular":
                if att_context_size[0] >= 0:
                    att_mask = att_mask.triu(diagonal=-att_context_size[0])
                if att_context_size[1] >= 0:
                    att_mask = att_mask.tril(diagonal=att_context_size[1])
            elif self.att_context_style == "chunked_limited":
                # When right context is unlimited, just the
                # left side of masking needs to get updated
                if att_context_size[1] == -1:
                    if att_context_size[0] >= 0:
                        att_mask = att_mask.triu(diagonal=-att_context_size[0])
                else:
                    chunk_size = att_context_size[1] + 1
                    # left_chunks_num specifies the number
                    # of chunks to be visible by each chunk
                    # on the left side
                    if att_context_size[0] >= 0:
                        left_chunks_num = att_context_size[0] // chunk_size
                    else:
                        left_chunks_num = 10000

                    chunk_idx = torch.arange(
                        0, max_audio_length, dtype=torch.int, device=att_mask.device
                    )
                    chunk_idx = torch.div(chunk_idx, chunk_size, rounding_mode="trunc")
                    diff_chunks = chunk_idx.unsqueeze(1) - chunk_idx.unsqueeze(0)
                    chunked_limited_mask = torch.logical_and(
                        torch.le(diff_chunks, left_chunks_num), torch.ge(diff_chunks, 0)
                    )
                    att_mask = torch.logical_and(
                        att_mask, chunked_limited_mask.unsqueeze(0)
                    )
        else:
            att_mask = None

        # pad_mask is the masking to be used to ignore paddings
        pad_mask = torch.arange(0, max_audio_length, device=device).expand(
            padding_length.size(0), -1
        ) < padding_length.unsqueeze(-1)

        if offset is not None:
            pad_mask_off = torch.arange(0, max_audio_length, device=device).expand(
                padding_length.size(0), -1
            ) >= offset.unsqueeze(-1)
            pad_mask = pad_mask_off.logical_and(pad_mask)

        if att_mask is not None:
            # pad_mask_for_att_mask is the mask which helps to ignore paddings
            pad_mask_for_att_mask = pad_mask.unsqueeze(1).repeat(
                [1, max_audio_length, 1]
            )
            pad_mask_for_att_mask = torch.logical_and(
                pad_mask_for_att_mask, pad_mask_for_att_mask.transpose(1, 2)
            )
            # att_mask is the masking to be used by MHA
            # layers to ignore tokens not supposed to be
            # visible
            att_mask = att_mask[:, :max_audio_length, :max_audio_length]
            # paddings should also get ignored, so
            # pad_mask_for_att_mask is used to ignore their
            # corresponding scores
            att_mask = torch.logical_and(
                pad_mask_for_att_mask, att_mask.to(pad_mask_for_att_mask.device)
            )
            att_mask = ~att_mask

        pad_mask = ~pad_mask
        return pad_mask, att_mask

    def_calc_context_sizes(
        self,
        att_context_size: list[int] | list[list[int]] | None,
        att_context_probs: list[float] | None,
        att_context_style: str,
        conv_context_size: list[int] | str | None,
        conv_kernel_size: int,
    ) -> tuple[list[list[int]], list[int], list[float], list[int]]:
        # convert att_context_size to a standard list of lists
        if att_context_size:
            att_context_size_all = list(att_context_size)
            if isinstance(att_context_size_all[0], int):
                att_context_size_all = [att_context_size_all]
            for i, att_cs in enumerate(att_context_size_all):
                if att_context_style == "chunked_limited":
                    if att_cs[0] > 0 and att_cs[0] % (att_cs[1] + 1) > 0:
                        raise ValueError(
                            f"att_context_size[{i}][0] % "
                            f"(att_context_size[{i}][1]"
                            f" + 1) should be zero!"
                        )
                    if att_cs[1] < 0 and len(att_context_size_all) <= 1:
                        raise ValueError(
                            f"Right context "
                            f"(att_context_size[{i}][1])"
                            f" can not be unlimited for"
                            f" chunked_limited style!"
                        )
        else:
            att_context_size_all = [[-1, -1]]

        if att_context_probs:
            if len(att_context_probs) != len(att_context_size_all):
                raise ValueError(
                    "The size of the att_context_probs "
                    "should be the same as att_context_size."
                )
            att_context_probs = list(att_context_probs)
            if sum(att_context_probs) != 1:
                raise ValueError(
                    "The sum of numbers in "
                    "att_context_probs should be equal "
                    "to one to be a distribution."
                )
        else:
            att_context_probs = [1.0 / len(att_context_size_all)] * len(
                att_context_size_all
            )

        if conv_context_size is not None:
            if not isinstance(conv_context_size, list) and not isinstance(
                conv_context_size, str
            ):
                raise ValueError(
                    "Invalid conv_context_size! It should "
                    "be the string 'causal' or a list of "
                    "two integers."
                )
            if conv_context_size == "causal":
                conv_context_size = [conv_kernel_size - 1, 0]
            else:
                total = conv_context_size[0] + conv_context_size[1] + 1
                if total != conv_kernel_size:
                    raise ValueError(
                        f"Invalid conv_context_size: {self.conv_context_size}!"
                    )
        else:
            conv_context_size = [
                (conv_kernel_size - 1) // 2,
                (conv_kernel_size - 1) // 2,
            ]
        return (
            att_context_size_all,
            att_context_size_all[0],
            att_context_probs,
            conv_context_size,
        )
```