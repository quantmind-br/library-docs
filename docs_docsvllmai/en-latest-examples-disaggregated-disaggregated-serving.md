---
title: Disaggregated Serving - vLLM
url: https://docs.vllm.ai/en/latest/examples/disaggregated/disaggregated_serving/
source: sitemap
fetched_at: 2026-05-07T21:12:39.89035923-03:00
rendered_js: false
word_count: 430
summary: This document provides scripts and examples for implementing disaggregated serving in vLLM, specifically demonstrating how to separate prefill and decode instances using a proxy.
tags:
    - vllm
    - disaggregated-serving
    - prefill-decode-separation
    - model-serving
    - proxy-implementation
    - distributed-inference
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/disaggregated/disaggregated_serving.md "Edit this page")

Source [https://github.com/vllm-project/vllm/tree/main/examples/disaggregated/disaggregated\_serving](https://github.com/vllm-project/vllm/tree/main/examples/disaggregated/disaggregated_serving).

This example contains scripts that demonstrate the disaggregated serving features of vLLM.

## Files[¶](#files "Permanent link")

- `disagg_proxy_demo.py` - Demonstrates XpYd (X prefill instances, Y decode instances).
- `kv_events.sh` - Demonstrates KV cache event publishing.
- `mooncake_connector` - A proxy demo for MooncakeConnector.

## Example materials[¶](#example-materials "Permanent link")

disagg\_proxy\_demo.py

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
This file provides a disaggregated prefilling proxy demo to demonstrate an
example usage of XpYd disaggregated prefilling.
We can launch multiple vllm instances (2 for prefill and 2 for decode), and
launch this proxy demo through:
  python3 examples/disaggregated/disaggregated_serving/disagg_proxy_demo.py  \
       --model $model_name  \
       --prefill localhost:8100 localhost:8101   \
       --decode localhost:8200 localhost:8201   \
       --port 8000

Note: This demo will be removed once the PDController implemented in PR 15343
(https://github.com/vllm-project/vllm/pull/15343) supports XpYd.
"""

importargparse
importipaddress
importitertools
importjson
importlogging
importos
importsys
fromabcimport ABC, abstractmethod
fromcollections.abcimport Callable

importaiohttp
importrequests
importuvicorn
fromfastapiimport APIRouter, Depends, FastAPI, Header, HTTPException, Request, status
fromfastapi.responsesimport JSONResponse, StreamingResponse

AIOHTTP_TIMEOUT = aiohttp.ClientTimeout(total=6 * 60 * 60)
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)


classSchedulingPolicy(ABC):
    @abstractmethod
    defschedule(self, cycler: itertools.cycle):
        raise NotImplementedError("Scheduling Proxy is not set.")


classProxy:
    def__init__(
        self,
        prefill_instances: list[str],
        decode_instances: list[str],
        model: str,
        scheduling_policy: SchedulingPolicy,
        custom_create_completion: Callable[[Request], StreamingResponse] | None = None,
        custom_create_chat_completion: Callable[[Request], StreamingResponse]
        | None = None,
    ):
        self.prefill_instances = prefill_instances
        self.decode_instances = decode_instances
        self.prefill_cycler = itertools.cycle(prefill_instances)
        self.decode_cycler = itertools.cycle(decode_instances)
        self.model = model
        self.scheduling_policy = scheduling_policy
        self.custom_create_completion = custom_create_completion
        self.custom_create_chat_completion = custom_create_chat_completion
        self.router = APIRouter()
        self.setup_routes()

    defsetup_routes(self):
        self.router.post(
            "/v1/completions", dependencies=[Depends(self.validate_json_request)]
        )(
            self.custom_create_completion
            if self.custom_create_completion
            else self.create_completion
        )
        self.router.post(
            "/v1/chat/completions", dependencies=[Depends(self.validate_json_request)]
        )(
            self.custom_create_chat_completion
            if self.custom_create_chat_completion
            else self.create_chat_completion
        )
        self.router.get("/status", response_class=JSONResponse)(self.get_status)
        self.router.post(
            "/instances/add", dependencies=[Depends(self.api_key_authenticate)]
        )(self.add_instance_endpoint)

    async defvalidate_json_request(self, raw_request: Request):
        content_type = raw_request.headers.get("content-type", "").lower()
        if content_type != "application/json":
            raise HTTPException(
                status_code=415,
                detail="Unsupported Media Type: Only 'application/json' is allowed",
            )

    defapi_key_authenticate(self, x_api_key: str = Header(...)):
        expected_api_key = os.environ.get("ADMIN_API_KEY")
        if not expected_api_key:
            logger.error("ADMIN_API_KEY is not set in the environment.")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Server configuration error.",
            )
        if x_api_key != expected_api_key:
            logger.warning("Unauthorized access attempt with API Key: %s", x_api_key)
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Forbidden: Invalid API Key.",
            )

    async defvalidate_instance(self, instance: str) -> bool:
        url = f"http://{instance}/v1/models"
        try:
            async with aiohttp.ClientSession(timeout=AIOHTTP_TIMEOUT) as client:
                logger.info("Verifying %s ...", instance)
                async with client.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        if "data" in data and len(data["data"]) > 0:
                            model_cur = data["data"][0].get("id", "")
                            if model_cur == self.model:
                                logger.info("Instance: %s could be added.", instance)
                                return True
                            else:
                                logger.warning(
                                    "Mismatch model %s : %s != %s",
                                    instance,
                                    model_cur,
                                    self.model,
                                )
                                return False
                        else:
                            return False
                    else:
                        return False
        except aiohttp.ClientError as e:
            logger.error(str(e))
            return False
        except Exception as e:
            logger.error(str(e))
            return False

    async defadd_instance_endpoint(self, request: Request):
        try:
            data = await request.json()
            logger.warning(str(data))
            instance_type = data.get("type")
            instance = data.get("instance")
            if instance_type not in ["prefill", "decode"]:
                raise HTTPException(status_code=400, detail="Invalid instance type.")
            if not instance or ":" not in instance:
                raise HTTPException(status_code=400, detail="Invalid instance format.")
            host, port_str = instance.split(":")
            try:
                if host != "localhost":
                    ipaddress.ip_address(host)
                port = int(port_str)
                if not (0 < port < 65536):
                    raise HTTPException(status_code=400, detail="Invalid port number.")
            except Exception as e:
                raise HTTPException(
                    status_code=400, detail="Invalid instance address."
                ) frome

            is_valid = await self.validate_instance(instance)
            if not is_valid:
                raise HTTPException(
                    status_code=400, detail="Instance validation failed."
                )

            if instance_type == "prefill":
                if instance not in self.prefill_instances:
                    self.prefill_instances.append(instance)
                    self.prefill_cycler = itertools.cycle(self.prefill_instances)
                else:
                    raise HTTPException(
                        status_code=400, detail="Instance already exists."
                    )
            else:
                if instance not in self.decode_instances:
                    self.decode_instances.append(instance)
                    self.decode_cycler = itertools.cycle(self.decode_instances)
                else:
                    raise HTTPException(
                        status_code=400, detail="Instance already exists."
                    )

            return JSONResponse(
                content={"message": f"Added {instance} to {instance_type}_instances."}
            )
        except HTTPException as http_exc:
            raise http_exc
        except Exception as e:
            logger.error("Error in add_instance_endpoint: %s", str(e))
            raise HTTPException(status_code=500, detail=str(e)) frome

    async defforward_request(self, url, data, use_chunked=True):
        async with aiohttp.ClientSession(timeout=AIOHTTP_TIMEOUT) as session:
            headers = {"Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}"}
            try:
                async with session.post(
                    url=url, json=data, headers=headers
                ) as response:
                    if 200 <= response.status < 300 or 400 <= response.status < 500:
                        if use_chunked:
                            async for chunk_bytes in response.content.iter_chunked(
                                1024
                            ):
                                yield chunk_bytes
                        else:
                            content = await response.read()
                            yield content
                    else:
                        error_content = await response.text()
                        try:
                            error_content = json.loads(error_content)
                        except json.JSONDecodeError:
                            error_content = error_content
                        logger.error(
                            "Request failed with status %s: %s",
                            response.status,
                            error_content,
                        )
                        raise HTTPException(
                            status_code=response.status,
                            detail=f"Request failed with status {response.status}: "
                            f"{error_content}",
                        )
            except aiohttp.ClientError as e:
                logger.error("ClientError occurred: %s", str(e))
                raise HTTPException(
                    status_code=502,
                    detail="Bad Gateway: Error communicating with upstream server.",
                ) frome
            except Exception as e:
                logger.error("Unexpected error: %s", str(e))
                raise HTTPException(status_code=500, detail=str(e)) frome

    defschedule(self, cycler: itertools.cycle) -> str:
        return self.scheduling_policy.schedule(cycler)

    async defget_status(self):
        status = {
            "prefill_node_count": len(self.prefill_instances),
            "decode_node_count": len(self.decode_instances),
            "prefill_nodes": self.prefill_instances,
            "decode_nodes": self.decode_instances,
        }
        return status

    async defcreate_completion(self, raw_request: Request):
        try:
            request = await raw_request.json()

            kv_prepare_request = request.copy()
            kv_prepare_request["max_tokens"] = 1

            prefill_instance = self.schedule(self.prefill_cycler)
            try:
                async for _ in self.forward_request(
                    f"http://{prefill_instance}/v1/completions", kv_prepare_request
                ):
                    continue
            except HTTPException as http_exc:
                self.remove_instance_endpoint("prefill", prefill_instance)
                raise http_exc

            # Perform kv recv and decoding stage
            decode_instance = self.schedule(self.decode_cycler)

            try:
                generator = self.forward_request(
                    f"http://{decode_instance}/v1/completions", request
                )
            except HTTPException as http_exc:
                self.remove_instance_endpoint("decode", decode_instance)
                raise http_exc
            response = StreamingResponse(generator)
            return response
        except Exception:
            importsys

            exc_info = sys.exc_info()
            print("Error occurred in disagg proxy server")
            print(exc_info)

    async defcreate_chat_completion(self, raw_request: Request):
        try:
            request = await raw_request.json()

            # add params to request
            kv_prepare_request = request.copy()
            kv_prepare_request["max_tokens"] = 1
            if "max_completion_tokens" in kv_prepare_request:
                kv_prepare_request["max_completion_tokens"] = 1

            # prefill stage
            prefill_instance = self.schedule(self.prefill_cycler)
            try:
                async for _ in self.forward_request(
                    f"http://{prefill_instance}/v1/chat/completions", kv_prepare_request
                ):
                    continue
            except HTTPException as http_exc:
                self.remove_instance_endpoint("prefill", prefill_instance)
                raise http_exc
            # Perform kv recv and decoding stage
            decode_instance = self.schedule(self.decode_cycler)

            try:
                generator = self.forward_request(
                    "http://" + decode_instance + "/v1/chat/completions", request
                )
            except HTTPException as http_exc:
                self.remove_instance_endpoint("decode", decode_instance)
                raise http_exc
            response = StreamingResponse(content=generator)
            return response
        except Exception:
            exc_info = sys.exc_info()
            error_messages = [str(e) for e in exc_info if e]
            print("Error occurred in disagg proxy server")
            print(error_messages)
            return StreamingResponse(
                content=iter(error_messages), media_type="text/event-stream"
            )

    defremove_instance_endpoint(self, instance_type, instance):
        if instance_type == "decode" and instance in self.decode_instances:
            self.decode_instances.remove(instance)
            self.decode_cycler = itertools.cycle(self.decode_instances)
        if instance_type == "prefill" and instance in self.prefill_instances:
            self.prefill_instances.remove(instance)
            self.prefill_cycler = itertools.cycle(self.prefill_instances)


classRoundRobinSchedulingPolicy(SchedulingPolicy):
    def__init__(self):
        super().__init__()

    defschedule(self, cycler: itertools.cycle) -> str:
        return next(cycler)


classProxyServer:
    def__init__(
        self,
        args: argparse.Namespace,
        scheduling_policy: SchedulingPolicy | None = None,
        create_completion: Callable[[Request], StreamingResponse] | None = None,
        create_chat_completion: Callable[[Request], StreamingResponse] | None = None,
    ):
        self.validate_parsed_serve_args(args)
        self.port = args.port
        self.proxy_instance = Proxy(
            prefill_instances=[] if args.prefill is None else args.prefill,
            decode_instances=[] if args.decode is None else args.decode,
            model=args.model,
            scheduling_policy=(
                scheduling_policy
                if scheduling_policy is not None
                else RoundRobinSchedulingPolicy()
            ),
            custom_create_completion=create_completion,
            custom_create_chat_completion=create_chat_completion,
        )

    defvalidate_parsed_serve_args(self, args: argparse.Namespace):
        if not args.prefill:
            raise ValueError("Please specify at least one prefill node.")
        if not args.decode:
            raise ValueError("Please specify at least one decode node.")
        self.validate_instances(args.prefill)
        self.validate_instances(args.decode)
        self.verify_model_config(args.prefill, args.model)
        self.verify_model_config(args.decode, args.model)

    defvalidate_instances(self, instances: list):
        for instance in instances:
            if len(instance.split(":")) != 2:
                raise ValueError(f"Invalid instance format: {instance}")
            host, port = instance.split(":")
            try:
                if host != "localhost":
                    ipaddress.ip_address(host)
                port = int(port)
                if not (0 < port < 65536):
                    raise ValueError(f"Invalid port number in instance: {instance}")
            except Exception as e:
                raise ValueError(f"Invalid instance {instance}: {str(e)}") frome

    defverify_model_config(self, instances: list, model: str) -> None:
        model_suffix = model.split("/")[-1]
        for instance in instances:
            try:
                response = requests.get(f"http://{instance}/v1/models")
                if response.status_code == 200:
                    model_cur = response.json()["data"][0]["id"]
                    model_cur_suffix = model_cur.split("/")[-1]
                    if model_cur_suffix != model_suffix:
                        raise ValueError(
                            f"{instance} serves a different model: "
                            f"{model_cur} != {model}"
                        )
                else:
                    raise ValueError(f"Cannot get model id from {instance}!")
            except requests.RequestException as e:
                raise ValueError(
                    f"Error communicating with {instance}: {str(e)}"
                ) frome

    defrun_server(self):
        app = FastAPI()
        app.include_router(self.proxy_instance.router)
        config = uvicorn.Config(app, port=self.port, loop="uvloop")
        server = uvicorn.Server(config)
        server.run()


defparse_args():
    # Todo: allow more config
    parser = argparse.ArgumentParser("vLLM disaggregated proxy server.")
    parser.add_argument("--model", "-m", type=str, required=True, help="Model name")

    parser.add_argument(
        "--prefill",
        "-p",
        type=str,
        nargs="+",
        help="List of prefill node URLs (host:port)",
    )

    parser.add_argument(
        "--decode",
        "-d",
        type=str,
        nargs="+",
        help="List of decode node URLs (host:port)",
    )

    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Server port number",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    proxy_server = ProxyServer(args=args)
    proxy_server.run_server()
```

example\_mm\_serve.py

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""Disaggregated multimodal serving: render → generate round-trip.

Demonstrates the two-phase disaggregated flow:
  1. /v1/chat/completions/render  – preprocesses a multimodal chat request
     into token IDs and serialized tensor features.
  2. /inference/v1/generate       – runs inference on the preprocessed tokens.

The render response is passed *directly* to generate with only
``sampling_params`` added, showing that the two endpoints compose with
zero client-side transformation.

Launch the server first:

    vllm serve Qwen/Qwen3-VL-2B-Instruct \
        --dtype bfloat16 --max-model-len 4096 --enforce-eager

Then run this script:

    python example_mm_serve.py
"""

importio

importpybase64asbase64
importrequests
fromPILimport Image
fromtransformersimport AutoTokenizer

BASE_URL = "http://localhost:8000"
MODEL_NAME = "Qwen/Qwen3-VL-2B-Instruct"


defmake_data_url(image: Image.Image) -> str:
"""Encode a PIL image as a base64 data URL."""
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode()
    return f"data:image/png;base64,{b64}"


defmain():
    # -- Step 1: Create a test image (solid red) -------------------------
    image = Image.new("RGB", (224, 224), color=(255, 0, 0))
    data_url = make_data_url(image)
    print("Created 224x224 red test image")

    # -- Step 2: Render (preprocess) -------------------------------------
    render_payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "image_url", "image_url": {"url": data_url}},
                    {
                        "type": "text",
                        "text": "What color is this image? Answer in one word.",
                    },
                ],
            }
        ],
    }

    print("\n--- Render ---")
    render_resp = requests.post(
        f"{BASE_URL}/v1/chat/completions/render", json=render_payload
    )
    render_resp.raise_for_status()
    render_data = render_resp.json()

    print(f"Response keys: {list(render_data.keys())}")
    print(f"Number of token_ids: {len(render_data['token_ids'])}")

    features = render_data.get("features")
    if features and features.get("kwargs_data"):
        print(f"kwargs_data modalities: {list(features['kwargs_data'].keys())}")
        for modality, items in features["kwargs_data"].items():
            print(
                f"  {modality}: {len(items)} item(s), "
                f"first item type: {type(items[0])} length: {len(items[0])}"
                if items
                else "First item: (empty)"
            )
    else:
        print("WARNING: no kwargs_data in render response")

    # -- Step 3: Generate (inference) ------------------------------------
    # Pass the render output directly — only add sampling_params.
    generate_payload = render_data
    generate_payload["sampling_params"] = {
        "max_tokens": 20,
        "temperature": 0.0,
    }

    print("\n--- Generate ---")
    gen_resp = requests.post(f"{BASE_URL}/inference/v1/generate", json=generate_payload)
    gen_resp.raise_for_status()
    gen_data = gen_resp.json()

    # -- Step 4: Decode & print ------------------------------------------
    output_ids = gen_data["choices"][0]["token_ids"]
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    text = tokenizer.decode(output_ids, skip_special_tokens=True)

    print(f"Output token count: {len(output_ids)}")
    print(f"Generated text: {text!r}")

    if "red" in text.lower():
        print("\nModel correctly identified the red image.")
    else:
        print(f"\nWARNING: Expected 'red' in output, got: {text!r}")


