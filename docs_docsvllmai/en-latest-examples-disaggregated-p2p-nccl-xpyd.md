---
title: P2P NCCL Xpyd - vLLM
url: https://docs.vllm.ai/en/latest/examples/disaggregated/p2p_nccl_xpyd/
source: sitemap
fetched_at: 2026-05-07T21:12:47.120484592-03:00
rendered_js: false
word_count: 16
summary: This document provides a shell script and configuration guide for setting up disaggregated prefill and decode serving in vLLM using the P2P NCCL XpYd architecture.
tags:
    - vllm
    - disaggregated-serving
    - nccl
    - gpu-cluster
    - model-serving
    - distributed-computing
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/disaggregated/p2p_nccl_xpyd.md "Edit this page")

Source [https://github.com/vllm-project/vllm/tree/main/examples/disaggregated/p2p\_nccl\_xpyd](https://github.com/vllm-project/vllm/tree/main/examples/disaggregated/p2p_nccl_xpyd).

## Disagg Example P2P NCCL Xpyd[¶](#disagg-example-p2p-nccl-xpyd "Permanent link")

```
#!/bin/bash

# =============================================================================
# vLLM Disaggregated Serving Script - P2P NCCL XpYd Architecture
# =============================================================================
# This script demonstrates disaggregated prefill and decode serving using
# P2P NCCL communication. The architecture supports various XpYd configurations:
#
# - 1P3D: 1 Prefill server + 3 Decode servers (current default)
# - 3P1D: 3 Prefill servers + 1 Decode server
# - etc.
#
# Configuration can be customized via environment variables:
#   MODEL: Model to serve
#   PREFILL_GPUS: Comma-separated GPU IDs for prefill servers
#   DECODE_GPUS: Comma-separated GPU IDs for decode servers
#   PREFILL_PORTS: Comma-separated ports for prefill servers
#   DECODE_PORTS: Comma-separated ports for decode servers
#   PROXY_PORT: Proxy server port used to setup XpYd connection.
#   TIMEOUT_SECONDS: Server startup timeout
# =============================================================================

# Configuration - can be overridden via environment variables
MODEL=${MODEL:-meta-llama/Llama-3.1-8B-Instruct}
TIMEOUT_SECONDS=${TIMEOUT_SECONDS:-1200}
PROXY_PORT=${PROXY_PORT:-30001}

# Default 1P3D configuration (1 Prefill + 3 Decode)
PREFILL_GPUS=${PREFILL_GPUS:-0}
DECODE_GPUS=${DECODE_GPUS:-1,2,3}
PREFILL_PORTS=${PREFILL_PORTS:-20003}
DECODE_PORTS=${DECODE_PORTS:-20005,20007,20009}

echo"Warning: P2P NCCL disaggregated prefill XpYd support for vLLM v1 is experimental and subject to change."
echo""
echo"Architecture Configuration:"
echo"  Model: $MODEL"
echo"  Prefill GPUs: $PREFILL_GPUS, Ports: $PREFILL_PORTS"
echo"  Decode GPUs: $DECODE_GPUS, Ports: $DECODE_PORTS"
echo"  Proxy Port: $PROXY_PORT"
echo"  Timeout: ${TIMEOUT_SECONDS}s"
echo""

PIDS=()

# Switch to the directory of the current script
cd"$(dirname"${BASH_SOURCE[0]}")"

check_required_files(){
localfiles=("disagg_proxy_p2p_nccl_xpyd.py")
forfilein"${files[@]}";do
if[[!-f"$file"]];then
echo"Required file $file not found in $(pwd)"
exit1
fi
done
}

check_hf_token(){
if[-z"$HF_TOKEN"];then
echo"HF_TOKEN is not set. Please set it to your Hugging Face token."
echo"Example: export HF_TOKEN=your_token_here"
exit1
fi
if[["$HF_TOKEN"!=hf_*]];then
echo"HF_TOKEN is not a valid Hugging Face token. Please set it to your Hugging Face token."
exit1
fi
echo"HF_TOKEN is set and valid."
}

check_num_gpus(){
# Check if the number of GPUs are >=2 via nvidia-smi
num_gpus=$(nvidia-smi--query-gpu=name--format=csv,noheader|wc-l)
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
echo"$1 is not installed. Please install it via pip install $1."
exit1
else
echo"$1 is installed."
fi
}

cleanup(){
echo"Stopping everything…"
trap-INTTERM# prevent re-entrancy
pkill-9-f"disagg_proxy_p2p_nccl_xpyd.py"
kill---$$# negative PID  ==  "this whole process-group"
wait# reap children so we don't leave zombies
exit0
}

wait_for_server(){
localport=$1
localtimeout_seconds=$TIMEOUT_SECONDS
localstart_time=$(date+%s)

echo"Waiting for server on port $port..."

whiletrue;do
ifcurl-s"localhost:${port}/v1/completions">/dev/null;then
echo"Server on port $port is ready."
return0
fi

localnow=$(date+%s)
if((now-start_time>=timeout_seconds));then
echo"Timeout waiting for server on port $port"
return1
fi

sleep1
done
}

main(){
check_required_files
check_hf_token
check_num_gpus
ensure_python_library_installedpandas
ensure_python_library_installeddatasets
ensure_python_library_installedvllm
ensure_python_library_installedquart

trapcleanupINT
trapcleanupUSR1
trapcleanupTERM

echo"Launching disaggregated serving components..."
echo"Please check the log files for detailed output:"
echo"  - prefill*.log: Prefill server logs"
echo"  - decode*.log: Decode server logs"
echo"  - proxy.log: Proxy server log"

# =============================================================================
# Launch Proxy Server
# =============================================================================
echo""
echo"Starting proxy server on port $PROXY_PORT..."
python3disagg_proxy_p2p_nccl_xpyd.py&
PIDS+=($!)

# Parse GPU and port arrays
IFS=','read-raPREFILL_GPU_ARRAY<<<"$PREFILL_GPUS"
IFS=','read-raDECODE_GPU_ARRAY<<<"$DECODE_GPUS"
IFS=','read-raPREFILL_PORT_ARRAY<<<"$PREFILL_PORTS"
IFS=','read-raDECODE_PORT_ARRAY<<<"$DECODE_PORTS"

# =============================================================================
# Launch Prefill Servers (X Producers)
# =============================================================================
echo""
echo"Starting ${#PREFILL_GPU_ARRAY[@]} prefill server(s)..."
foriin"${!PREFILL_GPU_ARRAY[@]}";do
localgpu_id=${PREFILL_GPU_ARRAY[$i]}
localport=${PREFILL_PORT_ARRAY[$i]}
localkv_port=$((21001+i))

echo"  Prefill server $((i+1)): GPU $gpu_id, Port $port, KV Port $kv_port"
CUDA_VISIBLE_DEVICES=$gpu_idvllmserve"$MODEL"\
--enforce-eager\
--host0.0.0.0\
--port"$port"\
--tensor-parallel-size1\
--seed1024\
--dtypefloat16\
--max-model-len10000\
--max-num-batched-tokens10000\
--max-num-seqs256\
--trust-remote-code\
--gpu-memory-utilization0.9\
--kv-transfer-config\
"{\"kv_connector\":\"P2pNcclConnector\",\"kv_role\":\"kv_producer\",\"kv_buffer_size\":\"1e1\",\"kv_port\":\"$kv_port\",\"kv_connector_extra_config\":{\"proxy_ip\":\"0.0.0.0\",\"proxy_port\":\"$PROXY_PORT\",\"http_port\":\"$port\",\"send_type\":\"PUT_ASYNC\",\"nccl_num_channels\":\"16\"}}">prefill$((i+1)).log2>&1&
PIDS+=($!)
done

# =============================================================================
# Launch Decode Servers (Y Decoders)
# =============================================================================
echo""
echo"Starting ${#DECODE_GPU_ARRAY[@]} decode server(s)..."
foriin"${!DECODE_GPU_ARRAY[@]}";do
localgpu_id=${DECODE_GPU_ARRAY[$i]}
localport=${DECODE_PORT_ARRAY[$i]}
localkv_port=$((22001+i))

echo"  Decode server $((i+1)): GPU $gpu_id, Port $port, KV Port $kv_port"
CUDA_VISIBLE_DEVICES=$gpu_idvllmserve"$MODEL"\
--enforce-eager\
--host0.0.0.0\
--port"$port"\
--tensor-parallel-size1\
--seed1024\
--dtypefloat16\
--max-model-len10000\
--max-num-batched-tokens10000\
--max-num-seqs256\
--trust-remote-code\
--gpu-memory-utilization0.7\
--kv-transfer-config\
"{\"kv_connector\":\"P2pNcclConnector\",\"kv_role\":\"kv_consumer\",\"kv_buffer_size\":\"8e9\",\"kv_port\":\"$kv_port\",\"kv_connector_extra_config\":{\"proxy_ip\":\"0.0.0.0\",\"proxy_port\":\"$PROXY_PORT\",\"http_port\":\"$port\",\"send_type\":\"PUT_ASYNC\",\"nccl_num_channels\":\"16\"}}">decode$((i+1)).log2>&1&
PIDS+=($!)
done

# =============================================================================
# Wait for All Servers to Start
# =============================================================================
echo""
echo"Waiting for all servers to start..."
forportin"${PREFILL_PORT_ARRAY[@]}""${DECODE_PORT_ARRAY[@]}";do
if!wait_for_server"$port";then
echo"Failed to start server on port $port"
cleanup
# shellcheck disable=SC2317
exit1
fi
done

echo""
echo"All servers are up. Starting benchmark..."

# =============================================================================
# Run Benchmark
# =============================================================================
cd../../../benchmarks/
vllmbenchserve--port10001--seed"$(date+%s)"\
--model"$MODEL"\
--dataset-namerandom--random-input-len7500--random-output-len200\
--num-prompts200--burstiness100--request-rate2|teebenchmark.log

echo"Benchmarking done. Cleaning up..."

cleanup
}

main
```

## Disagg Proxy P2P NCCL Xpyd[¶](#disagg-proxy-p2p-nccl-xpyd "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

importos
importsocket
importthreading
importtime
importuuid
fromtypingimport Any

importaiohttp
importmsgpack
importzmq
fromquartimport Quart, make_response, request

count = 0
prefill_instances: dict[str, Any] = {}  # http_address: (zmq_address, stamp)
decode_instances: dict[str, Any] = {}  # http_address: (zmq_address, stamp)

prefill_cv = threading.Condition()
decode_cv = threading.Condition()

DEFAULT_PING_SECONDS = 5


def_remove_oldest_instances(instances: dict[str, Any]) -> None:
    oldest_key = next(iter(instances), None)
    while oldest_key is not None:
        value = instances[oldest_key]
        if value[1] > time.time():
            break
        print(f"🔴Remove [HTTP:{oldest_key}, ZMQ:{value[0]}, stamp:{value[1]}]")
        instances.pop(oldest_key, None)
        oldest_key = next(iter(instances), None)


def_listen_for_register(poller, router_socket):
    while True:
        socks = dict(poller.poll())
        if router_socket in socks:
            remote_address, message = router_socket.recv_multipart()
            # data: {"type": "P", "http_address": "ip:port",
            #        "zmq_address": "ip:port"}
            data = msgpack.loads(message)
            if data["type"] == "P":
                global prefill_instances
                global prefill_cv
                with prefill_cv:
                    node = prefill_instances.get(data["http_address"], None)
                    prefill_instances[data["http_address"]] = (
                        data["zmq_address"],
                        time.time() + DEFAULT_PING_SECONDS,
                    )
                    _remove_oldest_instances(prefill_instances)

            elif data["type"] == "D":
                global decode_instances
                global decode_cv
                with decode_cv:
                    node = decode_instances.get(data["http_address"], None)
                    decode_instances[data["http_address"]] = (
                        data["zmq_address"],
                        time.time() + DEFAULT_PING_SECONDS,
                    )
                    _remove_oldest_instances(decode_instances)
            else:
                print(
                    "Unexpected, Received message from %s, data: %s",
                    remote_address,
                    data,
                )
                return

            if node is None:
                print(f"🔵Add [HTTP:{data['http_address']}, ZMQ:{data['zmq_address']}]")


defstart_service_discovery(hostname, port):
    if not hostname:
        hostname = socket.gethostname()
    if port == 0:
        raise ValueError("Port cannot be 0")

    context = zmq.Context()
    router_socket = context.socket(zmq.ROUTER)
    router_socket.bind(f"tcp://{hostname}:{port}")

    poller = zmq.Poller()
    poller.register(router_socket, zmq.POLLIN)

    _listener_thread = threading.Thread(
        target=_listen_for_register, args=[poller, router_socket], daemon=True
    )
    _listener_thread.start()
    return _listener_thread


AIOHTTP_TIMEOUT = aiohttp.ClientTimeout(total=6 * 60 * 60)

app = Quart(__name__)


defrandom_uuid() -> str:
    return str(uuid.uuid4().hex)


async defforward_request(url, data, request_id):
    async with aiohttp.ClientSession(timeout=AIOHTTP_TIMEOUT) as session:
        headers = {
            "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}",
            "X-Request-Id": request_id,
        }
        async with session.post(url=url, json=data, headers=headers) as response:
            if response.status == 200:
                if True:
                    async for chunk_bytes in response.content.iter_chunked(1024):
                        yield chunk_bytes
                else:
                    content = await response.read()
                    yield content


@app.route("/v1/completions", methods=["POST"])
@app.route("/v1/chat/completions", methods=["POST"])
async defhandle_request():
    try:
        original_request_data = await request.get_json()

        prefill_request = original_request_data.copy()
        # change max_tokens = 1 to let it only do prefill
        prefill_request["max_tokens"] = 1
        if "max_completion_tokens" in prefill_request:
            prefill_request["max_completion_tokens"] = 1

        global count
        global prefill_instances
        global prefill_cv
        with prefill_cv:
            prefill_list = list(prefill_instances.items())
            prefill_addr, prefill_zmq_addr = prefill_list[count % len(prefill_list)]
            prefill_zmq_addr = prefill_zmq_addr[0]

        global decode_instances
        global decode_cv
        with decode_cv:
            decode_list = list(decode_instances.items())
            decode_addr, decode_zmq_addr = decode_list[count % len(decode_list)]
            decode_zmq_addr = decode_zmq_addr[0]

        print(
            f"handle_request count: {count}, [HTTP:{prefill_addr}, "
            f"ZMQ:{prefill_zmq_addr}] 👉 [HTTP:{decode_addr}, "
            f"ZMQ:{decode_zmq_addr}]"
        )
        count += 1

        request_id = (
            f"___prefill_addr_{prefill_zmq_addr}___decode_addr_"
            f"{decode_zmq_addr}_{random_uuid()}"
        )

        # finish prefill
        async for _ in forward_request(
            f"http://{prefill_addr}{request.path}", prefill_request, request_id
        ):
            continue

        # return decode
        generator = forward_request(
            f"http://{decode_addr}{request.path}", original_request_data, request_id
        )
        response = await make_response(generator)
        response.timeout = None

        return response

    except Exception as e:
        importsys
        importtraceback

        exc_info = sys.exc_info()
        print("Error occurred in disagg prefill proxy server")
        print(e)
        print("".join(traceback.format_exception(*exc_info)))


if __name__ == "__main__":
    t = start_service_discovery("0.0.0.0", 30001)
    app.run(host="0.0.0.0", port=10001)
    t.join()
```