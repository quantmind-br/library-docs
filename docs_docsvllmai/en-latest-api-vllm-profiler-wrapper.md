---
title: wrapper - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/profiler/wrapper/
source: sitemap
fetched_at: 2026-05-07T21:34:48.031613885-03:00
rendered_js: false
word_count: 0
summary: This document defines a wrapper class for the PyTorch profiler to manage performance tracing, scheduling, and result reporting within a distributed training environment.
tags:
    - pytorch
    - profiling
    - performance-monitoring
    - distributed-training
    - trace-handling
    - code-optimization
category: reference
---

```
classTorchProfilerWrapper(WorkerProfiler):
    def__init__(
        self,
        profiler_config: ProfilerConfig,
        worker_name: str,
        local_rank: int,
        activities: list[TorchProfilerActivity],
        on_trace_ready: Callable[[torch.profiler.profile], None] | None = None,
    ) -> None:
        super().__init__(profiler_config)

        self.local_rank = local_rank
        self.profiler_config = profiler_config
        torch_profiler_trace_dir = profiler_config.torch_profiler_dir
        if local_rank in (None, 0):
            logger.info_once(
                "Torch profiling enabled. Traces will be saved to: %s",
                torch_profiler_trace_dir,
            )
            logger.debug(
                "Profiler config: record_shapes=%s,"
                "profile_memory=%s,with_stack=%s,with_flops=%s",
                profiler_config.torch_profiler_record_shapes,
                profiler_config.torch_profiler_with_memory,
                profiler_config.torch_profiler_with_stack,
                profiler_config.torch_profiler_with_flops,
            )

        # Determine trace handler: use custom handler if provided,
        # otherwise default to tensorboard trace handler
        if on_trace_ready is not None:
            trace_handler = on_trace_ready
        else:
            trace_handler = torch.profiler.tensorboard_trace_handler(
                torch_profiler_trace_dir,
                worker_name=worker_name,
                use_gzip=profiler_config.torch_profiler_use_gzip,
            )

        self.dump_cpu_time_total = "CPU" in activities and len(activities) == 1

        # Create profiler schedule if warmup or wait iterations are configured
        profiler_schedule = None
        if profiler_config.warmup_iterations > 0 or profiler_config.wait_iterations > 0:
            profiler_schedule = torch.profiler.schedule(
                skip_first=0,
                wait=profiler_config.wait_iterations,
                warmup=profiler_config.warmup_iterations,
                active=profiler_config.active_iterations,
                repeat=1,
            )
            if local_rank in (None, 0):
                logger.info_once(
                    "Profiler schedule configured: wait=%d, warmup=%d, active=%d",
                    profiler_config.wait_iterations,
                    profiler_config.warmup_iterations,
                    profiler_config.active_iterations,
                )

        self.profiler = torch.profiler.profile(
            activities=[TorchProfilerActivityMap[activity] for activity in activities],
            schedule=profiler_schedule,
            record_shapes=profiler_config.torch_profiler_record_shapes,
            profile_memory=profiler_config.torch_profiler_with_memory,
            with_stack=profiler_config.torch_profiler_with_stack,
            with_flops=profiler_config.torch_profiler_with_flops,
            on_trace_ready=trace_handler,
        )

        # Track if we're using a schedule (need to call step())
        self._uses_schedule = profiler_schedule is not None
        self._warmup_iterations = profiler_config.warmup_iterations
        # Subtract 1 because profiler.start() already consumes step 0
        # (WAIT or WARMUP), so only wait + warmup - 1 non-active steps
        # remain to be advanced through via profiler.step() calls.
        self._warmup_steps_remaining = max(
            profiler_config.wait_iterations + profiler_config.warmup_iterations - 1,
            0,
        )

    def_build_profiler_table(
        self,
        sort_key: str,
        row_limit: int | None = None,
    ) -> str:
        if row_limit is None:  # use profiler default row limit of 100
            return self.profiler.key_averages().table(sort_by=sort_key)
        return self.profiler.key_averages().table(
            sort_by=sort_key,
            row_limit=row_limit,
        )

    def_write_profiler_table(self, rank: int, table: str) -> None:
        profiler_dir = self.profiler_config.torch_profiler_dir

        # Skip file write for URI paths (gs://, s3://, etc.)
        # as standard file I/O doesn't work with URI schemes
        if not _is_uri_path(profiler_dir):
            profiler_out_file = f"{profiler_dir}/profiler_out_{rank}.txt"
            with open(profiler_out_file, "w") as f:
                print(table, file=f)

    @override
    def_start(self) -> None:
        self.profiler.start()

    @override
    def_stop(self) -> None:
        self.profiler.stop()

        profiler_config = self.profiler_config
        rank = self.local_rank
        if profiler_config.torch_profiler_dump_cuda_time_total:
            table = self._build_profiler_table(sort_key="self_cuda_time_total")
            self._write_profiler_table(rank, table)

            # only print profiler results on rank 0
            if rank == 0:
                print(table)

        if self.dump_cpu_time_total:
            table = self._build_profiler_table(
                sort_key="self_cpu_time_total", row_limit=50
            )
            self._write_profiler_table(rank, table)

            # only print profiler results on rank 0
            if rank == 0:
                print(table)

    @override
    def_profiler_step(self) -> bool:
"""Call profiler.step() when using schedule-based profiling.

        Returns:
            True if the step was an active profiling step (data recorded),
            False if the step was a warmup step (data discarded).
        """
        if self._uses_schedule:
            self.profiler.step()
            # Track warmup steps - only count active steps toward max_iterations
            if self._warmup_steps_remaining > 0:
                self._warmup_steps_remaining -= 1
                return False
        return True

    @override
    defannotate_context_manager(self, name: str):
        return torch.profiler.record_function(name)
```