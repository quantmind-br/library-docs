---
title: RunPod - vLLM
url: https://docs.vllm.ai/en/latest/deployment/frameworks/runpod/
source: sitemap
fetched_at: 2026-05-07T21:11:54.679356874-03:00
rendered_js: false
word_count: 256
summary: This document provides instructions for deploying and exposing a vLLM inference server on the RunPod cloud platform, including troubleshooting steps and verification methods.
tags:
    - vllm
    - runpod
    - gpu-deployment
    - inference-server
    - cloud-computing
    - model-hosting
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/deployment/frameworks/runpod.md "Edit this page")

vLLM can be deployed on [RunPod](https://www.runpod.io/), a cloud GPU platform that provides on-demand and serverless GPU instances for AI inference workloads.

## Prerequisites[¶](#prerequisites "Permanent link")

- A RunPod account with GPU pod access
- A GPU pod running a CUDA-compatible template (e.g., `runpod/pytorch`)

## Starting the Server[¶](#starting-the-server "Permanent link")

SSH into your RunPod pod and launch the vLLM OpenAI-compatible server:

```
python-mvllm.entrypoints.openai.api_server\
--model<model-name>\
--host0.0.0.0\
--port8000
```

Note

Use `--host 0.0.0.0` to bind to all interfaces so the server is reachable from outside the container.

## Exposing Port 8000[¶](#exposing-port-8000 "Permanent link")

RunPod exposes HTTP services through its proxy. To make port 8000 accessible:

1. In the RunPod dashboard, navigate to your pod settings.
2. Add `8000` to the list of exposed HTTP ports.
3. After the pod restarts, RunPod provides a public URL in the format:
   
   ```
   https://<pod-id>-8000.proxy.runpod.net
   ```

## Troubleshooting 502 Bad Gateway[¶](#troubleshooting-502-bad-gateway "Permanent link")

A `502 Bad Gateway` error from the RunPod proxy typically means the server is not yet listening. Common causes:

- **Model still loading** — Large models take time to download and load into GPU memory. Check the pod logs for progress.
- **Wrong host binding** — Ensure you passed `--host 0.0.0.0`. Binding to `127.0.0.1` (the default) makes the server unreachable from the proxy.
- **Port mismatch** — Verify the `--port` value matches the port exposed in the RunPod dashboard.
- **Out of GPU memory** — The model may be too large for the allocated GPU. Check logs for CUDA OOM errors and consider using a larger instance or adding `--tensor-parallel-size` for multi-GPU pods.

## Verifying the Deployment[¶](#verifying-the-deployment "Permanent link")

Once the server is running, test it with a curl request:

Command

```
curlhttps://<pod-id>-8000.proxy.runpod.net/v1/chat/completions\
-H"Content-Type: application/json"\
-d'{
        "model": "<model-name>",
        "messages": [
            {"role": "user", "content": "Hello, how are you?"}
        ],
        "max_tokens": 50
    }'
```

Response

```
{
"id":"chat-abc123",
"object":"chat.completion",
"choices":[
{
"message":{
"role":"assistant",
"content":"I'm doing well, thank you for asking! How can I help you today?"
},
"index":0,
"finish_reason":"stop"
}
]
}
```

You can also check the server health endpoint:

```
curlhttps://<pod-id>-8000.proxy.runpod.net/health
```