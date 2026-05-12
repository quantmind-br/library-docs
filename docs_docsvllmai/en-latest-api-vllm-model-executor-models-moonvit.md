---
title: moonvit - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/moonvit/
source: sitemap
fetched_at: 2026-05-07T21:32:09.367931384-03:00
rendered_js: false
word_count: 621
summary: This document defines the architectural components and implementation details for the MoonVit vision encoder, including MLP blocks, patch embedding, and encoder layers with parallelized attention mechanisms.
tags:
    - vllm
    - moonvit
    - vision-encoder
    - pytorch
    - neural-network
    - model-parallelism
category: reference
---

## MLP2 [¶](#vllm.model_executor.models.moonvit.MLP2 "Permanent link")

Bases: `Module`

Parameters:

Name Type Description Default `dims` `list[int]`

\[in\_dim, hidden\_dim, out\_dim]

*required* `bias` `bool`

whether to use bias in linear layer.

`True`

Source code in `vllm/model_executor/models/moonvit.py`

```
classMLP2(nn.Module):
"""
    Args:
        dims: [in_dim, hidden_dim, out_dim]
        bias: whether to use bias in linear layer.
    """

    def__init__(
        self,
        dims: list[int],
        activation,
        bias: bool = True,
        prefix: str = "",
    ):
        super().__init__()
        assert len(dims) == 3
        self.use_data_parallel = is_vit_use_data_parallel()
        self.fc0 = ColumnParallelLinear(
            dims[0],
            dims[1],
            bias=bias,
            prefix=maybe_prefix(prefix, "fc0"),
            disable_tp=self.use_data_parallel,
        )
        self.fc1 = RowParallelLinear(
            dims[1],
            dims[2],
            bias=bias,
            prefix=maybe_prefix(prefix, "fc1"),
            disable_tp=self.use_data_parallel,
        )
        self.activation = activation

    defforward(self, x: torch.Tensor) -> torch.Tensor:
        x, _ = self.fc0(x)
        x = self.activation(x)
        x, _ = self.fc1(x)
        return x
```

## MoonVisionPatchEmbed [¶](#vllm.model_executor.models.moonvit.MoonVisionPatchEmbed "Permanent link")

Bases: `Module`

Source code in `vllm/model_executor/models/moonvit.py`

```
classMoonVisionPatchEmbed(nn.Module):
    def__init__(
        self,
        out_dim: int,
        in_dim: int = 3,
        patch_size: int | tuple[int, int] = (14, 14),
        pos_emb_height: int = 14,
        pos_emb_width: int = 14,
    ):
        super().__init__()
        assert isinstance(patch_size, (int, Sequence)), (
            f"Invalid patch_size type: {type(patch_size)}"
        )
        if isinstance(patch_size, int):
            patch_size = (patch_size, patch_size)
        assert len(patch_size) == 2, (
            f"Expected patch_size to be a tuple of 2, got {patch_size}"
        )
        self.patch_size = patch_size

        self.proj = Conv2dLayer(
            in_dim, out_dim, kernel_size=patch_size, stride=patch_size
        )

        self.pos_emb = Learnable2DInterpPosEmb(
            height=pos_emb_height, width=pos_emb_width, dim=out_dim
        )

    defforward(self, x: torch.Tensor, grid_hw: torch.Tensor) -> torch.Tensor:
"""
        Args:
            x (L, Channels): input tensor
            grid_hw (N, 2): grid height and width

        Returns:
            (L, Cout) tensor
        """
        x = self.proj(x).view(x.size(0), -1)
        # apply positional embedding
        x = self.pos_emb(x, grid_hw)
        return x
```

### forward [¶](#vllm.model_executor.models.moonvit.MoonVisionPatchEmbed.forward "Permanent link")

Parameters:

Name Type Description Default `x` `(L, Channels)`

input tensor

*required* `grid_hw` `(N, 2)`

grid height and width

*required*

Returns:

Type Description `Tensor`

(L, Cout) tensor

Source code in `vllm/model_executor/models/moonvit.py`

