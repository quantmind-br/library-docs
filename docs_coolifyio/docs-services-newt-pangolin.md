---
title: Newt-Pangolin
url: https://coolify.io/docs/services/newt-pangolin.md
source: llms
fetched_at: 2026-02-17T14:46:20.944059-03:00
rendered_js: false
word_count: 91
summary: Newt is a user space WireGuard tunnel client and proxy service designed to securely expose private resources managed by Pangolin. This document defines the service's purpose and its required environment configuration.
tags:
    - wireguard
    - tunneling
    - proxy-service
    - pangolin
    - networking-tool
    - user-space
category: reference
---

![Newt Pangolin](/public/images/services/pangolin_newt.svg)

## What is Newt?

Newt is a fully user space WireGuard tunnel client and TCP/UDP proxy, designed to securely expose private resources controlled by Pangolin. By using Newt, you don't need to manage complex WireGuard tunnels and NATing.

## Env Variables

| Name              | Description | Required | Default Value |
| ----------------- | ----------- | -------- | ------------- |
| NEWT ID           | -           | yes      |
| NEWT SECRET       | -           | yes      |
| PANGOLIN ENDPOINT | -           | yes      | domain.tld    |

## Links

* [The official website](https://docs.fossorial.io/Newt/overview?utm_source=coolify.io)
* [GitHub](https://github.com/fosrl/newt?utm_source=coolify.io)