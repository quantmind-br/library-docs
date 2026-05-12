---
title: pooler - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/pooler/
source: sitemap
fetched_at: 2026-05-07T21:26:18.11850476-03:00
rendered_js: false
word_count: 13
summary: This document defines the ClassDispatchPooler class, which routes pooling operations to specialized sub-poolers based on the specific task type provided.
tags:
    - deep-learning
    - neural-networks
    - tensor-processing
    - pooling-logic
    - task-dispatching
    - pytorch
category: reference
---

```
classDispatchPooler(Pooler):
"""Dispatches calls to a sub-pooler based on the pooling task."""

    @classmethod
    deffor_embedding(cls, pooler_config: PoolerConfig):
        return cls(
            {
                "token_embed": pooler_for_token_embed(pooler_config),
                "embed": pooler_for_embed(pooler_config),
            },
        )

    @classmethod
    deffor_seq_cls(
        cls,
        pooler_config: PoolerConfig,
        *,
        pooling: SequencePoolingMethod | SequencePoolingFn | None = None,
        classifier: ClassifierFn | None = None,
    ):
        return cls(
            {
                "token_classify": pooler_for_token_classify(
                    pooler_config,
                    pooling=AllPool(),
                    classifier=classifier,
                ),
                "classify": pooler_for_classify(
                    pooler_config,
                    pooling=pooling,
                    classifier=classifier,
                ),
            }
        )

    def__init__(self, poolers_by_task: Mapping[PoolingTask, Pooler]) -> None:
        super().__init__()

        for task, pooler in poolers_by_task.items():
            if task not in pooler.get_supported_tasks():
                raise ValueError(
                    f"{pooler=} does not support {task=}. "
                    f"Supported tasks: {pooler.get_supported_tasks()}"
                )

        self.poolers_by_task = poolers_by_task

    defget_supported_tasks(self) -> Set[PoolingTask]:
        return set(self.poolers_by_task)

    defget_pooling_updates(self, task: PoolingTask) -> PoolingParamsUpdate:
        return self.poolers_by_task[task].get_pooling_updates(task)

    defforward(
        self,
        hidden_states: torch.Tensor,
        pooling_metadata: PoolingMetadata,
    ) -> PoolerOutput:
        poolers_by_task = self.poolers_by_task
        cursor = pooling_metadata.pooling_cursor

        outputs = list[torch.Tensor | None]()
        offset = 0
        token_offset = 0
        for task, group in groupby(pooling_metadata.tasks):
            if not (pooler := poolers_by_task.get(task)):
                raise ValueError(
                    f"Unsupported task: {task!r} "
                    f"Supported tasks: {self.get_supported_tasks()}"
                )

            num_items = len(list(group))
            group_metadata = pooling_metadata[offset : offset + num_items]
            if cursor is None:
                group_hidden_states = hidden_states
            else:
                # Slice out this group's tokens so sub-poolers see only their
                # portion of the batch. Token offset is computed from the CPU
                # `num_scheduled_tokens_cpu` to avoid a GPU->CPU sync.
                group_cursor = group_metadata.pooling_cursor
                num_group_tokens = int(group_cursor.num_scheduled_tokens_cpu.sum())
                group_hidden_states = hidden_states[
                    token_offset : token_offset + num_group_tokens
                ]
                if token_offset:
                    # Shift first/last indices to be relative to the slice
                    # so seqwise poolers (which index `hidden_states` directly)
                    # remain correct.
                    pooling_cursor = dataclasses.replace(
                        group_cursor,
                        first_token_indices_gpu=(
                            group_cursor.first_token_indices_gpu - token_offset
                        ),
                        last_token_indices_gpu=(
                            group_cursor.last_token_indices_gpu - token_offset
                        ),
                    )
                    group_metadata = dataclasses.replace(
                        group_metadata, pooling_cursor=pooling_cursor
                    )
                token_offset += num_group_tokens

            group_output: PoolerOutput = pooler(group_hidden_states, group_metadata)

            outputs.extend(group_output)
            offset += num_items

        return outputs

    defextra_repr(self) -> str:
        s = f"supported_task={self.get_supported_tasks()}"
        return s
```