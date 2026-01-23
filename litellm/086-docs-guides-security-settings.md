---
title: SSL, HTTP Proxy Security Settings | liteLLM
url: https://docs.litellm.ai/docs/guides/security_settings
source: sitemap
fetched_at: 2026-01-21T19:45:23.636755269-03:00
rendered_js: false
word_count: 323
summary: This document explains how to configure SSL and TLS settings in LiteLLM, covering custom CA bundles, verification disabling, security levels, and certificate-based authentication.
tags:
    - litellm
    - ssl-configuration
    - tls-security
    - ca-bundle
    - network-settings
    - proxy-configuration
category: configuration
---

If you're in an environment using an older TTS bundle, with an older encryption, follow this guide. By default LiteLLM uses the certifi CA bundle for SSL verification, which is compatible with most modern servers. However, if you need to disable SSL verification or use a custom CA bundle, you can do so by following the steps below.

Be aware that environmental variables take precedence over the settings in the SDK.

LiteLLM uses HTTPX for network requests, unless otherwise specified.

## 1. Custom CA Bundle[​](#1-custom-ca-bundle "Direct link to 1. Custom CA Bundle")

You can set a custom CA bundle file path using the `SSL_CERT_FILE` environmental variable or passing a string to the the ssl\_verify setting.

- SDK
- PROXY
- Environment Variables

```
import litellm
litellm.ssl_verify ="client.pem"
```

## 2. Disable SSL verification[​](#2-disable-ssl-verification "Direct link to 2. Disable SSL verification")

- SDK
- PROXY
- Environment Variables

```
import litellm
litellm.ssl_verify =False
```

## 3. Lower security settings[​](#3-lower-security-settings "Direct link to 3. Lower security settings")

The `ssl_security_level` allows setting a lower security level for SSL connections.

- SDK
- PROXY
- Environment Variables

```
import litellm
litellm.ssl_security_level ="DEFAULT@SECLEVEL=1"
```

## 4. Certificate authentication[​](#4-certificate-authentication "Direct link to 4. Certificate authentication")

The `SSL_CERTIFICATE` environmental variable or `ssl_certificate` attribute allows setting a client side certificate to authenticate the client to the server.

- SDK
- PROXY
- Environment Variables

```
import litellm
litellm.ssl_certificate ="/path/to/certificate.pem"
```

## 5. Configure ECDH Curve for SSL/TLS Performance[​](#5-configure-ecdh-curve-for-ssltls-performance "Direct link to 5. Configure ECDH Curve for SSL/TLS Performance")

The `ssl_ecdh_curve` setting allows you to configure the Elliptic Curve Diffie-Hellman (ECDH) curve used for SSL/TLS key exchange. This is particularly useful for disabling Post-Quantum Cryptography (PQC) to improve performance in environments where PQC is not required.

**Use Case:** Some OpenSSL 3.x systems enable PQC by default, which can slow down TLS handshakes. Setting the ECDH curve to `X25519` disables PQC and can significantly improve connection performance.

- SDK
- PROXY
- Environment Variables

```
import litellm
litellm.ssl_ecdh_curve ="X25519"# Disables PQC for better performance
```

**Common Valid Curves:**

- `X25519` - Modern, fast curve (recommended for disabling PQC)
- `prime256v1` - NIST P-256 curve
- `secp384r1` - NIST P-384 curve
- `secp521r1` - NIST P-521 curve

**Note:** If an invalid curve name is provided or if your Python/OpenSSL version doesn't support this feature, LiteLLM will log a warning and continue with default curves.

## 6. Use HTTP\_PROXY environment variable[​](#6-use-http_proxy-environment-variable "Direct link to 6. Use HTTP_PROXY environment variable")

Both httpx and aiohttp libraries use `urllib.request.getproxies` from environment variables. Before client initialization, you may set proxy (and optional SSL\_CERT\_FILE) by setting the environment variables:

- SDK
- PROXY

```
import litellm
litellm.aiohttp_trust_env =True
```

```
export HTTPS_PROXY='http://username:password@proxy_uri:port'
```