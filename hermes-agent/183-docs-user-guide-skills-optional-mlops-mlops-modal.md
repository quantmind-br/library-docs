---
title: Modal Serverless Gpu — Serverless GPU cloud platform for running ML workloads | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-modal
source: crawler
fetched_at: 2026-04-24T17:01:25.035552809-03:00
rendered_js: false
word_count: 404
summary: This document serves as a comprehensive reference and guide for using Modal, a serverless GPU cloud platform designed to run Machine Learning workloads. It details various features like deployment modes, GPU configurations, container image creation, persistent storage, and methods for exposing models as APIs.
tags:
    - serverless-gpu
    - mlops
    - modal
    - cloud-platform
    - deployment-guide
    - gpu-reference
category: guide
---

Serverless GPU cloud platform for running ML workloads. Use when you need on-demand GPU access without infrastructure management, deploying ML models as APIs, or running batch jobs with automatic scaling.

SourceOptional — install with `hermes skills install official/mlops/modal`Path`optional-skills/mlops/modal`Version`1.0.0`AuthorOrchestra ResearchLicenseMITDependencies`modal>=0.64.0`Tags`Infrastructure`, `Serverless`, `GPU`, `Cloud`, `Deployment`, `Modal`

## Reference: full SKILL.md[​](#reference-full-skillmd "Direct link to Reference: full SKILL.md")

info

The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.

## Modal Serverless GPU

Comprehensive guide to running ML workloads on Modal's serverless GPU cloud platform.

## When to use Modal[​](#when-to-use-modal "Direct link to When to use Modal")

**Use Modal when:**

- Running GPU-intensive ML workloads without managing infrastructure
- Deploying ML models as auto-scaling APIs
- Running batch processing jobs (training, inference, data processing)
- Need pay-per-second GPU pricing without idle costs
- Prototyping ML applications quickly
- Running scheduled jobs (cron-like workloads)

**Key features:**

- **Serverless GPUs**: T4, L4, A10G, L40S, A100, H100, H200, B200 on-demand
- **Python-native**: Define infrastructure in Python code, no YAML
- **Auto-scaling**: Scale to zero, scale to 100+ GPUs instantly
- **Sub-second cold starts**: Rust-based infrastructure for fast container launches
- **Container caching**: Image layers cached for rapid iteration
- **Web endpoints**: Deploy functions as REST APIs with zero-downtime updates

**Use alternatives instead:**

- **RunPod**: For longer-running pods with persistent state
- **Lambda Labs**: For reserved GPU instances
- **SkyPilot**: For multi-cloud orchestration and cost optimization
- **Kubernetes**: For complex multi-service architectures

## Quick start[​](#quick-start "Direct link to Quick start")

### Installation[​](#installation "Direct link to Installation")

```bash
pip install modal
modal setup  # Opens browser for authentication
```

### Hello World with GPU[​](#hello-world-with-gpu "Direct link to Hello World with GPU")

```python
import modal

app = modal.App("hello-gpu")

@app.function(gpu="T4")
defgpu_info():
import subprocess
return subprocess.run(["nvidia-smi"], capture_output=True, text=True).stdout

@app.local_entrypoint()
defmain():
print(gpu_info.remote())
```

Run: `modal run hello_gpu.py`

### Basic inference endpoint[​](#basic-inference-endpoint "Direct link to Basic inference endpoint")

```python
import modal

app = modal.App("text-generation")
image = modal.Image.debian_slim().pip_install("transformers","torch","accelerate")

@app.cls(gpu="A10G", image=image)
classTextGenerator:
@modal.enter()
defload_model(self):
from transformers import pipeline
        self.pipe = pipeline("text-generation", model="gpt2", device=0)

@modal.method()
defgenerate(self, prompt:str)->str:
return self.pipe(prompt, max_length=100)[0]["generated_text"]

@app.local_entrypoint()
defmain():
print(TextGenerator().generate.remote("Hello, world"))
```

## Core concepts[​](#core-concepts "Direct link to Core concepts")

### Key components[​](#key-components "Direct link to Key components")

ComponentPurpose`App`Container for functions and resources`Function`Serverless function with compute specs`Cls`Class-based functions with lifecycle hooks`Image`Container image definition`Volume`Persistent storage for models/data`Secret`Secure credential storage

### Execution modes[​](#execution-modes "Direct link to Execution modes")

CommandDescription`modal run script.py`Execute and exit`modal serve script.py`Development with live reload`modal deploy script.py`Persistent cloud deployment

## GPU configuration[​](#gpu-configuration "Direct link to GPU configuration")

### Available GPUs[​](#available-gpus "Direct link to Available GPUs")

GPUVRAMBest For`T4`16GBBudget inference, small models`L4`24GBInference, Ada Lovelace arch`A10G`24GBTraining/inference, 3.3x faster than T4`L40S`48GBRecommended for inference (best cost/perf)`A100-40GB`40GBLarge model training`A100-80GB`80GBVery large models`H100`80GBFastest, FP8 + Transformer Engine`H200`141GBAuto-upgrade from H100, 4.8TB/s bandwidth`B200`LatestBlackwell architecture

### GPU specification patterns[​](#gpu-specification-patterns "Direct link to GPU specification patterns")

```python
# Single GPU
@app.function(gpu="A100")

# Specific memory variant
@app.function(gpu="A100-80GB")

# Multiple GPUs (up to 8)
@app.function(gpu="H100:4")

# GPU with fallbacks
@app.function(gpu=["H100","A100","L40S"])

# Any available GPU
@app.function(gpu="any")
```

## Container images[​](#container-images "Direct link to Container images")