if __name__ == "__main__":
    main()
```

kv\_events.sh

```
#!/bin/bash
# This file demonstrates the KV cache event publishing
# We will launch a vllm instances configured to publish KV cache
# events and launch a simple subscriber to log those events.

set-xe

echo"🚧🚧 Warning: The usage of KV cache events is experimental and subject to change 🚧🚧"
sleep1

MODEL_NAME=${HF_MODEL_NAME:-meta-llama/Meta-Llama-3.1-8B-Instruct}

# Trap the SIGINT signal (triggered by Ctrl+C)
trap'cleanup'INT

# Cleanup function
cleanup(){
echo"Caught Ctrl+C, cleaning up..."
# Cleanup commands
pgreppython|xargskill-9
pkill-fpython
echo"Cleanup complete. Exiting."
exit0
}

exportVLLM_HOST_IP=$(hostname-I|awk'{print $1}')

# a function that waits vLLM server to start
wait_for_server(){
localport=$1
timeout1200bash-c"
    until curl -s localhost:${port}/v1/completions > /dev/null; do
      sleep 1
    done"&&return0||return1
}

vllmserve"$MODEL_NAME"\
--port8100\
--max-model-len100\
--enforce-eager\
--gpu-memory-utilization0.8\
--trust-remote-code\
--kv-events-config\
'{"enable_kv_cache_events": true, "publisher": "zmq", "topic": "kv-events"}'&

