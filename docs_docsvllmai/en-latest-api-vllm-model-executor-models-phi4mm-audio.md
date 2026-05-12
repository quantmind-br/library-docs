---
title: phi4mm_audio - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/phi4mm_audio/
source: sitemap
fetched_at: 2026-05-07T21:32:39.088432295-03:00
rendered_js: false
word_count: 0
summary: This document defines the configuration parameters and initialization structure for a Conformer encoder module, commonly used in speech processing tasks.
tags:
    - conformer
    - transformer-encoder
    - deep-learning
    - speech-processing
    - neural-network-architecture
    - streaming-models
category: reference
---

```
classConformerEncoder(TransformerEncoderBase):
"""ConformerEncoder module.
    see original paper for more details:
        https://arxiv.org/abs/2005.08100

    Please set causal = True in streaming model
    Args:
        input_size: int
            input feature dimension.
        chunk_size: int, list(int)
            Number of frames for each chunk
            This variable can take 2 forms:
            int:  Used for inference, or single chunk size training
            list(int) : Used only for variable chunk size training
            Some examples for the 2 cases:
            chunk_size = 12
            chunk_size = [6, 8, 12, 24]
        left_chunk: int, list(int)
            Number of chunks used for masking in streaming mode.
            This variable can take 2 forms:
            int:  Used for inference, or single chunk size training
            list(int) : Used only for variable chunk size training. When
            chunk_size is a list, left_chunk must be a list with same length.
            Some examples for the 2 cases:
            left_chunk = 6
            left_chunk = [12, 9, 6, 3]
        num_lang: int
            This parameter is used to store the number of languages in the
            lang_dict, only used for multiseed/multilingual models.
            default None.
        attention_dim: int, optional
            attention dimension. default 256.
        attention_heads: int, optional
            the number of heads. default 4
        linear_units:
            the number of units of position-wise feed forward.
            default 2048
        num_block:
            number of Transformer layer. default 6
        dropout_rate: float, optional
            dropout rate. default 0.1
        input_layer: str, optional
            input layer type before Conformer,
            one of ["linear", "conv2d", "custom", "vgg2l", "embed"],
            default "conv2d"
        causal: bool, optional
            if set to True, convolution have no access
             to future frames. default False.
        batch_norm: bool, optional
            if set to True, apply batchnorm before activation
            in ConvModule layer of the conformer.
            default False
        cnn_out: int, optional
            the number of CNN channels before Conformer.
            default -1.
        cnn_layer_norm: bool, optional
            layer norm between Conformer and the first CNN.
            default False.
        ext_pw_out_channel: int, optional
            the number of channel for CNN
            before depthwise_separable_CNN.
            If 0 then use linear. default 0.
        ext_pw_kernel_size: int, optional
            kernel size of N before depthwise_separable_CNN.
            only work for ext_pw_out_channel > 0.
            default 1
        depthwise_seperable_out_channel: int, optional
            the number of channel for
            depthwise_separable_CNN.
            default 256.
        depthwise_multiplier: int, optional
            the number of multiplier for
            depthwise_separable_CNN.
            default 1.
        chunk_se: int, optional
            0 for offline SE.
            1 for streaming SE, where mean is computed
             by accumulated history until current chunk_se.
            2 for streaming SE, where mean is computed
             by only the current chunk.
            default 0.
        kernel_size: int, optional
            the number of kernels for depthwise_separable_CNN.
            default 3.
        activation: str, optional
            FeedForward block activation.
            one of ["relu", "swish", "sigmoid"]
            default "relu".
        conv_activation: str, optional
            activation function used in ConvModule part
            of the conformer, default "relu".
        conv_glu_type: str, optional
            activation used use glu in depthwise_separable_CNN,
            default "sigmoid"
        bias_in_glu: bool, optional
            if set to True, use additive bias in the weight module
             before GLU. default True
        linear_glu_in_convm: bool, optional
            if set to True, use GLULinear module,
             otherwise, used GLUPointWiseConv module.
              default to False.
        attention_glu_type: str
            only work for glu_in_attention !=0
            default "swish".
        export: bool, optional
            if set to True, it removes the padding from convolutional layers
             and allow the onnx conversion for inference.
              default False.
        activation_checkpointing: str, optional
            a dictionarry of {"module","interval","offload"}, where
                "module": str
                    accept ["transformer", "attention"] to select
                    which module should do activation checkpointing.
                "interval": int, default 1,
                    interval of applying activation checkpointing,
                    interval = 1 means that we apply checkpointing
                    on every layer (if activation), otherwise,
                    we apply it every x interval.
                "offload": bool, default False,
                    if set to True, we offload activation to cpu and
                    reload it during backward, otherwise,
                    we recalculate activation in backward.
            default "".
        extra_layer_output_idx: int
            the layer index to be exposed.
        relative_attention_bias_args: dict, optional
            use more efficient scalar bias-based relative multihead attention
            (Q*K^T + B) implemented in cmb.basics.embedding.
            [T5/ALiBi]RelativeAttentionLogitBias
            usage: relative_attention_bias_args={"type": t5/alibi}
            additional method-specific arguments can be provided (see
            transformer_base.py)
        time_reduction: int optional
            time reduction factor
            default 4
        use_pt_scaled_dot_product_attention: whether to use pytorch scaled
            dot product attention in training.
            Default: False
        nemo_conv_settings: dict, optional
            A dictionary of settings for NeMo Subsampling.
            default: None
            usage: nemo_conv_settings=
                {
                    "subsampling":
                    dw_striding/striding/dw_striding_conv1d/striding_conv1d,
                    "conv_channels": int,
                    "subsampling_conv_chunking_factor": int,
                    "is_causal": True/False
                }
        conv2d_extra_padding: str, optional
            Add extra padding in conv2d subsampling layers. Choices are
            (feat, feat_time, none, True)
            Default: none
        replication_pad_for_subsample_embedding:  For batched-streaming
            decoding, use "replication" padding for the cache at start of
            utterance.
            Default: False
        attention_group_size: int, optional
            the number of groups to use for attention, default 1
            (Multi-Head Attention),
            1 = typical Multi-Head Attention,
            1 < attention_group_size < attention_heads = Grouped-Query
            Attention
            attention_group_size = attention_heads = Multi-Query Attention
    """

    extra_multi_layer_output_idxs: list[int]

    def__init__(  # pylint: disable-all
        self,
        input_size: int,
        chunk_size: int | list[int],
        left_chunk: int | list[int],
        num_lang: int | None = None,
        attention_dim: int = 256,
        attention_heads: int = 4,
        linear_units: int = 2048,
        num_blocks: int = 6,
        dropout_rate: float = 0.1,
        input_layer: str = "nemo_conv",
        causal: bool = True,
        batch_norm: bool = False,
        cnn_out: int = -1,
        cnn_layer_norm: bool = False,
        ext_pw_out_channel: int = 0,
        ext_pw_kernel_size: int = 1,
        depthwise_seperable_out_channel: int = 256,
        depthwise_multiplier: int = 1,
        chunk_se: int = 0,
        kernel_size: int = 3,
        activation: str = "relu",
        conv_activation: str = "relu",
        conv_glu_type: str = "sigmoid",
        bias_in_glu: bool = True,
        linear_glu_in_convm: bool = False,
        attention_glu_type: str = "swish",
        export: bool = False,
        extra_layer_output_idx: int = -1,
        extra_multi_layer_output_idxs: list[int] = [],  # noqa
        activation_checkpointing: str = "",
        relative_attention_bias_args: dict[str, Any] | None = None,
        time_reduction: int = 4,
        use_pt_scaled_dot_product_attention: bool = False,
        nemo_conv_settings: dict[str, Any] | None = None,
        conv2d_extra_padding: Literal["feat", "feat_time", "none", True] = "none",
        replication_pad_for_subsample_embedding: bool = False,
        attention_group_size: int = 1,
        encoder_embedding_config: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(
            input_size,
            chunk_size,
            left_chunk,
            attention_dim,
            attention_heads,
            input_layer,
            cnn_out,
            cnn_layer_norm,
            time_reduction,
            dropout_rate=dropout_rate,
            relative_attention_bias_args=relative_attention_bias_args,
            positional_dropout_rate=0.0,
            nemo_conv_settings=nemo_conv_settings,
            conv2d_extra_padding=conv2d_extra_padding,
            attention_group_size=attention_group_size,
            encoder_embedding_config=encoder_embedding_config,
        )
        self.num_blocks = num_blocks
        self.num_lang = num_lang
        self.kernel_size = kernel_size
        self.replication_pad_for_subsample_embedding: bool = (
            replication_pad_for_subsample_embedding
        )
        assert self.num_heads % attention_group_size == 0, (
            "attention_group_size must divide n_head"
        )
        self.num_heads_k = self.num_heads // attention_group_size

        self.encoders = MultiSequential(
            *[
                ConformerEncoderLayer(
                    d_model=attention_dim,
                    ext_pw_out_channel=ext_pw_out_channel,
                    depthwise_seperable_out_channel=depthwise_seperable_out_channel,
                    depthwise_multiplier=depthwise_multiplier,
                    n_head=attention_heads,
                    d_ffn=linear_units,
                    ext_pw_kernel_size=ext_pw_kernel_size,
                    kernel_size=kernel_size,
                    dropout_rate=dropout_rate,
                    causal=causal,
                    batch_norm=batch_norm,
                    activation=activation,
                    chunk_se=chunk_se,
                    chunk_size=chunk_size,
                    conv_activation=conv_activation,
                    conv_glu_type=conv_glu_type,
                    bias_in_glu=bias_in_glu,
                    linear_glu_in_convm=linear_glu_in_convm,
                    attention_glu_type=attention_glu_type,
                    activation_checkpointing=activation_checkpointing,
                    export=export,
                    use_pt_scaled_dot_product_attention=use_pt_scaled_dot_product_attention,
                    attn_group_sizes=attention_group_size,
                )
                for _ in range(num_blocks)
            ]
        )
        self.extra_layer_output_idx = extra_layer_output_idx
        self.extra_multi_layer_output_idxs = extra_multi_layer_output_idxs
        # Make a zeros scalar we can use in get_initial_state to determine
        # the device and the needed dtype:
        self.register_buffer("dev_type", torch.zeros(()), persistent=False)

    definit_relative_attention_bias(
        self, input_tensor: torch.Tensor
    ) -> torch.Tensor | None:
        if self.relative_attention_bias_layer:
            return self.relative_attention_bias_layer(input_tensor)

    defcalculate_hs_mask(
        self, xs_pad: torch.Tensor, device: torch.device, mask: torch.Tensor | None
    ) -> torch.Tensor:
        max_audio_length = xs_pad.shape[1]
        batch_size = xs_pad.shape[0]
        enc_streaming_mask = self._streaming_mask(
            max_audio_length, batch_size, self.chunk_size, self.left_chunk
        )
        enc_streaming_mask = enc_streaming_mask.to(device)
        if mask is None:
            return enc_streaming_mask

        feature_lens = mask.sum(1)
        padding_length = feature_lens
        pad_mask = torch.arange(0, max_audio_length, device=device).expand(
            padding_length.size(0), -1
        ) < padding_length.unsqueeze(1)
        pad_mask = pad_mask.unsqueeze(1)
        pad_mask = pad_mask & enc_streaming_mask
        return pad_mask

    @torch.jit.ignore
    defforward(
        self, xs_pad: torch.Tensor, masks: torch.Tensor
    ) -> tuple[torch.Tensor, torch.Tensor]:
"""Conformer Forward function

        Args:
            xs_pad: torch.Tensor
                input tensor
            masks: torch.Tensor
                post-embedding input lengths
        """
        xs_pad = self.encoder_embedding(xs_pad)
        input_tensor, pos_k, pos_v, hs_mask, masks = self.forward_embeddings(
            xs_pad, masks
        )

        unfolded = False
        ori_bz, seq_len, D = input_tensor.shape
        max_seq_len = 500  # maximum position for absolute positional encoding
        if seq_len > max_seq_len:
            # audio sequence is longer than max_seq_len, unfold it into chunks
            # of max_seq_len
            unfolded = True
            # the unfold op will drop residual frames, pad it to the multiple
            # of max_seq_len
            if seq_len % max_seq_len > 0:
                chunk_pad_size = max_seq_len - (seq_len % max_seq_len)
            else:
                chunk_pad_size = 0
            if chunk_pad_size > 0:
                input_tensor_pad = F.pad(
                    input_tensor, (0, 0, 0, chunk_pad_size), "constant", 0
                )
                input_tensor = input_tensor_pad.to(input_tensor.device)
            input_tensor = unfold_tensor(input_tensor, max_seq_len)
            if masks is not None:
                # revise hs_mask here because the previous calculated hs_mask
                # did not consider extra pad
                subsampled_pad_mask = masks.squeeze(
                    1
                )  # [bz, subsampled_unmask_seq_len]
                extra_padded_subsamlped_pad_mask = F.pad(
                    subsampled_pad_mask, (0, chunk_pad_size), "constant", False
                )  # extra padding to the pad mask
                extra_padded_subsamlped_pad_mask = (
                    extra_padded_subsamlped_pad_mask.unsqueeze(-1).float()
                )
                masks_unfold = unfold_tensor(
                    extra_padded_subsamlped_pad_mask, max_seq_len
                )  # unfold the pad mask like we did to the input tensor
                masks_unfold = masks_unfold.squeeze(
                    -1
                ).bool()  # unfold op does not support bool tensor
            else:
                masks_unfold = None
            hs_mask = self.calculate_hs_mask(
                input_tensor, input_tensor.device, masks_unfold
            )  # calculate hs_mask based on the unfolded pad mask

        # layer_emb = None

        relative_attention_bias = self.init_relative_attention_bias(input_tensor)

        _simplified_path = (
            self.extra_layer_output_idx == -1 and relative_attention_bias is None
        )

        if _simplified_path:
            input_tensor, *_ = self.encoders(input_tensor, pos_k, pos_v, hs_mask)
        else:
            for i, layer in enumerate(self.encoders):
                input_tensor, _, _, _ = layer(
                    input_tensor,
                    pos_k,
                    pos_v,
                    hs_mask,
                    relative_attention_bias=relative_attention_bias,
                )

                # if i == self.extra_layer_output_idx:
                #     layer_emb = input_tensor

        if unfolded:
            embed_dim = input_tensor.shape[-1]
            input_tensor = input_tensor.reshape(ori_bz, -1, embed_dim)
            # if we ever padded before unfolding, we need to remove the padding
            if chunk_pad_size > 0:
                input_tensor = input_tensor[:, :-chunk_pad_size, :]

        return input_tensor, masks  # , layer_emb
```