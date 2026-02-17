---
title: Terminal Access
url: https://coolify.io/docs/knowledge-base/server/terminal-access.md
source: llms
fetched_at: 2026-02-17T14:41:04.352093-03:00
rendered_js: false
word_count: 220
summary: This document explains how to manage centralized terminal access for servers and containers within the Coolify dashboard, including security implications and permission requirements.
tags:
    - terminal-access
    - server-security
    - access-control
    - coolify-dashboard
    - container-management
    - system-administration
category: guide
---

# Terminal Access

The **Terminal Access** feature allows you to enable or disable terminal access for your server and all containers running on it — directly from the Coolify dashboard.

This feature provides centralized control over terminal access, enhancing security by allowing administrators to quickly restrict access when needed.

::: warning IMPORTANT
This feature is introduced in **v4.0.0-beta.419**. To follow this guide, you **must** be using v4.0.0-beta.419 or a higher version.
:::

## How to use Terminal Access

1. Go to the **Servers** section in the sidebar.
2. Select your server from the list.
3. Navigate to the **Security** tab.
4. Locate the **Terminal Access** section.
5. Click **Disable Terminal** button to disable terminal (or click **Enable Terminal** button if currently disabled)

::: warning Important
Disabling Terminal Access affects all terminals on the server and its containers. Even root and admin users will be blocked. This setting cannot be overridden per container.
:::

## Terminal Access Permissions

As of **v4.0.0-beta.452**, only the **root user** and **admin users** have permission to modify the Terminal Access setting.

When terminal access is disabled:

* No users can access terminals for the server
* No users can access terminals for any containers on that server
* This restriction applies even to root and admin users
* The restriction takes effect immediately

That's it! You now have full control over terminal access for your servers and containers.