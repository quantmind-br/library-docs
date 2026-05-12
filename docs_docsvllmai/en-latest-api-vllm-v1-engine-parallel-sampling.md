---
title: parallel_sampling - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/engine/parallel_sampling/
source: sitemap
fetched_at: 2026-05-07T21:40:41.058109159-03:00
rendered_js: false
word_count: 157
summary: This class manages state and processing for parallel sampling requests by tracking parent and child request relationships, generating unique child sampling parameters, and aggregating output results.
tags:
    - parallel-sampling
    - request-management
    - vllm
    - sampling-parameters
    - engine-core
    - token-generation
category: concept
---

Info, state & processing for parallel sampling request.

Store parent request ID and sampling params. Facilitate generating child request sampling params.

Source code in `vllm/v1/engine/parallel_sampling.py`

```
classParentRequest:
"""Info, state & processing for parallel sampling request.

    Store parent request ID and sampling params.
    Facilitate generating child request sampling params.
    """

    request_id: str
    external_req_id: str
    sampling_params: SamplingParams

    # To track the completion of child requests
    child_requests: set[str]

    # To aggregate child completions when not streaming
    output_aggregator: list[CompletionOutput]

    # To find the max number of generated tokens across all children
    max_num_generation_tokens: int

    # To efficiently obtain child sampling params
    cached_child_sampling_params: SamplingParams | None

    def__init__(self, request: EngineCoreRequest) -> None:
        assert request.external_req_id is not None
        sampling_params = request.params
        self.request_id = request.request_id
        self.external_req_id = request.external_req_id
        self.sampling_params = sampling_params

        self.child_requests = set()
        self.output_aggregator = (
            [cast(CompletionOutput, None)] * sampling_params.n
            if (sampling_params.output_kind == RequestOutputKind.FINAL_ONLY)
            else []
        )
        self.max_num_generation_tokens = 0
        self.cached_child_sampling_params = None

    def_get_child_sampling_params(
        self,
        index: int,
    ) -> SamplingParams:
"""Efficiently obtain child `sampling_params`

        If `sampling_params.seed` is not `None` then
        each child request requires a unique clone of
        parent `sampling_params` with a unique seed.

        Args:
          index: index within `n` child requests

        Returns:
          Child `sampling_params` instance.
        """
        seed = self.sampling_params.seed
        if self.cached_child_sampling_params:
            # Reuse child sampling_params data structure
            return self.cached_child_sampling_params
        # Build child sampling_params
        child_sampling_params = copy(self.sampling_params)
        child_sampling_params.n = 1
        if seed is None:
            # Cache child sampling_params for later reuse
            self.cached_child_sampling_params = child_sampling_params
        else:
            # Each child gets a clone with a unique seed
            child_sampling_params.seed = seed + index
        return child_sampling_params

    defget_child_info(self, index: int) -> tuple[str, SamplingParams]:
"""Get child request ID and sampling params.

        Args:
          index: index within `n` child requests.

        Returns:
          (request ID, sampling_params) tuple
        """
        child_req_id = f"{index}_{self.request_id}"
        self.child_requests.add(child_req_id)
        return child_req_id, self._get_child_sampling_params(index)

    @property
    defn(self) -> int:
        return self.sampling_params.n

    defget_outputs(
        self,
        child_request_id: str,
        completion_output: CompletionOutput,
    ) -> tuple[list[CompletionOutput], bool]:
        already_finished_and_returned: bool = False
        if completion_output.finished():
            if child_request_id in self.child_requests:
                self.child_requests.remove(child_request_id)
            else:
                # child request ID is not available in child_requests
                # which means the request had finished in previous
                # batch step and returned to the client earlier
                already_finished_and_returned = True

        if self.sampling_params.output_kind != RequestOutputKind.FINAL_ONLY:
            # If streaming, just return the current output
            #
            # DO NOT output finished and already returned child request to client again
            outputs = [] if already_finished_and_returned else [completion_output]
        else:
            # If not streaming, aggregate the n final outputs.
            self.output_aggregator[completion_output.index] = completion_output
            outputs = [] if self.child_requests else self.output_aggregator

        finished = not self.child_requests
        return outputs, finished

    defobserve_num_generation_tokens(self, num_generation_tokens: int):
        self.max_num_generation_tokens = max(
            num_generation_tokens, self.max_num_generation_tokens
        )
        return self.max_num_generation_tokens

    @staticmethod
    defobserve_finished_request(
        parent_req: "ParentRequest | None",
        iteration_stats: IterationStats,
        num_generation_tokens: int,
    ):
        n_param = parent_req.n if parent_req is not None else 1

        if parent_req is not None:
            num_generation_tokens = parent_req.observe_num_generation_tokens(
                num_generation_tokens
            )

        # Child requests finished, we can now record to iteration stats
        if parent_req is None or not parent_req.child_requests:
            iteration_stats.max_num_generation_tokens_iter.append(num_generation_tokens)
            iteration_stats.n_params_iter.append(n_param)
```

### \_get\_child\_sampling\_params [¶](#vllm.v1.engine.parallel_sampling.ParentRequest._get_child_sampling_params "Permanent link")

Efficiently obtain child `sampling_params`

If `sampling_params.seed` is not `None` then each child request requires a unique clone of parent `sampling_params` with a unique seed.

Parameters:

Name Type Description Default `index` `int`

index within `n` child requests

*required*

Returns:

Type Description `SamplingParams`

Child `sampling_params` instance.

Source code in `vllm/v1/engine/parallel_sampling.py`

```
def_get_child_sampling_params(
    self,
    index: int,
) -> SamplingParams:
"""Efficiently obtain child `sampling_params`

    If `sampling_params.seed` is not `None` then
    each child request requires a unique clone of
    parent `sampling_params` with a unique seed.

    Args:
      index: index within `n` child requests

    Returns:
      Child `sampling_params` instance.
    """
    seed = self.sampling_params.seed
    if self.cached_child_sampling_params:
        # Reuse child sampling_params data structure
        return self.cached_child_sampling_params
    # Build child sampling_params
    child_sampling_params = copy(self.sampling_params)
    child_sampling_params.n = 1
    if seed is None:
        # Cache child sampling_params for later reuse
        self.cached_child_sampling_params = child_sampling_params
    else:
        # Each child gets a clone with a unique seed
        child_sampling_params.seed = seed + index
    return child_sampling_params
```

### get\_child\_info [¶](#vllm.v1.engine.parallel_sampling.ParentRequest.get_child_info "Permanent link")

Get child request ID and sampling params.

Parameters:

Name Type Description Default `index` `int`

index within `n` child requests.

*required*

Returns:

Type Description `tuple[str, SamplingParams]`

(request ID, sampling\_params) tuple

Source code in `vllm/v1/engine/parallel_sampling.py`

```
defget_child_info(self, index: int) -> tuple[str, SamplingParams]:
"""Get child request ID and sampling params.

    Args:
      index: index within `n` child requests.

    Returns:
      (request ID, sampling_params) tuple
    """
    child_req_id = f"{index}_{self.request_id}"
    self.child_requests.add(child_req_id)
    return child_req_id, self._get_child_sampling_params(index)
```