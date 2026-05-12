---
title: layernorm - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/layernorm/
source: sitemap
fetched_at: 2026-05-07T21:25:47.175427557-03:00
rendered_js: false
word_count: 291
summary: This document provides the implementation details for custom layer normalization components, including GemmaRMSNorm, LayerNorm, and RMSNorm, within the vLLM model execution framework.
tags:
    - normalization
    - layernorm
    - rmsnorm
    - vllm
    - deep-learning
    - pytorch
    - neural-networks
category: reference
---

Custom normalization layers.

## GemmaRMSNorm [¶](#vllm.model_executor.layers.layernorm.GemmaRMSNorm "Permanent link")

Bases: `CustomOp`

RMS normalization for Gemma.

Two differences from the above RMSNorm

1. x * (1 + w) instead of x * w.
2. (x * w).to(orig\_dtype) instead of x.to(orig\_dtype) * w.

Source code in `vllm/model_executor/layers/layernorm.py`

```
@CustomOp.register("gemma_rms_norm")
classGemmaRMSNorm(CustomOp):
"""RMS normalization for Gemma.

    Two differences from the above RMSNorm:
        1. x * (1 + w) instead of x * w.
        2. (x * w).to(orig_dtype) instead of x.to(orig_dtype) * w.
    """

    # --8<-- [end:gemma_rms_norm]

    def__init__(
        self,
        hidden_size: int,
        eps: float = 1e-6,
    ) -> None:
        super().__init__()
        self.weight = nn.Parameter(torch.zeros(hidden_size))
        self.variance_epsilon = eps

    defforward_native(
        self,
        x: torch.Tensor,
        residual: torch.Tensor | None = None,
    ) -> torch.Tensor | tuple[torch.Tensor, torch.Tensor]:
"""PyTorch-native implementation equivalent to forward()."""
        orig_dtype = x.dtype
        weight = self.weight.data.float() + 1.0
        if residual is not None:
            x = (
                x.float() + residual.float()
                if orig_dtype == torch.float16
                else x + residual
            )
            residual = x
        # ir.ops.rms_norm handles fp32 upcast internally
        out = ir.ops.rms_norm(x, weight, self.variance_epsilon)
        return (
            out.to(orig_dtype) if residual is None else (out.to(orig_dtype), residual)
        )

    defforward_cuda(
        self,
        x: torch.Tensor,
        residual: torch.Tensor | None = None,
    ) -> torch.Tensor | tuple[torch.Tensor, torch.Tensor]:
        return self.forward_native(x, residual)
```

### forward\_native [¶](#vllm.model_executor.layers.layernorm.GemmaRMSNorm.forward_native "Permanent link")

PyTorch-native implementation equivalent to forward().

Source code in `vllm/model_executor/layers/layernorm.py`

```
defforward_native(
    self,
    x: torch.Tensor,
    residual: torch.Tensor | None = None,
) -> torch.Tensor | tuple[torch.Tensor, torch.Tensor]:
"""PyTorch-native implementation equivalent to forward()."""
    orig_dtype = x.dtype
    weight = self.weight.data.float() + 1.0
    if residual is not None:
        x = (
            x.float() + residual.float()
            if orig_dtype == torch.float16
            else x + residual
        )
        residual = x
    # ir.ops.rms_norm handles fp32 upcast internally
    out = ir.ops.rms_norm(x, weight, self.variance_epsilon)
    return (
        out.to(orig_dtype) if residual is None else (out.to(orig_dtype), residual)
    )
```

Bases: `Module`

Layer Normalization.

Source code in `vllm/model_executor/layers/layernorm.py`

```
classLayerNorm(nn.Module):
"""
    Layer Normalization.
    """

    def__init__(self, dim: int, eps: float = 1e-6):
        super().__init__()
        self.dim = dim
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(dim, dtype=torch.float32))
        self.bias = nn.Parameter(torch.zeros(dim, dtype=torch.float32))

    defforward(self, x: torch.Tensor):
        return F.layer_norm(
            x.float(), (self.dim,), self.weight, self.bias, self.eps
        ).type_as(x)
```

