---
title: CustomOp - vLLM
url: https://docs.vllm.ai/en/latest/design/custom_op/
source: sitemap
fetched_at: 2026-05-07T21:12:12.772672197-03:00
rendered_js: false
word_count: 975
summary: This document explains the CustomOp system in vLLM, which provides an abstraction for dispatching operations to platform-specific backends and includes instructions for registering operations and configuring their execution.
tags:
    - vllm
    - custom-op
    - backend-dispatch
    - performance-optimization
    - extensibility
    - torch-compile
category: concept
---

[](https://github.com/vllm-project/vllm/edit/main/docs/design/custom_op.md "Edit this page")

[`CustomOp`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp "            CustomOp") is an abstract class used for dispatching the forward method of various operations to the appropriate backend. It also offers a mechanism for both vLLM and OOT (Out-Of-Tree) plugins to register their custom operations.

This document will introduce how CustomOp works in vLLM and how to implement a new [`CustomOp`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp "            CustomOp").

## How CustomOp Works in vLLM[¶](#how-customop-works-in-vllm "Permanent link")

[`CustomOp`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp "            CustomOp") manages two dictionaries of all custom ops (i.e., op classes, indexed by registered name) in its class, for vLLM and OOT plugins respectively.

We can use `@CustomOp.register("op_name")` to register an op class to the [`CustomOp`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp "            CustomOp") system. After this, the `op_name` and its class will be added into the `op_registry` dictionary. In addition, We can also register an OOT op by `@CustomOp.register_oot("op_name")`. We will introduce this mechanism in detail later.

When a [`CustomOp`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp "            CustomOp") is called (i.e., call its `forward()` method), if it is enabled (i.e., with `--compilation_config.custom_ops '["+op_name"]'`), it will automatically dispatch the forward method to the appropriate backend according to `current_platform`. Otherwise (i.e., it is disabled), it will only call the `forward_native()` method to use PyTorch-native implementation of this forward method.

- **CPU platform:** dispatch to `forward_cpu()`.
- **CUDA platform:** dispatch to `forward_cuda()`.
- **ROCm platform:** dispatch to `forward_hip()`. If `forward_hip()` is not implemented, it will use `forward_cuda()` as a fallback.
- **XPU platform:** dispatch to `forward_xpu()`.
- **TPU platform:** dispatch to `forward_tpu()`.
- **OOT platform:** dispatch to `forward_oot()`. This will only be called on OOT platforms.
- **Default:** dispatch to `forward_native()` as a final fallback for all platforms.

Note

Note that the dispatching logic might not be absolute because of class inheritance. Derived class might override the behavior.

Furthermore, vLLM decides whether to enable or disable a [`CustomOp`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp "            CustomOp") based on `compilation_config.custom_ops`. To be specific, if a [`CustomOp`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp "            CustomOp") is not registered in `compilation_config.custom_ops` (i.e., uses the default config), it will be enabled if `compilation_config.custom_ops` contains `all`, or will be disabled if it contains `none`.

Note

Note that `all` and `none` cannot coexist in `compilation_config.custom_ops`.

By default, if `compilation_config.backend == "inductor"` and `compilation_config.mode != CompilationMode.NONE`, a `none` will be appended into `compilation_config.custom_ops`, otherwise a `all` will be appended. In other words, this means [`CustomOp`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp "            CustomOp") will be disabled in some platforms (i.e., those use `inductor` as default backend for `torch.compile`) when running with torch compile mode. In this case, Inductor generates (fused) Triton kernels for those disabled custom ops.

Note

For multi-modal models, vLLM has enforced the enabling of some custom ops to use device-specific deep-optimized kernels for better performance in ViT part, such as [`MMEncoderAttention`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/attention/mm_encoder_attention/#vllm.model_executor.layers.attention.mm_encoder_attention.MMEncoderAttention "            MMEncoderAttention") and `ApplyRotaryEmb`. We can also pass a `enforce_enable=True` param to the `__init__()` method of the [`CustomOp`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp "            CustomOp") to enforce enable itself at object-level.

Note that this `enforce_enable` mechanism will be removed after we add a separate `compilation_config` for multi-modal part.

## How to Customise Your Configuration for CustomOp[¶](#how-to-customise-your-configuration-for-customop "Permanent link")

vLLM also offers fine-grained control over which custom ops to enable or disable for users, by manually passing a `--compilation_config.custom_ops '["..."]'` when launching a server.

For example:

- Use `--compilation_config.custom_ops '["all"]'` to enable all custom ops.
- Use `--compilation_config.custom_ops '["none"]'` to disable all custom ops.
- Use `--compilation_config.custom_ops '["all,-op1"]'` to enable all custom ops except op1 (i.e., prefixed with a `-` means "disable").
- Use `--compilation_config.custom_ops '["none,+op1,+op2"]'` to only enable op1 and op2 (i.e., prefixed with a `+` means "enable").

## Types of Supported CustomOp in vLLM[¶](#types-of-supported-customop-in-vllm "Permanent link")

**1. Attention:**

```
@PluggableLayer.register("multi_head_latent_attention")
classMultiHeadLatentAttentionWrapper(PluggableLayer):
"""Pluggable MLA layer which allows OOT backends to add
    custom implementations of the outer MLA layer (including rope & o_proj).
    Note that currently oot platforms can still use CustomOp.register_oot to
    replace MLA layer entirely, although we use PluggableLayer to register
    this layer now.

    This class takes positions and hidden_states as input.
    The input tensors can either contain prefill tokens or decode tokens.
    The class does the following:

    1. MLA Preprocess.
    2. Perform multi-head attention to prefill tokens and
       multi-query attention to decode tokens separately.
    3. Return the output tensor.
    """
```

**2. Activation:**

```
@CustomOp.register("silu_and_mul")
classSiluAndMul(CustomOp):
"""An activation function for SwiGLU.

    The function computes x -> silu(x[:d]) * x[d:] where d = x.shape[-1] // 2.

    Shapes:
        x: (num_tokens, 2 * d) or (batch_size, seq_len, 2 * d)
        return: (num_tokens, d) or (batch_size, seq_len, d)
    """


@CustomOp.register("mul_and_silu")
classMulAndSilu(CustomOp):
"""An activation function for SwiGLU.

    The function computes x -> x[:d] * silu(x[d:]) where d = x.shape[-1] // 2.

    Shapes:
        x: (num_tokens, 2 * d) or (batch_size, seq_len, 2 * d)
        return: (num_tokens, d) or (batch_size, seq_len, d)
    """


@CustomOp.register("gelu_new")
classNewGELU(CustomOp):

@CustomOp.register("gelu_fast")
classFastGELU(CustomOp):

@CustomOp.register("quick_gelu")
classQuickGELU(CustomOp):
    # https://github.com/huggingface/transformers/blob/main/src/transformers/activations.py#L90

@CustomOp.register("gelu_and_mul")
classGeluAndMul(CustomOp):
"""An activation function for GeGLU.

    The function computes x -> GELU(x[:d]) * x[d:] where d = x.shape[-1] // 2.

    Shapes:
        x: (batch_size, seq_len, 2 * d) or (num_tokens, 2 * d)
        return: (batch_size, seq_len, d) or (num_tokens, d)
    """


@CustomOp.register("gelu_and_mul_sparse")
classGeluAndMulSparse(CustomOp):
"""An activation function for GeluAndMulSparse.
    This activation function is used in Gemma3n. It computes:
        up_proj = self.up_proj(x)
        gate_proj = self.gate_proj(x)
        gate_proj = self._gaussian_topk(gate_proj) # sparsity
        activations = self.act_fn(gate_proj) # gelu
        down_proj = self.down_proj(activations * up_proj)
    Shapes:
        x: (num_tokens, 2 * d) or (batch_size, seq_len, 2 * d)
        return: (num_tokens, d) or (batch_size, seq_len, d)
    """


@CustomOp.register("relu2")
classReLUSquaredActivation(CustomOp):
"""
    Applies the relu^2 activation introduced in https://arxiv.org/abs/2109.08668v2
    """


@CustomOp.register("xielu")
classXIELU(CustomOp):
"""
    Applies the xIELU activation function introduced in https://arxiv.org/abs/2411.13010
    If the user has installed the nickjbrowning/XIELU, we import xIELU CUDA
    Otherwise, we emit a single warning and use xIELU Python
    """


@CustomOp.register("swigluoai_and_mul")
classSwigluOAIAndMul(CustomOp):
    # https://github.com/huggingface/transformers/blob/v4.55.0/src/transformers/models/gpt_oss/modeling_gpt_oss.py#L106-L110

@CustomOp.register("fatrelu_and_mul")
classFatreluAndMul(CustomOp):
"""An activation function for FATReLU.

    The function computes x -> FATReLU(x[:d]) * x[d:] where
    d = x.shape[-1] // 2.
    This is used in openbmb/MiniCPM-S-1B-sft.

    Shapes:
        x: (num_tokens, 2 * d) or (batch_size, seq_len, 2 * d)
        return: (num_tokens, d) or (batch_size, seq_len, d)
    """
```

**3. MM-Conv:**

```
@CustomOp.register("conv2d")
classConv2dLayer(ConvLayerBase):
"""Conv layer with Conv2d."""


@CustomOp.register("conv3d")
classConv3dLayer(ConvLayerBase):
"""Conv layer with Conv3d."""
```

**4. Embedding:**

```
@PluggableLayer.register("vocab_parallel_embedding")
classVocabParallelEmbedding(PluggableLayer):
"""Embedding parallelized in the vocabulary dimension.

    Adapted from torch.nn.Embedding, note that we pad the vocabulary size to
    make sure it is divisible by the number of model parallel GPUs.

    In order to support various loading methods, we ensure that LoRA-added
    embeddings are always at the end of TP-sharded tensors. In other words,
    we shard base embeddings and LoRA embeddings separately (both padded),
    and place them in the same tensor.
    In this example, we will have the original vocab size = 1010,
    added vocab size = 16 and padding to 64. Therefore, the total
    vocab size with padding will be 1088 (because we first pad 1010 to
    1024, add 16, and then pad to 1088).
    Therefore, the tensor format looks like the following:
    TP1, rank 0 (no sharding):
                            |< --------BASE-------- >|< -BASE PADDING-- >|< -----LORA------ >|< -LORA PADDING-- >|
    corresponding token_id: |  0  |  1  | ... | 1009 |  -1  | ... |  -1  | 1010 | ... | 1025 |  -1  | ... |  -1  |
                     index: |  0  |  1  | ... | 1009 | 1010 | ... | 1023 | 1024 | ... | 1039 | 1040 | ... | 1087 |

    TP2, rank 0:
                            |< --------------------BASE--------------------- >|< -----LORA------ >|< -LORA PADDING- >|
    corresponding token_id: |  0  |  1  |  2  | ... | 497  | 498 | ...  | 511 | 1010 | ... | 1025 |  -1  | ... |  -1 |
                     index: |  0  |  1  |  2  | ... | 497  | 498 | ...  | 511 | 512  | ... | 527  |  528 | ... | 543 |
    TP2, rank 1:
                            |< -----------BASE----------- >|< -BASE PADDING- >|< -----------LORA PADDING----------- >|
    corresponding token_id: | 512 | 513 | 514 | ... | 1009 | -1  | ...  | -1  |  -1  | ... |  -1  | -1  | ... |   -1 |
                     index: |  0  |  1  |  2  | ... | 497  | 498 | ...  | 511 | 512  | ... | 527  | 528 | ... |  543 |

    Args:
        num_embeddings: vocabulary size.
        embedding_dim: size of hidden state.
        params_dtype: type of the parameters.
        org_num_embeddings: original vocabulary size (without LoRA).
        padding_size: padding size for the vocabulary.
        quant_config: quant config for the layer
        prefix: full name of the layer in the state dict
    """  # noqa: E501


@PluggableLayer.register("parallel_lm_head")
classParallelLMHead(VocabParallelEmbedding):
"""Parallelized LM head.

    Output logits weight matrices used in the Sampler. The weight and bias
    tensors are padded to make sure they are divisible by the number of
    model parallel GPUs.

    Args:
        num_embeddings: vocabulary size.
        embedding_dim: size of hidden state.
        bias: whether to use bias.
        params_dtype: type of the parameters.
        org_num_embeddings: original vocabulary size (without LoRA).
        padding_size: padding size for the vocabulary.
    """
```

**5. Linear:**

```
@PluggableLayer.register("row_parallel_linear")
classRowParallelLinear(LinearBase):
"""Linear layer with row parallelism.

    The linear layer is defined as Y = XA + b. A is parallelized along
    its first dimension and X along its second dimension as:
               -   -
              | A_1 |
              | .   |
          A = | .   |        X = [X_1, ..., X_p]
              | .   |
              | A_p |
               -   -
    Arguments:
        input_size: first dimension of matrix A.
        output_size: second dimension of matrix A.
        bias: If true, add bias. Note that bias is not parallelized.
        input_is_parallel: If true, we assume that the input is already
                           split across the GPUs and we do not split
                           again.
        skip_bias_add: This was added to enable performance optimization where
                       bias can be fused with other element-wise operations.
                       We skip adding bias but instead return it.
        params_dtype: Data type for the parameters.
        reduce_results: If true, call all-reduce on output and make Y available
                       to all GPUs, otherwise, every GPU will have its output
                       which is Y = X_iA_i
        quant_config: Quantization configure.
        prefix: The name of the layer in the state dict, including all parents
                        (e.g. model.layers.0.down_proj)
        return_bias: If true, return bias together with outputs in forward pass.
        disable_tp: If true, weights matrix won't be sharded through tp rank.
    """


@PluggableLayer.register("column_parallel_linear")
classColumnParallelLinear(LinearBase):
"""Linear layer with column parallelism.

    The linear layer is defined as Y = XA + b. A is parallelized along
    its second dimension as A = [A_1, ..., A_p].

    Args:
        input_size: first dimension of matrix A.
        output_size: second dimension of matrix A.
        bias: If true, add bias.
        gather_output: If true, call all-gather on output and make Y available
                       to all GPUs, otherwise, every GPU will have its output
                       which is Y_i = XA_i
        skip_bias_add: This was added to enable performance optimizations where
                       bias can be fused with other element-wise operations. we
                       skip adding bias but instead return it.
        params_dtype: Data type for the parameters.
        quant_config: Quantization configure.
        prefix: The name of the layer in the state dict, including all parents
                        (e.g. model.layers.0.qkv_proj)
        return_bias: If true, return bias together with outputs in forward pass.
        disable_tp: If true, weights matrix won't be sharded through tp rank.
    """


@PluggableLayer.register("replicated_linear")
classReplicatedLinear(LinearBase):
"""Replicated linear layer.

    Args:
        input_size: input dimension of the linear layer.
        output_size: output dimension of the linear layer.
        bias: If true, add bias.
        skip_bias_add: If true, skip adding bias but instead return it.
        params_dtype: Data type for the parameters.
        quant_config: Quantization configure.
        prefix: The name of the layer in the state dict, including all parents
                        (e.g. model.layers.0.qkv_proj)
        return_bias: If true, return bias together with outputs in forward pass.
        disable_tp: Take no effect for replicated linear layers.
    """
```

**6. Logits Processor:**

```
@PluggableLayer.register("logits_processor")
classLogitsProcessor(PluggableLayer):
"""Process logits and apply logits processors from sampling metadata.

    This layer does the following:
    1. Gather logits from model hidden_states.
    2. Scale logits if needed.
    3. Apply logits processors (if any).
    """
```

**7. Mamba:**

```
@PluggableLayer.register("mamba_mixer")
classMambaMixer(MambaBase, PluggableLayer):
"""
    Compute ∆, A, B, C, and D the state space parameters and compute
    the `contextualized_states`. A, D are input independent
    (see Mamba paper [1] Section 3.5.2 "Interpretation of A"
    for why A isn't selective) ∆, B, C are input-dependent
    (this is a key difference between Mamba and the linear time
    invariant S4, and is why Mamba is called
    **selective** state spaces)
    """


@PluggableLayer.register("mamba_mixer2")
classMambaMixer2(MambaBase, PluggableLayer):
"""
    Compute ∆, A, B, C, and D the state space parameters and compute
    the `contextualized_states`. A, D are input independent
    (see Mamba paper [1] Section 3.5.2 "Interpretation of A"
    for why A isn't selective) ∆, B, C are input-dependent
    (this is a key difference between Mamba and the linear time
    invariant S4, and is why Mamba is called
    **selective** state spaces)
    """


@CustomOp.register("mixer2_gated_rms_norm")
classMixer2RMSNormGated(CustomOp):

@PluggableLayer.register("plamo2_mamba_mixer")
classPlamo2MambaMixer(MambaBase, PluggableLayer):

@CustomOp.register("short_conv")
classShortConv(MambaBase, CustomOp):
```

**8. MoE:**

```
@PluggableLayer.register("fused_moe")
classFusedMoE(PluggableLayer):
"""FusedMoE layer for MoE models.

    This layer contains both MergedColumnParallel weights (gate_up_proj /
    w13) and RowParallelLinear weights (down_proj/ w2).

    Note: Mixtral uses w1, w2, and w3 for gate, up, and down_proj. We
    copy that naming convention here and handle any remapping in the
    load_weights function in each model implementation.

    Args:
        num_experts: Number of experts in the model
        top_k: Number of experts selected for each token
        hidden_size: Input hidden state size of the transformer
        intermediate_size: Intermediate size of the experts
        params_dtype: Data type for the parameters.
        renormalize: Whether to renormalize the logits in the fused_moe kernel
        quant_config: Quantization configure.
        enable_eplb: Whether to enable expert parallelism load balancer.
        router_logits_dtype: Data type for router logits buffers.
        routed_scaling_factor: A scaling factor that is applied to the topk_weights
                               by the router or the output of the layer depending
                               on the value of `apply_routed_scale_to_output`
        apply_routed_scale_to_output: Determine whether or not `routed_scaling_factor`
                                      is applied to the topk_weights or to the experts
                                      output. It is applied to the experts output
                                      instead of the topk_weights when this feature is
                                      not supported by the router (or the experts).
    """

    # Auto-incrementing layer ID for routing replay buffer binding.
    _next_moe_layer_id: int = 0


@CustomOp.register("modular_fused_moe")
classFusedMoEModularMethod(FusedMoEMethodBase, CustomOp):

@CustomOp.register("unquantized_fused_moe")
classUnquantizedFusedMoEMethod(FusedMoEMethodBase, CustomOp):
"""MoE method without quantization."""


@PluggableLayer.register("transformers_fused_moe")
classTransformersFusedMoE(FusedMoE):
"""Custom FusedMoE for the Transformers modeling backend."""
```

**9. Norm:**

```
@CustomOp.register("rms_norm")
classRMSNorm(CustomOp):
"""Root mean square normalization.

    Computes x -> w * x / sqrt(E[x^2] + eps) where w is the learned weight.
    Refer to https://arxiv.org/abs/1910.07467
    """


@CustomOp.register("rms_norm_gated")
classRMSNormGated(CustomOp):
"""RMS Normalization with optional gating.

    This is a native PyTorch implementation that supports:
    - Standard RMS normalization
    - Group RMS normalization
    - Optional gating with SiLU activation
    """


@CustomOp.register("gemma_rms_norm")
classGemmaRMSNorm(CustomOp):
"""RMS normalization for Gemma.

    Two differences from the above RMSNorm:
        1. x * (1 + w) instead of x * w.
        2. (x * w).to(orig_dtype) instead of x.to(orig_dtype) * w.
    """
```

**10. Quantization:**

```
@CustomOp.register("quant_fp8")
classQuantFP8(CustomOp):
"""
    Quantize input tensor to FP8 (per-tensor, per-token, per-channel, or per-group).
    This CustomOp supports both static and dynamic quantization.
    """
```

**11. Rope:**

```
@CustomOp.register("rotary_embedding")
classRotaryEmbeddingBase(CustomOp):
"""Original rotary positional embedding."""


@CustomOp.register("dual_chunk_rotary_embedding")
classDualChunkRotaryEmbedding(CustomOp):
"""Rotary positional embedding for Dual Chunk Attention."""


@CustomOp.register("apply_rotary_emb")
classApplyRotaryEmb(CustomOp):
```

**12. Encoder:**

```
@PluggableLayer.register("qwen2_decoder")
classCustomQwen2Decoder(PluggableLayer):
"""
    Qwen2 visual encoder
    non-causal attention + causal attention
    token_type_ids ：0=non-causal, 1=causal
    """


@CustomOp.register("mm_encoder_attn")
classMMEncoderAttention(CustomOp):
"""Multi-headed attention without any cache, used for multimodal encoder."""


@PluggableLayer.register("rel_pos_attention")
classRelPosAttention(PluggableLayer):
"""Multi-head Attention block with relative position embeddings."""
```

## Guidelines for Implementing a New CustomOp[¶](#guidelines-for-implementing-a-new-customop "Permanent link")

### Implement a New CustomOp in vLLM[¶](#implement-a-new-customop-in-vllm "Permanent link")

This part is a tutorial of how to implement a New [`CustomOp`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp "            CustomOp") in vLLM.

Steps:

1. Implement a new op class, which extends from [`CustomOp`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp "            CustomOp") base class.
2. Add the `@CustomOp.register("op_name")` decorator on this op class to register it into [`CustomOp`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp "            CustomOp") system.
3. Implement different `forward_xxx()` method according to your needs.

Taking [`MMEncoderAttention`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/attention/mm_encoder_attention/#vllm.model_executor.layers.attention.mm_encoder_attention.MMEncoderAttention "            MMEncoderAttention") as an example:

Code

```
@CustomOp.register("mm_encoder_attn")
classMMEncoderAttention(CustomOp):

    def__init__(
        self,
        num_heads: int,
        head_size: int,
        scale: float | None = None,
        num_kv_heads: int | None = None,
        prefix: str = "",
        multimodal_config: MultiModalConfig | None = None,
    ) -> None:
        super().__init__()
        # Init...

    defforward_native(
        self,
        query: torch.Tensor,
        key: torch.Tensor,
        value: torch.Tensor,
        cu_seqlens: torch.Tensor | None = None,
        max_seqlen: torch.Tensor | None = None,  # Only used for Flash Attention
    ) -> torch.Tensor:
        # Call TORCH_SDPA implementation...

    defforward_cuda(
        self,
        query: torch.Tensor,
        key: torch.Tensor,
        value: torch.Tensor,
        cu_seqlens: torch.Tensor | None = None,
        max_seqlen: torch.Tensor | None = None,  # Only used for Flash Attention
    ) -> torch.Tensor:
        # Call FA or TORCH_SDPA implementation...

    defforward_cpu(
        self,
        query: torch.Tensor,
        key: torch.Tensor,
        value: torch.Tensor,
        cu_seqlens: torch.Tensor | None = None,
        max_seqlen: torch.Tensor | None = None,  # Only used for Flash Attention
    ) -> torch.Tensor:
        # Call TORCH_SDPA implementation...

    defforward_xpu(
        self,
        query: torch.Tensor,
        key: torch.Tensor,
        value: torch.Tensor,
        cu_seqlens: torch.Tensor | None = None,
        max_seqlen: torch.Tensor | None = None,  # Only used for Flash Attention
    ) -> torch.Tensor:
        # Call FA implementation...

    defforward_tpu(
        self,
        query: torch.Tensor,
        key: torch.Tensor,
        value: torch.Tensor,
        cu_seqlens: torch.Tensor | None = None,
        max_seqlen: torch.Tensor | None = None,  # Only used for Flash Attention
    ) -> torch.Tensor:
        # Call PALLAS implementation...
```

### Register a New CustomOp in OOT Device Plugins[¶](#register-a-new-customop-in-oot-device-plugins "Permanent link")

Currently, thanks to [vLLM's hardware-plugin mechanism](https://docs.vllm.ai/en/latest/design/plugin_system/), there are various OOT device plugins emerging out to enable vLLM seamlessly runs on different hardwares. You can also find more details about this mechanism at [Introducing vLLM Hardware Plugin, Best Practice from Ascend NPU](https://blog.vllm.ai/2025/05/12/hardware-plugin.html).

- **Official device plugins:** [vllm-ascend](https://github.com/vllm-project/vllm-ascend) (for Huawei Ascend NPU), [vllm-spyre](https://github.com/vllm-project/vllm-spyre) (for Spyre), [vllm-gaudi](https://github.com/vllm-project/vllm-gaudi) (for Intel Gaudi), [vllm-neuron](https://github.com/vllm-project/vllm-neuron) (for AWS Neuron), [vllm-meta](https://github.com/vllm-project/vllm-metal) (for Apple Silicon), etc.
- **Non-official device plugins:** [vllm-metax](https://github.com/MetaX-MACA/vLLM-metax) (for MetaX GPU), [vllm-kunlun](https://github.com/baidu/vLLM-Kunlun) (for Baidu Kunlun XPU), [vllm-musa](https://github.com/MooreThreads/vllm-musa) (for Moore Threads GPU), etc.

In this case, [`CustomOp`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp "            CustomOp") can enable these hardware manufacturers to seamlessly replace vLLM's operations with their deep-optimized kernels for specific devices at runtime, by just registering an OOT [`CustomOp`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp "            CustomOp") and implementing the `forward_oot()` method.

Now, this part will show you how to register an OOT [`CustomOp`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp "            CustomOp") for a device plugin.

Taking [`MMEncoderAttention`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/attention/mm_encoder_attention/#vllm.model_executor.layers.attention.mm_encoder_attention.MMEncoderAttention "            MMEncoderAttention") as an example:

1. Implement a `CustomMMEncoderAttention` class which extends from [`MMEncoderAttention`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/attention/mm_encoder_attention/#vllm.model_executor.layers.attention.mm_encoder_attention.MMEncoderAttention "            MMEncoderAttention") and implement its `forward_oot()` method.
2. Register your `CustomMMEncoderAttention` into vLLM to replace [`MMEncoderAttention`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/attention/mm_encoder_attention/#vllm.model_executor.layers.attention.mm_encoder_attention.MMEncoderAttention "            MMEncoderAttention").

Code

```
fromvllm.model_executor.layers.attentionimport MMEncoderAttention
fromvllm.model_executor.custom_opimport CustomOp


@CustomOp.register_oot("MMEncoderAttention")
classCustomMMEncoderAttention(MMEncoderAttention):

    def__init__(...):
        super().__init__(...)

    defforward_oot(...):
        # Call optimized device-specific kernels.
        ...
```

In this case, a new item `{"MMEncoderAttention": CustomMMEncoderAttention}` will be added into `op_registry_oot`. When initializing a [`MMEncoderAttention`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/attention/mm_encoder_attention/#vllm.model_executor.layers.attention.mm_encoder_attention.MMEncoderAttention "            MMEncoderAttention") op object, if the class name (i.e., [`MMEncoderAttention`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/attention/mm_encoder_attention/#vllm.model_executor.layers.attention.mm_encoder_attention.MMEncoderAttention "            MMEncoderAttention")) is contained in the keys of `op_registry_oot`, vLLM will replace it with our registered class (i.e., `CustomMMEncoderAttention`) and instantiate it.

After that, when this [`MMEncoderAttention`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/attention/mm_encoder_attention/#vllm.model_executor.layers.attention.mm_encoder_attention.MMEncoderAttention "            MMEncoderAttention") op is called, your `forward_oot()` will be called if it is enabled. Thus, you will get expected performance on your hardwares without directly modify vLLM.

In addition, you can also register all your [`CustomOp`](https://docs.vllm.ai/en/latest/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp "            CustomOp") at one place for better management.

Code

```
fromvllm.model_executor.custom_opimport CustomOp


REGISTERED_CUSTOM_OPS = {
    "CustomOP1": YourCustomOp1,
    "CustomOP2": YourCustomOp2,
    "CustomOP3": YourCustomOp3,
}

for op_name, op_cls in REGISTERED_CUSTOM_OPS.items():
    CustomOp.register_oot(_decorated_op_cls=op_cls, name=op_name)
```