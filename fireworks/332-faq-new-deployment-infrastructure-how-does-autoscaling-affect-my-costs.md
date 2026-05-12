---
title: How does autoscaling affect my costs? - Fireworks AI Docs
url: https://docs.fireworks.ai/faq-new/deployment-infrastructure/how-does-autoscaling-affect-my-costs
source: sitemap
fetched_at: 2026-04-27T20:13:02.160823717-03:00
rendered_js: false
word_count: 82
summary: Explains how autoscaling impacts costs — zero minimum cost when scaled to zero, and proportional GPU cost increases when scaling up.
tags:
    - deployment
    - autoscaling
    - costs
    - gpu
    - pricing
category: faq
optimized: true
optimized_at: 2026-04-27T20:20:00Z
---
Autoscaling affects your costs in two ways:

- **Scaling from 0**: No minimum cost when scaled to zero
- **Scaling up**: Each new replica adds to your total cost proportionally. For example:
  - Scaling from 1 to 2 replicas doubles your GPU costs
  - If each replica uses multiple GPUs, costs scale accordingly (e.g., scaling from 1 to 2 replicas with 2 GPUs each means paying for 4 GPUs total)

For current pricing details, visit our [pricing page](https://fireworks.ai/pricing).

#autoscaling #costs #gpu #deployment
