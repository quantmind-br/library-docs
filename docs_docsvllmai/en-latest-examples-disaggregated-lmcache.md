---
title: LMCache Examples - vLLM
url: https://docs.vllm.ai/en/latest/examples/disaggregated/lmcache/
source: sitemap
fetched_at: 2026-05-07T21:12:45.023476784-03:00
rendered_js: false
word_count: 1211
summary: This document provides examples and scripts for integrating LMCache with vLLM to enable disaggregated prefilling, KV cache sharing, and CPU memory offloading.
tags:
    - vllm
    - lmcache
    - kv-cache
    - disaggregated-prefill
    - gpu-optimization
    - cpu-offloading
    - llm-inference
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/disaggregated/lmcache.md "Edit this page")

Source [https://github.com/vllm-project/vllm/tree/main/examples/disaggregated/lmcache](https://github.com/vllm-project/vllm/tree/main/examples/disaggregated/lmcache).

This folder demonstrates how to use LMCache for disaggregated prefilling, CPU offloading and KV cache sharing.

## 1. Disaggregated Prefill in vLLM v1[¶](#1-disaggregated-prefill-in-vllm-v1 "Permanent link")

This example demonstrates how to run LMCache with disaggregated prefill using NIXL on a single node.

### Prerequisites[¶](#prerequisites "Permanent link")

- Install [LMCache](https://github.com/LMCache/LMCache). You can simply run `pip install lmcache`.
- Install [NIXL](https://github.com/ai-dynamo/nixl).
- At least 2 GPUs
- Valid Hugging Face token (HF\_TOKEN) for Llama 3.1 8B Instruct.

### Usage[¶](#usage "Permanent link")

Run `cd disagg_prefill_lmcache_v1` to get into `disagg_prefill_lmcache_v1` folder, and then run

```
bashdisagg_example_nixl.sh
```

to run disaggregated prefill and benchmark the performance.

### Components[¶](#components "Permanent link")

#### Server Scripts[¶](#server-scripts "Permanent link")

- `disagg_prefill_lmcache_v1/disagg_vllm_launcher.sh` - Launches individual vLLM servers for prefill/decode, and also launches the proxy server.
- `disagg_prefill_lmcache_v1/disagg_proxy_server.py` - FastAPI proxy server that coordinates between prefiller and decoder
- `disagg_prefill_lmcache_v1/disagg_example_nixl.sh` - Main script to run the example

#### Configuration[¶](#configuration "Permanent link")

- `disagg_prefill_lmcache_v1/configs/lmcache-prefiller-config.yaml` - Configuration for prefiller server
- `disagg_prefill_lmcache_v1/configs/lmcache-decoder-config.yaml` - Configuration for decoder server

#### Log Files[¶](#log-files "Permanent link")

The main script generates several log files:

- `prefiller.log` - Logs from the prefill server
- `decoder.log` - Logs from the decode server
- `proxy.log` - Logs from the proxy server

## 2. CPU Offload Examples[¶](#2-cpu-offload-examples "Permanent link")

- `python cpu_offload_lmcache.py -v v0` - CPU offloading implementation for vLLM v0
- `python cpu_offload_lmcache.py -v v1` - CPU offloading implementation for vLLM v1

## 3. KV Cache Sharing[¶](#3-kv-cache-sharing "Permanent link")

The `kv_cache_sharing_lmcache_v1.py` example demonstrates how to share KV caches between vLLM v1 instances.

## 4. Disaggregated Prefill in vLLM v0[¶](#4-disaggregated-prefill-in-vllm-v0 "Permanent link")

The `disaggregated_prefill_lmcache_v0.py` provides an example of how to run disaggregated prefill in vLLM v0.

## Example materials[¶](#example-materials "Permanent link")

cpu\_offload\_lmcache.py

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
This file demonstrates the example usage of cpu offloading
with LMCache in vLLM v1 or v0.

Usage:

    Specify vLLM version

    -v v0 : Use LMCacheConnector
            model = mistralai/Mistral-7B-Instruct-v0.2
            (Includes enable_chunked_prefill = True)

    -v v1 : Use LMCacheConnectorV1 (default)
            model = meta-llama/Meta-Llama-3.1-8B-Instruct
            (Without enable_chunked_prefill)

Note that `lmcache` is needed to run this example.
Requirements:
https://docs.lmcache.ai/getting_started/installation.html#prerequisites
Learn more about LMCache environment setup, please refer to:
https://docs.lmcache.ai/getting_started/installation.html
"""

importargparse
importcontextlib
importos
importtime
fromdataclassesimport asdict

fromlmcache.integration.vllm.utilsimport ENGINE_NAME
fromlmcache.v1.cache_engineimport LMCacheEngineBuilder

fromvllmimport LLM, SamplingParams
fromvllm.configimport KVTransferConfig
fromvllm.engine.arg_utilsimport EngineArgs


defsetup_environment_variables():
    # LMCache-related environment variables
    # Use experimental features in LMCache
    os.environ["LMCACHE_USE_EXPERIMENTAL"] = "True"
    # LMCache is set to use 256 tokens per chunk
    os.environ["LMCACHE_CHUNK_SIZE"] = "256"
    # Enable local CPU backend in LMCache
    os.environ["LMCACHE_LOCAL_CPU"] = "True"
    # Set local CPU memory limit to 5.0 GB
    os.environ["LMCACHE_MAX_LOCAL_CPU_SIZE"] = "5.0"


@contextlib.contextmanager
defbuild_llm_with_lmcache(lmcache_connector: str, model: str):
    ktc = KVTransferConfig(
        kv_connector=lmcache_connector,
        kv_role="kv_both",
    )
    # Set GPU memory utilization to 0.8 for an A40 GPU with 40GB
    # memory. Reduce the value if your GPU has less memory.
    # Note: LMCache supports chunked prefill (see vLLM#14505, LMCache#392).
    llm_args = EngineArgs(
        model=model,
        kv_transfer_config=ktc,
        max_model_len=8000,
        gpu_memory_utilization=0.8,
    )

    llm = LLM(**asdict(llm_args))
    try:
        yield llm
    finally:
        # Clean up lmcache backend
        LMCacheEngineBuilder.destroy(ENGINE_NAME)


defprint_output(
    llm: LLM,
    prompt: list[str],
    sampling_params: SamplingParams,
    req_str: str,
):
    # Should be able to see logs like the following:
    # `LMCache INFO: Storing KV cache for 6006 out of 6006 tokens for request 0`
    # This indicates that the KV cache has been stored in LMCache.
    start = time.time()
    outputs = llm.generate(prompt, sampling_params)
    print("-" * 50)
    for output in outputs:
        generated_text = output.outputs[0].text
        print(f"Generated text: {generated_text!r}")
    print(f"Generation took {time.time()-start:.2f} seconds, {req_str} request done.")
    print("-" * 50)


defparse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v",
        "--version",
        choices=["v0", "v1"],
        default="v1",
        help="Specify vLLM version (default: v1)",
    )
    return parser.parse_args()


defmain():
    lmcache_connector = "LMCacheConnectorV1"
    model = "meta-llama/Meta-Llama-3.1-8B-Instruct"
    setup_environment_variables()
    with build_llm_with_lmcache(lmcache_connector, model) as llm:
        # This example script runs two requests with a shared prefix.
        # Define the shared prompt and specific prompts
        shared_prompt = "Hello, how are you?" * 1000
        first_prompt = [
            shared_prompt + "Hello, my name is",
        ]
        second_prompt = [
            shared_prompt + "Tell me a very long story",
        ]

        sampling_params = SamplingParams(temperature=0, top_p=0.95, max_tokens=10)

        # Print the first output
        print_output(llm, first_prompt, sampling_params, "first")

        time.sleep(1)

        # print the second output
        print_output(llm, second_prompt, sampling_params, "second")


if __name__ == "__main__":
    main()
```

disagg\_prefill\_lmcache\_v0.py

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
This file demonstrates the example usage of disaggregated prefilling
with LMCache.
We will launch 2 vllm instances (GPU 0 for prefill and GPU 1 for decode),
and launch an additional LMCache server.
KV cache is transferred in the following manner:
vLLM prefill node -> LMCache server -> vLLM decode node.

Note that `pip install lmcache` is needed to run this example.
Learn more about LMCache in https://github.com/LMCache/LMCache.
"""

importos
importsubprocess
importtime
frommultiprocessingimport Event, Process

fromlmcache.experimental.cache_engineimport LMCacheEngineBuilder
fromlmcache.integration.vllm.utilsimport ENGINE_NAME

fromvllmimport LLM, SamplingParams
fromvllm.configimport KVTransferConfig

# LMCache-related environment variables
# The port to start LMCache server
port = 8100
# Use experimental features in LMCache
os.environ["LMCACHE_USE_EXPERIMENTAL"] = "True"
# LMCache is set to use 256 tokens per chunk
os.environ["LMCACHE_CHUNK_SIZE"] = "256"
# Disable local CPU backend in LMCache
os.environ["LMCACHE_LOCAL_CPU"] = "False"
# Set local CPU memory buffer limit to 5.0 GB
os.environ["LMCACHE_MAX_LOCAL_CPU_SIZE"] = "5.0"
# Set the remote URL for LMCache server
os.environ["LMCACHE_REMOTE_URL"] = f"lm://localhost:{port}"
# Set the serializer/deserializer between vllm and LMCache server
# `naive` indicates using raw bytes of the tensor without any compression
os.environ["LMCACHE_REMOTE_SERDE"] = "naive"

prompts = [
    "Hello, how are you?" * 1000,
]


defrun_prefill(prefill_done, prompts):
    # We use GPU 0 for prefill node.
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"

    sampling_params = SamplingParams(temperature=0, top_p=0.95, max_tokens=1)

    ktc = KVTransferConfig(
        kv_connector="LMCacheConnector",
        kv_role="kv_producer",
        kv_rank=0,
        kv_parallel_size=2,
    )
    # Set GPU memory utilization to 0.8 for an A40 GPU with 40GB
    # memory. Reduce the value if your GPU has less memory.
    llm = LLM(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        kv_transfer_config=ktc,
        max_model_len=8000,
        gpu_memory_utilization=0.8,
        enforce_eager=True,
    )

    # llm.generate(prompts, sampling_params)
    outputs = llm.generate(prompts, sampling_params)
    for output in outputs:
        generated_text = output.outputs[0].text
        print(f"Generated text: {generated_text!r}")
    print("Prefill node is finished.")
    prefill_done.set()

    # Clean up lmcache backend
    LMCacheEngineBuilder.destroy(ENGINE_NAME)


defrun_decode(prefill_done, prompts, timeout=1):
    # We use GPU 1 for decode node.
    os.environ["CUDA_VISIBLE_DEVICES"] = "1"

    sampling_params = SamplingParams(temperature=0, top_p=0.95, max_tokens=10)

    ktc = KVTransferConfig(
        kv_connector="LMCacheConnector",
        kv_role="kv_consumer",
        kv_rank=1,
        kv_parallel_size=2,
    )
    # Set GPU memory utilization to 0.8 for an A40 GPU with 40GB
    # of memory. Reduce the value if your GPU has less memory.
    llm = LLM(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        kv_transfer_config=ktc,
        max_model_len=8000,
        gpu_memory_utilization=0.8,
        enforce_eager=True,
    )

    print("Waiting for prefill node to finish...")
    prefill_done.wait()
    time.sleep(timeout)

    outputs = llm.generate(prompts, sampling_params)
    for output in outputs:
        generated_text = output.outputs[0].text
        print(f"Generated text: {generated_text!r}")

    # Clean up lmcache backend
    LMCacheEngineBuilder.destroy(ENGINE_NAME)


defrun_lmcache_server(port):
    server_proc = subprocess.Popen(
        ["python", "-m", "lmcache.experimental.server", "localhost", str(port)]
    )
    return server_proc


defmain():
    prefill_done = Event()
    prefill_process = Process(target=run_prefill, args=(prefill_done, prompts))
    decode_process = Process(target=run_decode, args=(prefill_done, prompts))
    lmcache_server_process = run_lmcache_server(port)

    # Start prefill node
    prefill_process.start()

    # Start decode node
    decode_process.start()

    # Clean up the processes
    decode_process.join()
    prefill_process.terminate()
    lmcache_server_process.terminate()
    lmcache_server_process.wait()


if __name__ == "__main__":
    main()
```

disagg\_prefill\_lmcache\_v1/configs/lmcache-decoder-config.yaml

```
local_cpu:False
max_local_cpu_size:0
#local_disk: 
max_local_disk_size:0
remote_serde:NULL

enable_nixl:True
nixl_role:"receiver"
nixl_peer_host:"localhost"
nixl_peer_port:55555
nixl_buffer_size:1073741824# 1GB
nixl_buffer_device:"cuda"
nixl_enable_gc:True
```

disagg\_prefill\_lmcache\_v1/configs/lmcache-prefiller-config.yaml

```
local_cpu:False
max_local_cpu_size:0
#local_disk: 
max_local_disk_size:0
remote_serde:NULL

enable_nixl:True
nixl_role:"sender"
nixl_peer_host:"localhost"
nixl_peer_port:55555
nixl_buffer_size:1073741824# 1GB
nixl_buffer_device:"cuda"
nixl_enable_gc:True
```

disagg\_prefill\_lmcache\_v1/disagg\_example\_nixl.sh

```
#!/bin/bash

echo"Warning: LMCache disaggregated prefill support for vLLM v1 is experimental and subject to change."


PIDS=()

# Switch to the directory of the current script
cd"$(dirname"${BASH_SOURCE[0]}")"

check_hf_token(){
if[-z"$HF_TOKEN"];then
echo"HF_TOKEN is not set. Please set it to your Hugging Face token."
exit1
fi
if[["$HF_TOKEN"!=hf_*]];then
echo"HF_TOKEN is not a valid Hugging Face token. Please set it to your Hugging Face token."
exit1
fi
echo"HF_TOKEN is set and valid."
}

check_num_gpus(){
# can you check if the number of GPUs are >=2 via nvidia-smi/rocm-smi?
if!whichrocm-smi>/dev/null2>&1;then
num_gpus=$(nvidia-smi--query-gpu=name--format=csv,noheader|wc-l)
else
num_gpus=$(rocm-smi--showid|grep-cInstinct)
fi

if["$num_gpus"-lt2];then
echo"You need at least 2 GPUs to run disaggregated prefill."
exit1
else
echo"Found $num_gpus GPUs."
fi
}

ensure_python_library_installed(){
echo"Checking if $1 is installed..."
if!python3-c"import $1">/dev/null2>&1;then
if["$1"=="nixl"];then
echo"$1 is not installed. Please refer to https://github.com/ai-dynamo/nixl for installation."
else
echo"$1 is not installed. Please install it via pip install $1."
fi
exit1
else
echo"$1 is installed."
fi
}

cleanup(){
echo"Stopping everything…"
trap-INTTERM# prevent re-entrancy
kill---$$# negative PID  ==  “this whole process-group”
wait# reap children so we don't leave zombies
exit0
}

wait_for_server(){
localport=$1
localtimeout_seconds=1200
localstart_time=$(date+%s)

echo"Waiting for server on port $port..."

whiletrue;do
ifcurl-s"localhost:${port}/v1/completions">/dev/null;then
return0
fi

localnow=$(date+%s)
if((now-start_time>=timeout_seconds));then
echo"Timeout waiting for server"
return1
fi

sleep1
done
}


main(){
check_hf_token
check_num_gpus
ensure_python_library_installedlmcache
ensure_python_library_installednixl
ensure_python_library_installedpandas
ensure_python_library_installeddatasets
ensure_python_library_installedvllm

trapcleanupINT
trapcleanupUSR1
trapcleanupTERM

echo"Launching prefiller, decoder and proxy..."
echo"Please check prefiller.log, decoder.log and proxy.log for logs."

bashdisagg_vllm_launcher.shprefiller\
>>(teeprefiller.log)2>&1&
prefiller_pid=$!
PIDS+=("$prefiller_pid")

bashdisagg_vllm_launcher.shdecoder\
>>(teedecoder.log)2>&1&
decoder_pid=$!
PIDS+=("$decoder_pid")

python3disagg_proxy_server.py\
--hostlocalhost\
--port9000\
--prefiller-hostlocalhost\
--prefiller-port8100\
--decoder-hostlocalhost\
--decoder-port8200\
>>(teeproxy.log)2>&1&
proxy_pid=$!
PIDS+=("$proxy_pid")

wait_for_server8100
wait_for_server8200
wait_for_server9000

echo"All servers are up. Starting benchmark..."

# begin benchmark
cd../../../../benchmarks/
vllmbenchserve--port9000--seed"$(date+%s)"\
--modelmeta-llama/Llama-3.1-8B-Instruct\
--dataset-namerandom--random-input-len7500--random-output-len200\
--num-prompts200--burstiness100--request-rate3.6|teebenchmark.log

echo"Benchmarking done. Cleaning up..."

cleanup

}

main
```

disagg\_prefill\_lmcache\_v1/disagg\_proxy\_server.py

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

importargparse
importos
importtime
fromcontextlibimport asynccontextmanager

importhttpx
importnumpyasnp
fromfastapiimport FastAPI, Request
fromfastapi.responsesimport StreamingResponse


@asynccontextmanager
async deflifespan(app: FastAPI):
"""
    Lifespan context manager to handle startup and shutdown events.
    """
    # Startup: Initialize clients
    prefiller_base_url = (
        f"http://{global_args.prefiller_host}:{global_args.prefiller_port}/v1"
    )
    decoder_base_url = (
        f"http://{global_args.decoder_host}:{global_args.decoder_port}/v1"
    )

    app.state.prefill_client = httpx.AsyncClient(
        timeout=None,
        base_url=prefiller_base_url,
        limits=httpx.Limits(
            max_connections=None,
            max_keepalive_connections=None,
        ),
    )
    app.state.decode_client = httpx.AsyncClient(
        timeout=None,
        base_url=decoder_base_url,
        limits=httpx.Limits(
            max_connections=None,
            max_keepalive_connections=None,
        ),
    )

    yield

    # Shutdown: Close clients
    await app.state.prefill_client.aclose()
    await app.state.decode_client.aclose()


# Update FastAPI app initialization to use lifespan
app = FastAPI(lifespan=lifespan)


classStatsCalculator:
    def__init__(self):
        self._stats = []
        self._last_log_time = time.time()

    defadd(self, value):
        self._stats.append(value)
        if time.time() - self._last_log_time > 5:
            self._log_stats()
            self._last_log_time = time.time()

    def_log_stats(self):
        # Print average, median, and 99th percentile
        np_arr = np.array(self._stats)
        output_str = (
            f"\nNum requests: {len(self._stats)}"
            "\nPrefill node TTFT stats:"
            f"\n - Average (ms): {np.mean(np_arr)}"
            f"\n - Median (ms): {np.median(np_arr)}"
            f"\n - 99th Percentile (ms): {np.percentile(np_arr,99)}\n"
        )
        print(
            "===============================",
            output_str,
            "===============================",
        )


stats_calculator = StatsCalculator()
counter = 0


defparse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--host", type=str, default="localhost")
    parser.add_argument("--prefiller-host", type=str, default="localhost")
    parser.add_argument("--prefiller-port", type=int, default=8100)
    parser.add_argument("--decoder-host", type=str, default="localhost")
    parser.add_argument("--decoder-port", type=int, default=8200)
    args = parser.parse_args()
    return args


# Initialize variables to hold the persistent clients
app.state.prefill_client = None
app.state.decode_client = None


async defsend_request_to_service(
    client: httpx.AsyncClient, endpoint: str, req_data: dict
):
"""
    Send a request to a service using a persistent client.
    """
    req_data = req_data.copy()
    req_data["max_tokens"] = 1
    if "max_completion_tokens" in req_data:
        req_data["max_completion_tokens"] = 1

    headers = {"Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}"}
    response = await client.post(endpoint, json=req_data, headers=headers)
    response.raise_for_status()

    # read/consume the response body to release the connection
    # otherwise, it would http.ReadError
    await response.aread()

    return response


async defstream_service_response(
    client: httpx.AsyncClient, endpoint: str, req_data: dict
):
"""
    Asynchronously stream the response from a service using a persistent client.
    """
    headers = {"Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}"}
    async with client.stream(
        "POST", endpoint, json=req_data, headers=headers
    ) as response:
        response.raise_for_status()
        async for chunk in response.aiter_bytes():
            yield chunk


@app.post("/v1/completions")
async defhandle_completions(request: Request):
    global counter, stats_calculator
    counter += 1

    st = time.time()
    try:
        req_data = await request.json()

        # Send request to prefill service, ignore the response
        await send_request_to_service(
            app.state.prefill_client, "/completions", req_data
        )

        et = time.time()
        stats_calculator.add(et - st)

        # Stream response from decode service
        async defgenerate_stream():
            async for chunk in stream_service_response(
                app.state.decode_client, "/completions", req_data
            ):
                yield chunk

        return StreamingResponse(generate_stream(), media_type="text/event-stream")

    except Exception as e:
        importsys
        importtraceback

        exc_info = sys.exc_info()
        print("Error occurred in disagg prefill proxy server - completions endpoint")
        print(e)
        print("".join(traceback.format_exception(*exc_info)))
        raise


@app.post("/v1/chat/completions")
async defhandle_chat_completions(request: Request):
    global counter, stats_calculator
    counter += 1

    st = time.time()
    try:
        req_data = await request.json()

        # Send request to prefill service, ignore the response
        await send_request_to_service(
            app.state.prefill_client, "/chat/completions", req_data
        )

        et = time.time()
        stats_calculator.add(et - st)

        # Stream response from decode service
        async defgenerate_stream():
            async for chunk in stream_service_response(
                app.state.decode_client, "/chat/completions", req_data
            ):
                yield chunk

        return StreamingResponse(generate_stream(), media_type="text/event-stream")

    except Exception as e:
        importsys
        importtraceback

        exc_info = sys.exc_info()
        print(
            "Error occurred in disagg prefill proxy server  - chat completions endpoint"
        )
        print(e)
        print("".join(traceback.format_exception(*exc_info)))
        raise


if __name__ == "__main__":
    global global_args
    global_args = parse_args()

    importuvicorn

    uvicorn.run(app, host=global_args.host, port=global_args.port)
```

disagg\_prefill\_lmcache\_v1/disagg\_vllm\_launcher.sh

```
#!/bin/bash

SCRIPT_DIR="$(cd"$(dirname"${BASH_SOURCE[0]}")"&&pwd)"

if[[$#-lt1]];then
echo"Usage: $0 <prefiller | decoder> [model]"
exit1
fi

if[[$#-eq1]];then
echo"Using default model: meta-llama/Llama-3.1-8B-Instruct"
MODEL="meta-llama/Llama-3.1-8B-Instruct"
else
echo"Using model: $2"
MODEL=$2
fi

# The prefillers and decoders in LMCache use the same hash seed for all chunk keys.
# This seed must be aligned so that decoders can identify and retrieve KV cache
# entries stored by prefillers.
#
# WARNING: Using a fixed hash seed is insecure and makes the application vulnerable to
# denial-of-service attacks. In a production environment, this should be set to a
# secure random value. This is set to a fixed value for demonstration purposes only.
exportPYTHONHASHSEED=${VLLM_PYTHON_HASH_SEED:-123}

if[[$1=="prefiller"]];then
# Prefiller listens on port 8100
prefill_config_file=$SCRIPT_DIR/configs/lmcache-prefiller-config.yaml

UCX_TLS=cuda_ipc,cuda_copy,tcp\
LMCACHE_CONFIG_FILE=$prefill_config_file\
LMCACHE_USE_EXPERIMENTAL=True\
VLLM_ENABLE_V1_MULTIPROCESSING=1\
VLLM_WORKER_MULTIPROC_METHOD=spawn\
CUDA_VISIBLE_DEVICES=0\
vllmserve"$MODEL"\
--port8100\
--enforce-eager\
--kv-transfer-config\
'{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_producer","kv_connector_extra_config": {"discard_partial_chunks": false, "lmcache_rpc_port": "producer1"}}'


elif[[$1=="decoder"]];then
# Decoder listens on port 8200
decode_config_file=$SCRIPT_DIR/configs/lmcache-decoder-config.yaml

UCX_TLS=cuda_ipc,cuda_copy,tcp\
LMCACHE_CONFIG_FILE=$decode_config_file\
LMCACHE_USE_EXPERIMENTAL=True\
VLLM_ENABLE_V1_MULTIPROCESSING=1\
VLLM_WORKER_MULTIPROC_METHOD=spawn\
CUDA_VISIBLE_DEVICES=1\
vllmserve"$MODEL"\
--port8200\
--enforce-eager\
--kv-transfer-config\
'{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_consumer","kv_connector_extra_config": {"discard_partial_chunks": false, "lmcache_rpc_port": "consumer1"}}'


else
echo"Invalid role: $1"
echo"Should be either prefiller, decoder"
exit1
fi
```

kv\_cache\_sharing\_lmcache\_v1.py

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
This file demonstrates the example usage of remote KV cache sharing
with LMCache.
We will launch 2 vllm instances, and launch an additional LMCache server.
KV cache is transferred in the following manner:
(1) vLLM instance 1 -> LMCache server (KV cache store).
(2) LMCache server -> vLLM instance 2 (KV cache reuse/retrieve).

Note that lmcache needs to be installed to run this example.
Learn more about LMCache in https://github.com/LMCache/LMCache.
"""

importos
importsubprocess
importtime
frommultiprocessingimport Event, Process

fromlmcache.integration.vllm.utilsimport ENGINE_NAME
fromlmcache.v1.cache_engineimport LMCacheEngineBuilder

fromvllmimport LLM, SamplingParams
fromvllm.configimport KVTransferConfig

# LMCache-related environment variables
# The port to start LMCache server
port = 8100
# Use experimental features in LMCache
os.environ["LMCACHE_USE_EXPERIMENTAL"] = "True"
# LMCache is set to use 256 tokens per chunk
os.environ["LMCACHE_CHUNK_SIZE"] = "256"
# Disable local CPU backend in LMCache
os.environ["LMCACHE_LOCAL_CPU"] = "False"
# Set local CPU memory buffer limit to 5.0 GB
os.environ["LMCACHE_MAX_LOCAL_CPU_SIZE"] = "5.0"
# Set the remote URL for LMCache server
os.environ["LMCACHE_REMOTE_URL"] = f"lm://localhost:{port}"
# Set the serializer/deserializer between vllm and LMCache server
# `naive` indicates using raw bytes of the tensor without any compression
os.environ["LMCACHE_REMOTE_SERDE"] = "naive"

prompts = [
    "Hello, how are you?" * 1000,
]


defrun_store(store_done, prompts):
    # We use GPU 0 for KV cache store process.
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"

    sampling_params = SamplingParams(temperature=0, top_p=0.95, max_tokens=10)

    ktc = KVTransferConfig(kv_connector="LMCacheConnectorV1", kv_role="kv_both")
    # Set GPU memory utilization to 0.8 for an A40 GPU with 40GB
    # memory. Reduce the value if your GPU has less memory.
    llm = LLM(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        kv_transfer_config=ktc,
        max_model_len=8000,
        gpu_memory_utilization=0.8,
        enforce_eager=True,
    )

    outputs = llm.generate(prompts, sampling_params)
    for output in outputs:
        generated_text = output.outputs[0].text
        print(f"Generated text: {generated_text!r}")
    print("KV cache store is finished.")
    store_done.set()

    # Clean up lmcache backend
    LMCacheEngineBuilder.destroy(ENGINE_NAME)


defrun_retrieve(store_done, prompts, timeout=1):
    # We use GPU 1 for KV cache retrieve process.
    os.environ["CUDA_VISIBLE_DEVICES"] = "1"

    sampling_params = SamplingParams(temperature=0, top_p=0.95, max_tokens=10)

    ktc = KVTransferConfig(kv_connector="LMCacheConnectorV1", kv_role="kv_both")
    # Set GPU memory utilization to 0.8 for an A40 GPU with 40GB
    # of memory. Reduce the value if your GPU has less memory.
    llm = LLM(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        kv_transfer_config=ktc,
        max_model_len=8000,
        gpu_memory_utilization=0.8,
        enforce_eager=True,
    )

    print("Waiting for KV cache store to finish...")
    store_done.wait()
    time.sleep(timeout)

    outputs = llm.generate(prompts, sampling_params)
    for output in outputs:
        generated_text = output.outputs[0].text
        print(f"Generated text: {generated_text!r}")

    # Clean up lmcache backend
    LMCacheEngineBuilder.destroy(ENGINE_NAME)


defrun_lmcache_server(port):
    server_proc = subprocess.Popen(
        ["python", "-m", "lmcache.v1.server", "localhost", str(port)]
    )
    return server_proc


defmain():
    store_done = Event()
    store_process = Process(target=run_store, args=(store_done, prompts))
    retrieve_process = Process(target=run_retrieve, args=(store_done, prompts))
    lmcache_server_process = run_lmcache_server(port)

    # Start KV cache store process
    store_process.start()

    # Start KV cache retrieve process
    retrieve_process.start()

    # Clean up the processes
    store_process.join()
    retrieve_process.terminate()
    lmcache_server_process.terminate()
    lmcache_server_process.wait()


if __name__ == "__main__":
    main()
```