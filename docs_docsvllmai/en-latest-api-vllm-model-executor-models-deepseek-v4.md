---
title: deepseek_v4 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/deepseek_v4/
source: sitemap
fetched_at: 2026-05-07T21:29:40.791278723-03:00
rendered_js: false
word_count: 166
summary: This document defines the configuration and implementation for the DeepSeek V4 model in vLLM, specifically detailing lazy resolution for FP8 expert quantization and weight mapping for MoE dispatch.
tags:
    - deepseek-v4
    - fp8-quantization
    - moe
    - vllm
    - model-config
    - expert-dtype
category: reference
---

## DeepseekV4FP8Config [¶](#vllm.model_executor.models.deepseek_v4.DeepseekV4FP8Config "Permanent link")

Bases: `Fp8Config`

FP8 config for DeepSeek V4 with expert-dtype-aware MoE dispatch.

DeepSeek V4 checkpoints always use FP8 block quantization for linear/attention layers. The MoE expert weights vary by checkpoint: - `expert_dtype="fp4"` (e.g. DeepSeek-V4-Flash): MXFP4 experts with ue8m0 (e8m0fnu) FP8 linear scales. - `expert_dtype="fp8"` (e.g. DeepSeek-V4-Flash-Base): FP8 block experts with float32 FP8 linear scales.

The dispatch and the linear scale dtype are both keyed off `expert_dtype` from the model's hf\_config; missing values default to `"fp4"` so existing FP4 checkpoints stay unchanged.

NOTE: `expert_dtype` is resolved lazily because this config is constructed during VllmConfig setup, before `set_current_vllm_config` is active. Reading hf\_config eagerly in `__init__` would always see the default `"fp4"` and silently misroute Flash-Base checkpoints.

Source code in `vllm/model_executor/models/deepseek_v4.py`

```
classDeepseekV4FP8Config(Fp8Config):
"""FP8 config for DeepSeek V4 with expert-dtype-aware MoE dispatch.

    DeepSeek V4 checkpoints always use FP8 block quantization for
    linear/attention layers. The MoE expert weights vary by checkpoint:
    - ``expert_dtype="fp4"`` (e.g. DeepSeek-V4-Flash): MXFP4 experts
      with ue8m0 (e8m0fnu) FP8 linear scales.
    - ``expert_dtype="fp8"`` (e.g. DeepSeek-V4-Flash-Base): FP8 block
      experts with float32 FP8 linear scales.

    The dispatch and the linear scale dtype are both keyed off
    ``expert_dtype`` from the model's hf_config; missing values default
    to ``"fp4"`` so existing FP4 checkpoints stay unchanged.

    NOTE: ``expert_dtype`` is resolved lazily because this config is
    constructed during VllmConfig setup, before ``set_current_vllm_config``
    is active. Reading hf_config eagerly in ``__init__`` would always see
    the default ``"fp4"`` and silently misroute Flash-Base checkpoints.
    """

    def__init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._resolved_expert_dtype: str | None = None
        # ``is_scale_e8m0`` is a property that resolves on first read,
        # by which time the current vllm_config has been set.

    @property
    defexpert_dtype(self) -> str:
        if self._resolved_expert_dtype is None:
            try:
                hf_config = get_current_vllm_config().model_config.hf_config
            except Exception:
                # vllm_config not yet set; defer the decision until a
                # later call lands inside set_current_vllm_config.
                return "fp4"
            expert_dtype = getattr(hf_config, "expert_dtype", "fp4")
            if expert_dtype not in _DEEPSEEK_V4_EXPERT_DTYPES:
                raise ValueError(
                    f"Unsupported DeepSeek V4 expert_dtype={expert_dtype!r}; "
                    f"expected one of {_DEEPSEEK_V4_EXPERT_DTYPES}."
                )
            self._resolved_expert_dtype = expert_dtype
            fromvllm.loggerimport init_logger

            init_logger(__name__).info_once(
                "DeepSeek V4 expert_dtype resolved to %r", expert_dtype
            )
        return self._resolved_expert_dtype

    @property
    defis_scale_e8m0(self) -> bool:
        # FP4 checkpoints store FP8 linear scales as e8m0fnu; FP8 expert
        # checkpoints (Flash-Base) store them as float32.
        return self.expert_dtype == "fp4"

    @classmethod
    defget_name(cls) -> QuantizationMethods:
        return "deepseek_v4_fp8"

    @classmethod
    defoverride_quantization_method(
        cls, hf_quant_cfg, user_quant, hf_config=None
    ) -> QuantizationMethods | None:
        if not (
            isinstance(hf_quant_cfg, dict)
            and hf_quant_cfg.get("quant_method") in ("fp8", "deepseek_v4_fp8")
        ):
            return None
        model_type = getattr(hf_config, "model_type", None)
        if model_type == "deepseek_v4" or user_quant == "deepseek_v4_fp8":
            return "deepseek_v4_fp8"
        return None

    defget_quant_method(self, layer, prefix):
        if isinstance(layer, FusedMoE):
            if is_layer_skipped(
                prefix=prefix,
                ignored_layers=self.ignored_layers,
                fused_mapping=self.packed_modules_mapping,
            ):
                return UnquantizedFusedMoEMethod(layer.moe_config)
            if self.expert_dtype == "fp4":
                return Mxfp4MoEMethod(layer.moe_config)
            # expert_dtype == "fp8": fall through to Fp8Config which
            # returns Fp8MoEMethod with block-wise float32 scales.
        return super().get_quant_method(layer, prefix)

    defis_mxfp4_quant(self, prefix, layer):
        return isinstance(layer, FusedMoE) and self.expert_dtype == "fp4"
```

