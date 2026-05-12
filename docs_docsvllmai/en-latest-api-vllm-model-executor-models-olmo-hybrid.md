---
title: olmo_hybrid - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/olmo_hybrid/
source: sitemap
fetched_at: 2026-05-07T21:32:21.314925477-03:00
rendered_js: false
word_count: 0
summary: This code implements the Gated DeltaNet linear attention layer for the OLMo Hybrid architecture, facilitating efficient recurrent state calculation and high-performance fused operations.
tags:
    - deep-learning
    - neural-network
    - linear-attention
    - gated-deltanet
    - tensor-parallelism
    - pytorch-module
category: concept
---

```
classOlmoHybridGatedDeltaNet(nn.Module, MambaBase):
"""
    Gated DeltaNet linear attention layer for OLMo Hybrid.

    This implements the linear attention mechanism that replaces sliding window
    attention in the hybrid architecture.
    """

    @property
    defmamba_type(self) -> str:
        return "gdn_attention"

    defget_state_dtype(self) -> tuple[torch.dtype, torch.dtype]:
        return MambaStateDtypeCalculator.gated_delta_net_state_dtype(
            self.model_config.dtype,
            self.cache_config.mamba_cache_dtype,
            self.cache_config.mamba_ssm_cache_dtype,
        )

    defget_state_shape(self) -> tuple[tuple[int, ...], tuple[int, ...]]:
        return MambaStateShapeCalculator.gated_delta_net_state_shape(
            self.tp_size,
            self.num_k_heads,
            self.num_v_heads,
            self.head_k_dim,
            self.head_v_dim,
            self.conv_kernel_size,
            self.num_spec,
        )

    def__init__(
        self,
        config,
        model_config: ModelConfig | None = None,
        cache_config: CacheConfig | None = None,
        quant_config: QuantizationConfig | None = None,
        speculative_config: SpeculativeConfig | None = None,
        prefix: str = "",
    ) -> None:
        super().__init__()
        self.tp_size = get_tensor_model_parallel_world_size()
        self.tp_rank = get_tensor_model_parallel_rank()
        self.hidden_size = config.hidden_size
        self.num_v_heads = config.linear_num_value_heads
        self.num_k_heads = config.linear_num_key_heads
        self.head_k_dim = config.linear_key_head_dim
        self.head_v_dim = config.linear_value_head_dim
        self.key_dim = self.head_k_dim * self.num_k_heads
        self.value_dim = self.head_v_dim * self.num_v_heads

        self.conv_kernel_size = config.linear_conv_kernel_dim
        self.layer_idx = extract_layer_index(prefix)
        self.activation = config.hidden_act
        self.act = ACT2FN[config.hidden_act]
        self.layer_norm_epsilon = config.rms_norm_eps
        assert getattr(config, "linear_use_gate", True), (
            "OlmoHybridGatedDeltaNet requires linear_use_gate=True"
        )
        self.allow_neg_eigval = getattr(config, "linear_allow_neg_eigval", False)
        self.prefix = prefix

        self.config = config
        self.model_config = model_config
        self.cache_config = cache_config
        self.quant_config = quant_config
        self.speculative_config = speculative_config
        self.num_spec = (
            self.speculative_config.num_speculative_tokens
            if self.speculative_config
            else 0
        )

        # Fused QKVG projection: 1 matmul instead of 4
        self.in_proj_qkvg = MergedColumnParallelLinear(
            input_size=self.hidden_size,
            output_sizes=[self.key_dim, self.key_dim, self.value_dim, self.value_dim],
            bias=False,
            quant_config=quant_config,
            prefix=f"{prefix}.in_proj_qkvg",
        )

        # Separate B and A projections to preserve numerical precision.
        # Fusing these into one matmul changes FP accumulation order for the
        # gating scalars, which compounds through the GDN recurrent state.
        self.b_proj = ColumnParallelLinear(
            input_size=self.hidden_size,
            output_size=self.num_v_heads,
            bias=False,
            quant_config=quant_config,
            prefix=f"{prefix}.b_proj",
        )
        self.a_proj = ColumnParallelLinear(
            input_size=self.hidden_size,
            output_size=self.num_v_heads,
            bias=False,
            quant_config=quant_config,
            prefix=f"{prefix}.a_proj",
        )

        # Fused conv1d: single parameter instead of 3
        self.conv_dim = self.key_dim * 2 + self.value_dim
        self.conv1d = ColumnParallelLinear(
            input_size=self.conv_kernel_size,
            output_size=self.conv_dim,
            bias=False,
            prefix=f"{prefix}.conv1d",
        )
        self.conv1d.weight.data = self.conv1d.weight.data.unsqueeze(1)
        delattr(self.conv1d.weight, "weight_loader")
        set_weight_attrs(
            self.conv1d.weight,
            {
                "weight_loader": _make_fused_conv1d_weight_loader(
                    [self.key_dim, self.key_dim, self.value_dim],
                    self.tp_size,
                    self.tp_rank,
                )
            },
        )

        self.dt_bias = nn.Parameter(
            torch.ones(self.num_v_heads // self.tp_size),
        )
        self.A_log = nn.Parameter(
            torch.empty(
                divide(self.num_v_heads, self.tp_size),
            )
        )

        set_weight_attrs(self.A_log, {"weight_loader": sharded_weight_loader(0)})
        set_weight_attrs(self.dt_bias, {"weight_loader": sharded_weight_loader(0)})

        # use eps=1e-5 to match FLA's FusedRMSNormGated
        self.o_norm = RMSNormGated(
            self.head_v_dim,
            eps=1e-5,
            group_size=None,
            norm_before_gate=True,
            device=current_platform.current_device(),
            dtype=config.torch_dtype if hasattr(config, "torch_dtype") else None,
        )

        self.o_proj = RowParallelLinear(
            self.value_dim,
            self.hidden_size,
            bias=False,
            input_is_parallel=True,
            quant_config=quant_config,
            prefix=f"{prefix}.o_proj",
        )

        # FLA triton kernels need a PyTorch-backed allocator for scratch
        # memory (required by triton >= 3.x autotuner). Set once at init.
        set_triton_allocator(current_platform.current_device())

        compilation_config = get_current_vllm_config().compilation_config
        if prefix in compilation_config.static_forward_context:
            raise ValueError(f"Duplicate layer name: {prefix}")
        compilation_config.static_forward_context[prefix] = self

    defrearrange_mixed_qkv(self, mixed_qkv):
        if mixed_qkv is None:
            return None, None, None
        query, key, value = torch.split(
            mixed_qkv,
            [
                self.key_dim // self.tp_size,
                self.key_dim // self.tp_size,
                self.value_dim // self.tp_size,
            ],
            dim=-1,
        )

        num_k_heads = self.num_k_heads // self.tp_size
        num_v_heads = self.num_v_heads // self.tp_size

        query = rearrange(query, "l (h d) -> 1 l h d", h=num_k_heads, d=self.head_k_dim)
        key = rearrange(key, "l (h d) -> 1 l h d", h=num_k_heads, d=self.head_k_dim)
        value = rearrange(value, "l (h d) -> 1 l h d", h=num_v_heads, d=self.head_v_dim)

        # GQA expansion if needed
        if num_v_heads > num_k_heads:
            expand_ratio = num_v_heads // num_k_heads
            query = query.unsqueeze(3).expand(-1, -1, -1, expand_ratio, -1)
            query = query.reshape(1, query.shape[1], num_v_heads, self.head_k_dim)
            key = key.unsqueeze(3).expand(-1, -1, -1, expand_ratio, -1)
            key = key.reshape(1, key.shape[1], num_v_heads, self.head_k_dim)

        return query.contiguous(), key.contiguous(), value.contiguous()

    defforward(
        self,
        hidden_states: torch.Tensor,
        output: torch.Tensor,
    ):
        # NOTE: We wrap the ENTIRE linear attention forward (projections +
        # core recurrence + output norm + output projection) in a single
        # custom op, rather than just wrapping the recurrent core like
        # other GDN models (e.g. Qwen3Next) do.
        #
        # Why: torch.compile with inductor generates fused kernels for
        # matmuls and pointwise ops. These fused kernels can differ in
        # floating-point accumulation order from eager-mode cuBLAS,
        # introducing small numerical differences (~1e-7 per op). For
        # standard transformer attention this is harmless because each
        # position is computed independently. But for the GDN recurrent
        # state, these tiny input differences compound at every timestep
        # across the full sequence length, causing severe logprob
        # divergence (e.g. ~15% top-1 agreement with eager baseline).
        #
        # By making the full forward opaque to inductor, the projections
        # and output norm run with eager-mode kernels (cuBLAS, triton),
        # preserving numerical consistency. The tradeoff is reduced
        # compilation speedup (~1.5x vs ~3x), but logprob agreement
        # improves from ~15% to ~83% top-1 vs eager.
        #
        # The remaining ~17% divergence comes from inductor compiling
        # the MLP and transformer attention layers that are NOT wrapped
        # in custom ops -- their small precision differences propagate
        # as inputs to the GDN layers from outside.
        torch.ops.vllm.olmo_hybrid_gdn_full_forward(
            hidden_states,
            output,
            self.prefix,
        )

    def_full_forward(
        self,
        hidden_states: torch.Tensor,
        output: torch.Tensor,
    ):
        num_tokens = hidden_states.size(0)

        # ============================================================
        # Part 1: Input Projection (2 fused matmuls instead of 6)
        # ============================================================
        projected_qkvg, _ = self.in_proj_qkvg(hidden_states)
        conv_dim_sharded = (self.key_dim * 2 + self.value_dim) // self.tp_size
        mixed_qkv = projected_qkvg[..., :conv_dim_sharded]
        gate = projected_qkvg[..., conv_dim_sharded:]

        b, _ = self.b_proj(hidden_states)
        a, _ = self.a_proj(hidden_states)

        # ============================================================
        # Part 2: Core Attention
        # ============================================================
        core_attn_out = torch.zeros(
            (num_tokens, self.num_v_heads // self.tp_size, self.head_v_dim),
            dtype=hidden_states.dtype,
            device=hidden_states.device,
        )

        self._forward_core(
            mixed_qkv=mixed_qkv,
            b=b,
            a=a,
            core_attn_out=core_attn_out,
        )

        # ============================================================
        # Part 3: Output Projection
        # ============================================================
        gate = gate.view(num_tokens, self.num_v_heads // self.tp_size, self.head_v_dim)
        core_attn_out_flat = core_attn_out.reshape(-1, core_attn_out.shape[-1])
        gate_flat = gate.reshape(-1, gate.shape[-1])
        core_attn_out_normed = self.o_norm(core_attn_out_flat, gate_flat)
        core_attn_out = core_attn_out_normed.view(
            num_tokens, self.num_v_heads // self.tp_size, self.head_v_dim
        )

        core_attn_out = rearrange(core_attn_out, "l h d -> l (h d)")
        output[:num_tokens], _ = self.o_proj(core_attn_out)

    def_forward_core(
        self,
        mixed_qkv: torch.Tensor,
        b: torch.Tensor,
        a: torch.Tensor,
        core_attn_out: torch.Tensor,
    ):
"""
        Core attention computation (called by custom op).
        """
        forward_context = get_forward_context()
        attn_metadata: AttentionMetadata = forward_context.attn_metadata

        if attn_metadata is None:
            # V1 profile run
            return

        assert isinstance(attn_metadata, dict)
        attn_metadata = attn_metadata[self.prefix]
        assert isinstance(attn_metadata, GDNAttentionMetadata)
        has_initial_state = attn_metadata.has_initial_state
        spec_query_start_loc = attn_metadata.spec_query_start_loc
        non_spec_query_start_loc = attn_metadata.non_spec_query_start_loc
        spec_sequence_masks = attn_metadata.spec_sequence_masks
        spec_token_indx = attn_metadata.spec_token_indx
        non_spec_token_indx = attn_metadata.non_spec_token_indx
        spec_state_indices_tensor = attn_metadata.spec_state_indices_tensor
        non_spec_state_indices_tensor = attn_metadata.non_spec_state_indices_tensor
        self_kv_cache = self.kv_cache
        # conv_state must be (..., dim, width-1) for the conv kernels.
        # DS layout stores it that way directly; SD layout needs a transpose.
        conv_state = (
            self_kv_cache[0]
            if is_conv_state_dim_first()
            else self_kv_cache[0].transpose(-1, -2)
        )
        ssm_state = self_kv_cache[1]
        num_actual_tokens = attn_metadata.num_actual_tokens
        num_accepted_tokens = attn_metadata.num_accepted_tokens

        mixed_qkv = mixed_qkv[:num_actual_tokens]
        b = b[:num_actual_tokens]
        a = a[:num_actual_tokens]

        conv_weights = self.conv1d.weight.view(
            self.conv1d.weight.size(0), self.conv1d.weight.size(2)
        )

        if spec_sequence_masks is not None:
            if attn_metadata.num_prefills == 0 and attn_metadata.num_decodes == 0:
                mixed_qkv_spec = mixed_qkv
                mixed_qkv_non_spec = None
            else:
                mixed_qkv_spec = mixed_qkv.index_select(0, spec_token_indx)
                mixed_qkv_non_spec = mixed_qkv.index_select(0, non_spec_token_indx)
        else:
            mixed_qkv_spec = None
            mixed_qkv_non_spec = mixed_qkv

        if spec_sequence_masks is not None:
            mixed_qkv_spec = causal_conv1d_update(
                mixed_qkv_spec,
                conv_state,
                conv_weights,
                None,  # no bias
                self.activation,
                conv_state_indices=spec_state_indices_tensor[:, 0][
                    : attn_metadata.num_spec_decodes
                ],
                num_accepted_tokens=num_accepted_tokens,
                query_start_loc=spec_query_start_loc,
                max_query_len=spec_state_indices_tensor.size(-1),
                validate_data=False,
            )

        if attn_metadata.num_prefills > 0:
            mixed_qkv_non_spec_T = mixed_qkv_non_spec.transpose(0, 1)
            mixed_qkv_non_spec = causal_conv1d_fn(
                mixed_qkv_non_spec_T,
                conv_weights,
                None,
                activation=self.activation,
                conv_states=conv_state,
                has_initial_state=has_initial_state,
                cache_indices=non_spec_state_indices_tensor,
                query_start_loc=non_spec_query_start_loc,
                metadata=attn_metadata,
            ).transpose(0, 1)
        elif attn_metadata.num_decodes > 0:
            mixed_qkv_non_spec = causal_conv1d_update(
                mixed_qkv_non_spec,
                conv_state,
                conv_weights,
                None,
                self.activation,
                conv_state_indices=non_spec_state_indices_tensor[
                    : attn_metadata.num_decodes
                ],
                validate_data=True,
            )
        else:
            mixed_qkv_non_spec = None

        query_spec, key_spec, value_spec = self.rearrange_mixed_qkv(mixed_qkv_spec)
        query_non_spec, key_non_spec, value_non_spec = self.rearrange_mixed_qkv(
            mixed_qkv_non_spec
        )

        g, beta = fused_olmo_hybrid_gdn_gating(
            self.A_log, a, b, self.dt_bias, self.allow_neg_eigval
        )

        if spec_sequence_masks is not None:
            if attn_metadata.num_prefills == 0 and attn_metadata.num_decodes == 0:
                g_spec = g
                beta_spec = beta
                g_non_spec = None
                beta_non_spec = None
            else:
                g_spec = g.index_select(1, spec_token_indx)
                beta_spec = beta.index_select(1, spec_token_indx)
                g_non_spec = g.index_select(1, non_spec_token_indx)
                beta_non_spec = beta.index_select(1, non_spec_token_indx)
        else:
            g_spec = None
            beta_spec = None
            g_non_spec = g
            beta_non_spec = beta

        if spec_sequence_masks is not None:
            core_attn_out_spec, last_recurrent_state = fused_recurrent_gated_delta_rule(
                q=query_spec,
                k=key_spec,
                v=value_spec,
                g=g_spec,
                beta=beta_spec,
                initial_state=ssm_state,
                inplace_final_state=True,
                cu_seqlens=spec_query_start_loc[: attn_metadata.num_spec_decodes + 1],
                ssm_state_indices=spec_state_indices_tensor,
                num_accepted_tokens=num_accepted_tokens,
                use_qk_l2norm_in_kernel=True,
            )
        else:
            core_attn_out_spec, last_recurrent_state = None, None

        if attn_metadata.num_prefills > 0:
            initial_state = ssm_state[non_spec_state_indices_tensor].contiguous()
            initial_state[~has_initial_state, ...] = 0
            (
                core_attn_out_non_spec,
                last_recurrent_state,
            ) = chunk_gated_delta_rule(
                q=query_non_spec,
                k=key_non_spec,
                v=value_non_spec,
                g=g_non_spec,
                beta=beta_non_spec,
                initial_state=initial_state,
                output_final_state=True,
                cu_seqlens=non_spec_query_start_loc,
                use_qk_l2norm_in_kernel=True,
            )
            ssm_state[non_spec_state_indices_tensor] = last_recurrent_state.to(
                ssm_state.dtype
            )
        elif attn_metadata.num_decodes > 0:
            core_attn_out_non_spec, last_recurrent_state = (
                fused_recurrent_gated_delta_rule(
                    q=query_non_spec,
                    k=key_non_spec,
                    v=value_non_spec,
                    g=g_non_spec,
                    beta=beta_non_spec,
                    initial_state=ssm_state,
                    inplace_final_state=True,
                    cu_seqlens=non_spec_query_start_loc[
                        : attn_metadata.num_decodes + 1
                    ],
                    ssm_state_indices=non_spec_state_indices_tensor,
                    use_qk_l2norm_in_kernel=True,
                )
            )
        else:
            core_attn_out_non_spec, last_recurrent_state = None, None

        if spec_sequence_masks is not None and core_attn_out_non_spec is not None:
            merged_out = torch.empty(
                (1, num_actual_tokens, *core_attn_out_spec.shape[2:]),
                dtype=core_attn_out_non_spec.dtype,
                device=core_attn_out_non_spec.device,
            )
            merged_out.index_copy_(1, spec_token_indx, core_attn_out_spec)
            merged_out.index_copy_(1, non_spec_token_indx, core_attn_out_non_spec)
            core_attn_out[:num_actual_tokens] = merged_out.squeeze(0)
        elif spec_sequence_masks is not None:
            core_attn_out[:num_actual_tokens] = core_attn_out_spec.squeeze(0)
        else:
            core_attn_out[:num_actual_tokens] = core_attn_out_non_spec.squeeze(0)
```