---
title: layernorm_guard - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fla/ops/layernorm_guard/
source: sitemap
fetched_at: 2026-05-07T21:24:24.71393853-03:00
rendered_js: false
word_count: 189
summary: This document provides the reference documentation for gated LayerNorm and RMSNorm implementations within the vLLM project, which include optional group normalization and activation-based gating.
tags:
    - vllm
    - layer-norm
    - rmsnorm
    - gated-normalization
    - triton-kernel
    - neural-network-layers
category: reference
---

## LayerNormGated [¶](#vllm.model_executor.layers.fla.ops.layernorm_guard.LayerNormGated "Permanent link")

Bases: `Module`

Source code in `vllm/model_executor/layers/fla/ops/layernorm_guard.py`

```
classLayerNormGated(nn.Module):
    def__init__(
        self,
        hidden_size,
        eps: float = 1e-5,
        group_size: int | None = None,
        norm_before_gate: bool = True,
        device: torch.device | None = None,
        dtype: torch.dtype | None = None,
    ):
"""If group_size is not None, we do GroupNorm with each group having group_size elements.
        group_size=None is equivalent to group_size=hidden_size (i.e. there's only 1 group).
        """

        factory_kwargs = {"device": device, "dtype": dtype}
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.empty(hidden_size, **factory_kwargs))
        self.bias = nn.Parameter(torch.empty(hidden_size, **factory_kwargs))
        self.group_size = group_size
        self.norm_before_gate = norm_before_gate
        self.reset_parameters()

    defreset_parameters(self):
        torch.nn.init.ones_(self.weight)
        torch.nn.init.zeros_(self.bias)

    defforward(self, x, z=None):
"""If z is not None, we do norm(x) * silu(z) if norm_before_gate, else norm(x * silu(z))"""
        return layernorm_fn(
            x,
            self.weight,
            self.bias,
            z=z,
            group_size=self.group_size,
            eps=self.eps,
            norm_before_gate=self.norm_before_gate,
        )
```

### \_\_init\__ [¶](#vllm.model_executor.layers.fla.ops.layernorm_guard.LayerNormGated.__init__ "Permanent link")

```
__init__(
    hidden_size,
    eps: float = 1e-05,
    group_size: int | None = None,
    norm_before_gate: bool = True,
    device: device | None = None,
    dtype: dtype | None = None,
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
    norm_before_gate: bool = True,
    device: torch.device | None = None,
    dtype: torch.dtype | None = None,
):
"""If group_size is not None, we do GroupNorm with each group having group_size elements.
    group_size=None is equivalent to group_size=hidden_size (i.e. there's only 1 group).
    """

    factory_kwargs = {"device": device, "dtype": dtype}
    super().__init__()
    self.eps = eps
    self.weight = nn.Parameter(torch.empty(hidden_size, **factory_kwargs))
    self.bias = nn.Parameter(torch.empty(hidden_size, **factory_kwargs))
    self.group_size = group_size
    self.norm_before_gate = norm_before_gate
    self.reset_parameters()
```

### forward [¶](#vllm.model_executor.layers.fla.ops.layernorm_guard.LayerNormGated.forward "Permanent link")

If z is not None, we do norm(x) * silu(z) if norm\_before\_gate, else norm(x * silu(z))

Source code in `vllm/model_executor/layers/fla/ops/layernorm_guard.py`

```
defforward(self, x, z=None):
"""If z is not None, we do norm(x) * silu(z) if norm_before_gate, else norm(x * silu(z))"""
    return layernorm_fn(
        x,
        self.weight,
        self.bias,
        z=z,
        group_size=self.group_size,
        eps=self.eps,
        norm_before_gate=self.norm_before_gate,
    )
```

## RMSNormGated [¶](#vllm.model_executor.layers.fla.ops.layernorm_guard.RMSNormGated "Permanent link")

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

### \_\_init\__ [¶](#vllm.model_executor.layers.fla.ops.layernorm_guard.RMSNormGated.__init__ "Permanent link")

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

### forward [¶](#vllm.model_executor.layers.fla.ops.layernorm_guard.RMSNormGated.forward "Permanent link")

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

## \_layer\_norm\_fn\_impl [¶](#vllm.model_executor.layers.fla.ops.layernorm_guard._layer_norm_fn_impl "Permanent link")

```
_layer_norm_fn_impl(
    x,
    weight,
    bias,
    z=None,
    eps=1e-06,
    group_size=None,
    norm_before_gate=True,
    is_rms_norm=False,
    activation: str = "swish",
)
```

Triton layer/RMS norm with optional gating.

If z is not None, computes norm(x) * silu(z) when norm\_before\_gate, else norm(x * silu(z)).

This calls the triton kernel directly. The original code wrapped this in a torch.autograd.Function (LayerNormFn) to save tensors for a backward pass, but vLLM is inference-only so there is no backward pass. The autograd wrapper also prevented torch.compile/dynamo from tracing through the function due to its @staticmethod forward.

Source code in `vllm/model_executor/layers/fla/ops/layernorm_guard.py`

```
def_layer_norm_fn_impl(
    x,
    weight,
    bias,
    z=None,
    eps=1e-6,
    group_size=None,
    norm_before_gate=True,
    is_rms_norm=False,
    activation: str = "swish",
):
"""Triton layer/RMS norm with optional gating.

    If z is not None, computes norm(x) * silu(z) when norm_before_gate,
    else norm(x * silu(z)).

    This calls the triton kernel directly. The original code wrapped this
    in a torch.autograd.Function (LayerNormFn) to save tensors for a
    backward pass, but vLLM is inference-only so there is no backward pass.
    The autograd wrapper also prevented torch.compile/dynamo from tracing
    through the function due to its @staticmethod forward.
    """
    x_shape_og = x.shape
    x = x.reshape(-1, x.shape[-1])
    if x.stride(-1) != 1:
        x = x.contiguous()
    if z is not None:
        assert z.shape == x_shape_og
        z = z.reshape(-1, z.shape[-1])
        if z.stride(-1) != 1:
            z = z.contiguous()
    weight = weight.contiguous()
    if bias is not None:
        bias = bias.contiguous()
    y, _, _ = layer_norm_fwd(
        x,
        weight,
        bias,
        eps,
        z=z,
        group_size=group_size,
        norm_before_gate=norm_before_gate,
        is_rms_norm=is_rms_norm,
        activation=activation,
    )
    return y.reshape(x_shape_og)
```