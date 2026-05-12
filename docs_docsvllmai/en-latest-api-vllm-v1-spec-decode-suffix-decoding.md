---
title: suffix_decoding - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/spec_decode/suffix_decoding/
source: sitemap
fetched_at: 2026-05-07T21:41:56.033590269-03:00
rendered_js: false
word_count: 67
summary: This document describes the SuffixDecodingProposer class, which implements speculative decoding for vLLM by utilizing suffix trees to generate dynamic token proposals.
tags:
    - vllm
    - speculative-decoding
    - suffix-decoding
    - llm-optimization
    - token-proposer
category: reference
---

## SuffixDecodingProposer [¶](#vllm.v1.spec_decode.suffix_decoding.SuffixDecodingProposer "Permanent link")

Speculative decoding proposer for Suffix Decoding (https://arxiv.org/pdf/2411.04975). This class imports and uses the official implementation from Arctic Inference (https://github.com/snowflakedb/ArcticInference).

Source code in `vllm/v1/spec_decode/suffix_decoding.py`

```
classSuffixDecodingProposer:
"""
    Speculative decoding proposer for Suffix Decoding (https://arxiv.org/pdf/2411.04975).
    This class imports and uses the official implementation from Arctic Inference
    (https://github.com/snowflakedb/ArcticInference).
    """

    def__init__(self, vllm_config: VllmConfig):
        config = vllm_config.speculative_config
        assert config is not None, "Speculative config must be set"
        self.num_speculative_tokens = config.num_speculative_tokens
        self.max_tree_depth = config.suffix_decoding_max_tree_depth
        self.max_spec_factor = config.suffix_decoding_max_spec_factor
        self.min_token_prob = config.suffix_decoding_min_token_prob
        self.max_model_len = vllm_config.model_config.max_model_len

        # Lazy import to avoid error when Suffix Decoding is not used.
        fromarctic_inference.suffix_decodingimport SuffixDecodingCache

        # Initialize and empty cache. This object will take care of caching request
        # outputs, evicting old requests, and manages the per-prompt suffix trees.
        self.suffix_cache = SuffixDecodingCache(
            max_tree_depth=config.suffix_decoding_max_tree_depth,
            max_cached_requests=config.suffix_decoding_max_cached_requests,
        )

    defpropose(
        self,
        input_batch: InputBatch,
        sampled_token_ids: list[list[int]],
        slot_mappings: dict[str, torch.Tensor]
        | list[dict[str, torch.Tensor]]
        | None = None,  # unused
    ) -> list[list[int]]:
"""
        Propose speculative tokens for each request in the input batch. Suffix Decoding
        will speculate a dynamic number of tokens for each request every decoding step,
        so each entry in the returned list may have different lengths.
        """
        draft_token_ids: list[list[int]] = []
        for i, sampled_ids in enumerate(sampled_token_ids):
            if not sampled_ids:
                # Skip speculative decoding for partial prefills.
                draft_token_ids.append([])
                continue

            req_id = input_batch.req_ids[i]
            num_tokens = input_batch.num_tokens_no_spec[i]
            if num_tokens >= self.max_model_len:
                # Skip requests that have already reached the max model length.
                draft_token_ids.append([])
                continue

            index = input_batch.req_id_to_index[req_id]
            if req_id not in self.suffix_cache.active_requests:
                if req_id in self.suffix_cache.cached_requests:
                    # Reset the suffix cache for this request.
                    self.suffix_cache.evict_cached_response(req_id)
                num_prompt_tokens = input_batch.num_prompt_tokens[index]
                prompt_token_ids = input_batch.token_ids_cpu[index, :num_prompt_tokens]
                # Start a new request, this will build the suffix tree for that prompt.
                self.suffix_cache.start_request(req_id, prompt_token_ids)

            # Append the newly sampled ids to the suffix cache for this request.
            self.suffix_cache.add_active_response(req_id, sampled_ids)

            # Suffix decoding only uses the most recent tokens up to max_tree_depth, so
            # we extract the pattern from the end of the input.
            start = max(0, num_tokens - self.max_tree_depth)
            pattern = input_batch.token_ids_cpu[i, start:num_tokens]
            draft = self.suffix_cache.speculate(
                req_id,
                pattern,
                max_spec_tokens=min(
                    self.num_speculative_tokens, self.max_model_len - num_tokens - 1
                ),
                max_spec_factor=self.max_spec_factor,
                min_token_prob=self.min_token_prob,
            )

            draft_token_ids.append(draft.token_ids)

        # Stop requests that were not seen in the input batch.
        for req_id in (
            self.suffix_cache.active_requests - input_batch.req_id_to_index.keys()
        ):
            self.suffix_cache.stop_request(req_id)

        return draft_token_ids

    defload_model(self, *args, **kwargs):
        # No model to load.
        pass
```

### propose [¶](#vllm.v1.spec_decode.suffix_decoding.SuffixDecodingProposer.propose "Permanent link")

Propose speculative tokens for each request in the input batch. Suffix Decoding will speculate a dynamic number of tokens for each request every decoding step, so each entry in the returned list may have different lengths.

Source code in `vllm/v1/spec_decode/suffix_decoding.py`

```
defpropose(
    self,
    input_batch: InputBatch,
    sampled_token_ids: list[list[int]],
    slot_mappings: dict[str, torch.Tensor]
    | list[dict[str, torch.Tensor]]
    | None = None,  # unused
) -> list[list[int]]:
"""
    Propose speculative tokens for each request in the input batch. Suffix Decoding
    will speculate a dynamic number of tokens for each request every decoding step,
    so each entry in the returned list may have different lengths.
    """
    draft_token_ids: list[list[int]] = []
    for i, sampled_ids in enumerate(sampled_token_ids):
        if not sampled_ids:
            # Skip speculative decoding for partial prefills.
            draft_token_ids.append([])
            continue

        req_id = input_batch.req_ids[i]
        num_tokens = input_batch.num_tokens_no_spec[i]
        if num_tokens >= self.max_model_len:
            # Skip requests that have already reached the max model length.
            draft_token_ids.append([])
            continue

        index = input_batch.req_id_to_index[req_id]
        if req_id not in self.suffix_cache.active_requests:
            if req_id in self.suffix_cache.cached_requests:
                # Reset the suffix cache for this request.
                self.suffix_cache.evict_cached_response(req_id)
            num_prompt_tokens = input_batch.num_prompt_tokens[index]
            prompt_token_ids = input_batch.token_ids_cpu[index, :num_prompt_tokens]
            # Start a new request, this will build the suffix tree for that prompt.
            self.suffix_cache.start_request(req_id, prompt_token_ids)

        # Append the newly sampled ids to the suffix cache for this request.
        self.suffix_cache.add_active_response(req_id, sampled_ids)

        # Suffix decoding only uses the most recent tokens up to max_tree_depth, so
        # we extract the pattern from the end of the input.
        start = max(0, num_tokens - self.max_tree_depth)
        pattern = input_batch.token_ids_cpu[i, start:num_tokens]
        draft = self.suffix_cache.speculate(
            req_id,
            pattern,
            max_spec_tokens=min(
                self.num_speculative_tokens, self.max_model_len - num_tokens - 1
            ),
            max_spec_factor=self.max_spec_factor,
            min_token_prob=self.min_token_prob,
        )

        draft_token_ids.append(draft.token_ids)

    # Stop requests that were not seen in the input batch.
    for req_id in (
        self.suffix_cache.active_requests - input_batch.req_id_to_index.keys()
    ):
        self.suffix_cache.stop_request(req_id)

    return draft_token_ids
```