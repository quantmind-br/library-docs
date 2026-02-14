---
title: Others | Dokploy
url: https://docs.dokploy.com/docs/core/domains/others
source: crawler
fetched_at: 2026-02-14T14:12:57.135408-03:00
rendered_js: true
word_count: 263
summary: This guide explains how to configure custom domains from external providers for applications in Dokploy by setting up DNS A records and internal routing settings.
tags:
    - dokploy
    - domain-setup
    - dns-records
    - traefik
    - ssl-certificates
    - https
category: guide
---

This guide will cover how to configure a domain from other providers for your applications in dokploy or panel.

In the case you don't want to use Cloudflare, you can use any domain from any provider:

01. Go to your DNS Panel.
02. Go to `Records` section.
03. Click on `Add Record`.
04. Select `A` record type.
05. Enter the `Host` name, eg. `api` so it will be `api.dokploy.com`.
06. Enter the `IPv4 Address` from your server where the application is hosted eg. `1.2.3.4`.
07. Click `Save`.
08. Go to dokploy panel and now you can assign either for `Applications` or `Docker Compose`.
09. Go to `Domains` section.
10. Click `Create Domain`.
11. In the `Host` field, enter the domain name eg. `api.dokploy.com`.
12. In the `Path` field, enter the path eg. `/`.
13. In the `Container Port` field, enter the port where your application is running eg. `3000`.
14. In the `HTTPS` field enable `ON`.
15. In the `Certificate` field select `Let's Encrypt`.
16. Click `Create`.
17. A domain will be automatically assigned to your application.
18. Wait a few seconds and refresh the application.
19. You should see the application running on the domain you just created.

### [Important Clarification on Container Ports](#important-clarification-on-container-ports)

The "Container Port" specified in the domain settings is exclusively for routing traffic to the correct application container through Traefik, and does not expose the port directly to the internet. This is fundamentally different from the port settings in the "Advanced -&gt; Ports" section, which are used to directly expose application ports. The container port in the domain settings ensures that Traefik can internally direct traffic to the specified port within the container based on the domain configuration.