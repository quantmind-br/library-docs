---
title: Configure CI/CD
url: https://docs.docker.com/guides/golang/configure-ci-cd/
source: llms
fetched_at: 2026-01-24T14:10:21.590431643-03:00
rendered_js: false
word_count: 448
summary: This guide provides step-by-step instructions on setting up a CI/CD pipeline using GitHub Actions to automate building and pushing Docker images for a Go application to Docker Hub.
tags:
    - go
    - github-actions
    - docker-hub
    - ci-cd
    - automation
    - docker-images
category: tutorial
---

## Configure CI/CD for your Go application

## [Prerequisites](#prerequisites)

Complete the previous sections of this guide, starting with [Build your Go image](https://docs.docker.com/guides/golang/build-images/). You must have a [GitHub](https://github.com/signup) account and a verified [Docker](https://hub.docker.com/signup) account to complete this section.

## [Overview](#overview)

In this section, you'll learn how to set up and use GitHub Actions to build and push your Docker image to Docker Hub. You will complete the following steps:

1. Create a new repository on GitHub.
2. Define the GitHub Actions workflow.
3. Run the workflow.

## [Step one: Create the repository](#step-one-create-the-repository)

Create a GitHub repository, configure the Docker Hub credentials, and push your source code.

1. [Create a new repository](https://github.com/new) on GitHub.
2. Open the repository **Settings**, and go to **Secrets and variables** &gt; **Actions**.
3. Create a new **Repository variable** named `DOCKER_USERNAME` and your Docker ID as a value.
4. Create a new [Personal Access Token (PAT)](https://docs.docker.com/security/access-tokens/#create-an-access-token) for Docker Hub. You can name this token `docker-tutorial`. Make sure access permissions include Read and Write.
5. Add the PAT as a **Repository secret** in your GitHub repository, with the name `DOCKERHUB_TOKEN`.
6. In your local repository on your machine, run the following command to change the origin to the repository you just created. Make sure you change `your-username` to your GitHub username and `your-repository` to the name of the repository you created.
   
   ```
   $ git remote set-url origin https://github.com/your-username/your-repository.git
   ```
7. Run the following commands to stage, commit, and push your local repository to GitHub.
   
   ```
   $ git add -A
   $ git commit -m "my commit"
   $ git push -u origin main
   ```

## [Step two: Set up the workflow](#step-two-set-up-the-workflow)

Set up your GitHub Actions workflow for building, testing, and pushing the image to Docker Hub.

1. Go to your repository on GitHub and then select the **Actions** tab.
2. Select **set up a workflow yourself**.
   
   This takes you to a page for creating a new GitHub actions workflow file in your repository, under `.github/workflows/main.yml` by default.
3. In the editor window, copy and paste the following YAML configuration and commit the changes.
   
   ```
   name:cion:push:branches:- mainjobs:build:runs-on:ubuntu-lateststeps:- name:Login to Docker Hubuses:docker/login-action@v3with:username:${{ vars.DOCKER_USERNAME }}password:${{ secrets.DOCKERHUB_TOKEN }}- name:Set up Docker Buildxuses:docker/setup-buildx-action@v3- name:Build and pushuses:docker/build-push-action@v6with:platforms:linux/amd64,linux/arm64push:truetags:${{ vars.DOCKER_USERNAME }}/${{ github.event.repository.name }}:latest
   ```
   
   For more information about the YAML syntax for `docker/build-push-action`, refer to the [GitHub Action README](https://github.com/docker/build-push-action/blob/master/README.md).

## [Step three: Run the workflow](#step-three-run-the-workflow)

Save the workflow file and run the job.

1. Select **Commit changes...** and push the changes to the `main` branch.
   
   After pushing the commit, the workflow starts automatically.
2. Go to the **Actions** tab. It displays the workflow.
   
   Selecting the workflow shows you the breakdown of all the steps.
3. When the workflow is complete, go to your [repositories on Docker Hub](https://hub.docker.com/repositories).
   
   If you see the new repository in that list, it means the GitHub Actions successfully pushed the image to Docker Hub.

## [Summary](#summary)

In this section, you learned how to set up a GitHub Actions workflow for your application.

Related information:

- [Introduction to GitHub Actions](https://docs.docker.com/guides/gha/)
- [Docker Build GitHub Actions](https://docs.docker.com/build/ci/github-actions/)
- [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

## [Next steps](#next-steps)

Next, learn how you can locally test and debug your workloads on Kubernetes before deploying.