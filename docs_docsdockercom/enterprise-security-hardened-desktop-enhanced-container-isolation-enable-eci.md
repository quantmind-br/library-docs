---
title: Enable ECI
url: https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/enable-eci/
source: llms
fetched_at: 2026-01-24T14:26:33.837961315-03:00
rendered_js: false
word_count: 510
summary: This document provides instructions for administrators and developers on how to enable, configure, and verify Enhanced Container Isolation in Docker Desktop to improve security through user namespace mapping and restricted container runtimes.
tags:
    - docker-desktop
    - enhanced-container-isolation
    - container-security
    - administration
    - user-namespaces
    - security-hardening
category: guide
---

## Enable Enhanced Container Isolation

Subscription: Business

For: Administrators

ECI prevents malicious containers from compromising Docker Desktop while maintaining full developer productivity.

This page shows you how to turn on Enhanced Container Isolation (ECI) and verify it's working correctly.

Before you begin, you must have:

- A Docker Business subscription
- Docker Desktop 4.13 or later
- [Enforced sign-in](https://docs.docker.com/enterprise/security/enforce-sign-in/) (for administrators managing organization-wide settings only)

### [For developers](#for-developers)

Turn on ECI in your Docker Desktop settings:

1. Sign in to your organization in Docker Desktop. Your organization must have a Docker Business subscription.
2. Stop and remove all existing containers:
3. In Docker Desktop, go to **Settings** &gt; **General**.
4. Select the **Use Enhanced Container Isolation** checkbox.
5. Select **Apply and restart**.

> ECI doesn't protect containers created before turning on the feature. Remove existing containers before turning on ECI.

### [For administrators](#for-administrators)

Configure Enhanced Container Isolation organization-wide using Settings Management:

1. Sign in to [Docker Home](https://app.docker.com) and select your organization from the top-left account drop-down.
2. Go to **Admin Console** &gt; **Desktop Settings Management**.
3. [Create or edit a setting policy](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-admin-console/).
4. Set **Enhanced Container Isolation** to **Always enabled**.

<!--THE END-->

1. Create an [`admin-settings.json` file](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-json-file/) and add:
2. Configure the following as needed:
   
   - `"value": true`: Turns on ECI by default (required)
   - `"locked": true`: Prevents developers from turning off ECI
   - `"locked": false`: Allows developers to control the setting

### [Apply the configuration](#apply-the-configuration)

For ECI settings to take effect:

- New installations: Users launch Docker Desktop and sign in
- Existing installations: Users must fully quit Docker Desktop and relaunch

> Restarting from the Docker Desktop menu isn't sufficient. Users must completely quit and reopen Docker Desktop.

You can also configure [Docker socket mount permissions](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/config/) for trusted images that need Docker API access.

After turning on ECI, verify it's working correctly using these methods.

### [Check user namespace mapping](#check-user-namespace-mapping)

Run a container and examine the user namespace mapping:

With ECI turned on:

This shows the container's root user (0) maps to an unprivileged user (100000) in the Docker Desktop VM, with a range of 64K user IDs. Each container gets an exclusive user ID range for isolation.

With ECI turned off:

This shows the container root user (0) maps directly to the VM root user (0), providing less isolation.

### [Check container runtime](#check-container-runtime)

Verify the container runtime being used:

With ECI turned on, it turns `sysbox-runc`. With ECI turned off, it returns `runc`.

### [Test security restrictions](#test-security-restrictions)

Verify that ECI security restrictions are active.

Test namespace sharing:

With ECI turned on, this command fails with an error about Sysbox containers not being able to share namespaces with the host.

Test Docker socket access:

With ECI turned on, this command fails unless you've configured Docker socket exceptions for trusted images.

When administrators enforce Enhanced Container Isolation through Settings Management:

- The **Use Enhanced Container Isolation** setting appears turned on in Docker Desktop settings.
- If set to `"locked": true`, the setting is locked and greyed out.
- All new containers automatically use Linux user namespaces.
- Existing development workflows continue to work without modification.
- Users see `sysbox-runc` as the container runtime in `docker inspect` output.

<!--THE END-->

- Review [Configure Docker socket exceptions and advanced settings](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/config/).
- Review [Enhanced Container Isolation limitations](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/limitations/).