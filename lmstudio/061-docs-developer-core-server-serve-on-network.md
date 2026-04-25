---
title: Serve on Local Network
url: https://lmstudio.ai/docs/developer/core/server/serve-on-network
source: sitemap
fetched_at: 2026-04-07T21:30:08.929304677-03:00
rendered_js: false
word_count: 126
summary: This document explains how enabling the "Serve on Local Network" option makes the LM Studio API server accessible to other devices connected to the same local network.
tags:
    - lm-studio
    - local-network
    - api-server
    - llm-access
    - networking
category: guide
---

Enabling the "Serve on Local Network" option allows the LM Studio API server running on your machine to be accessible by other devices connected to the same local network.

This is useful for scenarios where you want to:

- Use a local LLM on your other less powerful devices by connecting them to a more powerful machine running LM Studio.
- Let multiple people use a single LM Studio instance on the network.
- Use the API from IoT devices, edge computing units, or other services in your local setup.

Once enabled, the server will bind to your local network IP address instead of localhost. The API access URL will be updated accordingly which you can use in your applications.

![undefined](https://lmstudio.ai/assets/docs/serve-local-network.png)

Serve LM Studio API Server on Local Network