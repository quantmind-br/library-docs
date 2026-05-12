---
title: GPU - vLLM
url: https://docs.vllm.ai/en/latest/getting_started/installation/gpu/
source: sitemap
fetched_at: 2026-05-07T21:14:48.794649112-03:00
rendered_js: false
word_count: 1420
summary: This document provides instructions for setting up a development environment for vLLM, detailing both pre-compiled Python-only builds and full source compilation methods, including troubleshooting and optimization techniques.
tags:
    - vllm
    - development-setup
    - compilation
    - python-development
    - cuda
    - build-configuration
    - caching
category: guide
---

#### Set up using Python-only build (without compilation)[¶](#python-only-build "Permanent link")

If you only need to change Python code, you can build and install vLLM without compilation. Using `uv pip`'s [`--editable` flag](https://docs.astral.sh/uv/pip/packages/#editable-packages), changes you make to the code will be reflected when you run vLLM:

```
gitclonehttps://github.com/vllm-project/vllm.git
cdvllm
VLLM_USE_PRECOMPILED=1uvpipinstall--editable.--torch-backend=auto
```

This command will do the following:

1. Look for the current branch in your vLLM clone.
2. Identify the corresponding base commit in the main branch.
3. Download the pre-built wheel of the base commit.
4. Use its compiled libraries in the installation.

Note

1. If you change C++ or kernel code, you cannot use Python-only build; otherwise you will see an import error about library not found or undefined symbol.
2. If you rebase your dev branch, it is recommended to uninstall vllm and re-run the above command to make sure your libraries are up to date.

In case you see an error about wheel not found when running the above command, it might be because the commit you based on in the `main` branch was just merged and its precompiled wheel is not available yet. You can wait around an hour and retry, or set `VLLM_PRECOMPILED_WHEEL_COMMIT=nightly` to automatically select the most recent already-built commit on `main`.

```
exportVLLM_PRECOMPILED_WHEEL_COMMIT=nightly
exportVLLM_USE_PRECOMPILED=1
uvpipinstall--editable.
```

There are more environment variables to control the behavior of Python-only build:

- `VLLM_PRECOMPILED_WHEEL_LOCATION`: specify the exact wheel URL or local file path of a pre-compiled wheel to use. All other logic to find the wheel will be skipped.
- `VLLM_PRECOMPILED_WHEEL_COMMIT`: override the commit hash to download the pre-compiled wheel. It can be `nightly` to use the last **already built** commit on the main branch.
- `VLLM_PRECOMPILED_WHEEL_VARIANT`: specify the variant subdirectory to use on the nightly index, e.g., `cu129`, `cu130`, `cpu`. If not specified, the variant is auto-detected based on your system's CUDA version (from PyTorch or nvidia-smi). You can also set `VLLM_MAIN_CUDA_VERSION` to override auto-detection.

You can find more information about vLLM's wheels in [Install the latest code](#install-the-latest-code).

Note

