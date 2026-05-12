---
title: gritlm - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/gritlm/
source: sitemap
fetched_at: 2026-05-07T21:30:41.902098245-03:00
rendered_js: false
word_count: 12
summary: This code implements a custom sequence pooling method that calculates the mean of hidden states while excluding specific instruction tokens identified via pattern matching in prompt sequences.
tags:
    - sequence-pooling
    - nlp
    - token-matching
    - machine-learning
    - pytorch
    - embedding-optimization
category: api
---

```
classGritLMMeanPool(SequencePoolingMethod):
"""As `MeanPool`, but only includes non-instruction tokens."""

    def__init__(self, model_config: ModelConfig):
        super().__init__()

        self.model_config = model_config

        tokenizer = cached_tokenizer_from_config(self.model_config)

        # Collect the tokens needed for pattern matching.
        # "▁<" is different from "_<". The former uses "▁" to indicate that
        # the next token is the start of a word.
        # "<0x0A>" is the newline token (i.e. "\n")."
        self.token_ids = {
            tok: tokenizer.convert_tokens_to_ids([tok])[0]
            for tok in ["<s>", "▁<", "<", "|", "embed", ">", "<0x0A>", "user"]
        }

        deftokens_to_ids(tokens: list[str]) -> np.ndarray:
            return np.array([self.token_ids[token] for token in tokens])

        self.user_pattern_ids = tokens_to_ids(["▁<", "|", "user", "|", ">", "<0x0A>"])
        self.embed_newline_pattern_ids = tokens_to_ids(
            ["<0x0A>", "<", "|", "embed", "|", ">", "<0x0A>"]
        )
        self.embed_pattern_ids = tokens_to_ids(["▁<", "|", "embed", "|", ">", "<0x0A>"])

    def_find_array(
        self,
        arr: np.ndarray,
        target: np.ndarray,
        start_idx: int = 0,
        end_idx: int | None = None,
    ) -> int:
"""
        Find the first occurrence of `target` in `arr` starting from
        `start_idx`.

        Args:
            arr: The array to search within.
            target: The consecutive subsequence to find.
            start_idx: The starting index to search from (inclusive).
            end_idx: The ending index to search from (exclusive).

        Returns:
            The index of the first occurrence of `target` in `arr`.
        """
        if start_idx < 0:
            raise ValueError("`start_idx` must be non-negative")
        if len(arr) == 0 or len(target) == 0:
            raise ValueError("Empty `arr` or `target` not allowed")

        arr_len = len(arr)
        target_len = len(target)

        if end_idx is None:
            end_idx = arr_len

        for i in range(start_idx, min(end_idx, arr_len - target_len + 1)):
            if (arr[i : i + target_len] == target).all():
                return i

        return -1

    def_get_instruction_len(self, prompt_token_ids: np.ndarray) -> int:
"""
        Get the length of the instruction in the prompt.

        We do a pattern matching to find the instruction in the prompt,
        and then return the length of the instruction.

        The pattern matching is done using integers instead of strings
        because the prompt is given as a list of token IDs.
        """
        instruction_len = 0

        # Return no instruction in case of missing BOS token.
        if prompt_token_ids[0] != self.token_ids["<s>"]:
            logger.warning(
                "BOS token not found in prompt, "
                "thus using empty string for instruction. "
                "GritLM requires BOS token in prompt."
            )
            return instruction_len

        # If user pattern is found in the prompt, that means there should be
        # a newline token before the embed pattern.
        embed_pattern_ids = self.embed_pattern_ids
        if (
            self._find_array(
                prompt_token_ids, self.user_pattern_ids, start_idx=1, end_idx=2
            )
            == 1
        ):
            embed_pattern_ids = self.embed_newline_pattern_ids

        # Find the embed pattern in the prompt.
        found_embed_pattern_idx = self._find_array(
            prompt_token_ids, embed_pattern_ids, start_idx=1
        )

        if found_embed_pattern_idx != -1:
            instruction_len = found_embed_pattern_idx + len(embed_pattern_ids)
        else:
            logger.warning(
                "Query instruction not found in prompt, "
                "thus using BOS token as instruction instead. "
                "GritLM requires query instruction in prompt."
            )
            instruction_len = 1

        return instruction_len

    defget_supported_tasks(self) -> Set[PoolingTask]:
        return {"embed"}

    defget_pooling_updates(self, task: PoolingTask) -> PoolingParamsUpdate:
        return PoolingParamsUpdate(requires_token_ids=True)

    defforward(
        self,
        hidden_states: torch.Tensor,
        pooling_metadata: PoolingMetadata,
    ) -> SequencePoolingMethodOutput:
        prompt_lens = pooling_metadata.prompt_lens
        prompt_token_ids = pooling_metadata.get_prompt_token_ids_cpu()
        instr_lens = torch.tensor(
            [
                self._get_instruction_len(token_ids.numpy())
                for token_ids in prompt_token_ids
            ],
            device="cpu",
        )

        offset = 0
        pooled_data = list[torch.Tensor]()
        for prompt_len, instr_len in zip(prompt_lens, instr_lens):
            pooled_data.append(
                hidden_states[offset + instr_len : offset + prompt_len].mean(
                    dim=0, dtype=torch.float32
                )
            )
            offset += prompt_len

        return pooled_data
```