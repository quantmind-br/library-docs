---
title: "Proxy Configuration for ForgeCode"
url: https://forgecode.dev/docs/proxy-configuration/
source: sitemap
fetched_at: 2026-04-30T14:09:16.814649196-03:00
rendered_js: false
word_count: 213
summary: "Configure ForgeCode to route API traffic through HTTP/HTTPS proxies, including authentication and certificate management."
tags:
  - proxy-configuration
  - network-settings
  - environment-variables
  - tls-certificates
  - security
  - firewall-setup
category: configuration
optimized: true
---
# Proxy Configuration for ForgeCode

> **TL;DR**
> Use `HTTP_PROXY`/`HTTPS_PROXY` to route ForgeCode traffic through a proxy.

## Environment Variables

| Variable | Protocol | Example |
|-----------|----------|---------|
| `HTTP_PROXY` | HTTP | `http://proxy.company.com:8080` |
| `HTTPS_PROXY` | HTTPS | `http://proxy.company.com:8080` |
| `NO_PROXY` | Bypass | `localhost,127.0.0.1,.internal.io` |

> **Note**: Both `HTTP_PROXY` and `HTTPS_PROXY` use HTTP proxy URLs (HTTPS is tunneled via `CONNECT`).

## Configuration Methods

### 1. Persistent (ForgeCode-only: `~/.env`)
```bash
HTTP_PROXY=http://proxy.company.com:8080
HTTPS_PROXY=http://proxy.company.com:8080
NO_PROXY=localhost,127.0.0.1,.internal.io
```

### 2. Persistent (System-wide: `~/.zshrc`/`~/.bashrc`)
```bash
export HTTP_PROXY=http://proxy.company.com:8080
export HTTPS_PROXY=http://proxy.company.com:8080
export NO_PROXY=localhost,127.0.0.1,.internal.io
```
> **Reload**: `source ~/.zshrc`

### 3. Temporary (Current Session)
```bash
export HTTP_PROXY=http://proxy.company.com:8080
```

## Authentication

### Credentials in URL
```bash
export HTTPS_PROXY=http://user:pass@proxy.company.com:8080
```
> **Security Warning**: Avoid embedding credentials in URLs (visible in logs/history). Prefer `~/.env` with `chmod 600 ~/.env`.

## TLS Inspection

### Corporate CA Certificates
If your proxy intercepts HTTPS traffic, add its CA certificate:
```toml
# ~/.forge/.forge.toml
[http]
ca_bundle = ["/path/to/corporate-ca.pem"]
```

### Disable Validation (Not Recommended)
```bash
export FORGE_HTTP_ACCEPT_INVALID_CERTS=true
```
> **Security Warning**: Only for isolated dev environments. Never use in production.

## `NO_PROXY`
- **Format**: Comma-separated list of hostnames, IPs, or domain suffixes.
- **Example**: `localhost,127.0.0.1,.internal.io`
- **Leading dot**: Matches all subdomains (e.g., `.internal.io`).

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Certificate errors | Add corporate CA to `ca_bundle` |
| Proxy auth fails | Verify credentials, use `~/.env` |
| `NO_PROXY` not working | Check syntax (commas, no spaces) |

## Flow Diagram
```plaintext
ForgeCode → [HTTPS] → Proxy → [CONNECT] → AI Provider
```

## Related
- [`.forge.toml` Reference](https://forgecode.dev/docs/forgecode-config/)