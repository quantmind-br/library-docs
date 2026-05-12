---
title: Mooncake Connector - vLLM
url: https://docs.vllm.ai/en/latest/examples/disaggregated/mooncake_connector/
source: sitemap
fetched_at: 2026-05-07T21:12:46.131447806-03:00
rendered_js: false
word_count: 0
summary: This document defines a FastAPI-based server infrastructure that manages pools of prefill and decode service clients, implementing round-robin load balancing and asynchronous health monitoring for distributed machine learning inference services.
tags:
    - fastapi
    - load-balancing
    - asynchronous-programming
    - service-discovery
    - distributed-inference
    - httpx
category: configuration
---

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

importargparse
importasyncio
importipaddress
importitertools
importos
importurllib
importuuid
fromcontextlibimport asynccontextmanager
fromtypingimport Any

importhttpx
fromfastapiimport FastAPI, HTTPException, Request
fromfastapi.responsesimport StreamingResponse


defmaybe_wrap_ipv6_address(address: str) -> str:
    try:
        ipaddress.IPv6Address(address)
        return f"[{address}]"
    except ValueError:
        return address


defmake_http_path(host: str, port: int) -> str:
    return f"http://{host}:{port}"


defprefiller_cycle(prefill_clients: list[Any]):
    while True:
        for prefill_client in prefill_clients:
            for i in range(prefill_client["dp_size"]):
                yield prefill_client, i


async defget_prefiller_info(prefill_clients: list, ready: asyncio.Event):
    for prefill_client in prefill_clients:
        while True:
            try:
                # Wait for prefill service to be ready
                response = await prefill_client["client"].get("/health")
                response.raise_for_status()
            except Exception:
                await asyncio.sleep(1)
                continue

            response = await prefill_client["client"].get(
                prefill_client["bootstrap_addr"] + "/query"
            )
            response.raise_for_status()
            data = response.json()
            break

        for dp_rank, dp_entry in data.items():
            prefill_client["dp_engine_id"][int(dp_rank)] = dp_entry["engine_id"]
        dp_size = len(data)
        prefill_client["dp_size"] = dp_size
        print(f"Inited prefiller {prefill_client['url']} with dp_size={dp_size}")

    ready.set()
    print("All prefiller instances are ready.")


@asynccontextmanager
async deflifespan(app: FastAPI):
"""
    Lifespan context manager to handle startup and shutdown events.
    """
    # Startup: Initialize client pools for prefiller and decoder services
    app.state.prefill_clients = []
    app.state.decode_clients = []
    app.state.ready = asyncio.Event()

    # Create prefill clients
    for i, (url, bootstrap_port) in enumerate(global_args.prefill):
        parsed_url = urllib.parse.urlparse(url)
        hostname = maybe_wrap_ipv6_address(parsed_url.hostname)
        app.state.prefill_clients.append(
            {
                "client": httpx.AsyncClient(
                    timeout=None,
                    base_url=url,
                    limits=httpx.Limits(
                        max_connections=None,
                        max_keepalive_connections=None,
                    ),
                ),
                "url": url,
                "bootstrap_addr": make_http_path(hostname, bootstrap_port or 8998),
                "dp_engine_id": {},
            }
        )

    # Create decode clients
    for i, url in enumerate(global_args.decode):
        parsed_url = urllib.parse.urlparse(url)
        hostname = maybe_wrap_ipv6_address(parsed_url.hostname)
        app.state.decode_clients.append(
            {
                "client": httpx.AsyncClient(
                    timeout=None,
                    base_url=url,
                    limits=httpx.Limits(
                        max_connections=None,
                        max_keepalive_connections=None,
                    ),
                ),
            }
        )

    asyncio.create_task(get_prefiller_info(app.state.prefill_clients, app.state.ready))

    # Initialize round-robin iterators
    app.state.prefill_iterator = prefiller_cycle(app.state.prefill_clients)
    app.state.decode_iterator = itertools.cycle(range(len(app.state.decode_clients)))

    print(
        f"Got {len(app.state.prefill_clients)} prefill clients "
        f"and {len(app.state.decode_clients)} decode clients."
    )

    yield

    # Shutdown: Close all clients
    for client_info in app.state.prefill_clients:
        await client_info["client"].aclose()

    for client_info in app.state.decode_clients:
        await client_info["client"].aclose()


