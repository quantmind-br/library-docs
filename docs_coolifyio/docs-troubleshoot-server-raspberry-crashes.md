---
title: Raspberry Pi Crashes
url: https://coolify.io/docs/troubleshoot/server/raspberry-crashes.md
source: llms
fetched_at: 2026-02-17T14:41:53.981152-03:00
rendered_js: false
word_count: 69
summary: This document provides troubleshooting steps and configuration solutions for Raspberry Pi system crashes caused by memory limitations. It outlines hardware upgrade options and specific Docker configuration settings to limit resource usage for improved stability.
tags:
    - raspberry-pi
    - docker
    - memory-management
    - troubleshooting
    - system-stability
    - resource-allocation
category: guide
---

# Raspberry Pi Crashes

If you're using a Raspberry Pi with only 2GB of RAM, you may experience system crashes even with swap space enabled.

This is likely due to the slower SD cards often used in Raspberry Pis, which can be unstable.

## Solution

* Upgrade to a Raspberry Pi with 4GB+ of RAM for better stability.
* Or, limit Docker’s memory usage by adding the following configuration to your `/etc/docker/daemon.json` file:
  ```json
  {
  "memory": "1.8g"
  }
  ```