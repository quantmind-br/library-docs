---
title: Hardware requirements · Cloudflare Workers VPC
url: https://developers.cloudflare.com/workers-vpc/configuration/tunnel/hardware-requirements/index.md
source: llms
fetched_at: 2026-01-24T15:33:45.039514286-03:00
rendered_js: false
word_count: 180
summary: This document provides hardware recommendations and scaling strategies for deploying Cloudflare Tunnel in production to ensure high availability and performance.
tags:
    - cloudflare-tunnel
    - infrastructure-setup
    - scaling
    - system-requirements
    - high-availability
category: configuration
---

## Recommendations

For production use cases, we recommend the following baseline configuration:

* Run a cloudflared replica on two dedicated host machines per network location. Using two hosts enables server-side redundancy. See [tunnel availability and replicas](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/) for setup instructions.
* Size each host with minimum 4GB of RAM and 4 CPU cores.

This setup is usually sufficient to handle traffic from small-medium sized applications. The actual amount of resources used by cloudflared will depend on many variables, including the number of requests per second, bandwidth, network path, and hardware. If usage increases beyond your existing tunnel capacity, you can scale your tunnel by increasing the hardware allocated to the cloudflared hosts.

## Capacity calculator

To estimate tunnel capacity requirements for your deployment, refer to the [tunnel capacity calculator in the Zero Trust documentation](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/system-requirements/).

## Scaling considerations

Monitor tunnel performance and scale accordingly:

* **CPU utilization**: Keep below 70% average usage
* **Memory usage**: Maintain headroom for traffic spikes
* **Network bandwidth**: Ensure adequate throughput for peak loads
* **Connection count**: Scale cloudflared vertically when approaching capacity limits

## Next steps

* Configure [tunnel deployment](https://developers.cloudflare.com/workers-vpc/configuration/tunnel/)
* Set up [high availability](https://developers.cloudflare.com/workers-vpc/configuration/tunnel/) with multiple replicas