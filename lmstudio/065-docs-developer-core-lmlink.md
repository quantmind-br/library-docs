---
title: Using LM Link
url: https://lmstudio.ai/docs/developer/core/lmlink
source: sitemap
fetched_at: 2026-04-07T21:29:58.728772554-03:00
rendered_js: false
word_count: 181
summary: This document explains how LM Link allows users to interact with remote models as if they were loaded locally via the REST API and SDK, maintaining normal local usage patterns.
tags:
    - lm-link
    - rest-api
    - remote-models
    - local-access
    - network-connection
category: guide
---

## Overview[](#overview "Link to 'Overview'")

With [LM Link](https://lmstudio.ai/docs/lmlink), you can use a model loaded on a remote device as if it were loaded locally — from any machine on the same link. This naturally extends to the REST API and SDK: your laptop can make requests to `localhost` and have them served by a powerful remote machine on your network.

Requests to `localhost` still work as normal. LM Studio internally uses the model on the remote device as if it were loaded locally. For models present on multiple devices, the REST API will use the model on the preferred device.

![undefined](https://lmstudio.ai/assets/docs/rest-link-diagram.png)

Sequence diagram: REST API request routed through LM Link to a remote device

The preferred device setting is per-machine. Each device on the link independently controls which remote machine it prefers. See [how to set a preferred device](https://lmstudio.ai/docs/lmlink/basics/preferred-device) for more details.

## Use the REST API as normal[](#use-the-rest-api-as-normal "Link to 'Use the REST API as normal'")

Use the REST API exactly as you would locally. See the [REST API docs](https://lmstudio.ai/docs/developer/rest) for usage details.

If you're running into trouble, hop onto our [Discord](https://discord.gg/lmstudio)