wait_for_server8100

SCRIPT_DIR="$(cd"$(dirname"${BASH_SOURCE[0]}")"&&pwd)"

python3"$SCRIPT_DIR/kv_events_subscriber.py"&
sleep1

# serve two example requests
output1=$(curl-XPOST-shttp://localhost:8100/v1/completions\
-H"Content-Type: application/json"\
-d'{
"model": "'"$MODEL_NAME"'",
"prompt": "Explain quantum computing in simple terms a 5-year-old could understand.",
"max_tokens": 80,
"temperature": 0
}')

output2=$(curl-XPOST-shttp://localhost:8100/v1/completions\
-H"Content-Type: application/json"\
-d'{
"model": "'"$MODEL_NAME"'",
"prompt": "Explain quantum computing in simple terms a 50-year-old could understand.",
"max_tokens": 80,
"temperature": 0
}')

# Cleanup commands
pkill-9-u"$USER"-fpython
pkill-9-u"$USER"-fvllm

sleep1

echo"Cleaned up"

# Print the outputs of the curl requests
echo""
echo"Output of first request: $output1"
echo"Output of second request: $output2"

echo"🎉🎉 Successfully finished 2 test requests! 🎉🎉"
echo""
```

moriio\_toy\_proxy\_server.py

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
importargparse
importasyncio
importcopy
importlogging
importos
importsocket
importthreading
importuuid
fromurllib.parseimport urlparse

importaiohttp
importmsgpack
importzmq
fromquartimport Quart, Request, make_response, request

fromvllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_commonimport (
    MoRIIOConstants,
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
prefill_instances: list[dict] = []
decode_instances: list[dict] = []
request_nums = 0
app = Quart(__name__)


TRANSFER_TYPE = None


_list_lock = threading.RLock()


def_listen_for_register(hostname, port):
    context = zmq.Context()
    router_socket = context.socket(zmq.ROUTER)
    router_socket.bind(f"tcp://{hostname}:{port}")
    poller = zmq.Poller()
    poller.register(router_socket, zmq.POLLIN)
    global prefill_instances
    global decode_instances

    while True:
        socks = dict(poller.poll())
        if router_socket in socks:
            remote_addr, msg = router_socket.recv_multipart()
            data = msgpack.loads(msg)
            if data.get("type") == "HELLO":
                pass
            elif data.get("type") in ("P", "D"):
                role = data["type"]
                required_keys = {
                    "http_address",
                    "zmq_address",
                    "dp_size",
                    "tp_size",
                    "transfer_mode",
                }
                missing = required_keys - data.keys()
                if missing:
                    logger.error(
                        "Registration message missing required keys %s; skipping",
                        missing,
                    )
                    continue
                # Derive request_address from http_address
                # api path suffix is appended at request time
                instance = {
                    "role": role,
                    "request_address": f"http://{data['http_address']}/v1",
                    "http_address": data["http_address"],
                    "zmq_address": data["zmq_address"],
                    "dp_size": data["dp_size"],
                    "tp_size": data["tp_size"],
                    "transfer_mode": data["transfer_mode"],
                }
                # zmq_address format: "host:IP,handshake:PORT,notify:PORT"
                # Stored verbatim; embedded into the request_id by handle_request.

                global TRANSFER_TYPE
                transfer_mode = instance["transfer_mode"]
                target_list = prefill_instances if role == "P" else decode_instances
                with _list_lock:
                    if TRANSFER_TYPE is None:
                        TRANSFER_TYPE = transfer_mode
                        logger.info("SET TRANSFER TYPE TO %s", TRANSFER_TYPE)
                    elif transfer_mode != TRANSFER_TYPE:
                        logger.error(
                            "Mismatched transfer mode: expected %s, got %s;"
                            " skipping registration of %s",
                            TRANSFER_TYPE,
                            transfer_mode,
                            data["http_address"],
                        )
                        continue
                    existing_idx = next(
                        (
                            idx
                            for idx, i in enumerate(target_list)
                            if i.get("http_address") == data["http_address"]
                        ),
                        None,
                    )
                    if existing_idx is not None:
                        target_list[existing_idx] = instance
                        logger.info(
                            "Updated existing %s instance: %s",
                            "Prefill" if role == "P" else "Decode",
                            instance,
                        )
                    else:
                        target_list.append(instance)
                        logger.info(
                            "Registered %s instance: %s",
                            "Prefill" if role == "P" else "Decode",
                            instance,
                        )
            else:
                logger.warning(
                    "Received message with unrecognized type %r; ignoring",
                    data.get("type"),
                )


defstart_service_discovery(hostname, port):
    if not hostname:
        hostname = socket.gethostname()
    if port == 0:
        raise ValueError("Port cannot be 0")

    _listener_thread = threading.Thread(
        target=_listen_for_register, args=(hostname, port), daemon=True
    )
    _listener_thread.start()
    return _listener_thread


async defsend_request_to_prefill(
    endpoint, req_data, request_id, selected_prefill_dp_rank
):
    req_data_copy = req_data

    req_data_copy["kv_transfer_params"].update(
        {
            "do_remote_decode": True,
            "do_remote_prefill": False,
            "remote_engine_id": None,
            "remote_block_ids": None,
        }
    )
    req_data_copy["stream"] = False
    req_data_copy["max_tokens"] = 1
    if "max_completion_tokens" in req_data_copy:
        req_data_copy["max_completion_tokens"] = 1
    if "stream_options" in req_data_copy:
        del req_data_copy["stream_options"]
    async with aiohttp.ClientSession(
        timeout=aiohttp.ClientTimeout(total=6 * 6000 * 6000)
    ) as session:
        headers = {
            "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}",
            "X-Request-Id": request_id,
        }
        if selected_prefill_dp_rank is not None:
            headers["X-data-parallel-rank"] = str(selected_prefill_dp_rank)
        async with session.post(
            url=endpoint, json=req_data_copy, headers=headers
        ) as response:
            if response.status == 200:
                return await response.json()

            else:
                error_message = (
                    f"send_request_to_prefill response ={response},"
                    f"reason={response.reason}, status={response.status},"
                    f"method={response.method}, url={response.url},"
                    f"real_url={response.real_url}"
                )
                raise RuntimeError(error_message)


async defstart_decode_request(endpoint, req_data, request_id):
    session = aiohttp.ClientSession(
        timeout=aiohttp.ClientTimeout(total=6 * 6000 * 6000)
    )
    headers = {
        "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}",
        "X-Request-Id": request_id,
    }
    response = await session.post(url=endpoint, json=req_data, headers=headers)
    return session, response


async defstream_decode_response(session, response, request_id):
    try:
        if response.status == 200:
            async for chunk_bytes in response.content.iter_chunked(1024):
                yield chunk_bytes
        else:
            error_message = (
                f"stream_decode_response response ={response},"
                f"reason={response.reason}, status={response.status},"
                f"method={response.method}, url={response.url},"
                f"real_url={response.real_url}"
            )
            raise RuntimeError(error_message)
    finally:
        await session.close()


defexample_round_robin_dp_loader(request_number, dp_size):
    return request_nums % dp_size


@app.route("/v1/completions", methods=["POST"])
async defhandle_completions_request():
    return await handle_request("/completions", request)


@app.route("/v1/chat/completions", methods=["POST"])
async defhandle_chat_completions_request():
    return await handle_request("/chat/completions", request)


async defhandle_request(api: str, request: Request):
    try:
        with _list_lock:
            global request_nums
            request_nums += 1

        req_data = await request.get_json()

        prefill_instance_endpoint = None
        decode_instance_endpoint = None
        error_msg = (
            "Service Unavailable: No prefill or decode instances are registered."
        )
        if not prefill_instances or not decode_instances:
            return await make_response(
                (
                    error_msg,
                    503,
                )
            )
        pid = request_nums % len(prefill_instances)
        did = request_nums % len(decode_instances)
        prefill_instance_endpoint = prefill_instances[pid]
        decode_instance_endpoint = decode_instances[did]

        selected_prefill_dp_rank = None
        if prefill_instance_endpoint["dp_size"] > 1:
            selected_prefill_dp_rank = example_round_robin_dp_loader(
                request_nums // len(prefill_instance_endpoint),
                prefill_instance_endpoint["dp_size"],
            )

        # Embed both zmq_addresses in the request_id so the connector can parse
        # the peer's host/ports from it, similar to P2P-NCCL
        uid = str(uuid.uuid4()).replace("-", "")
        request_id = (
            f"___prefill_addr_{prefill_instance_endpoint['zmq_address']}"
            f"___decode_addr_{decode_instance_endpoint['zmq_address']}"
            f"_{uid}"
        )

        transfer_id = f"{MoRIIOConstants.TRANSFER_PREFIX}-{str(uuid.uuid4())}"

        req_data_to_prefill = copy.deepcopy(req_data)
        req_data_to_prefill["kv_transfer_params"] = {}
        req_data["kv_transfer_params"] = {}
        req_data_to_prefill["kv_transfer_params"]["remote_dp_size"] = (
            decode_instance_endpoint["dp_size"]
        )
        req_data_to_prefill["kv_transfer_params"]["remote_tp_size"] = (
            decode_instance_endpoint["tp_size"]
        )
        req_data_to_prefill["kv_transfer_params"]["transfer_id"] = transfer_id

        prefill_request_url = prefill_instance_endpoint["request_address"] + api
        send_prefill_task = asyncio.create_task(
            send_request_to_prefill(
                prefill_request_url,
                req_data_to_prefill,
                request_id,
                selected_prefill_dp_rank,
            )
        )

        req_data["max_tokens"] -= 1

        req_data["kv_transfer_params"] = {
            "do_remote_decode": False,
            "do_remote_prefill": True,
            "remote_engine_id": None,
            "remote_block_ids": None,
            "transfer_id": transfer_id,
        }
        if TRANSFER_TYPE == "READ":
            # In read mode, prefill and decode are executed serially.
            prefill_response = await send_prefill_task
            prefill_kv = prefill_response["kv_transfer_params"]
            req_data["kv_transfer_params"]["remote_engine_id"] = prefill_kv[
                "remote_engine_id"
            ]
            req_data["kv_transfer_params"]["remote_block_ids"] = prefill_kv[
                "remote_block_ids"
            ]
            req_data["kv_transfer_params"]["transfer_id"] = prefill_kv["transfer_id"]

        req_data["kv_transfer_params"]["remote_dp_size"] = prefill_instance_endpoint[
            "dp_size"
        ]
        req_data["kv_transfer_params"]["remote_tp_size"] = prefill_instance_endpoint[
            "tp_size"
        ]

        if selected_prefill_dp_rank is not None:
            req_data["kv_transfer_params"]["remote_dp_rank"] = selected_prefill_dp_rank

        decode_request_url = decode_instance_endpoint["request_address"] + api
        decode_request_task = asyncio.create_task(
            start_decode_request(decode_request_url, req_data, request_id)
        )

        session, decode_response = await decode_request_task
        stream_generator = stream_decode_response(session, decode_response, request_id)
        response = await make_response(stream_generator)
        return response
    except Exception as e:
        logger.exception("An error occurred while handling the request: %s", e)
        return await make_response(
            (
                f"Internal Server Error: {e!s}",
                500,
            )
        )


async defsend_profile_cmd(req_data: dict, profiler_cmd: str):
    assert profiler_cmd in {"start", "stop"}

    with _list_lock:
        p_instances = list(prefill_instances)
        d_instances = list(decode_instances)

    if not p_instances and not d_instances:
        raise RuntimeError(
            "Service Unavailable: No prefill or decode instances are registered."
        )

    headers = {
        "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}",
    }

    tasks = []

    async with aiohttp.ClientSession(
        timeout=aiohttp.ClientTimeout(total=60)
    ) as session:
        for instances in (p_instances, d_instances):
            for inst in instances:
                _p = urlparse(inst["request_address"])
                url = f"http://{_p.hostname}:{_p.port}/{profiler_cmd}_profile"

                tasks.append(
                    session.post(
                        url,
                        json=req_data,
                        headers=headers,
                    )
                )

        responses = await asyncio.gather(*tasks, return_exceptions=True)

        for r in responses:
            if isinstance(r, Exception):
                raise r
            if r.status >= 400:
                msg = await r.text()
                raise RuntimeError(f"{profiler_cmd}_profile failed: {r.status}, {msg}")

        return await responses[0].json()


@app.post("/start_profile")
async defstart_profile():
    try:
        req_data = await request.get_json()
        return await send_profile_cmd(req_data, "start")
    except Exception as e:
        logger.exception("start_profile failed: %s", e)
        return await make_response((str(e), 500))


@app.post("/stop_profile")
async defstop_profile():
    try:
        req_data = await request.get_json()
        return await send_profile_cmd(req_data, "stop")
    except Exception as e:
        logger.exception("stop_profile failed: %s", e)
        return await make_response((str(e), 500))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=10001)
    args = parser.parse_args()

    t = start_service_discovery("0.0.0.0", 36367)
    app.debug = True
    app.config["BODY_TIMEOUT"] = 360000
    app.config["RESPONSE_TIMEOUT"] = 360000

    app.run(host="0.0.0.0", port=args.port)
    t.join()
```