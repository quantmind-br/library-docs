---
title: How does billing work for on-demand deployments?
url: https://docs.fireworks.ai/faq-new/deployment-infrastructure/how-does-billing-work-for-on-demand-deployments
source: sitemap
fetched_at: 2026-04-27T20:13:08.028046054-03:00
rendered_js: false
word_count: 102
summary: On-demand deployments include automatic scale-to-zero autoscaling and charge only for active GPU time. Disabling scale-to-zero results in continuous charges.
tags:
    - on-demand
    - billing
    - autoscaling
    - deployment
category: faq
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
On-demand deployments include **automatic cost optimization**:

- **Default autoscaling to 0** — no replicas running when idle
- **Pay for what you use** — charged only for GPU time when replicas are active

## Best practices

1. **Leverage default autoscaling** — system scales down when not in use
2. **Don't disable scale-to-zero** — doing so results in **continuous GPU charges**
3. Consider [[084-guides-serverless-products|serverless]] for intermittent or low-frequency usage (may be more cost-effective)

> [!warning]
> Custom autoscaling configurations that prevent scale-to-zero will result in continuous GPU billing even during idle periods.

See [[070-guides-ondemand-deployments|On-demand deployments guide]] for detailed configuration.

#on-demand #billing #autoscaling #deployment