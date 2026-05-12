---
title: offloader - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/offloader/
source: sitemap
fetched_at: 2026-05-07T21:33:51.15769156-03:00
rendered_js: false
word_count: 0
summary: This class implements a prefetching-based offloader that utilizes group-based layer selection and asynchronous host-to-device transfers to hide latency. It integrates with torch.compile and CUDA graphs by using static buffers and stream synchronization.
tags:
    - memory-offloading
    - async-prefetch
    - cuda-graphs
    - pytorch-optimization
    - gpu-memory-management
    - layer-grouping
category: concept
---

```
classPrefetchOffloader(BaseOffloader):
"""Prefetching-based offloader with group-based layer selection.

    Groups layers and uses async H2D prefetch to hide transfer latency.
    Uses static buffers and stream synchronization for torch.compile and
    CUDA graph compatibility.

    Args:
        group_size: Group every N layers together.
        num_in_group: Offload this many layers per group (last N of each group).
        prefetch_step: Number of layers to prefetch ahead.
        mode: Offload mode ("cpu" is currently supported).
    """

    def__init__(
        self,
        group_size: int,
        num_in_group: int,
        prefetch_step: int,
        offload_params: set[str] | None = None,
        mode: str = "cpu",
    ):
        self.group_size = group_size
        self.num_in_group = num_in_group
        self.prefetch_step = prefetch_step
        self.offload_params = offload_params or set()
        self.mode = mode

        # Copy stream for async H2D transfers
        self.copy_stream = torch.cuda.Stream()

        # Module offloaders and buffer pool (populated in wrap_modules/post_init)
        self.module_offloaders: list[_ModuleOffloader] = []
        self.buffer_pool: StaticBufferPool | None = None
        self.total_offloaded_bytes = 0

    defwrap_modules(
        self,
        modules_generator: Generator[nn.Module, None, None],
    ) -> list[nn.Module]:
"""Wrap modules with prefetch offloading logic."""
        assert len(self.module_offloaders) == 0, (
            "wrap_modules should only be called once"
        )

        all_modules = []
        offload_modules = []

        for module_index, module in enumerate(modules_generator):
            all_modules.append(module)

            # Select layers to offload based on group pattern
            # Offload last num_in_group layers of each group_size
            if module_index % self.group_size >= self.group_size - self.num_in_group:
                if self.offload_params:
                    whitelist = [
                        name
                        for name, _ in module.named_parameters()
                        if any(f".{p}." in f".{name}." for p in self.offload_params)
                    ]
                else:
                    whitelist = [name for name, _ in module.named_parameters()]

                if not whitelist:
                    continue  # skip layers with no matching params

                offload_modules.append(module)
                self.module_offloaders.append(
                    _ModuleOffloader(
                        mode=self.mode,
                        module=module,
                        copy_stream=self.copy_stream,
                        whitelist_param_names=whitelist,
                        layer_idx=len(self.module_offloaders),
                    )
                )

        for index, module in enumerate(offload_modules):
            self._hook_module_forward(index, module)

        return all_modules

    def_hook_module_forward(self, index: int, module: nn.Module):
"""Hook module's forward with torch.compile-compatible sync."""
        original_forward = module.forward

        defforward(*args, **kwargs):
            # Temporarily restore original forward to avoid recursion
            module.forward = original_forward

            # Wait for this layer's prefetch to complete
            # mutates_args on input_tensor creates data dependency for torch.compile
            input_tensor = args[0] if args else kwargs.get("hidden_states")
            torch.ops.vllm.wait_prefetch(input_tensor, index)

            # No parameter swapping needed - parameters already point to
            # GPU static buffers (set in assign_static_buffer)
            output = original_forward(*args, **kwargs)

            # Start prefetch for next layer (circular)
            # mutates_args on output_tensor creates ordering dependency
            next_index = (index + self.prefetch_step) % len(self.module_offloaders)
            # Handle tuple output (e.g., (hidden_states, residual))
            if isinstance(output, tuple):
                torch.ops.vllm.start_prefetch(output[0], next_index)
            else:
                torch.ops.vllm.start_prefetch(output, next_index)

            # No explicit offload needed - static buffers are reused implicitly

            # Restore hooked forward
            module.forward = forward
            return output

        module.forward = forward

    def_wait_for_layer(self, layer_idx: int):
"""Called by custom op - wait for copy to complete.

        Synchronization strategy:
        - During CUDA graph capture: use event-based wait (graph-compatible)
        - Outside capture (warmup/eager): use wait_stream (more robust)

        During capture, we skip wait for pre-capture prefetches because:
        1. sync_before_graph_capture() ensures pre-capture work is complete
        2. We can't wait on pre-capture events during capture (isolation error)
        """
        offloader = self.module_offloaders[layer_idx]

        if torch.cuda.is_current_stream_capturing():
            # During capture, skip wait for pre-capture prefetches.
            # sync_before_graph_capture() ensures pre-capture work is complete.
            if not offloader._prefetch_in_capture:
                return
            # Event-based wait for in-capture prefetches (graph-compatible)
            torch.cuda.current_stream().wait_event(offloader._copy_done_event)
            # Mark that this prefetch has been waited on (joined).
            offloader._prefetch_in_capture = False
        else:
            if offloader._event_valid_for_eager:
                # Use per-layer event to only wait for THIS layer's copy,
                # allowing other layers' prefetches to run concurrently.
                torch.cuda.current_stream().wait_event(offloader._copy_done_event)
            else:
                # Event not usable (unrecorded or recorded during capture).
                # Fall back to wait_stream to drain all copy_stream work.
                torch.cuda.current_stream().wait_stream(self.copy_stream)

    defsync_prev_onload(self):
"""Sync previous onload operations.

        Ensures any H2D copies in flight on copy_stream complete before
        the compute stream continues. Call this before CUDA graph
        capture/replay or when synchronization is needed.
        """
        torch.cuda.current_stream().wait_stream(self.copy_stream)

    def_start_prefetch(self, layer_idx: int):
"""Called by custom op - start async copy to static buffer."""
        offloader = self.module_offloaders[layer_idx]
        offloader.start_onload_to_static()

    defjoin_after_forward(self):
"""Join copy_stream after model forward completes.

        Call this after the model forward pass but before CUDA graph capture
        ends. This ensures copy_stream is rejoined for any prefetches started
        during the forward pass.

        We join ALL layers that have _prefetch_in_capture=True, meaning their
        prefetch was started during capture but not yet waited on (joined).
        This handles both full and piecewise cudagraph modes correctly:
        - Full mode: joins layers 0..prefetch_step-1 (prefetched by last layers)
        - Piecewise mode: joins only layers prefetched by THIS subgraph's layers
        """
        if not self.module_offloaders:
            return
        # Join all layers whose prefetch was started in capture but not waited on
        for offloader in self.module_offloaders:
            if offloader._prefetch_in_capture:
                torch.cuda.current_stream().wait_event(offloader._copy_done_event)
                offloader._prefetch_in_capture = False

    defpost_init(self):
"""Allocate static buffer pool and start initial prefetches.

        Note: Parameters have already been offloaded to CPU during wrap_modules()
        (in _CpuParamOffloader.__init__), so GPU memory is available for the
        static buffer pool.
        """
        # Sync CPU storage with current param.data BEFORE collecting param info.
        # This is needed because process_weights_after_loading may have:
        # 1. Transformed weights (quantization, transpose, etc.)
        # 2. Created new CPU tensors via device_loading_context
        # Our _cpu_storage would be stale otherwise.
        for offloader in self.module_offloaders:
            offloader.sync_cpu_storage()

        # Collect parameter info (now using synced CPU storage)
        param_infos: list[ParamInfo] = []
        device: torch.device | None = None

        for offloader in self.module_offloaders:
            param_infos.extend(offloader.get_param_infos())
            if device is None:
                device = offloader.device

        if device is None:
            # No modules to offload
            return

        # Allocate static buffer pool
        self.buffer_pool = StaticBufferPool(
            param_infos=param_infos,
            slot_capacity=self.prefetch_step,
            device=device,
        )

        # Assign buffer slots and point parameters to GPU buffers
        for idx, offloader in enumerate(self.module_offloaders):
            slot_idx = idx % self.prefetch_step
            offloader.assign_buffer_slot(self.buffer_pool, slot_idx)

        # Collect offloaded bytes
        for offloader in self.module_offloaders:
            offloader.post_init()
            self.total_offloaded_bytes += offloader.offloaded_bytes

        logger.info_once(
            f"[PrefetchOffloader] Initialized {len(self.module_offloaders)} modules. "
            f"Total GPU memory saved: {self.total_offloaded_bytes/1e9:.4f} GB, "
            f"Static buffer pool: {self.buffer_pool.total_bytes/1e9:.4f} GB "
            f"(group_size={self.group_size}, num_in_group={self.num_in_group}, "
            f"prefetch_step={self.prefetch_step}, mode={self.mode})"
        )

        # Start initial prefetches
        for i in range(min(self.prefetch_step, len(self.module_offloaders))):
            self.module_offloaders[i].start_onload_to_static()
```