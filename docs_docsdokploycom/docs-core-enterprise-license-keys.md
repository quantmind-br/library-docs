---
title: License Keys | Dokploy
url: https://docs.dokploy.com/docs/core/enterprise/license-keys
source: crawler
fetched_at: 2026-02-14T14:12:49.348324-03:00
rendered_js: true
word_count: 166
summary: This document explains how to activate a Dokploy Enterprise license and describes the daily server-side validation process used to verify license keys.
tags:
    - dokploy
    - enterprise-edition
    - license-activation
    - license-management
    - server-validation
category: guide
---

Activate and manage your Enterprise license

To use Enterprise features (SSO, whitelabeling, audit logs, and more), you need a valid license issued by the Dokploy team.

By default, all Dokploy instances run in the standard edition. If you are interested in switching to the Enterprise version, [contact us](https://dokploy.com/contact). Once you receive your license key, you can activate it in your instance.

1. Go to **Settings** → **License** (or **Organization** → **License** in Enterprise).
2. Enter your license key and click **Activate**.

Your instance will then have access to Enterprise features for the duration of the license.

- The license is validated **every day** against our servers to verify that it is still valid.
- The **only data** used for validation is the **IP address** of your server. We check it against our license server to confirm that the key is valid and active for that server.
- No other data is sent or stored for license validation.

If your server’s IP changes, or you have questions about your license, [contact us](https://dokploy.com/contact).