---
title: Auto Deploy | Dokploy
url: https://docs.dokploy.com/docs/core/auto-deploy
source: crawler
fetched_at: 2026-02-14T14:18:10.500419-03:00
rendered_js: true
word_count: 418
summary: This document explains how to set up automated deployments in Dokploy using webhooks from various Git providers and DockerHub, or programmatically via the Dokploy API.
tags:
    - dokploy
    - deployment-automation
    - webhooks
    - api-deployment
    - github-integration
    - dockerhub
    - ci-cd
category: guide
---

Automatically deploying your application to Dokploy can be achieved through two primary methods using Webhooks or the Dokploy API. Each method supports various platforms and provides a streamlined deployment process.

Auto deploy is only valid for the following services:

- Applications
- Docker Compose

For Github, we provide autodeploy without any configuration. This will automatically deploy your application whenever you push to your repository.

Webhooks allow you to automatically deploy your application whenever changes are made in your source repository.

- GitHub
- GitLab
- Bitbucket
- Gitea
- DockerHub (Only for Applications)

### [Configuration Steps](#configuration-steps)

1. **Enable Auto Deploy**: Toggle the 'Auto Deploy' button found in the general tab of your application settings in Dokploy.
2. **Obtain Webhook URL**: Locate the Webhook URL from the deployment logs.

<!--THE END-->

![Webhook URL](https://docs.dokploy.com/_next/image?url=%2Fassets%2Fwebhook-url.png&w=3840&q=75)

3. **Configure Your Repository**:
   
   - Navigate to your repository settings on your chosen platform.
   - Add the webhook URL provided by Dokploy.
   - Ensure the settings match the configuration necessary for triggering the webhook.

![Webhook URL](https://docs.dokploy.com/_next/image?url=%2Fassets%2Fwebhook-github.png&w=3840&q=75)

#### [Important Notes](#important-notes)

- **Branch Matching**: When using Git-based providers (GitHub, GitLab, Gitea, etc.), ensure that the branch configured in Dokploy matches the branch you intend to push to. Misalignment will result in a "Branch Not Match" error.
- **Docker Tags**: For deployments using DockerHub, ensure the tag pushed matches the one specified in Dokploy.
- The steps are the same for all the providers.

The steps are almost the same for all the Git providers, GitHub, GitLab, Bitbucket, Gitea.

To setup auto deploys for Dockerhub, follow the steps below:

1. Go to your application and select `Deployments` tab.
2. Copy the `Webhook URL`.
3. Go to your Dockerhub repository and select `Webhooks` tab.
4. Set a name for the webhook and paste the `Webhook URL` copied in step 2.
5. That's it, now every time you push to your repository, your application will trigger a deployment in dokploy.

The deployment will trigger only if the `Tag` matches the one specified in Dokploy.

Deploy your application programmatically using the Dokploy API from anywhere, this is useful when you want to trigger a deployment from a CI/CD pipeline or from a script.

### [Steps to Deploy Using API](#steps-to-deploy-using-api)

Steps:

1. **Generate a Token**: Create an API token in your profile settings on Dokploy.
2. **Retrieve Application ID**:

```
curl -X 'GET' \
  'https://your-domain/api/project.all' \
  -H 'accept: application/json' \
  -H 'x-api-key: <token>'
```

This command lists all projects and services. Identify the applicationId for the application you wish to deploy.

3. **Trigger Deployment**:

```
curl -X 'POST' \
  'https://your-domain/api/application.deploy' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'x-api-key: <token>' \
  -d '{
  "applicationId": "string"
}'
```

This API method allows for flexible, scriptable deployment options, suitable for automated systems or situations where direct repository integration is not feasible. In this way you can deploy your application from anywhere, you can use the webhook URL or the API.