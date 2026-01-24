---
title: Usage
url: https://docs.docker.com/compose/bridge/usage/
source: llms
fetched_at: 2026-01-24T14:17:18.780903524-03:00
rendered_js: false
word_count: 174
summary: This document explains how Compose Bridge transforms Docker Compose configurations into Kubernetes manifests, specifically focusing on service model integration and Docker Model Runner support.
tags:
    - compose-bridge
    - kubernetes-manifests
    - docker-compose
    - docker-model-runner
    - container-deployment
    - manifest-generation
category: guide
---

Compose Bridge includes a built-in transformation that automatically converts your Compose configuration into a set of Kubernetes manifests.

If your Compose file defines a `models` section for a service, Compose Bridge automatically configures your deployment so your service can locate and use its models via Docker Model Runner.

You can optionally customize these variable names using `endpoint_var` and `model_var`.

The default transformation generates two different overlays - one for Docker Desktop whilst using a local instance of Docker Model Runner, and a `model-runner` overlay with all the relevant Kubernetes resources to deploy Docker Model Runner in a pod.

Compose looks for a `compose.yaml` file inside the current directory and generates Kubernetes manifests.

All generated files are stored in the `/out` directory in your project.

You can convert and deploy your Compose project to a Kubernetes cluster from the Compose file viewer.

Make sure you are signed in to your Docker account, navigate to your container in the **Containers** view, and in the top-right corner select **View configurations** and then **Convert and Deploy to Kubernetes**.