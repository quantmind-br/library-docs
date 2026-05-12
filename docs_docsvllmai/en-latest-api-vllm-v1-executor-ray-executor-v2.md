---
title: ray_executor_v2 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/executor/ray_executor_v2/
source: sitemap
fetched_at: 2026-05-07T21:40:49.33067487-03:00
rendered_js: false
word_count: 0
summary: This document defines the RayExecutorV2 class, which implements a distributed execution engine for vLLM using Ray actors for message queue-based communication and coordination. It manages the initialization of Ray clusters, placement of worker actors, and synchronization of GPU device assignments across distributed nodes.
tags:
    - distributed-computing
    - ray-framework
    - parallel-processing
    - gpu-scheduling
    - vllm-engine
    - actor-model
category: concept
---

```
classRayExecutorV2(MultiprocExecutor):
"""Ray-based distributed executor using MessageQueue communication.

    Inherits from MultiprocExecutor to reuse the MQ-based control plane
    and NCCL data plane. Workers are Ray actors.

    Async scheduling is enabled, inherited from MultiprocExecutor.
    This is cricitcal for RayExecutorV2 to be performant.
    """

    uses_ray: bool = True
    supports_pp: bool = True

    def__init__(self, vllm_config: VllmConfig):
        super().__init__(vllm_config)

    def_build_runtime_env(self) -> dict:
"""Build a runtime_env dict for RayWorkerProc actors.

        Driver env vars are applied separately via initialize_worker
        with setdefault semantics.
        """
        base = self.parallel_config.ray_runtime_env
        runtime_env: dict = copy.deepcopy(dict(base)) if base else {}

        env_vars = runtime_env.setdefault("env_vars", {})
        env_vars.update({v: "1" for v in current_platform.ray_noset_device_env_vars})
        if self.parallel_config.ray_workers_use_nsight:
            runtime_env["nsight"] = {
                "t": "cuda,cudnn,cublas",
                "o": "'worker_process_%p'",
                "cuda-graph-trace": "node",
            }
        return runtime_env

    @staticmethod
    def_get_actor_resource_kwargs() -> dict[str, Any]:
"""Return Ray actor resource kwargs for the current platform."""
        num_devices = envs.VLLM_RAY_PER_WORKER_GPUS
        device_key = current_platform.ray_device_key
        if device_key == "GPU":
            return {"num_gpus": num_devices}
        return {"num_gpus": 0, "resources": {device_key: num_devices}}

    def_init_executor(self) -> None:
"""Initialize the RayExecutorV2 executor."""
        self._finalizer = weakref.finalize(self, self.shutdown)
        self.is_failed = False
        self.failure_callback = None
        self.shutting_down = False
        self.shutdown_lock = threading.Lock()

        # Step 1: Initialize Ray cluster and retrieve placement group
        if ray is None:
            raise ImportError("Using Ray backend requires installation of ray.")
        initialize_ray_cluster(self.parallel_config, require_gpu_on_driver=False)
        placement_group = self.parallel_config.placement_group

        tp_size, pp_size, pcp_size = self._get_parallel_sizes()
        assert self.world_size == tp_size * pp_size * pcp_size, (
            f"world_size ({self.world_size}) must be equal to the "
            f"tensor_parallel_size ({tp_size}) x pipeline"
            f"_parallel_size ({pp_size}) x prefill_context"
            f"_parallel_size ({pcp_size}). "
        )

        # Step 2: Build bundle assignments for worker rank placement
        # while respecting VLLM_RAY_BUNDLE_INDICES.
        if envs.VLLM_RAY_BUNDLE_INDICES:
            bundle_to_node_id = get_bundles_for_indices(
                placement_group,
                list(map(int, envs.VLLM_RAY_BUNDLE_INDICES.split(","))),
                self.world_size,
            )
        else:
            bundle_to_node_id = get_bundles_sorted_by_node(placement_group)
        driver_node = ray.get_runtime_context().get_node_id()

        bundle_assignments: list[dict[str, Any]] = []
        for rank, (bundle_id_idx, node_id, node_ip) in enumerate(bundle_to_node_id):
            bundle_assignments.append(
                {
                    "rank": rank,
                    "bundle_id_idx": bundle_id_idx,
                    "node_id": node_id,
                    "node_ip": node_ip,
                }
            )

        # Step 3: Resolve the IP for torch.distributed TCPStore.
        # The TCPStore server runs on rank 0's node, so all workers
        # must be able to reach this address.
        dist_ip = bundle_assignments[0]["node_ip"]
        distributed_init_method = get_distributed_init_method(dist_ip, get_open_port())

        # Step 4: Create broadcast MessageQueue.
        # Workers on the driver node use shared memory; the rest use TCP.
        max_chunk_bytes = envs.VLLM_MQ_MAX_CHUNK_BYTES_MB * 1024 * 1024
        n_local = sum(1 for a in bundle_assignments if a["node_id"] == driver_node)
        self.rpc_broadcast_mq = MessageQueue(
            self.world_size,
            n_local,
            max_chunk_bytes=max_chunk_bytes,
            connect_ip=ray.util.get_node_ip_address(),
        )
        scheduler_output_handle = self.rpc_broadcast_mq.export_handle()

        # Step 5: Spawn RayWorkerProc actors into PG bundles (deferred init).
        # Workers are created lightweight here; full initialization happens
        # in Step 7 after GPU IDs are discovered.
        self.ray_worker_handles: list[RayWorkerHandle] = []
        instance_id = self.vllm_config.instance_id

        # Collect driver env vars and apply but don't overwrite node-local values.
        self.driver_env_vars = get_driver_env_vars(
            worker_specific_vars=WORKER_SPECIFIC_ENV_VARS,
        )

        runtime_env = self._build_runtime_env()
        resource_kwargs = self._get_actor_resource_kwargs()

        for bundle_idx in range(self.world_size):
            bundle = bundle_assignments[bundle_idx]
            is_driver_worker = self._is_driver_worker(bundle["rank"])
            is_driver_node = bundle["node_id"] == driver_node

            scheduling_strategy = PlacementGroupSchedulingStrategy(
                placement_group=placement_group,
                placement_group_bundle_index=bundle["bundle_id_idx"],
            )

            actor_name = build_actor_name(
                instance_id, bundle["rank"], tp_size, pp_size, pcp_size
            )

            actor = (
                ray.remote(RayWorkerProc)
                .options(
                    name=actor_name,
                    num_cpus=0,
                    **resource_kwargs,
                    scheduling_strategy=scheduling_strategy,
                    runtime_env=runtime_env,
                )
                .remote(
                    vllm_config=self.vllm_config,
                    rank=bundle["rank"],
                    distributed_init_method=distributed_init_method,
                    input_shm_handle=scheduler_output_handle,
                    is_driver_worker=is_driver_worker,
                    is_driver_node=is_driver_node,
                )
            )

            handle = RayWorkerHandle(
                actor=actor,
                rank=bundle["rank"],
                local_rank=-1,  # Set in Step 7 after GPU ID discovery
                node_id=bundle["node_id"],
                bundle_id_idx=bundle["bundle_id_idx"],
            )
            self.ray_worker_handles.append(handle)

        # Step 6: Discover GPU IDs assigned to each worker via Ray runtime context.
        worker_node_and_gpu_ids = ray.get(
            [h.actor.get_node_and_gpu_ids.remote() for h in self.ray_worker_handles]
        )

        node_workers: dict[str, list[int]] = defaultdict(list)
        node_gpus: dict[str, list[int]] = defaultdict(list)
        for i, (node_id, gpu_ids) in enumerate(worker_node_and_gpu_ids):
            node_workers[node_id].append(i)
            node_gpus[node_id].extend(gpu_ids)
        for node_id, gpu_ids in node_gpus.items():
            node_gpus[node_id] = sorted(gpu_ids)

        # Step 7: Initialize workers with correct local_rank and
        # CUDA_VISIBLE_DEVICES. Each worker sees all GPUs assigned to
        # this executor on its node; local_rank indexes into that set.
        init_worker_refs = []
        for i, (node_id, _) in enumerate(worker_node_and_gpu_ids):
            local_rank = node_workers[node_id].index(i)
            worker_env_vars = {
                current_platform.device_control_env_var: ",".join(
                    map(str, node_gpus[node_id])
                ),
            }
            self.ray_worker_handles[i].local_rank = local_rank
            init_worker_refs.append(
                self.ray_worker_handles[i].actor.initialize_worker.remote(
                    local_rank, worker_env_vars, self.driver_env_vars
                )
            )
        ray.get(init_worker_refs)

        # Step 8: Collect response MQ handles
        init_results = ray.get(
            [h.actor.wait_for_init.remote() for h in self.ray_worker_handles]
        )

        self.response_mqs: list[MessageQueue] = []
        for i, result in enumerate(init_results):
            if result["status"] != RayWorkerProc.READY_STR:
                raise RuntimeError(f"Worker {i} failed to initialize: {result}")
            self.response_mqs.append(
                MessageQueue.create_from_handle(result["handle"], 0)
            )

        # Step 9: Start run() before wait_until_ready() to avoid
        # deadlock — workers send subscriptions inside run().
        for handle in self.ray_worker_handles:
            handle.run()

        # Step 10: wait_until_ready() barrier
        self.rpc_broadcast_mq.wait_until_ready()
        for response_mq in self.response_mqs:
            response_mq.wait_until_ready()

        self.futures_queue = deque[FutureWrapper]()
        self._post_init_executor()

        self.start_worker_monitor()
        self.output_rank = self._get_output_rank()

    defstart_worker_monitor(self, inline=False) -> None:
"""Monitor worker liveness via ray.wait() on run() ObjectRefs."""
        run_refs = [h.run_ref for h in self.ray_worker_handles if h.run_ref is not None]
        if not run_refs:
            raise RuntimeError("Ray workers have not started successfully.")

        self_ref = weakref.ref(self)
        ref_to_rank = {
            h.run_ref: h.rank for h in self.ray_worker_handles if h.run_ref is not None
        }

        def_should_stop() -> bool:
            executor = self_ref()
            return not executor or executor.shutting_down

        defmonitor_workers():
            # Poll with a timeout rather than blocking on ray.wait()
            # because a blocking call would segfault if Ray is torn down
            # while this thread is inside it.
            while not _should_stop() and ray.is_initialized():
                try:
                    done, _ = ray.wait(run_refs, num_returns=1, timeout=5.0)
                except Exception:
                    logger.exception(
                        "RayWorkerMonitor: unexpected error, exiting monitor thread"
                    )
                    return
                if not done or _should_stop():
                    continue

                dead_ranks = [ref_to_rank[r] for r in done]
                executor = self_ref()
                if not executor:
                    return
                executor.is_failed = True
                logger.error(
                    "RayWorkerProc rank=%s died unexpectedly, shutting down executor.",
                    dead_ranks,
                )
                executor.shutdown()
                if executor.failure_callback is not None:
                    callback = executor.failure_callback
                    executor.failure_callback = None
                    callback()
                return

        t = threading.Thread(
            target=monitor_workers, daemon=True, name="RayWorkerMonitor"
        )
        t.start()
        self._monitor_thread = t

    def_join_monitor_thread(self) -> None:
"""Wait for the monitor thread to exit.

        Must be called before tearing down Ray resources — the monitor
        may be inside ray.wait() which would segfault if Ray is shut
        down underneath it. When the monitor itself calls shutdown()
        on worker death, we skip the join because the thread is about
        to return anyway.
        """
        monitor = getattr(self, "_monitor_thread", None)
        if (
            monitor is not None
            and monitor.is_alive()
            and threading.current_thread() is not monitor
        ):
            monitor.join(timeout=10)

    defshutdown(self) -> None:
"""Properly shut down the executor and its workers."""
        lock = getattr(self, "shutdown_lock", None)
        if lock is None:
            return

        with lock:
            if getattr(self, "shutting_down", False):
                return
            self.shutting_down = True

        self._join_monitor_thread()

        for handle in getattr(self, "ray_worker_handles", []):
            try:
                ray.kill(handle.actor)
                logger.debug("Killed actor rank=%d", handle.rank)
            except Exception:
                logger.exception("Failed to kill actor rank=%d", handle.rank)

        if rpc_broadcast_mq := getattr(self, "rpc_broadcast_mq", None):
            rpc_broadcast_mq.shutdown()
            self.rpc_broadcast_mq = None

        for mq in getattr(self, "response_mqs", []):
            mq.shutdown()
        self.response_mqs = []
```