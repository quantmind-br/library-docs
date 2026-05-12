---
title: model_arch_config_convertor - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/model_arch_config_convertor/
source: sitemap
fetched_at: 2026-05-07T21:37:44.4904806-03:00
rendered_js: false
word_count: 26
summary: This class provides a base interface for extracting and normalizing configuration parameters from Hugging Face model architectures to support model loading and inference.
tags:
    - huggingface
    - model-config
    - metadata-extraction
    - quantization
    - tensor-dtype
    - transformer-architecture
category: api
---

```
classModelArchConfigConvertorBase:
    def__init__(self, hf_config: PretrainedConfig, hf_text_config: PretrainedConfig):
        self.hf_config = hf_config
        self.hf_text_config = hf_text_config

    defget_architectures(self) -> list[str]:
        # Sometimes we get here from `vllm_config.with_hf_config(text_config)` where
        # `text_config` is a sub-config from a multi-modal model. If this is the case,
        # the sub-config will not have `architectures` and it will explicitly be `None`
        return getattr(self.hf_config, "architectures", None) or []

    defget_num_hidden_layers(self) -> int:
        return getattr(self.hf_text_config, "num_hidden_layers", 0)

    defget_total_num_attention_heads(self) -> int:
        return getattr(self.hf_text_config, "num_attention_heads", 0)

    defget_vocab_size(self) -> int:
        return getattr(self.hf_text_config, "vocab_size", 0)

    defget_hidden_size(self) -> int:
        return getattr(self.hf_text_config, "hidden_size", 0)

    defget_head_size(self) -> int:
        if self.is_deepseek_mla():
            # special case for deepseek_v4
            if hasattr(self.hf_text_config, "compress_ratios"):
                return self.hf_text_config.head_dim
            qk_rope_head_dim = getattr(self.hf_text_config, "qk_rope_head_dim", 0)
            if not envs.VLLM_MLA_DISABLE:
                return self.hf_text_config.kv_lora_rank + qk_rope_head_dim
            else:
                qk_nope_head_dim = getattr(self.hf_text_config, "qk_nope_head_dim", 0)
                if qk_rope_head_dim and qk_nope_head_dim:
                    return qk_rope_head_dim + qk_nope_head_dim

        # NOTE: Some configs may set head_dim=None in the config
        if getattr(self.hf_text_config, "head_dim", None) is not None:
            return self.hf_text_config.head_dim

        # NOTE: Some models (such as PLaMo2.1) use `hidden_size_per_head`
        if getattr(self.hf_text_config, "hidden_size_per_head", None) is not None:
            return self.hf_text_config.hidden_size_per_head

        if (total_num_attention_heads := self.get_total_num_attention_heads()) == 0:
            return 0
        # FIXME(woosuk): This may not be true for all models.
        return self.get_hidden_size() // total_num_attention_heads

    defget_total_num_kv_heads(self) -> int:
        attributes = [
            # For Falcon:
            "n_head_kv",
            "num_kv_heads",
            # For LLaMA-2:
            "num_key_value_heads",
            # For ChatGLM:
            "multi_query_group_num",
            # For Step3p5:
            "num_attention_groups",
        ]
        # For non-grouped-query attention models, the number of KV heads is
        # equal to the number of attention heads.
        default_factory = self.get_total_num_attention_heads
        return getattr_iter(
            self.hf_text_config, attributes, default_factory=default_factory
        )

    defget_num_experts_from_block_configs(self) -> int:
"""Check block_configs for heterogeneous models (e.g., NemotronH).

        For heterogeneous models with varying expert counts per layer,
        returns the MAX to ensure all expert weights can be loaded.
        """
        max_experts = 0
        block_configs = getattr(self.hf_text_config, "block_configs", None)
        if block_configs:
            for block in block_configs:
                if isinstance(block, dict):
                    if block.get("block_type", "") == "moe":
                        max_experts = max(max_experts, block.get("n_routed_experts", 0))
                else:
                    if getattr(block, "block_type", "") == "moe":
                        max_experts = max(
                            max_experts, getattr(block, "n_routed_experts", 0)
                        )
        return max_experts

    defget_num_experts(self) -> int:
"""Returns the number of experts in the model."""
        num_expert_names = [
            "num_experts",  # Jamba
            "moe_num_experts",  # Dbrx
            "n_routed_experts",  # DeepSeek
            "num_local_experts",  # Mixtral
        ]

        num_experts = getattr_iter(self.hf_text_config, num_expert_names, 0)
        if isinstance(num_experts, list):
            # Ernie VL's remote code uses list[int]...
            # The values are always the same so we just take the first one.
            return num_experts[0]

        if not num_experts:
            num_experts = self.get_num_experts_from_block_configs()
        return num_experts

    @final
    @classmethod
    defget_torch_dtype(
        cls,
        hf_config: PretrainedConfig,
        model_id: str,
        revision: str | None,
        config_format: str | ConfigFormat,
    ):
        # NOTE: getattr(config, "dtype", torch.float32) is not correct
        # because config.dtype can be None.
        config_dtype = getattr(hf_config, "dtype", None)

        # Fallbacks for multi-modal models if the root config
        # does not define dtype
        if config_dtype is None:
            config_dtype = getattr(hf_config.get_text_config(), "dtype", None)
        if config_dtype is None and hasattr(hf_config, "vision_config"):
            config_dtype = getattr(hf_config.vision_config, "dtype", None)
        if config_dtype is None and hasattr(hf_config, "encoder_config"):
            config_dtype = getattr(hf_config.encoder_config, "dtype", None)

        # Try to read the dtype of the weights if they are in safetensors format
        if config_dtype is None:
            param_mt = get_safetensors_params_metadata(model_id, revision=revision)

            if param_mt:
                param_dtypes: set[torch.dtype] = {
                    _SAFETENSORS_TO_TORCH_DTYPE[dtype]
                    for info in param_mt.values()
                    if (dtype := info.get("dtype", None))
                    and dtype in _SAFETENSORS_TO_TORCH_DTYPE
                }

                if param_dtypes:
                    return common_broadcastable_dtype(param_dtypes)

        if config_dtype is None:
            config_dtype = torch.float32

        return config_dtype

    def_normalize_quantization_config(self, config: PretrainedConfig):
        quant_cfg = getattr(config, "quantization_config", None)
        if quant_cfg is None:
            # compressed-tensors uses a "compression_config" key
            quant_cfg = getattr(config, "compression_config", None)

        else:
            # Set quant_method for ModelOpt models.
            producer_name = quant_cfg.get("producer", {}).get("name")
            if producer_name == "modelopt":
                quant_algo = quant_cfg.get("quantization", {}).get("quant_algo")
                if quant_algo is not None:
                    quant_algo_upper = str(quant_algo).upper()
                    if quant_algo_upper in {
                        "FP8",
                        "FP8_PER_CHANNEL_PER_TOKEN",
                        "FP8_PB_WO",
                    }:
                        quant_cfg["quant_method"] = "modelopt"
                    elif quant_algo_upper == "NVFP4":
                        quant_cfg["quant_method"] = "modelopt_fp4"
                    else:
                        raise ValueError(f"Unknown ModelOpt quant algo: {quant_algo}")

        if quant_cfg is not None:
            # Use the community standard 'quant_method'
            quant_method = quant_cfg.get("quant_method", "").lower()

            # Normalize library names
            quant_method = quant_method.replace(
                "compressed_tensors", "compressed-tensors"
            )

            quant_cfg["quant_method"] = quant_method

        return quant_cfg

    defget_quantization_config(self):
        quant_cfg = self._normalize_quantization_config(self.hf_config)
        if quant_cfg is None and (
            text_config := getattr(self.hf_config, "text_config", None)
        ):
            # Check the text config as well for multi-modal models.
            quant_cfg = self._normalize_quantization_config(text_config)
        return quant_cfg

    defis_deepseek_mla(self) -> bool:
        if not hasattr(self.hf_text_config, "model_type"):
            return False
        elif self.hf_text_config.model_type in (
            "AXK1",
            "deepseek_v2",
            "deepseek_v3",
            "deepseek_v32",
            "deepseek_v4",
            "deepseek_mtp",
            "glm_moe_dsa",
            "glm4_moe_lite",
            "glm4_moe_lite_mtp",
            "kimi_k2",
            "kimi_linear",
            "longcat_flash",
            "pangu_ultra_moe",
            "pangu_ultra_moe_mtp",
            "bailing_hybrid",
        ):
            # check is deepseek_v4 model
            if hasattr(self.hf_text_config, "compress_ratios"):
                return getattr(self.hf_text_config, "head_dim", None) is not None
            else:
                return getattr(self.hf_text_config, "kv_lora_rank", None) is not None
        elif self.hf_text_config.model_type == "eagle":
            # if the model is an EAGLE module, check for the
            # underlying architecture
            return (
                self.hf_text_config.model.model_type
                in (
                    "AXK1",
                    "deepseek_v2",
                    "deepseek_v3",
                    "deepseek_v32",
                    "deepseek_mtp",
                )
                and getattr(self.hf_text_config, "kv_lora_rank", None) is not None
            )
        return False

    defis_mm_prefix_lm(self) -> bool:
"""Whether to use bidirectional attention for mm positions."""
        if hasattr(self.hf_config, "is_mm_prefix_lm"):
            return bool(self.hf_config.is_mm_prefix_lm)
        # fallback to list of known models
        MM_PREFIX_LM_MODELS = (
            "bagel",
            "gemma3",
            "molmo2",
            "moondream3",
            "paligemma",
            "umm",
        )
        if not hasattr(self.hf_config, "model_type"):
            return False
        return self.hf_config.model_type in MM_PREFIX_LM_MODELS

    defderive_max_model_len_and_key(self) -> tuple[float, str | None]:
        derived_max_model_len = float("inf")
        possible_keys = [
            # OPT
            "max_position_embeddings",
            # GPT-2
            "n_positions",
            # MPT
            "max_seq_len",
            # ChatGLM2
            "seq_length",
            # Command-R
            "model_max_length",
            # Whisper
            "max_target_positions",
            # Others
            "max_sequence_length",
            "max_seq_length",
            "seq_len",
        ]
        # Choose the smallest "max_length" from the possible keys
        max_len_key = None
        for key in possible_keys:
            max_len = getattr(self.hf_text_config, key, None)
            if max_len is not None:
                if max_len < derived_max_model_len:
                    max_len_key = key
                derived_max_model_len = min(derived_max_model_len, max_len)

        # For Command-R / Cohere, Cohere2 / Aya Vision models
        if tmp_max_len := getattr(self.hf_text_config, "model_max_length", None):
            max_len_key = "model_max_length"
            derived_max_model_len = tmp_max_len
        return derived_max_model_len, max_len_key

    defconvert(self) -> ModelArchitectureConfig:
        model_arch_config = ModelArchitectureConfig(
            architectures=self.get_architectures(),
            model_type=self.hf_config.model_type,
            text_model_type=getattr(self.hf_text_config, "model_type", None),
            hidden_size=self.get_hidden_size(),
            total_num_hidden_layers=self.get_num_hidden_layers(),
            total_num_attention_heads=self.get_total_num_attention_heads(),
            head_size=self.get_head_size(),
            vocab_size=self.get_vocab_size(),
            total_num_kv_heads=self.get_total_num_kv_heads(),
            num_experts=self.get_num_experts(),
            quantization_config=self.get_quantization_config(),
            is_deepseek_mla=self.is_deepseek_mla(),
            is_mm_prefix_lm=self.is_mm_prefix_lm(),
            derived_max_model_len_and_key=self.derive_max_model_len_and_key(),
        )

        return model_arch_config
```