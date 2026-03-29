---
title: vLLM | Mistral Docs
url: https://docs.mistral.ai/deployment/self-deployment/vllm
source: crawler
fetched_at: 2026-01-29T07:34:14.08174994-03:00
rendered_js: false
word_count: 342
summary: A guide on deploying Mistral AI models using vLLM, a high-throughput and memory-efficient inference and serving engine.
tags:
    - vLLM
    - Mistral AI
    - inference
    - deployment
    - LLM
category: guide
---

[vLLM](https://github.com/vllm-project/vllm) is an open-source LLM inference and serving engine. It is particularly appropriate as a target platform for self-deploying Mistral models on-premise.

## Prerequisites

- The hardware requirements for vLLM are listed on its [installation documentation page](https://docs.vllm.ai/en/latest/getting_started/installation.html).
- By default, vLLM sources the model weights from Hugging Face. To access Mistral model repositories, you need to be authenticated on Hugging Face, so an access token `HF_TOKEN` with the `READ` permission will be required. You should also ensure that you have accepted the conditions of access on each model card page.
- If you already have the model artifacts on your infrastructure, you can use them directly by pointing vLLM to their local path instead of a Hugging Face model ID. In this scenario, you will be able to skip all Hugging Face-related setup steps.

## Getting Started

The following sections will guide you through the process of deploying and querying Mistral models on vLLM.

## Installing vLLM

- Create a Python virtual environment and install the `vllm` package (version `>=0.6.1.post1` to ensure maximum compatibility with all Mistral models).
- Authenticate on the HuggingFace Hub using your access token `$HF_TOKEN`:
  
  ```
  huggingface-cli login --token $HF_TOKEN
  ```
  
  ```
  huggingface-cli login --token $HF_TOKEN
  ```

## Offline Mode Inference

When using vLLM in **offline mode**, the model is loaded and used for one-off batch inference workloads.

```
from vllm import LLM
from vllm.sampling_params import SamplingParams
model_name ="mistralai/Mistral-NeMo-Instruct-2407"sampling_params = SamplingParams(max_tokens=8192)llm = LLM(    model=model_name,    tokenizer_mode="mistral",    load_format="mistral",    config_format="mistral",)messages =[{"role":"user","content":"Who is the best French painter? Answer with detailed explanations.",}]res = llm.chat(messages=messages, sampling_params=sampling_params)print(res[0].outputs[0].text)
```

```
from vllm import LLM
from vllm.sampling_params import SamplingParams
model_name ="mistralai/Mistral-NeMo-Instruct-2407"sampling_params = SamplingParams(max_tokens=8192)llm = LLM(    model=model_name,    tokenizer_mode="mistral",    load_format="mistral",    config_format="mistral",)messages =[{"role":"user","content":"Who is the best French painter? Answer with detailed explanations.",}]res = llm.chat(messages=messages, sampling_params=sampling_params)print(res[0].outputs[0].text)
```

## Server Mode Inference

In **server mode**, vLLM spawns an HTTP server that continuously waits for clients to connect and send requests concurrently. The server exposes a REST API that implements the OpenAI protocol, allowing you to directly reuse existing code relying on the OpenAI API.

Start the inference server to deploy your model, e.g., for Mistral NeMo:

```
vllm serve mistralai/Mistral-Nemo-Instruct-2407 \    --tokenizer_mode mistral \    --config_format mistral \    --load_format mistral
```

```
vllm serve mistralai/Mistral-Nemo-Instruct-2407 \    --tokenizer_mode mistral \    --config_format mistral \    --load_format mistral
```

You can now run inference requests with text input:

```
curl --location 'http://localhost:8000/v1/chat/completions'\    --header 'Content-Type: application/json'\    --header 'Authorization: Bearer token'\    --data '{
        "model": "mistralai/Mistral-Nemo-Instruct-2407",
        "messages": [
            {
                "role": "user",
                "content": "Who is the best French painter? Answer in one short sentence."
            }
        ]
    }'
```

```
curl --location 'http://localhost:8000/v1/chat/completions'\    --header 'Content-Type: application/json'\    --header 'Authorization: Bearer token'\    --data '{
        "model": "mistralai/Mistral-Nemo-Instruct-2407",
        "messages": [
            {
                "role": "user",
                "content": "Who is the best French painter? Answer in one short sentence."
            }
        ]
    }'
```

## Deploying with Docker

If you are looking to deploy vLLM as a containerized inference server, you can leverage the project's official Docker image (see more details in the [vLLM Docker documentation](https://docs.vllm.ai/en/latest/serving/deploying_with_docker.html)).

- Set the HuggingFace access token environment variable in your shell:
  
  ```
  exportHF_TOKEN=your-access-token
  ```
  
  ```
  exportHF_TOKEN=your-access-token
  ```
- Run the Docker command to start the container:
  
  ```
  docker run --runtime nvidia --gpus all \    -v ~/.cache/huggingface:/root/.cache/huggingface \    --env "HUGGING_FACE_HUB_TOKEN=${HF_TOKEN}"\    -p 8000:8000 \    --ipc=host \    vllm/vllm-openai:latest \    --model mistralai/Mistral-NeMo-Instruct-2407 \    --tokenizer_mode mistral \    --load_format mistral \    --config_format mistral
  ```
  
  ```
  docker run --runtime nvidia --gpus all \    -v ~/.cache/huggingface:/root/.cache/huggingface \    --env "HUGGING_FACE_HUB_TOKEN=${HF_TOKEN}"\    -p 8000:8000 \    --ipc=host \    vllm/vllm-openai:latest \    --model mistralai/Mistral-NeMo-Instruct-2407 \    --tokenizer_mode mistral \    --load_format mistral \    --config_format mistral
  ```

Once the container is up and running, you will be able to run inference on your model using the same code as in a standalone deployment.