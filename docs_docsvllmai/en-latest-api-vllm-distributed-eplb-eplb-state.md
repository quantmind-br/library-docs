---
title: eplb_state - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/eplb/eplb_state/
source: sitemap
fetched_at: 2026-05-07T21:17:56.847723926-03:00
rendered_js: false
word_count: 45
summary: This document defines the EplbState class, which manages the expert load balancing and physical-to-logical expert mapping state for distributed Mixture of Experts (MoE) models.
tags:
    - expert-parallelism
    - mixture-of-experts
    - load-balancing
    - distributed-training
    - pytorch-optimization
category: reference
---

```
classEplbState:
"""
    EplbState of each expert parallel model. Key is the model config hash.
    """

    def__init__(self, parallel_config: ParallelConfig, device: torch.device):
        self.parallel_config = parallel_config
        self.device = device
        self.model_states: dict[str, EplbModelState] = {}
        self.policy: type[AbstractEplbPolicy] = DefaultEplbPolicy
"""
        Selected EPLB algorithm class
        """
        self.expert_load_window_step: int = 0
"""
        Current step in the sliding window.

        Different from `expert_rearrangement_step`, 
        each EP rank may have its own `expert_load_window_step`.
        """
        self.expert_load_window_size: int = 0
"""
        Size of the expert load sliding window.
        This is a constant and is taken from the config.
        """
        self.expert_rearrangement_step: int = 0
"""
        Steps after last rearrangement.
        Will trigger a rearrangement if it exceeds the threshold.

        NOTE: Keep in mind that all EP ranks need to have the same
        `expert_rearrangement_step` value to ensure synchronization.
        Otherwise, the rearrangement will hang at collective
        communication calls.
        """
        self.expert_rearrangement_step_interval: int = 0
"""
        Interval for expert rearrangement steps.
        This is a constant and is taken from the config.
        """
        self.should_record_tensor: torch.Tensor | None = None
"""
        Shared scalar bool tensor for all layers.  Every
        :class:`EplbLayerState` holds a reference to the **same** object so
        a single ``.fill_()`` updates all layers at once.  Allocated on the
        first call to :meth:`_init_should_record_tensor`.
        """
        self.is_async: bool = False
"""
        The flag indicates whether the EPLB is running in async mode.
        """
        self.rearrange_event: CpuGpuEvent = CpuGpuEvent()
"""
        Event to signal when a new rearrangement is needed for the async thread.
        """
        self.async_worker: threading.Thread | None = None
"""
        Background thread handling async transfers.
        """
        self.cuda_device_index: int | None = None
"""
        CUDA device index for the async EPLB worker thread.
        """
        self.num_valid_physical_experts: int = 0
"""
        Number of valid physical experts.
        This is the number of physical experts that are
        actually mapped to logical experts. In elastic EP,
        newly started EP ranks may not have physical experts
        mapped yet.
        """
        if self.device.type == "cuda":
            self.cuda_device_index = self.device.index
            if self.cuda_device_index is None and torch.cuda.is_available():
                self.cuda_device_index = torch.accelerator.current_device_index()

    @staticmethod
    defbuild_initial_global_physical_to_logical_map(
        num_routed_experts: int,
        num_redundant_experts: int,
    ) -> Sequence[int]:
"""
        Build an initial expert arrangement using the following structure:
        [original routed experts, redundant experts]

        Returns:
            physical_to_logical_map (Sequence[int]): A list of integers,
                where each integer is the index of the logical expert
                that the corresponding physical expert maps to.
        """
        global_physical_to_logical_map = list(range(num_routed_experts))
        global_physical_to_logical_map += [
            i % num_routed_experts for i in range(num_redundant_experts)
        ]
        return global_physical_to_logical_map

    defvalidate_ep_configuration(self, new_model: MixtureOfExperts):
"""
        Validate that the expert parallel configuration of
        the new model is the same as the existing models.
        """
        if len(self.model_states) > 0:
            model = next(iter(self.model_states.values())).model
            if (
                model.num_routed_experts != new_model.num_routed_experts
                or model.num_redundant_experts != new_model.num_redundant_experts
                or model.num_physical_experts != new_model.num_physical_experts
                or model.num_logical_experts != new_model.num_logical_experts
                or model.num_expert_groups != new_model.num_expert_groups
            ):
                raise RuntimeError(
                    "Model: {} "
                    "with config {} "
                    "{}{}{}{} "
                    "mismatch with new model {} "
                    "with config {} "
                    "{}{}{}{}".format(
                        type(model),
                        model.num_routed_experts,
                        model.num_redundant_experts,
                        model.num_physical_experts,
                        model.num_logical_experts,
                        model.num_expert_groups,
                        type(new_model),
                        new_model.num_routed_experts,
                        new_model.num_redundant_experts,
                        new_model.num_physical_experts,
                        new_model.num_logical_experts,
                        new_model.num_expert_groups,
                    )
                )

    defadd_model(
        self,
        model: MixtureOfExperts,
        model_config: ModelConfig,
    ):
"""
        Build the initial EPLB state.
        """
        self.validate_ep_configuration(model)
        self.is_async = self.parallel_config.eplb_config.use_async

        physical_to_logical_map_list = (
            EplbState.build_initial_global_physical_to_logical_map(
                model.num_routed_experts,
                model.num_redundant_experts,
            )
        )
        physical_to_logical_map = torch.tensor(
            physical_to_logical_map_list,
            device=self.device,
        )
        # Assuming 8 GPUs per node, this supports up to
        # (1023 + 1) / 8 = 128 nodes for now.
        # TODO(rui): make this configurable
        MAX_EXPERT_REDUNDANCY = 1023
        assert model.num_redundant_experts <= MAX_EXPERT_REDUNDANCY, (
            f"num_redundant_experts {model.num_redundant_experts} "
            f"must be less than or equal to {MAX_EXPERT_REDUNDANCY}"
        )
        max_slots_per_logical_expert = MAX_EXPERT_REDUNDANCY + 1
        logical_to_physical_map = torch.full(
            (model.num_logical_experts, max_slots_per_logical_expert),
            -1,
            device=self.device,
        )
        logical_replica_count = torch.zeros(
            (model.num_logical_experts,),
            device=self.device,
            dtype=torch.long,
        )

        for i in range(model.num_physical_experts):
            logical_idx = physical_to_logical_map[i]
            logical_to_physical_map[logical_idx, logical_replica_count[logical_idx]] = i
            logical_replica_count[logical_idx] += 1

        # Duplicate initial mapping for all layers
        physical_to_logical_map = (
            physical_to_logical_map.unsqueeze(0)
            .expand(
                model.num_moe_layers,
                -1,
            )
            .contiguous()
        )
        logical_to_physical_map = (
            logical_to_physical_map.unsqueeze(0)
            .expand(
                model.num_moe_layers,
                -1,
                -1,
            )
            .contiguous()
        )
        logical_replica_count = (
            logical_replica_count.unsqueeze(0)
            .expand(
                model.num_moe_layers,
                -1,
            )
            .contiguous()
        )

        expert_load_pass = torch.zeros(
            (model.num_moe_layers, model.num_physical_experts),
            dtype=torch.int32,
            device=self.device,
        )
        self.expert_load_window_size = self.parallel_config.eplb_config.window_size
        expert_load_window = torch.zeros(
            (
                self.expert_load_window_size,
                model.num_moe_layers,
                model.num_physical_experts,
            ),
            dtype=torch.int32,
            device=self.device,
        )

        # Set the initial progress of rearrangement to 3/4
        eplb_step_interval = self.parallel_config.eplb_config.step_interval
        self.expert_rearrangement_step = max(
            0, eplb_step_interval - eplb_step_interval // 4
        )
        self.expert_rearrangement_step_interval = eplb_step_interval

        policy_type = self.parallel_config.eplb_config.policy
        self.policy = EPLB_POLICIES[policy_type]
        logger.debug("Selected EPLB policy: %s", policy_type)

        model.set_eplb_state(
            expert_load_pass,
            logical_to_physical_map,
            logical_replica_count,
        )
        self._init_should_record_tensor(model)
        expert_buffer = [torch.empty_like(w) for w in model.expert_weights[0]]

        communicator = create_eplb_communicator(
            group_coordinator=get_eplb_group(),
            backend=self.parallel_config.eplb_config.communicator,
            expert_weights=model.expert_weights[0],
        )

        model_state = EplbModelState(
            physical_to_logical_map=physical_to_logical_map,
            logical_to_physical_map=logical_to_physical_map,
            logical_replica_count=logical_replica_count,
            expert_load_pass=expert_load_pass,
            expert_load_window=expert_load_window,
            model_name=model_config.model,
            model=model,
            expert_buffer=expert_buffer,
            rebalanced=False,
            eplb_stats=None,
            cuda_device_index=self.cuda_device_index,
            communicator=communicator,
        )
        self.model_states[model_config.compute_hash()] = model_state
        self.num_valid_physical_experts = model.num_physical_experts

    defstep(
        self,
        is_dummy: bool = False,
        is_profile: bool = False,
        log_stats: bool = False,
    ) -> None:
"""
        Step the EPLB state.

        Args:
            is_dummy (bool): If `True`, this is a dummy step and the load
                metrics recorded in this forward pass will not count.
                Defaults to `False`.
            is_profile (bool): If `True`, perform a dummy rearrangement
                with maximum communication cost. This is used in
                `profile_run` to reserve enough memory
                for the communication buffer.
            log_stats (bool): If `True`, log the expert load metrics.

        # Stats
            The metrics are all summed up across layers.
            - `avg_tokens`: The average load across ranks.
            - `max_tokens`: The maximum load across ranks.
            - `balancedness`: The ratio of average load to maximum load.
        """
        ep_group = get_ep_group().device_group
        if is_profile:
            self.rearrange(is_profile=True)
            return

        if is_dummy:
            # Do not record load metrics for dummy steps
            for eplb_model_state in self.model_states.values():
                eplb_model_state.expert_load_pass.zero_()

        if (
            log_stats
            and self.expert_rearrangement_step
            % self.parallel_config.eplb_config.log_balancedness_interval
            == 0
        ):
            # Sync the expert load pass for each model (main and drafter).
            # expert_load_pass: (num_moe_layers, num_physical_experts)
            expert_load_pass_list = self._sync_load_pass()
            ep_group = get_ep_group().device_group
            for expert_load_pass, eplb_model_state in zip(
                expert_load_pass_list, self.model_states.values()
            ):
                # num_tokens_per_rank: (num_moe_layers, num_ranks)
                num_tokens_per_rank = (
                    expert_load_pass.reshape(
                        expert_load_pass.shape[0], ep_group.size(), -1
                    )
                    .sum(dim=-1)
                    .float()
                )

                # Compute balancedness ratio:
                # for each layer:
                #   (mean load across ranks) / (max load across ranks)
                avg_tokens_tensor = num_tokens_per_rank.mean(dim=0).sum(dim=0)
                max_tokens_tensor = num_tokens_per_rank.max(dim=0).values.sum(dim=0)

                # Just to make type checker happy
                tokens_tensors: list[float] = torch.stack(
                    [avg_tokens_tensor, max_tokens_tensor]
                ).tolist()
                avg_tokens, max_tokens = tokens_tensors
                balancedness = avg_tokens / max_tokens if max_tokens > 0 else 0.0

                if ep_group.rank() == 0:
                    logger.info(
                        "EPLB step: %d for model %s: avg_tokens=%.2f, "
                        "max_tokens=%d, balancedness=%.4f, "
                        "steps until the next rearrangement: %d",
                        self.expert_rearrangement_step,
                        eplb_model_state.model_name,
                        avg_tokens,
                        max_tokens,
                        balancedness,
                        self.expert_rearrangement_step_interval
                        - self.expert_rearrangement_step,
                    )

        # Update the expert load sliding window
        if not is_dummy:
            should_record = self._should_record_current_step(log_stats=log_stats)
            for eplb_model_state in self.model_states.values():
                if should_record:
                    eplb_model_state.expert_load_window[
                        self.expert_load_window_step
                    ].copy_(eplb_model_state.expert_load_pass)
                    eplb_model_state.expert_load_pass.zero_()

            if should_record:
                self.expert_load_window_step += 1
                if self.expert_load_window_step >= self.expert_load_window_size:
                    self.expert_load_window_step = 0

        # Step the expert rearrangement step
        # Note that even if this is a dummy step, we still increment the
        # rearrangement step and perform rearrangement to ensure all ranks are
        # performing collective communication.
        self.expert_rearrangement_step += 1

        if self.is_async:
            # Run _move_to_workspace if all ranks have finished transferring the
            # new weights to the intermediate buffer
            for eplb_model_state in self.model_states.values():
                # rebalanced must remain consistent amongst all ranks otherwise the
                # all_reduce in _all_ranks_result_ready will hang
                if eplb_model_state.rebalanced and self._all_ranks_result_ready(
                    eplb_model_state
                ):
                    _move_to_workspace(
                        model_state=eplb_model_state,
                        ep_rank=ep_group.rank(),
                    )

        if self.expert_rearrangement_step >= self.expert_rearrangement_step_interval:
            if self.is_async and any(
                eplb_model_state.rebalanced
                for eplb_model_state in self.model_states.values()
            ):
                # Still performing asynchronous rearrangement; update
                # should_record (step > step_interval, so always True) and
                # bail out before the step counter is reset.
                self._update_layer_should_record(log_stats=log_stats)
                return
            self.expert_rearrangement_step = 0
            self.rearrange()

        self._update_layer_should_record(log_stats=log_stats)

    def_should_record_current_step(self, log_stats: bool = False) -> bool:
"""Return whether expert-load recording should be enabled this step.

        Recording is enabled when we are close to either:
        1) The next rearrangement step, so the sliding window is ready.
        2) The next balancedness logging step, when log_stats is enabled.
        """
        steps_remaining = (
            self.expert_rearrangement_step_interval - self.expert_rearrangement_step
        )
        should_record_for_rearrange = steps_remaining <= self.expert_load_window_size

        if not log_stats:
            return should_record_for_rearrange

        log_interval = self.parallel_config.eplb_config.log_balancedness_interval
        steps_until_next_log = (
            log_interval - (self.expert_rearrangement_step % log_interval)
        ) % log_interval
        should_record_for_log = steps_until_next_log <= self.expert_load_window_size
        return should_record_for_rearrange or should_record_for_log

    def_update_layer_should_record(self, log_stats: bool = False) -> None:
"""Update the shared ``should_record_tensor`` for all layers."""
        if self.should_record_tensor is not None:
            self.should_record_tensor.fill_(
                self._should_record_current_step(log_stats=log_stats)
            )

    def_init_should_record_tensor(self, model: "MixtureOfExperts") -> None:  # type: ignore[name-defined]
"""Allocate (once) and propagate the shared ``should_record_tensor``.

        Must be called after :meth:`model.set_eplb_state` so that each
        layer's ``eplb_state`` is already populated with the tensor views.
        """
        layer_states = [
            layer.eplb_state
            for layer in model.moe_layers
            if hasattr(layer, "eplb_state")
            and isinstance(layer.eplb_state, EplbLayerState)
        ]

        if self.should_record_tensor is None and layer_states:
            self.should_record_tensor = torch.ones(
                (), dtype=torch.bool, device=self.device
            )

        for ls in layer_states:
            ls.should_record_tensor = self.should_record_tensor

    defrearrange(
        self,
        is_profile: bool = False,
        rank_mapping: dict[int, int] | None = None,
    ) -> torch.Tensor | None:
"""
        Rearrange the experts according to the current load.

        Args:
            is_profile (bool): If `True`, perform a dummy rearrangement.
                This is used in `profile_run` to reserve enough memory,
                no memory movement will be performed. Default is False.
            rank_mapping (dict[int, int] | None): The rank mapping
                when scaling is done in EEP.
        """

        ep_group = get_ep_group().device_group
        ep_rank = ep_group.rank()

        start_event = None
        end_event = None
        is_main_rank = ep_rank == 0
        if is_main_rank:
            if not self.is_async or is_profile:
                start_event = torch.cuda.Event(enable_timing=True)
                end_event = torch.cuda.Event(enable_timing=True)
                start_event.record()
            logger.info(
                "Rearranging experts %s%s...",
                "(async mode)" if self.is_async else "sync mode",
                "(profile)" if is_profile else "",
            )

        # Map the physical expert load to global logical experts
        global_expert_load_windows = []
        for eplb_model_state in self.model_states.values():
            expert_load_window = eplb_model_state.expert_load_window[
                :, :, : self.num_valid_physical_experts
            ]
            logical_expert_load_window = torch.zeros(
                self.expert_load_window_size,
                eplb_model_state.model.num_moe_layers,
                eplb_model_state.model.num_logical_experts,
                dtype=eplb_model_state.expert_load_window.dtype,
                device=eplb_model_state.expert_load_window.device,
            )
            logical_expert_load_window.scatter_add_(
                dim=-1,
                index=eplb_model_state.physical_to_logical_map[
                    :, : self.num_valid_physical_experts
                ]
                .unsqueeze(0)
                .expand_as(expert_load_window)
                .long(),
                src=expert_load_window,
            )

            global_expert_load_window = logical_expert_load_window.sum(dim=0)
            global_expert_load_windows.append(global_expert_load_window)
        # Perform all-reduce to get the expert load across all ranks for each model
        global_expert_load_windows = self._allreduce_list(global_expert_load_windows)

        # TODO(bowen): Treat differently for prefill and decode nodes
        eplb_model_state = next(iter(self.model_states.values()))
        model = eplb_model_state.model
        num_replicas = model.num_physical_experts
        num_groups = model.num_expert_groups

        if rank_mapping is not None and len(rank_mapping) == ep_group.size():
            # NOTE(yongji): scale down, we need to rebalance the experts on
            # remaining GPUs, transfer the experts while we haven't shutdown
            # the GPUs to be released.
            coordinator = get_ep_group()
            assert isinstance(coordinator, StatelessGroupCoordinator)
            tcp_store_group = coordinator.tcp_store_group
            num_nodes = _node_count_with_rank_mapping(tcp_store_group, rank_mapping)
            num_gpus = sum(new_rank != -1 for new_rank in rank_mapping.values())
            num_replicas = (
                num_replicas // ep_group.size() * num_gpus
            )  # handle num replicas change
        else:
            num_nodes = get_node_count()
            num_gpus = ep_group.size()

        if num_gpus % num_nodes != 0:
            num_nodes = 1
            logger.warning_once(
                f"num_gpus % num_nodes != 0, "
                "not using hierarchical rearrangement algorithm.\n"
                f"{num_gpus=}, {num_nodes=}"
            )

        # Get new expert mappings
        for eplb_model_state, global_expert_load_window in zip(
            self.model_states.values(), global_expert_load_windows
        ):
            if not self.is_async or is_profile:
                # Get new expert mappings for the model
                new_physical_to_logical_map = self.policy.rebalance_experts(
                    global_expert_load_window.cpu(),
                    num_replicas,
                    num_groups,
                    num_nodes,
                    num_gpus,
                    eplb_model_state.physical_to_logical_map.cpu(),
                )

                # Update expert weights
                rearrange_expert_weights_inplace(
                    eplb_model_state.physical_to_logical_map,
                    new_physical_to_logical_map,
                    eplb_model_state.model.expert_weights,
                    ep_group,
                    eplb_model_state.communicator,
                    is_profile,
                    rank_mapping,
                )

                if not is_profile:
                    _commit_eplb_maps(
                        eplb_model_state,
                        new_physical_to_logical_map=new_physical_to_logical_map,
                    )

                if is_main_rank:
                    assert start_event is not None
                    assert end_event is not None
                    end_event.record()
                    end_event.synchronize()
                    gpu_elapsed = start_event.elapsed_time(end_event) / 1000.0
                    logger.info(
                        "Rearranged experts %s in %.2f s.",
                        " (profile) " if is_profile else " ",
                        gpu_elapsed,
                    )
            else:
                eplb_model_state.eplb_stats = EplbStats(
                    # We copy the tensor to snapshot the global_expert_load_window
                    # on the main thread so that async worker can access it safely
                    # while the main thread is running.
                    global_expert_load_window=global_expert_load_window.clone(),
                    num_replicas=num_replicas,
                    num_groups=num_groups,
                    num_nodes=num_nodes,
                    num_gpus=num_gpus,
                )
                eplb_model_state.rebalanced = True
        # Signal async thread to start transferring layers
        if self.is_async and (not is_profile):
            self.rearrange_event.record()
        return None

    defstart_async_loop(
        self,
        rank_mapping: dict[int, int] | None = None,
        is_profile: bool = False,
    ):
        if not self.is_async:
            return
        if self.async_worker is None:
            self.async_worker = start_async_worker(
                self,
                is_profile=is_profile,
            )

    def_all_ranks_result_ready(self, model_state: EplbModelState) -> bool:
        parallel_state = get_ep_group()
        has_result = int(model_state.pending_result is not None)

        cpu_group = getattr(parallel_state, "cpu_group", None)
        if cpu_group is not None and cpu_group.size() > 1:
            flag = torch.tensor((has_result,), dtype=torch.int32, device="cpu")
            all_reduce(flag, group=cpu_group)
            return int(flag.item()) == cpu_group.size()

        device_group = parallel_state.device_group
        if device_group.size() <= 1:
            return bool(has_result)

        device = getattr(
            parallel_state, "device", model_state.physical_to_logical_map.device
        )
        flag = torch.tensor((has_result,), dtype=torch.int32, device=device)
        all_reduce(flag, group=device_group)
        return int(flag.item()) == device_group.size()

    def_allreduce_list(self, tensor_list: list[torch.Tensor]) -> list[torch.Tensor]:
"""
        All-reduce a list of tensors.
        """
        if len(tensor_list) == 1:
            all_reduce(tensor_list[0], group=get_ep_group().device_group)
            return tensor_list
        assert all(t.dim() == 2 for t in tensor_list), "All tensors must be 2D."
        assert all(t.shape[1] == tensor_list[0].shape[1] for t in tensor_list), (
            "All tensors must have the same shape[1]."
        )
        # Concatenate, all_reduce, then unpack to original shapes.
        # We assume all tensors are 2D and shape[1] (num_physical_experts)
        # is the same across all models.
        shapes = [t.shape for t in tensor_list]
        concat_tensor = torch.cat(tensor_list, dim=0)

        ep_group = get_ep_group().device_group
        all_reduce(concat_tensor, group=ep_group)

        all_reduce_list = []
        offset = 0
        for shape in shapes:
            all_reduce_list.append(concat_tensor[offset : offset + shape[0], :])
            offset += shape[0]
        return all_reduce_list

    def_sync_load_pass(self) -> list[torch.Tensor]:
"""
        Sync the expert load pass across all ranks for log stats.
        Doesn't update the expert load pass in eplb_model_state.
        """
        load_pass_list = []
        for eplb_model_state in self.model_states.values():
            load_pass_list.append(eplb_model_state.expert_load_pass.clone())
        return self._allreduce_list(load_pass_list)

    @classmethod
    deffrom_mapping(
        cls,
        model: MixtureOfExperts,
        model_config: ModelConfig,
        device: torch.device,
        parallel_config: ParallelConfig,
        expanded_physical_to_logical: torch.Tensor,
        num_valid_physical_experts: int,
    ) -> "EplbState":
        eplb_state = cls(
            parallel_config=parallel_config,
            device=device,
        )
        eplb_state.add_model(
            model=model,
            model_config=model_config,
        )
        eplb_state.num_valid_physical_experts = num_valid_physical_experts
        eplb_model_state = eplb_state.model_states[model_config.compute_hash()]
        eplb_model_state.physical_to_logical_map.copy_(expanded_physical_to_logical)

        (logical_to_physical_map_cpu, logical_replica_count_cpu) = compute_logical_maps(
            expanded_physical_to_logical.cpu(), model.num_logical_experts
        )

        max_num_replicas = eplb_model_state.logical_to_physical_map.shape[-1]
        num_replicas = logical_to_physical_map_cpu.shape[-1]
        logical_to_physical_map = torch.nn.functional.pad(
            logical_to_physical_map_cpu,
            (
                0,
                max_num_replicas - num_replicas,
            ),
            value=-1,
        ).to(device)
        logical_replica_count = logical_replica_count_cpu.to(device)

        eplb_model_state.logical_to_physical_map.copy_(logical_to_physical_map)
        eplb_model_state.logical_replica_count.copy_(logical_replica_count)

        return eplb_state
```