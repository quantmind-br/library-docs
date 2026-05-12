---
title: activation - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/activation/
source: sitemap
fetched_at: 2026-05-07T21:24:30.28646441-03:00
rendered_js: false
word_count: 162
summary: This document defines the MoEActivation enum and utility functions used to manage and apply various activation functions, including gated and non-gated variants, within Mixture-of-Experts (MoE) layers.
tags:
    - moe
    - activation-functions
    - vllm
    - deep-learning
    - neural-networks
    - gated-linear-unit
category: api
---

MoE activation function enum and utilities.

## MoEActivation [¶](#vllm.model_executor.layers.fused_moe.activation.MoEActivation "Permanent link")

Bases: `Enum`

Activation functions for MoE layers.

Source code in `vllm/model_executor/layers/fused_moe/activation.py`

```
classMoEActivation(Enum):
"""Activation functions for MoE layers."""

    # Gated activations (gate * activation(up)) expect input of shape [..., 2*d]
    # and produce output of shape [..., d]
    SILU = "silu"
    GELU = "gelu"
    GELU_TANH = "gelu_tanh"
    RELU2 = "relu2"
    SWIGLUOAI = "swigluoai"
    SWIGLUSTEP = "swiglustep"

    # Non-gated activations (no mul with gate) expect input of shape [..., d]
    # and produce output of shape [..., d].
    # NOTE: Non-gated activations require the "_no_mul" suffix to be present.
    SILU_NO_MUL = "silu_no_mul"
    GELU_NO_MUL = "gelu_no_mul"
    GELU_TANH_NO_MUL = "gelu_tanh_no_mul"
    RELU2_NO_MUL = "relu2_no_mul"

    @property
    defis_gated(self) -> bool:
"""Returns True if activation expects gate*activation(up) pattern.

        Gated activations expect input tensor with 2x the output size,
        where the first half is the gate and second half is the up projection.
        """
        return not self.value.endswith("_no_mul")

    @property
    defcustom_op_name(self) -> str:
"""Maps to the CustomOp name of activations
        in vllm/model_executor/layers/activation.py."""
        return _CUSTOM_OP_NAMES[self]

    defwithout_mul(self) -> "MoEActivation":
"""Get the non-gated variant of this activation.

        For activations that have a _no_mul variant, returns that variant.
        For activations without a _no_mul variant (or already _no_mul),
        returns self.
        """
        return _WITHOUT_MUL.get(self, self)

    @classmethod
    deffrom_str(cls, s: str) -> "MoEActivation":
"""Parse from string for backward compatibility."""
        s = _STR_ALIASES.get(s, s)
        for member in cls:
            if member.value == s:
                return member
        valid = [m.value for m in cls]
        raise ValueError(f"Unknown MoE activation: {s!r}. Valid activations: {valid}")
```

### custom\_op\_name `property` [¶](#vllm.model_executor.layers.fused_moe.activation.MoEActivation.custom_op_name "Permanent link")

Maps to the CustomOp name of activations in vllm/model\_executor/layers/activation.py.

### is\_gated `property` [¶](#vllm.model_executor.layers.fused_moe.activation.MoEActivation.is_gated "Permanent link")

Returns True if activation expects gate\*activation(up) pattern.

Gated activations expect input tensor with 2x the output size, where the first half is the gate and second half is the up projection.

### from\_str `classmethod` [¶](#vllm.model_executor.layers.fused_moe.activation.MoEActivation.from_str "Permanent link")

Parse from string for backward compatibility.

Source code in `vllm/model_executor/layers/fused_moe/activation.py`

```
@classmethod
deffrom_str(cls, s: str) -> "MoEActivation":
"""Parse from string for backward compatibility."""
    s = _STR_ALIASES.get(s, s)
    for member in cls:
        if member.value == s:
            return member
    valid = [m.value for m in cls]
    raise ValueError(f"Unknown MoE activation: {s!r}. Valid activations: {valid}")
```

