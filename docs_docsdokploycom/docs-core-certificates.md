---
title: Certificates | Dokploy
url: https://docs.dokploy.com/docs/core/certificates
source: crawler
fetched_at: 2026-02-14T14:18:07.099361-03:00
rendered_js: true
word_count: 205
summary: This document explains how to manage and configure SSL/TLS certificates within the Dokploy UI to secure applications and enable HTTPS via Traefik.
tags:
    - dokploy
    - ssl-certificates
    - traefik-configuration
    - https-setup
    - certificate-management
    - server-security
category: configuration
---

Configure your certificates to secure your applications.

Dokploy offers a UI to manage your certificates.

We expose a UI to create and delete the certificates, we ask two fields:

1. **Name**: Enter a name for the certificate (this can be anything you choose).
2. **Certificate Data**: Provide the certificate details.
3. **Private Key**: Enter the private key.
4. **(Optional) Server**: If you want to create a certificate for a server, you can select it here.

This action will create the files, but that doesn't mean it will work automatically. You need to adjust the Traefik configuration to use it, this configuration will make to traefik can recognize the certificate.

By default, all the domains from `traefik.me` are HTTP only, if you want to use HTTPS you need to create a certificate and use it in the domain settings.

You need to download the full [https://traefik.me/fullchain.pem](https://traefik.me/fullchain.pem) and [https://traefik.me/privkey.pem](https://traefik.me/privkey.pem), this are valid for 30 days.s

The fullchain.pem paste in the `Certificate Data` field and the privkey.pem paste in the `Private Key` field.

Now when using the traefik.me domains, make sure to enable `HTTPS` toggle and select the certificate provider set `None`

If you want to remove the certificate, just remove the certificate and in your domains settings remove the `HTTPS` toggle.