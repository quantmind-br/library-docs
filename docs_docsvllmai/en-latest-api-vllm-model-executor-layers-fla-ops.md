---
title: ops - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fla/ops/
source: sitemap
fetched_at: 2026-05-07T21:24:12.686307294-03:00
rendered_js: false
word_count: 1002
summary: This document provides technical documentation and API specifications for specialized layers and operations used in FLA models, including RMSNormGated and chunked gated delta rule implementations.
tags:
    - deep-learning
    - vllm
    - neural-network-layers
    - gated-attention
    - rmsnorm
    - tensor-operations
category: api
---

Modules:

Name Description `chunk` `chunk_scaled_dot_kkt` `fused_gdn_prefill_post_conv`

Fused post-conv1d preparation for GDN prefill.

`fused_recurrent` `fused_sigmoid_gating` `kda` `layernorm_guard` `op` `solve_tril` `utils`

## RMSNormGated [¶](#vllm.model_executor.layers.fla.ops.RMSNormGated "Permanent link")

Bases: `Module`

Source code in `vllm/model_executor/layers/fla/ops/layernorm_guard.py`

```
classRMSNormGated(nn.Module):
    def__init__(
        self,
        hidden_size,
        eps: float = 1e-5,
        group_size: int | None = None,
        norm_before_gate: bool = False,
        device: torch.device | None = None,
        dtype: torch.dtype | None = None,
        activation: str = "swish",
    ):
"""If group_size is not None, we do GroupNorm with each group having group_size elements.
        group_size=None is equivalent to group_size=hidden_size (i.e. there's only 1 group).
        """
        factory_kwargs = {"device": device, "dtype": dtype}
        super().__init__()
        self.eps = eps
        self.activation = activation
        self.weight = nn.Parameter(torch.empty(hidden_size, **factory_kwargs))
        self.register_parameter("bias", None)
        self.group_size = group_size
        self.norm_before_gate = norm_before_gate
        self.reset_parameters()

    defreset_parameters(self):
        torch.nn.init.ones_(self.weight)

    defforward(self, x, z=None):
"""If z is not None, we do norm(x) * silu(z) if norm_before_gate, else norm(x * silu(z))"""
        return rmsnorm_fn(
            x,
            self.weight,
            self.bias,
            z=z,
            eps=self.eps,
            group_size=self.group_size,
            norm_before_gate=self.norm_before_gate,
            activation=self.activation,
        )
```

### \_\_init\__ [¶](#vllm.model_executor.layers.fla.ops.RMSNormGated.__init__ "Permanent link")

```
__init__(
    hidden_size,
    eps: float = 1e-05,
    group_size: int | None = None,
    norm_before_gate: bool = False,
    device: device | None = None,
    dtype: dtype | None = None,
    activation: str = "swish",
)
```