## DeepseekV4ForCausalLM [¶](#vllm.model_executor.models.deepseek_v4.DeepseekV4ForCausalLM "Permanent link")

Bases: `Module`

Source code in `vllm/model_executor/models/deepseek_v4.py`

```
classDeepseekV4ForCausalLM(nn.Module):
    model_cls = DeepseekV4Model

    # Default mapper assumes the original FP4-expert checkpoint layout.
    # Overridden per-instance in __init__ when expert_dtype != "fp4".
    hf_to_vllm_mapper = _make_deepseek_v4_weights_mapper("fp4")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()

        config = vllm_config.model_config.hf_config
        self.config = config
        expert_dtype = getattr(config, "expert_dtype", "fp4")
        if expert_dtype != "fp4":
            self.hf_to_vllm_mapper = _make_deepseek_v4_weights_mapper(expert_dtype)

        self.model = self.model_cls(
            vllm_config=vllm_config, prefix=maybe_prefix(prefix, "model")
        )
        self.lm_head = ParallelLMHead(
            config.vocab_size,
            config.hidden_size,
            prefix=maybe_prefix(prefix, "lm_head"),
        )
        self.logits_processor = LogitsProcessor(config.vocab_size)

    defembed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
        return self.model.embed_input_ids(input_ids)

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor | None:
        logits = self.logits_processor(self.lm_head, hidden_states)
        return logits

    defforward(
        self,
        input_ids: torch.Tensor,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
    ) -> torch.Tensor | IntermediateTensors:
        hidden_states = self.model(
            input_ids, positions, intermediate_tensors, inputs_embeds
        )
        return hidden_states

    defget_mtp_target_hidden_states(self) -> torch.Tensor | None:
"""Pre-hc_head residual stream buffer (max_num_batched_tokens,
        hc_mult * hidden_size) for the MTP draft model. Populated by
        forward(); valid after each target step."""
        return getattr(self.model, "_mtp_hidden_buffer", None)

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        loader = AutoWeightsLoader(self, skip_substrs=["mtp."])
        loaded_params = loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
        self.model.finalize_mega_moe_weights()
        return loaded_params

    defget_expert_mapping(self) -> list[tuple[str, str, int, str]]:
        return self.model.get_expert_mapping()
```

### get\_mtp\_target\_hidden\_states [¶](#vllm.model_executor.models.deepseek_v4.DeepseekV4ForCausalLM.get_mtp_target_hidden_states "Permanent link")

```
get_mtp_target_hidden_states() -> Tensor | None
```

Pre-hc\_head residual stream buffer (max\_num\_batched\_tokens, hc\_mult * hidden\_size) for the MTP draft model. Populated by forward(); valid after each target step.

Source code in `vllm/model_executor/models/deepseek_v4.py`

```
defget_mtp_target_hidden_states(self) -> torch.Tensor | None:
"""Pre-hc_head residual stream buffer (max_num_batched_tokens,
    hc_mult * hidden_size) for the MTP draft model. Populated by
    forward(); valid after each target step."""
    return getattr(self.model, "_mtp_hidden_buffer", None)
```