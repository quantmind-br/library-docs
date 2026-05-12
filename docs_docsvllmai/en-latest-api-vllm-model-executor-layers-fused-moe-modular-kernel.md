---
title: modular_kernel - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/modular_kernel/
source: sitemap
fetched_at: 2026-05-07T21:25:02.103016452-03:00
rendered_js: false
word_count: 8
summary: This document defines a modular kernel implementation for Mixture of Experts (MoE) models, managing buffer allocation, input preparation, and expert execution, including support for asynchronous operations and shared experts.
tags:
    - moe
    - deep-learning
    - gpu-kernels
    - pytorch
    - memory-management
    - distributed-training
category: concept
---

```
@final
classFusedMoEKernelModularImpl:
    def__init__(
        self,
        prepare_finalize: FusedMoEPrepareAndFinalizeModular,
        fused_experts: FusedMoEExpertsModular,
        shared_experts: SharedExperts | None,
        inplace: bool = False,
    ):
        self.prepare_finalize = prepare_finalize
        self.fused_experts = fused_experts
        # Only accept shared experts if they can be run w/async.
        # The MoERunner/SharedExperts class will coordinate with the MK to ensure
        # that the SharedExperts are executed only once.
        self.shared_experts = (
            shared_experts if prepare_finalize.supports_async() else None
        )
        self.inplace = inplace
        moe_parallel_config = fused_experts.moe_config.moe_parallel_config
        self.moe_parallel_config = moe_parallel_config
        self.is_dp_ep = (
            moe_parallel_config is not None
            and moe_parallel_config.dp_size > 1
            and moe_parallel_config.use_ep
        )

    def_allocate_buffers(
        self,
        out_dtype: torch.dtype,
        device: torch.device,
        M_chunk: int,
        M_full: int,
        N: int,
        K: int,
        top_k: int,
        global_num_experts: int,
        local_num_experts: int,
        expert_tokens_meta: ExpertTokensMetadata | None,
        activation: MoEActivation,
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
"""
        Allocate temporary and output buffers for the fused experts op.
        Inputs:
        - out_dtype: output type of workspace and output tensors.
        - device: the device of the workspace and output tensors.
        See `workspace_shapes` for a description of the remainder of arguments.
        Returns a tuple of (workspace13, workspace2, output) tensors.
        """
        assert M_full > 0 and M_chunk > 0

        workspace_dtype = self.fused_experts.workspace_dtype(out_dtype)

        # Get intermediate workspace shapes based off the chunked M size.
        workspace13_shape, workspace2_shape, _ = self.fused_experts.workspace_shapes(
            M_chunk,
            N,
            K,
            top_k,
            global_num_experts,
            local_num_experts,
            expert_tokens_meta,
            activation,
        )

        # Get final output shape based on the full M size.
        _, _, fused_out_shape = self.fused_experts.workspace_shapes(
            M_full,
            N,
            K,
            top_k,
            global_num_experts,
            local_num_experts,
            expert_tokens_meta,
            activation,
        )

        # We can reuse the memory between cache1 and cache3 because by the
        # time we need cache3, we're done with cache1.
        # Reuse workspace13 for the output since there is only one chunk.
        max_shape_size = max(prod(workspace13_shape), prod(fused_out_shape))
        common_workspace, workspace2 = current_workspace_manager().get_simultaneous(
            ((max_shape_size,), workspace_dtype),
            (workspace2_shape, workspace_dtype),
        )
        workspace13 = _resize_cache(common_workspace, workspace13_shape)
        fused_out = _resize_cache(common_workspace, fused_out_shape)

        return workspace13, workspace2, fused_out

    def_maybe_apply_shared_experts(
        self,
        shared_experts_input: torch.Tensor | None,
    ):
        if self.shared_experts is not None:
            assert shared_experts_input is not None
            self.shared_experts.apply(
                shared_experts_input,
                SharedExpertsOrder.MK_INTERNAL_OVERLAPPED,
            )

    def_prepare(
        self,
        hidden_states: torch.Tensor,
        topk_weights: torch.Tensor,
        topk_ids: torch.Tensor,
        global_num_experts: int,
        expert_map: torch.Tensor | None,
        apply_router_weight_on_input: bool,
    ) -> tuple[
        torch.Tensor,
        torch.Tensor | None,
        ExpertTokensMetadata | None,
        torch.Tensor,
        torch.Tensor,
    ]:
"""
        The _prepare method is a wrapper around self.prepare_finalize.prepare
        that handles DBO and async.
        """
        if not self.prepare_finalize.supports_async():
            # We shouldn't be running an a2a kernel that doesn't
            # support async prepare/finalize
            # TODO(lucas): enable in follow-up
            assert not dbo_enabled()

            (
                a1q,
                a1q_scale,
                expert_tokens_meta,
                _expert_topk_ids,
                _expert_topk_weights,
            ) = self.prepare_finalize.prepare(
                hidden_states,
                topk_weights,
                topk_ids,
                global_num_experts,
                expert_map,
                apply_router_weight_on_input,
                self.fused_experts.quant_config,
                defer_input_quant=self.fused_experts.expects_unquantized_inputs,
            )
        else:
            # Overlap shared expert compute with all2all dispatch.
            dbo_maybe_run_recv_hook()
            prepare_ret = self.prepare_finalize.prepare_async(
                hidden_states,
                topk_weights,
                topk_ids,
                global_num_experts,
                expert_map,
                apply_router_weight_on_input,
                self.fused_experts.quant_config,
                defer_input_quant=self.fused_experts.expects_unquantized_inputs,
            )

            # TODO(lucas): refactor this in the alternative schedules followup
            # currently unpack if we have hook + receiver pair or just
            # receiver (see finalize_async docstring)
            hook, receiver = (
                prepare_ret if isinstance(prepare_ret, tuple) else (None, prepare_ret)
            )

            if hook is not None:
                if dbo_enabled():
                    # If DBO is being used, register the hook with the ubatch
                    # context and call it in dbo_maybe_run_recv_hook instead of
                    #  passing it to the receiver.
                    dbo_register_recv_hook(hook)
                    dbo_yield()
                else:
                    hook()

            (
                a1q,
                a1q_scale,
                expert_tokens_meta,
                _expert_topk_ids,
                _expert_topk_weights,
            ) = receiver()

        # Maybe prepare gathered topk_ids and topk_weights from other EP ranks.
        topk_ids = topk_ids if _expert_topk_ids is None else _expert_topk_ids
        topk_weights = (
            topk_weights if _expert_topk_weights is None else _expert_topk_weights
        )

        return a1q, a1q_scale, expert_tokens_meta, topk_ids, topk_weights

    def_fused_experts(
        self,
        in_dtype: torch.dtype,
        a1q: torch.Tensor,
        a1q_scale: torch.Tensor | None,
        w1: torch.Tensor,
        w2: torch.Tensor,
        topk_weights: torch.Tensor,
        topk_ids: torch.Tensor,
        activation: MoEActivation,
        global_num_experts: int,
        local_num_experts: int,
        expert_map: torch.Tensor | None,
        apply_router_weight_on_input: bool,
        expert_tokens_meta: ExpertTokensMetadata | None,
        output_alias: torch.Tensor | None = None,
    ) -> torch.Tensor:
        _, M_full, N, K, top_k = self.fused_experts.moe_problem_size(
            a1q, w1, w2, topk_ids
        )

        # This happens when none of the tokens from the all2all reach this
        # EP rank. Also, note that this is only relevant for CUDAGraph
        # incompatible all2all kernels like the DeepEP high-throughput
        # kernels. CUDAGraph compatible all2all kernels like the DeepEP
        # low-latency kernels are always batched and can never run into
        # the tensor.numel() == 0 case.
        if M_full == 0:
            return torch.empty_like(a1q, dtype=in_dtype)

        workspace13, workspace2, fused_out = self._allocate_buffers(
            in_dtype,
            a1q.device,
            M_full,
            M_full,
            N,
            K,
            top_k,
            global_num_experts,
            local_num_experts,
            expert_tokens_meta,
            activation,
        )

        # If caller's output buffer already matches fused_out shape/dtype, alias
        # to skip the redundant copy in TopKWeightAndReduceNoOP.apply downstream.
        # This eliminates ~94% of __amd_rocclr_copyBuffer events (Copy 2 of the
        # double-copy MoE write-back path).
        if current_platform.is_rocm():
            fromvllm._aiter_opsimport rocm_aiter_ops

            if (
                rocm_aiter_ops.is_fused_moe_enabled()
                and output_alias is not None
                and output_alias.shape == fused_out.shape
                and output_alias.dtype == fused_out.dtype
                and output_alias.device == fused_out.device
                and output_alias.is_contiguous()
            ):
                fused_out = output_alias

        self.fused_experts.apply(
            output=fused_out,
            hidden_states=a1q,
            w1=w1,
            w2=w2,
            topk_weights=topk_weights,
            topk_ids=topk_ids,
            activation=activation,
            global_num_experts=global_num_experts,
            expert_map=expert_map,
            a1q_scale=a1q_scale,
            a2_scale=self.fused_experts.a2_scale,
            workspace13=workspace13,
            workspace2=workspace2,
            expert_tokens_meta=expert_tokens_meta,
            apply_router_weight_on_input=apply_router_weight_on_input,
        )

        return fused_out

    def_finalize(
        self,
        output: torch.Tensor,
        fused_out: torch.Tensor,
        hidden_states: torch.Tensor,
        topk_weights: torch.Tensor,
        topk_ids: torch.Tensor,
        apply_router_weight_on_input: bool,
        shared_experts_input: torch.Tensor | None,
    ) -> torch.Tensor:
"""
        The _finalize method is a wrapper around self.prepare_finalize.finalize
        that handles DBO, async and shared expert overlap.

        Args:
            shared_experts_input: Optional separate input for shared experts.
                When latent MoE is used, hidden_states is the latent-projected
                tensor (smaller dimension) used by routed experts, while
                shared_experts_input is the original hidden_states (full
                dimension) needed by the shared expert MLP.
        """
        if not self.prepare_finalize.supports_async():
            assert not dbo_enabled()

            self.prepare_finalize.finalize(
                output,
                fused_out,
                topk_weights,
                topk_ids,
                apply_router_weight_on_input,
                self.fused_experts.finalize_weight_and_reduce_impl(),
            )
        else:
            finalize_ret = self.prepare_finalize.finalize_async(
                output,
                fused_out,
                topk_weights,
                topk_ids,
                apply_router_weight_on_input,
                self.fused_experts.finalize_weight_and_reduce_impl(),
            )
            self._maybe_apply_shared_experts(shared_experts_input)

            # TODO(lucas): refactor this in the alternative schedules followup
            # currently unpack if we have hook + receiver pair or just
            # receiver (see finalize_async docstring)
            hook, receiver = (
                finalize_ret
                if isinstance(finalize_ret, tuple)
                else (None, finalize_ret)
            )

            if hook is not None:
                if dbo_enabled():
                    # If DBO is being used, register the hook with the ubatch
                    # context and call it in dbo_maybe_run_recv_hook instead of
                    #  passing it to the receiver.
                    dbo_register_recv_hook(hook)
                    dbo_yield()
                else:
                    hook()

            receiver()

        return output

    defapply(
        self,
        hidden_states: torch.Tensor,
        w1: torch.Tensor,
        w2: torch.Tensor,
        topk_ids: torch.Tensor,
        topk_weights: torch.Tensor,
        activation: MoEActivation = MoEActivation.SILU,
        global_num_experts: int = -1,
        expert_map: torch.Tensor | None = None,
        apply_router_weight_on_input: bool = False,
        shared_experts_input: torch.Tensor | None = None,
    ) -> torch.Tensor:
"""
        This function computes a Mixture of Experts (MoE) layer using two sets
        of weights, w1 and w2, and top-k gating mechanism.

        Parameters:
        - hidden_states: (torch.Tensor): The input tensor to the MoE layer.
        - w1 (torch.Tensor): The first set of expert weights.
        - w2 (torch.Tensor): The second set of expert weights.
        - topk_weights (torch.Tensor): The topk weights applied at the end of the layer.
        - topk_ids (torch.Tensor): A map of row to expert id.
        - activation (MoEActivation): The activation function to apply after the first
          MoE layer.
        - global_num_experts (int): The total number of experts in the global
          expert space.
        - expert_map (Optional[torch.Tensor]):  A tensor mapping expert indices
          from the global expert space to the local expert space of the expert
          parallel shard.
        - apply_router_weight_on_input (bool): When true, the topk weights are
          applied directly on the inputs. This is only applicable when topk is
          1.
        - shared_experts_input (Optional[torch.Tensor]): Optional separate
          input for shared experts. For latent MoE, this is the original
          hidden_states before latent projection.

        Returns:
        - torch.Tensor: The output tensor after applying the MoE layer.
        """
        if self.inplace:
            assert self.shared_experts is None
            assert not disable_inplace()
            output = hidden_states
        else:
            output = torch.empty_like(hidden_states)

        local_num_experts = w1.shape[0]
        if global_num_experts == -1:
            global_num_experts = local_num_experts

        a1q, a1q_scale, expert_tokens_meta, topk_ids, topk_weights = self._prepare(
            hidden_states,
            topk_weights,
            topk_ids,
            global_num_experts,
            expert_map,
            apply_router_weight_on_input,
        )

        fused_out = self._fused_experts(
            in_dtype=hidden_states.dtype,
            a1q=a1q,
            a1q_scale=a1q_scale,
            w1=w1,
            w2=w2,
            topk_weights=topk_weights,
            topk_ids=topk_ids,
            activation=activation,
            global_num_experts=global_num_experts,
            local_num_experts=local_num_experts,
            expert_map=expert_map,
            apply_router_weight_on_input=apply_router_weight_on_input,
            expert_tokens_meta=expert_tokens_meta,
            output_alias=output,
        )

        return self._finalize(
            output,
            fused_out,
            hidden_states,
            topk_weights,
            topk_ids,
            apply_router_weight_on_input,
            shared_experts_input=shared_experts_input,
        )
```