## RMSNorm [¶](#vllm.model_executor.layers.layernorm.RMSNorm "Permanent link")

Bases: `CustomOp`

Root mean square normalization.

Computes x -&gt; w * x / sqrt(E\[x^2] + eps) where w is the learned weight. Refer to https://arxiv.org/abs/1910.07467

Source code in `vllm/model_executor/layers/layernorm.py`

```
@CustomOp.register("rms_norm")
classRMSNorm(CustomOp):
"""Root mean square normalization.

    Computes x -> w * x / sqrt(E[x^2] + eps) where w is the learned weight.
    Refer to https://arxiv.org/abs/1910.07467
    """

    # --8<-- [end:rms_norm]

    def__init__(
        self,
        hidden_size: int,
        eps: float = 1e-6,
        var_hidden_size: int | None = None,
        has_weight: bool = True,
        dtype: torch.dtype | None = None,
    ) -> None:
        super().__init__()

        self.hidden_size = hidden_size
        self.variance_epsilon = eps
        self.variance_size_override = (
            None if var_hidden_size == hidden_size else var_hidden_size
        )
        weight_dtype = dtype or torch.get_default_dtype()
        self.has_weight = has_weight
        self.weight = torch.ones(hidden_size, dtype=weight_dtype)
        if self.has_weight:
            self.weight = nn.Parameter(self.weight)

        # Do not pass identity weight to native implementation (causes issue on TPU).
        # Other implementations require weight to be passed even if all ones.
        # Cheat and predict if native will be dispatched to:
        #  1) if native is first in priority list
        #  2) if variance_size_override is given (only supported by native impl)
        # TODO(luka): address weight passing inconsistency:
        # https://github.com/vllm-project/vllm/issues/39370
        priority = get_current_vllm_config().kernel_config.ir_op_priority
        var_override = self.variance_size_override is not None
        native_rms_norm = priority.rms_norm[0] == "native" or var_override
        native_add_rms_norm = priority.fused_add_rms_norm[0] == "native" or var_override
        self.pass_weight = self.has_weight or not native_rms_norm
        self.pass_weight_add = self.has_weight or not native_add_rms_norm

    defforward_native(
        self,
        x: torch.Tensor,
        residual: torch.Tensor | None = None,
    ) -> torch.Tensor | tuple[torch.Tensor, torch.Tensor]:
"""PyTorch-native implementation equivalent to forward()."""
        if residual is None:
            return ir.ops.rms_norm(
                x,
                self.weight.data if self.pass_weight else None,
                self.variance_epsilon,
                self.variance_size_override,
            )
        else:
            return ir.ops.fused_add_rms_norm.maybe_inplace(
                x,
                residual,
                self.weight.data if self.pass_weight_add else None,
                self.variance_epsilon,
                self.variance_size_override,
            )

    defforward_cuda(
        self,
        x: torch.Tensor,
        residual: torch.Tensor | None = None,
    ) -> torch.Tensor | tuple[torch.Tensor, torch.Tensor]:
        if (
            envs.VLLM_BATCH_INVARIANT
            and residual is None
            and self.variance_size_override is None
        ):
            return rms_norm_batch_invariant(x, self.weight.data, self.variance_epsilon)

        return self.forward_native(x, residual)

    defforward_xpu(
        self,
        x: torch.Tensor,
        residual: torch.Tensor | None = None,
    ) -> torch.Tensor | tuple[torch.Tensor, torch.Tensor]:
        return self.forward_cuda(x, residual)

    defextra_repr(self) -> str:
        s = f"hidden_size={self.weight.data.size(0)}"
        s += f", eps={self.variance_epsilon}"
        return s
```

### forward\_native [¶](#vllm.model_executor.layers.layernorm.RMSNorm.forward_native "Permanent link")

PyTorch-native implementation equivalent to forward().

Source code in `vllm/model_executor/layers/layernorm.py`

