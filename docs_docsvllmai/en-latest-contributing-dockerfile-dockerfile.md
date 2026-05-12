---
title: Dockerfile - vLLM
url: https://docs.vllm.ai/en/latest/contributing/dockerfile/dockerfile/
source: sitemap
fetched_at: 2026-05-07T21:11:25.664706305-03:00
rendered_js: false
word_count: 164
summary: This document describes the structure of the vLLM Dockerfile and provides instructions for generating a visual dependency graph of its multi-stage build process.
tags:
    - docker
    - dockerfile
    - vllm
    - containerization
    - dependency-graph
    - deployment
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/contributing/dockerfile/dockerfile.md "Edit this page")

We provide a [docker/Dockerfile](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile) to construct the image for running an OpenAI compatible server with vLLM. More information about deploying with Docker can be found [here](https://docs.vllm.ai/en/latest/deployment/docker/).

Below is a visual representation of the multi-stage Dockerfile. The build graph contains the following nodes:

- All build stages
- The default build target (highlighted in grey)
- External images (with dashed borders)

The edges of the build graph represent:

- `FROM ...` dependencies (with a solid line and a full arrow head)
- `COPY --from=...` dependencies (with a dashed line and an empty arrow head)
- `RUN --mount=(.\*)from=...` dependencies (with a dotted line and an empty diamond arrow head)

> [![query](https://docs.vllm.ai/en/latest/assets/contributing/dockerfile-stages-dependency.png)](https://docs.vllm.ai/en/latest/assets/contributing/dockerfile-stages-dependency.png)
> 
> Made using: [https://github.com/patrickhoefler/dockerfilegraph](https://github.com/patrickhoefler/dockerfilegraph)
> 
> Commands to regenerate the build graph (make sure to run it **from the \`root\` directory of the vLLM repository** where the dockerfile is present):
> 
> ```
> dockerfilegraph\
-opng\
--legend\
--dpi200\
--max-label-length50\
--filenamedocker/Dockerfile
> ```
> 
> or in case you want to run it directly with the docker image:
> 
> ```
> dockerrun\
--rm\
--user"$(id-u):$(id-g)"\
--workdir/workspace\
--volume"$(pwd)":/workspace\
ghcr.io/patrickhoefler/dockerfilegraph:alpine\
--outputpng\
--dpi200\
--max-label-length50\
--filenamedocker/Dockerfile\
--legend
> ```
> 
> (To run it for a different file, you can pass in a different argument to the flag `--filename`.)