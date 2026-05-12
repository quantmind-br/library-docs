---
title: async_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/utils/async_utils/
source: sitemap
fetched_at: 2026-05-07T21:38:29.456580522-03:00
rendered_js: false
word_count: 32
summary: This document defines an asynchronous tokenizer wrapper that utilizes micro-batching to aggregate multiple requests into single execution calls, improving throughput while maintaining event loop responsiveness.
tags:
    - asynchronous-programming
    - micro-batching
    - tokenization
    - performance-optimization
    - concurrency
    - thread-pool
category: concept
---

```
classAsyncMicrobatchTokenizer:
"""Asynchronous tokenizer with micro-batching.

    Pulls pending encode/decode requests from a queue and batches them
    up to reduce overhead. A single-thread ThreadPoolExecutor is used
    so the event loop stays responsive.
    """

    def__init__(
        self,
        tokenizer,
        max_batch_size: int = 32,
        batch_wait_timeout_s: float = 0.002,
        executor: ThreadPoolExecutor | None = None,
    ) -> None:
        self.tokenizer = tokenizer
        self.max_batch_size = max_batch_size
        self.batch_wait_timeout_s = batch_wait_timeout_s

        self._loop = asyncio.get_running_loop()
        self._queues: dict[
            tuple,
            asyncio.Queue[tuple[str, dict, Future] | tuple[list[int], Future]],
        ] = {}
        self._batcher_tasks: list[Task] = []

        # Single-thread executor for blocking tokenizer calls.
        # Accept an external executor to serialize with other tokenizer users.
        self._executor = executor or ThreadPoolExecutor(max_workers=1)

    # === Public async API ===
    async def__call__(self, prompt, **kwargs) -> BatchEncoding:
        result_future: Future = self._loop.create_future()
        key = self._queue_key("encode", kwargs)
        queue = self._get_queue(self._loop, key)
        await queue.put((prompt, kwargs, result_future))
        return await result_future

    async defencode(self, prompt, **kwargs) -> list[int]:
        return (await self(prompt, **kwargs)).input_ids

    async defdecode(self, token_ids, **kwargs) -> str:
        result_future: Future = self._loop.create_future()
        key = self._queue_key("decode", kwargs)
        queue = self._get_queue(self._loop, key)
        await queue.put((token_ids, result_future))
        return await result_future

    # === Internal helpers ===
    def_get_queue(
        self, loop: asyncio.AbstractEventLoop, key: tuple
    ) -> asyncio.Queue[tuple[str, dict, Future] | tuple[list[int], Future]]:
"""Get the request queue for the given operation key, creating a new
        queue and batcher task if needed."""
        queue = self._queues.get(key)
        if queue is None:
            self._queues[key] = queue = asyncio.Queue()
            if key[0] == "encode":
                can_batch = key[1] != "other"
                coro = self._batch_encode_loop(queue, can_batch)
            else:
                assert key[0] == "decode", f"Unknown operation type: {key[0]}."
                coro = self._batch_decode_loop(queue)
            self._batcher_tasks.append(loop.create_task(coro))
        return queue

    async def_batch_encode_loop(self, queue: asyncio.Queue, can_batch: bool):
"""Batch incoming encode requests for efficiency."""
        while True:
            prompt, kwargs, result_future = await queue.get()
            prompts = [prompt]
            kwargs_list = [kwargs]
            result_futures = [result_future]
            deadline = self._loop.time() + self.batch_wait_timeout_s

            while len(prompts) < self.max_batch_size:
                timeout = deadline - self._loop.time()
                if timeout <= 0:
                    break
                try:
                    prompt, kwargs, result_future = await asyncio.wait_for(
                        queue.get(), timeout
                    )
                    prompts.append(prompt)
                    result_futures.append(result_future)
                    if not can_batch:
                        kwargs_list.append(kwargs)
                except asyncio.TimeoutError:
                    break

            try:
                # If every request uses identical kwargs we can run a single
                # batched tokenizer call for a big speed-up.
                if can_batch and len(prompts) > 1:
                    batch_encode_fn = partial(self.tokenizer, prompts, **kwargs)
                    results = await self._loop.run_in_executor(
                        self._executor, batch_encode_fn
                    )

                    for i, fut in enumerate(result_futures):
                        if not fut.done():
                            data = {k: v[i] for k, v in results.items()}
                            fut.set_result(BatchEncoding(data))
                else:
                    encode_fn = lambda prompts=prompts, kwargs=kwargs_list: [
                        self.tokenizer(p, **kw) for p, kw in zip(prompts, kwargs)
                    ]
                    results = await self._loop.run_in_executor(
                        self._executor, encode_fn
                    )

                    for fut, res in zip(result_futures, results):
                        if not fut.done():
                            fut.set_result(res)
            except Exception as e:
                for fut in result_futures:
                    if not fut.done():
                        fut.set_exception(e)

    async def_batch_decode_loop(self, queue: asyncio.Queue):
"""Batch incoming decode requests for efficiency."""
        while True:
            token_ids, result_future = await queue.get()
            token_ids_list = [token_ids]
            result_futures = [result_future]
            deadline = self._loop.time() + self.batch_wait_timeout_s

            while len(token_ids_list) < self.max_batch_size:
                timeout = deadline - self._loop.time()
                if timeout <= 0:
                    break
                try:
                    token_ids, result_future = await asyncio.wait_for(
                        queue.get(), timeout
                    )
                    token_ids_list.append(token_ids)
                    result_futures.append(result_future)
                except asyncio.TimeoutError:
                    break

            try:
                # Perform a single batched decode call for all requests
                results = await self._loop.run_in_executor(
                    self._executor, self.tokenizer.batch_decode, token_ids_list
                )
                for fut, res in zip(result_futures, results):
                    if not fut.done():
                        fut.set_result(res)
            except Exception as e:
                for fut in result_futures:
                    if not fut.done():
                        fut.set_exception(e)

    def_queue_key(self, op: str, kwargs: dict) -> tuple:
"""
        Return a normalized key describing operation + kwargs.

        - `add_special_tokens`: {True/False}
        - `truncation`: {True/False}
          - If `truncation` is False (`max_length` is None),
            returns a key for a can_batch queue.
          - If `truncation` is True and `max_length` is None or equals
            `tokenizer.model_max_length`, returns a key for a can_batch queue.
          - Otherwise, returns a key for a cannot_batch queue.

        Examples:
          - Decode: ("decode",)
          - Encode typical:
            ("encode", add_special_tokens, bool_truncation, max_length_label)
          - Fallback: ("encode", "other")
        """

        if op == "decode":
            return ("decode",)

        add_special_tokens = kwargs.get("add_special_tokens", True)
        truncation = kwargs.get("truncation", False)
        max_length = kwargs.get("max_length")

        if not truncation:
            return "encode", add_special_tokens, False, None

        model_max = getattr(self.tokenizer, "model_max_length", None)
        if max_length is None or (model_max is not None and max_length == model_max):
            return "encode", add_special_tokens, True, "model_max"

        return "encode", "other"

    def__del__(self):
        if (
            (tasks := getattr(self, "_batcher_tasks", None))
            and (loop := getattr(self, "_loop", None))
            and not loop.is_closed()
        ):

            defcancel_tasks():
                for task in tasks:
                    task.cancel()

            loop.call_soon_threadsafe(cancel_tasks)
```