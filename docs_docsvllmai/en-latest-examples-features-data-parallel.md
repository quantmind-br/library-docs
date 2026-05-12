---
title: Data Parallel - vLLM
url: https://docs.vllm.ai/en/latest/examples/features/data_parallel/
source: sitemap
fetched_at: 2026-05-07T21:12:50.78595276-03:00
rendered_js: false
word_count: 13
summary: This document provides example implementations and configurations for enabling data parallel inference across single and multi-node environments using the vLLM library.
tags:
    - vllm
    - data-parallelism
    - distributed-inference
    - multi-node
    - high-performance-computing
    - llm-serving
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/features/data_parallel.md "Edit this page")

Source [https://github.com/vllm-project/vllm/tree/main/examples/features/data\_parallel](https://github.com/vllm-project/vllm/tree/main/examples/features/data_parallel).

## Data Parallel Offline[¶](#data-parallel-offline "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
Usage:
Single node:
    python examples/features/data_parallel/data_parallel_offline.py \
            --model="ibm-research/PowerMoE-3b" \
            -dp=2 \
            -tp=2

Multi-node:
    Node 0 (assume the node has ip of 10.99.48.128):
            python examples/features/data_parallel/data_parallel_offline.py \
                    --model="ibm-research/PowerMoE-3b" \
                    -dp=2 \
                    -tp=2 \
                    --dp-num-nodes=2 \
                    --dp-node-rank=0 \
                    --dp-master-addr=10.99.48.128 \
                    --dp-master-port=13345
    Node 1:
            python examples/features/data_parallel/data_parallel_offline.py \
                    --model="ibm-research/PowerMoE-3b" \
                    -dp=2 \
                    -tp=2 \
                    --dp-num-nodes=2 \
                    --dp-node-rank=1 \
                    --dp-master-addr=10.99.48.128 \
                    --dp-master-port=13345
"""

importos
fromtimeimport sleep

fromvllmimport LLM, EngineArgs, SamplingParams
fromvllm.platformsimport current_platform
fromvllm.utils.argparse_utilsimport FlexibleArgumentParser
fromvllm.utils.network_utilsimport get_open_port


defcreate_parser():
    parser = FlexibleArgumentParser(description="Data Parallel Inference")

    # Add all engine args
    EngineArgs.add_cli_args(parser)
    parser.set_defaults(
        model="ibm-research/PowerMoE-3b",
        enable_expert_parallel=True,
    )

    # Add DP-specific args (separate from engine args to avoid conflicts)
    parser.add_argument(
        "--dp-num-nodes",
        type=int,
        default=1,
        help="Total number of nodes for data parallel.",
    )
    parser.add_argument(
        "--dp-node-rank",
        type=int,
        default=0,
        help="Rank of the current node for data parallel.",
    )
    parser.add_argument(
        "--dp-master-addr",
        type=str,
        default="",
        help="Master node IP address for DP coordination.",
    )
    parser.add_argument(
        "--dp-master-port",
        type=int,
        default=0,
        help="Master node port for DP coordination.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=300,
        help="Number of seconds before unresponsive process is killed.",
    )

    return parser


defmain(
    dp_size,
    local_dp_rank,
    global_dp_rank,
    dp_master_ip,
    dp_master_port,
    engine_args,
):
    os.environ["VLLM_DP_RANK"] = str(global_dp_rank)
    os.environ["VLLM_DP_RANK_LOCAL"] = str(local_dp_rank)
    os.environ["VLLM_DP_SIZE"] = str(dp_size)
    os.environ["VLLM_DP_MASTER_IP"] = dp_master_ip
    os.environ["VLLM_DP_MASTER_PORT"] = str(dp_master_port)

    # CUDA_VISIBLE_DEVICES for each DP rank is set automatically inside the
    # engine processes.

    # Sample prompts.
    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        "The capital of France is",
        "The future of AI is",
    ] * 100

    # with DP, each rank should process different prompts.
    # usually all the DP ranks process a full dataset,
    # and each rank processes a different part of the dataset.
    floor = len(prompts) // dp_size
    remainder = len(prompts) % dp_size

    # Distribute prompts into even groups.
    defstart(rank):
        return rank * floor + min(rank, remainder)

    prompts = prompts[start(global_dp_rank) : start(global_dp_rank + 1)]
    if len(prompts) == 0:
        # if any rank has no prompts to process,
        # we need to set a placeholder prompt
        prompts = ["Placeholder"]
    print(f"DP rank {global_dp_rank} needs to process {len(prompts)} prompts")

    # Create a sampling params object.
    # since we are doing data parallel, every rank can have different
    # sampling params. here we set different max_tokens for different
    # ranks for demonstration.
    sampling_params = SamplingParams(
        temperature=0.8, top_p=0.95, max_tokens=[16, 20][global_dp_rank % 2]
    )

    # Create an LLM.
    llm = LLM(**engine_args)
    outputs = llm.generate(prompts, sampling_params)
    # Print the outputs.
    for i, output in enumerate(outputs):
        if i >= 5:
            # print only 5 outputs
            break
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(
            f"DP rank {global_dp_rank}, Prompt: {prompt!r}, "
            f"Generated text: {generated_text!r}"
        )

    # Give engines time to pause their processing loops before exiting.
    sleep(1)


if __name__ == "__main__":
    parser = create_parser()
    args = vars(parser.parse_args())

    # Extract DP-specific args (pop to remove from engine_args)
    dp_size = args.pop("data_parallel_size")
    dp_num_nodes = args.pop("dp_num_nodes")
    dp_node_rank = args.pop("dp_node_rank")
    dp_master_addr = args.pop("dp_master_addr")
    dp_master_port = args.pop("dp_master_port")
    timeout = args.pop("timeout")

    # Remaining args are engine args
    engine_args = args

    if dp_num_nodes == 1:
        dp_master_ip = "127.0.0.1"
        dp_master_port_val = get_open_port()
    else:
        dp_master_ip = dp_master_addr
        dp_master_port_val = dp_master_port

    assert dp_size % dp_num_nodes == 0, "dp_size should be divisible by dp_num_nodes"
    dp_per_node = dp_size // dp_num_nodes

    frommultiprocessingimport Process

    if current_platform.is_rocm():
        frommultiprocessingimport set_start_method

        set_start_method("spawn", force=True)

    procs = []
    for local_dp_rank, global_dp_rank in enumerate(
        range(dp_node_rank * dp_per_node, (dp_node_rank + 1) * dp_per_node)
    ):
        proc = Process(
            target=main,
            args=(
                dp_size,
                local_dp_rank,
                global_dp_rank,
                dp_master_ip,
                dp_master_port_val,
                engine_args,
            ),
        )
        proc.start()
        procs.append(proc)
    exit_code = 0
    for proc in procs:
        proc.join(timeout=timeout)
        if proc.exitcode is None:
            print(f"Killing process {proc.pid} that didn't stop within 5 minutes.")
            proc.kill()
            exit_code = 1
        elif proc.exitcode:
            exit_code = proc.exitcode

    exit(exit_code)
```

## Multi Instance Data Parallel[¶](#multi-instance-data-parallel "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
importasyncio
importthreading

fromvllm.engine.arg_utilsimport AsyncEngineArgs
fromvllm.engine.async_llm_engineimport AsyncLLMEngine
fromvllm.outputsimport RequestOutput
fromvllm.sampling_paramsimport SamplingParams
fromvllm.v1.metrics.loggersimport AggregatedLoggingStatLogger

"""
To run this example, run the following commands simultaneously with
different CUDA_VISIBLE_DEVICES:
    python examples/features/data_parallel/multi_instance_data_parallel.py

    vllm serve ibm-research/PowerMoE-3b -dp 2 -dpr 1 \
        --data-parallel-address 127.0.0.1 --data-parallel-rpc-port 62300 \
        --data-parallel-size-local 1 --enforce-eager --headless

Once both instances have completed the handshake, this example will
send a request to the instance with DP rank 1.
"""


def_do_background_logging(engine, interval, stop_event):
    try:
        while not stop_event.is_set():
            asyncio.run(engine.do_log_stats())
            stop_event.wait(interval)
    except Exception as e:
        print(f"vLLM background logging shutdown: {e}")
        pass


async defmain():
    engine_args = AsyncEngineArgs(
        model="ibm-research/PowerMoE-3b",
        data_parallel_size=2,
        tensor_parallel_size=1,
        dtype="auto",
        max_model_len=2048,
        data_parallel_address="127.0.0.1",
        data_parallel_rpc_port=62300,
        data_parallel_size_local=1,
        enforce_eager=True,
        enable_log_requests=True,
        disable_custom_all_reduce=True,
    )

    engine_client = AsyncLLMEngine.from_engine_args(
        engine_args,
        # Example: Using aggregated logger
        stat_loggers=[AggregatedLoggingStatLogger],
    )
    stop_logging_event = threading.Event()
    logging_thread = threading.Thread(
        target=_do_background_logging,
        args=(engine_client, 5, stop_logging_event),
        daemon=True,
    )
    logging_thread.start()
    sampling_params = SamplingParams(
        temperature=0.7,
        top_p=0.9,
        max_tokens=100,
    )
    num_prompts = 10
    for i in range(num_prompts):
        prompt = "Who won the 2004 World Series?"
        final_output: RequestOutput | None = None
        async for output in engine_client.generate(
            prompt=prompt,
            sampling_params=sampling_params,
            request_id=f"abcdef-{i}",
            data_parallel_rank=1,
        ):
            final_output = output
        if final_output:
            print(final_output.outputs[0].text)

    stop_logging_event.set()
    logging_thread.join()


if __name__ == "__main__":
    asyncio.run(main())
```