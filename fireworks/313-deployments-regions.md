---
title: Regions
url: https://docs.fireworks.ai/deployments/regions
source: sitemap
fetched_at: 2026-04-27T20:18:50.067439556-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - multi-region
    - single-region
    - quotas
category: reference
word_count: 213
---
# Regions

Fireworks runs a global fleet for multi-region deployment, data residency, and elastic scaling.

## Multi-region (recommended)

By default, deployments are multi-region. Fireworks can move and spread them across regions as needed. Supported groupings: `GLOBAL`, `US`, `EUROPE`, `APAC`.

## Single region availability

Concrete locations where deployments can be pinned. Contact [inquiries@fireworks.ai](mailto:inquiries@fireworks.ai) to request single-region pinning.

| Region | Accelerator Type |
|--------|-----------------|
| `US_ARIZONA_1` | NVIDIA_H100_80GB |
| `US_CALIFORNIA_1` | NVIDIA_H200_141GB |
| `US_GEORGIA_2` | NVIDIA_B200_180GB |
| `US_GEORGIA_3` | NVIDIA_H200_141GB |
| `US_ILLINOIS_1` | NVIDIA_H100_80GB |
| `US_ILLINOIS_2` | NVIDIA_A100_80GB |
| `US_IOWA_1` | NVIDIA_H100_80GB |
| `US_OHIO_1` | NVIDIA_B200_180GB |
| `US_TEXAS_2` | NVIDIA_H100_80GB |
| `US_UTAH_1` | NVIDIA_B200_180GB |
| `US_VIRGINIA_1` | NVIDIA_H100_80GB, NVIDIA_H200_141GB |
| `US_WASHINGTON_2` | NVIDIA_H100_80GB |
| `US_WASHINGTON_3` | NVIDIA_B200_180GB |
| `US_WASHINGTON_4` | NVIDIA_B200_180GB |
| `EU_FRANKFURT_1` | NVIDIA_H100_80GB |
| `EU_ICELAND_1` | NVIDIA_H200_141GB |
| `EU_ICELAND_2` | NVIDIA_B200_180GB, NVIDIA_H200_141GB |
| `AP_TOKYO_1` | NVIDIA_H100_80GB |
| `AP_TOKYO_2` | NVIDIA_H200_141GB |

## Pin a deployment to a region

```bash
firectl deployment create accounts/fireworks/models/llama-v3p1-8b-instruct \
    --region GLOBAL
```

## Change region

Updating in-place is not supported. Create a new deployment in the desired region, then delete the old one.

## Quotas

Quota is granted at the **multi-region** level. Default new users receive `GLOBAL` quota. To request single-region quota or additional multi-region quota, contact [inquiries@fireworks.ai](mailto:inquiries@fireworks.ai).