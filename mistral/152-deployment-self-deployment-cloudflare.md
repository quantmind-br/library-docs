---
title: Cloudflare Workers AI | Mistral Docs
url: https://docs.mistral.ai/deployment/self-deployment/cloudflare
source: crawler
fetched_at: 2026-01-29T07:34:18.556389655-03:00
rendered_js: false
word_count: 108
summary: A guide on integrating and running Mistral AI models within the Cloudflare Workers AI serverless execution environment.
tags:
    - Cloudflare Workers
    - Mistral AI
    - Serverless
    - AI Deployment
    - LLM
category: guide
---

## Deploy with Cloudflare Workers AI

[Cloudflare](https://www.cloudflare.com/en-gb/) is a web performance and security company that provides content delivery network (CDN), DDoS protection, Internet security, and distributed domain name server services. Cloudflare launched Workers AI, which allows developers to run LLM models powered by serverless GPUs on Cloudflare’s global network.

To learn more about Mistral models on Workers AI, you can read the dedicated [Cloudflare documentation page](https://developers.cloudflare.com/workers-ai/models/mistral-7b-instruct-v0.1/).

To set up Workers AI on Cloudflare, you need to create an account on the [Cloudflare dashboard](https://dash.cloudflare.com/), get your account ID, and generate a token with Workers AI permissions. You can then send a completion request:

Here is the output you should receive: