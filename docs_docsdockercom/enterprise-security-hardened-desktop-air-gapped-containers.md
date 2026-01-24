---
title: Air-gapped containers
url: https://docs.docker.com/enterprise/security/hardened-desktop/air-gapped-containers/
source: llms
fetched_at: 2026-01-24T14:26:31.059443219-03:00
rendered_js: false
word_count: 601
summary: This document explains how to configure air-gapped containers in Docker Desktop to restrict network access and manage traffic using proxy rules and Proxy Auto-Configuration (PAC) files.
tags:
    - docker-desktop
    - air-gapped-containers
    - network-security
    - proxy-configuration
    - pac-files
    - enterprise-security
category: configuration
---

Requires: Docker Desktop [4.29.0](https://docs.docker.com/desktop/release-notes/#4290) and later

Air-gapped containers let you restrict container network access by controlling where containers can send and receive data. This feature applies custom proxy rules to container network traffic, helping secure environments where containers shouldn't have unrestricted internet access.

Docker Desktop can configure container network traffic to accept connections, reject connections, or tunnel through HTTP or SOCKS proxies. You control which TCP ports the policy applies to and whether to use a single proxy or per-destination policies via Proxy Auto-Configuration (PAC) files.

This page provides an overview of air-gapped containers and configuration steps.

Air-gapped containers help organizations maintain security in restricted environments:

- Secure development environments: Prevent containers from accessing unauthorized external services
- Compliance requirements: Meet regulatory standards that require network isolation
- Data loss prevention: Block containers from uploading sensitive data to external services
- Supply chain security: Control which external resources containers can access during builds
- Corporate network policies: Enforce existing network security policies for containerized applications

Air-gapped containers operate by intercepting container network traffic and applying proxy rules:

1. Traffic interception: Docker Desktop intercepts all outgoing network connections from containers
2. Port filtering: Only traffic on specified ports (`transparentPorts`) is subject to proxy rules
3. Rule evaluation: PAC file rules or static proxy settings determine how to handle each connection
4. Connection handling: Traffic is allowed directly, routed through a proxy, or blocked based on the rules

Some important considerations include:

- The existing `proxy` setting continues to apply to Docker Desktop application traffic on the host
- If PAC file download fails, containers block requests to target URLs
- Hostname is available for ports 80 and 443, but only IP addresses for other ports

Before configuring air-gapped containers, you must have:

- [Enforce sign-in](https://docs.docker.com/enterprise/security/enforce-sign-in/) enabled to ensure users authenticate with your organization
- A Docker Business subscription
- Configured [Settings Management](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/) to manage organization policies
- Downloaded Docker Desktop 4.29 or later

Add the container proxy to your [`admin-settings.json` file](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-json-file/). For example:

### [Configuration parameters](#configuration-parameters)

The `containersProxy` setting controls network policies applied to container traffic:

ParameterDescriptionValue`locked`Prevents developers from overriding settings`true` (locked), `false` (default)`mode`Proxy configuration method`system` (use system proxy), `manual` (custom)`http`HTTP proxy serverURL (e.g., `"http://proxy.company.com:8080"`)`https`HTTPS proxy serverURL (e.g., `"https://proxy.company.com:8080"`)`exclude`Bypass proxy for these addressesArray of hostnames/IPs`pac`Proxy Auto-Configuration file URLURL to PAC file`transparentPorts`Ports subject to proxy rulesComma-separated ports or wildcard (`"*"`)

### [Configuration examples](#configuration-examples)

Block all external access:

Allow specific internal services:

Route through corporate proxy:

PAC files provide fine-grained control over container network access by defining rules for different destinations.

### [Basic PAC file structure](#basic-pac-file-structure)

### [General considerations](#general-considerations)

- `FindProxyForURL` function URL parameter format is http://host\_or\_ip:port or https://host\_or\_ip:port
- If you have an internal container trying to access [https://docs.docker.com/enterprise/security/hardened-desktop/air-gapped-containers](https://docs.docker.com/enterprise/security/hardened-desktop/air-gapped-containers) the docker proxy service will submit docs.docker.com for the host value and [https://docs.docker.com:443](https://docs.docker.com:443) for the url value to FindProxyForURL, if you are using `shExpMatch` function in your PAC file as follows:
  
  `shExpMatch` function will fail, instead use:

### [PAC file return values](#pac-file-return-values)

Return valueAction`PROXY host:port`Route through HTTP proxy at specified host and port`SOCKS5 host:port`Route through SOCKS5 proxy at specified host and port`DIRECT`Allow direct connection without proxy`PROXY reject.docker.internal:any_port`Block the request completely

### [Advanced PAC file example](#advanced-pac-file-example)

After applying the configuration, test that container network restrictions work:

Test blocked access:

Test allowed access:

Test proxy routing:

- Network policy enforcement: Air-gapped containers work at the Docker Desktop level. Advanced users might bypass restrictions through various means, so consider additional network-level controls for high-security environments.
- Development workflow impact: Overly restrictive policies can break legitimate development workflows. Test thoroughly and provide clear exceptions for necessary services.
- PAC file management: Host PAC files on reliable internal infrastructure. Failed PAC downloads result in blocked container network access.
- Performance considerations: Complex PAC files with many rules may impact container network performance. Keep rules simple and efficient.