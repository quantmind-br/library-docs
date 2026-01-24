---
title: Azure Pipelines and Docker
url: https://docs.docker.com/guides/azure-pipelines/
source: llms
fetched_at: 2026-01-24T14:03:21.940134656-03:00
rendered_js: false
word_count: 792
summary: This guide provides instructions for setting up a CI workflow using Azure Pipelines to build and push Docker images to Docker Hub securely. It covers configuring service connections, defining YAML pipeline stages, and implementing build best practices like SBOM and BuildKit.
tags:
    - azure-pipelines
    - docker-hub
    - ci-cd
    - containerization
    - automation
    - devops
category: guide
---

## Introduction to Azure Pipelines with Docker

> This guide is a community contribution. Docker would like to thank [Kristiyan Velkov](https://www.linkedin.com/in/kristiyan-velkov-763130b3/) for his valuable contribution.

Before you begin, ensure you have the following requirements:

- A [Docker Hub account](https://hub.docker.com) with a generated access token.
- An active [Azure DevOps project](https://dev.azure.com/) with a connected [Git repository](https://learn.microsoft.com/en-us/azure/devops/repos/git/?view=azure-devops).
- A project that includes a valid [`Dockerfile`](https://docs.docker.com/engine/reference/builder/) at its root or appropriate build context.

This guide walks you through building and pushing Docker images using [Azure Pipelines](https://azure.microsoft.com/en-us/products/devops/pipelines), enabling a streamlined and secure CI workflow for containerized applications. You’ll learn how to:

- Configure Docker authentication securely.
- Set up an automated pipeline to build and push images.

### [Step 1: Configure a Docker Hub service connection](#step-1-configure-a-docker-hub-service-connection)

To securely authenticate with Docker Hub using Azure Pipelines:

1. Navigate to **Project Settings &gt; Service Connections** in your Azure DevOps project.
2. Select **New service connection &gt; Docker Registry**.
3. Choose **Docker Hub** and provide your Docker Hub credentials or access token.
4. Give the service connection a recognizable name, such as `my-docker-registry`.
5. Grant access only to the specific pipeline(s) that require it for improved security and least privilege.

> Avoid selecting the option to grant access to all pipelines unless absolutely necessary. Always apply the principle of least privilege.

### [Step 2: Create your pipeline](#step-2-create-your-pipeline)

Add the following `azure-pipelines.yml` file to the root of your repository:

This pipeline automates the Docker image build and deployment process for the main branch. It ensures a secure and efficient workflow with best practices like caching, tagging, and conditional cleanup. Here's what it does:

- Triggers on commits and pull requests targeting the `main` branch.
- Authenticates securely with Docker Hub using an Azure DevOps service connection.
- Builds and tags the Docker image using Docker BuildKit for caching.
- Pushes both buildId and latest tags to Docker Hub.
- Logs out from Docker if running on a self-hosted Linux agent.

### [Step 1: Define pipeline triggers](#step-1-define-pipeline-triggers)

This pipeline is triggered automatically on:

- Commits pushed to the `main` branch
- Pull requests targeting `main` main branch

### [Step 2: Define common variables](#step-2-define-common-variables)

These variables ensure consistent naming, versioning, and reuse throughout the pipeline steps:

- `imageName`: your image path on Docker Hub
- `buildTag`: a unique tag for each pipeline run
- `latestTag`: a stable alias for your most recent image

> The variable `dockerUsername` is not set automatically.  
> Set it securely in your Azure DevOps pipeline variables:
> 
> 1. Go to **Pipelines &gt; Edit &gt; Variables**
> 2. Add `dockerUsername` with your Docker Hub username
> 
> Learn more: [Define and use variables in Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops&tabs=yaml%2Cbatch)

### [Step 3: Define pipeline stages and jobs](#step-3-define-pipeline-stages-and-jobs)

This stage executes only if the source branch is `main`.

### [Step 4: Job configuration](#step-4-job-configuration)

This job utilizes the latest Ubuntu VM image with Docker support, provided by Microsoft-hosted agents. It can be replaced with a custom pool for self-hosted agents if necessary.

#### [Step 4.1: Checkout code](#step-41-checkout-code)

This step pulls your repository code into the build agent, so the pipeline can access the Dockerfile and application files.

#### [Step 4.2: Authenticate to Docker Hub](#step-42-authenticate-to-docker-hub)

Uses a pre-configured Azure DevOps Docker registry service connection to authenticate securely without exposing credentials directly.

#### [Step 4.3: Build the Docker image](#step-43-build-the-docker-image)

This builds the image with:

- Two tags: one with the unique Build ID and one as latest
- Docker BuildKit enabled for faster builds and efficient layer caching
- Cache pull from the most recent pushed latest image
- Software Bill of Materials (SBOM) for supply chain transparency
- Provenance attestation to verify how and where the image was built

#### [Step 4.4: Push the Docker image](#step-44-push-the-docker-image)

By applying this condition, the pipeline builds the Docker image on every run to ensure early detection of issues, but only pushes the image to the registry when changes are merged into the main branch—keeping your Docker Hub clean and focused

This uploads both tags to Docker Hub:

- `$(buildTag)` ensures traceability per run.
- `latest` is used for most recent image references.

#### [Step 4.5 Logout of Docker (self-hosted agents)](#step-45--logout-of-docker-self-hosted-agents)

Executes docker logout at the end of the pipeline on Linux-based self-hosted agents to proactively clean up credentials and enhance security posture.

With this Azure Pipelines CI setup, you get:

- Secure Docker authentication using a built-in service connection.
- Automated image building and tagging triggered by code changes.
- Efficient builds leveraging Docker BuildKit cache.
- Safe cleanup with logout on persistent agents.
- Build images that meet modern software supply chain requirements with SBOM and attestation

<!--THE END-->

- [Azure Pipelines Documentation](https://learn.microsoft.com/en-us/azure/devops/pipelines/?view=azure-devops): Comprehensive guide to configuring and managing CI/CD pipelines in Azure DevOps.
- [Docker Task for Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/build/docker): Detailed reference for using the Docker task in Azure Pipelines to build and push images.
- [Docker Buildx Bake](https://docs.docker.com/build/bake/): Explore Docker's advanced build tool for complex, multi-stage, and multi-platform build setups. See also the [Mastering Buildx Bake Guide](https://docs.docker.com/guides/bake/) for practical examples and best practices.
- [Docker Build Cloud](https://docs.docker.com/guides/docker-build-cloud/): Learn about Docker's managed build service for faster, scalable, and multi-platform image builds in the cloud.