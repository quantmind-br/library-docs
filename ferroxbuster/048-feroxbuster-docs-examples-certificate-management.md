---
title: Server and Client Certificate Management
url: https://epi052.github.io/feroxbuster-docs/examples/certificate-management
source: github_pages
fetched_at: 2026-02-06T10:55:05.374481974-03:00
rendered_js: true
word_count: 161
summary: This document explains how to configure and use server and client certificates for mutual TLS (mTLS) authentication within the feroxbuster tool.
tags:
    - feroxbuster
    - mtls
    - certificates
    - authentication
    - security-configuration
    - tls
category: guide
---

## Server and Client Certificate Management

[Section titled “Server and Client Certificate Management”](#server-and-client-certificate-management)

Version 2.10.0 introduces three flags:

- `--server-certs`
- `--client-cert`
- `--client-key`

## When to use Certificate Management

[Section titled “When to use Certificate Management”](#when-to-use-certificate-management)

When a server requires mutual transport layer security (mTLS) authentication, the client upon verification of the server certificate, is required to send its own certificate to the server. The server subsequently checks its list of trusted CAs and verifies the client’s certificate.

In such a situation, the `--client-key` flag needs to be supplied a `.pem` file which has the PKCS #8 PEM encoded private key and the `--client-cert` flag must be supplied a PEM encoded certificate for the client. Additional root CA certificates may need to be supplied through `--server-certs` as a `.pem` or `.der` file if the server uses a self-signed certificate.

For example, if the server uses a root certificate called `ca-crt.pem` and the client is issued a certificate `client-crt.pem`and a key file `client-key.pem`, we will run:

```

feroxbuster --url https://localhost \
--client-key client-key.pem \
--client-cert client-crt.pem \
--server-certs ca-crt.pem
```