```
defforward_native(
    self,
    x: torch.Tensor,
    residual: torch.Tensor | None = None,
) -> torch.Tensor | tuple[torch.Tensor, torch.Tensor]:
"""PyTorch-native implementation equivalent to forward()."""
    if residual is None:
        return ir.ops.rms_norm(
            x,
            self.weight.data if self.pass_weight else None,
            self.variance_epsilon,
            self.variance_size_override,
        )
    else:
        return ir.ops.fused_add_rms_norm.maybe_inplace(
            x,
            residual,
            self.weight.data if self.pass_weight_add else None,
            self.variance_epsilon,
            self.variance_size_override,
        )
```

## RMSNormGated [¶](#vllm.model_executor.layers.layernorm.RMSNormGated "Permanent link")

Bases: `CustomOp`

RMS Normalization with optional gating.

This is a native PyTorch implementation that supports: - Standard RMS normalization - Group RMS normalization - Optional gating with SiLU activation

Source code in `vllm/model_executor/layers/layernorm.py`

```
@CustomOp.register("rms_norm_gated")
classRMSNormGated(CustomOp):
"""RMS Normalization with optional gating.

    This is a native PyTorch implementation that supports:
    - Standard RMS normalization
    - Group RMS normalization
    - Optional gating with SiLU activation
    """

    # --8<-- [end:rms_norm_gated]

    def__init__(
        self,
        hidden_size: int,
        eps: float = 1e-5,
        group_size: int | None = None,
        norm_before_gate: bool = False,
        device: torch.device | None = None,
        dtype: torch.dtype | None = None,
        activation: str = "swish",
    ):
"""Initialize RMSNormGated.

        Args:
            hidden_size: Size of the hidden dimension
            eps: Epsilon for numerical stability
            group_size: If not None, do GroupNorm with each group
                        having group_size elements.
                        group_size=None is equivalent to group_size=hidden_size
                        (i.e. there's only 1 group).
            norm_before_gate: If True and z is provided: out = norm(x) * silu(z)
                              If False and z is provided: out = norm(x * silu(z))
            device: Device to create parameters on
            dtype: Data type for parameters
            activation: Activation function name for gating
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

    defforward_native(
        self, x: torch.Tensor, z: torch.Tensor | None = None
    ) -> torch.Tensor:
"""
        Native PyTorch implementation of RMS normalization with gating.

        Args:
            x: Input tensor
            z: Optional gating tensor

        Returns:
            Normalized (and optionally gated) tensor

        If z is not None:
            - norm_before_gate=True: out = norm(x) * silu(z)
            - norm_before_gate=False: out = norm(x * silu(z))
        """
        orig_dtype = x.dtype
        x = x.float()
        weight = self.weight.float()
        z = z.float() if z is not None else None

        assert self.activation in ["silu", "sigmoid", "swish"]
        act_fn = F.sigmoid if self.activation == "sigmoid" else F.silu

        # Apply gating before normalization if needed
        if z is not None and not self.norm_before_gate:
            x = x * act_fn(z)

        # RMS Normalization
        if self.group_size is None:
            # Standard RMS norm across the last dimension
            variance = x.pow(2).mean(dim=-1, keepdim=True)
            x_normed = x * torch.rsqrt(variance + self.eps)
            out = x_normed * weight
        else:
            # Group RMS norm
            fromeinopsimport rearrange

            x_group = rearrange(x, "... (g d) -> ... g d", d=self.group_size)
            variance = x_group.pow(2).mean(dim=-1, keepdim=True)
            x_normed = x_group * torch.rsqrt(variance + self.eps)
            out = rearrange(x_normed, "... g d -> ... (g d)") * weight

        # Apply gating after normalization if needed
        if z is not None and self.norm_before_gate:
            out = out * act_fn(z)

        return out.to(orig_dtype)

    defforward_cuda(
        self, x: torch.Tensor, z: torch.Tensor | None = None
    ) -> torch.Tensor:
        fromvllm.model_executor.layers.fla.ops.layernorm_guardimport rmsnorm_fn

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

    defforward_xpu(
        self, x: torch.Tensor, z: torch.Tensor | None = None
    ) -> torch.Tensor:
        return self.forward_cuda(x, z)
```

### \_\_init\__ [¶](#vllm.model_executor.layers.layernorm.RMSNormGated.__init__ "Permanent link")

