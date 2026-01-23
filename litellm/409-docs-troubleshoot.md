---
title: Troubleshooting & Support | liteLLM
url: https://docs.litellm.ai/docs/troubleshoot
source: sitemap
fetched_at: 2026-01-21T19:54:55.610303516-03:00
rendered_js: false
word_count: 244
summary: This document outlines the specific information required to effectively report issues with LiteLLM and lists available support channels for technical assistance.
tags:
    - troubleshooting
    - issue-reporting
    - debugging
    - customer-support
    - litellm-configuration
    - error-logs
category: guide
---

## Information to Provide When Seeking Help[​](#information-to-provide-when-seeking-help "Direct link to Information to Provide When Seeking Help")

When reporting issues, please include as much of the following as possible. It's okay if you can't provide everything—especially in production scenarios where the trigger might be unknown. Sharing most of this information will help us assist you more effectively.

### 1. LiteLLM Configuration File[​](#1-litellm-configuration-file "Direct link to 1. LiteLLM Configuration File")

Your `config.yaml` file (redact sensitive info like API keys). Include number of workers if not in config.

### 2. Initialization Command[​](#2-initialization-command "Direct link to 2. Initialization Command")

The command used to start LiteLLM (e.g., `litellm --config config.yaml --num_workers 8 --detailed_debug`).

### 3. LiteLLM Version[​](#3-litellm-version "Direct link to 3. LiteLLM Version")

- Current version
- Version when the issue first appeared (if different)
- If upgraded, the version changed from → to

### 4. Environment Variables[​](#4-environment-variables "Direct link to 4. Environment Variables")

Non-sensitive environment variables not in your config (e.g., `NUM_WORKERS`, `LITELLM_LOG`, `LITELLM_MODE`). Do not include passwords or API keys.

### 5. Server Specifications[​](#5-server-specifications "Direct link to 5. Server Specifications")

CPU cores, RAM, OS, number of instances/replicas, etc.

### 6. Database and Redis Usage[​](#6-database-and-redis-usage "Direct link to 6. Database and Redis Usage")

- **Database:** Using database? (`DATABASE_URL` set), database type and version
- **Redis:** Using Redis? Redis version, configuration type (Standalone/Cluster/Sentinel).

### 7. Endpoints[​](#7-endpoints "Direct link to 7. Endpoints")

The endpoint(s) you're using that are experiencing issues (e.g., `/chat/completions`, `/embeddings`).

### 8. Request Example[​](#8-request-example "Direct link to 8. Request Example")

A realistic example of the request causing issues, including expected vs. actual response and any error messages.

### 9. Error Logs, Stack Traces, and Metrics[​](#9-error-logs-stack-traces-and-metrics "Direct link to 9. Error Logs, Stack Traces, and Metrics")

Full error logs, stack traces, and any images from service metrics (CPU, memory, request rates, etc.) that might help diagnose the issue.

* * *

## Support Channels[​](#support-channels "Direct link to Support Channels")

[Schedule Demo 👋](https://calendly.com/d/4mp-gd3-k5k/berriai-1-1-onboarding-litellm-hosted-version)

[Community Discord 💭](https://discord.gg/wuPM9dRgDw) [Community Slack 💭](https://www.litellm.ai/support)

Our numbers 📞 +1 (770) 8783-106 / +1 (412) 618-6238

Our emails ✉️ [ishaan@berri.ai](mailto:ishaan@berri.ai) / [krrish@berri.ai](mailto:krrish@berri.ai)

[![Chat on WhatsApp](https://img.shields.io/static/v1?label=Chat%20on&message=WhatsApp&color=success&logo=WhatsApp&style=flat-square)](https://wa.link/huol9n) [![Chat on Discord](https://img.shields.io/static/v1?label=Chat%20on&message=Discord&color=blue&logo=Discord&style=flat-square)](https://discord.gg/wuPM9dRgDw)