```
defforward(self, x: torch.Tensor, grid_hw: torch.Tensor) -> torch.Tensor:
"""
    Args:
        x (L, Channels): input tensor
        grid_hw (N, 2): grid height and width

    Returns:
        (L, Cout) tensor
    """
    x = self.proj(x).view(x.size(0), -1)
    # apply positional embedding
    x = self.pos_emb(x, grid_hw)
    return x
```

## MoonVitEncoderLayer [¶](#vllm.model_executor.models.moonvit.MoonVitEncoderLayer "Permanent link")

Bases: `Module`

Source code in `vllm/model_executor/models/moonvit.py`

```
classMoonVitEncoderLayer(nn.Module):
    def__init__(
        self,
        num_heads: int,
        hidden_dim: int,
        mlp_dim: int,
        prefix: str = "",
        *,
        activation=F.gelu,
        attn_bias: bool = False,
    ):
        super().__init__()
        self.use_data_parallel = is_vit_use_data_parallel()

        self.num_heads = num_heads
        self.hidden_dim = hidden_dim
        self.hidden_size_per_attention_head = self.hidden_dim // self.num_heads
        self.tp_size = (
            1 if self.use_data_parallel else get_tensor_model_parallel_world_size()
        )
        self.num_attention_heads_per_partition = divide(num_heads, self.tp_size)

        self.norm0 = nn.LayerNorm(hidden_dim)
        self.norm1 = nn.LayerNorm(hidden_dim)
        self.mlp = MLP2(
            [hidden_dim, mlp_dim, hidden_dim],
            activation,
            prefix=f"{prefix}.mlp",
        )
        self.wqkv = QKVParallelLinear(
            hidden_size=hidden_dim,
            head_size=self.hidden_size_per_attention_head,
            total_num_heads=num_heads,
            total_num_kv_heads=num_heads,
            bias=attn_bias,
            prefix=f"{prefix}.wqkv",
            disable_tp=self.use_data_parallel,
        )
        self.wo = RowParallelLinear(
            hidden_dim,
            hidden_dim,
            bias=attn_bias,
            prefix=f"{prefix}.wo",
            disable_tp=self.use_data_parallel,
        )
        self.attn = MMEncoderAttention(
            num_heads=self.num_attention_heads_per_partition,
            head_size=self.hidden_size_per_attention_head,
            scale=self.hidden_size_per_attention_head**-0.5,
            prefix=f"{prefix}.attn",
        )

    defattention_qkvpacked(
        self,
        x: torch.Tensor,
        cu_seqlens: torch.Tensor,
        rope_freqs_cis: torch.Tensor | None = None,
    ):
"""
        Args:
            x (torch.Tensor): (seqlen, hidden_dim)
            cu_seqlens (torch.Tensor):
        """
        seq_length = x.size(0)
        xqkv, _ = self.wqkv(x)

        qkv_shape = xqkv.size()[:-1] + (
            3,
            self.num_attention_heads_per_partition,
            self.hidden_size_per_attention_head,
        )
        # xqkv: (batch_size, seqlen, 3, nheads, headdim)
        xqkv = xqkv.view(*qkv_shape)
        xq, xk, xv = torch.unbind(xqkv, dim=-3)

        xq, xk = apply_rope(xq, xk, rope_freqs_cis)

        max_seqlen = (cu_seqlens[1:] - cu_seqlens[:-1]).max()
        attn_out = self.attn(
            xq.unsqueeze(0),
            xk.unsqueeze(0),
            xv.unsqueeze(0),
            cu_seqlens=cu_seqlens,
            max_seqlen=max_seqlen,
        )
        attn_out = attn_out.reshape(
            seq_length,
            self.num_attention_heads_per_partition
            * self.hidden_size_per_attention_head,
        )
        attn_out, _ = self.wo(attn_out)
        return attn_out

    defforward(
        self,
        hidden_states: torch.Tensor,
        cu_seqlens: torch.Tensor,
        rope_freqs_cis: torch.Tensor | None = None,
    ) -> torch.Tensor:
"""
        Args:
            hidden_states: non-packed (B, N, D) or packed (L, D). if non-packed, seqlens should be None, if packed, seqlens should be set

        Returns:
            output: same shape of input, non-packed (B, N, D) for non-packed input, (L, D) for packed input
        """
        residual = hidden_states
        hidden_states = self.norm0(hidden_states)
        attn_out = self.attention_qkvpacked(
            hidden_states, cu_seqlens, rope_freqs_cis=rope_freqs_cis
        )
        hidden_states = residual + attn_out

        residual = hidden_states
        hidden_states = self.mlp(self.norm1(hidden_states))
        hidden_states = residual + hidden_states
        return hidden_states
```