```
__init__(
    hidden_size: int,
    eps: float = 1e-05,
    group_size: int | None = None,
    norm_before_gate: bool = False,
    device: device | None = None,
    dtype: dtype | None = None,
    activation: str = "swish",
)
```

Initialize RMSNormGated.

Parameters:

Name Type Description Default `hidden_size` `int`

Size of the hidden dimension

*required* `eps` `float`

Epsilon for numerical stability

`1e-05` `group_size` `int | None`

If not None, do GroupNorm with each group having group\_size elements. group\_size=None is equivalent to group\_size=hidden\_size (i.e. there's only 1 group).

`None` `norm_before_gate` `bool`

If True and z is provided: out = norm(x) * silu(z) If False and z is provided: out = norm(x * silu(z))

`False` `device` `device | None`

Device to create parameters on

`None` `dtype` `dtype | None`

Data type for parameters

`None` `activation` `str`

Activation function name for gating

`'swish'`

Source code in `vllm/model_executor/layers/layernorm.py`

```
def__init__(
    self,
    hidden_size: int,
    eps: float = 1e-5,
    group_size: int | None = None,
    norm_before_gate: bool = False,
    device: torch.device | None = None,
    dtype: torch.dtype | None = None,
    activation: str = "swish",
):
"""Initialize RMSNormGated.

    Args:
        hidden_size: Size of the hidden dimension
        eps: Epsilon for numerical stability
        group_size: If not None, do GroupNorm with each group
                    having group_size elements.
                    group_size=None is equivalent to group_size=hidden_size
                    (i.e. there's only 1 group).
        norm_before_gate: If True and z is provided: out = norm(x) * silu(z)
                          If False and z is provided: out = norm(x * silu(z))
        device: Device to create parameters on
        dtype: Data type for parameters
        activation: Activation function name for gating
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

### forward\_native [¶](#vllm.model_executor.layers.layernorm.RMSNormGated.forward_native "Permanent link")

Native PyTorch implementation of RMS normalization with gating.

Parameters:

Name Type Description Default `x` `Tensor`

Input tensor

*required* `z` `Tensor | None`

Optional gating tensor

`None`

Returns:

Type Description `Tensor`

Normalized (and optionally gated) tensor

If z is not None

- norm\_before\_gate=True: out = norm(x) * silu(z)
- norm\_before\_gate=False: out = norm(x * silu(z))

Source code in `vllm/model_executor/layers/layernorm.py`

```
defforward_native(
    self, x: torch.Tensor, z: torch.Tensor | None = None
) -> torch.Tensor:
"""
    Native PyTorch implementation of RMS normalization with gating.

    Args:
        x: Input tensor
        z: Optional gating tensor

    Returns:
        Normalized (and optionally gated) tensor

    If z is not None:
        - norm_before_gate=True: out = norm(x) * silu(z)
        - norm_before_gate=False: out = norm(x * silu(z))
    """
    orig_dtype = x.dtype
    x = x.float()
    weight = self.weight.float()
    z = z.float() if z is not None else None

    assert self.activation in ["silu", "sigmoid", "swish"]
    act_fn = F.sigmoid if self.activation == "sigmoid" else F.silu

    # Apply gating before normalization if needed
    if z is not None and not self.norm_before_gate:
        x = x * act_fn(z)

    # RMS Normalization
    if self.group_size is None:
        # Standard RMS norm across the last dimension
        variance = x.pow(2).mean(dim=-1, keepdim=True)
        x_normed = x * torch.rsqrt(variance + self.eps)
        out = x_normed * weight
    else:
        # Group RMS norm
        fromeinopsimport rearrange

        x_group = rearrange(x, "... (g d) -> ... g d", d=self.group_size)
        variance = x_group.pow(2).mean(dim=-1, keepdim=True)
        x_normed = x_group * torch.rsqrt(variance + self.eps)
        out = rearrange(x_normed, "... g d -> ... (g d)") * weight

    # Apply gating after normalization if needed
    if z is not None and self.norm_before_gate:
        out = out * act_fn(z)

    return out.to(orig_dtype)
```