### without\_mul [¶](#vllm.model_executor.layers.fused_moe.activation.MoEActivation.without_mul "Permanent link")

```
without_mul() -> MoEActivation
```

Get the non-gated variant of this activation.

For activations that have a \_no\_mul variant, returns that variant. For activations without a \_no\_mul variant (or already \_no\_mul), returns self.

Source code in `vllm/model_executor/layers/fused_moe/activation.py`

```
defwithout_mul(self) -> "MoEActivation":
"""Get the non-gated variant of this activation.

    For activations that have a _no_mul variant, returns that variant.
    For activations without a _no_mul variant (or already _no_mul),
    returns self.
    """
    return _WITHOUT_MUL.get(self, self)
```

## activation\_without\_mul [¶](#vllm.model_executor.layers.fused_moe.activation.activation_without_mul "Permanent link")

```
activation_without_mul(activation: str) -> str
```

Get the non-gated variant of an activation function.

Parameters:

Name Type Description Default `activation` `str`

The activation function name (e.g., "silu", "gelu")

*required*

Returns:

Type Description `str`

The non-gated activation name (e.g., "silu\_no\_mul", "gelu\_no\_mul")

Source code in `vllm/model_executor/layers/fused_moe/activation.py`

```
defactivation_without_mul(activation: str) -> str:
"""Get the non-gated variant of an activation function.

    Args:
        activation: The activation function name (e.g., "silu", "gelu")

    Returns:
        The non-gated activation name (e.g., "silu_no_mul", "gelu_no_mul")
    """
    return MoEActivation.from_str(activation).without_mul().value
```

## apply\_moe\_activation [¶](#vllm.model_executor.layers.fused_moe.activation.apply_moe_activation "Permanent link")

Apply MoE activation function.

Source code in `vllm/model_executor/layers/fused_moe/activation.py`

```
defapply_moe_activation(
    activation: MoEActivation,
    output: torch.Tensor,
    input: torch.Tensor,
) -> torch.Tensor:
"""Apply MoE activation function."""
    assert input.dim() == 2, "Input must be 2D"
    assert output.dim() == 2, "Output must be 2D"
    if activation.is_gated:
        assert output.size(-1) * 2 == input.size(-1), (
            f"{activation.value} expects 2x ratio: "
            f"{output.size(-1)*2} vs {input.size(-1)}"
        )
    else:
        assert output.size(-1) == input.size(-1), (
            f"{activation.value} expects equal sizes: "
            f"{output.size(-1)} vs {input.size(-1)}"
        )

    # Activations with gated multiplication (gate × activation(up))
    if activation == MoEActivation.SILU:
        torch.ops._C.silu_and_mul(output, input)
    elif activation == MoEActivation.GELU:
        torch.ops._C.gelu_and_mul(output, input)
    elif activation == MoEActivation.GELU_TANH:
        torch.ops._C.gelu_tanh_and_mul(output, input)
    elif activation == MoEActivation.SWIGLUOAI:
        torch.ops._C.swigluoai_and_mul(output, input)
    elif activation == MoEActivation.SWIGLUSTEP:
        fromvllm.model_executor.layers.activationimport swiglustep_and_mul_triton

        swiglustep_and_mul_triton(output, input)

    # Activations without gated multiplication
    elif activation == MoEActivation.SILU_NO_MUL:
        output.copy_(F.silu(input))
    elif activation == MoEActivation.GELU_NO_MUL:
        output.copy_(F.gelu(input))
    elif activation == MoEActivation.GELU_TANH_NO_MUL:
        output.copy_(F.gelu(input, approximate="tanh"))
    elif activation == MoEActivation.RELU2_NO_MUL:
        F.relu(input, inplace=True)
        torch.square(input, out=output)
    else:
        raise ValueError(f"Unsupported FusedMoe activation: {activation}")

    return output
```