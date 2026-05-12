---
title: minimax_text_01 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/minimax_text_01/
source: sitemap
fetched_at: 2026-05-07T21:31:51.078962696-03:00
rendered_js: false
word_count: 0
summary: This document defines the MiniMaxText01 model class architecture for the vLLM framework, including initialization, forward pass logic, and state management for linear attention mechanisms.
tags:
    - vllm
    - model-architecture
    - minimax-text
    - pytorch
    - causal-lm
    - model-weights
category: reference
---

```
classMiniMaxText01ForCausalLM(nn.Module, HasInnerState, IsHybrid):
    def__init__(self, *, vllm_config: VllmConfig, prefix: str = "") -> None:
        super().__init__()
        config = vllm_config.model_config.hf_config

        self.config = config

        if not hasattr(config, "sliding_window"):
            config.sliding_window = None

        self.CONCAT_FFN = True

        if hasattr(vllm_config.model_config, "max_model_len"):
            self.config.max_model_len = vllm_config.model_config.max_model_len
        self.model = MiniMaxText01Model(
            vllm_config=vllm_config, prefix=maybe_prefix(prefix, "model")
        )
        if get_pp_group().is_last_rank:
            self.lm_head = ParallelLMHead(
                config.vocab_size,
                self.config.hidden_size,
                prefix=maybe_prefix(prefix, "lm_head"),
            )

            self.logits_processor = LogitsProcessor(
                config.vocab_size, self.config.vocab_size
            )

        else:
            self.lm_head = PPMissingLayer()
        self.lm_head.float()
        flash_layer_count = sum(
            1 for attn_type in self.model.decoder_attention_types if attn_type == 1
        )
        self.kv_cache = [torch.tensor([]) for _ in range(flash_layer_count)]
        return

    defcopy_inputs_before_cuda_graphs(self, input_buffers, **kwargs):
        return self.model.minimax_cache.copy_inputs_before_cuda_graphs(
            input_buffers, **kwargs
        )

    defget_seqlen_agnostic_capture_inputs(self, batch_size: int):
        return self.model.minimax_cache.get_seqlen_agnostic_capture_inputs(batch_size)

    defembed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
        return self.model.embed_input_ids(input_ids)

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs,
    ) -> torch.Tensor:
        hidden_states = self.model(
            input_ids, positions, intermediate_tensors, inputs_embeds, **kwargs
        )

        return hidden_states

    defcompute_logits(self, hidden_states: torch.Tensor) -> torch.Tensor:
        logits = self.logits_processor(self.lm_head, hidden_states.float())

        return logits

    defmake_empty_intermediate_tensors(
        self, batch_size: int, dtype: torch.dtype, device: torch.device
    ) -> IntermediateTensors:
        return IntermediateTensors(
            {
                "hidden_states": torch.zeros(
                    (batch_size, self.config.hidden_size), dtype=dtype, device=device
                ),
                "residual": torch.zeros(
                    (batch_size, self.config.hidden_size), dtype=dtype, device=device
                ),
            }
        )

    @classmethod
    defget_mamba_state_dtype_from_config(
        cls,
        vllm_config: "VllmConfig",
    ) -> tuple[torch.dtype, torch.dtype]:
        return MambaStateDtypeCalculator.linear_attention_state_dtype(
            vllm_config.model_config.dtype,
            vllm_config.cache_config.mamba_cache_dtype,
        )

    @classmethod
    defget_mamba_state_shape_from_config(
        cls,
        vllm_config: "VllmConfig",
    ) -> tuple[tuple[int, ...], ...]:
"""Calculate shape for MiniMaxText01LinearAttention cache.

        Args:
            vllm_config: vLLM config

        Returns:
            Tuple containing:
            - state_shape: Shape of the cache
        """
        parallel_config = vllm_config.parallel_config
        hf_config = vllm_config.model_config.hf_config

        return MambaStateShapeCalculator.linear_attention_state_shape(
            num_heads=hf_config.num_attention_heads,
            tp_size=parallel_config.tensor_parallel_size,
            head_dim=hf_config.head_dim,
        )

    @classmethod
    defget_mamba_state_copy_func(cls) -> tuple[MambaStateCopyFunc]:
        return MambaStateCopyFuncCalculator.linear_attention_state_copy_func()

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        loader = AutoWeightsLoader(self)
        return loader.load_weights(weights)
```