```python
# Basic image with pip
image = modal.Image.debian_slim(python_version="3.11").pip_install(
"torch==2.1.0","transformers==4.36.0","accelerate"
)

# From CUDA base
image = modal.Image.from_registry(
"nvidia/cuda:12.1.0-cudnn8-devel-ubuntu22.04",
    add_python="3.11"
).pip_install("torch","transformers")

# With system packages
image = modal.Image.debian_slim().apt_install("git","ffmpeg").pip_install("whisper")
```

## Persistent storage[​](#persistent-storage "Direct link to Persistent storage")

```python
volume = modal.Volume.from_name("model-cache", create_if_missing=True)

@app.function(gpu="A10G", volumes={"/models": volume})
defload_model():
import os
    model_path ="/models/llama-7b"
ifnot os.path.exists(model_path):
        model = download_model()
        model.save_pretrained(model_path)
        volume.commit()# Persist changes
return load_from_path(model_path)
```

## Web endpoints[​](#web-endpoints "Direct link to Web endpoints")

### FastAPI endpoint decorator[​](#fastapi-endpoint-decorator "Direct link to FastAPI endpoint decorator")

```python
@app.function()
@modal.fastapi_endpoint(method="POST")
defpredict(text:str)->dict:
return{"result": model.predict(text)}
```

### Full ASGI app[​](#full-asgi-app "Direct link to Full ASGI app")

```python
from fastapi import FastAPI
web_app = FastAPI()

@web_app.post("/predict")
asyncdefpredict(text:str):
return{"result":await model.predict.remote.aio(text)}

@app.function()
@modal.asgi_app()
deffastapi_app():
return web_app
```

### Web endpoint types[​](#web-endpoint-types "Direct link to Web endpoint types")

DecoratorUse Case`@modal.fastapi_endpoint()`Simple function → API`@modal.asgi_app()`Full FastAPI/Starlette apps`@modal.wsgi_app()`Django/Flask apps`@modal.web_server(port)`Arbitrary HTTP servers

## Dynamic batching[​](#dynamic-batching "Direct link to Dynamic batching")

```python
@app.function()
@modal.batched(max_batch_size=32, wait_ms=100)
asyncdefbatch_predict(inputs:list[str])->list[dict]:
# Inputs automatically batched
return model.batch_predict(inputs)
```

## Secrets management[​](#secrets-management "Direct link to Secrets management")

```bash
# Create secret
modal secret create huggingface HF_TOKEN=hf_xxx
```

```python
@app.function(secrets=[modal.Secret.from_name("huggingface")])
defdownload_model():
import os
    token = os.environ["HF_TOKEN"]
```

## Scheduling[​](#scheduling "Direct link to Scheduling")

```python
@app.function(schedule=modal.Cron("0 0 * * *"))# Daily midnight
defdaily_job():
pass

@app.function(schedule=modal.Period(hours=1))
defhourly_job():
pass
```

## Performance optimization[​](#performance-optimization "Direct link to Performance optimization")

### Cold start mitigation[​](#cold-start-mitigation "Direct link to Cold start mitigation")

```python
@app.function(
    container_idle_timeout=300,# Keep warm 5 min
    allow_concurrent_inputs=10,# Handle concurrent requests
)
definference():
pass
```

### Model loading best practices[​](#model-loading-best-practices "Direct link to Model loading best practices")

```python
@app.cls(gpu="A100")
classModel:
@modal.enter()# Run once at container start
defload(self):
        self.model = load_model()# Load during warm-up

@modal.method()
defpredict(self, x):
return self.model(x)
```

## Parallel processing[​](#parallel-processing "Direct link to Parallel processing")

```python
@app.function()
defprocess_item(item):
return expensive_computation(item)

@app.function()
defrun_parallel():
    items =list(range(1000))
# Fan out to parallel containers
    results =list(process_item.map(items))
return results
```

## Common configuration[​](#common-configuration "Direct link to Common configuration")

```python
@app.function(
    gpu="A100",
    memory=32768,# 32GB RAM
    cpu=4,# 4 CPU cores
    timeout=3600,# 1 hour max
    container_idle_timeout=120,# Keep warm 2 min
    retries=3,# Retry on failure
    concurrency_limit=10,# Max concurrent containers
)
defmy_function():
pass
```

## Debugging[​](#debugging "Direct link to Debugging")

```python
# Test locally
if __name__ =="__main__":
    result = my_function.local()

# View logs
# modal app logs my-app
```

## Common issues[​](#common-issues "Direct link to Common issues")

IssueSolutionCold start latencyIncrease `container_idle_timeout`, use `@modal.enter()`GPU OOMUse larger GPU (`A100-80GB`), enable gradient checkpointingImage build failsPin dependency versions, check CUDA compatibilityTimeout errorsIncrease `timeout`, add checkpointing

## References[​](#references "Direct link to References")

- [**Advanced Usage**](https://github.com/NousResearch/hermes-agent/blob/main/optional-skills/mlops/modal/references/advanced-usage.md) - Multi-GPU, distributed training, cost optimization
- [**Troubleshooting**](https://github.com/NousResearch/hermes-agent/blob/main/optional-skills/mlops/modal/references/troubleshooting.md) - Common issues and solutions

## Resources[​](#resources "Direct link to Resources")

- **Documentation**: [https://modal.com/docs](https://modal.com/docs)
- **Examples**: [https://github.com/modal-labs/modal-examples](https://github.com/modal-labs/modal-examples)
- **Pricing**: [https://modal.com/pricing](https://modal.com/pricing)
- **Discord**: [https://discord.gg/modal](https://discord.gg/modal)