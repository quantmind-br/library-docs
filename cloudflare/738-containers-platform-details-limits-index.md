---
title: Limits and Instance Types · Cloudflare Containers docs
url: https://developers.cloudflare.com/containers/platform-details/limits/index.md
source: llms
fetched_at: 2026-01-24T15:11:29.99748197-03:00
rendered_js: false
word_count: 399
summary: This document defines the available instance types and resource limits for Workers Containers, including specifications for vCPU, memory, and disk allocation.
tags:
    - instance-types
    - workers-containers
    - resource-limits
    - container-configuration
    - vcpu-specs
category: reference
---

## Instance Types

The memory, vCPU, and disk space for Containers are set through predefined instance types. Six instance types are currently available:

| Instance Type | vCPU | Memory | Disk |
| - | - | - | - |
| lite | 1/16 | 256 MiB | 2 GB |
| basic | 1/4 | 1 GiB | 4 GB |
| standard-1 | 1/2 | 4 GiB | 8 GB |
| standard-2 | 1 | 6 GiB | 12 GB |
| standard-3 | 2 | 8 GiB | 16 GB |
| standard-4 | 4 | 12 GiB | 20 GB |

These are specified using the [`instance_type` property](https://developers.cloudflare.com/workers/wrangler/configuration/#containers) in your Worker's Wrangler configuration file.

Note

The `dev` and `standard` instance types are preserved for backward compatibility and are aliases for `lite` and `standard-1`, respectively.

### Custom Instance Types

In addition to the predefined instance types, you can configure custom instance types by specifying `vcpu`, `memory_mib`, and `disk_mb` values. See the [Wrangler configuration documentation](https://developers.cloudflare.com/workers/wrangler/configuration/#custom-instance-types) for configuration details.

Custom instance types have the following constraints:

| Resource | Limit |
| - | - |
| Minimum vCPU | 1 |
| Maximum vCPU | 4 |
| Maximum Memory | 12 GiB |
| Maximum Disk | 20 GB |
| Memory to vCPU ratio | Minimum 3 GiB memory per vCPU |
| Disk to Memory ratio | Maximum 2 GB disk per 1 GiB memory |

For workloads requiring less than 1 vCPU, use the predefined instance types such as `lite` or `basic`.

Looking for larger instances? [Give us feedback here](https://developers.cloudflare.com/containers/beta-info/#feedback-wanted) and tell us what size instances you need, and what you want to use them for.

## Limits

While in open beta, the following limits are currently in effect:

| Feature | Workers Paid |
| - | - |
| GiB Memory for all concurrent live Container instances | 400GiB |
| vCPU for all concurrent live Container instances | 100 |
| TB Disk for all concurrent live Container instances | 2TB |
| Image size | Same as [instance disk space](#instance-types) |
| Total image storage per account | 50 GB [1](#user-content-fn-1) |

## Footnotes

1. Delete container images with `wrangler containers delete` to free up space. Note that if you delete a container image and then [roll back](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/rollbacks/) your Worker to a previous version, this version may no longer work. [↩](#user-content-fnref-1)