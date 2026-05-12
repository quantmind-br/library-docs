---
title: jina - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/jina/
source: sitemap
fetched_at: 2026-05-07T21:31:07.856094213-03:00
rendered_js: false
word_count: 92
summary: This document describes the implementation of the Jina Embeddings V5 model in vLLM, detailing how it integrates task-specific LoRA adapters and handles pooling configurations.
tags:
    - jina-embeddings
    - lora-adapters
    - model-execution
    - pooling-layer
    - vllm-framework
    - machine-learning-architecture
category: reference
---

## JinaEmbeddingsV5Model [¶](#vllm.model_executor.models.jina.JinaEmbeddingsV5Model "Permanent link")

Bases: `Qwen3ForCausalLM`, `VllmModelForPooling`

Jina Embeddings V5 with task-specific LoRA adapters merged at load time.

Extends Qwen3ForCausalLM (the underlying architecture) and declares itself as a pooling model so that as\_embedding\_model() does not wrap it.

Source code in `vllm/model_executor/models/jina.py`

```
classJinaEmbeddingsV5Model(Qwen3ForCausalLM, VllmModelForPooling):
"""Jina Embeddings V5 with task-specific LoRA adapters merged at load time.

    Extends Qwen3ForCausalLM (the underlying architecture) and declares itself
    as a pooling model so that as_embedding_model() does not wrap it.
    """

    is_pooling_model = True

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__(vllm_config=vllm_config, prefix=prefix)

        self._model_name = vllm_config.model_config.model
        self._revision = vllm_config.model_config.revision

        self._task = getattr(
            vllm_config.model_config.hf_config, "jina_task", _DEFAULT_TASK
        )
        if self._task not in _SUPPORTED_TASKS:
            logger.warning(
                "Unknown jina_task=%r. Falling back to %r.",
                self._task,
                _DEFAULT_TASK,
            )
            self._task = _DEFAULT_TASK

        pooler_config = vllm_config.model_config.pooler_config
        assert pooler_config is not None
        self.pooler = DispatchPooler.for_embedding(pooler_config)

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        lora_pairs: dict = {}
        scaling = 1.0

        result = _load_adapter(self._model_name, self._task, self._revision)
        if result is None:
            logger.warning(
                "No adapter found for task %r in %r. Loading raw base weights.",
                self._task,
                self._model_name,
            )
        else:
            adapter_config, adapter_weights = result
            scaling = adapter_config["lora_alpha"] / adapter_config["r"]
            lora_pairs = _build_lora_pairs(adapter_weights)
            logger.info(
                "Loaded %d adapter tensors for task %r (scaling=%.4f, %d LoRA pairs)",
                len(adapter_weights),
                self._task,
                scaling,
                len(lora_pairs),
            )

        def_merge_weights(
            weights: Iterable[tuple[str, torch.Tensor]],
        ) -> Iterable[tuple[str, torch.Tensor]]:
            for name, tensor in weights:
                clean_name = name
                if clean_name.startswith("model."):
                    clean_name = clean_name[len("model.") :]

                if clean_name in lora_pairs:
                    pair = lora_pairs[clean_name]
                    if "A" in pair and "B" in pair:
                        lora_A = pair["A"].to(device=tensor.device, dtype=tensor.dtype)
                        lora_B = pair["B"].to(device=tensor.device, dtype=tensor.dtype)
                        tensor = tensor + (lora_B @ lora_A) * scaling
                yield name, tensor

        loaded = self.model.load_weights(_merge_weights(weights))
        return {f"model.{name}" for name in loaded}
```

## \_build\_lora\_pairs [¶](#vllm.model_executor.models.jina._build_lora_pairs "Permanent link")

```
_build_lora_pairs(adapter_weights: dict) -> dict
```

Group raw adapter tensors into {base\_key: {"A": tensor, "B": tensor}} pairs.

Transforms adapter keys like

base\_model.model.layers.0.self\_attn.q\_proj.lora\_A.weight

Into base keys like: layers.0.self\_attn.q\_proj.weight

Source code in `vllm/model_executor/models/jina.py`

```
def_build_lora_pairs(adapter_weights: dict) -> dict:
"""Group raw adapter tensors into {base_key: {"A": tensor, "B": tensor}} pairs.

    Transforms adapter keys like:
        base_model.model.layers.0.self_attn.q_proj.lora_A.weight
    Into base keys like:
        layers.0.self_attn.q_proj.weight
    """
    lora_pairs = defaultdict(dict)
    for key, tensor in adapter_weights.items():
        clean_key = key
        if clean_key.startswith("base_model.model."):
            clean_key = clean_key[len("base_model.model.") :]

        if ".lora_A." in clean_key:
            base_key = clean_key.split(".lora_A.")[0] + ".weight"
            lora_pairs[base_key]["A"] = tensor
        elif ".lora_B." in clean_key:
            base_key = clean_key.split(".lora_B.")[0] + ".weight"
            lora_pairs[base_key]["B"] = tensor

    return dict(lora_pairs)
```

## \_load\_adapter [¶](#vllm.model_executor.models.jina._load_adapter "Permanent link")

Load adapter config and weights from a local path or HF repo.

Returns (adapter\_config, adapter\_weights) or None if not found.

Source code in `vllm/model_executor/models/jina.py`

```
def_load_adapter(
    model: str,
    task: str,
    revision: str | None,
) -> tuple[dict, dict[str, torch.Tensor]] | None:
"""Load adapter config and weights from a local path or HF repo.

    Returns (adapter_config, adapter_weights) or None if not found.
    """
    config_bytes = get_hf_file_bytes(
        f"adapters/{task}/adapter_config.json",
        model,
        revision,
    )
    if config_bytes is None:
        return None

    adapter_config = json.loads(config_bytes)

    weights_bytes = get_hf_file_bytes(
        f"adapters/{task}/adapter_model.safetensors",
        model,
        revision,
    )
    if weights_bytes is None:
        return None

    adapter_weights = safetensors_load(weights_bytes)
    return adapter_config, adapter_weights
```