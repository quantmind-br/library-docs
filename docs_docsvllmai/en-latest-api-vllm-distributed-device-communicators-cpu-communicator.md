---
title: cpu_communicator - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/device_communicators/cpu_communicator/
source: sitemap
fetched_at: 2026-05-07T21:17:29.081380433-03:00
rendered_js: false
word_count: 8
summary: This document defines the CpuCommunicator class, which manages distributed communication operations for CPU-based tensor processing, including fallback mechanisms to shared memory backends.
tags:
    - pytorch
    - distributed-computing
    - cpu-communication
    - shared-memory
    - tensor-processing
    - parallel-computing
category: reference
---

```
classCpuCommunicator(DeviceCommunicatorBase):
    def__init__(
        self,
        cpu_group: ProcessGroup,
        device: torch.device | None = None,
        device_group: ProcessGroup | None = None,
        unique_name: str = "",
    ):
        super().__init__(cpu_group, device, device_group, unique_name)
        self.dist_module = torch.distributed

        if (
            (
                current_platform.get_cpu_architecture() == CpuArchEnum.X86
                or current_platform.get_cpu_architecture() == CpuArchEnum.ARM
            )
            and hasattr(torch.ops._C, "init_shm_manager")
            and (unique_name.startswith("tp") or unique_name.startswith("pp"))
            and self._all_group_ranks_share_shm_group_name()
        ):
            self.dist_module = _CPUSHMDistributed(self)
        elif unique_name.startswith("tp") or unique_name.startswith("pp"):
            logger.info(
                "CPU SHM communicator disabled for group %s: ranks do not share "
                "the same SHM group name, falling back to torch.distributed.",
                unique_name,
            )

        # send/recv tensor_dict is only supported through the SHM communicator backend
        self.supports_tensor_dict = isinstance(self.dist_module, _CPUSHMDistributed)

        if self.use_all2all:
            if self.all2all_backend not in (
                "naive",
                "allgather_reducescatter",
            ):  # type: ignore[has-type]
                logger.warning(
                    "`%s` all2all manager is not supported on CPU. "
                    "Falling back to `allgather_reducescatter` manager.",
                    self.all2all_backend,  # type: ignore[has-type]
                )
            from.all2allimport AgRsAll2AllManager

            self.all2all_manager = AgRsAll2AllManager(self.cpu_group)
            logger.info("Using allgather_reducescatter all2all manager.")

    def_all_group_ranks_share_shm_group_name(self) -> bool:
"""
        CPUSHM requires all ranks in this group to agree on one SHM group name.
        This is a lightweight consistency check for VLLM_DIST_IDENT/name inputs.
        """
        local_name = _CPUSHMDistributed.make_group_name(self)
        names: list[str] = [""] * self.world_size
        torch.distributed.all_gather_object(
            names,
            local_name,
            group=self.device_group,
        )
        return len(set(names)) == 1

    defall_reduce(self, input_):
        self.dist_module.all_reduce(input_, group=self.device_group)
        return input_

    defgather(
        self, input_: torch.Tensor, dst: int = 0, dim: int = -1
    ) -> torch.Tensor | None:
"""
        NOTE: We assume that the input tensor is on the same device across
        all the ranks.
        NOTE: `dst` is the local rank of the destination rank.
        """
        world_size = self.world_size
        assert -input_.dim() <= dim < input_.dim(), (
            f"Invalid dim ({dim}) for input tensor with shape {input_.size()}"
        )
        if dim < 0:
            # Convert negative dim to positive.
            dim += input_.dim()

        # Allocate output tensor.
        if self.rank_in_group == dst:
            gather_list = [torch.empty_like(input_) for _ in range(world_size)]
        else:
            gather_list = None

        # Gather.
        self.dist_module.gather(
            input_, gather_list, dst=self.ranks[dst], group=self.device_group
        )

        if self.rank_in_group == dst:
            output_tensor = torch.cat(gather_list, dim=dim)
        else:
            output_tensor = None
        return output_tensor

    defall_gather(self, input_: torch.Tensor, dim: int = -1) -> torch.Tensor:
        if dim < 0:
            # Convert negative dim to positive.
            dim += input_.dim()
        input_size = input_.size()
        # NOTE: we have to use concat-style all-gather here,
        # stack-style all-gather has compatibility issues with
        # torch.compile . see https://github.com/pytorch/pytorch/issues/138795
        output_size = (input_size[0] * self.world_size,) + input_size[1:]
        # Allocate output tensor.
        output_tensor = torch.empty(
            output_size, dtype=input_.dtype, device=input_.device
        )
        # All-gather.
        self.dist_module.all_gather_into_tensor(
            output_tensor, input_, group=self.device_group
        )

        # Reshape
        output_tensor = output_tensor.reshape((self.world_size,) + input_size)
        output_tensor = output_tensor.movedim(0, dim)
        output_tensor = output_tensor.reshape(
            input_size[:dim]
            + (self.world_size * input_size[dim],)
            + input_size[dim + 1 :]
        )
        return output_tensor

    defsend_tensor_dict(
        self,
        tensor_dict: dict[str, torch.Tensor | Any],
        dst: int,
    ) -> None:
        if not self.supports_tensor_dict:
            raise NotImplementedError(
                "CpuCommunicator does not support tensor dict fastpath with "
                "torch.distributed backend."
            )
        return self.dist_module.send_tensor_dict(tensor_dict, dst)

    defrecv_tensor_dict(
        self,
        src: int,
    ) -> dict[str, torch.Tensor | Any]:
        if not self.supports_tensor_dict:
            raise NotImplementedError(
                "CpuCommunicator does not support tensor dict fastpath with "
                "torch.distributed backend."
            )
        return self.dist_module.recv_tensor_dict(src)

    defdispatch_router_logits(
        self,
        hidden_states: torch.Tensor,
        router_logits: torch.Tensor,
        is_sequence_parallel: bool = False,
        extra_tensors: list[torch.Tensor] | None = None,
    ) -> (
        tuple[torch.Tensor, torch.Tensor]
        | tuple[torch.Tensor, torch.Tensor, list[torch.Tensor]]
    ):
"""
        Dispatch the hidden states and router logits to the appropriate device.
        This is a no-op in the base class.
        """

        assert self.all2all_manager is not None
        return self.all2all_manager.dispatch_router_logits(
            hidden_states,
            router_logits,
            is_sequence_parallel,
            extra_tensors,
        )

    defdispatch(
        self,
        hidden_states: torch.Tensor,
        topk_weights: torch.Tensor,
        topk_ids: torch.Tensor,
        is_sequence_parallel: bool = False,
        extra_tensors: list[torch.Tensor] | None = None,
    ) -> (
        tuple[torch.Tensor, torch.Tensor, torch.Tensor]
        | tuple[torch.Tensor, torch.Tensor, torch.Tensor, list[torch.Tensor]]
    ):
"""
        Dispatch the hidden states and topk weights/ids to the appropriate device.
        This is a no-op in the base class.
        """
        assert self.all2all_manager is not None
        return self.all2all_manager.dispatch(
            hidden_states,
            topk_weights,
            topk_ids,
            is_sequence_parallel,
            extra_tensors=extra_tensors,
        )

    defcombine(
        self, hidden_states: torch.Tensor, is_sequence_parallel: bool = False
    ) -> torch.Tensor:
"""
        Combine the hidden states and router logits from the appropriate device.
        This is a no-op in the base class.
        """
        assert self.all2all_manager is not None
        return self.all2all_manager.combine(
            hidden_states,
            is_sequence_parallel,
        )
```