### attention\_qkvpacked [¶](#vllm.model_executor.models.moonvit.MoonVitEncoderLayer.attention_qkvpacked "Permanent link")

```
attention_qkvpacked(
    x: Tensor,
    cu_seqlens: Tensor,
    rope_freqs_cis: Tensor | None = None,
)
```

Parameters:

Name Type Description Default `x` `Tensor`

(seqlen, hidden\_dim)

*required* `cu_seqlens` `Tensor` *required*

Source code in `vllm/model_executor/models/moonvit.py`

```
defattention_qkvpacked(
    self,
    x: torch.Tensor,
    cu_seqlens: torch.Tensor,
    rope_freqs_cis: torch.Tensor | None = None,
):
"""
    Args:
        x (torch.Tensor): (seqlen, hidden_dim)
        cu_seqlens (torch.Tensor):
    """
    seq_length = x.size(0)
    xqkv, _ = self.wqkv(x)

    qkv_shape = xqkv.size()[:-1] + (
        3,
        self.num_attention_heads_per_partition,
        self.hidden_size_per_attention_head,
    )
    # xqkv: (batch_size, seqlen, 3, nheads, headdim)
    xqkv = xqkv.view(*qkv_shape)
    xq, xk, xv = torch.unbind(xqkv, dim=-3)

    xq, xk = apply_rope(xq, xk, rope_freqs_cis)

    max_seqlen = (cu_seqlens[1:] - cu_seqlens[:-1]).max()
    attn_out = self.attn(
        xq.unsqueeze(0),
        xk.unsqueeze(0),
        xv.unsqueeze(0),
        cu_seqlens=cu_seqlens,
        max_seqlen=max_seqlen,
    )
    attn_out = attn_out.reshape(
        seq_length,
        self.num_attention_heads_per_partition
        * self.hidden_size_per_attention_head,
    )
    attn_out, _ = self.wo(attn_out)
    return attn_out
```

### forward [¶](#vllm.model_executor.models.moonvit.MoonVitEncoderLayer.forward "Permanent link")

Parameters:

Name Type Description Default `hidden_states` `Tensor`

non-packed (B, N, D) or packed (L, D). if non-packed, seqlens should be None, if packed, seqlens should be set

*required*

Returns:

Name Type Description `output` `Tensor`

same shape of input, non-packed (B, N, D) for non-packed input, (L, D) for packed input

Source code in `vllm/model_executor/models/moonvit.py`

```
defforward(
    self,
    hidden_states: torch.Tensor,
    cu_seqlens: torch.Tensor,
    rope_freqs_cis: torch.Tensor | None = None,
) -> torch.Tensor:
"""
    Args:
        hidden_states: non-packed (B, N, D) or packed (L, D). if non-packed, seqlens should be None, if packed, seqlens should be set

    Returns:
        output: same shape of input, non-packed (B, N, D) for non-packed input, (L, D) for packed input
    """
    residual = hidden_states
    hidden_states = self.norm0(hidden_states)
    attn_out = self.attention_qkvpacked(
        hidden_states, cu_seqlens, rope_freqs_cis=rope_freqs_cis
    )
    hidden_states = residual + attn_out

    residual = hidden_states
    hidden_states = self.mlp(self.norm1(hidden_states))
    hidden_states = residual + hidden_states
    return hidden_states
```