If group\_size is not None, we do GroupNorm with each group having group\_size elements. group\_size=None is equivalent to group\_size=hidden\_size (i.e. there's only 1 group).

Source code in `vllm/model_executor/layers/fla/ops/layernorm_guard.py`

```
def__init__(
    self,
    hidden_size,
    eps: float = 1e-5,
    group_size: int | None = None,
    norm_before_gate: bool = False,
    device: torch.device | None = None,
    dtype: torch.dtype | None = None,
    activation: str = "swish",
):
"""If group_size is not None, we do GroupNorm with each group having group_size elements.
    group_size=None is equivalent to group_size=hidden_size (i.e. there's only 1 group).
    """
    factory_kwargs = {"device": device, "dtype": dtype}
    super().__init__()
    self.eps = eps
    self.activation = activation
    self.weight = nn.Parameter(torch.empty(hidden_size, **factory_kwargs))
    self.register_parameter("bias", None)
    self.group_size = group_size
    self.norm_before_gate = norm_before_gate
    self.reset_parameters()
```

### forward [¶](#vllm.model_executor.layers.fla.ops.RMSNormGated.forward "Permanent link")

If z is not None, we do norm(x) * silu(z) if norm\_before\_gate, else norm(x * silu(z))

Source code in `vllm/model_executor/layers/fla/ops/layernorm_guard.py`

```
defforward(self, x, z=None):
"""If z is not None, we do norm(x) * silu(z) if norm_before_gate, else norm(x * silu(z))"""
    return rmsnorm_fn(
        x,
        self.weight,
        self.bias,
        z=z,
        eps=self.eps,
        group_size=self.group_size,
        norm_before_gate=self.norm_before_gate,
        activation=self.activation,
    )
```

## chunk\_gated\_delta\_rule [¶](#vllm.model_executor.layers.fla.ops.chunk_gated_delta_rule "Permanent link")

```
chunk_gated_delta_rule(
    q: Tensor,
    k: Tensor,
    v: Tensor,
    g: Tensor,
    beta: Tensor,
    scale: float = None,
    initial_state: Tensor = None,
    output_final_state: bool = False,
    cu_seqlens: Tensor | None = None,
    chunk_indices: Tensor | None = None,
    chunk_offsets: Tensor | None = None,
    use_qk_l2norm_in_kernel: bool = False,
)
```

Parameters:

Name Type Description Default `q` `Tensor`

Queries of shape `[B, T, H, K]`.

*required* `k` `Tensor`

Keys of shape `[B, T, H, K]`.

*required* `v` `Tensor`

Values of shape `[B, T, H, V]`.

*required* `g` `Tensor`

(forget) Gating tensor (in log space!) of shape `[B, T, H]`.

*required* `beta` `Tensor`

Betas of shape `[B, T, H]`.

*required* `scale` `Optional[int]`

Scale factor for the RetNet attention scores. If not provided, it will default to `1 / sqrt(K)`. Default: `None`.

`None` `initial_state` `Optional[Tensor]`

Initial state of shape `[N, H, V, K]` for `N` input sequences. For equal-length input sequences, `N` equals the batch size `B`. Default: `None`.

`None` `output_final_state` `Optional[bool]`

Whether to output the final state of shape `[N, H, V, K]`. Default: `False`.

`False` `cu_seqlens` `Tensor`

Cumulative sequence lengths of shape `[N+1]` used for variable-length training, consistent with the FlashAttention API.

`None`

Returns: o (torch.Tensor): Outputs of shape `[B, T, H, V]`. final\_state (torch.Tensor): Final state of shape `[N, H, V, K]` if `output_final_state=True` else `None`.

Examples:: &gt;&gt;&gt; import torch &gt;&gt;&gt; import torch.nn.functional as F &gt;&gt;&gt; from einops import rearrange &gt;&gt;&gt; from fla.ops.gated\_delta\_rule import chunk\_gated\_delta\_rule # inputs with equal lengths &gt;&gt;&gt; B, T, H, K, V = 4, 2048, 4, 512, 512 &gt;&gt;&gt; q = torch.randn(B, T, H, K, dtype=torch.bfloat16, device='cuda') &gt;&gt;&gt; k = F.normalize(torch.randn(B, T, H, K, dtype=torch.bfloat16, device='cuda'), p=2, dim=-1) &gt;&gt;&gt; v = torch.randn(B, T, H, V, dtype=torch.bfloat16, device='cuda') &gt;&gt;&gt; beta = torch.rand(B, T, H, dtype=torch.bfloat16, device='cuda').sigmoid() &gt;&gt;&gt; g = F.logsigmoid(torch.rand(B, T, H, dtype=torch.bfloat16, device='cuda')) &gt;&gt;&gt; h0 = torch.randn(B, H, V, K, dtype=torch.bfloat16, device='cuda') &gt;&gt;&gt; o, ht = chunk\_gated\_delta\_rule( q, k, v, g, beta, initial\_state=h0, output\_final\_state=True ) # for variable-length inputs, the batch size `B` is expected to be 1 and `cu_seqlens` is required &gt;&gt;&gt; q, k, v, beta, g = map(lambda x: rearrange(x, 'b t ... -&gt; 1 (b t) ...'), (q, k, v, beta, g)) # for a batch with 4 sequences, `cu_seqlens` with 5 start/end positions are expected &gt;&gt;&gt; cu\_seqlens = q.new\_tensor(\[0, 2048, 4096, 6144, 8192], dtype=torch.int32) &gt;&gt;&gt; o\_var, ht\_var = chunk\_gated\_delta\_rule( q, k, v, g, beta, initial\_state=h0, output\_final\_state=True, cu\_seqlens=cu\_seqlens )

Source code in `vllm/model_executor/layers/fla/ops/chunk.py`

```
@torch.compiler.disable
defchunk_gated_delta_rule(
    q: torch.Tensor,
    k: torch.Tensor,
    v: torch.Tensor,
    g: torch.Tensor,
    beta: torch.Tensor,
    scale: float = None,
    initial_state: torch.Tensor = None,
    output_final_state: bool = False,
    cu_seqlens: torch.Tensor | None = None,
    chunk_indices: torch.Tensor | None = None,
    chunk_offsets: torch.Tensor | None = None,
    use_qk_l2norm_in_kernel: bool = False,
):
r"""
    Args:
        q (torch.Tensor):
            Queries of shape `[B, T, H, K]`.
        k (torch.Tensor):
            Keys of shape `[B, T, H, K]`.
        v (torch.Tensor):
            Values of shape `[B, T, H, V]`.
        g (torch.Tensor):
            (forget) Gating tensor (in log space!) of shape `[B, T, H]`.
        beta (torch.Tensor):
            Betas of shape `[B, T, H]`.
        scale (Optional[int]):
            Scale factor for the RetNet attention scores.
            If not provided, it will default to `1 / sqrt(K)`. Default: `None`.
        initial_state (Optional[torch.Tensor]):
            Initial state of shape `[N, H, V, K]` for `N` input sequences.
            For equal-length input sequences, `N` equals the batch size `B`.
            Default: `None`.
        output_final_state (Optional[bool]):
            Whether to output the final state of shape `[N, H, V, K]`. Default: `False`.
        cu_seqlens (torch.Tensor):
            Cumulative sequence lengths of shape `[N+1]` used for variable-length training,
            consistent with the FlashAttention API.
    Returns:
        o (torch.Tensor):
            Outputs of shape `[B, T, H, V]`.
        final_state (torch.Tensor):
            Final state of shape `[N, H, V, K]` if `output_final_state=True` else `None`.

    Examples::
        >>> import torch
        >>> import torch.nn.functional as F
        >>> from einops import rearrange
        >>> from fla.ops.gated_delta_rule import chunk_gated_delta_rule
        # inputs with equal lengths
        >>> B, T, H, K, V = 4, 2048, 4, 512, 512
        >>> q = torch.randn(B, T, H, K, dtype=torch.bfloat16, device='cuda')
        >>> k = F.normalize(torch.randn(B, T, H, K, dtype=torch.bfloat16, device='cuda'), p=2, dim=-1)
        >>> v = torch.randn(B, T, H, V, dtype=torch.bfloat16, device='cuda')
        >>> beta = torch.rand(B, T, H, dtype=torch.bfloat16, device='cuda').sigmoid()
        >>> g = F.logsigmoid(torch.rand(B, T, H, dtype=torch.bfloat16, device='cuda'))
        >>> h0 = torch.randn(B, H, V, K, dtype=torch.bfloat16, device='cuda')
        >>> o, ht = chunk_gated_delta_rule(
            q, k, v, g, beta,
            initial_state=h0,
            output_final_state=True
        )
        # for variable-length inputs, the batch size `B` is expected to be 1 and `cu_seqlens` is required
        >>> q, k, v, beta, g = map(lambda x: rearrange(x, 'b t ... -> 1 (b t) ...'), (q, k, v, beta, g))
        # for a batch with 4 sequences, `cu_seqlens` with 5 start/end positions are expected
        >>> cu_seqlens = q.new_tensor([0, 2048, 4096, 6144, 8192], dtype=torch.int32)
        >>> o_var, ht_var = chunk_gated_delta_rule(
            q, k, v, g, beta,
            initial_state=h0,
            output_final_state=True,
            cu_seqlens=cu_seqlens
        )
    """
    assert q.dtype == k.dtype == v.dtype
    assert q.dtype != torch.float32, (
        "ChunkGatedDeltaRuleFunction does not support float32. Please use bfloat16."
    )
    assert len(beta.shape) == 3, "beta must be of shape [B, T, H]."
    if cu_seqlens is not None:
        if q.shape[0] != 1:
            raise ValueError(
                f"The batch size is expected to be 1 rather than {q.shape[0]} when using `cu_seqlens`."
                f"Please flatten variable-length inputs before processing."
            )
        if initial_state is not None and initial_state.shape[0] != len(cu_seqlens) - 1:
            raise ValueError(
                f"The number of initial states is expected to be equal to the number of input sequences, "
                f"i.e., {len(cu_seqlens)-1} rather than {initial_state.shape[0]}."
            )
    if scale is None:
        scale = k.shape[-1] ** -0.5
    o, final_state = ChunkGatedDeltaRuleFunction.apply(
        q,
        k,
        v,
        g,
        beta,
        scale,
        initial_state,
        output_final_state,
        cu_seqlens,
        chunk_indices,
        chunk_offsets,
        use_qk_l2norm_in_kernel,
    )
    return o, final_state
```

## fused\_post\_conv\_prep [¶](#vllm.model_executor.layers.fla.ops.fused_post_conv_prep "Permanent link")

```
fused_post_conv_prep(
    conv_output: Tensor,
    a: Tensor,
    b: Tensor,
    A_log: Tensor,
    dt_bias: Tensor,
    num_k_heads: int,
    head_k_dim: int,
    head_v_dim: int,
    apply_l2norm: bool = True,
    output_g_exp: bool = False,
) -> tuple[Tensor, Tensor, Tensor, Tensor, Tensor]
```

Fused post-conv1d prep: split + l2norm + gating in one kernel.

Parameters:

Name Type Description Default `conv_output` `Tensor`

\[L, qkv\_dim] contiguous conv'd mixed\_qkv

*required* `a` `Tensor`

\[L, HV] gating input

*required* `b` `Tensor`

\[L, HV] gating input

*required* `A_log` `Tensor`

\[HV] log decay parameter

*required* `dt_bias` `Tensor`

\[HV] dt bias parameter

*required* `num_k_heads` `int`

number of K heads (H)

*required* `head_k_dim` `int`

dimension per K head (K)

*required* `head_v_dim` `int`

dimension per V head (V)

*required* `apply_l2norm` `bool`

whether to L2-normalize q and k

`True` `output_g_exp` `bool`

if True, output exp(g) instead of g (for FlashInfer)

`False`

Returns:

Name Type Description `q` `Tensor`

\[L, H, K] contiguous, optionally l2-normalized

`k` `Tensor`

\[L, H, K] contiguous, optionally l2-normalized

`v` `Tensor`

\[L, HV, V] contiguous

`g` `Tensor`

\[L, HV] float32

`beta` `Tensor`

\[L, HV] float32

Source code in `vllm/model_executor/layers/fla/ops/fused_gdn_prefill_post_conv.py`

```
deffused_post_conv_prep(
    conv_output: torch.Tensor,  # [L, qkv_dim] conv'd mixed_qkv
    a: torch.Tensor,  # [L, HV]
    b: torch.Tensor,  # [L, HV]
    A_log: torch.Tensor,  # [HV]
    dt_bias: torch.Tensor,  # [HV]
    num_k_heads: int,
    head_k_dim: int,
    head_v_dim: int,
    apply_l2norm: bool = True,
    output_g_exp: bool = False,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
"""Fused post-conv1d prep: split + l2norm + gating in one kernel.

    Args:
        conv_output: [L, qkv_dim] contiguous conv'd mixed_qkv
        a: [L, HV] gating input
        b: [L, HV] gating input
        A_log: [HV] log decay parameter
        dt_bias: [HV] dt bias parameter
        num_k_heads: number of K heads (H)
        head_k_dim: dimension per K head (K)
        head_v_dim: dimension per V head (V)
        apply_l2norm: whether to L2-normalize q and k
        output_g_exp: if True, output exp(g) instead of g (for FlashInfer)

    Returns:
        q: [L, H, K] contiguous, optionally l2-normalized
        k: [L, H, K] contiguous, optionally l2-normalized
        v: [L, HV, V] contiguous
        g: [L, HV] float32
        beta: [L, HV] float32
    """
    L = conv_output.shape[0]
    qkv_dim = conv_output.shape[1]
    H = num_k_heads
    K = head_k_dim
    V = head_v_dim
    HV = A_log.shape[0]
    dtype = conv_output.dtype
    device = conv_output.device

    assert qkv_dim == 2 * H * K + HV * V, (
        f"qkv_dim={qkv_dim} != 2*H*K + HV*V = {2*H*K+HV*V}"
    )

    # Allocate outputs in target contiguous layout
    q = torch.empty(L, H, K, dtype=dtype, device=device)
    k = torch.empty(L, H, K, dtype=dtype, device=device)
    v = torch.empty(L, HV, V, dtype=dtype, device=device)
    g = torch.empty(L, HV, dtype=torch.float32, device=device)
    beta = torch.empty(L, HV, dtype=torch.float32, device=device)

    if L == 0:
        return q, k, v, g, beta

    # ---- Kernel config ----
    BK = triton.next_power_of_2(K)
    BV = triton.next_power_of_2(V)
    BLOCK_T = 16  # tokens per block

    # Single kernel: blocks [0,H) do Q/K, blocks [H, H+HV) do V+gating
    grid = (triton.cdiv(L, BLOCK_T), H + HV)
    _fused_post_conv_kernel[grid](
        mixed_qkv_ptr=conv_output,
        a_ptr=a,
        b_ptr=b,
        A_log_ptr=A_log,
        dt_bias_ptr=dt_bias,
        q_ptr=q,
        k_ptr=k,
        v_ptr=v,
        g_ptr=g,
        beta_ptr=beta,
        stride_x_tok=conv_output.stride(0),
        stride_a_tok=a.stride(0),
        stride_b_tok=b.stride(0),
        stride_q_tok=q.stride(0),
        stride_k_tok=k.stride(0),
        stride_v_tok=v.stride(0),
        L=L,
        H=H,
        HV=HV,
        K=K,
        V=V,
        APPLY_L2NORM=apply_l2norm,
        L2NORM_EPS=1e-6,
        OUTPUT_G_EXP=output_g_exp,
        SOFTPLUS_THRESHOLD=20.0,
        BLOCK_T=BLOCK_T,
        BK=BK,
        BV=BV,
        num_warps=4,
        num_stages=2,
    )

    return q, k, v, g, beta
```

## fused\_recurrent\_gated\_delta\_rule [¶](#vllm.model_executor.layers.fla.ops.fused_recurrent_gated_delta_rule "Permanent link")

```
fused_recurrent_gated_delta_rule(
    q: Tensor,
    k: Tensor,
    v: Tensor,
    g: Tensor,
    beta: Tensor = None,
    scale: float = None,
    initial_state: Tensor = None,
    inplace_final_state: bool = True,
    cu_seqlens: Tensor | None = None,
    ssm_state_indices: Tensor | None = None,
    num_accepted_tokens: Tensor | None = None,
    use_qk_l2norm_in_kernel: bool = False,
) -> tuple[Tensor, Tensor]
```

Parameters:

Name Type Description Default `q` `Tensor`

queries of shape `[B, T, H, K]`.

*required* `k` `Tensor`

keys of shape `[B, T, H, K]`.

*required* `v` `Tensor`

values of shape `[B, T, HV, V]`. GVA is applied if `HV > H`.

*required* `g` `Tensor`

g (decays) of shape `[B, T, HV]`.

*required* `beta` `Tensor`

betas of shape `[B, T, HV]`.

`None` `scale` `Optional[int]`

Scale factor for the RetNet attention scores. If not provided, it will default to `1 / sqrt(K)`. Default: `None`.

`None` `initial_state` `Optional[Tensor]`

Initial state of shape `[N, HV, V, K]` for `N` input sequences. For equal-length input sequences, `N` equals the batch size `B`. Default: `None`.

`None` `inplace_final_state` `bool`

bool: Whether to store the final state in-place to save memory. Default: `True`.

`True` `cu_seqlens` `Tensor`

Cumulative sequence lengths of shape `[N+1]` used for variable-length training, consistent with the FlashAttention API.

`None` `ssm_state_indices` `Optional[Tensor]`

Indices to map the input sequences to the initial/final states.

`None` `num_accepted_tokens` `Optional[Tensor]`

Number of accepted tokens for each sequence during decoding.

`None`

Returns:

Name Type Description `o` `Tensor`

Outputs of shape `[B, T, HV, V]`.

`final_state` `Tensor`

Final state of shape `[N, HV, V, K]`.

Examples:: &gt;&gt;&gt; import torch &gt;&gt;&gt; import torch.nn.functional as F &gt;&gt;&gt; from einops import rearrange &gt;&gt;&gt; from fla.ops.gated\_delta\_rule import fused\_recurrent\_gated\_delta\_rule # inputs with equal lengths &gt;&gt;&gt; B, T, H, HV, K, V = 4, 2048, 4, 8, 512, 512 &gt;&gt;&gt; q = torch.randn(B, T, H, K, device='cuda') &gt;&gt;&gt; k = F.normalize(torch.randn(B, T, H, K, device='cuda'), p=2, dim=-1) &gt;&gt;&gt; v = torch.randn(B, T, HV, V, device='cuda') &gt;&gt;&gt; g = F.logsigmoid(torch.rand(B, T, HV, device='cuda')) &gt;&gt;&gt; beta = torch.rand(B, T, HV, device='cuda').sigmoid() &gt;&gt;&gt; h0 = torch.randn(B, HV, V, K, device='cuda') &gt;&gt;&gt; o, ht = fused\_gated\_recurrent\_delta\_rule( q, k, v, g, beta, initial\_state=h0, ) # for variable-length inputs, the batch size `B` is expected to be 1 and `cu_seqlens` is required &gt;&gt;&gt; q, k, v, g, beta = map(lambda x: rearrange(x, 'b t ... -&gt; 1 (b t) ...'), (q, k, v, g, beta)) # for a batch with 4 sequences, `cu_seqlens` with 5 start/end positions are expected &gt;&gt;&gt; cu\_seqlens = q.new\_tensor(\[0, 2048, 4096, 6144, 8192], dtype=torch.int32) &gt;&gt;&gt; o\_var, ht\_var = fused\_gated\_recurrent\_delta\_rule( q, k, v, g, beta, initial\_state=h0, cu\_seqlens=cu\_seqlens )

Source code in `vllm/model_executor/layers/fla/ops/fused_recurrent.py`

```
deffused_recurrent_gated_delta_rule(
    q: torch.Tensor,
    k: torch.Tensor,
    v: torch.Tensor,
    g: torch.Tensor,
    beta: torch.Tensor = None,
    scale: float = None,
    initial_state: torch.Tensor = None,
    inplace_final_state: bool = True,
    cu_seqlens: torch.Tensor | None = None,
    ssm_state_indices: torch.Tensor | None = None,
    num_accepted_tokens: torch.Tensor | None = None,
    use_qk_l2norm_in_kernel: bool = False,
) -> tuple[torch.Tensor, torch.Tensor]:
r"""
    Args:
        q (torch.Tensor):
            queries of shape `[B, T, H, K]`.
        k (torch.Tensor):
            keys of shape `[B, T, H, K]`.
        v (torch.Tensor):
            values of shape `[B, T, HV, V]`.
            GVA is applied if `HV > H`.
        g (torch.Tensor):
            g (decays) of shape `[B, T, HV]`.
        beta (torch.Tensor):
            betas of shape `[B, T, HV]`.
        scale (Optional[int]):
            Scale factor for the RetNet attention scores.
            If not provided, it will default to `1 / sqrt(K)`. Default: `None`.
        initial_state (Optional[torch.Tensor]):
            Initial state of shape `[N, HV, V, K]` for `N` input sequences.
            For equal-length input sequences, `N` equals the batch size `B`.
            Default: `None`.
        inplace_final_state: bool:
            Whether to store the final state in-place to save memory.
            Default: `True`.
        cu_seqlens (torch.Tensor):
            Cumulative sequence lengths of shape `[N+1]` used for variable-length training,
            consistent with the FlashAttention API.
        ssm_state_indices (Optional[torch.Tensor]):
            Indices to map the input sequences to the initial/final states.
        num_accepted_tokens (Optional[torch.Tensor]):
            Number of accepted tokens for each sequence during decoding.

    Returns:
        o (torch.Tensor):
            Outputs of shape `[B, T, HV, V]`.
        final_state (torch.Tensor):
            Final state of shape `[N, HV, V, K]`.

    Examples::
        >>> import torch
        >>> import torch.nn.functional as F
        >>> from einops import rearrange
        >>> from fla.ops.gated_delta_rule import fused_recurrent_gated_delta_rule
        # inputs with equal lengths
        >>> B, T, H, HV, K, V = 4, 2048, 4, 8, 512, 512
        >>> q = torch.randn(B, T, H, K, device='cuda')
        >>> k = F.normalize(torch.randn(B, T, H, K, device='cuda'), p=2, dim=-1)
        >>> v = torch.randn(B, T, HV, V, device='cuda')
        >>> g = F.logsigmoid(torch.rand(B, T, HV, device='cuda'))
        >>> beta = torch.rand(B, T, HV, device='cuda').sigmoid()
        >>> h0 = torch.randn(B, HV, V, K, device='cuda')
        >>> o, ht = fused_gated_recurrent_delta_rule(
            q, k, v, g, beta,
            initial_state=h0,
        )
        # for variable-length inputs, the batch size `B` is expected to be 1 and `cu_seqlens` is required
        >>> q, k, v, g, beta = map(lambda x: rearrange(x, 'b t ... -> 1 (b t) ...'), (q, k, v, g, beta))
        # for a batch with 4 sequences, `cu_seqlens` with 5 start/end positions are expected
        >>> cu_seqlens = q.new_tensor([0, 2048, 4096, 6144, 8192], dtype=torch.int32)
        >>> o_var, ht_var = fused_gated_recurrent_delta_rule(
            q, k, v, g, beta,
            initial_state=h0,
            cu_seqlens=cu_seqlens
        )
    """
    if cu_seqlens is not None and q.shape[0] != 1:
        raise ValueError(
            f"The batch size is expected to be 1 rather than {q.shape[0]} when using `cu_seqlens`."
            f"Please flatten variable-length inputs before processing."
        )
    if scale is None:
        scale = k.shape[-1] ** -0.5
    else:
        assert scale > 0, "scale must be positive"
    if beta is None:
        beta = torch.ones_like(q[..., 0])
    o, final_state = FusedRecurrentFunction.apply(
        q,
        k,
        v,
        g,
        beta,
        scale,
        initial_state,
        inplace_final_state,
        cu_seqlens,
        ssm_state_indices,
        num_accepted_tokens,
        use_qk_l2norm_in_kernel,
    )
    return o, final_state
```

## fused\_sigmoid\_gating\_delta\_rule\_update [¶](#vllm.model_executor.layers.fla.ops.fused_sigmoid_gating_delta_rule_update "Permanent link")

```
fused_sigmoid_gating_delta_rule_update(
    A_log: Tensor,
    a: Tensor,
    b: Tensor,
    dt_bias: Tensor,
    q: Tensor,
    k: Tensor,
    v: Tensor,
    beta: float = 1.0,
    threshold: float = 20.0,
    scale: float = None,
    initial_state: Tensor = None,
    inplace_final_state: bool = True,
    cu_seqlens: Tensor | None = None,
    ssm_state_indices: Tensor | None = None,
    num_accepted_tokens: Tensor | None = None,
    use_qk_l2norm_in_kernel: bool = False,
    is_kda: bool = False,
)
```

Fused triton implementation of sigmoid gating delta rule update. This function uses a single fused kernel that combines both sigmoid gating computation and the recurrent delta rule update for better performance.

Source code in `vllm/model_executor/layers/fla/ops/fused_sigmoid_gating.py`

```
deffused_sigmoid_gating_delta_rule_update(
    A_log: torch.Tensor,
    a: torch.Tensor,
    b: torch.Tensor,
    dt_bias: torch.Tensor,
    q: torch.Tensor,
    k: torch.Tensor,
    v: torch.Tensor,
    beta: float = 1.0,
    threshold: float = 20.0,
    scale: float = None,
    initial_state: torch.Tensor = None,
    inplace_final_state: bool = True,
    cu_seqlens: torch.Tensor | None = None,
    ssm_state_indices: torch.Tensor | None = None,
    num_accepted_tokens: torch.Tensor | None = None,
    use_qk_l2norm_in_kernel: bool = False,
    is_kda: bool = False,
):
"""
    Fused triton implementation of sigmoid gating delta rule update.
    This function uses a single fused kernel that combines both sigmoid gating
    computation and the recurrent delta rule update for better performance.
    """
    B, T, H, K, V = *k.shape, v.shape[-1]
    HV = v.shape[2]
    N = B if cu_seqlens is None else len(cu_seqlens) - 1
    BK, BV = triton.next_power_of_2(K), min(triton.next_power_of_2(V), 32)
    NK, NV = triton.cdiv(K, BK), triton.cdiv(V, BV)
    assert NK == 1, "NK > 1 is not supported yet"
    num_stages = 3
    num_warps = 4

    if cu_seqlens is not None and q.shape[0] != 1:
        raise ValueError(
            f"The batch size is expected to be 1 rather than {q.shape[0]}"
            f" when using `cu_seqlens`. Please flatten variable-length"
            f" inputs before processing."
        )
    if scale is None:
        scale = k.shape[-1] ** -0.5
    else:
        assert scale > 0, "scale must be positive"

    o = q.new_empty(NK, *v.shape)
    if inplace_final_state:
        final_state = initial_state
    else:
        final_state = q.new_empty(T, HV, V, K, dtype=initial_state.dtype)

    stride_init_state_token = initial_state.stride(0)
    stride_final_state_token = final_state.stride(0)

    if ssm_state_indices is None:
        stride_indices_seq, stride_indices_tok = 1, 1
    elif ssm_state_indices.ndim == 1:
        stride_indices_seq, stride_indices_tok = ssm_state_indices.stride(0), 1
    else:
        stride_indices_seq, stride_indices_tok = ssm_state_indices.stride()

    grid = (NK, NV, N * HV)
    fused_sigmoid_gating_delta_rule_update_kernel[grid](
        A_log=A_log,
        a=a.contiguous(),
        b=b.contiguous(),
        dt_bias=dt_bias,
        beta=beta,
        threshold=threshold,
        q=q.contiguous(),
        k=k.contiguous(),
        v=v.contiguous(),
        o=o,
        h0=initial_state,
        ht=final_state,
        cu_seqlens=cu_seqlens,
        ssm_state_indices=ssm_state_indices,
        num_accepted_tokens=num_accepted_tokens,
        scale=scale,
        N=N,
        T=T,
        B=B,
        H=H,
        HV=HV,
        K=K,
        V=V,
        BK=BK,
        BV=BV,
        stride_init_state_token=stride_init_state_token,
        stride_final_state_token=stride_final_state_token,
        stride_indices_seq=stride_indices_seq,
        stride_indices_tok=stride_indices_tok,
        INPLACE_FINAL_STATE=inplace_final_state,
        USE_QK_L2NORM_IN_KERNEL=use_qk_l2norm_in_kernel,
        IS_KDA=is_kda,
        num_warps=num_warps,
        num_stages=num_stages,
    )
    o = o.squeeze(0)
    return o, final_state
```