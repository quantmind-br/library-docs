---
title: outputs - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/outputs/
source: sitemap
fetched_at: 2026-05-07T21:41:17.171241989-03:00
rendered_js: false
word_count: 108
summary: This document defines core components for handling asynchronous model output, including tensor-based log-probability management and structure initialization for model runner outputs.
tags:
    - vllm
    - async-model-runner
    - logprobs
    - tensors
    - api-reference
    - pytorch
category: reference
---

## AsyncModelRunnerOutput [¶](#vllm.v1.outputs.AsyncModelRunnerOutput "Permanent link")

Bases: `ABC`

Source code in `vllm/v1/outputs.py`

```
classAsyncModelRunnerOutput(ABC):
    @abstractmethod
    defget_output(self) -> ModelRunnerOutput:
"""Get the ModelRunnerOutput for this async output.

        This is a blocking call that waits until the results are ready, which
        might involve copying device tensors to the host.
        This method should only be called once per AsyncModelRunnerOutput.
        """
        pass
```

### get\_output `abstractmethod` [¶](#vllm.v1.outputs.AsyncModelRunnerOutput.get_output "Permanent link")

```
get_output() -> ModelRunnerOutput
```

Get the ModelRunnerOutput for this async output.

This is a blocking call that waits until the results are ready, which might involve copying device tensors to the host. This method should only be called once per AsyncModelRunnerOutput.

Source code in `vllm/v1/outputs.py`

```
@abstractmethod
defget_output(self) -> ModelRunnerOutput:
"""Get the ModelRunnerOutput for this async output.

    This is a blocking call that waits until the results are ready, which
    might involve copying device tensors to the host.
    This method should only be called once per AsyncModelRunnerOutput.
    """
    pass
```

## LogprobsTensors [¶](#vllm.v1.outputs.LogprobsTensors "Permanent link")

Bases: `NamedTuple`

Source code in `vllm/v1/outputs.py`

```
classLogprobsTensors(NamedTuple):
    # [num_reqs x num_generated_tokens, max_num_logprobs + 1]
    logprob_token_ids: torch.Tensor
    # [num_reqs x num_generated_tokens, max_num_logprobs + 1]
    logprobs: torch.Tensor
    # [num_reqs x num_generated_tokens]
    selected_token_ranks: torch.Tensor
    # [num_reqs]
    cu_num_generated_tokens: list[int] | None = None

    deftolists(self, cu_num_generated_tokens: list[int] | None = None):
        return LogprobsLists(
            self.logprob_token_ids.cpu().numpy(),
            self.logprobs.cpu().numpy(),
            self.selected_token_ranks.cpu().numpy(),
            cu_num_generated_tokens
            if cu_num_generated_tokens is not None
            else self.cu_num_generated_tokens,
        )

    defto_cpu_nonblocking(self) -> "LogprobsTensors":
        if self.logprob_token_ids.device.type == "cpu":
            return self
        return LogprobsTensors(
            self.logprob_token_ids.to("cpu", non_blocking=True),
            self.logprobs.to("cpu", non_blocking=True),
            self.selected_token_ranks.to("cpu", non_blocking=True),
            self.cu_num_generated_tokens,
        )

    deffilter(self, mask: torch.Tensor) -> "LogprobsTensors":
"""Filter the logprobs tensors with the given bool mask."""
        assert self.cu_num_generated_tokens is None, (
            "filter can't be used with cu_num_generated_tokens"
        )
        return LogprobsTensors(
            self.logprob_token_ids[mask],
            self.logprobs[mask],
            self.selected_token_ranks[mask],
        )

    @staticmethod
    defempty_cpu(
        num_positions: int, num_tokens_per_position: int
    ) -> "LogprobsTensors":
"""Create empty LogprobsTensors on CPU."""

        logprob_token_ids = torch.empty(
            (num_positions, num_tokens_per_position), dtype=torch.int32, device="cpu"
        )
        logprobs = torch.empty_like(logprob_token_ids, dtype=torch.float32)
        selected_token_ranks = torch.empty(
            num_positions, dtype=torch.int32, device="cpu"
        )
        return LogprobsTensors(
            logprob_token_ids=logprob_token_ids,
            logprobs=logprobs,
            selected_token_ranks=selected_token_ranks,
        )
```

### empty\_cpu `staticmethod` [¶](#vllm.v1.outputs.LogprobsTensors.empty_cpu "Permanent link")

```
empty_cpu(
    num_positions: int, num_tokens_per_position: int
) -> LogprobsTensors
```

Create empty LogprobsTensors on CPU.

Source code in `vllm/v1/outputs.py`

```
@staticmethod
defempty_cpu(
    num_positions: int, num_tokens_per_position: int
) -> "LogprobsTensors":
"""Create empty LogprobsTensors on CPU."""

    logprob_token_ids = torch.empty(
        (num_positions, num_tokens_per_position), dtype=torch.int32, device="cpu"
    )
    logprobs = torch.empty_like(logprob_token_ids, dtype=torch.float32)
    selected_token_ranks = torch.empty(
        num_positions, dtype=torch.int32, device="cpu"
    )
    return LogprobsTensors(
        logprob_token_ids=logprob_token_ids,
        logprobs=logprobs,
        selected_token_ranks=selected_token_ranks,
    )
```

### filter [¶](#vllm.v1.outputs.LogprobsTensors.filter "Permanent link")

Filter the logprobs tensors with the given bool mask.

Source code in `vllm/v1/outputs.py`

```
deffilter(self, mask: torch.Tensor) -> "LogprobsTensors":
"""Filter the logprobs tensors with the given bool mask."""
    assert self.cu_num_generated_tokens is None, (
        "filter can't be used with cu_num_generated_tokens"
    )
    return LogprobsTensors(
        self.logprob_token_ids[mask],
        self.logprobs[mask],
        self.selected_token_ranks[mask],
    )
```

## make\_empty\_encoder\_model\_runner\_output [¶](#vllm.v1.outputs.make_empty_encoder_model_runner_output "Permanent link")

```
make_empty_encoder_model_runner_output(
    scheduler_output: SchedulerOutput,
) -> ModelRunnerOutput
```

Create a ModelRunnerOutput stub that contains the correct per-request bookkeeping but no generated data yet.

Source code in `vllm/v1/outputs.py`

```
defmake_empty_encoder_model_runner_output(
    scheduler_output: "SchedulerOutput",
) -> ModelRunnerOutput:
"""
    Create a ModelRunnerOutput stub that contains the correct
    per-request bookkeeping but no generated data yet.
    """
    if not scheduler_output.num_scheduled_tokens:
        return EMPTY_MODEL_RUNNER_OUTPUT

    # Convert to list so we get a deterministic, indexable sequence
    req_ids: list[str] = list(scheduler_output.num_scheduled_tokens.keys())

    # Give every request its own contiguous index
    req_id_to_index: dict[str, int] = {rid: idx for idx, rid in enumerate(req_ids)}

    # No tokens generated yet ⇒ one empty list per request
    sampled_token_ids: list[list[int]] = [[0] for _ in req_ids]

    # Pooler outputs are not available yet ⇒ use None placeholders
    pooler_output: list[torch.Tensor | None] = [None for _ in req_ids]

    return ModelRunnerOutput(
        req_ids=req_ids,
        req_id_to_index=req_id_to_index,
        sampled_token_ids=sampled_token_ids,
        pooler_output=pooler_output,
    )
```