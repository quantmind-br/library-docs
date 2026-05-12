---
title: metadata - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/pool/metadata/
source: sitemap
fetched_at: 2026-05-07T21:41:20.596328948-03:00
rendered_js: false
word_count: 7
summary: This document defines the PoolingMetadata dataclass, which manages tensor states, sequence lengths, and pooling cursors for token processing tasks in a deep learning context.
tags:
    - dataclass
    - tensor-management
    - pooling
    - machine-learning
    - pytorch
    - token-processing
category: reference
---

```
@dataclass
classPoolingMetadata:
"""Tensors for pooling."""

    prompt_lens: torch.Tensor  # CPU Tensor
    prompt_token_ids: torch.Tensor | None  # Model-device tensor
    prompt_token_ids_cpu: torch.Tensor | None  # CPU tensor
    pooling_params: list[PoolingParams]
    pooling_states: list[PoolingStates]
    pooling_cursor: PoolingCursor | None = None

    def__post_init__(self) -> None:
        pooling_params = self.pooling_params

        tasks: list[PoolingTask] = [
            task
            for pooling_param in pooling_params
            if (task := pooling_param.task) is not None
        ]
        assert len(pooling_params) == len(tasks)

        self.tasks = tasks

    def__getitem__(self, indices: slice):
        return PoolingMetadata(
            prompt_lens=self.prompt_lens[indices],
            prompt_token_ids=None
            if self.prompt_token_ids is None
            else self.prompt_token_ids[indices],
            prompt_token_ids_cpu=None
            if self.prompt_token_ids_cpu is None
            else self.prompt_token_ids_cpu[indices],
            pooling_params=self.pooling_params[indices],
            pooling_states=self.pooling_states[indices],
            pooling_cursor=None
            if self.pooling_cursor is None
            else self.pooling_cursor[indices],
        )

    defget_prompt_token_ids(self) -> list[torch.Tensor]:
        prompt_token_ids = self.prompt_token_ids
        assert prompt_token_ids is not None, (
            "Please set `requires_token_ids=True` in `get_pooling_updates`"
        )
        return [prompt_token_ids[i, :num] for i, num in enumerate(self.prompt_lens)]

    defget_prompt_token_ids_cpu(self) -> list[torch.Tensor]:
        prompt_token_ids = self.prompt_token_ids_cpu
        assert prompt_token_ids is not None, (
            "Please set `requires_token_ids=True` in `get_pooling_updates`"
        )
        return [prompt_token_ids[i, :num] for i, num in enumerate(self.prompt_lens)]

    defget_pooling_cursor(self) -> PoolingCursor:
        pooling_cursor = self.pooling_cursor
        assert pooling_cursor is not None, "Should call `build_pooling_cursor` first"

        return pooling_cursor

    defbuild_pooling_cursor(
        self,
        num_scheduled_tokens_np: np.ndarray,
        seq_lens_cpu: torch.Tensor,
        device: torch.device,
        query_start_loc_gpu: torch.Tensor | None = None,
    ):
        n_seq = len(num_scheduled_tokens_np)
        prompt_lens = self.prompt_lens

        assert len(prompt_lens) == n_seq

        num_scheduled_tokens_cpu = torch.from_numpy(num_scheduled_tokens_np)
        if query_start_loc_gpu is None:
            cumsum = torch.zeros(
                n_seq + 1, dtype=torch.int64, pin_memory=pin_memory, device="cpu"
            )
            torch.cumsum(num_scheduled_tokens_cpu, dim=0, out=cumsum[1:])
            cumsum = cumsum.to(device, non_blocking=True)
        else:
            if query_start_loc_gpu.shape[0] != n_seq + 1:
                raise ValueError(
                    "query_start_loc_gpu length does not match "
                    f"the number of sequences: {query_start_loc_gpu.shape[0]} "
                    f"!= {n_seq+1}."
                )
            if query_start_loc_gpu.device != device:
                raise ValueError(
                    "query_start_loc_gpu must be on the same device as the "
                    f"hidden states: {query_start_loc_gpu.device} != {device}."
                )
            cumsum = query_start_loc_gpu
        self.pooling_cursor = PoolingCursor(
            first_token_indices_gpu=cumsum[:n_seq],
            last_token_indices_gpu=cumsum[1:] - 1,
            prompt_lens_cpu=prompt_lens,
            seq_lens_cpu=seq_lens_cpu,
            num_scheduled_tokens_cpu=num_scheduled_tokens_cpu,
        )
```