# Update FastAPI app initialization to use lifespan
app = FastAPI(lifespan=lifespan)


defparse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--port", type=int, default=8000)
    # Always use 127.0.0.1 as localhost binds to IPv6 which is blocked on CI
    parser.add_argument("--host", type=str, default="127.0.0.1")

    # For prefiller instances
    parser.add_argument(
        "--prefill",
        nargs="+",
        action="append",
        dest="prefill_raw",
        metavar=("URL", "bootstrap_port"),
        help=(
            "Prefill server URL and optional bootstrap port. "
            "Can be specified multiple times. "
            "Format: --prefill URL [BOOTSTRAP_PORT]. "
            "BOOTSTRAP_PORT can be a port number, "
            "'none', or omitted (defaults to none)."
        ),
    )

    # For decoder instances
    parser.add_argument(
        "--decode",
        nargs=1,
        action="append",
        dest="decode_raw",
        metavar=("URL",),
        help="Decode server URL. Can be specified multiple times.",
    )

    args = parser.parse_args()
    args.prefill = _parse_prefill_urls(args.prefill_raw)
    args.decode = _parse_decode_urls(args.decode_raw)

    return args


# From sglang router_args.py
def_parse_prefill_urls(prefill_list):
"""Parse prefill URLs from --prefill arguments.

    Format: --prefill URL [BOOTSTRAP_PORT]
    Example:
        --prefill http://prefill1:8080 9000  # With bootstrap port
        --prefill http://prefill2:8080 none  # Explicitly no bootstrap port
        --prefill http://prefill3:8080       # Defaults to no bootstrap port
    """
    if not prefill_list:
        return []

    prefill_urls = []
    for prefill_args in prefill_list:
        url = prefill_args[0]

        # Handle optional bootstrap port
        if len(prefill_args) >= 2:
            bootstrap_port_str = prefill_args[1]
            # Handle 'none' as None
            if bootstrap_port_str.lower() == "none":
                bootstrap_port = None
            else:
                try:
                    bootstrap_port = int(bootstrap_port_str)
                except ValueError as e:
                    raise ValueError(
                        f"Invalid bootstrap port: {bootstrap_port_str}. Must be a number or 'none'"  # noqa: E501
                    ) frome
        else:
            # No bootstrap port specified, default to None
            bootstrap_port = None

        prefill_urls.append((url, bootstrap_port))

    return prefill_urls


def_parse_decode_urls(decode_list):
"""Parse decode URLs from --decode arguments.

    Format: --decode URL
    Example: --decode http://decode1:8081 --decode http://decode2:8081
    """
    if not decode_list:
        return []

    # decode_list is a list of single-element lists due to nargs=1
    return [url[0] for url in decode_list]


defget_next_client(app, service_type: str):
"""
    Get the next client in round-robin fashion.

    Args:
        app: The FastAPI app instance
        service_type: Either 'prefill' or 'decode'

    Returns:
        The next client to use
    """
    if service_type == "prefill":
        return next(app.state.prefill_iterator)
    elif service_type == "decode":
        client_idx = next(app.state.decode_iterator)
        return app.state.decode_clients[client_idx]
    else:
        raise ValueError(f"Unknown service type: {service_type}")


async defsend_request_to_service(
    client_info: dict, dp_rank: int, endpoint: str, req_data: dict, request_id: str
):
"""
    Send a request to a service using a client from the pool.
    """
    req_data = req_data.copy()
    req_data["kv_transfer_params"] = {
        "do_remote_decode": True,
        "do_remote_prefill": False,
        "transfer_id": f"xfer-{request_id}",
    }
    req_data["stream"] = False
    req_data["max_tokens"] = 1
    if "max_completion_tokens" in req_data:
        req_data["max_completion_tokens"] = 1
    if "stream_options" in req_data:
        del req_data["stream_options"]
    headers = {
        "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}",
        "X-Request-Id": request_id,
        "X-data-parallel-rank": str(dp_rank),
    }

    response = await client_info["client"].post(
        endpoint, json=req_data, headers=headers
    )
    response.raise_for_status()

    # CRITICAL: Release connection back to pool
    await response.aclose()


