---
title: Using Nginx - vLLM
url: https://docs.vllm.ai/en/latest/deployment/nginx/
source: sitemap
fetched_at: 2026-05-07T21:11:34.875792434-03:00
rendered_js: false
word_count: 272
summary: This document provides instructions on how to set up and deploy multiple vLLM serving containers load-balanced by an Nginx reverse proxy using Docker.
tags:
    - vllm
    - nginx
    - load-balancing
    - docker-deployment
    - containerization
    - server-infrastructure
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/deployment/nginx.md "Edit this page")

This document shows how to launch multiple vLLM serving containers and use Nginx to act as a load balancer between the servers.

## Build Nginx Container[¶](#build-nginx-container "Permanent link")

This guide assumes that you have just cloned the vLLM project and you're currently in the vllm root directory.

Create a file named `Dockerfile.nginx`:

```
FROMnginx:latest
RUNrm/etc/nginx/conf.d/default.conf
EXPOSE80
CMD["nginx","-g","daemon off;"]
```

Build the container:

```
dockerbuild.-fDockerfile.nginx--tagnginx-lb
```

## Create Simple Nginx Config file[¶](#create-simple-nginx-config-file "Permanent link")

Create a file named `nginx_conf/nginx.conf`. Note that you can add as many servers as you'd like. In the below example we'll start with two. To add more, add another `server vllmN:8000 max_fails=3 fail_timeout=10000s;` entry to `upstream backend`.

Config

```
upstream backend {
    least_conn;
    server vllm0:8000 max_fails=3 fail_timeout=10000s;
    server vllm1:8000 max_fails=3 fail_timeout=10000s;
}
server {
    listen 80;
    location / {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## Build vLLM Container[¶](#build-vllm-container "Permanent link")

```
cd$vllm_root
dockerbuild-fdocker/Dockerfile.--tagvllm
```

If you are behind proxy, you can pass the proxy settings to the docker build command as shown below:

```
cd$vllm_root
dockerbuild\
-fdocker/Dockerfile.\
--tagvllm\
--build-arghttp_proxy=$http_proxy\
--build-arghttps_proxy=$https_proxy
```

## Create Docker Network[¶](#create-docker-network "Permanent link")

```
dockernetworkcreatevllm_nginx
```

## Launch vLLM Containers[¶](#launch-vllm-containers "Permanent link")

Notes:

- If you have your HuggingFace models cached somewhere else, update `hf_cache_dir` below.
- If you don't have an existing HuggingFace cache you will want to start `vllm0` and wait for the model to complete downloading and the server to be ready. This will ensure that `vllm1` can leverage the model you just downloaded and it won't have to be downloaded again.
- The below example assumes GPU backend used. If you are using CPU backend, remove `--gpus device=ID`, add `VLLM_CPU_KVCACHE_SPACE` and `VLLM_CPU_OMP_THREADS_BIND` environment variables to the docker run command.
- Adjust the model name that you want to use in your vLLM servers if you don't want to use `Llama-2-7b-chat-hf`.

Commands

```
mkdir -p ~/.cache/huggingface/hub/
hf_cache_dir=~/.cache/huggingface/
docker run \
    -itd \
    --ipc host \
    --network vllm_nginx \
    --gpus device=0 \
    --shm-size=10.24gb \
    -v $hf_cache_dir:/root/.cache/huggingface/ \
    -p 8081:8000 \
    --name vllm0 vllm \
    --model meta-llama/Llama-2-7b-chat-hf
docker run \
    -itd \
    --ipc host \
    --network vllm_nginx \
    --gpus device=1 \
    --shm-size=10.24gb \
    -v $hf_cache_dir:/root/.cache/huggingface/ \
    -p 8082:8000 \
    --name vllm1 vllm \
    --model meta-llama/Llama-2-7b-chat-hf
```

Note

If you are behind proxy, you can pass the proxy settings to the docker run command via `-e http_proxy=$http_proxy -e https_proxy=$https_proxy`.

## Launch Nginx[¶](#launch-nginx "Permanent link")

```
dockerrun\
-itd\
-p8000:80\
--networkvllm_nginx\
-v./nginx_conf/:/etc/nginx/conf.d/\
--namenginx-lbnginx-lb:latest
```

## Verify That vLLM Servers Are Ready[¶](#verify-that-vllm-servers-are-ready "Permanent link")

```
dockerlogsvllm0|grepUvicorn
dockerlogsvllm1|grepUvicorn
```

Both outputs should look like this:

```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```