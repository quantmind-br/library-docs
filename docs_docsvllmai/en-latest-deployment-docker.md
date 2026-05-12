---
title: Using Docker - vLLM
url: https://docs.vllm.ai/en/latest/deployment/docker/
source: sitemap
fetched_at: 2026-05-07T21:11:32.855710781-03:00
rendered_js: false
word_count: 1344
summary: This document provides instructions for deploying vLLM using official pre-built Docker images across various hardware platforms and explains how to build custom images from source.
tags:
    - docker
    - containerization
    - deployment
    - nvidia-cuda
    - amd-rocm
    - intel-xpu
    - build-from-source
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/deployment/docker.md "Edit this page")

## Pre-built images[¶](#pre-built-images "Permanent link")

NVIDIA CUDAAMD ROCmIntel XPU

vLLM offers an official Docker image for deployment. The image can be used to run OpenAI compatible server and is available on Docker Hub as [vllm/vllm-openai](https://hub.docker.com/r/vllm/vllm-openai/tags).

```
dockerrun--runtimenvidia--gpusall\
-v~/.cache/huggingface:/root/.cache/huggingface\
--env"HF_TOKEN=$HF_TOKEN"\
-p8000:8000\
--ipc=host\
vllm/vllm-openai:latest\
--modelQwen/Qwen3-0.6B
```

This image can also be used with other container engines such as [Podman](https://podman.io/).

```
podmanrun--devicenvidia.com/gpu=all\
-v~/.cache/huggingface:/root/.cache/huggingface\
--env"HF_TOKEN=$HF_TOKEN"\
-p8000:8000\
--ipc=host\
docker.io/vllm/vllm-openai:latest\
--modelQwen/Qwen3-0.6B
```

You can add any other [engine-args](https://docs.vllm.ai/en/latest/configuration/engine_args/) you need after the image tag (`vllm/vllm-openai:latest`).

Note

You can either use the `ipc=host` flag or `--shm-size` flag to allow the container to access the host's shared memory. vLLM uses PyTorch, which uses shared memory to share data between processes under the hood, particularly for tensor parallel inference.

Note

Optional dependencies are not included in order to avoid licensing issues (e.g. [Issue #8030](https://github.com/vllm-project/vllm/issues/8030)).

If you need to use those dependencies (having accepted the license terms), create a custom Dockerfile on top of the base image with an extra layer that installs them:

```
FROMvllm/vllm-openai:v0.11.0

# e.g. install the `audio` optional dependencies
# NOTE: Make sure the version of vLLM matches the base image!
RUNuvpipinstall--systemvllm[audio]==0.11.0
```

Tip

Some new models may only be available on the main branch of [HF Transformers](https://github.com/huggingface/transformers).

To use the development version of `transformers`, create a custom Dockerfile on top of the base image with an extra layer that installs their code from source:

```
FROMvllm/vllm-openai:latest

RUNuvpipinstall--systemgit+https://github.com/huggingface/transformers.git
```

#### Running on Systems with Older CUDA Drivers[¶](#running-on-systems-with-older-cuda-drivers "Permanent link")

vLLM's Docker image comes with [CUDA compatibility libraries](https://docs.nvidia.com/deploy/cuda-compatibility/index.html) pre-installed. This allows you to run vLLM on systems with NVIDIA drivers that are older than the CUDA Toolkit version used in the image, but only supports select professional and datacenter NVIDIA GPUs.

To enable this feature, set the `VLLM_ENABLE_CUDA_COMPATIBILITY` environment variable to `1` or `true` when running the container:

```
dockerrun--runtimenvidia--gpusall\
-v~/.cache/huggingface:/root/.cache/huggingface\
-p8000:8000\
--env"HF_TOKEN=<secret>"\
--env"VLLM_ENABLE_CUDA_COMPATIBILITY=1"\
vllm/vllm-openai<args...>
```

This will automatically configure `LD_LIBRARY_PATH` to point to the compatibility libraries before loading PyTorch and other dependencies.

vLLM offers official Docker images for deployment. The images can be used to run OpenAI compatible server and are available on Docker Hub as [vllm/vllm-openai-rocm](https://hub.docker.com/r/vllm/vllm-openai-rocm/tags).

- `vllm/vllm-openai-rocm:latest` — stable release
- `vllm/vllm-openai-rocm:nightly` — preview build from the latest development branch, use this if you want the latest features and fixes

```
dockerrun--rm\
--group-add=video\
--cap-add=SYS_PTRACE\
--security-optseccomp=unconfined\
--device/dev/kfd\
--device/dev/dri\
-v~/.cache/huggingface:/root/.cache/huggingface\
--env"HF_TOKEN=$HF_TOKEN"\
-p8000:8000\
--ipc=host\
vllm/vllm-openai-rocm:<tag>\
--modelQwen/Qwen3-0.6B
```

To use the docker image as base for development, you can launch it in interactive session through overriding the entrypoint.

Commands

```
dockerrun--rm-it\
--group-add=video\
--cap-add=SYS_PTRACE\
--security-optseccomp=unconfined\
--device/dev/kfd\
--device/dev/dri\
-v~/.cache/huggingface:/root/.cache/huggingface\
--env"HF_TOKEN=$HF_TOKEN"\
--network=host\
--ipc=host\
--entrypoint/bin/bash\
vllm/vllm-openai-rocm:<tag>
```

#### Use AMD's Docker Images (Deprecated)[¶](#use-amds-docker-images-deprecated "Permanent link")

Deprecated

AMD's Docker images (`rocm/vllm` and `rocm/vllm-dev`) are deprecated in favor of the official vLLM Docker images above (`vllm/vllm-openai-rocm`). Please migrate to the official images.

Prior to January 20th, 2026 when the official docker images became available on [upstream vLLM docker hub](https://hub.docker.com/v2/repositories/vllm/vllm-openai-rocm/tags/), the [AMD Infinity hub for vLLM](https://hub.docker.com/r/rocm/vllm/tags) offered a prebuilt, optimized docker image designed for validating inference performance on the AMD Instinct MI300X™ accelerator. AMD also offered nightly prebuilt docker image from [Docker Hub](https://hub.docker.com/r/rocm/vllm-dev), which has vLLM and all its dependencies installed. The entrypoint of this docker image is `/bin/bash` (different from the vLLM's Official Docker Image).

Currently, we release prebuilt XPU images at docker [hub](https://hub.docker.com/r/intel/vllm/tags) based on vLLM released version. For more information, please refer release [note](https://github.com/intel/ai-containers/blob/main/vllm).

## Build image from source[¶](#build-image-from-source "Permanent link")

NVIDIA CUDAAMD ROCmIntel XPU

You can build and run vLLM from source via the provided [docker/Dockerfile](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile). To build vLLM:

```
# optionally specifies: --build-arg max_jobs=8 --build-arg nvcc_threads=2
DOCKER_BUILDKIT=1dockerbuild.\
--targetvllm-openai\
--tagvllm/vllm-openai\
--filedocker/Dockerfile
```

Note

By default vLLM will build for all GPU types for widest distribution. If you are just building for the current GPU type the machine is running on, you can add the argument `--build-arg torch_cuda_arch_list=""` for vLLM to find the current GPU type and build for that.

If you are using Podman instead of Docker, you might need to disable SELinux labeling by adding `--security-opt label=disable` when running `podman build` command to avoid certain [existing issues](https://github.com/containers/buildah/discussions/4184).

Note

If you have not changed any C++ or CUDA kernel code, you can use precompiled wheels to significantly reduce Docker build time.

- **Enable the feature** by adding the build argument: `--build-arg VLLM_USE_PRECOMPILED="1"`.
- **How it works**: By default, vLLM automatically finds the correct wheels from our [Nightly Builds](https://docs.vllm.ai/en/latest/contributing/ci/nightly_builds/) by using the merge-base commit with the upstream `main` branch.
- **Override commit**: To use wheels from a specific commit, provide the `--build-arg VLLM_PRECOMPILED_WHEEL_COMMIT=<commit_hash>` argument.

For a detailed explanation, refer to the documentation on 'Set up using Python-only build (without compilation)' part in [Build wheel from source](https://docs.vllm.ai/en/latest/contributing/ci/nightly_builds/#precompiled-wheels-usage), these args are similar.

#### Building vLLM's Docker Image from Source for Arm64/aarch64[¶](#building-vllms-docker-image-from-source-for-arm64aarch64 "Permanent link")

A docker container can be built for aarch64 systems such as the Nvidia Grace-Hopper and Grace-Blackwell. Using the flag `--platform "linux/arm64"` will build for arm64.

Note

Multiple modules must be compiled, so this process can take a while. Recommend using `--build-arg max_jobs=` & `--build-arg nvcc_threads=` flags to speed up build process. However, ensure your `max_jobs` is substantially larger than `nvcc_threads` to get the most benefits. Keep an eye on memory usage with parallel jobs as it can be substantial (see example below).

Command

```
# Example of building on Nvidia GH200 server. (Memory usage: ~15GB, Build time: ~1475s / ~25 min, Image size: 6.93GB)
DOCKER_BUILDKIT=1dockerbuild.\
--filedocker/Dockerfile\
--targetvllm-openai\
--platform"linux/arm64"\
-tvllm/vllm-gh200-openai:latest\
--build-argmax_jobs=66\
--build-argnvcc_threads=2\
--build-argtorch_cuda_arch_list="9.0 10.0+PTX"\
--build-argRUN_WHEEL_CHECK=false
```

For (G)B300, we recommend using CUDA 13, as shown in the following command.

Command

```
DOCKER_BUILDKIT=1dockerbuild\
--build-argCUDA_VERSION=13.0.2\
--build-argBUILD_BASE_IMAGE=nvidia/cuda:13.0.2-devel-ubuntu22.04\
--build-argmax_jobs=256\
--build-argnvcc_threads=2\
--build-argRUN_WHEEL_CHECK=false\
--build-argtorch_cuda_arch_list='9.0 10.0+PTX'\
--platform"linux/arm64"\
--tagvllm/vllm-gb300-openai:latest\
--targetvllm-openai\
-fdocker/Dockerfile\
.
```

Note

If you are building the `linux/arm64` image on a non-ARM host (e.g., an x86\_64 machine), you need to ensure your system is set up for cross-compilation using QEMU. This allows your host machine to emulate ARM64 execution.

Run the following command on your host machine to register QEMU user static handlers:

```
dockerrun--rm--privilegedmultiarch/qemu-user-static--reset-pyes
```

After setting up QEMU, you can use the `--platform "linux/arm64"` flag in your `docker build` command.

#### Use the custom-built vLLM Docker image\*\*[¶](#use-the-custom-built-vllm-docker-image "Permanent link")

To run vLLM with the custom-built Docker image:

```
dockerrun--runtimenvidia--gpusall\
-v~/.cache/huggingface:/root/.cache/huggingface\
-p8000:8000\
--env"HF_TOKEN=<secret>"\
vllm/vllm-openai<args...>
```

The argument `vllm/vllm-openai` specifies the image to run, and should be replaced with the name of the custom-built image (the `-t` tag from the build command).

Note

**For version 0.4.1 and 0.4.2 only** - the vLLM docker images under these versions are supposed to be run under the root user since a library under the root user's home directory, i.e. `/root/.config/vllm/nccl/cu12/libnccl.so.2.18.1` is required to be loaded during runtime. If you are running the container under a different user, you may need to first change the permissions of the library (and all the parent directories) to allow the user to access it, then run vLLM with environment variable `VLLM_NCCL_SO_PATH=/root/.config/vllm/nccl/cu12/libnccl.so.2.18.1` .

You can build and run vLLM from source via the provided [docker/Dockerfile.rocm](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm).

(Optional) Build an image with ROCm software stack

Build a docker image from [docker/Dockerfile.rocm\_base](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm_base) which setup ROCm software stack needed by the vLLM. **This step is optional as this rocm\_base image is usually prebuilt and store at [Docker Hub](https://hub.docker.com/r/rocm/vllm-dev) under tag `rocm/vllm-dev:base` to speed up user experience.** If you choose to build this rocm\_base image yourself, the steps are as follows.

It is important that the user kicks off the docker build using buildkit. Either the user put `DOCKER_BUILDKIT=1` as environment variable when calling docker build command, or the user needs to set up buildkit in the docker daemon configuration `/etc/docker/daemon.json` as follows and restart the daemon:

```
{
"features":{
"buildkit":true
}
}
```

To build vllm on ROCm 7.0 for MI200 and MI300 series, you can use the default:

```
DOCKER_BUILDKIT=1dockerbuild\
-fdocker/Dockerfile.rocm_base\
-trocm/vllm-dev:base.
```

First, build a docker image from [docker/Dockerfile.rocm](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm) and launch a docker container from the image. It is important that the user kicks off the docker build using buildkit. Either the user put `DOCKER_BUILDKIT=1` as environment variable when calling docker build command, or the user needs to set up buildkit in the docker daemon configuration /etc/docker/daemon.json as follows and restart the daemon:

```
{
"features":{
"buildkit":true
}
}
```

[docker/Dockerfile.rocm](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm) uses ROCm 7.0 by default, but also supports ROCm 5.7, 6.0, 6.1, 6.2, 6.3, and 6.4, in older vLLM branches. It provides flexibility to customize the build of docker image using the following arguments:

- `BASE_IMAGE`: specifies the base image used when running `docker build`. The default value `rocm/vllm-dev:base` is an image published and maintained by AMD. It is being built using [docker/Dockerfile.rocm\_base](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm_base)
- `ARG_PYTORCH_ROCM_ARCH`: Allows to override the gfx architecture values from the base docker image

Their values can be passed in when running `docker build` with `--build-arg` options.

To build vllm on ROCm 7.0 for MI200 and MI300 series, you can use the default (which build a docker image with `vllm serve` as entrypoint):

```
DOCKER_BUILDKIT=1dockerbuild-fdocker/Dockerfile.rocm-tvllm/vllm-openai-rocm.
```

To run vLLM with the custom-built Docker image:

```
dockerrun--rm\
--group-add=video\
--cap-add=SYS_PTRACE\
--security-optseccomp=unconfined\
--device/dev/kfd\
--device/dev/dri\
-v~/.cache/huggingface:/root/.cache/huggingface\
--env"HF_TOKEN=$HF_TOKEN"\
-p8000:8000\
--ipc=host\
vllm/vllm-openai-rocm<args...>
```

The argument `vllm/vllm-openai-rocm` specifies the image to run, and should be replaced with the name of the custom-built image (the `-t` tag from the build command).

To use the docker image as base for development, you can launch it in interactive session through overriding the entrypoint.

Commands

```
dockerrun--rm-it\
--group-add=video\
--cap-add=SYS_PTRACE\
--security-optseccomp=unconfined\
--device/dev/kfd\
--device/dev/dri\
-v~/.cache/huggingface:/root/.cache/huggingface\
--env"HF_TOKEN=$HF_TOKEN"\
--network=host\
--ipc=host\
--entrypointbash\
vllm/vllm-openai-rocm

dockerbuild-fdocker/Dockerfile.xpu-tvllm-xpu-env--shm-size=4g.
dockerrun-it\
--rm\
--network=host\
--device/dev/dri:/dev/dri\
-v/dev/dri/by-path:/dev/dri/by-path\
--ipc=host\
--privileged\
vllm-xpu-env
```