There is a possibility that your source code may have a different commit ID compared to the latest vLLM wheel, which could potentially lead to unknown errors. It is recommended to use the same commit ID for the source code as the vLLM wheel you have installed. Please refer to [Install the latest code](#install-the-latest-code) for instructions on how to install a specified wheel.

#### Full build (with compilation)[¶](#full-build "Permanent link")

If you want to modify C++ or CUDA code, you'll need to build vLLM from source. This can take several minutes:

```
gitclonehttps://github.com/vllm-project/vllm.git
cdvllm
uvpipinstall-e.--torch-backend=auto
```

Tip

Building from source requires a lot of compilation. If you are building from source repeatedly, it's more efficient to cache the compilation results.

For example, you can install [ccache](https://github.com/ccache/ccache) using `conda install ccache` or `apt install ccache` . As long as `which ccache` command can find the `ccache` binary, it will be used automatically by the build system. After the first build, subsequent builds will be much faster.

When using `ccache` with `pip install -e .`, you should run `CCACHE_NOHASHDIR="true" pip install --no-build-isolation -e .`. This is because `pip` creates a new folder with a random name for each build, preventing `ccache` from recognizing that the same files are being built.

[sccache](https://github.com/mozilla/sccache) works similarly to `ccache`, but has the capability to utilize caching in remote storage environments. The following environment variables can be set to configure the vLLM `sccache` remote: `SCCACHE_BUCKET=vllm-build-sccache SCCACHE_REGION=us-west-2 SCCACHE_S3_NO_CREDENTIALS=1`. We also recommend setting `SCCACHE_IDLE_TIMEOUT=0`.

Faster Kernel Development

For frequent C++/CUDA kernel changes, after the initial `uv pip install -e .` setup, consider using the [Incremental Compilation Workflow](https://docs.vllm.ai/en/latest/contributing/incremental_build/) for significantly faster rebuilds of only the modified kernel code.

##### Use an existing PyTorch installation[¶](#use-an-existing-pytorch-installation "Permanent link")

There are scenarios where the PyTorch dependency cannot be easily installed with `uv`, for example, when building vLLM with non-default PyTorch builds (like nightly or a custom build).

To build vLLM using an existing PyTorch installation:

```
# install PyTorch first, either from PyPI or from source
gitclonehttps://github.com/vllm-project/vllm.git
cdvllm
pythonuse_existing_torch.py
uvpipinstall-rrequirements/build/cuda.txt
uvpipinstall--no-build-isolation-e.
```

Alternatively: if you are exclusively using `uv` to create and manage virtual environments, it has [a unique mechanism](https://docs.astral.sh/uv/concepts/projects/config/#disabling-build-isolation) for disabling build isolation for specific packages. vLLM can leverage this mechanism to specify `torch` as the package to disable build isolation for:

```
# install PyTorch first, either from PyPI or from source
gitclonehttps://github.com/vllm-project/vllm.git
cdvllm
# pip install -e . does not work directly, only uv can do this
uvpipinstall-e.
```

##### Use the local cutlass for compilation[¶](#use-the-local-cutlass-for-compilation "Permanent link")

Currently, before starting the build process, vLLM fetches cutlass code from GitHub. However, there may be scenarios where you want to use a local version of cutlass instead. To achieve this, you can set the environment variable VLLM\_CUTLASS\_SRC\_DIR to point to your local cutlass directory.

```
gitclonehttps://github.com/vllm-project/vllm.git
cdvllm
VLLM_CUTLASS_SRC_DIR=/path/to/cutlassuvpipinstall-e.--torch-backend=auto
```

##### Troubleshooting[¶](#troubleshooting "Permanent link")

To avoid your system being overloaded, you can limit the number of compilation jobs to be run simultaneously, via the environment variable `MAX_JOBS`. For example:

```
exportMAX_JOBS=6
uvpipinstall-e.
```

This is especially useful when you are building on less powerful machines. For example, when you use WSL it only [assigns 50% of the total memory by default](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#main-wsl-settings), so using `export MAX_JOBS=1` can avoid compiling multiple files simultaneously and running out of memory. A side effect is a much slower build process.

Additionally, if you have trouble building vLLM, we recommend using the NVIDIA PyTorch Docker image.

```
# Use `--ipc=host` to make sure the shared memory is large enough.
dockerrun\
--gpusall\
-it\
--rm\
--ipc=hostnvcr.io/nvidia/pytorch:23.10-py3
```

If you don't want to use docker, it is recommended to have a full installation of CUDA Toolkit. You can download and install it from [the official website](https://developer.nvidia.com/cuda-toolkit-archive). After installation, set the environment variable `CUDA_HOME` to the installation path of CUDA Toolkit, and make sure that the `nvcc` compiler is in your `PATH`, e.g.:

```
exportCUDA_HOME=/usr/local/cuda
exportPATH="${CUDA_HOME}/bin:$PATH"
```

Here is a sanity check to verify that the CUDA Toolkit is correctly installed:

```
nvcc--version# verify that nvcc is in your PATH
${CUDA_HOME}/bin/nvcc--version# verify that nvcc is in your CUDA_HOME
```

#### Unsupported OS build[¶](#unsupported-os-build "Permanent link")

vLLM can fully run only on Linux but for development purposes, you can still build it on other systems (for example, macOS), allowing for imports and a more convenient development environment. The binaries will not be compiled and won't work on non-Linux systems.

Simply disable the `VLLM_TARGET_DEVICE` environment variable before installing:

```
exportVLLM_TARGET_DEVICE=empty
uvpipinstall-e.
```

Tip

- If you found that the following installation step does not work for you, please refer to [docker/Dockerfile.rocm\_base](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm_base). Dockerfile is a form of installation steps.

<!--THE END-->

1. Install prerequisites (skip if you are already in an environment/docker with the following installed):
   
   - [ROCm](https://rocm.docs.amd.com/en/latest/deploy/linux/index.html)
   - [PyTorch](https://pytorch.org/)
   
   For installing PyTorch, you can start from a fresh docker image, e.g, `rocm/pytorch:rocm7.0_ubuntu22.04_py3.10_pytorch_release_2.8.0`, `rocm/pytorch-nightly`. If you are using docker image, you can skip to Step 3.
   
   Alternatively, you can install PyTorch using PyTorch wheels. You can check PyTorch installation guide in PyTorch [Getting Started](https://pytorch.org/get-started/locally/). Example:
   
   ```
   # Install PyTorch
   pipuninstalltorch-y
   pipinstall--no-cache-dirtorchtorchvision--index-urlhttps://download.pytorch.org/whl/nightly/rocm7.0
   ```
2. Install [Triton for ROCm](https://github.com/ROCm/triton.git)
   
   Install ROCm's Triton following the instructions from [ROCm/triton](https://github.com/ROCm/triton.git)
   
   ```
   python3-mpipinstallninjacmakewheelpybind11
   pipuninstall-ytriton
   gitclonehttps://github.com/ROCm/triton.git
   cdtriton
   # git checkout $TRITON_BRANCH
   gitcheckoutf9e5bf54
   if[!-fsetup.py];thencdpython;fi
   python3setup.pyinstall
   cd../..
   ```
   
   Note
   
   - The validated `$TRITON_BRANCH` can be found in the [docker/Dockerfile.rocm\_base](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm_base).
   - If you see HTTP issue related to downloading packages during building triton, please try again as the HTTP error is intermittent.
3. Optionally, if you choose to use CK flash attention, you can install [flash attention for ROCm](https://github.com/Dao-AILab/flash-attention.git)
   
   Install ROCm's flash attention (v2.8.0) following the instructions from [ROCm/flash-attention](https://github.com/Dao-AILab/flash-attention#amd-rocm-support)
   
   For example, for ROCm 7.0, suppose your gfx arch is `gfx942`. To get your gfx architecture, run `rocminfo |grep gfx`.
   
   ```
   gitclonehttps://github.com/Dao-AILab/flash-attention.git
   cdflash-attention
   # git checkout $FA_BRANCH
   gitcheckout0e60e394
   gitsubmoduleupdate--init
   GPU_ARCHS="gfx942"python3setup.pyinstall
   cd..
   ```
   
   Note
   
   - The validated `$FA_BRANCH` can be found in the [docker/Dockerfile.rocm\_base](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm_base).
4. Optionally, if you choose to build AITER yourself to use a certain branch or commit, you can build AITER using the following steps:
   
   ```
   python3-mpipuninstall-yaiter
   gitclone--recursivehttps://github.com/ROCm/aiter.git
   cdaiter
   gitcheckout$AITER_BRANCH_OR_COMMIT
   gitsubmodulesync;gitsubmoduleupdate--init--recursive
   python3setup.pydevelop
   ```
   
   Note
   
   - You will need to config the `$AITER_BRANCH_OR_COMMIT` for your purpose.
   - The validated `$AITER_BRANCH_OR_COMMIT` can be found in the [docker/Dockerfile.rocm\_base](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm_base).
5. Optionally, if you want to use MORI for EP or PD disaggregation, you can install [MORI](https://github.com/ROCm/mori) using the following steps:
   
   ```
   gitclonehttps://github.com/ROCm/mori.git
   cdmori
   gitcheckout$MORI_BRANCH_OR_COMMIT
   gitsubmodulesync;gitsubmoduleupdate--init--recursive
   MORI_GPU_ARCHS="gfx942;gfx950"python3setup.pyinstall
   ```
   
   Note
   
   - You will need to config the `$MORI_BRANCH_OR_COMMIT` for your purpose.
   - The validated `$MORI_BRANCH_OR_COMMIT` can be found in the [docker/Dockerfile.rocm\_base](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm_base).
6. Build vLLM. For example, vLLM on ROCM 7.0 can be built with the following steps:
   
   Commands
   
   ```
   pipinstall--upgradepip
   
   # Build & install AMD SMI
   pipinstall/opt/rocm/share/amd_smi
   
   # Install dependencies
   pipinstall--upgradenumba\
   scipy\
   huggingface-hub[cli]\
   setuptools_scm
   pipinstall-rrequirements/rocm.txt
   
   # To build for a single architecture (e.g., MI300) for faster installation (recommended):
   exportPYTORCH_ROCM_ARCH="gfx942"
   
   # To build vLLM for multiple arch MI210/MI250/MI300, use this instead
   # export PYTORCH_ROCM_ARCH="gfx90a;gfx942"
   
   python3setup.pydevelop
   ```
   
   This may take 5-10 minutes. Currently, `pip install .` does not work for ROCm when installing vLLM from source.
   
   Tip
   
   - The ROCm version of PyTorch, ideally, should match the ROCm driver version.

Tip

- For MI300x (gfx942) users, to achieve optimal performance, please refer to [MI300x tuning guide](https://rocm.docs.amd.com/en/latest/how-to/tuning-guides/mi300x/index.html) for performance optimization and tuning tips on system and workflow level. For vLLM, please refer to [vLLM performance optimization](https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference-optimization/vllm-optimization.html).

<!--THE END-->

- First, install required [driver](https://dgpu-docs.intel.com/driver/installation.html#installing-gpu-drivers).
- Second, install Python packages for vLLM XPU backend building (Intel OneAPI dependencies are installed automatically as part of `torch-xpu`, see [PyTorch XPU get started](https://docs.pytorch.org/docs/stable/notes/get_start_xpu.html)):

```
gitclonehttps://github.com/vllm-project/vllm.git
cdvllm
pipinstall--upgradepip
pipinstall-v-rrequirements/xpu.txt
```

- Then, install the correct Triton package for Intel XPU.
  
  The default `triton` package (for NVIDIA GPUs) may be installed as a transitive dependency (e.g., via `xgrammar`). For Intel XPU, you must replace it with `triton-xpu`:
  
  ```
  pipuninstall-ytritontriton-xpu
  pipinstalltriton-xpu==3.6.0--extra-index-urlhttps://download.pytorch.org/whl/xpu
  ```
  
  Note
  
  - `triton` (without suffix) is for NVIDIA GPUs only. On XPU, using it instead of `triton-xpu` can cause correctness or runtime issues.
  - For torch 2.11 (the version used in `requirements/xpu.txt`), the matching package is `triton-xpu==3.7.0`. If you use a different version of torch, check the corresponding `triton-xpu` version in [docker/Dockerfile.xpu](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.xpu).
- Finally, build and install vLLM XPU backend:

```
VLLM_TARGET_DEVICE=xpupipinstall--no-build-isolation-e.-v
```