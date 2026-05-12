---
title: medusa - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/spec_decode/medusa/
source: sitemap
fetched_at: 2026-05-07T21:41:51.436649952-03:00
rendered_js: false
word_count: 15
summary: This document defines the MedusaProposer class, which implements speculative decoding for token sequence generation using Medusa heads.
tags:
    - speculative-decoding
    - medusa
    - token-generation
    - vllm
    - llm-inference
category: reference
---

## vllm.v1.spec\_decode.medusa [¶](#vllm.v1.spec_decode.medusa "Permanent link")

## MedusaProposer [¶](#vllm.v1.spec_decode.medusa.MedusaProposer "Permanent link")

Medusa proposer class for generating token sequences

Source code in `vllm/v1/spec_decode/medusa.py`

```
classMedusaProposer:
"""
    Medusa proposer class for generating token sequences
    """

    def__init__(
        self,
        vllm_config: VllmConfig,
        device: torch.device,
    ):
        # Save config parameters
        self.vllm_config = vllm_config
        assert vllm_config.speculative_config is not None, (
            "Speculative config must be set"
        )
        self.spec_config = vllm_config.speculative_config
        self.device = device
        self.max_num_tokens = vllm_config.scheduler_config.max_num_batched_tokens
        self.hidden_size = self.spec_config.draft_model_config.get_hidden_size()
        self.dtype = vllm_config.model_config.dtype

    defpropose(
        self,
        target_hidden_states: torch.Tensor,
        sampling_metadata: SamplingMetadata,
        slot_mappings: dict[str, torch.Tensor]
        | list[dict[str, torch.Tensor]]
        | None = None,  # unused
    ) -> torch.Tensor:
        # Generate blocks and compute logits
        blocks = self.model(target_hidden_states)
        logits = self.model.compute_logits(blocks)

        # Compute argmax for each Medusa head and stack into a single tensor
        # Shape: [batch_size, num_heads]
        draft_tokens = torch.stack([logit.argmax(dim=-1) for logit in logits], dim=1)

        return draft_tokens

    defload_model(self, target_model: nn.Module) -> None:
        fromvllm.compilation.backendsimport set_model_tag

        with set_model_tag("medusa_head"):
            self.model = get_model(
                vllm_config=self.vllm_config,
                model_config=self.spec_config.draft_model_config,
            )
        assert not (
            is_mixture_of_experts(self.model)
            and self.vllm_config.parallel_config.enable_eplb
        ), "EPLB for Medusa is not supported"

    @torch.inference_mode()
    defdummy_run(self, num_tokens: int) -> None:
        hidden_states = torch.zeros(
            (self.max_num_tokens, self.hidden_size),
            dtype=self.dtype,
            device=self.device,
        )
        with set_forward_context(None, self.vllm_config, num_tokens=num_tokens):
            self.model(hidden_states)
```