---
title: Custom SSL Certificates
url: https://coolify.io/docs/knowledge-base/proxy/traefik/custom-ssl-certs.md
source: llms
fetched_at: 2026-02-17T14:41:21.273513-03:00
rendered_js: false
word_count: 203
summary: This document provides instructions for configuring custom SSL certificates within Coolify by placing files in the proxy directory and updating Traefik's dynamic configuration.
tags:
    - coolify
    - traefik
    - ssl-certificates
    - tls-configuration
    - reverse-proxy
    - certificate-management
category: guide
---

# Custom SSL Certificates

If you want to use custom SSL certificates with Traefik, you can easily do so by following the steps below.

On each server, `/data/coolify/proxy` is mounted into the Coolify Proxy (Traefik) container.

You can add your custom SSL certificates in the `/data/coolify/proxy/certs` directory.

1. **Generate or request an SSL certificate** for your domain. It can be a
   self-signed certificate, a certificate from a public CA, or a certificate
   from Let's Encrypt.

   Read more [here](https://certbot.eff.org/instructions) about certbot and Let's Encrypt.

2. **Copy the key and cert files to the server** where your resource that will use the certificate is running.
   Use `scp` or any other method to copy the files.

   It should be placed under `/data/coolify/proxy` directory, for example:

   ```bash
   scp /path/to/your/domain.cert root@your-server-ip:/data/coolify/proxy/certs/domain.cert
   scp /path/to/your/domain.key root@your-server-ip:/data/coolify/proxy/certs/domain.key
   ```

   ::: tip Tip
   Make sure the directory `/data/coolify/proxy/certs` exists on the server.
   :::

3. You can **configure Traefik** to use the custom SSL certificates by adding a dynamic configuration file through Coolify's UI or directly adding it to `/data/coolify/proxy/dynamic`:

   ```yaml
   tls:
     certificates:
       - certFile: /traefik/certs/domain.cert
         keyFile: /traefik/certs/domain.key
       - certFile: /traefik/certs/domain2.cert
         keyFile: /traefik/certs/domain2.key
   ```

   ::: tip Tip
   `/traefik` is the directory inside `coolify-proxy` container where
   `/data/coolify/proxy` is mounted.
   :::

   Traefik will automatically use this certificate if it matches the domain of the incoming request and the certificate in any of the provided files.

For more information check Traefik's [official documentation](https://doc.traefik.io/traefik/https/tls/).