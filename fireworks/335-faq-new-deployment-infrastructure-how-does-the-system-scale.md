---
title: How does the system scale?
url: https://docs.fireworks.ai/faq-new/deployment-infrastructure/how-does-the-system-scale
source: sitemap
fetched_at: 2026-04-27T20:13:02.063471343-03:00
rendered_js: false
word_count: 50
summary: Fireworks scales horizontally by adding deployment replicas, with automatic resource allocation based on demand.
tags:
    - scalability
    - horizontal-scaling
    - deployment
category: faq
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Fireworks is **horizontally scalable**:

- Scales linearly with additional **replicas** of the deployment
- **Automatically allocates resources** based on demand
- Efficient **distributed load handling** across replicas

> [!tip]
> Increase replica count to handle more concurrent requests. See [[031-deployments-routers|Routers]] and [[028-deployments-direct-routing|Direct Routing]] for traffic distribution options.

#scalability #horizontal-scaling #deployment