async defstream_service_response(
    prefill_client_info: dict,
    prefill_dp_rank: int,
    decode_client_info: dict,
    endpoint: str,
    req_data: dict,
    request_id: str,
):
"""
    Asynchronously stream response from a service using a client from the pool.
    """
    headers = {
        "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}",
        "X-Request-Id": request_id,
    }

    req_data["kv_transfer_params"] = {
        "do_remote_decode": False,
        "do_remote_prefill": True,
        "remote_bootstrap_addr": prefill_client_info["bootstrap_addr"],
        "remote_engine_id": prefill_client_info["dp_engine_id"][prefill_dp_rank],
        "transfer_id": f"xfer-{request_id}",
    }

    async with decode_client_info["client"].stream(
        "POST", endpoint, json=req_data, headers=headers
    ) as response:
        response.raise_for_status()
        async for chunk in response.aiter_bytes():
            yield chunk


async def_handle_completions(api: str, request: Request):
    if not app.state.ready.is_set():
        raise HTTPException(status_code=503, detail="Service Unavailable")

    try:
        req_data = await request.json()
        request_id = str(uuid.uuid4())

        # Get the next prefill client in round-robin fashion
        prefill_client_info, prefill_dp_rank = get_next_client(request.app, "prefill")

        # Send request to prefill service
        asyncio.create_task(
            send_request_to_service(
                prefill_client_info, prefill_dp_rank, api, req_data, request_id
            )
        )

        decode_client_info = get_next_client(request.app, "decode")

        # Stream response from decode service
        async defgenerate_stream():
            async for chunk in stream_service_response(
                prefill_client_info,
                prefill_dp_rank,
                decode_client_info,
                api,
                req_data,
                request_id=request_id,
            ):
                yield chunk

        return StreamingResponse(generate_stream(), media_type="application/json")

    except Exception as e:
        importsys
        importtraceback

        exc_info = sys.exc_info()
        print(f"Error occurred in disagg prefill proxy server - {api} endpoint")
        print(e)
        print("".join(traceback.format_exception(*exc_info)))
        raise


@app.post("/v1/completions")
async defhandle_completions(request: Request):
    return await _handle_completions("/v1/completions", request)


@app.post("/v1/chat/completions")
async defhandle_chat_completions(request: Request):
    return await _handle_completions("/v1/chat/completions", request)


if __name__ == "__main__":
    global global_args
    global_args = parse_args()

    importuvicorn

    uvicorn.run(app, host=global_args.host, port=global_args.port)

#!/bin/bash

# =============================================================================
# vLLM Disaggregated Serving Script for Mooncake Connector
# =============================================================================
# This script demonstrates disaggregated prefill and decode serving using
# Mooncake Connector.
#
# Configuration can be customized via environment variables:
#   MODEL: Model to serve
#   PREFILL_GPUS: Comma-separated GPU IDs for prefill servers
#   DECODE_GPUS: Comma-separated GPU IDs for decode servers
#   PREFILL_PORTS: Comma-separated ports for prefill servers
#   BOOTSTRAP_PORTS: Bootstrap server port launched by prefill servers
#   DECODE_PORTS: Comma-separated ports for decode servers
#   PROXY_PORT: Proxy server port used to setup P/D disaggregated connection.
#   TIMEOUT_SECONDS: Server startup timeout
# =============================================================================

# Configuration - can be overridden via environment variables
MODEL=${MODEL:-Qwen/Qwen2.5-7B-Instruct}
TIMEOUT_SECONDS=${TIMEOUT_SECONDS:-1200}
PROXY_PORT=${PROXY_PORT:-8000}

PREFILL_GPUS=${PREFILL_GPUS:-0}
DECODE_GPUS=${DECODE_GPUS:-1}
PREFILL_PORTS=${PREFILL_PORTS:-8010}
BOOTSTRAP_PORTS=${BOOTSTRAP_PORTS:-8998}
DECODE_PORTS=${DECODE_PORTS:-8020}

