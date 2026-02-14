---
title: Gitlab | Dokploy
url: https://docs.dokploy.com/docs/core/gitlab
source: crawler
fetched_at: 2026-02-14T14:18:19.471354-03:00
rendered_js: true
word_count: 469
summary: This document provides instructions for connecting GitLab repositories to Dokploy, including application authorization and configuring automated deployments via webhooks.
tags:
    - dokploy
    - gitlab-integration
    - automated-deployments
    - webhooks
    - ci-cd
    - version-control
category: configuration
---

Git Sources

Configure Gitlab repositories for deployments. This includes setting up access tokens, repository names, and branches.

Dokploy offer a way to connect your Gitlab Repository to your Dokploy panel, you can use Groups Names or personal accounts.

Go to `Git` and select `Gitlab` as the source, then you can use the following options:

- **Application ID**: Select the application ID that you want to connect to Dokploy.
- **Personal Secret**: Select the secret that you want to connect to Dokploy.
- **Group Name(Optional)**: Select the group name that you want to connect to Dokploy(Ideal for Gitlab Groups).

Follow the steps to connect your Gitlab account to Dokploy.

01. Go to `https://gitlab.com/-/profile/applications` and click on `Add New Application`.
02. Set Application Name: eg. `Dokploy-Gitlab-App`. choose any name that you want.
03. Redirect URI: Copy the `Redirect URI` from Dokploy. eg. `https://dokploy.com/api/providers/gitlab/callback`.
04. Select Permissions: `api`, `read_user`, `read_repository`.
05. Click on `Save Application`.
06. Copy the `Application ID` and `Secret` from Gitlab and paste it in Dokploy `Gitlab` Modal section.
07. (Optional) If you want to use Groups, go to `https://gitlab.com/dashboard/groups` enter the group name you want to connect, and look at the URL in the address bar, it will be something like this `https://gitlab.com/dokploy-panel/frontend` you can use Nested Groups and SubGroups and copy the `dokploy-panel/frontend` from Gitlab and paste it in Dokploy `Gitlab` Modal section.
08. Click on `Continue`.
09. Go Back to Dokploy and click on `Install` button.
10. Click on `Authorize`.
11. You will be redirected to the `Git` section of Dokploy.
12. Now you can use the repositories from your Gitlab Account in `Applications` or `Docker Compose` services.

Dokploy doesn't support Gitlab Automatic deployments on each push you make to your repository.

You can configure automatic deployments in Dokploy for the Following Services:

1. **Applications**
2. **Docker Compose**

The steps are the same for both services.

01. Go to either `Applications` or `Docker Compose` and go to `Deployments` Tab.
02. Copy the `Webhook URL`.
03. Go to your Gitlab Account and select the repository.
04. In the left menu, select `Settings` and then `Webhooks`.
05. Click on `Add Webhook`.
06. Set the `URL` to the one you copied in the previous step.
07. In the Trigger section, select `Push Events`.
08. Click on `Add Webhook`.
09. Click on `Save`.
10. Now you have automatic deployments enabled for the selected repository.

By default, Dokploy will automatically deploy your application on the Branch you have selected.

eg. Let's suppose you have a `application` in this way:

Repository: `my-app` Branch: `feature`

If you try to make a push on another branch eg. `main`, Dokploy will not automatically deploy your application, because your application have selected `feature` as the Branch.

In the case you want to have multiple applications in the same repository, eg. (development, staging, production), you can create 3 `Applications` in Dokploy and select the branch in each of them.

This is very usefull if you want to have multiple environments for the same application.