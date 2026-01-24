---
title: Circle CI
url: https://docs.docker.com/scout/integrations/ci/circle-ci/
source: llms
fetched_at: 2026-01-24T14:28:57.756616172-03:00
rendered_js: false
word_count: 119
summary: This document provides instructions for integrating Docker Scout into a CircleCI pipeline to automate image building and vulnerability scanning for critical and high-severity CVEs.
tags:
    - docker-scout
    - circleci
    - vulnerability-scanning
    - ci-cd-integration
    - container-security
    - devops
category: guide
---

## Integrate Docker Scout with Circle CI

The following examples runs when triggered in CircleCI. When triggered, it checks out the "docker/scout-demo-service:latest" image and tag and then uses Docker Scout to create a CVE report.

Add the following to a *.circleci/config.yml* file.

First, set up the rest of the workflow. Add the following to the YAML file:

```
version:2.1jobs:build:docker:- image:cimg/base:stableenvironment:IMAGE_TAG:docker/scout-demo-service:latest
```

This defines the container image the workflow uses and an environment variable for the image.

Add the following to the YAML file to define the steps for the workflow:

```
steps:# Checkout the repository files- checkout# Set up a separate Docker environment to run `docker` commands in- setup_remote_docker:version:20.10.24# Install Docker Scout and login to Docker Hub- run:name:Install Docker Scoutcommand:|        env
        curl -sSfL https://raw.githubusercontent.com/docker/scout-cli/main/install.sh | sh -s -- -b /home/circleci/bin
        echo $DOCKER_HUB_PAT | docker login -u $DOCKER_HUB_USER --password-stdin# Build the Docker image- run:name:Build Docker imagecommand:docker build -t $IMAGE_TAG .# Run Docker Scout          - run:name:Scan image for CVEscommand:|        docker-scout cves $IMAGE_TAG --exit-code --only-severity critical,high
```

This checks out the repository files and then sets up a separate Docker environment to run commands in.

It installs Docker Scout, logs into Docker Hub, builds the Docker image, and then runs Docker Scout to generate a CVE report. It only shows critical or high-severity vulnerabilities.

Finally, add a name for the workflow and the workflow's jobs:

```
workflows:build-docker-image:jobs:- build
```