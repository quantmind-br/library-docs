---
title: Mindspore backend - SGLang Documentation
url: https://docs.sglang.io/docs/hardware-platforms/ascend-npus/mindspore_backend
source: sitemap
fetched_at: 2026-05-11T05:48:39.105695626-03:00
rendered_js: false
word_count: 222
summary: This document provides instructions for deploying and running supported AI models using the MindSpore backend within the SGLang framework on Ascend NPU hardware.
tags:
    - mindspore
    - sglang
    - ascend-npu
    - model-deployment
    - offline-inference
    - distributed-serving
    - troubleshooting
category: guide
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

## Introduction

MindSpore is a high-performance AI framework optimized for Ascend NPUs. This doc guides users to run MindSpore models in SGLang.

## Requirements

MindSpore currently only supports Ascend NPU devices. Users need to first install Ascend CANN software packages. The CANN software packages can be downloaded from the [Ascend Official Website](https://www.hiascend.com). The recommended version is 8.3.RC2.

## Supported Models

Currently, the following models are supported:

- **Qwen3**: Dense and MoE models
- **DeepSeek V3/R1**
- *More models coming soon…*

## Installation

## Run Model

Current SGLang-MindSpore supports Qwen3 and DeepSeek V3/R1 models. This doc uses Qwen3-8B as an example.

### Offline infer

Use the following script for offline infer:

### Start server

Launch a server with MindSpore backend:

For distributed server with multiple nodes:

## Troubleshooting

#### Debug Mode

Enable sglang debug logging by log-level argument.

Enable mindspore info and debug logging by setting environments.

#### Explicitly select devices

Use the following environment variable to explicitly select the devices to use.

#### Some communication environment issues

In case of some environment with special communication environment, users need set some environment variables.

#### Some dependencies of protobuf

In case of some environment with special protobuf version, users need set some environment variables to avoid binary version mismatch.

## Support

For MindSpore-specific issues:

- Refer to the [MindSpore documentation](https://www.mindspore.cn/)