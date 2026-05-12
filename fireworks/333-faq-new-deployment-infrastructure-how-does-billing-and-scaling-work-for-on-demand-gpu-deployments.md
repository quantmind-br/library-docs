---
title: How does billing and scaling work for on-demand GPU deployments?
url: https://docs.fireworks.ai/faq-new/deployment-infrastructure/how-does-billing-and-scaling-work-for-on-demand-gpu-deployments
source: sitemap
fetched_at: 2026-04-27T20:13:03.32445549-03:00
rendered_js: false
word_count: 131
summary: On-demand GPU deployments bill per GPU-second from first request, support autoscaling from 0 to multiple GPUs, and require manual deletion unless autoscaling to zero is configured.
tags:
    - gpu-deployment
    - on-demand
    - billing
    - autoscaling
category: faq
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
## Billing

- Charges **start when the server begins accepting requests**
- **Billed by GPU-second** per active instance
- Costs accumulate even with **no active API calls**

## Scaling

- Supports **autoscaling from 0 to multiple GPUs**
- Each additional GPU **increases the billing rate**
- Handles unlimited requests within GPU capacity

## Management

- Not fully serverless — requires manual management
- **Manually delete deployments** when no longer needed
- Or configure autoscaling to **scale down to 0** during inactive periods

> [!warning]
> GPU instances bill continuously while active. Delete unused deployments or enable scale-to-zero to avoid charges.

**Cost control tips**:
- Monitor active deployments regularly
- Delete unused deployments
- Use [[070-guides-ondemand-deployments|on-demand deployments]] for intermittent workloads
- Enable autoscaling to 0 during low-demand periods

#gpu-deployment #on-demand #billing #autoscaling