---
title: Pause Resume - vLLM
url: https://docs.vllm.ai/en/latest/examples/features/pause_resume/
source: sitemap
fetched_at: 2026-05-07T21:12:55.800156702-03:00
rendered_js: false
word_count: 13
summary: This document provides examples and scripts for testing the pause and resume functionality in vLLM, demonstrating how to control generation processes across both HTTP API-based data parallel configurations and offline engine instances.
tags:
    - vllm
    - pause-resume
    - data-parallelism
    - inference-engine
    - llm-serving
    - asynchronous-processing
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/features/pause_resume.md "Edit this page")

Source [https://github.com/vllm-project/vllm/tree/main/examples/features/pause\_resume](https://github.com/vllm-project/vllm/tree/main/examples/features/pause_resume).

## Data Parallel Pause Resume[¶](#data-parallel-pause-resume "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
Test pause/resume with Data Parallel (DP) via HTTP API.

This example demonstrates coordinated pause/resume across multiple DP ranks.
The pause synchronizes across all DP engines via all-reduce.

Prerequisites:
    Start a vLLM server with data parallelism:

    $ VLLM_SERVER_DEV_MODE=1 vllm serve facebook/opt-125m \
        --enforce-eager \
        --data-parallel-size 4 \
        --tensor-parallel-size 1

    Then run this script:

    $ python data_parallel_pause_resume.py

The test verifies pause works by:
1. Starting a streaming generation request
2. Pausing the server mid-generation
3. Sleeping for PAUSE_DURATION seconds
4. Resuming the server
5. Verifying there was a gap in token generation matching the pause duration
"""

importargparse
importthreading
importtime

importrequests
fromopenaiimport OpenAI

BASE_URL = "http://localhost:8000"
MODEL_NAME = "facebook/opt-125m"
PAUSE_DURATION = 3.0


defpause_generation(base_url: str, mode: str = "keep") -> None:
"""Pause generation via HTTP endpoint."""
    url = f"{base_url}/pause"
    response = requests.post(url, params={"mode": mode}, timeout=60)
    response.raise_for_status()
    print("Server paused")


defresume_generation(base_url: str) -> None:
"""Resume generation via HTTP endpoint."""
    url = f"{base_url}/resume"
    response = requests.post(url, timeout=60)
    response.raise_for_status()
    print("Server resumed")


defmain():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default=BASE_URL)
    parser.add_argument("--model", default=MODEL_NAME)
    args = parser.parse_args()

    client = OpenAI(
        base_url=f"{args.base_url}/v1",
        api_key="EMPTY",
    )

    prompt = "Write a long story about a dragon. Once upon a time"
    token_times: list[float] = []
    pause_token_idx = 0
    pause_triggered = threading.Event()

    defgenerator_thread():
"""Stream tokens and record timestamps."""
        stream = client.completions.create(
            model=args.model,
            prompt=prompt,
            max_tokens=50,
            stream=True,
        )
        for chunk in stream:
            if chunk.choices[0].text:
                token_times.append(time.monotonic())
                token_count = len(token_times)
                print(f"Token {token_count}: {chunk.choices[0].text!r}")

                # Signal controller after some tokens
                if token_count >= 5 and not pause_triggered.is_set():
                    pause_triggered.set()

    defcontroller_thread():
"""Pause and resume the server."""
        nonlocal pause_token_idx

        # Wait for some tokens
        pause_triggered.wait()

        print(f"\nPausing server (keep mode) at token {len(token_times)}...")
        pause_generation(args.base_url, mode="keep")
        pause_token_idx = len(token_times)
        print(f"Sleeping for {PAUSE_DURATION}s...")

        time.sleep(PAUSE_DURATION)

        print("Resuming server...")
        resume_generation(args.base_url)
        print("Resumed!\n")

    # Run both threads
    gen_thread = threading.Thread(target=generator_thread)
    ctrl_thread = threading.Thread(target=controller_thread)

    gen_thread.start()
    ctrl_thread.start()

    gen_thread.join()
    ctrl_thread.join()

    # Check gap at the pause point
    if pause_token_idx < len(token_times):
        pause_gap = token_times[pause_token_idx] - token_times[pause_token_idx - 1]
        print(
            f"\nGap after pause (token {pause_token_idx} -> "
            f"{pause_token_idx+1}): {pause_gap:.3f}s"
        )
        if pause_gap >= PAUSE_DURATION * 0.9:
            print("Test passed! Pause synchronized across DP ranks.")
        else:
            print(f"Test failed! Expected ~{PAUSE_DURATION}s gap, got {pause_gap:.3f}s")
    else:
        print("Test failed! No tokens were generated after resuming.")


if __name__ == "__main__":
    main()
```

## Pause Resume Offline[¶](#pause-resume-offline "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""Test for pause/resume with keep mode.

This test uses concurrent tasks to verify the engine truly stops generating
during pause:
1. Generator task: continuously generates and logs time between tokens
2. Controller task: sends pause/resume commands

If the engine properly pauses, we should see a gap in token timestamps
matching the pause duration.
"""

importasyncio
importtime

fromvllmimport SamplingParams
fromvllm.engine.arg_utilsimport AsyncEngineArgs
fromvllm.v1.engine.async_llmimport AsyncLLM

PAUSE_DURATION = 3.0  # seconds


async defmain():
    # Create engine with a small model
    engine_args = AsyncEngineArgs(
        model="facebook/opt-125m",
        enforce_eager=True,
    )
    engine = AsyncLLM.from_engine_args(engine_args)

    prompt = "Write a story about a dragon. Once upon a time"
    sampling_params = SamplingParams(max_tokens=30, ignore_eos=True)

    # Track token arrival times
    token_times: list[tuple[int, float]] = []  # (token_count, timestamp)
    pause_time: float = 0
    resume_time: float = 0
    pause_token_idx: int = 0  # Index in token_times when pause occurred

    async defgenerator_task():
"""Generate tokens and record timestamps."""
        async for output in engine.generate(
            request_id="test-req",
            prompt=prompt,
            sampling_params=sampling_params,
        ):
            token_count = len(output.outputs[0].token_ids)
            token_times.append((token_count, time.monotonic()))
            print(
                f"Token {token_count} arrived:"
                f"T={token_times[-1][1]-token_times[0][1]:.3f}s"
            )
        return output

    async defcontroller_task():
"""Pause and resume the engine after some tokens generated."""
        nonlocal pause_time, resume_time, pause_token_idx

        # Wait for some tokens to be generated
        while len(token_times) < 5:
            await asyncio.sleep(0.01)

        print(f"\nPausing engine (keep mode) at token {len(token_times)}")
        pause_time = time.monotonic()
        await engine.pause_generation(mode="keep")
        pause_token_idx = len(token_times)
        print(f"Paused! Sleeping for {PAUSE_DURATION}s...")

        # Sleep while paused - no tokens should be generated during this time
        await asyncio.sleep(PAUSE_DURATION)

        print("Resuming engine...")
        await engine.resume_generation()
        resume_time = time.monotonic()
        print("Resumed!\n")

    # Run both tasks concurrently
    gen_task = asyncio.create_task(generator_task())
    ctrl_task = asyncio.create_task(controller_task())

    final_output, _ = await asyncio.gather(gen_task, ctrl_task)

    # Verify the pause actually stopped generation.
    # The gap after the pause token should be approximately the sleep duration.
    pause_gap = token_times[pause_token_idx][1] - token_times[pause_token_idx - 1][1]
    print(
        f"\nGap after pause (token {pause_token_idx-1} -> {pause_token_idx}): "
        f"{pause_gap:.3f}s"
    )
    if pause_gap >= PAUSE_DURATION * 0.9:
        print(f"✓ Test passed! Engine paused for ~{pause_gap:.1f}s")
    else:
        print(
            f"✗ Test failed! Expected ~{PAUSE_DURATION}s gap after pause, "
            f"got {pause_gap:.3f}s"
        )
        raise AssertionError("Engine did not properly pause")

    # Verify request completed
    assert final_output.finished, "Request should have finished"
    assert len(final_output.outputs[0].token_ids) == 30, "Should have all tokens"

    engine.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
```