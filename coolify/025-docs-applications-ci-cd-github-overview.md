---
title: GitHub Integration
url: https://coolify.io/docs/applications/ci-cd/github/overview.md
source: llms
fetched_at: 2026-02-17T14:39:21.173747-03:00
rendered_js: false
word_count: 215
summary: This document outlines the various methods for integrating GitHub with Coolify to enable automated deployments from public and private repositories.
tags:
    - github-integration
    - coolify
    - ci-cd
    - github-app
    - automated-deployments
    - pull-request-previews
category: guide
---

# GitHub Integration

Coolify simplifies deploying applications from your GitHub repositories or Docker images hosted on GitHub Container Registry.

GitHub integration with Coolify supports deploying from both private and public repositories, automatic deployments on new commits, and pull request deployments.

## Ways to Use GitHub with Coolify

You can integrate GitHub with Coolify in several ways, depending on your needs. Below are the available options, each linked to a detailed guide for easy setup:

| Method | Description |
|--------|-------------|
| [Public Repository](/applications/ci-cd/github/public-repository) | Deploy applications directly using the URL of a public repository. |
| [Private Repository using GitHub App](/applications/ci-cd/github/setup-app) | Install the GitHub App on your personal account or organization to deploy both private and public repositories. |
| [Private Repository using Deploy Key](/applications/ci-cd/github/deploy-key) | Deploy applications from private repositories using a deploy key. |
| [Automatic Deployments](/applications/ci-cd/github/auto-deploy) | Automatically deploy new versions of your application when commits are pushed to a specific branch in your GitHub repository. |
| [Build and Deploy Using GitHub Actions](/applications/ci-cd/github/actions) | Build your application on GitHub using GitHub Actions as part of your CI/CD pipeline, push it to any Docker registry (such as GHCR or Docker Hub), and automatically deploy on Coolify. |
| [Preview Deployments](/applications/ci-cd/github/preview-deploy) | Automatically deploy new versions of your application based on pull requests. |