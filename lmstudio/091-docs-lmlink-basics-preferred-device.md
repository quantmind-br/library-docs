---
title: Set a preferred device
url: https://lmstudio.ai/docs/lmlink/basics/preferred-device
source: sitemap
fetched_at: 2026-04-07T21:27:41.548183084-03:00
rendered_js: false
word_count: 110
summary: This document explains how to set a preferred remote device for accessing models via LM Link, detailing separate procedures for GUI-based and terminal-based machines.
tags:
    - lm-link
    - preferred-device
    - remote-models
    - sdk-api
    - machine-settings
category: guide
---

## Choosing a preferred device[](#choosing-a-preferred-device "Link to 'Choosing a preferred device'")

When the same model is available on multiple devices in the link, LM Link uses the preferred device to load and use the model. This setting is per-machine: each device on the link independently controls which remote machine it prefers.

This is especially relevant when accessing remote models via the SDK or [REST API](https://lmstudio.ai/docs/developer/core/lmlink).

### Machines with GUI[](#machines-with-gui)

In the app, head to the LM Link page, select the device and toggle the "Set as preferred device" option.

![undefined](https://lmstudio.ai/assets/docs/lmlink-preferred.png)

Set a device as your preferred device

### Machines without GUI[](#machines-without-gui)

To set a preferred device from the terminal, use the following command:

```

lms link set-preferred-device
```