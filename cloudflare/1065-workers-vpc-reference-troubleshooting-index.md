---
title: Troubleshoot and debug · Cloudflare Workers VPC
url: https://developers.cloudflare.com/workers-vpc/reference/troubleshooting/index.md
source: llms
fetched_at: 2026-01-24T15:33:44.402983173-03:00
rendered_js: false
word_count: 199
summary: Provides troubleshooting steps and recommended fixes for common connection and DNS errors encountered when using Workers VPC with Cloudflare Tunnel.
tags:
    - workers-vpc
    - troubleshooting
    - cloudflare-tunnel
    - networking
    - debugging
    - dns-resolution
category: guide
---

Troubleshoot and debug errors commonly associated with Workers VPC.

## Connection errors

Workers VPC may return errors at runtime when connecting to private services through Cloudflare Tunnel.

### Tunnel errors

| Error Message | Details | Recommended fixes |
| - | - | - |
| `Error: ProxyError: dns_error` | DNS resolution failed when attempting to connect to your private service through the tunnel. | This error may occur if your `cloudflared` version is outdated. Ensure you are running `cloudflared` version 2025.7.0 or later (latest version recommended). See [Cloudflare Tunnel update instructions](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/update-cloudflared/). |
| `Error: ProxyError: dns_error` | Cloudflare Tunnel may be configured with `http2` protocol (`TUNNEL_TRANSPORT_PROTOCOL:http2`), which works for Cloudflare Zero Trust [(see note)](https://developers.cloudflare.com/workers-vpc/configuration/tunnel/#create-and-run-tunnel-cloudflared) traffic but prevents DNS resolution from Workers VPC. | Workers VPC requires Cloudflare Tunnel to connect using the [QUIC transport protocol](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/cloudflared-parameters/run-parameters/#protocol). Ensure outbound UDP traffic on port 7844 is allowed through your firewall. |
| Requests not staying within VPC | Worker requests using `.fetch()` with a public hostname are routing out of the VPC to the hostname configured for the VPC Service. | Ensure your Worker code and the VPC Service use the internal VPC hostname for backend services, not a public hostname. |