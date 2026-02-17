---
title: Paymenter
url: https://coolify.io/docs/services/paymenter.md
source: llms
fetched_at: 2026-02-17T14:47:03.651598-03:00
rendered_js: false
word_count: 91
summary: This document introduces Paymenter as an open-source billing platform for hosting companies and provides a step-by-step configuration guide for deploying it via Coolify.
tags:
    - paymenter
    - billing-platform
    - coolify
    - hosting-management
    - open-source
    - installation
    - server-administration
category: guide
---

## What is Paymenter?

Paymenter is an open-source billing platform tailored for hosting companies. It simplifies the management of hosting services, providing a seamless experience for both providers and customers. Built on modern web technologies, Paymenter offers a flexible and robust solution for your hosting business needs.

## How to configure Paymenter with Coolify

1. Create a new resource using the **Paymenter** service.
2. Start the resource.
3. Set the correct app URL via the terminal:

Select the Paymenter container and run the following command:

```bash
php artisan app:init
```

4. Create the first admin user:
   ```bash
   php artisan app:user:create
   ```

## Links

* [The official website](https://paymenter.org/)
* [GitHub](https://github.com/Paymenter/Paymenter)
* [Demo](https://demo.paymenter.org/)