---
title: Installation - vLLM
url: https://docs.vllm.ai/en/latest/getting_started/installation/
source: sitemap
fetched_at: 2026-05-07T21:14:45.777248384-03:00
rendered_js: false
word_count: 78
summary: This document provides an overview of supported hardware platforms and architectures for the vLLM project, including GPU and CPU compatibility. It also outlines the process for integrating third-party hardware via the plugin system.
tags:
    - vllm
    - hardware-compatibility
    - gpu-support
    - cpu-support
    - plugin-system
    - installation-guide
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/getting_started/installation/README.md "Edit this page")

vLLM supports the following hardware platforms:

- [GPU](https://docs.vllm.ai/en/latest/getting_started/installation/gpu/)
  
  - [NVIDIA CUDA](https://docs.vllm.ai/en/latest/getting_started/installation/gpu/#nvidia-cuda)
  - [AMD ROCm](https://docs.vllm.ai/en/latest/getting_started/installation/gpu/#amd-rocm)
  - [Intel XPU](https://docs.vllm.ai/en/latest/getting_started/installation/gpu/#intel-xpu)
- [CPU](https://docs.vllm.ai/en/latest/getting_started/installation/cpu/)
  
  - [Intel/AMD x86](https://docs.vllm.ai/en/latest/getting_started/installation/cpu/#intelamd-x86)
  - [ARM AArch64](https://docs.vllm.ai/en/latest/getting_started/installation/cpu/#arm-aarch64)
  - [Apple silicon](https://docs.vllm.ai/en/latest/getting_started/installation/cpu/#apple-silicon)
  - [IBM Z (S390X)](https://docs.vllm.ai/en/latest/getting_started/installation/cpu/#ibm-z-s390x)

## Hardware Plugins[¶](#hardware-plugins "Permanent link")

vLLM supports third-party hardware plugins that live **outside** the main `vllm` repository. These follow the [Hardware-Pluggable RFC](https://docs.vllm.ai/en/latest/design/plugin_system/).

A list of all supported hardware can be found on the vLLM website, see [Universal Compatibility - Hardware](https://vllm.ai/#compatibility).

If you want to add new hardware, please contact us on [Slack](https://slack.vllm.ai/) or [Email](https://docs.vllm.ai/cdn-cgi/l/email-protection#1e7d7172727f7c716c7f6a7771705e68727273307f77).