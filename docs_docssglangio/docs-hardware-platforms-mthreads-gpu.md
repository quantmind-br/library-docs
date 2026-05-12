---
title: Moore Threads GPUs - SGLang Documentation
url: https://docs.sglang.io/docs/hardware-platforms/mthreads_gpu
source: sitemap
fetched_at: 2026-05-11T05:48:26.928452037-03:00
rendered_js: false
word_count: 62
summary: This document provides instructions for installing the SGLang framework specifically for Moore Threads GPU hardware environments.
tags:
    - sglang
    - installation
    - gpu-acceleration
    - moore-threads
    - musa
    - source-installation
category: guide
---

- [Install SGLang](#install-sglang)
- [Install from Source](#install-from-source)

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

This document describes how run SGLang on Moore Threads GPUs. If you encounter issues or have questions, please [open an issue](https://github.com/sgl-project/sglang/issues).

## Install SGLang

You can install SGLang using one of the methods below.

### Install from Source

```
# Use the default branch
git clone https://github.com/sgl-project/sglang.git
cd sglang

# Compile sgl-kernel
pip install --upgrade pip
cd sgl-kernel
python setup_musa.py install

# Install sglang python package
cd ..
rm -f python/pyproject.toml && mv python/pyproject_other.toml python/pyproject.toml
pip install -e "python[all_musa]"
```