echo"Warning: Mooncake Connector support for vLLM v1 is experimental and subject to change."
echo""
echo"Architecture Configuration:"
echo"  Model: $MODEL"
echo"  Prefill GPUs: $PREFILL_GPUS, Ports: $PREFILL_PORTS, Bootstrap Port:$BOOTSTRAP_PORTS"
echo"  Decode GPUs: $DECODE_GPUS, Ports: $DECODE_PORTS"
echo"  Proxy Port: $PROXY_PORT"
echo"  Timeout: ${TIMEOUT_SECONDS}s"
echo""

PIDS=()

# Switch to the directory of the current script
cd"$(dirname"${BASH_SOURCE[0]}")"

check_required_files(){
localfiles=("mooncake_connector_proxy.py")
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
pkill-9-f"mooncake_connector_proxy.py"
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
ensure_python_library_installedvllm
ensure_python_library_installedmooncake.engine

trapcleanupINT
trapcleanupUSR1
trapcleanupTERM

echo"Launching disaggregated serving components..."
echo"Please check the log files for detailed output:"
echo"  - prefill*.log: Prefill server logs"
echo"  - decode*.log: Decode server logs"
echo"  - proxy.log: Proxy server log"

# Parse GPU and port arrays
IFS=','read-raPREFILL_GPU_ARRAY<<<"$PREFILL_GPUS"
IFS=','read-raDECODE_GPU_ARRAY<<<"$DECODE_GPUS"
IFS=','read-raPREFILL_PORT_ARRAY<<<"$PREFILL_PORTS"
IFS=','read-raBOOTSTRAP_PORT_ARRAY<<<"$BOOTSTRAP_PORTS"
IFS=','read-raDECODE_PORT_ARRAY<<<"$DECODE_PORTS"

proxy_args=()

# =============================================================================
# Launch Prefill Servers (X Producers)
# =============================================================================
echo""
echo"Starting ${#PREFILL_GPU_ARRAY[@]} prefill server(s)..."
foriin"${!PREFILL_GPU_ARRAY[@]}";do
localgpu_id=${PREFILL_GPU_ARRAY[$i]}
localport=${PREFILL_PORT_ARRAY[$i]}
localbootstrap_port=${BOOTSTRAP_PORT_ARRAY[$i]}

echo"  Prefill server $((i+1)): GPU $gpu_id, Port $port, Bootstrap Port $bootstrap_port"
VLLM_MOONCAKE_BOOTSTRAP_PORT=$bootstrap_portCUDA_VISIBLE_DEVICES=$gpu_idvllmserve"$MODEL"\
--port"$port"\
--kv-transfer-config\
"{\"kv_connector\":\"MooncakeConnector\",\"kv_role\":\"kv_producer\"}">prefill$((i+1)).log2>&1&
PIDS+=($!)
proxy_args+=(--prefill"http://0.0.0.0:${port}""$bootstrap_port")
done

# =============================================================================
# Launch Decode Servers (Y Decoders)
# =============================================================================
echo""
echo"Starting ${#DECODE_GPU_ARRAY[@]} decode server(s)..."
foriin"${!DECODE_GPU_ARRAY[@]}";do
localgpu_id=${DECODE_GPU_ARRAY[$i]}
localport=${DECODE_PORT_ARRAY[$i]}

echo"  Decode server $((i+1)): GPU $gpu_id, Port $port"
CUDA_VISIBLE_DEVICES=$gpu_idvllmserve"$MODEL"\
--port"$port"\
--kv-transfer-config\
"{\"kv_connector\":\"MooncakeConnector\",\"kv_role\":\"kv_consumer\"}">decode$((i+1)).log2>&1&
PIDS+=($!)
proxy_args+=(--decode"http://0.0.0.0:${port}")
done

# =============================================================================
# Launch Proxy Server
# =============================================================================
echo""
echo"Starting proxy server on port $PROXY_PORT..."
python3mooncake_connector_proxy.py"${proxy_args[@]}"--port"$PROXY_PORT">proxy.log2>&1&
PIDS+=($!)

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
vllmbenchserve--port"$PROXY_PORT"--seed"$(date+%s)"\
--backendvllm--model"$MODEL"\
--dataset-namerandom--random-input-len7500--random-output-len200\
--num-prompts200--burstiness100--request-rate2|teebenchmark.log

echo"Benchmarking done. Cleaning up..."

cleanup
}

main
```