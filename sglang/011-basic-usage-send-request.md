---
title: Sending Requests — SGLang
url: https://docs.sglang.io/basic_usage/send_request.html
source: crawler
fetched_at: 2026-02-04T08:46:40.427103669-03:00
rendered_js: false
word_count: 426
summary: This document provides a quick-start guide for launching an SGLang server and sending chat completion requests using cURL and Python.
tags:
    - sglang
    - chat-completions
    - llm-serving
    - python-requests
    - curl
    - api-integration
category: tutorial
---

## Sending Requests[#](#Sending-Requests "Link to this heading")

This notebook provides a quick-start guide to use SGLang in chat completions after installation. Once your server is running, API documentation is available at `http://localhost:30000/docs` (Swagger UI), `http://localhost:30000/redoc` (ReDoc), or `http://localhost:30000/openapi.json` (OpenAPI spec, useful for AI agents). Replace `30000` with your port if using a different one.

- For Vision Language Models, see [OpenAI APIs - Vision](https://docs.sglang.io/basic_usage/openai_api_vision.html).
- For Embedding Models, see [OpenAI APIs - Embedding](https://docs.sglang.io/basic_usage/openai_api_embeddings.html) and [Encode (embedding model)](https://docs.sglang.io/basic_usage/native_api.html#Encode-%28embedding-model%29).
- For Reward Models, see [Classify (reward model)](https://docs.sglang.io/basic_usage/native_api.html#Classify-%28reward-model%29).

## Launch A Server[#](#Launch-A-Server "Link to this heading")

```
fromsglang.test.doc_patchimport launch_server_cmd
fromsglang.utilsimport wait_for_server, print_highlight, terminate_process

# This is equivalent to running the following command in your terminal
# python3 -m sglang.launch_server --model-path qwen/qwen2.5-0.5b-instruct --host 0.0.0.0

server_process, port = launch_server_cmd(
"""
python3 -m sglang.launch_server --model-path qwen/qwen2.5-0.5b-instruct \
 --host 0.0.0.0 --log-level warning
"""
)

wait_for_server(f"http://localhost:{port}")
```

```
[2026-02-04 11:26:07] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:26:07] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:26:07] INFO utils.py:164: NumExpr defaulting to 16 threads.
```

```
[2026-02-04 11:26:13] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:26:13] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:26:13] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:26:15] INFO server_args.py:1796: Attention backend not specified. Use fa3 backend by default.
[2026-02-04 11:26:15] INFO server_args.py:2783: Set soft_watchdog_timeout since in CI
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[2026-02-04 11:26:22] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:26:22] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:26:22] INFO utils.py:164: NumExpr defaulting to 16 threads.
[2026-02-04 11:26:22] INFO utils.py:148: Note: detected 112 virtual cores but NumExpr set to maximum of 64, check "NUMEXPR_MAX_THREADS" environment variable.
[2026-02-04 11:26:22] INFO utils.py:151: Note: NumExpr detected 112 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
[2026-02-04 11:26:22] INFO utils.py:164: NumExpr defaulting to 16 threads.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.cudart module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.runtime module instead.
<frozen importlib._bootstrap_external>:1184: FutureWarning: The cuda.nvrtc module is deprecated and will be removed in a future release, please switch to use the cuda.bindings.nvrtc module instead.
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[2026-02-04 11:26:28] Ignore import error when loading sglang.srt.models.glm_ocr: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:26:28] Ignore import error when loading sglang.srt.models.glm_ocr_nextn: No module named 'transformers.models.glm_ocr'
[2026-02-04 11:26:28] Ignore import error when loading sglang.srt.models.glmasr: cannot import name 'GlmAsrConfig' from 'transformers' (/usr/local/lib/python3.10/dist-packages/transformers/__init__.py)
[2026-02-04 11:26:28] Ignore import error when loading sglang.srt.models.midashenglm: Detected that PyTorch and TorchAudio were compiled with different CUDA versions. PyTorch has CUDA version 12.8 whereas TorchAudio has CUDA version 12.9. Please install the TorchAudio version that matches your PyTorch version.
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  4.50it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  4.49it/s]

Capturing batches (bs=1 avail_mem=71.93 GB): 100%|██████████| 3/3 [00:00<00:00,  6.15it/s]
```

**NOTE: Typically, the server runs in a separate terminal.**  
**In this notebook, we run the server and notebook code together, so their outputs are combined.**  
**To improve clarity, the server logs are displayed in the original black color, while the notebook outputs are highlighted in blue.**  
**To reduce the log length, we set the log level to warning for the server, the default log level is info.**  
**We are running those notebooks in a CI environment, so the throughput is not representative of the actual performance.**

## Using cURL[#](#Using-cURL "Link to this heading")

```
importsubprocess,json

curl_command = f"""
curl -s http://localhost:{port}/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{{"model": "qwen/qwen2.5-0.5b-instruct", "messages": [{{"role": "user", "content": "What is the capital of France?"}}]}}'
"""

response = json.loads(subprocess.check_output(curl_command, shell=True))
print_highlight(response)
```

**{'id': 'de246edc5af04f319ba457695f274d2b', 'object': 'chat.completion', 'created': 1770204396, 'model': 'qwen/qwen2.5-0.5b-instruct', 'choices': \[{'index': 0, 'message': {'role': 'assistant', 'content': 'The capital of France is Paris.', 'reasoning\_content': None, 'tool\_calls': None}, 'logprobs': None, 'finish\_reason': 'stop', 'matched\_stop': 151645}], 'usage': {'prompt\_tokens': 36, 'total\_tokens': 44, 'completion\_tokens': 8, 'prompt\_tokens\_details': None, 'reasoning\_tokens': 0}, 'metadata': {'weight\_version': 'default'}}**

## Using Python Requests[#](#Using-Python-Requests "Link to this heading")

```
importrequests

url = f"http://localhost:{port}/v1/chat/completions"

data = {
    "model": "qwen/qwen2.5-0.5b-instruct",
    "messages": [{"role": "user", "content": "What is the capital of France?"}],
}

response = requests.post(url, json=data)
print_highlight(response.json())
```

**{'id': '794aa3547264454aa8f2114d87718547', 'object': 'chat.completion', 'created': 1770204396, 'model': 'qwen/qwen2.5-0.5b-instruct', 'choices': \[{'index': 0, 'message': {'role': 'assistant', 'content': 'The capital of France is Paris.', 'reasoning\_content': None, 'tool\_calls': None}, 'logprobs': None, 'finish\_reason': 'stop', 'matched\_stop': 151645}], 'usage': {'prompt\_tokens': 36, 'total\_tokens': 44, 'completion\_tokens': 8, 'prompt\_tokens\_details': None, 'reasoning\_tokens': 0}, 'metadata': {'weight\_version': 'default'}}**

## Using OpenAI Python Client[#](#Using-OpenAI-Python-Client "Link to this heading")

```
importopenai

client = openai.Client(base_url=f"http://127.0.0.1:{port}/v1", api_key="None")

response = client.chat.completions.create(
    model="qwen/qwen2.5-0.5b-instruct",
    messages=[
        {"role": "user", "content": "List 3 countries and their capitals."},
    ],
    temperature=0,
    max_tokens=64,
)
print_highlight(response)
```

**ChatCompletion(id='f7a5e3ae912e4fdb8ea9450d9f0b9dc8', choices=\[Choice(finish\_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='Sure, here are three countries and their respective capitals:\\n\\n1. \*\*United States\** - Washington, D.C.\\n2. \*\*Canada\** - Ottawa\\n3. \*\*Australia\** - Canberra', refusal=None, role='assistant', annotations=None, audio=None, function\_call=None, tool\_calls=None, reasoning\_content=None), matched\_stop=151645)], created=1770204396, model='qwen/qwen2.5-0.5b-instruct', object='chat.completion', service\_tier=None, system\_fingerprint=None, usage=CompletionUsage(completion\_tokens=39, prompt\_tokens=37, total\_tokens=76, completion\_tokens\_details=None, prompt\_tokens\_details=None, reasoning\_tokens=0), metadata={'weight\_version': 'default'})**

### Streaming[#](#Streaming "Link to this heading")

```
importopenai

client = openai.Client(base_url=f"http://127.0.0.1:{port}/v1", api_key="None")

# Use stream=True for streaming responses
response = client.chat.completions.create(
    model="qwen/qwen2.5-0.5b-instruct",
    messages=[
        {"role": "user", "content": "List 3 countries and their capitals."},
    ],
    temperature=0,
    max_tokens=64,
    stream=True,
)

# Handle the streaming output
for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

```
Sure, here are three countries and their respective capitals:

1. **United States** - Washington, D.C.
2. **Canada** - Ottawa
3. **Australia** - Canberra
```

## Using Native Generation APIs[#](#Using-Native-Generation-APIs "Link to this heading")

You can also use the native `/generate` endpoint with requests, which provides more flexibility. An API reference is available at [Sampling Parameters](https://docs.sglang.io/basic_usage/sampling_params.html).

```
importrequests

response = requests.post(
    f"http://localhost:{port}/generate",
    json={
        "text": "The capital of France is",
        "sampling_params": {
            "temperature": 0,
            "max_new_tokens": 32,
        },
    },
)

print_highlight(response.json())
```

**{'text': ' Paris. It is the largest city in Europe and the second largest city in the world. It is located in the south of France, on the banks of the', 'output\_ids': \[12095, 13, 1084, 374, 279, 7772, 3283, 304, 4505, 323, 279, 2086, 7772, 3283, 304, 279, 1879, 13, 1084, 374, 7407, 304, 279, 9806, 315, 9625, 11, 389, 279, 13959, 315, 279], 'meta\_info': {'id': '71f5c84f80374000b160babfe95c78af', 'finish\_reason': {'type': 'length', 'length': 32}, 'prompt\_tokens': 5, 'weight\_version': 'default', 'total\_retractions': 0, 'completion\_tokens': 32, 'cached\_tokens': 2, 'cached\_tokens\_details': None, 'e2e\_latency': 0.05470705032348633, 'response\_sent\_to\_client\_ts': 1770204396.993388}}**

### Streaming[#](#id1 "Link to this heading")

```
importrequests,json

response = requests.post(
    f"http://localhost:{port}/generate",
    json={
        "text": "The capital of France is",
        "sampling_params": {
            "temperature": 0,
            "max_new_tokens": 32,
        },
        "stream": True,
    },
    stream=True,
)

prev = 0
for chunk in response.iter_lines(decode_unicode=False):
    chunk = chunk.decode("utf-8")
    if chunk and chunk.startswith("data:"):
        if chunk == "data: [DONE]":
            break
        data = json.loads(chunk[5:].strip("\n"))
        output = data["text"]
        print(output[prev:], end="", flush=True)
        prev = len(output)
```

```
 Paris. It is the largest city in Europe and the second largest city in the world. It is located in the south of France, on the banks of the
```

```
terminate_process(server_process)
```