## MoonVitPretrainedModel [¶](#vllm.model_executor.models.moonvit.MoonVitPretrainedModel "Permanent link")

Bases: `PreTrainedModel`

Source code in `vllm/model_executor/models/moonvit.py`

```
classMoonVitPretrainedModel(PreTrainedModel):
    config_class = MoonViTConfig
    model_type = "moonvit"
    _no_split_modules = ["PackingTransformer"]
    _supports_flash_attn_2 = True
    _supports_sdpa = True

    def__init__(
        self,
        config: MoonViTConfig,
        prefix: str = "",
        *inputs,
        **kwargs,
    ):
        super().__init__(config, *inputs, **kwargs)
        config = deepcopy(config)
        self.merge_kernel_size = config.merge_kernel_size
        self.hidden_size = config.hidden_size
        self.patch_size = config.patch_size
        self.vit_processing_type = "rope_2d"
        self.patch_embed = MoonVisionPatchEmbed(
            out_dim=config.hidden_size,
            patch_size=config.patch_size,
            pos_emb_height=config.init_pos_emb_height,
            pos_emb_width=config.init_pos_emb_width,
        )

        self.encoder = MoonVitEncoder(
            hidden_dim=config.hidden_size,
            num_layers=config.num_hidden_layers,
            block_cfg={
                "num_heads": config.num_attention_heads,
                "hidden_dim": config.hidden_size,
                "mlp_dim": config.intermediate_size,
                "activation": ACT2FN["gelu_pytorch_tanh"],
                "attn_bias": True,
            },
            prefix=f"{prefix}.encoder",
        )

    defforward(
        self, pixel_values: torch.Tensor, grid_hw: torch.Tensor
    ) -> torch.Tensor:
"""
        Args:
            pixel_values (torch.Tensor): The input pixel values.
            grid_hw (torch.Tensor): The grid height and width.

        Returns:
            torch.Tensor: The output tokens.
        """
        hidden_states = self.patch_embed(pixel_values, grid_hw)
        hidden_states = self.encoder(hidden_states, grid_hw)
        hidden_states = patch_merger(
            hidden_states, grid_hw, merge_kernel_size=self.merge_kernel_size
        )
        return hidden_states
```

### forward [¶](#vllm.model_executor.models.moonvit.MoonVitPretrainedModel.forward "Permanent link")

Parameters:

Name Type Description Default `pixel_values` `Tensor`

The input pixel values.

*required* `grid_hw` `Tensor`

The grid height and width.

*required*

Returns:

Type Description `Tensor`

torch.Tensor: The output tokens.

Source code in `vllm/model_executor/models/moonvit.py`

```
defforward(
    self, pixel_values: torch.Tensor, grid_hw: torch.Tensor
) -> torch.Tensor:
"""
    Args:
        pixel_values (torch.Tensor): The input pixel values.
        grid_hw (torch.Tensor): The grid height and width.

    Returns:
        torch.Tensor: The output tokens.
    """
    hidden_states = self.patch_embed(pixel_values, grid_hw)
    hidden_states = self.encoder(hidden_states, grid_hw)
    hidden_states = patch_merger(
        hidden_states, grid_hw, merge_kernel_size=self.merge_kernel_size
    )
    return hidden_states
```

## Rope2DPosEmb [¶](#vllm.model_executor.models.moonvit.Rope2DPosEmb "Permanent link")

Bases: `Module`

2D rotary position embedding with multi-resolution support.

This class is intended to be used in the following way: 1. Before training, create an instance of Rope2DPosEmb. This instance will hold the precomputed cis. 2. Before each forward pass, call `get_freqs_cis_by_*` to get the `freqs_cis` tensor for this iteration. 3. During the forward pass, pass the `freqs_cis` tensor to each attention layer, and call `apply` just before each attention operation. The rope is shared across all attention layers and all heads.

Refs: - RoFormer: https://arxiv.org/abs/2104.09864 - VisionLLaMA: https://arxiv.org/abs/2403.00522 - https://github.com/Meituan-AutoML/VisionLLaMA/blob/main/dit/models.py

