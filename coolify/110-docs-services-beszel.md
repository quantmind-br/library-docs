---
title: Beszel
url: https://coolify.io/docs/services/beszel.md
source: llms
fetched_at: 2026-02-17T14:42:25.517084-03:00
rendered_js: false
word_count: 81
summary: This document explains how to deploy and configure Beszel, a lightweight server monitoring hub, specifically using Coolify templates and environment variables.
tags:
    - server-monitoring
    - beszel
    - coolify
    - deployment
    - docker-stats
    - alerting
category: guide
---

## What is Beszel?

Lightweight server monitoring hub with historical data, docker stats, and alerts.

## Setup

* Deploy Beszel using Coolify template
* In the UI, `Add a new System`
* Enter `beszel-agent` in Host/IP
* Copy the public Key to `KEY` env variable and token to `TOKEN` variable in Beszel's project environment variables (These are obtained from Beszel UI when adding a new system)
* Disable the gzip compression in the hub service settings. ( it's handled by Coolify automatically after the version v4.0.0-beta.452)

## Links

* [GitHub](https://github.com/henrygd/beszel)