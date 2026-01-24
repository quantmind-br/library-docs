---
title: Data security · Cloudflare Workers KV docs
url: https://developers.cloudflare.com/kv/reference/data-security/index.md
source: llms
fetched_at: 2026-01-24T15:16:38.612930513-03:00
rendered_js: false
word_count: 175
summary: This document outlines the security properties of Cloudflare KV, detailing its implementation of encryption-at-rest, encryption-in-transit, and adherence to industry compliance standards.
tags:
    - cloudflare-kv
    - data-security
    - encryption-at-rest
    - encryption-in-transit
    - compliance
    - aes-256
    - tls
category: concept
---

This page details the data security properties of KV, including:

* Encryption-at-rest (EAR).
* Encryption-in-transit (EIT).
* Cloudflare's compliance certifications.

## Encryption at Rest

All values stored in KV are encrypted at rest. Encryption and decryption are automatic, do not require user configuration to enable, and do not impact the effective performance of KV.

Values are only decrypted by the process executing your Worker code or responding to your API requests.

Encryption keys are managed by Cloudflare and securely stored in the same key management systems we use for managing encrypted data across Cloudflare internally.

Objects are encrypted using [AES-256](https://www.cloudflare.com/learning/ssl/what-is-encryption/), a widely tested, highly performant and industry-standard encryption algorithm. KV uses GCM (Galois/Counter Mode) as its preferred mode.

## Encryption in Transit

Data transfer between a Cloudflare Worker, and/or between nodes within the Cloudflare network and KV is secured using the same [Transport Layer Security](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) (TLS/SSL).

API access via the HTTP API or using the [wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/) command-line interface is also over TLS/SSL (HTTPS).

## Compliance

To learn more about Cloudflare's adherence to industry-standard security compliance certifications, refer to Cloudflare's [Trust Hub](https://www.cloudflare.com/trust-hub/compliance-resources/).