Parameters:

Name Type Description Default `dim` `int`

usually the multi-head attention dimension, should be divisible by 4 (TODO: relax this constraint if needed)

*required* `max_height` `int`

the maximum height of the 2D grid

*required* `max_width` `int`

the maximum width of the 2D grid

*required* `theta_base` `float`

the base of the theta

`10000` `device` `str`

the device to store the precomputed cis

`device_type`

Source code in `vllm/model_executor/models/moonvit.py`

```
classRope2DPosEmb(nn.Module):
"""2D rotary position embedding with multi-resolution support.

    This class is intended to be used in the following way:
    1. Before training, create an instance of Rope2DPosEmb. This instance will hold the precomputed cis.
    2. Before each forward pass, call `get_freqs_cis_by_*` to get the `freqs_cis` tensor for this iteration.
    3. During the forward pass, pass the `freqs_cis` tensor to each attention layer, and call `apply` just before each attention operation.
        The rope is shared across all attention layers and all heads.

    Refs:
    - RoFormer: https://arxiv.org/abs/2104.09864
    - VisionLLaMA: https://arxiv.org/abs/2403.00522
    - https://github.com/Meituan-AutoML/VisionLLaMA/blob/main/dit/models.py

    Args:
        dim (int): usually the multi-head attention dimension, should be divisible by 4 (TODO: relax this constraint if needed)
        max_height (int): the maximum height of the 2D grid
        max_width (int): the maximum width of the 2D grid
        theta_base (float): the base of the theta
        device (str): the device to store the precomputed cis
    """

    def__init__(
        self,
        dim: int,
        max_height: int,
        max_width: int,
        theta_base=10000,
        device=current_platform.device_type,
    ):
        super().__init__()
        self.dim = dim
        assert self.dim % 4 == 0, "dim must be divisible by 4"
        self.max_height = max_height
        self.max_width = max_width
        self.theta_base = theta_base
        self.device = device

    defextra_repr(self):
        return f"dim={self.dim}, max_height={self.max_height}, max_width={self.max_width}, theta_base={self.theta_base}"

    @cached_property
    defprecomputed_freqs_cis(self) -> torch.Tensor:
"""Calculate the cis(freqs) for each position in the 2D grid.

        Return: complex tensor of shape (max_height, max_width, dim//2) and value:
            height axis: ret[h, w, 2*i] = cis(h * theta_base**(-4*i/dim))
            weight axis: ret[h, w, 2*i+1] = cis(w * theta_base**(-4*i/dim))   with (i in [0, dim//4))
            note: `cis` is a mathematical notation defined by cis x = cos x + i sin x,
        """
        N = self.max_height * self.max_width
        flat_pos = torch.arange(0, N).float().to(self.device)
        x_pos = flat_pos % self.max_width
        y_pos = flat_pos // self.max_width
        dim_range = (
            torch.arange(0, self.dim, 4)[: (self.dim // 4)].float().to(self.device)
        )  # C/4
        freqs = 1.0 / (self.theta_base ** (dim_range / self.dim))
        x_freqs = torch.outer(x_pos, freqs).float()  # N, C/4
        y_freqs = torch.outer(y_pos, freqs).float()  # N, C/4
        x_cis = torch.polar(torch.ones_like(x_freqs), x_freqs)  # N, C/4
        y_cis = torch.polar(torch.ones_like(y_freqs), y_freqs)  # N, C/4
        # N, C/4, 2
        freqs_cis = torch.cat(
            [x_cis.unsqueeze(dim=-1), y_cis.unsqueeze(dim=-1)], dim=-1
        )
        # max_height, max_width, C/2
        freqs_cis = freqs_cis.reshape(self.max_height, self.max_width, -1)
        return freqs_cis

    defget_freqs_cis_by_seqlens(self, grid_hws: torch.Tensor) -> torch.Tensor:
"""
        Args:
            grid_hws (torch.Tensor): containing list of (height, width) or (t, height, width) tuples.
        Returns:
            freqs_cis: tensor of shape (sum(t * height * width), dim//2)
        """
        shapes = grid_hws.tolist()
        assert all(
            1 <= h <= self.max_height and 1 <= w <= self.max_width for h, w in shapes
        ), (
            shapes,
            self.max_height,
            self.max_width,
        )
        freqs_cis = torch.cat(
            [
                self.precomputed_freqs_cis[:h, :w].reshape(-1, self.dim // 2)
                for h, w in shapes
            ],
            dim=0,
        )
        return freqs_cis

    defget_freqs_cis_by_idx(
        self, pos_idx: torch.Tensor, pos_idx_mask: torch.Tensor
    ) -> torch.Tensor:
"""
        Args:
            pos_idx: tensor of shape (..., 2), It contains the (h, w) position indices of each 2D token.
            pos_idx_mask: a mask of shape (...), the leading dimensions should be the same as pos_idx.
                Rope will only be applied to the tokens with True mask. `freqs_cis` for the tokens with False mask with be ones.
        Return:
            freqs_cis: tensor of shape (..., dim//2)
        """
        assert (
            pos_idx.shape[:-1] == pos_idx_mask.shape
            and pos_idx.shape[-1] == 2
            and pos_idx.ndim == pos_idx_mask.ndim + 1
        ), (pos_idx.shape, pos_idx_mask.shape)
        assert pos_idx_mask.dtype == torch.bool, pos_idx_mask.dtype

        shp = pos_idx_mask.shape + (self.dim // 2,)  # ..., head_dim/2
        freqs_cis = torch.ones(
            shp, dtype=torch.complex64, device=self.device
        )  # ..., head_dim/2
        freqs_cis[pos_idx_mask] = self.precomputed_freqs_cis[
            pos_idx[..., 0][pos_idx_mask], pos_idx[..., 1][pos_idx_mask]
        ]
        return freqs_cis
```

