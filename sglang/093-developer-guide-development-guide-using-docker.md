---
title: Development Guide Using Docker — SGLang
url: https://docs.sglang.io/developer_guide/development_guide_using_docker.html#setup-docker-container
source: crawler
fetched_at: 2026-02-04T08:47:33.415842239-03:00
rendered_js: false
word_count: 530
summary: This document provides a comprehensive guide for setting up an SGLang development environment using Docker and VSCode, covering remote tunnels, dev containers, and debugging configurations.
tags:
    - sglang
    - docker
    - vscode
    - dev-containers
    - remote-development
    - debugging
    - profiling
category: guide
---

## Contents

## Development Guide Using Docker[#](#development-guide-using-docker "Link to this heading")

## Setup VSCode on a Remote Host[#](#setup-vscode-on-a-remote-host "Link to this heading")

(Optional - you can skip this step if you plan to run sglang dev container locally)

1. In the remote host, download `code` from [Https://code.visualstudio.com/docs/?dv=linux64cli](https://code.visualstudio.com/download) and run `code tunnel` in a shell.

Example

```
wgethttps://vscode.download.prss.microsoft.com/dbazure/download/stable/fabdb6a30b49f79a7aba0f2ad9df9b399473380f/vscode_cli_alpine_x64_cli.tar.gz
tarxfvscode_cli_alpine_x64_cli.tar.gz

# https://code.visualstudio.com/docs/remote/tunnels
./codetunnel
```

2. In your local machine, press F1 in VSCode and choose “Remote Tunnels: Connect to Tunnel”.

## Setup Docker Container[#](#setup-docker-container "Link to this heading")

### Option 1. Use the default dev container automatically from VSCode[#](#option-1-use-the-default-dev-container-automatically-from-vscode "Link to this heading")

There is a `.devcontainer` folder in the sglang repository root folder to allow VSCode to automatically start up within dev container. You can read more about this VSCode extension in VSCode official document [Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers). ![image](https://github.com/user-attachments/assets/6a245da8-2d4d-4ea8-8db1-5a05b3a66f6d) (*Figure 1: Diagram from VSCode official documentation [Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers).*)

To enable this, you only need to:

1. Start Visual Studio Code and install [VSCode dev container extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
2. Press F1, type and choose “Dev Container: Open Folder in Container.
3. Input the `sglang` local repo path in your machine and press enter.

The first time you open it in dev container might take longer due to docker pull and build. Once it’s successful, you should set on your status bar at the bottom left displaying that you are in a dev container:

![image](https://github.com/user-attachments/assets/650bba0b-c023-455f-91f9-ab357340106b)

Now when you run `sglang.launch_server` in the VSCode terminal or start debugging using F5, sglang server will be started in the dev container with all your local changes applied automatically:

![image](https://github.com/user-attachments/assets/748c85ba-7f8c-465e-8599-2bf7a8dde895)

### Option 2. Start up containers manually (advanced)[#](#option-2-start-up-containers-manually-advanced "Link to this heading")

The following startup command is an example for internal development by the SGLang team. You can **modify or add directory mappings as needed**, especially for model weight downloads, to prevent repeated downloads by different Docker containers.

❗️ **Note on RDMA**

```
1. `--network host` and `--privileged` are required by RDMA. If you don't need RDMA, you can remove them but keeping them there does not harm. Thus, we enable these two flags by default in the commands below.
2. You may need to set `NCCL_IB_GID_INDEX` if you are using RoCE, for example: `export NCCL_IB_GID_INDEX=3`.
```

```
# Change the name to yours
dockerrun-itd--shm-size32g--gpusall-v<volumes-to-mount>--ipc=host--network=host--privileged--namesglang_devlmsysorg/sglang:dev/bin/zsh
dockerexec-itsglang_dev/bin/zsh
```

Some useful volumes to mount are:

1. **Huggingface model cache**: mounting model cache can avoid re-download every time docker restarts. Default location on Linux is `~/.cache/huggingface/`.
2. **SGLang repository**: code changes in the SGLang local repository will be automatically synced to the .devcontainer.

Example 1: Monting local cache folder `/opt/dlami/nvme/.cache` but not the SGLang repo. Use this when you prefer to manually transfer local code changes to the devcontainer.

```
dockerrun-itd--shm-size32g--gpusall-v/opt/dlami/nvme/.cache:/root/.cache--ipc=host--network=host--privileged--namesglang_zhyncslmsysorg/sglang:dev/bin/zsh
dockerexec-itsglang_zhyncs/bin/zsh
```

Example 2: Mounting both HuggingFace cache and local SGLang repo. Local code changes are automatically synced to the devcontainer as the SGLang is installed in editable mode in the dev image.

```
dockerrun-itd--shm-size32g--gpusall-v$HOME/.cache/huggingface/:/root/.cache/huggingface-v$HOME/src/sglang:/sgl-workspace/sglang--ipc=host--network=host--privileged--namesglang_zhyncslmsysorg/sglang:dev/bin/zsh
dockerexec-itsglang_zhyncs/bin/zsh
```

## Debug SGLang with VSCode Debugger[#](#debug-sglang-with-vscode-debugger "Link to this heading")

1. (Create if not exist) open `launch.json` in VSCode.
2. Add the following config and save. Please note that you can edit the script as needed to apply different parameters or debug a different program (e.g. benchmark script).
   
   ```
   {
   "version":"0.2.0",
   "configurations":[
   {
   "name":"Python Debugger: launch_server",
   "type":"debugpy",
   "request":"launch",
   "module":"sglang.launch_server",
   "console":"integratedTerminal",
   "args":[
   "--model-path","meta-llama/Llama-3.2-1B",
   "--host","0.0.0.0",
   "--port","30000",
   "--trust-remote-code",
   ],
   "justMyCode":false
   }
   ]
   }
   ```
3. Press “F5” to start. VSCode debugger will ensure that the program will pause at the breakpoints even if the program is running at remote SSH/Tunnel host + dev container.

## Profile[#](#profile "Link to this heading")

```
# Change batch size, input, output and add `disable-cuda-graph` (for easier analysis)
# e.g. DeepSeek V3
nsysprofile-odeepseek_v3python3-msglang.bench_one_batch--batch-size1--input128--output256--modeldeepseek-ai/DeepSeek-V3--trust-remote-code--tp8--disable-cuda-graph
```

## Evaluation[#](#evaluation "Link to this heading")

```
# e.g. gsm8k 8 shot
python3benchmark/gsm8k/bench_sglang.py--num-questions2000--parallel2000--num-shots8
```