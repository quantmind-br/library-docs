---
title: ngram_proposer_gpu - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/spec_decode/ngram_proposer_gpu/
source: sitemap
fetched_at: 2026-05-07T21:41:55.660275224-03:00
rendered_js: false
word_count: 6
summary: This document defines the NgramProposerGPU class, which implements GPU-accelerated n-gram matching for speculative decoding in LLM inference pipelines.
tags:
    - speculative-decoding
    - ngram-matching
    - gpu-optimization
    - vllm
    - torch-kernels
    - inference-optimization
category: concept
---

```
classNgramProposerGPU:
    def__init__(self, vllm_config: VllmConfig, device: torch.device, runner=None):
        assert vllm_config.speculative_config is not None
        assert vllm_config.speculative_config.prompt_lookup_min is not None
        assert vllm_config.speculative_config.prompt_lookup_max is not None

        compilation_config = CompilationConfig(
            mode=CompilationMode.VLLM_COMPILE,
            custom_ops=["none"],
            splitting_ops=[],
            compile_sizes=[],
            inductor_compile_config={
                "enable_auto_functionalized_v2": False,
                "max_autotune": True,
                "aggressive_fusion": True,
                "triton.autotune_pointwise": True,
                "coordinate_descent_tuning": True,
                "use_mixed_mm": False,
            },
            cudagraph_mode=CUDAGraphMode.NONE,
        )
        model_config = vllm_config.model_config
        speculative_config = vllm_config.speculative_config
        scheduler_config = vllm_config.scheduler_config

        self.vllm_config = VllmConfig(
            compilation_config=compilation_config,
            model_config=model_config,
            speculative_config=speculative_config,
            scheduler_config=scheduler_config,
        )

        self.min_n = vllm_config.speculative_config.prompt_lookup_min
        self.max_n = vllm_config.speculative_config.prompt_lookup_max
        self.k = vllm_config.speculative_config.num_speculative_tokens
        self.max_model_len = vllm_config.model_config.max_model_len
        self.max_num_seqs = vllm_config.scheduler_config.max_num_seqs
        self.device = device

        self.kernel = NgramGPUKernel(
            vllm_config=self.vllm_config, prefix="ngram_gpu_kernel", device=device
        )
        self.kernel.to(device)
        self.kernel.eval()

        self._dummy_run()

    def_dummy_run(self):
        token_ids, num_tokens, sampled_flags, valid_mask = self._generate_dummy_data(
            batch_size=self.max_num_seqs,
            max_seq_len=self.max_model_len,
            pattern_len=self.k,
            device=self.device,
        )

        combined_mask = sampled_flags & valid_mask & (num_tokens >= self.min_n)

        for _ in range(3):
            with set_forward_context(None, self.vllm_config):
                _, _ = self.kernel(num_tokens, token_ids, combined_mask)

    def_generate_dummy_data(
        self,
        batch_size: int,
        max_seq_len: int,
        pattern_len: int,
        device: str = "cuda",
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
"""
        Generate random test data with n-gram repetitions.

        Args:
            batch_size: Number of sequences in the batch
            max_seq_len: Maximum sequence length
            pattern_len: Length of patterns to inject for matching
            device: Device to place tensors on

        Returns:
            token_ids: [batch_size, max_seq_len] tensor
            num_tokens: [batch_size] tensor
            sampled_flags: [batch_size] bool tensor
            valid_mask: [batch_size] bool tensor
        """
        token_ids = torch.zeros(
            batch_size,
            max_seq_len,
            dtype=torch.int32,
            device=device,
        )

        num_tokens = torch.randint(
            pattern_len, max_seq_len, (batch_size,), dtype=torch.int32, device=device
        )

        sampled_flags = torch.ones(batch_size, dtype=torch.bool, device=device)
        valid_mask = torch.ones(batch_size, dtype=torch.bool, device=device)

        return token_ids, num_tokens, sampled_flags, valid_mask

    defpropose(
        self,
        num_tokens_no_spec: torch.Tensor,  # [batch_size]
        token_ids_gpu: torch.Tensor,  # [batch_size, max_len]
        valid_sampled_token_ids_gpu: torch.Tensor,  # [batch_size, num_spec_tokens + 1]
        valid_sampled_tokens_count: torch.Tensor,  # [batch_size]
    ) -> tuple[torch.Tensor, torch.Tensor]:
"""
        Propose draft tokens using GPU-accelerated n-gram matching.

        Scatter sampled tokens into `token_ids_gpu`, compute temporary
        updated lengths, then run the kernel.

        Args:
            num_tokens_no_spec: Number of tokens per sequence (read-only)
            token_ids_gpu: Token IDs tensor (modified in-place with new tokens)
            valid_sampled_token_ids_gpu: Newly sampled tokens to scatter
            valid_sampled_tokens_count: Count of valid tokens per sequence

        Returns:
            draft_tokens: Proposed draft token IDs [batch_size, k]
            num_valid_draft_tokens: Count of leading valid draft tokens
                per request [batch_size]
        """
        assert token_ids_gpu.device == self.device
        assert num_tokens_no_spec.device == self.device

        batch_size = num_tokens_no_spec.shape[0]
        max_seq_len = token_ids_gpu.shape[1]
        max_new_tokens = valid_sampled_token_ids_gpu.shape[1]  # num_spec_tokens + 1

        # Scatter newly sampled tokens into token_ids_gpu.
        offsets = torch.arange(max_new_tokens, device=self.device)
        write_positions = num_tokens_no_spec.unsqueeze(1) + offsets.unsqueeze(0)
        valid_write_mask = offsets.unsqueeze(0) < valid_sampled_tokens_count.unsqueeze(
            1
        )
        in_bounds = write_positions < max_seq_len
        scatter_mask = (
            valid_write_mask & (valid_sampled_token_ids_gpu != -1) & in_bounds
        )

        write_positions_long = write_positions.clamp(max=max_seq_len - 1).long()
        existing_values = token_ids_gpu.gather(1, write_positions_long)

        tokens_cast = valid_sampled_token_ids_gpu.to(token_ids_gpu.dtype)
        tokens_to_scatter = torch.where(
            scatter_mask,
            tokens_cast,
            existing_values,
        )
        token_ids_gpu.scatter_(1, write_positions_long, tokens_to_scatter)

        num_tokens_tmp = (num_tokens_no_spec + valid_sampled_tokens_count).to(
            torch.int32
        )

        # Compute validity masks.
        sampled_flags = valid_sampled_tokens_count > 0
        valid_mask = torch.ones(batch_size, dtype=torch.bool, device=self.device)

        with set_forward_context(None, self.vllm_config):
            combined_mask = sampled_flags & valid_mask & (num_tokens_tmp >= self.min_n)

            with record_function_or_nullcontext("ngram_proposer_gpu: kernel"):
                draft_tokens, num_valid_draft_tokens = self.kernel(
                    num_tokens_tmp,
                    token_ids_gpu,
                    combined_mask,
                )

            return draft_tokens, num_valid_draft_tokens

    defupdate_token_ids_ngram(
        self,
        sampled_token_ids: torch.Tensor | list[list[int]],
        gpu_input_batch: InputBatch,
        token_ids_gpu: torch.Tensor,
        num_tokens_no_spec: torch.Tensor,
        discard_request_mask: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
"""
        Prepare speculative decoding inputs on device:
        compute next token ids and valid counts, honoring discarded requests
        and rejected tokens, without CPU-GPU sync.
        """
        num_reqs = gpu_input_batch.num_reqs

        if isinstance(sampled_token_ids, list):
            # When disable_padded_drafter_batch=True, sampled_token_ids is
            # an irregular list[list[int]] where sublists may have different
            # lengths (including empty lists for discarded requests).
            # Pad all sublists to the same length with -1 before converting
            # to tensor.
            max_len = max(
                (len(sublist) for sublist in sampled_token_ids),
                default=0,
            )
            # Ensure at least length 1 for tensor creation
            max_len = max(max_len, 1)
            padded_list = [
                sublist + [-1] * (max_len - len(sublist))
                for sublist in sampled_token_ids
            ]
            sampled_token_ids = torch.tensor(
                padded_list, dtype=torch.int32, device=self.device
            )
        assert isinstance(sampled_token_ids, torch.Tensor), (
            "sampled_token_ids should be a torch.Tensor for ngram_gpu"
        )

        # Backup last valid token before speculative tokens.
        backup_indices = (num_tokens_no_spec[:num_reqs] - 1).clamp(min=0).long()
        backup_next_token_ids = torch.gather(
            token_ids_gpu[:num_reqs], dim=1, index=backup_indices.unsqueeze(1)
        ).squeeze(1)

        valid_sampled_token_ids_gpu = sampled_token_ids.clone()
        # Invalidate sampled tokens for discarded requests.
        discard_mask_expanded = discard_request_mask[:num_reqs].unsqueeze(1)
        valid_sampled_token_ids_gpu.masked_fill_(discard_mask_expanded, -1)

        # Mask valid tokens within each request.
        valid_mask = (valid_sampled_token_ids_gpu != -1) & (
            valid_sampled_token_ids_gpu < gpu_input_batch.vocab_size
        )

        # Count valid tokens per request.
        valid_sampled_tokens_count = valid_mask.sum(dim=1).to(torch.int32)

        # Rightmost valid index per row.
        last_valid_indices = valid_sampled_tokens_count - 1
        last_valid_indices_safe = torch.clamp(last_valid_indices, min=0)

        # Last valid token from each row; undefined if none.
        selected_tokens = torch.gather(
            valid_sampled_token_ids_gpu, 1, last_valid_indices_safe.unsqueeze(1)
        ).squeeze(1)

        # Use last token if valid; otherwise fallback to backup.
        next_token_ids = torch.where(
            last_valid_indices != -1,
            selected_tokens,
            backup_next_token_ids,
        )

        return next_token_ids, valid_sampled_tokens_count, valid_sampled_token_ids_gpu

    defload_model(self, *args, **kwargs):
        self.kernel.load_model(*args, **kwargs)
```