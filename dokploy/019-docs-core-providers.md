---
title: Providers | Dokploy
url: https://docs.dokploy.com/docs/core/providers
source: crawler
fetched_at: 2026-02-14T14:18:10.737029-03:00
rendered_js: true
word_count: 301
summary: This document explains how to configure and use various deployment providers in Dokploy, including Git repositories, Docker registries, and direct file uploads. It provides instructions for setting up public and private repository access using HTTPS and SSH keys.
tags:
    - dokploy
    - deployment-providers
    - git-integration
    - ssh-keys
    - docker-registry
    - private-repositories
    - automated-deployment
category: guide
---

Learn how to use providers in your application or docker compose.

Dokploy offers several deployment methods, streamlining the process whether you're utilizing GitHub, any Git provider, Docker, or automated deployments.

1. GitHub
2. Gitlab
3. Bitbucket
4. Gitea
5. Git
6. Docker (Only Applications)
7. Drag and Drop .zip (Only Applications)
8. Raw (Only Docker Compose)

<!--THE END-->

1. [Github](https://docs.dokploy.com/docs/core/github) Guide.
2. [Gitlab](https://docs.dokploy.com/docs/core/gitlab) guide.
3. [Bitbucket](https://docs.dokploy.com/docs/core/bitbucket) guide.
4. [Gitea](https://docs.dokploy.com/docs/core/gitea) guide.

For deployments from any Git repository, whether public or private, you can use either SSH or HTTPS:

### [Public Repositories (HTTPS)](#public-repositories-https)

1. Enter the repository URL in `HTTPS URL`.
2. Type the branch name.
3. Click on `Save`.

### [Private Repositories](#private-repositories)

For private repositories, is required to first create an SSH Key The Steps are almost similar for all providers.

1. Go to [SSH Keys Section](https://docs.dokploy.com/docs/core/ssh-keys) and click on `Create SSH Key`.
2. Click on `Generate RSA SSH Key` and copy the `Public Key`.
3. Go to your Git Provider, either Github, Gitlab, Bitbucket, Gitea or any other.
4. Go to `Settings` and search for `SSH Keys`.
5. Click on `Add SSH Key`.
6. Paste the SSH Key and click on `Add Key`.

You can then copy the SSH key and paste it into the settings of your account.

This is for Github, but the same applies for Gitlab, Bitbucket, Gitea, etc.

![](https://docs.dokploy.com/_next/image?url=%2Fassets%2Fprivate-repository.png&w=3840&q=75)

This enables you to pull repositories from your private repository, a method consistent across nearly all providers, remember to use the SSH URL `git@github.com:user/repo.git` and not the HTTPS URL `https://github.com/user/repo.git`.

For Docker deployments you have two options:

1. Login to your registry using the [Registry Section](https://docs.dokploy.com/docs/core/registry) and it automatically will pull the image from the registry in the case of a private registry.
2. Provide the username and password directly in the application settings.

You can upload a zip file directly from your computer and trigger a deployment.

You specify a docker compose file directly in the code editor and trigger a deployment.

Normal