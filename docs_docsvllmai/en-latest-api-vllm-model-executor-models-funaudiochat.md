---
title: funaudiochat - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/funaudiochat/
source: sitemap
fetched_at: 2026-05-07T21:30:06.935236284-03:00
rendered_js: false
word_count: 6
summary: This document defines a continuous audio encoder module using PyTorch, designed to process audio features through convolutional layers and transformer-based encoder blocks, including support for FlashAttention for long-form audio sequences.
tags:
    - pytorch
    - audio-processing
    - flash-attention
    - neural-network
    - feature-extraction
    - deep-learning
category: reference
---

```
classFunAudioChatAudioEncoder(nn.Module):
"""Continuous audio tower."""

    def__init__(self, config: Any):
        super().__init__()
        self.config = config

        embed_dim = int(config.d_model)
        self.num_mel_bins = int(config.num_mel_bins)
        self.max_source_positions = int(config.max_source_positions)
        self.embed_scale = (embed_dim**0.5) if bool(config.scale_embedding) else 1.0
        self.n_window = int(config.n_window)

        self.conv1 = nn.Conv1d(self.num_mel_bins, embed_dim, kernel_size=3, padding=1)
        self.conv2 = nn.Conv1d(embed_dim, embed_dim, kernel_size=3, stride=2, padding=1)
        self.layers = nn.ModuleList(
            [
                FunAudioChatAudioEncoderLayer(config)
                for _ in range(int(config.encoder_layers))
            ]
        )
        self.ln_post = nn.LayerNorm(embed_dim)
        self.avg_pooler = nn.AvgPool1d(2, stride=2)
        self.proj = nn.Linear(embed_dim, int(config.output_dim))
        self.positional_embedding = _SinusoidsPositionEmbedding(
            self.max_source_positions, embed_dim
        )

        # Present in HF weights even if unused during S2T.
        self.audio_bos_eos_token = nn.Embedding(2, int(config.output_dim))

    @property
    defdtype(self) -> torch.dtype:
        return self.conv1.weight.dtype

    def_prepare_attention_mask(
        self, inputs_tensor: torch.Tensor, cu_seqlens: torch.Tensor
    ) -> torch.Tensor | None:
        if getattr(self.config, "_attn_implementation", "eager") == "flash_attention_2":
            return None

        seq_length = inputs_tensor.shape[0]
        attention_mask = torch.full(
            (1, 1, seq_length, seq_length),
            torch.finfo(inputs_tensor.dtype).min,
            device=inputs_tensor.device,
            dtype=inputs_tensor.dtype,
        )
        for i in range(1, len(cu_seqlens)):
            start = int(cu_seqlens[i - 1].item())
            end = int(cu_seqlens[i].item())
            attention_mask[..., start:end, start:end] = 0
        return attention_mask

    defforward(
        self,
        input_features: torch.Tensor,
        feature_lens: torch.Tensor,
        aftercnn_lens: torch.Tensor,
        speech_maxlen: int,
        **kwargs: object,
    ) -> BaseModelOutput:
        # For max-length audio (300s => ~7500 speech frames at 25Hz), the
        # Torch SDPA path can be prohibitively memory hungry (~O(n^2) inside the
        # longest chunks). Require FlashAttention for such inputs to avoid OOM
        # and performance cliffs.
        if int(speech_maxlen) >= 7500:
            if not _has_module("flash_attn"):
                raise RuntimeError(
                    "FunAudioChat long audio (~300s) requires FlashAttention-2 "
                    "for the continuous audio tower, but `flash_attn` is not "
                    "installed in the runtime environment."
                )
            if not getattr(
                self.layers[0].self_attn.attn, "is_flash_attn_backend", False
            ):
                raise RuntimeError(
                    "FunAudioChat long audio (~300s) requires FlashAttention for the "
                    "continuous audio tower, but the selected MM encoder attention "
                    "backend is not FlashAttention."
                )

        # Handle empty / invalid items (feature_lens == 0) without crashing.
        original_batch_size = int(feature_lens.size(0))
        device = input_features.device

        valid_mask = feature_lens > 0
        valid_indices = torch.where(valid_mask)[0]

        if valid_indices.numel() == 0:
            output_dim = int(self.proj.out_features)
            return BaseModelOutput(
                last_hidden_state=torch.zeros(
                    (original_batch_size, speech_maxlen, output_dim),
                    device=device,
                    dtype=self.proj.weight.dtype,
                )
            )

        input_features_list = input_features.split(feature_lens.tolist(), dim=1)
        valid_input_features_list = [input_features_list[int(i)] for i in valid_indices]
        valid_input_features = torch.cat(valid_input_features_list, dim=1)

        valid_feature_lens = feature_lens[valid_mask]
        valid_aftercnn_lens = aftercnn_lens[valid_mask]

        chunk_num = torch.ceil(valid_feature_lens / (self.n_window * 2)).long()

        chunk_lengths_list: list[int] = []
        full_chunk_len = self.n_window * 2
        for i, length in enumerate(valid_feature_lens):
            num_chunks_for_sample = int(chunk_num[i].item())
            if num_chunks_for_sample == 0:
                continue
            chunk_lengths_list.extend([full_chunk_len] * (num_chunks_for_sample - 1))
            last_chunk_len = int(length.item()) % full_chunk_len
            if last_chunk_len == 0:
                last_chunk_len = full_chunk_len
            chunk_lengths_list.append(last_chunk_len)

        chunk_lengths = torch.tensor(
            chunk_lengths_list, dtype=torch.long, device=device
        )

        chunk_list = valid_input_features.split(chunk_lengths.tolist(), dim=1)
        padded_feature, padded_mask, padded_mask_after_cnn = (
            self.padded_and_mask_function(
                chunk_list, chunk_lengths, padding_value=0, padding_side="right"
            )
        )

        padded_embed = nn.functional.gelu(self.conv1(padded_feature)) * padded_mask
        padded_embed = nn.functional.gelu(self.conv2(padded_embed)).transpose(1, 2)

        padded_embed = padded_embed + self.positional_embedding.positional_embedding[
            : padded_embed.shape[1], :
        ].unsqueeze(0).to(padded_embed.dtype)

        hidden_states = padded_embed[padded_mask_after_cnn]
        cu_seqlens = torch.cat(
            (
                torch.zeros(1, device=padded_mask_after_cnn.device, dtype=torch.int32),
                padded_mask_after_cnn.sum(1).cumsum(0),
            )
        ).to(torch.int32)

        for encoder_layer in self.layers:
            (hidden_states,) = encoder_layer(
                hidden_states,
                cu_seqlens=cu_seqlens,
                **kwargs,
            )

        hidden_states_list = hidden_states.split(valid_aftercnn_lens.tolist(), dim=0)

        pooled_list: list[torch.Tensor] = []
        pooled_lengths: list[int] = []
        for each_audio_states in hidden_states_list:
            seq_len = int(each_audio_states.shape[0])
            if seq_len >= 2:
                pooled = nn.functional.avg_pool1d(
                    each_audio_states.transpose(0, 1), kernel_size=2, stride=2
                ).transpose(0, 1)
            else:
                pooled = each_audio_states
            pooled_list.append(pooled)
            pooled_lengths.append(int(pooled.shape[0]))

        pooled_concat = torch.cat(pooled_list, dim=0)
        processed_concat = self.proj(self.ln_post(pooled_concat))
        processed_audio_list = list(processed_concat.split(pooled_lengths, dim=0))

        output_dim = (
            int(processed_audio_list[0].shape[-1])
            if processed_audio_list
            else int(self.proj.out_features)
        )
        output_hidden_states = torch.zeros(
            (original_batch_size, speech_maxlen, output_dim),
            dtype=processed_audio_list[0].dtype
            if processed_audio_list
            else self.proj.weight.dtype,
            device=device,
        )

        for valid_idx, processed in zip(valid_indices, processed_audio_list):
            seq_len = min(int(processed.shape[0]), int(speech_maxlen))
            output_hidden_states[int(valid_idx), :seq_len] = processed[:seq_len]

        return BaseModelOutput(last_hidden_state=output_hidden_states)

    defpadded_and_mask_function(
        self,
        tensor_list: Sequence[torch.Tensor],
        tensor_len: torch.Tensor,
        padding_value: float = 0.0,
        padding_side: str = "right",
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        max_len = int(tensor_len.max().item())
        dim = int(tensor_list[0].shape[0])
        padded_tensor = torch.full(
            size=(len(tensor_list), dim, max_len),
            fill_value=padding_value,
            dtype=self.dtype,
            device=tensor_list[0].device,
        )

        batch_mask = torch.zeros(
            (len(tensor_len), max_len), dtype=torch.long, device=padded_tensor.device
        )
        for i, length in enumerate(tensor_len):
            length_val = int(length.item())
            batch_mask[i, :length_val] = 1
            padded_tensor[i, :, :length_val] = tensor_list[i]

        feature_lens_after_cnn = (tensor_len - 1) // 2 + 1
        max_len_after_cnn = int(feature_lens_after_cnn.max().item())
        batch_mask_after_cnn = torch.zeros(
            (len(tensor_len), max_len_after_cnn),
            dtype=torch.long,
            device=padded_tensor.device,
        )
        for i, length in enumerate(feature_lens_after_cnn):
            batch_mask_after_cnn[i, : int(length.item())] = 1

        if padding_side != "right":
            raise NotImplementedError("Only right padding is supported.")

        return (
            padded_tensor,
            batch_mask.unsqueeze(1).to(padded_tensor.dtype),
            batch_mask_after_cnn.bool(),
        )

    # From the HF FunAudioChat implementation.
    def_get_feat_extract_output_lengths(
        self, input_lengths: torch.LongTensor
    ) -> tuple[torch.LongTensor, torch.LongTensor]:
        input_lengths = (input_lengths - 1) // 2 + 1
        output_lengths = (input_lengths - 2) // 2 + 1
        return input_lengths, output_lengths
```