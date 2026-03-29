---
title: README
url: https://github.com/kholia/OSX-KVM/blob/master/resources/README.md
source: git
fetched_at: 2026-02-04T11:39:06.253040654-03:00
rendered_js: false
word_count: 29
summary: This document provides instructions for using the idadif.py script to apply a differential patch file to the macOS kernel binary.
tags:
    - macos-kernel
    - binary-patching
    - idadif-py
    - kernel-patching
    - system-modification
category: guide
---

Use `idadif.py` to apply the `kernel.dif` patch to the macOS `kernel` binary.


```
$ sha256sum kernel*
be90edb9653be25e1747cefc1ec9fd452b90dd917ba9eb391a76f260f84cd9f0  kernel <-- patched 10.15.4 kernel
ac2fc51e53519a3147359e2b25dd8aa6b1fa79d41f92091cc058b2aab7e901d6  kernel.bak <-- original 10.15.4 kernel
```
