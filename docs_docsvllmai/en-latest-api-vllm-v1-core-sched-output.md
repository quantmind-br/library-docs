---
title: output - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/core/sched/output/
source: sitemap
fetched_at: 2026-05-07T21:40:24.291015858-03:00
rendered_js: false
word_count: 42
summary: The CachedRequestData class defines a data structure for managing request scheduling states, including block management, token tracking, and phase identification within the vLLM scheduler.
tags:
    - vllm
    - scheduler
    - dataclass
    - request-management
    - token-tracking
    - scheduling-engine
category: reference
---

## CachedRequestData `dataclass` [¶](#vllm.v1.core.sched.output.CachedRequestData "Permanent link")

Source code in `vllm/v1/core/sched/output.py`

```
@dataclass
classCachedRequestData:
    req_ids: list[str]
    # For request ids not in resumed_req_ids, new_block_ids will be appended to
    # the request's block IDs. For those in the set, new_block_ids will be used as the
    # request's block IDs instead of appending to the existing block IDs.
    resumed_req_ids: set[str]
    # NOTE(woosuk): new_token_ids is only used for pipeline parallelism.
    # When PP is not used, new_token_ids will be empty.
    new_token_ids: list[list[int]]
    # For requests not scheduled in the last step, propagate the token ids to the
    # connector. Won't contain requests that were scheduled in the prior step.
    all_token_ids: dict[str, list[int]]
    new_block_ids: list[tuple[list[int], ...] | None]
    num_computed_tokens: list[int]
    num_output_tokens: list[int]

    # Version of dataclass repr with token IDs obfuscated.
    defanon_repr(self) -> str:
        new_token_ids_lens = [len(toks) for toks in self.new_token_ids]
        all_token_ids_lens = {
            req_id: len(toks) for req_id, toks in self.all_token_ids.items()
        }
        return (
            f"CachedRequestData("
            f"req_ids={self.req_ids},"
            f"resumed_req_ids={self.resumed_req_ids},"
            f"new_token_ids_lens={new_token_ids_lens},"
            f"all_token_ids_lens={all_token_ids_lens},"
            f"new_block_ids={self.new_block_ids},"
            f"num_computed_tokens={self.num_computed_tokens},"
            f"num_output_tokens={self.num_output_tokens}"
            f")"
        )

    def__repr__(self) -> str:
        return self.anon_repr()

    @property
    defnum_reqs(self) -> int:
        return len(self.req_ids)

    @cached_property
    def_req_id_to_num_output_tokens(self) -> dict[str, int]:
"""Cache mapping of req_id to num_output_tokens for O(1) lookup.

        This cached property is safe because CachedRequestData instances
        are created fresh each scheduling iteration and not mutated during
        computation of iteration details.
        """
        return dict(zip(self.req_ids, self.num_output_tokens))

    defis_context_phase(self, req_id: str) -> bool:
        num_output_tokens = self._req_id_to_num_output_tokens.get(req_id)
        return num_output_tokens is not None and num_output_tokens == 0

    @classmethod
    defmake_empty(cls) -> "CachedRequestData":
        return cls(
            req_ids=[],
            resumed_req_ids=set(),
            new_token_ids=[],
            all_token_ids={},
            new_block_ids=[],
            num_computed_tokens=[],
            num_output_tokens=[],
        )
```

### \_req\_id\_to\_num\_output\_tokens `cached` `property` [¶](#vllm.v1.core.sched.output.CachedRequestData._req_id_to_num_output_tokens "Permanent link")

Cache mapping of req\_id to num\_output\_tokens for O(1) lookup.

This cached property is safe because CachedRequestData instances are created fresh each scheduling iteration and not mutated during computation of iteration details.