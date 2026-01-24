---
title: Personal settings
url: https://docs.docker.com/docker-hub/repos/settings/
source: llms
fetched_at: 2026-01-24T14:22:24.312828984-03:00
rendered_js: false
word_count: 234
summary: This document provides instructions on how to manage personal account settings for Docker Hub repositories, including default privacy visibility and autobuild email notifications.
tags:
    - docker-hub
    - repository-settings
    - privacy-settings
    - autobuilds
    - notifications
    - account-management
category: configuration
---

## Personal settings for repositories

Table of contents

* * *

For your account, you can set personal settings for repositories, including default repository privacy and autobuild notifications.

## [Default repository privacy](#default-repository-privacy)

When creating a new repository in Docker Hub, you are able to specify the repository visibility. You can also change the visibility at any time in Docker Hub.

The default setting is useful if you use the `docker push` command to push to a repository that doesn't exist yet. In this case, Docker Hub automatically creates the repository with your default repository privacy.

### [Configure default repository privacy](#configure-default-repository-privacy)

1. Sign in to [Docker Hub](https://hub.docker.com).
2. Select **My Hub** &gt; **Settings** &gt; **Default privacy**.
3. Select the **Default privacy** for any new repository created.
   
   - **Public**: All new repositories appear in Docker Hub search results and can be pulled by everyone.
   - **Private**: All new repositories don't appear in Docker Hub search results and are only accessible to you and collaborators. In addition, if the repository is created in an organization's namespace, then the repository is accessible to those with applicable roles or permissions.
4. Select **Save**.

## [Autobuild notifications](#autobuild-notifications)

You can send notifications to your email for all your repositories using autobuilds.

### [Configure autobuild notifications](#configure-autobuild-notifications)

1. Sign in to [Docker Hub](https://hub.docker.com).
2. Select **My Hub** &gt; **Repositories** &gt; **Settings** &gt; **Notifications**.
3. Select the notifications to receive by email.
   
   - **Off**: No notifications.
   - **Only failures**: Only notifications about failed builds.
   - **Everything**: Notifications for successful and failed builds.
4. Select **Save**.