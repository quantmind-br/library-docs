---
title: Cloudflare | Dokploy
url: https://docs.dokploy.com/docs/core/domains/cloudflare
source: crawler
fetched_at: 2026-02-14T14:12:56.184494-03:00
rendered_js: true
word_count: 967
summary: This document provides step-by-step instructions for configuring Cloudflare SSL/TLS modes and domain certificates for applications hosted on Dokploy. It explains how to set up Full (Strict) and Flexible encryption using Let's Encrypt or Cloudflare's Origin CA.
tags:
    - cloudflare
    - ssl-tls
    - dokploy
    - domain-configuration
    - certificates
    - lets-encrypt
    - origin-ca
    - dns-settings
category: guide
---

This guide will cover how to configure a Cloudflare domain for your applications in dokploy or panel.

Cloudflare has multiple SSL's Modes:

1. **Strict (SSL-Only Origin Pull)**: Enforce encryption between Cloudflare and your origin. Use this mode to guarantee connections to your origin will always be encrypted, regardless of your visitor’s request.
2. **Full (Strict)**: Enable encryption end-to-end and enforce validation on origin certificates. Use Cloudflare’s Origin CA to generate certificates for your origin.
3. **Full**: Enable encryption end-to-end. Use this mode when your origin server supports SSL certification but does not use a valid, publicly trusted certificate.
4. **Flexible**: Enable encryption only between your visitors and Cloudflare. This will avoid browser security warnings, but all connections between Cloudflare and your origin are made through HTTP.
5. **Off (not secure)**: No encryption applied. Turning off SSL disables HTTPS and causes browsers to show a warning that your website is not secure.

We will cover two of SSL modes in this guide:

- **Full (Strict)**
- **Flexible**

To switch between modes, follow these steps:

1. Go to cloudflare dashboard and then click on `Account Home` -&gt; Select the Domain you want to change.
2. On the left side, click `SSL/TLS`.
3. Click on `Overview`.
4. Click on Configure SSL/TLS Encryption.
5. Select the desired mode Full (Strict) or Flexible.
6. Click `Save`.

## [Assign a Domain Full (Strict)](#assign-a-domain-full-strict)

Follow the steps in the same order to prevent any issues.

You can create a certificate for your origin server using two methods:

- Using Let's Encrypt to generate a certificate for your origin server.
- Using Cloudflare's Origin CA to generate a certificate for your origin server.

We assume that you have enabled the `Full (Strict)` mode in the previous step, is super important to follow the steps in the same order to prevent any issues.

### [Using Let's Encrypt](#using-lets-encrypt)

01. Go to cloudflare dashboard and then click on `Account Home` -&gt; Select the Domain.
02. On the left side, click `DNS`.
03. Click on `Records`.
04. Click on `Add Record`.
05. Select `A` record type.
06. Enter the `Host` name, eg. `api` so it will be `api.dokploy.com`.
07. Enter the `IPv4 Address` from your server where the application is hosted eg. `1.2.3.4`.
08. Click `Save`.
09. Go to dokploy panel and now you can assign either for `Applications` or `Docker Compose`.
10. Go to `Domains` section.
11. Click `Create Domain`.
12. In the `Host` field, enter the domain name eg. `api.dokploy.com`.
13. In the `Path` field, enter the path eg. `/`.
14. In the `Container Port` field, enter the port where your application is running eg. `3000`.
15. In the `HTTPS` field enable `ON`.
16. In the `Certificate` field select `Let's Encrypt`.
17. Click `Create`.
18. A domain will be automatically assigned to your application.
19. Wait a few seconds and refresh the application.
20. You should see the application running on the domain you just created.

### [Using Cloudflare's Origin CA](#using-cloudflares-origin-ca)

01. Go to cloudflare dashboard and then click on `Account Home` -&gt; Select the Domain.
02. On the left side, click `SSL/TLS`.
03. Click on `Origin Server`.
04. Click on `Create Certificate`.
05. Select `Generate private key and CSR with Cloudflare`.
06. Choose the list of hostnames you want the certificate to cover eg. `api.dokploy.com`.
07. Choose the validity period eg. `15 years`.
08. Click `Create`.
09. Using the PEM format, copy the `Origin Certificate` and `Private Key` in the respective fields in the dokploy new certificate panel (Certificates &gt; Add Certificate).
10. Go to `Domains` section in your application.
11. Click `Create Domain`.
12. In the `Host` field, enter the domain name eg. `api.dokploy.com`. (Make sure that the domain is already pointing to your server IP in Cloudflare DNS settings and the **hostname matches the one in the certificate**).
13. In the `Path` field, enter the path eg. `/`.
14. In the `Container Port` field, enter the port where your application is running eg. `3000`.
15. In the `HTTPS` field enable `ON`.
16. In the `Certificate` field select `None`.
17. Click `Create`.

Using Cloudflare's Origin CA, you are sure that the certificate will be valid for the next 15 years, or the duration you selected, and you don't have to worry about failed renewals.

You can also create a certificate for wildcards domains eg. `*.dokploy.com` and use it for multiple subdomains.

**Important**: With a free Cloudflare account, this methods work only for the main domain and subdomains, not for sub-subdomains. Eg. `api.dokploy.com` works but `staging.api.dokploy.com` does not work.

## [Assign a Domain Flexible](#assign-a-domain-flexible)

We assume that you have enabled the `Flexible` mode in the previous step, is super important to follow the steps in the same order to prevent any issues.

01. Go to cloudflare dashboard and then click on `Account Home` -&gt; Select the Domain.
02. On the left side, click `DNS`.
03. Click on `Records`.
04. Click on `Add Record`.
05. Select `A` record type.
06. Enter the `Host` name, eg. `api` so it will be `api.dokploy.com`.
07. Enter the `IPv4 Address` from your server where the application is hosted eg. `1.2.3.4`.
08. Click `Save`.
09. Go to dokploy panel and now you can assign either for `Applications` or `Docker Compose`.
10. Go to `Domains` section.
11. Click `Create Domain`.
12. In the `Host` field, enter the domain name eg. `api.dokploy.com`.
13. In the `Path` field, enter the path eg. `/`.
14. In the `Container Port` field, enter the port where your application is running eg. `3000`.
15. In the `HTTPS` field enable `OFF`.
16. In the `Certificate` field select `None`.
17. Click `Create`.
18. A domain will be automatically assigned to your application.
19. Wait a few seconds and refresh the application.
20. You should see the application running on the domain you just created.

### [Important Clarification on Container Ports](#important-clarification-on-container-ports)

The "Container Port" specified in the domain settings is exclusively for routing traffic to the correct application container through Traefik, and does not expose the port directly to the internet. This is fundamentally different from the port settings in the "Advanced -&gt; Ports" section, which are used to directly expose application ports. The container port in the domain settings ensures that Traefik can internally direct traffic to the specified port within the container based on the domain configuration.