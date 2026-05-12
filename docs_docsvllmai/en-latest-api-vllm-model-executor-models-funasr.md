---
title: funasr - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/funasr/
source: sitemap
fetched_at: 2026-05-07T21:30:06.019152934-03:00
rendered_js: false
word_count: 0
summary: This document defines a PyTorch module for a FunASR encoder that integrates an audio encoder with a transformer-based adaptor, including custom logic for loading and mapping pre-trained model weights from HuggingFace.
tags:
    - py-torch
    - fun-asr
    - model-architecture
    - weight-loading
    - audio-encoder
    - transformer-adaptor
category: reference
---

```
classFunASREncoder(nn.Module):
    def__init__(
        self, *, vllm_config: VllmConfig, prefix: str = "", init_in_fp32: bool = False
    ):
        super().__init__()
        self.audio_encoder = SenseVoiceEncoderSmall(
            input_size=560, **vllm_config.model_config.hf_config.audio_encoder_conf
        )
        self.audio_adaptor = Transformer(
            downsample_rate=1,
            use_low_frame_rate=True,
            ffn_dim=2048,
            llm_dim=1024,
            encoder_dim=512,
            n_layer=2,
            freeze=True,
            prefix=maybe_prefix(prefix, "audio_encoder"),
        )

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
"""Load weights with mapping from HuggingFace format."""
        stacked_params_mapping = [
            # (param_name, shard_name, shard_id)
            ("self_attn.qkv.", "self_attn.q_proj.", "q"),
            ("self_attn.qkv.", "self_attn.k_proj.", "k"),
            ("self_attn.qkv.", "self_attn.v_proj.", "v"),
        ]
        params_dict = dict(self.named_parameters(remove_duplicate=False))
        loaded_params: set[str] = set()

        for name, loaded_weight in weights:
            for param_name, weight_name, shard_id in stacked_params_mapping:
                if weight_name not in name:
                    continue
                name = name.replace(weight_name, param_name)

                param = params_dict[name]
                weight_loader = param.weight_loader
                weight_loader(param, loaded_weight, shard_id)
                break
            else:
                param = params_dict.get(name)
                if param is not None:
                    weight_loader = getattr(
                        param, "weight_loader", default_weight_loader
                    )
                    weight_loader(param, loaded_weight)
            loaded_params.add(name)
        return loaded_params
```