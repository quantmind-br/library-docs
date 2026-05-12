---
title: qwen - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/qwen/
source: sitemap
fetched_at: 2026-05-07T21:32:46.876844745-03:00
rendered_js: false
word_count: 36
summary: This document provides the technical reference and implementation details for the QWen model architecture, specifically focusing on the Multi-Layer Perceptron (MLP) component within the vLLM executor framework.
tags:
    - vllm
    - qwen-model
    - mlp-architecture
    - model-inference
    - neural-network-layers
category: reference
---

## vllm.model\_executor.models.qwen [¶](#vllm.model_executor.models.qwen "Permanent link")

Inference-only QWen model compatible with HuggingFace weights.

## QWenMLP [¶](#vllm.model_executor.models.qwen.QWenMLP "Permanent link")

Bases: `Module`

MLP for the language component of the Qwen model, which contains a MergedColumnParallelLinear merging 2 outputs via silu activation.

Source code in `vllm/model_executor/models/qwen.py`

```
classQWenMLP(nn.Module):
"""MLP for the language component of the Qwen model, which contains a
    MergedColumnParallelLinear merging 2 outputs via silu activation."""

    def__init__(
        self,
        hidden_size: int,
        intermediate_size: int,
        hidden_act: str = "silu",
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ):
        super().__init__()
        self.gate_up_proj = MergedColumnParallelLinear(
            hidden_size,
            [intermediate_size] * 2,
            bias=False,
            quant_config=quant_config,
            prefix=f"{prefix}.gate_up_proj",
        )
        self.c_proj = RowParallelLinear(
            intermediate_size,
            hidden_size,
            bias=False,
            quant_config=quant_config,
            prefix=f"{prefix}.c_proj",
        )
        if hidden_act != "silu":
            raise ValueError(
                f"Unsupported activation: {hidden_act}. Only silu is supported for now."
            )
        self.act_fn = SiluAndMul()

    defforward(self, x: torch.Tensor) -> torch.Tensor:
        gate_up, _ = self.gate_up_proj(x)
        x = self.act_fn(gate_up)
        x, _ = self.c_proj(x)
        return x
```