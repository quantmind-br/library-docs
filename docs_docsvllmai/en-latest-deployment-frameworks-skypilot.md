---
title: SkyPilot - vLLM
url: https://docs.vllm.ai/en/latest/deployment/frameworks/skypilot/
source: sitemap
fetched_at: 2026-05-07T21:11:55.684348235-03:00
rendered_js: false
word_count: 520
summary: This document explains how to deploy, scale, and manage vLLM inference services on cloud infrastructure using the SkyPilot framework.
tags:
    - vllm
    - skypilot
    - llm-deployment
    - cloud-computing
    - autoscaling
    - kubernetes
    - model-serving
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/deployment/frameworks/skypilot.md "Edit this page")

[![vLLM](https://imgur.com/yxtzPEu.png)](https://imgur.com/yxtzPEu.png)

vLLM can be **run and scaled to multiple service replicas on clouds and Kubernetes** with [SkyPilot](https://github.com/skypilot-org/skypilot), an open-source framework for running LLMs on any cloud. More examples for various open models, such as Llama-3, Mixtral, etc., can be found in [SkyPilot AI gallery](https://skypilot.readthedocs.io/en/latest/gallery/index.html).

## Prerequisites[¶](#prerequisites "Permanent link")

- Go to the [HuggingFace model page](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) and request access to the model `meta-llama/Meta-Llama-3-8B-Instruct`.
- Check that you have installed SkyPilot ([docs](https://skypilot.readthedocs.io/en/latest/getting-started/installation.html)).
- Check that `sky check` shows clouds or Kubernetes are enabled.

```
pipinstallskypilot-nightly
skycheck
```

## Run on a single instance[¶](#run-on-a-single-instance "Permanent link")

See the vLLM SkyPilot YAML for serving, [serving.yaml](https://github.com/skypilot-org/skypilot/blob/master/llm/vllm/serve.yaml).

Yaml

```
resources:
accelerators:{L4,A10g,A10,L40,A40,A100,A100-80GB}# We can use cheaper accelerators for 8B model.
use_spot:True
disk_size:512# Ensure model checkpoints can fit.
disk_tier:best
ports:8081# Expose to internet traffic.

envs:
PYTHONUNBUFFERED:1
MODEL_NAME:meta-llama/Meta-Llama-3-8B-Instruct
HF_TOKEN:<your-huggingface-token># Change to your own huggingface token, or use --env to pass.

setup:|
conda create -n vllm python=3.10 -y
conda activate vllm

pip install vllm==0.4.0.post1
# Install Gradio for web UI.
pip install gradio openai
pip install flash-attn==2.5.7

run:|
conda activate vllm
echo 'Starting vllm api server...'
vllm serve $MODEL_NAME \
--port 8081 \
--trust-remote-code \
--tensor-parallel-size $SKYPILOT_NUM_GPUS_PER_NODE \
2>&1 | tee api_server.log &

echo 'Waiting for vllm api server to start...'
while ! `cat api_server.log | grep -q 'Uvicorn running on'`; do sleep 1; done

echo 'Starting gradio server...'
git clone https://github.com/vllm-project/vllm.git || true
python vllm/examples/online_serving/gradio_openai_chatbot_webserver.py \
-m $MODEL_NAME \
--port 8811 \
--model-url http://localhost:8081/v1 \
--stop-token-ids 128009,128001
```

Start the serving the Llama-3 8B model on any of the candidate GPUs listed (L4, A10g, ...):

```
HF_TOKEN="your-huggingface-token"skylaunchserving.yaml--envHF_TOKEN
```

Check the output of the command. There will be a shareable gradio link (like the last line of the following). Open it in your browser to use the LLaMA model to do the text completion.

```
(task, pid=7431) Running on public URL: https://<gradio-hash>.gradio.live
```

**Optional**: Serve the 70B model instead of the default 8B and use more GPU:

```
HF_TOKEN="your-huggingface-token"\
skylaunchserving.yaml\
--gpusA100:8\
--envHF_TOKEN\
--envMODEL_NAME=meta-llama/Meta-Llama-3-70B-Instruct
```

## Scale up to multiple replicas[¶](#scale-up-to-multiple-replicas "Permanent link")

SkyPilot can scale up the service to multiple service replicas with built-in autoscaling, load-balancing and fault-tolerance. You can do it by adding a services section to the YAML file.

Yaml

```
service:
replicas:2
# An actual request for readiness probe.
readiness_probe:
path:/v1/chat/completions
post_data:
model:$MODEL_NAME
messages:
-role:user
content:Hello! What is your name?
max_completion_tokens:1
```

Yaml

```
service:
replicas:2
# An actual request for readiness probe.
readiness_probe:
path:/v1/chat/completions
post_data:
model:$MODEL_NAME
messages:
-role:user
content:Hello! What is your name?
max_completion_tokens:1

resources:
accelerators:{L4,A10g,A10,L40,A40,A100,A100-80GB}# We can use cheaper accelerators for 8B model.
use_spot:True
disk_size:512# Ensure model checkpoints can fit.
disk_tier:best
ports:8081# Expose to internet traffic.

envs:
PYTHONUNBUFFERED:1
MODEL_NAME:meta-llama/Meta-Llama-3-8B-Instruct
HF_TOKEN:<your-huggingface-token># Change to your own huggingface token, or use --env to pass.

setup:|
conda create -n vllm python=3.10 -y
conda activate vllm

pip install vllm==0.4.0.post1
# Install Gradio for web UI.
pip install gradio openai
pip install flash-attn==2.5.7

run:|
conda activate vllm
echo 'Starting vllm api server...'
vllm serve $MODEL_NAME \
--port 8081 \
--trust-remote-code \
--tensor-parallel-size $SKYPILOT_NUM_GPUS_PER_NODE \
2>&1 | tee api_server.log
```

Start the serving the Llama-3 8B model on multiple replicas:

```
HF_TOKEN="your-huggingface-token"\
skyserveup-nvllmserving.yaml\
--envHF_TOKEN
```

Wait until the service is ready:

```
watch-n10skyservestatusvllm
```

Example outputs:

```
Services
NAME  VERSION  UPTIME  STATUS  REPLICAS  ENDPOINT
vllm  1        35s     READY   2/2       xx.yy.zz.100:30001

Service Replicas
SERVICE_NAME  ID  VERSION  IP            LAUNCHED     RESOURCES                STATUS  REGION
vllm          1   1        xx.yy.zz.121  18 mins ago  1x GCP([Spot]{'L4': 1})  READY   us-east4
vllm          2   1        xx.yy.zz.245  18 mins ago  1x GCP([Spot]{'L4': 1})  READY   us-east4
```

After the service is READY, you can find a single endpoint for the service and access the service with the endpoint:

Commands

```
ENDPOINT=$(skyservestatus--endpoint8081vllm)
curl-Lhttp://$ENDPOINT/v1/chat/completions\
-H"Content-Type: application/json"\
-d'{
    "model": "meta-llama/Meta-Llama-3-8B-Instruct",
    "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "Who are you?"
    }
    ],
    "stop_token_ids": [128009,  128001]
  }'
```

To enable autoscaling, you could replace the `replicas` with the following configs in `service`:

```
service:
replica_policy:
min_replicas:2
max_replicas:4
target_qps_per_replica:2
```

This will scale the service up to when the QPS exceeds 2 for each replica.

Yaml

```
service:
replica_policy:
min_replicas:2
max_replicas:4
target_qps_per_replica:2
# An actual request for readiness probe.
readiness_probe:
path:/v1/chat/completions
post_data:
model:$MODEL_NAME
messages:
-role:user
content:Hello! What is your name?
max_completion_tokens:1

resources:
accelerators:{L4,A10g,A10,L40,A40,A100,A100-80GB}# We can use cheaper accelerators for 8B model.
use_spot:True
disk_size:512# Ensure model checkpoints can fit.
disk_tier:best
ports:8081# Expose to internet traffic.

envs:
PYTHONUNBUFFERED:1
MODEL_NAME:meta-llama/Meta-Llama-3-8B-Instruct
HF_TOKEN:<your-huggingface-token># Change to your own huggingface token, or use --env to pass.

setup:|
conda create -n vllm python=3.10 -y
conda activate vllm

pip install vllm==0.4.0.post1
# Install Gradio for web UI.
pip install gradio openai
pip install flash-attn==2.5.7

run:|
conda activate vllm
echo 'Starting vllm api server...'
vllm serve $MODEL_NAME \
--port 8081 \
--trust-remote-code \
--tensor-parallel-size $SKYPILOT_NUM_GPUS_PER_NODE \
2>&1 | tee api_server.log
```

To update the service with the new config:

```
HF_TOKEN="your-huggingface-token"skyserveupdatevllmserving.yaml--envHF_TOKEN
```

To stop the service:

### **Optional**: Connect a GUI to the endpoint[¶](#optional-connect-a-gui-to-the-endpoint "Permanent link")

It is also possible to access the Llama-3 service with a separate GUI frontend, so the user requests send to the GUI will be load-balanced across replicas.

Yaml

```
envs:
MODEL_NAME:meta-llama/Meta-Llama-3-8B-Instruct
ENDPOINT:x.x.x.x:3031# Address of the API server running vllm.

resources:
cpus:2

setup:|
conda create -n vllm python=3.10 -y
conda activate vllm

# Install Gradio for web UI.
pip install gradio openai

run:|
conda activate vllm
export PATH=$PATH:/sbin

echo 'Starting gradio server...'
git clone https://github.com/vllm-project/vllm.git || true
python vllm/examples/online_serving/gradio_openai_chatbot_webserver.py \
-m $MODEL_NAME \
--port 8811 \
--model-url http://$ENDPOINT/v1 \
--stop-token-ids 128009,128001 | tee ~/gradio.log
```

1. Start the chat web UI:
   
   ```
   skylaunch\
   -cgui./gui.yaml\
   --envENDPOINT=$(skyservestatus--endpointvllm)
   ```
2. Then, we can access the GUI at the returned gradio link:
   
   ```
   | INFO | stdout | Running on public URL: https://6141e84201ce0bb4ed.gradio.live
   ```