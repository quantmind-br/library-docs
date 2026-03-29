---
title: Install SGLang — SGLang
url: https://docs.sglang.io/get_started/install.html
source: crawler
fetched_at: 2026-02-04T08:46:40.483946365-03:00
rendered_js: false
word_count: 810
summary: This document provides comprehensive instructions for installing and deploying the SGLang library using various methods including pip, Docker, Kubernetes, and cloud platforms.
tags:
    - sglang-installation
    - docker-deployment
    - kubernetes-setup
    - gpu-computing
    - python-package
    - cloud-infrastructure
category: guide
---

## Contents

## Install SGLang[#](#install-sglang "Link to this heading")

You can install SGLang using one of the methods below. This page primarily applies to common NVIDIA GPU platforms. For other or newer platforms, please refer to the dedicated pages for [AMD GPUs](https://docs.sglang.io/platforms/amd_gpu.html), [Intel Xeon CPUs](https://docs.sglang.io/platforms/cpu_server.html), [TPU](https://docs.sglang.io/platforms/tpu.html), [NVIDIA DGX Spark](https://lmsys.org/blog/2025-11-03-gpt-oss-on-nvidia-dgx-spark/), [NVIDIA Jetson](https://docs.sglang.io/platforms/nvidia_jetson.html), [Ascend NPUs](https://docs.sglang.io/platforms/ascend_npu.html), and [Intel XPU](https://docs.sglang.io/platforms/xpu.html).

## Method 1: With pip or uv[#](#method-1-with-pip-or-uv "Link to this heading")

It is recommended to use uv for faster installation:

```
pipinstall--upgradepip
pipinstalluv
uvpipinstall"sglang"
```

**Quick fixes to common problems**

- For CUDA 13, Docker is recommended (see Method 3 note on B300/GB300/CUDA 13). If you do not have Docker access, an extra index url needs to be provided when installing wheels:

```
uv pip install "sglang" --extra-index-url https://download.pytorch.org/whl/cu130
```

- The `sgl_kernel` wheel for CUDA 13 can be downloaded from [the sgl-project whl releases](https://github.com/sgl-project/whl/blob/gh-pages/cu130/sgl-kernel/index.html). Replace `X.Y.Z` with the `sgl_kernel` version required by your SGLang install (you can find this by running `uv pip show sgl_kernel`). Examples:
  
  ```
  # x86_64
  uvpipinstall"https://github.com/sgl-project/whl/releases/download/vX.Y.Z/sgl_kernel-X.Y.Z+cu130-cp310-abi3-manylinux2014_x86_64.whl"
  
  # aarch64
  uvpipinstall"https://github.com/sgl-project/whl/releases/download/vX.Y.Z/sgl_kernel-X.Y.Z+cu130-cp310-abi3-manylinux2014_aarch64.whl"
  ```
- If you encounter `OSError: CUDA_HOME environment variable is not set`. Please set it to your CUDA install root with either of the following solutions:
  
  1. Use `export CUDA_HOME=/usr/local/cuda-<your-cuda-version>` to set the `CUDA_HOME` environment variable.
  2. Install FlashInfer first following [FlashInfer installation doc](https://docs.flashinfer.ai/installation.html), then install SGLang as described above.

## Method 2: From source[#](#method-2-from-source "Link to this heading")

```
# Use the last release branch
gitclone-bv0.5.6.post2https://github.com/sgl-project/sglang.git
cdsglang

# Install the python packages
pipinstall--upgradepip
pipinstall-e"python"
```

**Quick fixes to common problems**

- If you want to develop SGLang, you can try the dev docker image. Please refer to [setup docker container](https://docs.sglang.io/developer_guide/development_guide_using_docker.html#setup-docker-container). The docker image is `lmsysorg/sglang:dev`.

## Method 3: Using docker[#](#method-3-using-docker "Link to this heading")

The docker images are available on Docker Hub at [lmsysorg/sglang](https://hub.docker.com/r/lmsysorg/sglang/tags), built from [Dockerfile](https://github.com/sgl-project/sglang/tree/main/docker). Replace `<secret>` below with your huggingface hub [token](https://huggingface.co/docs/hub/en/security-tokens).

```
dockerrun--gpusall\
--shm-size32g\
-p30000:30000\
-v~/.cache/huggingface:/root/.cache/huggingface\
--env"HF_TOKEN=<secret>"\
--ipc=host\
lmsysorg/sglang:latest\
python3-msglang.launch_server--model-pathmeta-llama/Llama-3.1-8B-Instruct--host0.0.0.0--port30000
```

For production deployments, use the `runtime` variant which is significantly smaller (~40% reduction) by excluding build tools and development dependencies:

```
dockerrun--gpusall\
--shm-size32g\
-p30000:30000\
-v~/.cache/huggingface:/root/.cache/huggingface\
--env"HF_TOKEN=<secret>"\
--ipc=host\
lmsysorg/sglang:latest-runtime\
python3-msglang.launch_server--model-pathmeta-llama/Llama-3.1-8B-Instruct--host0.0.0.0--port30000
```

You can also find the nightly docker images [here](https://hub.docker.com/r/lmsysorg/sglang/tags?name=nightly).

Notes:

- On B300/GB300 (SM103) or CUDA 13 environment, we recommend using the nightly image at `lmsysorg/sglang:dev-cu13` or stable image at `lmsysorg/sglang:latest-cu130-runtime`. Please, do not re-install the project as editable inside the docker image, since it will override the version of libraries specified by the cu13 docker image.

## Method 4: Using Kubernetes[#](#method-4-using-kubernetes "Link to this heading")

Please check out [OME](https://github.com/sgl-project/ome), a Kubernetes operator for enterprise-grade management and serving of large language models (LLMs).

More

1. Option 1: For single node serving (typically when the model size fits into GPUs on one node)
   
   Execute command `kubectl apply -f docker/k8s-sglang-service.yaml`, to create k8s deployment and service, with llama-31-8b as example.
2. Option 2: For multi-node serving (usually when a large model requires more than one GPU node, such as `DeepSeek-R1`)
   
   Modify the LLM model path and arguments as necessary, then execute command `kubectl apply -f docker/k8s-sglang-distributed-sts.yaml`, to create two nodes k8s statefulset and serving service.

## Method 5: Using docker compose[#](#method-5-using-docker-compose "Link to this heading")

More

> This method is recommended if you plan to serve it as a service. A better approach is to use the [k8s-sglang-service.yaml](https://github.com/sgl-project/sglang/blob/main/docker/k8s-sglang-service.yaml).

1. Copy the [compose.yml](https://github.com/sgl-project/sglang/blob/main/docker/compose.yaml) to your local machine
2. Execute the command `docker compose up -d` in your terminal.

## Method 6: Run on Kubernetes or Clouds with SkyPilot[#](#method-6-run-on-kubernetes-or-clouds-with-skypilot "Link to this heading")

More

To deploy on Kubernetes or 12+ clouds, you can use [SkyPilot](https://github.com/skypilot-org/skypilot).

1. Install SkyPilot and set up Kubernetes cluster or cloud access: see [SkyPilot’s documentation](https://skypilot.readthedocs.io/en/latest/getting-started/installation.html).
2. Deploy on your own infra with a single command and get the HTTP API endpoint:

SkyPilot YAML: `sglang.yaml`

```
# sglang.yaml
envs:
HF_TOKEN:null

resources:
image_id:docker:lmsysorg/sglang:latest
accelerators:A100
ports:30000

run:|
conda deactivate
python3 -m sglang.launch_server \
--model-path meta-llama/Llama-3.1-8B-Instruct \
--host 0.0.0.0 \
--port 30000
```

```
# Deploy on any cloud or Kubernetes cluster. Use --cloud <cloud> to select a specific cloud provider.
HF_TOKEN=<secret>skylaunch-csglang--envHF_TOKENsglang.yaml

# Get the HTTP API endpoint
skystatus--endpoint30000sglang
```

3. To further scale up your deployment with autoscaling and failure recovery, check out the [SkyServe + SGLang guide](https://github.com/skypilot-org/skypilot/tree/master/llm/sglang#serving-llama-2-with-sglang-for-more-traffic-using-skyserve).

## Method 7: Run on AWS SageMaker[#](#method-7-run-on-aws-sagemaker "Link to this heading")

More

To deploy on SGLang on AWS SageMaker, check out [AWS SageMaker Inference](https://aws.amazon.com/sagemaker/ai/deploy)

Amazon Web Services provide supports for SGLang containers along with routine security patching. For available SGLang containers, check out [AWS SGLang DLCs](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sglang-containers)

To host a model with your own container, follow the following steps:

1. Build a docker container with [sagemaker.Dockerfile](https://github.com/sgl-project/sglang/blob/main/docker/sagemaker.Dockerfile) alongside the [serve](https://github.com/sgl-project/sglang/blob/main/docker/serve) script.
2. Push your container onto AWS ECR.

Dockerfile Build Script: `build-and-push.sh`

```
#!/bin/bash
AWS_ACCOUNT="<YOUR_AWS_ACCOUNT>"
AWS_REGION="<YOUR_AWS_REGION>"
REPOSITORY_NAME="<YOUR_REPOSITORY_NAME>"
IMAGE_TAG="<YOUR_IMAGE_TAG>"

ECR_REGISTRY="${AWS_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com"
IMAGE_URI="${ECR_REGISTRY}/${REPOSITORY_NAME}:${IMAGE_TAG}"

echo"Starting build and push process..."

# Login to ECR
echo"Logging into ECR..."
awsecrget-login-password--region${AWS_REGION}|dockerlogin--usernameAWS--password-stdin${ECR_REGISTRY}

# Build the image
echo"Building Docker image..."
dockerbuild-t${IMAGE_URI}-fsagemaker.Dockerfile.

echo"Pushing ${IMAGE_URI}"
dockerpush${IMAGE_URI}

echo"Build and push completed successfully!"
```

3. Deploy a model for serving on AWS Sagemaker, refer to [deploy\_and\_serve\_endpoint.py](https://github.com/sgl-project/sglang/blob/main/examples/sagemaker/deploy_and_serve_endpoint.py). For more information, check out [sagemaker-python-sdk](https://github.com/aws/sagemaker-python-sdk).
   
   1. By default, the model server on SageMaker will run with the following command: `python3 -m sglang.launch_server --model-path opt/ml/model --host 0.0.0.0 --port 8080`. This is optimal for hosting your own model with SageMaker.
   2. To modify your model serving parameters, the [serve](https://github.com/sgl-project/sglang/blob/main/docker/serve) script allows for all available options within `python3 -m sglang.launch_server --help` cli by specifying environment variables with prefix `SM_SGLANG_`.
   3. The serve script will automatically convert all environment variables with prefix `SM_SGLANG_` from `SM_SGLANG_INPUT_ARGUMENT` into `--input-argument` to be parsed into `python3 -m sglang.launch_server` cli.
   4. For example, to run [Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) with reasoning parser, simply add additional environment variables `SM_SGLANG_MODEL_PATH=Qwen/Qwen3-0.6B` and `SM_SGLANG_REASONING_PARSER=qwen3`.

## Common Notes[#](#common-notes "Link to this heading")

- [FlashInfer](https://github.com/flashinfer-ai/flashinfer) is the default attention kernel backend. It only supports sm75 and above. If you encounter any FlashInfer-related issues on sm75+ devices (e.g., T4, A10, A100, L4, L40S, H100), please switch to other kernels by adding `--attention-backend triton --sampling-backend pytorch` and open an issue on GitHub.
- To reinstall flashinfer locally, use the following command: `pip3 install --upgrade flashinfer-python --force-reinstall --no-deps` and then delete the cache with `rm -rf ~/.cache/flashinfer`.
- When encountering `ptxas fatal   : Value 'sm_103a' is not defined for option 'gpu-name'` on B300/GB300, fix it with `export TRITON_PTXAS_PATH=/usr/local/cuda/bin/ptxas`.