### precomputed\_freqs\_cis `cached` `property` [¶](#vllm.model_executor.models.moonvit.Rope2DPosEmb.precomputed_freqs_cis "Permanent link")

Calculate the cis(freqs) for each position in the 2D grid.

complex tensor of shape (max\_height, max\_width, dim//2) and value:

height axis: ret\[h, w, 2*i] = cis(h * theta\_base(-4*i/dim)) weight axis: ret\[h, w, 2*i+1] = cis(w * theta\_base(-4*i/dim)) with (i in [0, dim//4)) note: `cis` is a mathematical notation defined by cis x = cos x + i sin x,

### get\_freqs\_cis\_by\_idx [¶](#vllm.model_executor.models.moonvit.Rope2DPosEmb.get_freqs_cis_by_idx "Permanent link")

Parameters:

Name Type Description Default `pos_idx` `Tensor`

tensor of shape (..., 2), It contains the (h, w) position indices of each 2D token.

*required* `pos_idx_mask` `Tensor`

a mask of shape (...), the leading dimensions should be the same as pos\_idx. Rope will only be applied to the tokens with True mask. `freqs_cis` for the tokens with False mask with be ones.

*required*

Return: freqs\_cis: tensor of shape (..., dim//2)

Source code in `vllm/model_executor/models/moonvit.py`

```
defget_freqs_cis_by_idx(
    self, pos_idx: torch.Tensor, pos_idx_mask: torch.Tensor
) -> torch.Tensor:
"""
    Args:
        pos_idx: tensor of shape (..., 2), It contains the (h, w) position indices of each 2D token.
        pos_idx_mask: a mask of shape (...), the leading dimensions should be the same as pos_idx.
            Rope will only be applied to the tokens with True mask. `freqs_cis` for the tokens with False mask with be ones.
    Return:
        freqs_cis: tensor of shape (..., dim//2)
    """
    assert (
        pos_idx.shape[:-1] == pos_idx_mask.shape
        and pos_idx.shape[-1] == 2
        and pos_idx.ndim == pos_idx_mask.ndim + 1
    ), (pos_idx.shape, pos_idx_mask.shape)
    assert pos_idx_mask.dtype == torch.bool, pos_idx_mask.dtype

    shp = pos_idx_mask.shape + (self.dim // 2,)  # ..., head_dim/2
    freqs_cis = torch.ones(
        shp, dtype=torch.complex64, device=self.device
    )  # ..., head_dim/2
    freqs_cis[pos_idx_mask] = self.precomputed_freqs_cis[
        pos_idx[..., 0][pos_idx_mask], pos_idx[..., 1][pos_idx_mask]
    ]
    return freqs_cis
```

### get\_freqs\_cis\_by\_seqlens [¶](#vllm.model_executor.models.moonvit.Rope2DPosEmb.get_freqs_cis_by_seqlens "Permanent link")

Parameters:

Name Type Description Default `grid_hws` `Tensor`

containing list of (height, width) or (t, height, width) tuples.

*required*

Returns: freqs\_cis: tensor of shape (sum(t * height * width), dim//2)

Source code in `vllm/model_executor/models/moonvit.py`

```
defget_freqs_cis_by_seqlens(self, grid_hws: torch.Tensor) -> torch.Tensor:
"""
    Args:
        grid_hws (torch.Tensor): containing list of (height, width) or (t, height, width) tuples.
    Returns:
        freqs_cis: tensor of shape (sum(t * height * width), dim//2)
    """
    shapes = grid_hws.tolist()
    assert all(
        1 <= h <= self.max_height and 1 <= w <= self.max_width for h, w in shapes
    ), (
        shapes,
        self.max_height,
        self.max_width,
    )
    freqs_cis = torch.cat(
        [
            self.precomputed_freqs_cis[:h, :w].reshape(-1, self.dim // 2)
            for h, w in shapes
        ],
        dim=0,
    )
    return freqs_cis
```

## apply\_rope [¶](#vllm.model_executor.models.moonvit.apply_rope "Permanent link")

(The leading dimensions of all inputs should be the same)

Name Type Description Default `xq` `Tensor`

query, tensor of shape (..., num\_heads, head\_dim)

*required* `xk` `Tensor`

key, tensor of shape (..., num\_heads, head\_dim)

*required* `freqs_cis` `Tensor`

tensor of shape (..., head\_dim/2), dtype=torch.complex64. It contains the precomputed cis(freqs) for each position in the 2D grid.

*required*

Returns: xq\_out, xk\_out: tensors of shape (..., num\_heads, head\_dim)

Source code in `vllm/model_executor/models/moonvit.py`

```
defapply_rope(
    xq: torch.Tensor, xk: torch.Tensor, freqs_cis: torch.Tensor
) -> tuple[torch.Tensor, torch.Tensor]:
"""
    Args: (The leading dimensions of all inputs should be the same)
        xq: query, tensor of shape (..., num_heads, head_dim)
        xk: key, tensor of shape (..., num_heads, head_dim)
        freqs_cis: tensor of shape (..., head_dim/2), dtype=torch.complex64. It contains the precomputed cis(freqs) for each position in the 2D grid.
    Returns:
        xq_out, xk_out: tensors of shape (..., num_heads, head_dim)
    """
    _apply_rope_input_validation(xq, freqs_cis)
    _apply_rope_input_validation(xk, freqs_cis)

    freqs_cis = freqs_cis.unsqueeze(-2)  # ..., 1, head_dim/2
    # ..., num_heads, head_dim/2
    xq_ = torch.view_as_complex(xq.float().view(*xq.shape[:-1], -1, 2))
    xk_ = torch.view_as_complex(xk.float().view(*xq.shape[:-1], -1, 2))
    xq_out = torch.view_as_real(xq_ * freqs_cis).flatten(-2)  # ..., num_heads, head_dim
    xk_out = torch.view_as_real(xk_ * freqs_cis).flatten(-2)  # ..., num_heads, head_dim
    return xq_out.type_as(xq), xk_out.type_as(xk)
```