---
title: Issue certificates · Cloudflare for Platforms docs
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/issue-certificates/index.md
source: llms
fetched_at: 2026-01-24T15:10:49.967596236-03:00
rendered_js: false
word_count: 171
summary: This document explains how Cloudflare automatically issues and manages SSL/TLS certificates for custom hostnames, including details on certificate authorities and dual-certificate compatibility bundling.
tags:
    - cloudflare-for-saas
    - ssl-tls
    - custom-hostnames
    - certificate-authority
    - browser-compatibility
    - certificate-issuance
category: concept
---

Cloudflare automatically issues certificates when you [create a custom hostname](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/create-custom-hostnames/).

Note

There are several required steps before a custom hostname and its certificate can become active. For more details, refer to our [Get started guide](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/).

## Certificate authorities

If you create the custom hostname via API, you can leave the `certificate_authority` parameter empty to set it to “default CA”. With this option, Cloudflare checks the CAA records before requesting the certificates, which helps ensure the certificates can be issued from the CA.

Refer to [this certificate authorities reference page](https://developers.cloudflare.com/ssl/reference/certificate-authorities/) to learn more about the CAs that Cloudflare uses to issue SSL/TLS certificates.

## Certificate details and compatibility

For each custom hostname, Cloudflare issues two certificates bundled in chains that maximize browser compatibility (unless you [upload custom certificates](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/custom-certificates/uploading-certificates/)).

The primary certificate uses a `P-256` key, is `SHA-2/ECDSA` signed, and will be presented to browsers that support elliptic curve cryptography (ECC). The secondary or fallback certificate uses an `RSA 2048-bit` key, is `SHA-2/RSA` signed, and will be presented to browsers that do not support ECC.