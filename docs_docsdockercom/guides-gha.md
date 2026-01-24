---
title: GitHub Actions and Docker
url: https://docs.docker.com/guides/gha/
source: llms
fetched_at: 2026-01-24T14:04:55.471895258-03:00
rendered_js: false
word_count: 812
---

## Introduction to GitHub Actions with Docker

This guide provides an introduction to building CI pipelines using Docker and GitHub Actions. You will learn how to use Docker's official GitHub Actions to build your application as a Docker image and push it to Docker Hub. By the end of the guide, you'll have a simple, functional GitHub Actions configuration for Docker builds. Use it as-is, or extend it further to fit your needs.

If you want to follow along with the guide, ensure you have the following:

- A verified Docker account.
- Familiarity with Dockerfiles.

This guide assumes basic knowledge of Docker concepts but provides explanations for using Docker in GitHub Actions workflows.

This guide is project-agnostic and assumes you have an application with a Dockerfile.

If you need a sample project to follow along, you can use [this sample application](https://github.com/dvdksn/rpg-name-generator.git), which includes a Dockerfile for building a containerized version of the app. Alternatively, use your own GitHub project or create a new repository from the template.

The workflow in this guide pushes the image you build to Docker Hub. To do that, you must authenticate with your Docker credentials (username and access token) as part of the GitHub Actions workflow.

For instructions on how to create a Docker access token, see [Create and manage access tokens](https://docs.docker.com/security/access-tokens/).

Once you have your Docker credentials ready, add the credentials to your GitHub repository so you can use them in GitHub Actions:

1. Open your repository's **Settings**.
2. Under **Security**, go to **Secrets and variables &gt; Actions**.
3. Under **Secrets**, create a new repository secret named `DOCKER_PASSWORD`, containing your Docker access token.
4. Next, under **Variables**, create a `DOCKER_USERNAME` repository variable containing your Docker Hub username.

GitHub Actions workflows define a series of steps to automate tasks, such as building and pushing Docker images, in response to triggers like commits or pull requests. In this guide, the workflow focuses on automating Docker builds and testing, ensuring your containerized application works correctly before publishing it.

Create a file named `docker-ci.yml` in the `.github/workflows/` directory of your repository. Start with the basic workflow configuration:

This configuration runs the workflow on pushes to the main branch and on pull requests. By including both triggers, you can ensure that the image builds correctly for a pull request before it's merged.

For the first step in your workflow, use the `docker/metadata-action` to generate metadata for your image. This action extracts information about your Git repository, such as branch names and commit SHAs, and generates image metadata such as tags and annotations.

Add the following YAML to your workflow file:

These steps prepare metadata to tag and annotate your images during the build and push process.

- The **Checkout** step clones the Git repository.
- The **Extract Docker image metadata** step extracts Git metadata and generates image tags and annotations for the Docker build.

Before you build the image, authenticate to your registry to ensure that you can push your built image to the registry.

To authenticate with Docker Hub, add the following step to your workflow:

This step uses the Docker credentials [configured in the repository settings](#configure-your-github-repository).

Finally, build the final production image and push it to your registry. The following configuration builds the image and pushes it directly to a registry.

In this configuration:

- `push: ${{ github.event_name != 'pull_request' }}` ensures that images are only pushed when the event is not a pull request. This way, the workflow builds and tests images for pull requests but only pushes images for commits to the main branch.
- `tags` and `annotations` use the outputs from the metadata action to apply consistent tags and [annotations](https://docs.docker.com/build/metadata/annotations/) to the image automatically.

SBOM (Software Bill of Materials) and provenance attestations improve security and traceability, ensuring your images meet modern software supply chain requirements.

With a small amount of additional configuration, you can configure `docker/build-push-action` to generate Software Bill of Materials (SBOM) and provenance attestations for the image, at build-time.

To generate this additional metadata, you need to make two changes to your workflow:

- Before the build step, add a step that uses `docker/setup-buildx-action`. This action configures your Docker build client with additional capabilities that the default client doesn't support.
- Then, update the **Build and push Docker image** step to also enable SBOM and provenance attestations.

Here's the updated snippet:

For more details about attestations, refer to [the documentation](https://docs.docker.com/build/metadata/attestations/).

With all the steps outlined in the previous section, here's the full workflow configuration:

This workflow implements best practices for building and pushing Docker images using GitHub Actions. This configuration can be used as-is or extended with additional features based on your project's needs, such as [multi-platform](https://docs.docker.com/build/building/multi-platform/).

### [Further reading](#further-reading)

- Learn more about advanced configurations and examples in the [Docker Build GitHub Actions](https://docs.docker.com/build/ci/github-actions/) section.
- For more complex build setups, you may want to consider [Bake](https://docs.docker.com/build/bake/). (See also the [Mastering Buildx Bake guide](https://docs.docker.com/guides/bake/).)
- Learn about Docker's managed build service, designed for faster, multi-platform builds, see [Docker Build Cloud](https://docs.docker.com/guides/docker-build-cloud/).