---
title: SGLang installation with NPUs support — SGLang
url: https://docs.sglang.io/platforms/ascend_npu.html
source: crawler
fetched_at: 2026-02-04T08:47:32.894203013-03:00
rendered_js: false
word_count: 390
summary: This document provides instructions for installing and configuring SGLang with Ascend NPU support, covering prerequisite setup, source and Docker installation methods, and system performance optimizations.
tags:
    - sglang
    - ascend-npu
    - cann
    - installation-guide
    - docker
    - performance-optimization
category: guide
---

## Contents

## SGLang installation with NPUs support[#](#sglang-installation-with-npus-support "Link to this heading")

You can install SGLang using any of the methods below. Please go through `System Settings` section to ensure the clusters are roaring at max performance. Feel free to leave an issue [here at sglang](https://github.com/sgl-project/sglang/issues) if you encounter any issues or have any problems.

## Component Version Mapping For SGLang[#](#component-version-mapping-for-sglang "Link to this heading")

### Obtain CANN Image[#](#obtain-cann-image "Link to this heading")

You can obtain the dependency of a specified version of CANN through an image.

```
# for Atlas 800I A3 and Ubuntu OS
dockerpullquay.io/ascend/cann:8.5.0-a3-ubuntu22.04-py3.11
# for Atlas 800I A2 and Ubuntu OS
dockerpullquay.io/ascend/cann:8.5.0-910b-ubuntu22.04-py3.11
```

## Preparing the Running Environment[#](#preparing-the-running-environment "Link to this heading")

### Method 1: Installing from source with prerequisites[#](#method-1-installing-from-source-with-prerequisites "Link to this heading")

#### Python Version[#](#python-version "Link to this heading")

Only `python==3.11` is supported currently. If you don’t want to break system pre-installed python, try installing with [conda](https://github.com/conda/conda).

```
condacreate--namesglang_npupython=3.11
condaactivatesglang_npu
```

#### CANN[#](#cann "Link to this heading")

Prior to start work with SGLang on Ascend you need to install CANN Toolkit, Kernels operator package and NNAL version 8.3.RC2 or higher, check the [installation guide](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/83RC1/softwareinst/instg/instg_0008.html?Mode=PmIns&amp%3BInstallType=local&amp%3BOS=openEuler&amp%3BSoftware=cannToolKit)

#### MemFabric-Hybrid[#](#memfabric-hybrid "Link to this heading")

If you want to use PD disaggregation mode, you need to install MemFabric-Hybrid. MemFabric-Hybrid is a drop-in replacement of Mooncake Transfer Engine that enables KV cache transfer on Ascend NPU clusters.

```
pipinstallmemfabric-hybrid==1.0.5
```

#### Pytorch and Pytorch Framework Adaptor on Ascend[#](#pytorch-and-pytorch-framework-adaptor-on-ascend "Link to this heading")

```
PYTORCH_VERSION=2.8.0
TORCHVISION_VERSION=0.23.0
TORCH_NPU_VERSION=2.8.0
pipinstalltorch==$PYTORCH_VERSIONtorchvision==$TORCHVISION_VERSION--index-urlhttps://download.pytorch.org/whl/cpu
pipinstalltorch_npu==$TORCH_NPU_VERSION
```

If you are using other versions of `torch` and install `torch_npu`, check [installation guide](https://github.com/Ascend/pytorch/blob/master/README.md)

#### Triton on Ascend[#](#triton-on-ascend "Link to this heading")

We provide our own implementation of Triton for Ascend.

```
pipinstalltriton-ascend
```

For installation of Triton on Ascend nightly builds or from sources, follow [installation guide](https://gitcode.com/Ascend/triton-ascend/blob/master/docs/sources/getting-started/installation.md)

#### SGLang Kernels NPU[#](#sglang-kernels-npu "Link to this heading")

We provide SGL kernels for Ascend NPU, check [installation guide](https://github.com/sgl-project/sgl-kernel-npu/blob/main/python/sgl_kernel_npu/README.md).

#### DeepEP-compatible Library[#](#deepep-compatible-library "Link to this heading")

We provide a DeepEP-compatible Library as a drop-in replacement of deepseek-ai’s DeepEP library, check the [installation guide](https://github.com/sgl-project/sgl-kernel-npu/blob/main/python/deep_ep/README.md).

#### Installing SGLang from source[#](#installing-sglang-from-source "Link to this heading")

```
# Use the last release branch
gitclonehttps://github.com/sgl-project/sglang.git
cdsglang
mvpython/pyproject_npu.tomlpython/pyproject.toml
pipinstall-epython[all_npu]
```

### Method 2: Using Docker Image[#](#method-2-using-docker-image "Link to this heading")

#### Obtain Image[#](#obtain-image "Link to this heading")

You can download the SGLang image or build an image based on Dockerfile to obtain the Ascend NPU image.

1. Download SGLang image

```
dockerhub: docker.io/lmsysorg/sglang:$tag
# Main-based tag, change main to specific version like v0.5.6,
# you can get image for specific version
Atlas 800I A3 : {main}-cann8.5.0-a3
Atlas 800I A2: {main}-cann8.5.0-910b
```

2. Build an image based on Dockerfile

```
# Clone the SGLang repository
gitclonehttps://github.com/sgl-project/sglang.git
cdsglang/docker

# Build the docker image
# If there are network errors, please modify the Dockerfile to use offline dependencies or use a proxy
dockerbuild-t<image_name>-fnpu.Dockerfile.
```

#### Create Docker[#](#create-docker "Link to this heading")

**Notice:** `--privileged` and `--network=host` are required by RDMA, which is typically needed by Ascend NPU clusters.

**Notice:** The following docker command is based on Atlas 800I A3 machines. If you are using Atlas 800I A2, make sure only `davinci[0-7]` are mapped into container.

```
aliasdrun='docker run -it --rm --privileged --network=host --ipc=host --shm-size=16g \
    --device=/dev/davinci0 --device=/dev/davinci1 --device=/dev/davinci2 --device=/dev/davinci3 \
    --device=/dev/davinci4 --device=/dev/davinci5 --device=/dev/davinci6 --device=/dev/davinci7 \
    --device=/dev/davinci8 --device=/dev/davinci9 --device=/dev/davinci10 --device=/dev/davinci11 \
    --device=/dev/davinci12 --device=/dev/davinci13 --device=/dev/davinci14 --device=/dev/davinci15 \
    --device=/dev/davinci_manager --device=/dev/hisi_hdc \
    --volume /usr/local/sbin:/usr/local/sbin --volume /usr/local/Ascend/driver:/usr/local/Ascend/driver \
    --volume /usr/local/Ascend/firmware:/usr/local/Ascend/firmware \
    --volume /etc/ascend_install.info:/etc/ascend_install.info \
    --volume /var/queue_schedule:/var/queue_schedule --volume ~/.cache/:/root/.cache/'

# Add HF_TOKEN env for download model by SGLang.
drun--env"HF_TOKEN=<secret>"\
<image_name>\
python3-msglang.launch_server--model-pathmeta-llama/Llama-3.1-8B-Instruct--attention-backendascend
```

## System Settings[#](#system-settings "Link to this heading")

### CPU performance power scheme[#](#cpu-performance-power-scheme "Link to this heading")

The default power scheme on Ascend hardware is `ondemand` which could affect performance, changing it to `performance` is recommended.

```
echoperformance|sudotee/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

# Make sure changes are applied successfully
cat/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor# shows performance
```

### Disable NUMA balancing[#](#disable-numa-balancing "Link to this heading")

```
sudosysctl-wkernel.numa_balancing=0
# Check
cat/proc/sys/kernel/numa_balancing# shows 0
```

### Prevent swapping out system memory[#](#prevent-swapping-out-system-memory "Link to this heading")

```
sudosysctl-wvm.swappiness=10

# Check
cat/proc/sys/vm/swappiness# shows 10
```

## Running SGLang Service[#](#running-sglang-service "Link to this heading")

### Running Service For Large Language Models[#](#running-service-for-large-language-models "Link to this heading")

#### PD Mixed Scene[#](#pd-mixed-scene "Link to this heading")

```
# Enabling CPU Affinity
exportSGLANG_SET_CPU_AFFINITY=1
python3-msglang.launch_server--model-pathmeta-llama/Llama-3.1-8B-Instruct--attention-backendascend
```

#### PD Separation Scene[#](#pd-separation-scene "Link to this heading")

1. Launch Prefill Server

```
# Enabling CPU Affinity
exportSGLANG_SET_CPU_AFFINITY=1

# PIP: recommended to config first Prefill Server IP
# PORT: one free port
# all sglang servers need to be config the same PIP and PORT,
exportASCEND_MF_STORE_URL="tcp://PIP:PORT"
# if you are Atlas 800I A2 hardware and use rdma for kv cache transfer, add this parameter
exportASCEND_MF_TRANSFER_PROTOCOL="device_rdma"
python3-msglang.launch_server\
--model-pathmeta-llama/Llama-3.1-8B-Instruct\
--disaggregation-modeprefill\
--disaggregation-transfer-backendascend\
--disaggregation-bootstrap-port8995\
--attention-backendascend\
--devicenpu\
--base-gpu-id0\
--tp-size1\
--host127.0.0.1\
--port8000
```

2. Launch Decode Server

```
# PIP: recommended to config first Prefill Server IP
# PORT: one free port
# all sglang servers need to be config the same PIP and PORT,
exportASCEND_MF_STORE_URL="tcp://PIP:PORT"
# if you are Atlas 800I A2 hardware and use rdma for kv cache transfer, add this parameter
exportASCEND_MF_TRANSFER_PROTOCOL="device_rdma"
python3-msglang.launch_server\
--model-pathmeta-llama/Llama-3.1-8B-Instruct\
--disaggregation-modedecode\
--disaggregation-transfer-backendascend\
--attention-backendascend\
--devicenpu\
--base-gpu-id1\
--tp-size1\
--host127.0.0.1\
--port8001
```

3. Launch Router

```
python3-msglang_router.launch_router\
--pd-disaggregation\
--policycache_aware\
--prefillhttp://127.0.0.1:80008995\
--decodehttp://127.0.0.1:8001\
--host127.0.0.1\
--port6688
```

### Running Service For Multimodal Language Models[#](#running-service-for-multimodal-language-models "Link to this heading")

#### PD Mixed Scene[#](#id1 "Link to this heading")

```
python3-msglang.launch_server\
--model-pathQwen3-VL-30B-A3B-Instruct\
--host127.0.0.1\
--port8000\
--tp4\
--devicenpu\
--attention-backendascend\
--mm-attention-backendascend_attn\
--disable-radix-cache\
--trust-remote-code\
--enable-multimodal\
--sampling-backendascend
```