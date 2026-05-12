---
title: CPU - vLLM
url: https://docs.vllm.ai/en/latest/getting_started/installation/cpu/
source: sitemap
fetched_at: 2026-05-07T21:14:47.016248519-03:00
rendered_js: false
word_count: 3004
summary: This document provides instructions for installing and configuring the vLLM library on various CPU architectures, including x86, Arm, Apple Silicon, and IBM Z.
tags:
    - vllm
    - cpu-inference
    - installation-guide
    - python-environment
    - hardware-acceleration
    - linux-setup
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/getting_started/installation/cpu.md "Edit this page")

vLLM is a Python library that supports the following CPU variants. Select your CPU type to see vendor specific instructions:

Intel/AMD x86ARM AArch64Apple siliconIBM Z (S390X)

vLLM supports basic model inferencing and serving on x86 CPU platform, with data types FP32, FP16 and BF16.

vLLM offers basic model inferencing and serving on Arm CPU platform, with support for NEON, data types FP32, FP16 and BF16.

vLLM has experimental support for macOS with Apple Silicon. For now, users must build from source to natively run on macOS.

Currently the CPU implementation for macOS supports FP32 and FP16 datatypes.

GPU-Accelerated Inference with vLLM-Metal

For GPU-accelerated inference on Apple Silicon using Metal, check out [vllm-metal](https://github.com/vllm-project/vllm-metal), a community-maintained hardware plugin that uses MLX as the compute backend.

vLLM has experimental support for s390x architecture on IBM Z platform. For now, users must build from source to natively run on IBM Z platform.

Currently, the CPU implementation for s390x architecture supports FP32, BF16 and FP16.

## Technical Discussions[¶](#technical-discussions "Permanent link")

The main discussions happen in the `#sig-cpu` channel of [vLLM Slack](https://slack.vllm.ai/).

When open a Github issue about the CPU backend, please add `[CPU Backend]` in the title and it will be labeled with `cpu` for better awareness.

## Requirements[¶](#requirements "Permanent link")

- Python: 3.10 -- 3.13

Intel/AMD x86ARM AArch64Apple siliconIBM Z (S390X)

- OS: Linux
- CPU flags: `avx512f` (Recommended), `avx2` (Limited features)

Tip

Use `lscpu` to check the CPU flags.

- OS: Linux
- Compiler: `gcc/g++ >= 12.3.0` (optional, recommended)
- Instruction Set Architecture (ISA): NEON support is required

<!--THE END-->

- OS: `macOS Sonoma` or later
- SDK: `XCode 15.4` or later with Command Line Tools
- Compiler: `Apple Clang >= 15.0.0`

<!--THE END-->

- OS: `Linux`
- SDK: `gcc/g++ >= 14.0.0` or later with Command Line Tools
- Instruction Set Architecture (ISA): VXE support is required. Works with Z14 and above.
- Build install python packages: `torchvision`, `llvmlite`, `numba`, `pyarrow (for testing)`, `opencv-headless`

## Set up using Python[¶](#set-up-using-python "Permanent link")

### Create a new Python environment[¶](#create-a-new-python-environment "Permanent link")

It's recommended to use [uv](https://docs.astral.sh/uv/), a very fast Python environment manager, to create and manage Python environments. Please follow the [documentation](https://docs.astral.sh/uv/#getting-started) to install `uv`. After installing `uv`, you can create a new Python environment using the following commands:

```
uvvenv--python3.12--seed--managed-python
source.venv/bin/activate
```

### Pre-built wheels[¶](#pre-built-wheels "Permanent link")

When specifying the index URL, please make sure to use the `cpu` variant subdirectory. For example, the nightly build index is: `https://wheels.vllm.ai/nightly/cpu/`.

Intel/AMD x86ARM AArch64Apple siliconIBM Z (S390X)

Pre-built vLLM wheels for x86 with AVX512/AVX2 are available since version 0.17.0. To install release wheels:

```
exportVLLM_VERSION=$(curl-shttps://api.github.com/repos/vllm-project/vllm/releases/latest|jq-r.tag_name|sed's/^v//')

# use uv
uvpipinstallhttps://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cpu-cp38-abi3-manylinux_2_35_x86_64.whl--torch-backendcpu
```

pip

```
# use pip
pipinstallhttps://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cpu-cp38-abi3-manylinux_2_35_x86_64.whl--extra-index-urlhttps://download.pytorch.org/whl/cpu
```

set `LD_PRELOAD`

Before use vLLM CPU installed via wheels, make sure TCMalloc and Intel OpenMP are installed and added to `LD_PRELOAD`:

```
# install TCMalloc, Intel OpenMP is installed with vLLM CPU
sudoapt-getinstall-y--no-install-recommendslibtcmalloc-minimal4

# manually find the path
sudofind/-iname*libtcmalloc_minimal.so.4
sudofind/-iname*libiomp5.so
TC_PATH=...
IOMP_PATH=...

# add them to LD_PRELOAD
exportLD_PRELOAD="$TC_PATH:$IOMP_PATH:$LD_PRELOAD"
```

#### Install the latest code[¶](#install-the-latest-code "Permanent link")

To install the wheel built from the latest main branch:

```
uvpipinstallvllm--extra-index-urlhttps://wheels.vllm.ai/nightly/cpu--index-strategyfirst-index--torch-backendcpu
```

#### Install specific revisions[¶](#install-specific-revisions "Permanent link")

If you want to access the wheels for previous commits (e.g. to bisect the behavior change, performance regression), you can specify the commit hash in the URL:

```
exportVLLM_COMMIT=730bd35378bf2a5b56b6d3a45be28b3092d26519# use full commit hash from the main branch
uvpipinstallvllm--extra-index-urlhttps://wheels.vllm.ai/${VLLM_COMMIT}/cpu--index-strategyfirst-index--torch-backendcpu
```

Pre-built vLLM wheels for Arm are available since version 0.11.2. These wheels contain pre-compiled C++ binaries.

```
exportVLLM_VERSION=$(curl-shttps://api.github.com/repos/vllm-project/vllm/releases/latest|jq-r.tag_name|sed's/^v//')
uvpipinstallhttps://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cpu-cp38-abi3-manylinux_2_35_aarch64.whl
```

pip

```
pipinstallhttps://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cpu-cp38-abi3-manylinux_2_35_aarch64.whl
```

set `LD_PRELOAD`

Before use vLLM CPU installed via wheels, make sure TCMalloc is installed and added to `LD_PRELOAD`:

```
# install TCMalloc
sudoapt-getinstall-y--no-install-recommendslibtcmalloc-minimal4

# manually find the path
sudofind/-iname*libtcmalloc_minimal.so.4
TC_PATH=...

# add them to LD_PRELOAD
exportLD_PRELOAD="$TC_PATH:$LD_PRELOAD"
```

The `uv` approach works for vLLM `v0.6.6` and later. A unique feature of `uv` is that packages in `--extra-index-url` have [higher priority than the default index](https://docs.astral.sh/uv/pip/compatibility/#packages-that-exist-on-multiple-indexes). If the latest public release is `v0.6.6.post1`, `uv`'s behavior allows installing a commit before `v0.6.6.post1` by specifying the `--extra-index-url`. In contrast, `pip` combines packages from `--extra-index-url` and the default index, choosing only the latest version, which makes it difficult to install a development version prior to the released version.

#### Install the latest code[¶](#install-the-latest-code_1 "Permanent link")

LLM inference is a fast-evolving field, and the latest code may contain bug fixes, performance improvements, and new features that are not released yet. To allow users to try the latest code without waiting for the next release, vLLM provides working pre-built Arm CPU wheels for every commit since `v0.11.2` on [https://wheels.vllm.ai/nightly](https://wheels.vllm.ai/nightly). For native CPU wheels, this index should be used:

- `https://wheels.vllm.ai/nightly/cpu/vllm`

To install from nightly index, run:

```
uvpipinstallvllm--extra-index-urlhttps://wheels.vllm.ai/nightly/cpu--index-strategyfirst-index
```

pip (there's a caveat)

Using `pip` to install from nightly indices is *not supported*, because `pip` combines packages from `--extra-index-url` and the default index, choosing only the latest version, which makes it difficult to install a development version prior to the released version. In contrast, `uv` gives the extra index [higher priority than the default index](https://docs.astral.sh/uv/pip/compatibility/#packages-that-exist-on-multiple-indexes).

If you insist on using `pip`, you have to specify the full URL (link address) of the wheel file (which can be obtained from https://wheels.vllm.ai/nightly/cpu/vllm).

```
pipinstallhttps://wheels.vllm.ai/4fa7ce46f31cbd97b4651694caf9991cc395a259/vllm-0.13.0rc2.dev104%2Bg4fa7ce46f.cpu-cp38-abi3-manylinux_2_35_aarch64.whl# current nightly build (the filename will change!)
```

#### Install specific revisions[¶](#install-specific-revisions_1 "Permanent link")

If you want to access the wheels for previous commits (e.g. to bisect the behavior change, performance regression), you can specify the commit hash in the URL:

```
exportVLLM_COMMIT=730bd35378bf2a5b56b6d3a45be28b3092d26519# use full commit hash from the main branch
uvpipinstallvllm--extra-index-urlhttps://wheels.vllm.ai/${VLLM_COMMIT}/cpu--index-strategyfirst-index
```

Currently, there are no pre-built Apple silicon CPU wheels.

Currently, there are no pre-built IBM Z CPU wheels.

### Build wheel from source[¶](#build-wheel-from-source "Permanent link")

#### Set up using Python-only build (without compilation)[¶](#python-only-build "Permanent link")

This method requires [pre-built wheels](#pre-built-wheels) for your platform.

Please refer to the instructions for [Python-only build on GPU](https://docs.vllm.ai/en/latest/getting_started/installation/gpu/#python-only-build), and replace the build commands with:

```
VLLM_USE_PRECOMPILED=1VLLM_PRECOMPILED_WHEEL_VARIANT=cpuVLLM_TARGET_DEVICE=cpuuvpipinstall--editable.
```

#### Full build (with compilation)[¶](#full-build "Permanent link")

Intel/AMD x86ARM AArch64Apple siliconIBM Z (s390x)

Install recommended compiler. We recommend to use `gcc/g++ >= 12.3.0` as the default compiler to avoid potential problems. For example, on Ubuntu 22.4, you can run:

```
sudoapt-getupdate-y
sudoapt-getinstall-ygcc-12g++-12libnuma-dev
sudoupdate-alternatives--install/usr/bin/gccgcc/usr/bin/gcc-1210--slave/usr/bin/g++g++/usr/bin/g++-12
```

It's recommended to use [uv](https://docs.astral.sh/uv/), a very fast Python environment manager, to create and manage Python environments. Please follow the [documentation](https://docs.astral.sh/uv/#getting-started) to install `uv`. After installing `uv`, you can create a new Python environment using the following commands:

```
uvvenv--python3.12--seed--managed-python
source.venv/bin/activate
```

Clone the vLLM project:

```
gitclonehttps://github.com/vllm-project/vllm.gitvllm_source
cdvllm_source
```

Install the required dependencies:

```
uvpipinstall-rrequirements/build/cpu.txt--torch-backendcpu
uvpipinstall-rrequirements/cpu.txt--torch-backendcpu
```

pip

```
pipinstall--upgradepip
pipinstall-v-rrequirements/build/cpu.txt--extra-index-urlhttps://download.pytorch.org/whl/cpu
pipinstall-v-rrequirements/cpu.txt--extra-index-urlhttps://download.pytorch.org/whl/cpu
```

Build and install vLLM:

```
VLLM_TARGET_DEVICE=cpuuvpipinstall.--no-build-isolation
```

If you want to develop vLLM, install it in editable mode instead.

```
VLLM_TARGET_DEVICE=cpupython3setup.pydevelop
```

Optionally, build a portable wheel which you can then install elsewhere:

```
VLLM_TARGET_DEVICE=cpuuvbuild--wheel--no-build-isolation

uvpipinstalldist/*.whl
```

pip

```
VLLM_TARGET_DEVICE=cpupython-mbuild--wheel--no-isolation
```

set `LD_PRELOAD`

Before use vLLM CPU installed via wheels, make sure TCMalloc and Intel OpenMP are installed and added to `LD_PRELOAD`:

```
# install TCMalloc, Intel OpenMP is installed with vLLM CPU
sudoapt-getinstall-y--no-install-recommendslibtcmalloc-minimal4

# manually find the path
sudofind/-iname*libtcmalloc_minimal.so.4
sudofind/-iname*libiomp5.so
TC_PATH=...
IOMP_PATH=...

# add them to LD_PRELOAD
exportLD_PRELOAD="$TC_PATH:$IOMP_PATH:$LD_PRELOAD"
```

Troubleshooting

- **NumPy ≥2.0 error**: Downgrade using `pip install "numpy<2.0"`.
- **CMake picks up CUDA**: Add `CMAKE_DISABLE_FIND_PACKAGE_CUDA=ON` to prevent CUDA detection during CPU builds, even if CUDA is installed.
- `AMD` requires at least 4th gen processors (Zen 4/Genoa) or higher to support [AVX512](https://www.phoronix.com/review/amd-zen4-avx512) to run vLLM on CPU.
- If you receive an error such as: `Could not find a version that satisfies the requirement torch==X.Y.Z+cpu+cpu`, consider updating [pyproject.toml](https://github.com/vllm-project/vllm/blob/main/pyproject.toml) to help pip resolve the dependency.
  
  pyproject.toml
  
  ```
  [build-system]
  requires=[
  "cmake>=3.26.1",
  ...
  "torch==X.Y.Z+cpu"# <-------
  ]
  ```

First, install the recommended compiler. We recommend using `gcc/g++ >= 12.3.0` as the default compiler to avoid potential problems. For example, on Ubuntu 22.4, you can run:

```
sudoapt-getupdate-y
sudoapt-getinstall-y--no-install-recommendsccachegitcurlwgetca-certificatesgcc-12g++-12libtcmalloc-minimal4libnuma-devffmpeglibsm6libxext6libgl1jqlsof
sudoupdate-alternatives--install/usr/bin/gccgcc/usr/bin/gcc-1210--slave/usr/bin/g++g++/usr/bin/g++-12
```

Second, clone the vLLM project:

```
gitclonehttps://github.com/vllm-project/vllm.gitvllm_source
cdvllm_source
```

Third, install required dependencies:

```
uvpipinstall-rrequirements/build/cpu.txt--torch-backendcpu
uvpipinstall-rrequirements/cpu.txt--torch-backendcpu
```

pip

```
pipinstall--upgradepip
pipinstall-v-rrequirements/build/cpu.txt--extra-index-urlhttps://download.pytorch.org/whl/cpu
pipinstall-v-rrequirements/cpu.txt--extra-index-urlhttps://download.pytorch.org/whl/cpu
```

Finally, build and install vLLM:

```
VLLM_TARGET_DEVICE=cpuuvpipinstall.--no-build-isolation
```

If you want to develop vLLM, install it in editable mode instead.

```
VLLM_TARGET_DEVICE=cpuuvpipinstall-e.--no-build-isolation
```

Testing has been conducted on AWS Graviton3 instances for compatibility.

set `LD_PRELOAD`

Before use vLLM CPU installed via wheels, make sure TCMalloc is installed and added to `LD_PRELOAD`:

```
# install TCMalloc
sudoapt-getinstall-y--no-install-recommendslibtcmalloc-minimal4

# manually find the path
sudofind/-iname*libtcmalloc_minimal.so.4
TC_PATH=...

# add them to LD_PRELOAD
exportLD_PRELOAD="$TC_PATH:$LD_PRELOAD"
```

After installation of XCode and the Command Line Tools, which include Apple Clang, execute the following commands to build and install vLLM from source.

```
gitclonehttps://github.com/vllm-project/vllm.git
cdvllm
uvpipinstall-rrequirements/cpu.txt--index-strategyunsafe-best-match
uvpipinstall-e.
```

Tip

The `--index-strategy unsafe-best-match` flag is needed to resolve dependencies across multiple package indexes (PyTorch CPU index and PyPI). Without this flag, you may encounter `typing-extensions` version conflicts.

The term "unsafe" refers to the package resolution strategy, not security. By default, `uv` only searches the first index where a package is found to prevent dependency confusion attacks. This flag allows `uv` to search all configured indexes to find the best compatible versions. Since both PyTorch and PyPI are trusted package sources, using this strategy is safe and appropriate for vLLM installation.

Note

On macOS the `VLLM_TARGET_DEVICE` is automatically set to `cpu`, which is currently the only supported device.

Troubleshooting

If the build fails with errors like the following where standard C++ headers cannot be found, try to remove and reinstall your [Command Line Tools for Xcode](https://developer.apple.com/download/all/).

```
[...] fatal error: 'map' file not found
        1 | #include <map>
            |          ^~~~~
    1 error generated.
    [2/8] Building CXX object CMakeFiles/_C.dir/csrc/cpu/pos_encoding.cpp.o

[...] fatal error: 'cstddef' file not found
        10 | #include <cstddef>
            |          ^~~~~~~~~
    1 error generated.
```

* * *

If the build fails with C++11/C++17 compatibility errors like the following, the issue is that the build system is defaulting to an older C++ standard:

```
[...] error: 'constexpr' is not a type
[...] error: expected ';' before 'constexpr'
[...] error: 'constexpr' does not name a type
```

**Solution**: Your compiler might be using an older C++ standard. Edit `cmake/cpu_extension.cmake` and add `set(CMAKE_CXX_STANDARD 17)` before `set(CMAKE_CXX_STANDARD_REQUIRED ON)`.

To check your compiler's C++ standard support:

```
clang++-std=c++17-pedantic-dM-E-xc++/dev/null|grep__cplusplus
```

On Apple Clang 16 you should see: `#define __cplusplus 201703L`

Install the following packages from the package manager before building the vLLM. For example on RHEL 9.6:

```
dnfinstall-y\
whichprocpsfindutilstarvimgitgcc-toolset-14gcc-toolset-14-binutilsgcc-toolset-14-libatomic-develzlib-devel\
libjpeg-turbo-devellibtiff-devellibpng-devellibwebp-develfreetype-develharfbuzz-devel\
openssl-developenblasopenblas-develautoconfautomakelibtoolcmakenumpylibsndfile\
clangllvm-develllvm-staticclang-devel
```

Install rust&gt;=1.80 which is needed for `outlines-core` and `uvloop` python packages installation.

```
curlhttps://sh.rustup.rs-sSf|sh-s---y&&\
."$HOME/.cargo/env"
```

Execute the following commands to build and install vLLM from source.

Tip

Please build the following dependencies, `torchvision`, `llvmlite`, `numba`, `llguidance`, `pyarrow`, `opencv-headless` from source before building vLLM.

```
uvpipinstall-v\
--extra-index-urlhttps://download.pytorch.org/whl/cpu\
--torch-backendauto\
-rrequirements/build/cpu.txt\
-rrequirements/cpu.txt\
VLLM_TARGET_DEVICE=cpupythonsetup.pybdist_wheel&&\
uvpipinstalldist/*.whl
```

pip

```
pipinstall-v\
--extra-index-urlhttps://download.pytorch.org/whl/cpu\
-rrequirements/build/cpu.txt\
-rrequirements/cpu.txt\
VLLM_TARGET_DEVICE=cpupythonsetup.pybdist_wheel&&\
pipinstalldist/*.whl
```

## Set up using Docker[¶](#set-up-using-docker "Permanent link")

### Pre-built images[¶](#pre-built-images "Permanent link")

Intel/AMD x86ARM AArch64Apple siliconIBM Z (S390X)

You can pull the latest available CPU image from Docker Hub:

```
dockerpullvllm/vllm-openai-cpu:latest-x86_64
```

To pull an image for a specific vLLM version:

```
exportVLLM_VERSION=$(curl-shttps://api.github.com/repos/vllm-project/vllm/releases/latest|jq-r.tag_name|sed's/^v//')
dockerpullvllm/vllm-openai-cpu:v${VLLM_VERSION}-x86_64
```

All available image tags are here: [https://hub.docker.com/r/vllm/vllm-openai-cpu/tags](https://hub.docker.com/r/vllm/vllm-openai-cpu/tags)

You can run these images via:

```
dockerrun\
-v~/.cache/huggingface:/root/.cache/huggingface\
-p8000:8000\
--env"HF_TOKEN=<secret>"\
vllm/vllm-openai-cpu:latest-x86_64<args...>
```

To pull the latest image from Docker Hub:

```
dockerpullvllm/vllm-openai-cpu:latest-arm64
```

To pull an image with a specific vLLM version:

```
exportVLLM_VERSION=$(curl-shttps://api.github.com/repos/vllm-project/vllm/releases/latest|jq-r.tag_name|sed's/^v//')
dockerpullvllm/vllm-openai-cpu:v${VLLM_VERSION}-arm64
```

All available image tags are here: [https://hub.docker.com/r/vllm/vllm-openai-cpu/tags](https://hub.docker.com/r/vllm/vllm-openai-cpu/tags).

You can run these images via:

```
dockerrun\
-v~/.cache/huggingface:/root/.cache/huggingface\
-p8000:8000\
--env"HF_TOKEN=<secret>"\
vllm/vllm-openai-cpu:latest-arm64<args...>
```

You can also access the latest code with Docker images. These are not intended for production use and are meant for CI and testing only. They will expire after several days.

The latest code can contain bugs and may not be stable. Please use it with caution.

```
exportVLLM_COMMIT=6299628d326f429eba78736acb44e76749b281f5# use full commit hash from the main branch
dockerpullpublic.ecr.aws/q9t5s3a7/vllm-ci-postmerge-repo:${VLLM_COMMIT}-arm64-cpu
```

Currently, there are no pre-built Arm silicon CPU images.

Currently, there are no pre-built IBM Z CPU images.

### Build image from source[¶](#build-image-from-source "Permanent link")

Intel/AMD x86ARM AArch64Apple siliconIBM Z (S390X)

#### Building for your target CPU[¶](#building-for-your-target-cpu "Permanent link")

```
dockerbuild-fdocker/Dockerfile.cpu\
--build-argVLLM_CPU_X86=<false(default)|true>\ # For cross-compilation
--tagvllm-cpu-env\
--targetvllm-openai.
```

#### Launching the OpenAI server[¶](#launching-the-openai-server "Permanent link")

```
dockerrun--rm\
--security-optseccomp=unconfined\
--cap-addSYS_NICE\
--shm-size=4g\
-p8000:8000\
-eVLLM_CPU_KVCACHE_SPACE=<KVcachespace>\
vllm-cpu-env\
meta-llama/Llama-3.2-1B-Instruct\
--dtype=bfloat16\
othervLLMOpenAIserverarguments
```

#### Building for your target ARM CPU[¶](#building-for-your-target-arm-cpu "Permanent link")

```
dockerbuild-fdocker/Dockerfile.cpu\
--platform=linux/arm64\
--build-argVLLM_CPU_ARM_BF16=<false(default)|true>\
--tagvllm-cpu-env\
--targetvllm-openai.
```

Auto-detection by default

By default, ARM CPU instruction sets (BF16, NEON, etc.) are automatically detected from the build system's CPU flags. The `VLLM_CPU_ARM_BF16` build argument is used for cross-compilation:

- `VLLM_CPU_ARM_BF16=true` - Force-enable ARM BF16 support (build with BF16 regardless of build system capabilities)
- `VLLM_CPU_ARM_BF16=false` - Rely on auto-detection (default)

##### Examples[¶](#examples "Permanent link")

###### Auto-detection build (native ARM)[¶](#auto-detection-build-native-arm "Permanent link")

```
# Building on ARM64 system - platform auto-detected
dockerbuild-fdocker/Dockerfile.cpu\
--tagvllm-cpu-arm64\
--targetvllm-openai.
```

###### Cross-compile for ARM with BF16 support[¶](#cross-compile-for-arm-with-bf16-support "Permanent link")

```
# Building on ARM64 for newer ARM CPUs with BF16
dockerbuild-fdocker/Dockerfile.cpu\
--build-argVLLM_CPU_ARM_BF16=true\
--tagvllm-cpu-arm64-bf16\
--targetvllm-openai.
```

###### Cross-compile from x86\_64 to ARM64 with BF16[¶](#cross-compile-from-x86_64-to-arm64-with-bf16 "Permanent link")

```
# Requires Docker buildx with ARM emulation (QEMU)
dockerbuildxbuild-fdocker/Dockerfile.cpu\
--platform=linux/arm64\
--build-argVLLM_CPU_ARM_BF16=true\
--build-argmax_jobs=4\
--tagvllm-cpu-arm64-bf16\
--targetvllm-openai\
--load.
```

ARM BF16 requirements

ARM BF16 support requires ARMv8.6-A or later (FEAT\_BF16). Supported on AWS Graviton3/4, AmpereOne, and other recent ARM processors.

#### Launching the OpenAI server[¶](#launching-the-openai-server_1 "Permanent link")

```
dockerrun--rm\
--security-optseccomp=unconfined\
--cap-addSYS_NICE\
--shm-size=4g\
-p8000:8000\
-eVLLM_CPU_KVCACHE_SPACE=<KVcachespace>\
-eVLLM_CPU_OMP_THREADS_BIND=<CPUcoresforinference>\
vllm-cpu-arm64\
meta-llama/Llama-3.2-1B-Instruct\
--dtype=bfloat16\
othervLLMOpenAIserverarguments
```

Alternative to --privileged

Instead of `--privileged=true`, use `--cap-add SYS_NICE --security-opt seccomp=unconfined` for better security.

```
dockerbuild-fdocker/Dockerfile.s390x\
--tagvllm-cpu-env.

# Launch OpenAI server
dockerrun--rm\
--privilegedtrue\
--shm-size4g\
-p8000:8000\
-eVLLM_CPU_KVCACHE_SPACE=<KVcachespace>\
-eVLLM_CPU_OMP_THREADS_BIND=<CPUcoresforinference>\
vllm-cpu-env\
--modelmeta-llama/Llama-3.2-1B-Instruct\
--dtypefloat\
othervLLMOpenAIserverarguments
```

Tip

An alternative of `--privileged true` is `--cap-add SYS_NICE --security-opt seccomp=unconfined`.

- `VLLM_CPU_KVCACHE_SPACE`: specify the KV Cache size (e.g, `VLLM_CPU_KVCACHE_SPACE=40` means 40 GiB space for KV cache), larger setting will allow vLLM to run more requests in parallel. This parameter should be set based on the hardware configuration and memory management pattern of users. Default value is `0`.
- `VLLM_CPU_OMP_THREADS_BIND`: specify the CPU cores dedicated to the OpenMP threads, can be set as CPU id lists, `auto` (by default), or `nobind` (to disable binding to individual CPU cores and to inherit user-defined OpenMP variables). For example, `VLLM_CPU_OMP_THREADS_BIND=0-31` means there will be 32 OpenMP threads bound on 0-31 CPU cores. `VLLM_CPU_OMP_THREADS_BIND=0-31|32-63` means there will be 2 tensor parallel processes, 32 OpenMP threads of rank0 are bound on 0-31 CPU cores, and the OpenMP threads of rank1 are bound on 32-63 CPU cores. By setting to `auto`, the OpenMP threads of each rank are bound to the CPU cores in each NUMA node respectively. If set to `nobind`, the number of OpenMP threads is determined by the standard `OMP_NUM_THREADS` environment variable.
- `VLLM_CPU_NUM_OF_RESERVED_CPU`: specify the number of CPU cores which are not dedicated to the OpenMP threads for each rank. The variable only takes effect when VLLM\_CPU\_OMP\_THREADS\_BIND is set to `auto`. Default value is `None`. If the value is not set and use `auto` thread binding, no CPU will be reserved for `world_size == 1`, 1 CPU per rank will be reserved for `world_size > 1`.
- `CPU_VISIBLE_MEMORY_NODES`: specify visible NUMA memory nodes for vLLM CPU workers, similar to `CUDA_VISIBLE_DEVICES`. The variable only takes effect when VLLM\_CPU\_OMP\_THREADS\_BIND is set to `auto`. The variable provides more control for the auto thread-binding feature, such as masking nodes and changing nodes binding sequence.
- `VLLM_CPU_SGL_KERNEL` (x86 only, Experimental): whether to use small-batch optimized kernels for linear layer and MoE layer, especially for low-latency requirements like online serving. The kernels require AMX instruction set, BFloat16 weight type and weight shapes divisible by 32. Default is `0` (False).

## FAQ[¶](#faq "Permanent link")

### Which `dtype` should be used?[¶](#which-dtype-should-be-used "Permanent link")

- Currently, vLLM CPU uses model default settings as `dtype`. However, due to unstable float16 support in torch CPU, it is recommended to explicitly set `dtype=bfloat16` if there are any performance or accuracy problem.

### How to launch a vLLM service on CPU?[¶](#how-to-launch-a-vllm-service-on-cpu "Permanent link")

- When using the online serving, it is recommended to reserve 1-2 CPU cores for the serving framework to avoid CPU oversubscription. For example, on a platform with 32 physical CPU cores, reserving CPU 31 for the framework and using CPU 0-30 for inference threads:

```
exportVLLM_CPU_KVCACHE_SPACE=40
exportVLLM_CPU_OMP_THREADS_BIND=0-30
vllmservefacebook/opt-125m--dtype=bfloat16
```

or using default auto thread binding:

```
exportVLLM_CPU_KVCACHE_SPACE=40
exportVLLM_CPU_NUM_OF_RESERVED_CPU=1
vllmservefacebook/opt-125m--dtype=bfloat16
```

Note, it is recommended to manually reserve 1 CPU for vLLM front-end process when `world_size == 1`.

### What are supported models on CPU?[¶](#what-are-supported-models-on-cpu "Permanent link")

For the full and up-to-date list of models validated on CPU platforms, please see the official documentation: [Supported Models on CPU](https://docs.vllm.ai/en/latest/models/hardware_supported_models/cpu/)

### How to find benchmark configuration examples for supported CPU models?[¶](#how-to-find-benchmark-configuration-examples-for-supported-cpu-models "Permanent link")

For any model listed under [Supported Models on CPU](https://docs.vllm.ai/en/latest/models/hardware_supported_models/cpu/), optimized runtime configurations are provided in the vLLM Benchmark Suite’s CPU test cases, defined in cpu test cases as serving-tests-cpu.json. Full test cases for Text-only models, Multi-Modal models and Embedded models are in cpu Text-Only test cases as serving-tests-cpu-text.json, cpu Multi-Modal test cases as serving-tests-cpu-multimodal.json and cpu Embedded test cases as serving-tests-cpu-embed.json.  
For details on how these optimized configurations are determined, see: [performance-benchmark-details](https://github.com/vllm-project/vllm/blob/main/.buildkite/performance-benchmarks/README.md#performance-benchmark-details). To benchmark the supported models using these optimized settings, follow the steps in [running vLLM Benchmark Suite manually](https://docs.vllm.ai/en/latest/benchmarking/dashboard/#manually-trigger-the-benchmark) and run the Benchmark Suite on a CPU environment.

Below is an example command to benchmark all CPU-supported models using optimized configurations.

```
ON_CPU=1bash.buildkite/performance-benchmarks/scripts/run-performance-benchmarks.sh
```

The benchmark results will be saved in `./benchmark/results/`. In the directory, the generated `.commands` files contain all example commands for the benchmark.

We recommend configuring tensor-parallel-size to match the number of NUMA nodes on your system. Note that the current release does not support tensor-parallel-size=6. To determine the number of NUMA nodes available, use the following command:

```
lscpu|grep"NUMA node(s):"|awk'{print $3}'
```

For performance reference, users may also consult the [vLLM Performance Dashboard](https://hud.pytorch.org/benchmark/llms?repoName=vllm-project%2Fvllm&deviceName=cpu) , which publishes default-model CPU results produced using the same Benchmark Suite.

#### Dry-Run[¶](#dry-run "Permanent link")

For users only need to get the optimized runtime configurations without running benchmark, a Dry-Run mode is provided. By passing an environment variable DRY\_RUN=1 with run-performance-benchmarks.sh, all commands will be generated under `./benchmark/results/`.

```
ON_CPU=1DRY_RUN=1bash.buildkite/performance-benchmarks/scripts/run-performance-benchmarks.sh
```

By providing different JSON file, users can get runtime configurations for different models such as Embedded Models.

```
ON_CPU=1SERVING_JSON=serving-tests-cpu-embed.jsonDRY_RUN=1bash.buildkite/performance-benchmarks/scripts/run-performance-benchmarks.sh
```

By providing MODEL\_FILTER and DTYPE\_FILTER, only commands for related model ID and Data Type will be generated.

```
ON_CPU=1SERVING_JSON=serving-tests-cpu-text.jsonDRY_RUN=1MODEL_FILTER=meta-llama/Llama-3.1-8B-InstructDTYPE_FILTER=bfloat16bash.buildkite/performance-benchmarks/scripts/run-performance-benchmarks.sh
```

### How to decide `VLLM_CPU_OMP_THREADS_BIND`?[¶](#how-to-decide-vllm_cpu_omp_threads_bind "Permanent link")

- Default `auto` thread-binding is recommended for most cases. Ideally, each OpenMP thread will be bound to a dedicated physical core respectively, threads of each rank will be bound to the same NUMA node respectively, and 1 CPU per rank will be reserved for other vLLM components when `world_size > 1`. If you have any performance problems or unexpected binding behaviours, please try to bind threads as following.
- On a hyper-threading enabled platform with 16 logical CPU cores / 8 physical CPU cores:

Commands

```
$ lscpu-e# check the mapping between logical CPU cores and physical CPU cores

# The"CPU"columnmeansthelogicalCPUcoreIDs,andthe"CORE"columnmeansthephysicalcoreIDs.Onthisplatform,twologicalcoresaresharingonephysicalcore.
CPU NODE SOCKET CORE L1d:L1i:L2:L3 ONLINE    MAXMHZ   MINMHZ      MHZ
0    0      0    0 0:0:0:0          yes 2401.0000 800.0000  800.000
1    0      0    1 1:1:1:0          yes 2401.0000 800.0000  800.000
2    0      0    2 2:2:2:0          yes 2401.0000 800.0000  800.000
3    0      0    3 3:3:3:0          yes 2401.0000 800.0000  800.000
4    0      0    4 4:4:4:0          yes 2401.0000 800.0000  800.000
5    0      0    5 5:5:5:0          yes 2401.0000 800.0000  800.000
6    0      0    6 6:6:6:0          yes 2401.0000 800.0000  800.000
7    0      0    7 7:7:7:0          yes 2401.0000 800.0000  800.000
8    0      0    0 0:0:0:0          yes 2401.0000 800.0000  800.000
9    0      0    1 1:1:1:0          yes 2401.0000 800.0000  800.000
10   0      0    2 2:2:2:0          yes 2401.0000 800.0000  800.000
11   0      0    3 3:3:3:0          yes 2401.0000 800.0000  800.000
12   0      0    4 4:4:4:0          yes 2401.0000 800.0000  800.000
13   0      0    5 5:5:5:0          yes 2401.0000 800.0000  800.000
14   0      0    6 6:6:6:0          yes 2401.0000 800.0000  800.000
15   0      0    7 7:7:7:0          yes 2401.0000 800.0000  800.000

# Onthisplatform,itisrecommendedtoonlybindopenMPthreadsonlogicalCPUcores0-7or8-15
$ exportVLLM_CPU_OMP_THREADS_BIND=0-7
$ pythonexamples/basic/offline_inference/basic.py
```

- When deploying vLLM CPU backend on a multi-socket machine with NUMA and enable tensor parallel or pipeline parallel, each NUMA node is treated as a TP/PP rank. So be aware to set CPU cores of a single rank on the same NUMA node to avoid cross NUMA node memory access.

### How to decide `VLLM_CPU_KVCACHE_SPACE`?[¶](#how-to-decide-vllm_cpu_kvcache_space "Permanent link")

This value is 4GB by default. Larger space can support more concurrent requests, longer context length. However, users should take care of memory capacity of each NUMA node. The memory usage of each TP rank is the sum of `weight shard size` and `VLLM_CPU_KVCACHE_SPACE`, if it exceeds the capacity of a single NUMA node, the TP worker will be killed with `exitcode 9` due to out-of-memory.

### How to do performance tuning for vLLM CPU?[¶](#how-to-do-performance-tuning-for-vllm-cpu "Permanent link")

First of all, please make sure the thread-binding and KV cache space are properly set and take effect. You can check the thread-binding by running a vLLM benchmark and observing CPU cores usage via `htop`.

Use multiples of 32 as `--block-size`, which is 128 by default.

Inference batch size is an important parameter for the performance. A larger batch usually provides higher throughput, a smaller batch provides lower latency. Tuning the max batch size starting from the default value to balance throughput and latency is an effective way to improve vLLM CPU performance on specific platforms. There are two important related parameters in vLLM:

- `--max-num-batched-tokens`, defines the limit of token numbers in a single batch, has more impacts on the first token performance. The default value is set as:
  
  - Offline Inference: `4096 * world_size`
  - Online Serving: `2048 * world_size`
- `--max-num-seqs`, defines the limit of sequence numbers in a single batch, has more impacts on the output token performance.
  
  - Offline Inference: `256 * world_size`
  - Online Serving: `128 * world_size`

vLLM CPU supports data parallel (DP), tensor parallel (TP) and pipeline parallel (PP) to leverage multiple CPU sockets and memory nodes. For more details of tuning DP, TP and PP, please refer to [Optimization and Tuning](https://docs.vllm.ai/en/latest/configuration/optimization/). For vLLM CPU, it is recommended to use DP, TP and PP together if there are enough CPU sockets and memory nodes.

### Which quantization configs does vLLM CPU support?[¶](#which-quantization-configs-does-vllm-cpu-support "Permanent link")

- vLLM CPU supports quantizations:
  
  - AWQ (x86 only)
  - GPTQ (x86 only)
  - compressed-tensor INT8 W8A8 (x86, s390x)

### Why do I see `get_mempolicy: Operation not permitted` when running in Docker?[¶](#why-do-i-see-get_mempolicy-operation-not-permitted-when-running-in-docker "Permanent link")

In some container environments (like Docker), NUMA-related syscalls used by vLLM (e.g., `get_mempolicy`, `migrate_pages`) are blocked/denied in the runtime's default seccomp/capabilities settings. This may lead to warnings like `get_mempolicy: Operation not permitted`. Functionality is not affected, but NUMA memory binding/migration optimizations may not take effect and performance can be suboptimal.

To enable these optimizations inside Docker with the least privilege, you can follow below tips:

```
dockerrun...--cap-addSYS_NICE--security-optseccomp=unconfined...

# 1) `--cap-add SYS_NICE` is to address `get_mempolicy` EPERM issue.

# 2) `--security-opt seccomp=unconfined` is to enable `migrate_pages` for `numa_migrate_pages()`.
# Actually, `seccomp=unconfined` bypasses the seccomp for container,
# if it's unacceptable, you can customize your own seccomp profile,
# based on docker/runtime default.json and add `migrate_pages` to `SCMP_ACT_ALLOW` list.

# reference : https://docs.docker.com/engine/security/seccomp/
```

Alternatively, running with `--privileged=true` also works but is broader and not generally recommended.

In K8S, the following configuration can be added to workload yaml to achieve the same effect as above:

```
securityContext:
seccompProfile:
type:Unconfined
capabilities:
add:
-SYS_NICE
```