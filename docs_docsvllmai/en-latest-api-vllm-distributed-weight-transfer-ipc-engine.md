---
title: ipc_engine - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/ipc_engine/
source: sitemap
fetched_at: 2026-05-07T21:19:07.874171946-03:00
rendered_js: false
word_count: 0
summary: This document defines the IPCWeightTransferEngine class, which facilitates high-performance model weight distribution between a trainer and inference workers using CUDA IPC handles.
tags:
    - cuda-ipc
    - weight-transfer
    - distributed-training
    - gpu-memory
    - tensor-sharing
    - vllm
category: api
---

```
classIPCWeightTransferEngine(
    WeightTransferEngine[IPCWeightTransferInitInfo, IPCWeightTransferUpdateInfo]
):
"""
    Weight transfer engine using CUDA IPC for communication between trainer and workers.

    This implementation uses CUDA IPC to transfer weights from the trainer (rank 0)
    to all inference workers in a process group. IPC handles are used to share
    memory between processes on the same node.
    """

    # Define backend-specific dataclass types
    init_info_cls = IPCWeightTransferInitInfo
    update_info_cls = IPCWeightTransferUpdateInfo

    def__init__(
        self, config: WeightTransferConfig, parallel_config: ParallelConfig
    ) -> None:
"""
        Initialize the IPC weight transfer engine.

        Args:
            config: The configuration for the weight transfer engine
            parallel_config: The configuration for the parallel setup
        """
        super().__init__(config, parallel_config)

    definit_transfer_engine(self, init_info: IPCWeightTransferInitInfo) -> None:
"""
        Initialize the weight transfer mechanism.
        This is called once at the beginning of training.
        No initialization needed for IPC backend.

        Args:
            init_info: IPC initialization info (empty)
        """
        pass

    defreceive_weights(
        self,
        update_info: IPCWeightTransferUpdateInfo,
        load_weights: Callable[[list[tuple[str, torch.Tensor]]], None],
    ) -> None:
"""
        Receive weights from the trainer via CUDA IPC handles.

        Args:
            update_info: IPC update info containing parameter names, dtypes, shapes,
                        and IPC handles. Each IPC handle is a mapping between physical
                        GPU UUID and the IPC handle tuple (func, args).
            load_weights: Callable that loads weights into the model. Called
                         incrementally for each weight to avoid OOM.
        """
        assert update_info.ipc_handles is not None
        weights = []
        for name, _dtype_name, _shape, ipc_handle in zip(
            update_info.names,
            update_info.dtype_names,
            update_info.shapes,
            update_info.ipc_handles,
        ):
            device_index = torch.accelerator.current_device_index()
            props = torch.cuda.get_device_properties(device_index)
            physical_gpu_id = str(props.uuid)

            if physical_gpu_id not in ipc_handle:
                raise ValueError(
                    f"IPC handle not found for GPU UUID {physical_gpu_id}. "
                    f"Available UUIDs: {list(ipc_handle.keys())}"
                )

            handle = ipc_handle[physical_gpu_id]

            func, args = handle
            list_args = list(args)  # type: ignore
            # Index 6 is the device_index parameter in torch's
            # IPC handle tuple (rebuild_cuda_tensor). Update it
            # to the current device since the logical index can
            # differ between sender and receiver.
            list_args[6] = device_index
            weight = func(*list_args)  # type: ignore
            weights.append((name, weight))

        load_weights(weights)

    defshutdown(self) -> None:
"""
        Shutdown the weight transfer engine.
        """
        pass

    @staticmethod
    deftrainer_send_weights(
        iterator: Iterator[tuple[str, torch.Tensor]],
        trainer_args: dict[str, Any] | IPCTrainerSendWeightsArgs,
    ) -> None:
"""
        Send weights from trainer to inference workers via CUDA IPC.

        Supports two modes:
        - 'ray': Sends weights via Ray RPC to a Ray-based LLM handle
        - 'http': Sends weights via HTTP POST to a vLLM HTTP server

        Args:
            iterator: Iterator of model parameters. Returns (name, tensor) tuples.
                     Tensors should be on the same GPU as the inference workers.
            trainer_args: Dictionary containing IPC-specific arguments.
                         Should contain keys from IPCTrainerSendWeightsArgs:
                         - mode: 'ray' or 'http'
                         - llm_handle: Ray ObjectRef (for 'ray' mode)
                         - url: Base URL string (for 'http' mode)

        Example (Ray mode):
            >>> from vllm.distributed.weight_transfer.ipc_engine import (
            ...     IPCWeightTransferEngine,
            ...     IPCTrainerSendWeightsArgs,
            ... )
            >>> param_iter = ((n, p) for n, p in model.named_parameters())
            >>> args = IPCTrainerSendWeightsArgs(mode="ray", llm_handle=llm_handle)
            >>> IPCWeightTransferEngine.trainer_send_weights(param_iter, asdict(args))

        Example (HTTP mode):
            >>> args = IPCTrainerSendWeightsArgs(
            ...     mode="http", url="http://localhost:8000"
            ... )
            >>> IPCWeightTransferEngine.trainer_send_weights(param_iter, asdict(args))
        """
        # Parse trainer args - accept either dict or dataclass instance
        if isinstance(trainer_args, dict):
            args = IPCTrainerSendWeightsArgs(**trainer_args)
        else:
            args = trainer_args

        # Get physical GPU UUID
        device_index = torch.accelerator.current_device_index()
        props = torch.cuda.get_device_properties(device_index)
        gpu_uuid = str(props.uuid)

        # Collect weight metadata and create IPC handles
        names = []
        dtype_names = []
        shapes = []
        ipc_handles = []

        for name, tensor in iterator:
            names.append(name)
            dtype_names.append(str(tensor.dtype).split(".")[-1])
            shapes.append(list(tensor.shape))

            # Create IPC handle for this weight tensor
            # The tensor must remain in memory for IPC to work
            weight = tensor.detach().contiguous()
            ipc_handle = reduce_tensor(weight)
            ipc_handles.append({gpu_uuid: ipc_handle})

        # Send weights based on mode
        if args.mode == "ray":
            # Ray mode: send via Ray RPC
            importray

            update_info = asdict(
                IPCWeightTransferUpdateInfo(
                    names=names,
                    dtype_names=dtype_names,
                    shapes=shapes,
                    ipc_handles=ipc_handles,
                )
            )
            ray.get(
                args.llm_handle.update_weights.remote(dict(update_info=update_info))
            )
        elif args.mode == "http":
            # HTTP mode: send via HTTP POST with pickled handles
            # Pickle and base64 encode IPC handles for HTTP transmission
            pickled_handles = base64.b64encode(pickle.dumps(ipc_handles)).decode(
                "utf-8"
            )

            url = f"{args.url}/update_weights"
            payload = {
                "update_info": {
                    "names": names,
                    "dtype_names": dtype_names,
                    "shapes": shapes,
                    "ipc_handles_pickled": pickled_handles,
                }
            }
            response = requests.post(url, json=payload, timeout=300)
            response.raise_for_status()
```