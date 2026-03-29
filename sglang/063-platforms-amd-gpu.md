---
title: AMD GPUs — SGLang
url: https://docs.sglang.io/platforms/amd_gpu.html
source: crawler
fetched_at: 2026-02-04T08:47:09.517821048-03:00
rendered_js: false
word_count: 415
summary: This document provides instructions for configuring, installing, and running SGLang on AMD GPUs, specifically targeting MI300X hardware. It covers system-level optimizations, ROCm-specific installation methods, and deployment examples for large language models.
tags:
    - amd-gpu
    - rocm
    - mi300x
    - sglang
    - installation-guide
    - system-optimization
    - docker-deployment
category: guide
---

## Contents

## AMD GPUs[#](#amd-gpus "Link to this heading")

This document describes how run SGLang on AMD GPUs. If you encounter issues or have questions, please [open an issue](https://github.com/sgl-project/sglang/issues).

## System Configuration[#](#system-configuration "Link to this heading")

When using AMD GPUs (such as MI300X), certain system-level optimizations help ensure stable performance. Here we take MI300X as an example. AMD provides official documentation for MI300X optimization and system tuning:

- [AMD MI300X Tuning Guides](https://rocm.docs.amd.com/en/latest/how-to/tuning-guides/mi300x/index.html)
- [LLM inference performance validation on AMD Instinct MI300X](https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/vllm-benchmark.html)
- [AMD Instinct MI300X System Optimization](https://rocm.docs.amd.com/en/latest/how-to/system-optimization/mi300x.html)
- [AMD Instinct MI300X Workload Optimization](https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference-optimization/workload.html)
- [Supercharge DeepSeek-R1 Inference on AMD Instinct MI300X](https://rocm.blogs.amd.com/artificial-intelligence/DeepSeekR1-Part2/README.html)

**NOTE:** We strongly recommend reading these docs and guides entirely to fully utilize your system.

Below are a few key settings to confirm or enable for SGLang:

### Update GRUB Settings[#](#update-grub-settings "Link to this heading")

In `/etc/default/grub`, append the following to `GRUB_CMDLINE_LINUX`:

Afterward, run `sudo update-grub` (or your distro’s equivalent) and reboot.

### Disable NUMA Auto-Balancing[#](#disable-numa-auto-balancing "Link to this heading")

```
sudosh-c'echo 0 > /proc/sys/kernel/numa_balancing'
```

You can automate or verify this change using [this helpful script](https://github.com/ROCm/triton/blob/rocm_env/scripts/amd/env_check.sh).

Again, please go through the entire documentation to confirm your system is using the recommended configuration.

## Install SGLang[#](#install-sglang "Link to this heading")

You can install SGLang using one of the methods below.

### Install from Source[#](#install-from-source "Link to this heading")

```
# Use the last release branch
gitclone-bv0.5.6.post2https://github.com/sgl-project/sglang.git
cdsglang

# Compile sgl-kernel
pipinstall--upgradepip
cdsgl-kernel
pythonsetup_rocm.pyinstall

# Install sglang python package along with diffusion support
cd..
rm-rfpython/pyproject.toml&&mvpython/pyproject_other.tomlpython/pyproject.toml
pipinstall-e"python[all_hip]"
```

### Install Using Docker (Recommended)[#](#install-using-docker-recommended "Link to this heading")

The docker images are available on Docker Hub at [lmsysorg/sglang](https://hub.docker.com/r/lmsysorg/sglang/tags), built from [rocm.Dockerfile](https://github.com/sgl-project/sglang/tree/main/docker).

The steps below show how to build and use an image.

1. Build the docker image. If you use pre-built images, you can skip this step and replace `sglang_image` with the pre-built image names in the steps below.
   
   ```
   dockerbuild-tsglang_image-frocm.Dockerfile.
   ```
2. Create a convenient alias.
   
   ```
   aliasdrun='docker run -it --rm --network=host --privileged --device=/dev/kfd --device=/dev/dri \
       --ipc=host --shm-size 16G --group-add video --cap-add=SYS_PTRACE \
       --security-opt seccomp=unconfined \
       -v $HOME/dockerx:/dockerx \
       -v /data:/data'
   ```
   
   If you are using RDMA, please note that:
   
   - `--network host` and `--privileged` are required by RDMA. If you don’t need RDMA, you can remove them.
   - You may need to set `NCCL_IB_GID_INDEX` if you are using RoCE, for example: `export NCCL_IB_GID_INDEX=3`.
3. Launch the server.
   
   **NOTE:** Replace `<secret>` below with your [huggingface hub token](https://huggingface.co/docs/hub/en/security-tokens).
   
   ```
   drun-p30000:30000\
   -v~/.cache/huggingface:/root/.cache/huggingface\
   --env"HF_TOKEN=<secret>"\
   sglang_image\
   python3-msglang.launch_server\
   --model-pathNousResearch/Meta-Llama-3.1-8B\
   --host0.0.0.0\
   --port30000
   ```
4. To verify the utility, you can run a benchmark in another terminal or refer to [other docs](https://docs.sglang.io/basic_usage/openai_api_completions.html) to send requests to the engine.
   
   ```
   drunsglang_image\
   python3-msglang.bench_serving\
   --backendsglang\
   --dataset-namerandom\
   --num-prompts4000\
   --random-input128\
   --random-output128
   ```

With your AMD system properly configured and SGLang installed, you can now fully leverage AMD hardware to power SGLang’s machine learning capabilities.

## Examples[#](#examples "Link to this heading")

### Running DeepSeek-V3[#](#running-deepseek-v3 "Link to this heading")

The only difference when running DeepSeek-V3 is in how you start the server. Here’s an example command:

```
drun-p30000:30000\
-v~/.cache/huggingface:/root/.cache/huggingface\
--ipc=host\
--env"HF_TOKEN=<secret>"\
sglang_image\
python3-msglang.launch_server\
--model-pathdeepseek-ai/DeepSeek-V3\ # <- here
--tp8\
--trust-remote-code\
--host0.0.0.0\
--port30000
```

[Running DeepSeek-R1 on a single NDv5 MI300X VM](https://techcommunity.microsoft.com/blog/azurehighperformancecomputingblog/running-deepseek-r1-on-a-single-ndv5-mi300x-vm/4372726) could also be a good reference.

### Running Llama3.1[#](#running-llama3-1 "Link to this heading")

Running Llama3.1 is nearly identical to running DeepSeek-V3. The only difference is in the model specified when starting the server, shown by the following example command:

```
drun-p30000:30000\
-v~/.cache/huggingface:/root/.cache/huggingface\
--ipc=host\
--env"HF_TOKEN=<secret>"\
sglang_image\
python3-msglang.launch_server\
--model-pathmeta-llama/Meta-Llama-3.1-8B-Instruct\ # <- here
--tp8\
--trust-remote-code\
--host0.0.0.0\
--port30000
```

### Warmup Step[#](#warmup-step "Link to this heading")

When the server displays `The server is fired up and ready to roll!`, it means the startup is successful.