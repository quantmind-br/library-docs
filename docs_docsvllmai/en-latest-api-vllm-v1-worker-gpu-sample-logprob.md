---
title: logprob - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/worker/gpu/sample/logprob/
source: sitemap
fetched_at: 2026-05-07T21:42:48.117664317-03:00
rendered_js: false
word_count: 27
summary: This document defines the LogprobTokenIdsState class, which manages per-request overrides for token ID log probability tracking in the vLLM engine.
tags:
    - vllm
    - logprobs
    - sampling-params
    - token-tracking
    - gpu-worker
    - memory-management
category: reference
---

Per-request override of which token ids' logprobs to return.

See `SamplingParams.logprob_token_ids`.

Source code in `vllm/v1/worker/gpu/sample/logprob.py`

```
classLogprobTokenIdsState:
"""Per-request override of which token ids' logprobs to return.

    See `SamplingParams.logprob_token_ids`.
    """

    def__init__(self, max_num_reqs: int, device: torch.device):
        self.max_num_reqs = max_num_reqs
        self.num_token_ids = UvaBackedTensor(max_num_reqs, dtype=torch.int32)
        self.token_ids = StagedWriteTensor(
            (max_num_reqs, MAX_LOGPROB_TOKEN_IDS),
            dtype=torch.int32,
            device=device,
        )

    defadd_request(self, req_idx: int, sampling_params: SamplingParams) -> None:
        token_ids = sampling_params.logprob_token_ids
        if not token_ids:
            self.num_token_ids.np[req_idx] = 0
            return
        n = len(token_ids)
        if n > MAX_LOGPROB_TOKEN_IDS:
            raise ValueError(
                f"Too many logprob_token_ids: {n}. The max is {MAX_LOGPROB_TOKEN_IDS}."
            )
        self.num_token_ids.np[req_idx] = n
        self.token_ids.stage_write(req_idx, 0, token_ids)

    defapply_staged_writes(self) -> None:
        self.num_token_ids.copy_to_uva()
        self.token_ids.apply_write()

    defmax_num_token_ids(self, idx_mapping_np: np.ndarray) -> int:
        return int(self.num_token_ids.np[idx_mapping_np].max(initial=0))
```