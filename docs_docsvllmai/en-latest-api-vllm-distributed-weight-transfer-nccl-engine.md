---
title: nccl_engine - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/nccl_engine/
source: sitemap
fetched_at: 2026-05-07T21:19:07.753016124-03:00
rendered_js: false
word_count: 17
summary: This document defines the NCCLWeightTransferEngine, which facilitates the synchronization of model weights between a trainer process and inference workers using NCCL collective communication operations.
tags:
    - nccl
    - weight-transfer
    - distributed-training
    - gpu-communication
    - model-synchronization
    - pytorch
category: api
---

```
classNCCLWeightTransferEngine(
    WeightTransferEngine[NCCLWeightTransferInitInfo, NCCLWeightTransferUpdateInfo]
):
"""
    Weight transfer engine using NCCL for communication between trainer and workers.

    This implementation uses NCCL broadcast operations to transfer weights from
    the trainer (rank 0) to all inference workers in a process group.
    """

    # Define backend-specific dataclass types
    init_info_cls = NCCLWeightTransferInitInfo
    update_info_cls = NCCLWeightTransferUpdateInfo

    def__init__(
        self, config: WeightTransferConfig, parallel_config: ParallelConfig
    ) -> None:
"""
        Initialize the NCCL weight transfer engine.

        Args:
            config: The configuration for the weight transfer engine
            parallel_config: The configuration for the parallel setup
        """
        super().__init__(config, parallel_config)
        self.model_update_group: PyNcclCommunicator | None = None

    definit_transfer_engine(self, init_info: NCCLWeightTransferInitInfo) -> None:
"""
        Initialize NCCL process group with the trainer.

        Args:
            init_info: NCCL initialization info containing master address, port,
                      rank offset, and world size
        """

        # Calculate the global rank in the trainer-worker process group
        # Must account for data parallel to get unique ranks across all workers
        dp_rank = self.parallel_config.data_parallel_index
        world_size_per_dp = self.parallel_config.world_size  # TP * PP
        rank_within_dp = self.parallel_config.rank

        # Unique rank across all DP groups
        worker_rank = dp_rank * world_size_per_dp + rank_within_dp
        rank = worker_rank + init_info.rank_offset
        # Create stateless process group
        device = torch.accelerator.current_device_index()
        self.model_update_group = (
            NCCLWeightTransferEngine._stateless_init_process_group(
                init_info.master_address,
                init_info.master_port,
                rank,
                init_info.world_size,
                device=device,
            )
        )

    defreceive_weights(
        self,
        update_info: NCCLWeightTransferUpdateInfo,
        load_weights: Callable[[list[tuple[str, torch.Tensor]]], None],
    ) -> None:
"""
        Receive weights from trainer via NCCL broadcast and load them incrementally.

        If update_info.packed is True, uses packed tensor broadcasting for
        efficient transfer of multiple weights in batches. Otherwise, uses simple
        one-by-one broadcasting.

        Args:
            update_info: NCCL update info containing parameter names, dtypes, shapes,
                        and packed flag
            load_weights: Callable that loads weights into the model. Called
                         incrementally for each batch of weights to avoid OOM.
        """
        if self.model_update_group is None:
            raise RuntimeError(
                "NCCL weight transfer not initialized. "
                "Call init_transfer_engine() first."
            )

        if update_info.packed:
            # Build iterator of (name, (shape, dtype)) from update_info
            defstate_dict_info_iterator():
                for name, dtype_name, shape in zip(
                    update_info.names, update_info.dtype_names, update_info.shapes
                ):
                    dtype = getattr(torch, dtype_name)
                    yield (name, (shape, dtype))

            packed_broadcast_consumer(
                iterator=state_dict_info_iterator(),
                group=self.model_update_group,
                src=0,
                post_unpack_func=load_weights,
                buffer_size_bytes=update_info.packed_buffer_size_bytes,
                num_buffers=update_info.packed_num_buffers,
            )
        else:
            # Use simple one-by-one broadcasting
            for name, dtype_name, shape in zip(
                update_info.names, update_info.dtype_names, update_info.shapes
            ):
                dtype = getattr(torch, dtype_name)
                weight = torch.empty(shape, dtype=dtype, device="cuda")
                self.model_update_group.broadcast(
                    weight, src=0, stream=torch.cuda.current_stream()
                )
                load_weights([(name, weight)])
                del weight

    defshutdown(self) -> None:
        if self.model_update_group is not None:
            # Clean up the communicator by removing the reference
            self.model_update_group = None

    @staticmethod
    deftrainer_send_weights(
        iterator: Iterator[tuple[str, torch.Tensor]],
        trainer_args: dict[str, Any] | NCCLTrainerSendWeightsArgs,
    ) -> None:
"""Broadcast weights from trainer to vLLM workers.

        Args:
            iterator: Iterator of model parameters. Returns (name, tensor) tuples
            trainer_args: Dictionary or NCCLTrainerSendWeightsArgs instance containing
                         NCCL-specific arguments. If a dict, should contain keys from
                         NCCLTrainerSendWeightsArgs.

        Example:
            >>> from vllm.distributed.weight_transfer.nccl_engine import (
            ...     NCCLWeightTransferEngine,
            ...     NCCLTrainerSendWeightsArgs,
            ... )
            >>> param_iter = ((n, p) for n, p in model.named_parameters())
            >>> args = NCCLTrainerSendWeightsArgs(group=group, packed=True)
            >>> NCCLWeightTransferEngine.trainer_send_weights(param_iter, args)
        """
        # Parse trainer args - accept either dict or dataclass instance
        if isinstance(trainer_args, dict):
            args = NCCLTrainerSendWeightsArgs(**trainer_args)
        else:
            args = trainer_args

        if args.post_iter_func is None:
            # Default: extract just the tensor from (name, tensor) tuple
            post_iter_func = lambda x: x[1]
        else:
            post_iter_func = args.post_iter_func

        if args.packed:
            # Use packed tensor broadcasting for efficiency
            fromvllm.distributed.weight_transfer.packed_tensorimport (
                packed_broadcast_producer,
            )

            packed_broadcast_producer(
                iterator=iterator,
                group=args.group,
                src=args.src,
                post_iter_func=post_iter_func,
                buffer_size_bytes=args.packed_buffer_size_bytes,
                num_buffers=args.packed_num_buffers,
            )
        else:
            # Use simple one-by-one broadcasting
            for item in iterator:
                tensor = post_iter_func(item)
                args.group.broadcast(
                    tensor,
                    src=args.src,
                    stream=args.stream or torch.cuda.current_stream(),
                )

    @staticmethod
    deftrainer_init(
        init_info: NCCLWeightTransferInitInfo | dict,
    ) -> "PyNcclCommunicator":
"""
        Initialize NCCL process group for trainer-side weight transfer.

        The trainer is always rank 0 in the process group. Uses the current
        CUDA device (torch.accelerator.current_device_index()).

        Args:
            init_info: Either an NCCLWeightTransferInitInfo object or a dict with keys:
                - master_address: str
                - master_port: int
                - world_size: int

        Returns:
            PyNcclCommunicator for weight transfer.

        Example:
            >>> from vllm.distributed.weight_transfer.nccl_engine import (
            ...     NCCLWeightTransferEngine,
            ... )
            >>> group = NCCLWeightTransferEngine.trainer_init(
            ...     dict(
            ...         master_address=master_address,
            ...         master_port=master_port,
            ...         world_size=world_size,
            ...     ),
            ... )
        """
        if isinstance(init_info, dict):
            master_address = init_info["master_address"]
            master_port = init_info["master_port"]
            world_size = init_info["world_size"]
        else:
            # NCCLWeightTransferInitInfo object
            master_address = init_info.master_address
            master_port = init_info.master_port
            world_size = init_info.world_size

        # Trainer is always rank 0
        device = torch.accelerator.current_device_index()
        return NCCLWeightTransferEngine._stateless_init_process_group(
            master_address,
            master_port,
            0,
            world_size,
            device,
        )

    @staticmethod
    def_stateless_init_process_group(
        master_address, master_port, rank, world_size, device
    ):
"""
        vLLM provides `StatelessProcessGroup` to create a process group
        without considering the global process group in torch.distributed.
        It is recommended to create `StatelessProcessGroup`, and then initialize
        the data-plane communication (NCCL) between external (train processes)
        and vLLM workers.
        """
        fromvllm.distributed.device_communicators.pyncclimport PyNcclCommunicator
        fromvllm.distributed.utilsimport StatelessProcessGroup

        pg = StatelessProcessGroup.create(
            host=master_address, port=master_port, rank=rank, world_size=world_size
        )
        pynccl = PyNcclCommunicator(pg, device=device)
        return pynccl
```